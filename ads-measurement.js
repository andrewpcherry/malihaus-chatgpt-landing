(function () {
  'use strict';
  var allowed = false, started = false, sent = {}, banner;
  var privacySignal = typeof navigator !== 'undefined' && navigator.globalPrivacyControl === true;
  var production = location.hostname === 'getoffer.malihaus.com';
  function measure(name, data, id) {
    try {
      if (!allowed || !production || !window.oaiq || (id && sent[id])) return;
      window.oaiq('measure', name, data, { opt_out: true, event_id: id });
      if (id) sent[id] = true;
    } catch (_) {}
  }
  function start() {
    if (started || !production) return;
    started = true;
    try {
      if (!window.oaiq) {
        var q = function () { q.q.push(arguments); }; q.q = []; window.oaiq = q;
        var script = document.createElement('script'); script.async = true;
        script.src = 'https://bzrcdn.openai.com/sdk/oaiq.min.js'; document.head.appendChild(script);
      }
      window.oaiq('consent', true);
      window.oaiq('init', { pixelId: 'K2kNqc2FLNKXtz2mAmaTSh' });
      measure('page_viewed', { type: 'contents' });
    } catch (_) {}
  }
  function choose(value) {
    value = value && !privacySignal;
    allowed = value;
    try { localStorage.setItem('mh_ads_consent', value ? 'allow' : 'deny'); } catch (_) {}
    try { if (window.oaiq) window.oaiq('consent', value); } catch (_) {}
    if (banner) banner.remove();
    if (value) start();
  }
  window.MHAds = {
    leadCreated: function (submissionId) {
      measure('lead_created', { type: 'customer_action' }, 'mh-lead-' + submissionId);
    },
    preferences: function () {
      if (banner && banner.isConnected) return;
      banner = document.createElement('section'); banner.setAttribute('aria-label', 'Advertising measurement choice');
      banner.style.cssText = 'position:fixed;bottom:16px;left:16px;right:16px;z-index:10000;max-width:580px;padding:20px;border:1px solid #b78c59;background:#171d25;color:#fff;border-radius:12px;box-shadow:0 6px 30px #0008;font:16px/1.5 sans-serif';
      banner.innerHTML = '<p style="margin:0 0 12px">Allow advertising measurement? Mali Haus uses the OpenAI Ads Pixel to measure visits and successful enquiries. Matching may use hashed contact information. Your choice does not affect your enquiry. <a href="/privacy-policy/" style="color:#e8c28e">Privacy policy</a></p><button type="button" data-choice="allow">Allow measurement</button> <button type="button" data-choice="deny">Decline</button>';
      if (privacySignal) banner.innerHTML = banner.innerHTML.replace('Allow advertising measurement?', 'Your browser privacy signal disables advertising measurement.');
      banner.querySelector('[data-choice="allow"]').disabled = privacySignal;
      banner.querySelector('[data-choice="allow"]').onclick = function () { choose(true); };
      banner.querySelector('[data-choice="deny"]').onclick = function () { choose(false); };
      document.body.appendChild(banner);
    }
  };
  var choice; try { choice = localStorage.getItem('mh_ads_consent'); } catch (_) {}
  if (privacySignal) { choose(false); }
  else if (choice === 'allow') { allowed = true; start(); }
  else if (choice !== 'deny') window.MHAds.preferences();
  var preferences = document.createElement('button'); preferences.type = 'button';
  preferences.textContent = 'Advertising privacy choices'; preferences.onclick = window.MHAds.preferences;
  preferences.style.cssText = 'margin:12px;padding:8px 12px';
  (document.querySelector('footer') || document.body).appendChild(preferences);
})();
