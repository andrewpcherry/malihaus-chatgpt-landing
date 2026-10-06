# Seller funnel → HighLevel

## Owner and route

`get-offer/index.html` loads `seller-delivery.js` and `funnel.js`. **The seller adapter, not `MALIHAUS.leadEndpoint`, owns delivery.** The empty legacy endpoint in `site.js` is intentional for this route and no longer means seller submissions are saved only locally. Legacy `form.js` is not loaded by the current pages.

The qualified enquiry becomes the native DOM form `malihaus-seller-enquiry`. After contact and consent validation, the adapter loads the official public `https://link.msgsndr.com/js/external-tracking.js` using the account's public tracking ID and allows one validated native submit through. The script is not installed globally: incomplete homepage/address handoff forms must not create contacts. No private CRM token is present in the site.

Official reference: https://help.gohighlevel.com/support/solutions/articles/155000006092-tracking-external-forms-with-gohighlevel

## Confirmation and duplicate handling

The vendor SDK can swallow submission failures. The adapter therefore observes only this form's actual vendor POST acknowledgment: matching event type, form ID and tracking ID, HTTP success and JSON `status: "ok"`. It does not treat `fetch()` resolution, local storage, or SDK completion alone as success. This confirms ingestion, not subsequent automation completion. A vendor transport change fails closed and requires retesting.

A single in-flight promise prevents double clicks. Capture-phase guards prevent native/keyboard events from bypassing validation. Text, consent and navigation are locked while the attempt is active. A SHA-256 enquiry fingerprint and status in sessionStorage prevent same-session reload re-submission for 24 hours. Only hashes/status/timestamps are added to that deduplication ledger. The existing local lead diagnostic storage is unchanged. If storage is blocked, the in-memory guard still works, but reload protection cannot be guaranteed.

Uncertain delivery is not automatically resubmitted; the visitor is told confirmation was unavailable and to call. This is not an exactly-once guarantee across independent browsers or the vendor's own network retries. Native GHL contact matching/upsert is separate from the website guard.

## Field mapping and boundaries

- Standard name, phone or email, city/state/ZIP are named native fields. Phone-only remains supported.
- **Use `name="address"` and label `Street Address`.** Although the API property is `address1`, a native input called `address1` and labeled `Property address` was not mapped during actual read-back.
- Existing seller custom fields are matched by exact names, including **Conversation Summary**, **Important Circumstances / Notes**, Property Type, Property Ownership, Occupancy Status, Price Expectation (Optional), Preferred Callback Time, Preferred Contact Method, Phone/Text Contact Permission, Human Follow-Up Requested, Reason for Considering a Sale, Property Condition and Desired Selling Timeframe.
- Conversation Summary retains the website source, tier/reason, canonical qualification answers, consent timestamp/page, seller notes and original session attribution/UTMs. The notes field also retains seller notes separately.
- Native contact `source` is **`external_form`**, with attribution `mediumId` **`malihaus-seller-enquiry`**. This integration does **not** promise `contact.source = Website Funnel` or apply CRM tags. Source/tier form fields without matching custom fields may remain unmapped; their authoritative retained copy is the existing summary field.
- Original homepage UTMs are retained in the summary even when internal navigation removes them from the final page URL. Native top-level GHL attribution UTMs may then be null; do not confuse that with lost enquiry attribution.
- Existing buyer Zaps, published/draft workflows, chatbot behavior and downstream follow-up sequences are not edited. The broader flow remains website/chatbot → GHL → Zapier → REsimpli. **REsimpli delivery is not verified by this change.**

## Tests and release acceptance

`tests/test_seller_delivery.py` runs isolated Playwright/Chrome tests. Install `playwright` in a Python virtual environment; set `CHROME_BIN` when Chrome is not `/usr/local/bin/google-chrome`. Tests fetch the current public vendor script, serve local pages, and intercept all tracker POSTs: they do not create CRM contacts.

```sh
python tests/test_seller_delivery.py
node --check funnel.js
node --check seller-delivery.js
git diff --check
```

A release additionally requires a real isolated browser on the **deployed** homepage, all qualification steps, UI submission with a controlled example.invalid email or reserved fictional NANP phone, one captured native submission, and authenticated GET read-back of the exact contact ID. Assert standard address and seller custom-field values, not merely HTTP200 or contact existence. GHL processing/search indexing may take several seconds; use bounded repeat reads. Save request/response evidence and screenshots outside this public repository; never commit API headers or credentials.
