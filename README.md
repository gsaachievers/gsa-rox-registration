# GSA ROX Registration — GitHub Pages + Supabase

1. In Supabase > SQL Editor, run `supabase.sql` in your intended project. Review existing table/policies before running again.
2. In Supabase > Project Settings > API, copy **Project URL** and **publishable/anon key** into `config.js`. **Never use the secret/service_role key.**
3. Create a GitHub repository, e.g. `gsa-rox-registration`, and upload `index.html` and `config.js` to its root. Keep `supabase.sql`/README in the repo if desired.
4. GitHub repository > Settings > Pages > Deploy from a branch > main > / (root) > Save. Wait for GitHub to show the live URL, normally `https://YOUR-USERNAME.github.io/gsa-rox-registration/`.
5. Test a registration. Check Supabase > Table Editor > `gsa_rox_registrations` to confirm the new row. Only organizers with authenticated dashboard access should see records. Payment fields are editable by staff in Supabase dashboard.
6. **QR code:** Once the final Pages URL is live, paste it into a reputable QR generator, or use the companion `make_qr.py` script. Download a high-resolution PNG and test on two phones before printing.

**Important:** This is a static website, not a GitHub-hosted database. GitHub Pages serves the form; Supabase stores the records. The public key is designed to be exposed, so RLS is critical. Public anonymous inserts can be spammed: add CAPTCHA, rate limiting and server-side validation before a high-volume launch. The medical and children's data is sensitive; minimize collection, restrict access, set a retention policy, and obtain appropriate privacy/legal review of consent language. Payment is NOT collected online by this form. Do not claim an entry is confirmed until staff checks payment.
