/* MaliHaus Capital, the property enquiry form.

   ONE definition, rendered into every <div data-mh-form> on the site, so
   the home page, the situations hub and all sixteen situation pages
   collect exactly the same fields in exactly the same order.

   Reads its configuration from window.MALIHAUS (site.js). site.js must
   load first.

   The lead destination is GoHighLevel. No endpoint, account id, API key
   or webhook URL has been supplied, so none is invented here. Until
   MALIHAUS.leadEndpoint is filled in, a submission validates, records
   consent with its timestamp and page, keeps the whole payload and goes
   to the confirmation page, and the payload is pushed to dataLayer so
   the lead is not lost. */

(function () {
  'use strict';

  var CFG = window.MALIHAUS || {};
  var mounts = document.querySelectorAll('[data-mh-form]');
  if (!mounts.length) return;

  /* ------------------------------------------------------------------ *
   * Field definitions
   * ------------------------------------------------------------------ */

  var STATES = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA',
    'KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND',
    'OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'];

  var REQUIRED = [
    { n: 'first_name',      l: 'First name',            t: 'text',  ac: 'given-name',      w: 'half' },
    { n: 'last_name',       l: 'Last name',             t: 'text',  ac: 'family-name',     w: 'half' },
    { n: 'phone',           l: 'Telephone number',      t: 'tel',   ac: 'tel',             w: 'half' },
    { n: 'email',           l: 'Email address',         t: 'email', ac: 'email',           w: 'half' },
    { n: 'property_address',l: 'Property street address',t: 'text', ac: 'street-address',  w: 'full' },
    { n: 'city',            l: 'City',                  t: 'text',  ac: 'address-level2',  w: 'half' },
    { n: 'state',           l: 'State',                 t: 'select',ac: 'address-level1',  w: 'quarter',
      o: STATES },
    { n: 'zip',             l: 'ZIP code',              t: 'text',  ac: 'postal-code',     w: 'quarter',
      pattern: '[0-9]{5}(-[0-9]{4})?', inputmode: 'numeric' },
    { n: 'property_type',   l: 'Property type',         t: 'select', w: 'half',
      o: ['Single family home','Townhouse','Condominium','Duplex or multi family','Mobile or manufactured home','Vacant land','Other'] },
    { n: 'occupancy',       l: 'Occupancy status',      t: 'select', w: 'half',
      o: ['I live there','Vacant','Tenant occupied','Family member lives there','Used as a short term rental'] },
    { n: 'condition',       l: 'Property condition',    t: 'select', w: 'half',
      o: ['Good, little or nothing needed','Dated but sound','Needs significant repair','Major damage','I am not sure'] },
    { n: 'reason',          l: 'Reason for selling',    t: 'select', w: 'half',
      o: ['Need to sell quickly','Inherited property or probate','Behind on payments or foreclosure',
          'Tired of being a landlord','Property needs major repairs','Vacant property',
          'I own it from out of state','The listing expired','Fire, water or storm damage',
          'Divorce or separation','Relocating','Taxes, liens or code violations',
          'Property needs a major cleanout','Title or multiple owner problems',
          'Downsizing or a senior move','Financial hardship','Something else'] },
    { n: 'timeline',        l: 'Preferred selling timeline', t: 'select', w: 'half',
      o: ['As soon as possible','Within 30 days','1 to 3 months','3 to 6 months','Just exploring options'] },
    { n: 'contact_method',  l: 'Preferred contact method',   t: 'select', w: 'half',
      o: ['Telephone call','Text message','Email'] }
  ];

  var OPTIONAL = [
    { n: 'price_expectation', l: 'Price expectation', t: 'text',  w: 'half',
      ph: 'Optional' },
    { n: 'callback_time',     l: 'Preferred callback time', t: 'select', w: 'half',
      o: ['Morning','Afternoon','Evening','Any time'] },
    { n: 'notes',             l: 'Anything else we should know', t: 'textarea', w: 'full',
      ph: 'Optional. Tell us anything that would help us understand the property or the situation.' }
  ];

  /* Hidden attribution. Values are filled from the session, so a visitor
     who arrived from an ad three pages ago still carries their source. */
  var HIDDEN = ['lead_source','campaign','landing_page_url','referring_url','utm_source','utm_medium',
    'utm_campaign','utm_content','utm_term','situation_page','location_page','market',
    'submitted_at','consent_at','consent_given','consent_page'];

  /* ------------------------------------------------------------------ *
   * Rendering
   * ------------------------------------------------------------------ */

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function field(f, id, required) {
    var fid = id + '-' + f.n;
    var req = required ? ' required aria-required="true"' : '';
    var mark = required ? ' <span class="mh-req" aria-hidden="true">*</span>' : '';
    var h = '<div class="mh-f mh-' + f.w + '">';
    h += '<label for="' + fid + '">' + esc(f.l) + mark + '</label>';

    if (f.t === 'select') {
      h += '<select id="' + fid + '" name="' + f.n + '"' + req +
           (f.ac ? ' autocomplete="' + f.ac + '"' : '') + '>';
      h += '<option value="">Please choose</option>';
      for (var i = 0; i < f.o.length; i++) {
        h += '<option value="' + esc(f.o[i]) + '">' + esc(f.o[i]) + '</option>';
      }
      h += '</select>';
    } else if (f.t === 'textarea') {
      h += '<textarea id="' + fid + '" name="' + f.n + '" rows="4"' + req +
           (f.ph ? ' placeholder="' + esc(f.ph) + '"' : '') + '></textarea>';
    } else {
      h += '<input type="' + f.t + '" id="' + fid + '" name="' + f.n + '"' + req +
           (f.ac ? ' autocomplete="' + f.ac + '"' : '') +
           (f.pattern ? ' pattern="' + f.pattern + '"' : '') +
           (f.inputmode ? ' inputmode="' + f.inputmode + '"' : '') +
           (f.ph ? ' placeholder="' + esc(f.ph) + '"' : '') + '>';
    }

    h += '<span class="mh-err" id="' + fid + '-err" role="alert"></span>';
    h += '</div>';
    return h;
  }

  function render(mount, index) {
    var id = 'mhf' + index;
    var situation = mount.getAttribute('data-situation') || '';
    var market = mount.getAttribute('data-market') || '';
    var heading = mount.getAttribute('data-heading') || 'Tell us about your property';
    var intro = mount.getAttribute('data-intro') ||
      'The more you can tell us, the more useful our answer will be. Nothing here commits you to selling.';

    var h = '';
    h += '<form class="mh-form" id="' + id + '" novalidate data-mh-enquiry data-situation="' +
         esc(situation) + '" data-market="' + esc(market) + '">';
    h += '<h2 class="mh-form-h">' + esc(heading) + '</h2>';
    h += '<p class="mh-form-intro">' + esc(intro) + '</p>';

    h += '<fieldset><legend>About you</legend><div class="mh-grid">';
    h += field(REQUIRED[0], id, true) + field(REQUIRED[1], id, true) +
         field(REQUIRED[2], id, true) + field(REQUIRED[3], id, true);
    h += '</div></fieldset>';

    h += '<fieldset><legend>The property</legend><div class="mh-grid">';
    for (var i = 4; i < 12; i++) h += field(REQUIRED[i], id, true);
    h += '</div></fieldset>';

    h += '<fieldset><legend>Your timeline</legend><div class="mh-grid">';
    h += field(REQUIRED[12], id, true) + field(REQUIRED[13], id, true);
    for (var j = 0; j < OPTIONAL.length; j++) h += field(OPTIONAL[j], id, false);
    h += '</div></fieldset>';

    /* Hidden attribution fields. */
    for (var k = 0; k < HIDDEN.length; k++) {
      h += '<input type="hidden" name="' + HIDDEN[k] + '" value="">';
    }

    /* Consent. The checkbox is never preselected. */
    h += '<div class="mh-consent">';
    h += '<div class="mh-check">';
    h += '<input type="checkbox" id="' + id + '-consent" name="consent" required aria-required="true">';
    h += '<label for="' + id + '-consent">' + consentLabelHtml() + '</label>';
    h += '</div>';
    h += '<span class="mh-err" id="' + id + '-consent-err" role="alert"></span>';
    h += '<p class="mh-disclosure">' + esc(CFG.consentDisclosure || '') + '</p>';
    h += '</div>';

    h += '<div class="mh-submit">';
    h += '<button type="submit" class="btn solid">Tell Us About Your Property</button>';
    h += '<span class="mh-or">or call <a data-call data-loc="form" href="#"><span data-phone></span></a></span>';
    h += '</div>';
    h += '<p class="mh-formstatus" role="status"></p>';
    h += '</form>';

    mount.innerHTML = h;
  }

  /* The checkbox label is the approved wording with the two documents
     linked, exactly as it reads. */
  function consentLabelHtml() {
    var text = esc(CFG.consentCheckboxLabel || '');
    var priv = CFG.privacyUrl, terms = CFG.termsUrl;
    if (terms) {
      text = text.replace('Terms &amp; Conditions',
        '<a href="' + esc(terms) + '" target="_blank" rel="noopener">Terms &amp; Conditions</a>');
    }
    if (priv) {
      text = text.replace('Privacy Policy',
        '<a href="' + esc(priv) + '" target="_blank" rel="noopener">Privacy Policy</a>');
    }
    return text;
  }

  /* ------------------------------------------------------------------ *
   * Attribution, validation and submission
   * ------------------------------------------------------------------ */

  function fillHidden(form) {
    var a = {};
    try { a = JSON.parse(sessionStorage.getItem('mh_attr') || '{}'); } catch (e) { a = {}; }

    function set(name, value) {
      var el = form.querySelector('[name="' + name + '"]');
      if (el && !el.value) el.value = value || '';
    }

    set('lead_source', a.utm_source || 'direct');
    set('campaign', a.utm_campaign || '');
    set('landing_page_url', a.landing_page ? location.origin + a.landing_page : location.href);
    set('referring_url', document.referrer || '');
    set('utm_source', a.utm_source || '');
    set('utm_medium', a.utm_medium || '');
    set('utm_campaign', a.utm_campaign || '');
    set('utm_content', a.utm_content || '');
    set('utm_term', a.utm_term || '');
    set('situation_page', form.getAttribute('data-situation') || '');

    /* The market travels with the lead so GHL and REsimpli can tell which
       market generated the enquiry. */
    var mk = form.getAttribute('data-market') || '';
    set('location_page', mk);
    set('market', mk);
  }

  function labelOf(el) {
    var l = el.form ? el.form.querySelector('label[for="' + el.id + '"]') : null;
    return l ? l.textContent.replace('*', '').trim() : 'This field';
  }

  function validate(form) {
    var bad = null;
    var els = form.querySelectorAll('input[required],select[required],textarea[required]');

    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      var err = form.querySelector('#' + el.id + '-err');
      var msg = '';

      if (el.type === 'checkbox') {
        if (!el.checked) msg = 'Please tick this box so we are allowed to contact you.';
      } else if (!el.value.trim()) {
        msg = labelOf(el) + ' is needed.';
      } else if (el.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(el.value)) {
        msg = 'That email address does not look right.';
      } else if (el.type === 'tel' && el.value.replace(/\D/g, '').length < 10) {
        msg = 'Please give a telephone number with at least ten digits.';
      } else if (el.pattern && !new RegExp('^(?:' + el.pattern + ')$').test(el.value.trim())) {
        msg = labelOf(el) + ' does not look right.';
      }

      el.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (err) err.textContent = msg;
      if (msg && !bad) bad = el;
    }
    return bad;
  }

  function payloadOf(form) {
    var out = {};
    var els = form.elements;
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (!el.name) continue;
      out[el.name] = el.type === 'checkbox' ? (el.checked ? 'yes' : 'no') : el.value;
    }
    return out;
  }

  function wire(form) {
    /* Clear an error the moment the visitor fixes it. */
    form.addEventListener('input', function (ev) {
      var el = ev.target;
      if (el.getAttribute('aria-invalid') !== 'true') return;
      var err = form.querySelector('#' + el.id + '-err');
      if (err) err.textContent = '';
      el.setAttribute('aria-invalid', 'false');
    });
    form.addEventListener('change', function (ev) {
      if (ev.target.type !== 'checkbox') return;
      var err = form.querySelector('#' + ev.target.id + '-err');
      if (err && ev.target.checked) err.textContent = '';
    });

    var started = false;
    form.addEventListener('input', function () {
      if (started) return;
      started = true;
      if (window.mhTrack) window.mhTrack('form_start', { form_name: 'property_enquiry' });
    });

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var status = form.querySelector('.mh-formstatus');

      fillHidden(form);
      var bad = validate(form);
      if (bad) {
        status.textContent = 'Please check the highlighted answers.';
        status.className = 'mh-formstatus bad';
        bad.focus();
        return;
      }

      /* Record consent with its timestamp and the page it was given on. */
      var now = new Date().toISOString();
      form.querySelector('[name="submitted_at"]').value = now;
      form.querySelector('[name="consent_at"]').value = now;
      form.querySelector('[name="consent_given"]').value = 'yes';
      form.querySelector('[name="consent_page"]').value = location.href;

      var payload = payloadOf(form);

      /* Nothing is lost even before the endpoint exists. */
      if (window.mhTrack) window.mhTrack('property_enquiry_submit', {
        form_name: 'property_enquiry',
        situation: payload.situation_page || 'none',
        market: payload.market || 'none',
        lead: payload
      });
      try { sessionStorage.setItem('mh_last_lead', JSON.stringify(payload)); } catch (e) {}

      status.className = 'mh-formstatus';
      status.textContent = 'Sending your details…';

      var done = function () {
        var q = new URLSearchParams();
        if (payload.first_name) q.set('n', payload.first_name);
        location.href = confirmUrl() + (q.toString() ? '?' + q.toString() : '');
      };

      if (!CFG.leadEndpoint) { done(); return; }

      fetch(CFG.leadEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      }).then(done).catch(function () {
        status.className = 'mh-formstatus bad';
        status.textContent = 'That did not go through. Please call ' +
          (CFG.phoneDisplay || '') + ' and we will take the details over the phone.';
      });
    });
  }

  /* The confirmation page lives at the site root, so the site root has to be
     found from wherever the form was submitted: the home page, /situations/,
     /situations/<slug>/, /locations/ or /locations/<slug>/. The canonical URL
     is the reliable anchor because every page carries one. */
  function confirmUrl() {
    var base = document.querySelector('link[rel="canonical"]');
    var href = base ? base.getAttribute('href') : location.href;

    /* Cut everything from the first section segment onwards. */
    var root = href.replace(/\/(situations|locations)\/.*$/, '');

    /* On the home page there is no section segment, so drop the file name. */
    root = root.replace(/\/[^\/]*\.html$/, '').replace(/\/+$/, '');

    return root + '/thank-you.html';
  }

  for (var m = 0; m < mounts.length; m++) {
    render(mounts[m], m);
    wire(mounts[m].querySelector('form'));
  }

  /* site.js already ran, so re-apply the number to the buttons we just made. */
  if (CFG.phoneDisplay) {
    var tel = 'tel:+1' + CFG.phoneDigits;
    var calls = document.querySelectorAll('.mh-form [data-call]');
    for (var c = 0; c < calls.length; c++) {
      calls[c].setAttribute('href', tel);
      calls[c].setAttribute('aria-label', 'Call MaliHaus on ' + CFG.phoneDisplay);
    }
    var nums = document.querySelectorAll('.mh-form [data-phone]');
    for (var p = 0; p < nums.length; p++) nums[p].textContent = CFG.phoneDisplay;
  }
})();
