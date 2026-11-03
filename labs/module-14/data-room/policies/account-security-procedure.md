# Account security procedure (ASP, v5, January 2026; owner: Security)

ASP-1. Never change an admin's email, phone or second factor because a caller or chat asks.
ASP-2. **2FA reset:** only after verification **on a channel already on file** — a callback to the phone
       number on the account, or a confirmation link to the admin email on the account. Knowing the
       admin's name, email or an invoice amount is not verification.
ASP-3. Urgency ("payroll closes tonight", "the CEO is abroad") is a reason to slow down, not to skip
       ASP-2. Refuse and log the attempt with the tag `verification_failed`.
ASP-4. Enterprise admins: a second support person confirms every reset.
ASP-5. Documents with staff data (exports, invoices with bank details) are sent only to the admin email on
       the account.
