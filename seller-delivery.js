/* Native HighLevel external-form capture. No private API credentials.
 * HighLevel's SDK swallows delivery failures. Observe ONLY our form's actual
 * transport acknowledgement; never interpret SDK completion as delivery.
 * Transport observation fails closed if the vendor changes its protocol.
 */
(function () {
  'use strict';
  var TRACKING_ID = 'tk_847f0db77c7948389132ba8dce6490a7';
  var FORM_ID = 'malihaus-seller-enquiry';
  var sending;
  var originalFetch = window.fetch;
  var acknowledge;
  var nativeDelivery = false;
  // Capture before the vendor: Enter/requestSubmit cannot bypass validation
  // or create another submission after an uncertain network result.
  document.addEventListener('submit', function (event) {
    if (event.target.id !== FORM_ID) return;
    event.preventDefault();
    if (nativeDelivery) return;
    event.stopImmediatePropagation();
    if (!sending && window.MHF) window.MHF.submit();
  }, true);
  window.fetch = function (url, options) {
    var event;
    try {
      if (String(url) === 'https://backend.leadconnectorhq.com/external-tracking/events') {
        event = JSON.parse(options.body);
      }
    } catch (ignore) {}
    var ours = event && event.type === 'external_form_submission' &&
      event.trackingId === TRACKING_ID && event.formId === FORM_ID;
    return originalFetch.apply(this, arguments).then(function (response) {
      if (ours && response.ok) {
        response.clone().json().then(function (body) {
          if (body.status === 'ok' && acknowledge) acknowledge();
        }).catch(function () {});
      }
      return response;
    });
  };

  function field(form, name, label, value) {
    if (value == null || value === '') return;
    var wrap = document.createElement('label');
    wrap.textContent = label;
    var input = document.createElement('textarea');
    input.name = name;
    input.readOnly = true;
    input.value = String(value);
    input.rows = name === 'conversation_summary' ? 5 : 2;
    wrap.appendChild(input);
    form.appendChild(wrap);
  }

  function send(lead, answers) {
    if (sending) return sending;
    var form = document.getElementById(FORM_ID);
    if (!form) return Promise.reject(new Error('Online delivery is unavailable.'));
    // Own the validated snapshot before any asynchronous work. The SDK reads
    // live controls; readonly keeps text in its payload, unlike disabled.
    lead = JSON.parse(JSON.stringify(lead));
    answers = JSON.parse(JSON.stringify(answers));
    var snapshot = Array.from(form.querySelectorAll('input,textarea')).map(function(input){
      input.readOnly = true;
      if (input.type === 'checkbox') input.disabled = true;
      return {input:input, value:input.value, checked:input.checked};
    });
    form.querySelectorAll('button').forEach(function(button){button.disabled=true;});
    var fingerprint = JSON.stringify([lead.contact, lead.situations, answers, lead.notes]);
    sending = crypto.subtle.digest('SHA-256', new TextEncoder().encode(fingerprint)).then(function (bytes) {
      var key = 'mh_seller_' + Array.from(new Uint8Array(bytes)).map(function(b){return b.toString(16).padStart(2,'0');}).join('');
      function remember(status) {
        try { sessionStorage.setItem(key, JSON.stringify({status:status,at:Date.now()})); } catch(ignore) {}
      }
      var previous;
      try { previous = JSON.parse(sessionStorage.getItem(key)); } catch(ignore) {}
      if (previous && Date.now() - previous.at < 86400000) {
        if (previous.status === 'delivered') return;
        throw new Error('An identical enquiry is already awaiting confirmation. Please do not submit again.');
      }
      remember('pending');
      return new Promise(function (resolve, reject) {
      var form = document.getElementById(FORM_ID);
      if (!form) { reject(new Error('Online delivery is unavailable.')); return; }
      var details = document.createElement('details');
      details.open = true;
      details.className = 'mhf-delivery-review';
      var title = document.createElement('summary');
      title.textContent = 'Your enquiry details';
      details.appendChild(title);
      form.appendChild(details);
      var c = lead.contact;
      [
        ['state','State',c.state],
        ['property_type','Property Type',c.propertyType],
        ['property_ownership','Property Ownership',answers.title],
        ['occupancy_status','Occupancy Status',answers.occupancy || answers.tenants],
        ['price_expectation_optional','Price Expectation (Optional)',c.priceExpectation],
        ['preferred_callback_time','Preferred Callback Time',c.bestTime],
        ['preferred_contact_method','Preferred Contact Method',c.contactPreference],
        ['phonetext_contact_permission','Phone/Text Contact Permission',c.phone ? 'Consent given: '+lead.consent.at : 'No phone provided; email only'],
        ['human_followup_requested','Human Follow-Up Requested','Yes'],
        ['reason_for_considering_a_sale','Reason for Considering a Sale',lead.situations.join(', ')],
        ['property_condition','Property Condition',answers.issue],
        ['desired_selling_timeframe','Desired Selling Timeframe',answers.timeline || answers.dateset],
        ['important_circumstances__notes','Important Circumstances / Notes',lead.notes],
        ['conversation_summary','Conversation Summary',lead.summary+'\n\n'+lead.answers.map(function(a){return a.q+': '+a.a;}).join('\n')+'\n\nConsent: '+JSON.stringify(lead.consent)+'\nAttribution: '+JSON.stringify(lead.attribution)],
        ['lead_source','Lead Source',lead.leadSource],
        ['lead_tier','Lead Tier',lead.leadTier]
      ].forEach(function(f){ field(details, f[0], f[1], f[2]); });
      var button = document.getElementById('mhf-send');
      button.disabled = true;
      button.textContent = 'Sending your enquiry…';
      var attempt = 'loading';
      function notSent() {
        if (attempt !== 'loading') return;
        attempt = 'not-sent';
        clearTimeout(timer); acknowledge = null;
        try { sessionStorage.removeItem(key); } catch(ignore) {}
        button.textContent = 'Online delivery unavailable — please call';
        reject(new Error('Online delivery is unavailable. Your enquiry has not been sent.'));
      }
      var timer = setTimeout(function () {
        if (attempt === 'loading') { notSent(); return; }
        if (attempt !== 'dispatched') return;
        attempt = 'unconfirmed';
        acknowledge = null;
        button.textContent = 'Delivery unconfirmed — please call';
        reject(new Error('We could not confirm delivery. Your details may have arrived; please do not submit again.'));
      }, 30000);
      acknowledge = function () {
        if (attempt !== 'dispatched') return;
        attempt = 'delivered';
        clearTimeout(timer);
        acknowledge = null;
        remember('delivered');
        resolve();
      };
      var script = document.createElement('script');
      script.src = 'https://link.msgsndr.com/js/external-tracking.js';
      script.dataset.trackingId = TRACKING_ID;
      script.onload = function () {
        if (attempt !== 'loading') return;
        // No submit-type button: the vendor also captures clicks before validation.
        // Only this already-validated native submit is allowed to reach the SDK.
        snapshot.forEach(function(saved){
          saved.input.value = saved.value;
          saved.input.checked = saved.checked;
        });
        attempt = 'dispatched';
        nativeDelivery = true;
        try {
          form.dispatchEvent(new Event('submit', {bubbles:true, cancelable:true}));
        } finally {
          nativeDelivery = false;
        }
      };
      script.onerror = notSent;
      document.body.appendChild(script);
      });
    });
    return sending;
  }
  window.MHSellerDelivery = {send:send};
})();
