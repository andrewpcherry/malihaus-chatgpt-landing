"""Run with Python + playwright; Chrome executable is configurable.
No real CRM writes: serve local pages and intercept every tracker POST.
"""
import json, os, unittest
from pathlib import Path
from urllib.request import urlopen
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parents[1]
TRACKER = urlopen('https://link.msgsndr.com/js/external-tracking.js').read().decode()

class SellerDeliveryTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.p=sync_playwright().start()
  cls.browser=cls.p.chromium.launch(executable_path=os.environ.get('CHROME_BIN','/usr/local/bin/google-chrome'),headless=True,args=['--no-sandbox'])
 @classmethod
 def tearDownClass(cls): cls.browser.close();cls.p.stop()
 def setUp(self):
  self.page=self.browser.new_page();self.events=[];self.status=200;self.body={'status':'ok'}
  self.page.clock.install()
  self.page.route('**/*',lambda r:r.abort())
  self.page.route('https://test.malihaus.invalid/**',lambda r:r.fulfill(path=str(ROOT/(r.request.url.split('invalid/')[1].split('?')[0] or 'index.html'))))
  self.page.route('**/external-tracking.js',lambda r:r.fulfill(body=TRACKER,content_type='application/javascript'))
  self.page.route('**/external-tracking/events',self.event)
  self.page.goto('https://test.malihaus.invalid/get-offer/index.html')
  self.page.evaluate("MHF.pickAndGo('condition'); MHF.answer('issue','The roof','What is wrong?'); MHF.toContact()")
  for k,v in {'firstName':'QA','lastName':'Seller','email':'qa@example.invalid','address':'123 QA Test Lane','city':'Boca Raton','zip':'33432','mhfNotes':'CONTROLLED QA ONLY'}.items():self.page.locator('#'+k).fill(v)
  self.page.locator('#consent').check()
 def tearDown(self):self.page.close()
 def event(self,r):
  self.events.append(r.request.post_data_json)
  r.fulfill(status=self.status,json=self.body,headers={'Access-Control-Allow-Origin':'*'})
 def submit(self):self.page.locator('#mhf-send').click();self.page.wait_for_timeout(1500)
 def submissions(self):return [e for e in self.events if e['type']=='external_form_submission']
 def test_success(self):
  self.submit();self.page.wait_for_selector('.mhf-done');self.assertEqual(len(self.submissions()),1)
  data=self.submissions()[0]['formData']
  self.assertEqual(data['important_circumstances__notes'],'CONTROLLED QA ONLY')
  self.assertIn('Lead tier',data['conversation_summary']);self.assertEqual(data['state'],'FL')
  self.assertEqual(self.page.locator('.mhf-done').count(),1)
 def test_delayed_sdk_keeps_validated_contact_and_consent(self):
  held=[]
  self.page.route('**/external-tracking.js',lambda r:held.append(r))
  self.page.locator('#phone').fill('2025550189')
  self.submit();self.assertEqual(len(held),1)
  accepted=self.page.evaluate('JSON.parse(JSON.stringify(window.mhLastLead))')
  # Real keyboard/pointer edits must not change the accepted enquiry.
  self.page.locator('#email').focus();self.page.keyboard.press('Control+A');self.page.keyboard.type('changed@example.invalid')
  self.page.locator('#phone').focus();self.page.keyboard.press('Control+A');self.page.keyboard.type('2025550199')
  self.page.locator('#consent').scroll_into_view_if_needed()
  box=self.page.locator('#consent').bounding_box()
  self.page.mouse.click(box['x']+box['width']/2,box['y']+box['height']/2)
  self.assertTrue(self.page.locator('#consent').is_checked())
  self.assertTrue(self.page.locator('#consent').is_disabled())
  self.assertEqual(self.page.locator('#email').input_value(),accepted['contact']['email'])
  self.assertEqual(self.page.locator('#phone').input_value(),accepted['contact']['phone'])
  # Caller-owned objects and live DOM must not replace the accepted snapshot.
  self.page.evaluate("mhLastLead.contact.email='changed@example.invalid'; mhLastLead.consent.given=false; document.getElementById('phone').value='2025550199'")
  held[0].fulfill(body=TRACKER,content_type='application/javascript')
  self.page.wait_for_selector('.mhf-done')
  self.assertEqual(len(self.submissions()),1)
  data=self.submissions()[0]['formData']
  self.assertEqual(data['email'],accepted['contact']['email'])
  self.assertEqual(data['phone'],accepted['contact']['phone'])
  self.assertIn('Consent: '+json.dumps(accepted['consent'],separators=(',',':')),data['conversation_summary'])
  self.assertEqual(data['phonetext_contact_permission'],'Consent given: '+accepted['consent']['at'])
  self.assertEqual(self.page.locator('.mhf-done').count(),1)
 def test_invalid_email(self):
  self.page.locator('#email').fill('not-an-email');self.submit()
  self.assertEqual(len(self.submissions()),0)
 def test_invalid_phone(self):
  self.page.locator('#phone').fill('123');self.submit();self.assertEqual(len(self.submissions()),0)
 def test_reload_does_not_resend_confirmed_enquiry(self):
  self.submit();self.page.wait_for_selector('.mhf-done');self.assertEqual(len(self.submissions()),1)
  self.page.reload()
  self.page.evaluate("MHF.pickAndGo('condition'); MHF.answer('issue','The roof','What is wrong?'); MHF.toContact()")
  for k,v in {'firstName':'QA','lastName':'Seller','email':'qa@example.invalid','address':'123 QA Test Lane','city':'Boca Raton','zip':'33432','mhfNotes':'CONTROLLED QA ONLY'}.items():self.page.locator('#'+k).fill(v)
  self.page.locator('#consent').check();self.submit();self.page.wait_for_selector('.mhf-done');self.assertEqual(len(self.submissions()),1)
 def test_missing_consent(self):
  self.page.locator('#consent').uncheck();self.submit();self.assertEqual(len(self.submissions()),0)
 def test_phone_only(self):
  self.page.locator('#email').fill('');self.page.locator('#phone').fill('+12025550189');self.submit()
  self.page.wait_for_selector('.mhf-done')
  self.assertEqual(len(self.submissions()),1)
 def test_http_failure_is_not_success(self):
  self.page.evaluate("window.nativeSubmits=0; document.getElementById('malihaus-seller-enquiry').addEventListener('submit',()=>window.nativeSubmits++)")
  self.status=500
  with self.page.expect_request(lambda r:r.url.endswith('/external-tracking/events') and r.post_data_json.get('type')=='external_form_submission'):
   self.submit()
  self.assertEqual(self.page.locator('.mhf-done').count(),0)
  self.assertTrue(self.page.locator('.mhf-backbtn').is_disabled())
  self.page.locator('#malihaus-seller-enquiry').evaluate('(f)=>f.requestSubmit()')
  self.page.clock.fast_forward(31000)
  message=self.page.locator('#mhf-err').inner_text()
  self.assertIn('could not confirm delivery',message)
  self.assertIn('may have arrived',message)
  self.assertNotIn('has not been sent',message)
  # The SDK can retry its HTTP request; the adapter must dispatch only once.
  self.assertGreaterEqual(len(self.submissions()),1)
  self.assertEqual(self.page.evaluate('window.nativeSubmits'),1)
  self.assertEqual(self.page.evaluate("Object.keys(sessionStorage).filter(k=>k.startsWith('mh_seller_')).map(k=>JSON.parse(sessionStorage[k]).status)"),['pending'])
  self.assertTrue(self.page.locator('#consent').is_disabled())
 def test_negative_ack_is_not_success(self):
  self.body={'status':'error'};self.submit();self.assertEqual(self.page.locator('.mhf-done').count(),0)
 def test_double_submit(self):
  self.page.evaluate('MHF.submit();MHF.submit()');self.page.wait_for_selector('.mhf-done')
  self.assertEqual(len(self.submissions()),1)
 def test_native_submit_runs_validation_and_delivery(self):
  self.page.locator('#malihaus-seller-enquiry').evaluate('(f)=>f.requestSubmit()');self.page.wait_for_selector('.mhf-done')
  self.assertEqual(len(self.submissions()),1)
 def test_script_timeout_cannot_dispatch_when_sdk_arrives_late(self):
  held=[]
  self.page.route('**/external-tracking.js',lambda r:held.append(r))
  self.submit();self.assertEqual(len(held),1)
  self.page.clock.fast_forward(31000)
  timeout_message=self.page.locator('#mhf-err').inner_text()
  held[0].fulfill(body=TRACKER,content_type='application/javascript')
  self.page.wait_for_timeout(1500)
  self.page.locator('#malihaus-seller-enquiry').evaluate('(f)=>f.requestSubmit()')
  self.page.evaluate('MHF.submit()')
  self.page.wait_for_timeout(1500)
  self.assertEqual(len(self.submissions()),0)
  self.assertEqual(self.page.locator('.mhf-done').count(),0)
  self.assertIn('has not been sent',timeout_message)
  self.assertNotIn('may have arrived',timeout_message)
  self.assertEqual(self.page.locator('#mhf-err').inner_text(),timeout_message)
  self.assertEqual(self.page.evaluate("Object.keys(sessionStorage).filter(k=>k.startsWith('mh_seller_')).length"),0)
 def test_missing_tracker_is_not_success(self):
  self.page.route('**/external-tracking.js',lambda r:r.abort());self.submit()
  self.assertEqual(self.page.locator('.mhf-done').count(),0)
  self.assertIn('unavailable',self.page.locator('#mhf-err').inner_text())

if __name__=='__main__':unittest.main(verbosity=2)
