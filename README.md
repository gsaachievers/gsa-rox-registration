# GSA ROX registration form — GitHub Pages + Supabase

## Included
- `index.html` — responsive entry form matching the supplied PDF style, including consent and payment section
- `logo.png` — supplied GrowStrong Achievers logo
- `payment-qr.jpeg` — supplied Paytm QR image (recipient AP WIZARD PRO)
- `config.js` — configure Supabase URL and **publishable/anon** key
- `supabase.sql` — create registration table and public INSERT-only RLS policy

## Install
1. In Supabase SQL Editor, run `supabase.sql`. Creates a NEW `gsa_rox_registrations` table. Does not alter `gsa_leads`.
2. In Supabase Project Settings > API, copy the Project URL and publishable/anon key into `config.js`. **Never** put the service-role/secret key in GitHub.
3. Create a public GitHub repo. Upload all five files to repo root.
4. Repo Settings > Pages > Deploy from branch > main > /(root) > Save. Wait for published URL.
5. Test registration on phone, then verify record in Supabase Table Editor.
6. Generate registration QR using the exact GitHub Pages URL at https://www.qrcode-monkey.com/ . The Paytm QR in the form is a DIFFERENT QR.

## Important
- The PDF says **₹1,000**, while the supplied Google Form screenshot says **₹500**. This version uses ₹1,000 as printed in the PDF. Confirm pricing before launch; if changed, update the HTML and SQL constraint together.
- Payment link is transcribed from the supplied screenshot: `https://p.ppsl.io/PYTMPS/03liBk`. Confirm that it is active, points to AP WIZARD PRO, and supports entering ₹1,000 before publishing.
- Payment status is a **parent's claim**, not verified payment. Verify the UTR with your Paytm/bank settlement records. No automatic payment reconciliation.
- Supabase RLS allows anonymous inserts only. No public SELECT/UPDATE/DELETE. Add CAPTCHA/Turnstile and server-side rate limiting before public promotion.
- Avoid publicly storing child medical data without appropriate privacy notice, access control, retention policy and secure handling.
- If you already ran an earlier version of `supabase.sql`, use a new table or migrate the existing schema; `CREATE TABLE IF NOT EXISTS` will not add new columns to an existing table.
