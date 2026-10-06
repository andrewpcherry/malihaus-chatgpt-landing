/* MaliHaus Capital, shared site layer
   Covers proposal section 03 items 02 (measurement), 03 (call tracking foundation)
   and 11 (conversion event tracking).

   EVERYTHING CONFIGURABLE LIVES IN ONE PLACE: the CONFIG block below.
   Change the phone number here and it changes on every page, every button,
   the mobile call bar, the footer and the structured data. */

(function () {
  'use strict';

  var CONFIG = {
    /* ---- The approved telephone number. ONE PLACE. ----
       Approved by Michael Mali and confirmed in the 2026-09-03 build brief.
       Every header, mobile menu, call button, contact section, form,
       confirmation page, footer, structured data block and accessibility
       label on this site is driven from these two values and nothing else.
       digits: 10 digits, no punctuation. display: exactly how it should read. */
    phoneDigits: '4079173347',
    phoneDisplay: '407-917-3347',

    /* ---- Measurement foundation ----
       Put the real GTM container ID here and the container loads on every page.
       Left empty the site runs normally and events queue into dataLayer,
       so nothing breaks and nothing is lost before the container exists. */
    gtmId: '',

    /* Seller qualification path */
    /* The funnel now lives inside this site at /get-offer/. The old
       standalone at /malihaus-funnel/ is superseded. Path is resolved
       against the site root at runtime, so it works from any depth. */
    funnelPath: './',
    funnelHash: '#start',

    /* ---- Lead destination ----
       GoHighLevel captures the website visitor and hands the completed lead
       to REsimpli through the separately configured integration.
       NO endpoint has been supplied, so nothing is invented here. While this
       is empty the form validates, records consent, keeps the full payload
       and routes to the confirmation page, and the payload is pushed to
       dataLayer so nothing is lost. Paste the real endpoint here to go live. */
    leadEndpoint: '',

    /* ---- Chat: the GHL Conversation AI widget ----
       Paste the official script URL supplied from the GHL sub account.
       While it is empty the concept receptionist on the home page runs
       instead. When it is set, the GHL widget loads on every page and the
       concept widget stands down so the two never overlap. */
    ghlWidgetSrc: '',
    ghlWidgetAttrs: {
      'data-resources-url': 'https://widgets.leadconnectorhq.com/chat-widget/loader.js',
      'data-widget-id': '6a9995f77e179c4b66653b9f'
    },

    /* ---- Legal links ----
       Both verified live on malihaus.com, 2026-09-03. */
    privacyUrl: new URL('./privacy-policy/', location.href).href,
    termsUrl: new URL('./terms-of-use/', location.href).href,

    /* ---- A2P consent ----
       Michael's approved wording, used verbatim. Do not reword it.
       The HELP number inside it is the A2P REGISTERED number and is
       deliberately NOT the public website number above. It stays at
       (321) 655-2099 unless Michael, Rocky or the REsimpli team
       confirms in writing that it should change. Never swap it
       automatically for the public number. */
    consentCheckboxLabel: 'I agree to the Terms & Conditions and Privacy Policy.',
    consentDisclosure: 'I request a response about my property enquiry using the contact details I provide. Marketing permission is optional.',
    marketingConsentDisclosure: 'I agree to receive marketing calls and text messages, including calls using automated technology or an artificial or prerecorded voice, at the phone number I provide, from MaliHaus, a brand of Real Estate RE Marketing Inc. Consent is not a condition of purchasing any property, goods or services. Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe or HELP for help at (321) 655-2099. We will not share or sell mobile data to third parties for promotional or marketing purposes.',


    /* ---- Review proof ----
       Michael's figures, supplied by him. Wording is the approved wording. */
    reviewRating: '4.8',
    reviewLine: 'Rated 4.8 stars by more than 400 MaliHaus clients',
    reviewUrl: 'https://www.experience.com/reviews/michael-mali',

    /* ---- Coverage ----
       The approved public coverage line. The advertising market list is
       deliberately NOT here and is never rendered to a visitor. */
    coverageLine: 'Serving homeowners across Florida and selected markets nationwide.'
  };

  window.MALIHAUS = CONFIG;

  /* ------------------------------------------------------------------ *
   * 1. dataLayer and Google Tag Manager
   * ------------------------------------------------------------------ */

  window.dataLayer = window.dataLayer || [];

  function track(event, params) {
    var payload = { event: event };
    if (params) for (var k in params) if (params.hasOwnProperty(k)) payload[k] = params[k];
    var a = attribution();
    for (var j in a) if (a.hasOwnProperty(j)) payload[j] = a[j];
    window.dataLayer.push(payload);
  }
  window.mhTrack = track;

  if (CONFIG.gtmId) {
    window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
    var g = document.createElement('script');
    g.async = true;
    g.src = 'https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(CONFIG.gtmId);
    document.head.appendChild(g);
  }

  /* ------------------------------------------------------------------ *
   * 2. Source attribution (proposal 03/02 and 03/11)
   *    First touch is kept for the whole session so a lead that arrives
   *    from an ad and converts three pages later still carries its source.
   * ------------------------------------------------------------------ */

  var ATTR_KEY = 'mh_attr';
  var ATTR_FIELDS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
                     'gclid', 'fbclid', 'msclkid', 'ttclid'];
  var attrCache = null;

  function store(key, value) {
    try { sessionStorage.setItem(key, value); } catch (e) { /* private mode */ }
  }
  function read(key) {
    try { return sessionStorage.getItem(key); } catch (e) { return null; }
  }

  function attribution() {
    if (attrCache) return attrCache;

    var existing = read(ATTR_KEY);
    if (existing) {
      try { attrCache = JSON.parse(existing); return attrCache; } catch (e) { /* fall through */ }
    }

    var q = new URLSearchParams(window.location.search);
    var a = {};
    for (var i = 0; i < ATTR_FIELDS.length; i++) {
      var v = q.get(ATTR_FIELDS[i]);
      if (v) a[ATTR_FIELDS[i]] = v.slice(0, 200);
    }

    /* No campaign parameters means we still want to know where they came from. */
    if (!a.utm_source) {
      var ref = document.referrer || '';
      if (!ref) {
        a.utm_source = 'direct';
        a.utm_medium = 'none';
      } else {
        var host = '';
        try { host = new URL(ref).hostname.replace(/^www\./, ''); } catch (e) { host = 'unknown'; }
        if (host === window.location.hostname.replace(/^www\./, '')) {
          return (attrCache = {}); /* internal navigation, do not overwrite */
        }
        a.utm_source = host;
        a.utm_medium = /google|bing|duckduckgo|yahoo|ecosia|brave/.test(host) ? 'organic' : 'referral';
      }
    }

    a.landing_page = window.location.pathname;
    a.first_seen = new Date().toISOString();

    attrCache = a;
    store(ATTR_KEY, JSON.stringify(a));
    return a;
  }

  /* Carry attribution across to the funnel so the lead record knows its source. */
  /* The site root, derived from the page's own canonical URL so this works
     identically from /, /situations/<slug>/ and /locations/<slug>/. */
  function siteRoot() {
    var base = document.querySelector('link[rel="canonical"]');
    var href = base ? base.getAttribute('href') : window.location.href;
    var root = href.replace(/\/(situations|locations|get-offer)\/.*$/, '');
    return root.replace(/\/[^\/]*\.html$/, '').replace(/\/+$/, '') + '/';
  }

  function funnelLink(extra) {
    var q = new URLSearchParams();
    var a = attribution();
    for (var k in a) if (a.hasOwnProperty(k) && k !== 'first_seen') q.set(k, a[k]);
    if (extra) for (var e in extra) if (extra.hasOwnProperty(e) && extra[e]) q.set(e, extra[e]);
    var s = q.toString();
    /* Query BEFORE the fragment, or the funnel never sees the attribution. */
    return siteRoot() + CONFIG.funnelPath + (s ? '?' + s : '') + CONFIG.funnelHash;
  }
  window.mhFunnelLink = funnelLink;

  /* ------------------------------------------------------------------ *
   * 3. Consistent number presentation (proposal 03/03)
   * ------------------------------------------------------------------ */

  function applyPhone(root) {
    var tel = 'tel:+1' + CONFIG.phoneDigits;
    var sms = 'sms:+1' + CONFIG.phoneDigits;
    var i, els;

    els = root.querySelectorAll('[data-call]');
    for (i = 0; i < els.length; i++) {
      els[i].setAttribute('href', tel);
      els[i].setAttribute('aria-label', 'Call MaliHaus on ' + CONFIG.phoneDisplay);
    }

    els = root.querySelectorAll('[data-sms]');
    for (i = 0; i < els.length; i++) {
      els[i].setAttribute('href', sms);
      els[i].setAttribute('aria-label', 'Text MaliHaus on ' + CONFIG.phoneDisplay);
    }

    els = root.querySelectorAll('[data-phone]');
    for (i = 0; i < els.length; i++) els[i].textContent = CONFIG.phoneDisplay;

    /* Structured data has to be readable by crawlers that do not run
       JavaScript, so the number is written into the JSON-LD literally.
       This checks the two can never drift apart unnoticed. */
    els = root.querySelectorAll('script[type="application/ld+json"]');
    for (i = 0; i < els.length; i++) {
      var found = els[i].textContent.match(/"telephone"\s*:\s*"([^"]+)"/);
      if (found && found[1] !== '+1' + CONFIG.phoneDigits) {
        if (window.console) console.warn(
          'MaliHaus: structured data telephone ' + found[1] +
          ' does not match the configured number +1' + CONFIG.phoneDigits);
      }
    }
  }

  /* ------------------------------------------------------------------ *
   * 4. Conversion events (proposal 03/11)
   * ------------------------------------------------------------------ */

  function wireEvents(root) {
    /* Phone taps and text taps, on every page and every button. */
    root.addEventListener('click', function (ev) {
      var el = ev.target.closest ? ev.target.closest('[data-call],[data-sms],[data-cta],[data-situation-link]') : null;
      if (!el) return;

      if (el.hasAttribute('data-call')) {
        track('phone_tap', { link_location: el.getAttribute('data-loc') || 'unknown' });
      } else if (el.hasAttribute('data-sms')) {
        track('text_tap', { link_location: el.getAttribute('data-loc') || 'unknown' });
      } else if (el.hasAttribute('data-situation-link')) {
        track('situation_click', { situation: el.getAttribute('data-situation-link') });
      } else {
        track('cta_click', {
          cta_text: (el.textContent || '').trim().slice(0, 80),
          link_location: el.getAttribute('data-loc') || 'unknown'
        });
      }
    }, true);

    /* Address form: start, submit and abandonment. */
    var forms = root.querySelectorAll('form[data-address-form]');
    for (var i = 0; i < forms.length; i++) {
      (function (form) {
        var started = false, submitted = false;
        var input = form.querySelector('input[type="text"]');

        if (input) {
          input.addEventListener('input', function () {
            if (started || !input.value.trim()) return;
            started = true;
            track('form_start', { form_name: 'address_entry' });
          });
        }

        form.addEventListener('submit', function (ev) {
          ev.preventDefault();
          submitted = true;
          var addr = input ? input.value.trim() : '';
          track('address_submit', {
            form_name: 'address_entry',
            has_address: addr ? 'yes' : 'no',
            situation: form.getAttribute('data-situation') || 'none'
          });
          window.location.href = funnelLink({
            address: addr,
            situation: form.getAttribute('data-situation') || ''
          });
        });

        window.addEventListener('pagehide', function () {
          if (started && !submitted) track('form_abandon', { form_name: 'address_entry' });
        });
      })(forms[i]);
    }

    /* Scroll depth, so we can see where the page loses people. */
    var marks = [25, 50, 75, 90], hit = {};
    window.addEventListener('scroll', function () {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      if (h <= 0) return;
      var pct = (window.scrollY / h) * 100;
      for (var i = 0; i < marks.length; i++) {
        if (pct >= marks[i] && !hit[marks[i]]) {
          hit[marks[i]] = true;
          track('scroll_depth', { percent_scrolled: marks[i] });
        }
      }
    }, { passive: true });
  }

  /* ------------------------------------------------------------------ *
   * 5. Chat: the GHL Conversation AI widget
   *    The widget sits in the reserved bottom right corner. Nothing else
   *    is allowed to live there, and the page reserves space at the foot
   *    of the document so it can never cover a button, a form control or
   *    the consent wording. See .mh-chat-safe in components.css.
   * ------------------------------------------------------------------ */

  function mountChat() {
    if (!CONFIG.ghlWidgetSrc) return false;

    var s = document.createElement('script');
    s.src = CONFIG.ghlWidgetSrc;
    s.async = true;
    for (var k in CONFIG.ghlWidgetAttrs) {
      if (CONFIG.ghlWidgetAttrs.hasOwnProperty(k)) s.setAttribute(k, CONFIG.ghlWidgetAttrs[k]);
    }
    document.body.appendChild(s);

    /* The concept receptionist stands down so the two never overlap. */
    document.documentElement.setAttribute('data-chat', 'ghl');
    var own = document.getElementById('launch');
    var wid = document.getElementById('wid');
    var nudge = document.getElementById('nudge');
    if (own) own.remove();
    if (wid) wid.remove();
    if (nudge) nudge.remove();
    return true;
  }

  /* ------------------------------------------------------------------ *
   * 6. Mobile navigation
   *    Keyboard operable: Escape closes it and focus is not left behind
   *    the overlay.
   * ------------------------------------------------------------------ */

  function wireDrawer() {
    var drawer = document.getElementById('mhdrawer');
    var open = document.getElementById('mhburger');
    if (!drawer || !open) return;

    var close = drawer.querySelector('.mh-drawer-x');
    var bg = drawer.querySelector('.mh-drawer-bg');
    var last = null;

    function show() {
      last = document.activeElement;
      drawer.classList.add('on');
      open.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      var first = drawer.querySelector('a,button');
      if (first) first.focus();
    }
    function hide() {
      drawer.classList.remove('on');
      open.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      if (last) last.focus();
    }

    open.addEventListener('click', show);
    if (close) close.addEventListener('click', hide);
    if (bg) bg.addEventListener('click', hide);
    drawer.addEventListener('click', function (ev) {
      if (ev.target.closest('a')) hide();
    });
    document.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape' && drawer.classList.contains('on')) hide();
    });
  }

  /* ------------------------------------------------------------------ *
   * 7. Boot
   * ------------------------------------------------------------------ */

  function init() {
    applyPhone(document);
    wireEvents(document);
    wireDrawer();
    attribution();
    if (CONFIG.ghlWidgetSrc) {
    var chatChoice = document.createElement('button');
    chatChoice.type = 'button';
    chatChoice.textContent = 'Open chat (HighLevel/LeadConnector)';
    chatChoice.style.cssText = 'margin:12px;padding:8px 12px';
    chatChoice.onclick = function(){ mountChat(); chatChoice.remove(); };
    (document.querySelector('footer') || document.body).appendChild(chatChoice);
    }
    track('page_ready', { page_type: document.body.getAttribute('data-page-type') || 'other' });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

/* Keep the embedded GHL message composer legible in the MaliHaus dark theme. */
(function () {
  'use strict';
  var STYLE_ID = 'mh-ghl-dark-composer';
  var CSS = [
    '.input-container-textarea{background:#0B0B0B!important;border:1px solid #C68C4E!important;}',
    '.native-textarea,textarea{color:#FFFFFF!important;caret-color:#C68C4E!important;}',
    'textarea::placeholder{color:#9CA3AF!important;opacity:1!important;}'
  ].join('');

  function apply(root) {
    if (!root || !root.querySelectorAll) return;
    if (root.querySelector('textarea')) {
      if (!root.querySelector('#' + STYLE_ID)) {
        var style = document.createElement('style');
        style.id = STYLE_ID;
        style.textContent = CSS;
        root.appendChild(style);
      }
    }
    root.querySelectorAll('*').forEach(function (element) {
      if (element.shadowRoot) apply(element.shadowRoot);
    });
  }

  function refresh() {
    apply(document);
  }

  document.addEventListener('click', function () {
    setTimeout(refresh, 100);
  }, true);

  var attempts = 0;
  var timer = setInterval(function () {
    refresh();
    attempts += 1;
    if (attempts >= 120) clearInterval(timer);
  }, 500);
})();
