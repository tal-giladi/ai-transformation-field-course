# Data deletion procedure (v2, September 2025; owner: Legal / DPO)

1. Deletion requests go to **privacy-requests** (Deskly group) and are handled by Legal.
2. Before deleting: confirm the requester is the account admin (ASP-2); check what must be kept — invoices
   and payment records (tax), and payroll exports the customer may need; confirm in writing with the admin.
3. Deletion in the **admin console** is a soft delete: data is hidden at once and purged after **14 days**,
   during which Legal can restore it.
4. The Admin API endpoint `DELETE /accounts/{id}/data` is for R&D maintenance only. **It purges at once and
   cannot be undone.**
5. "Stop emails" is not a deletion request: point the customer to notification settings (HC-160).
