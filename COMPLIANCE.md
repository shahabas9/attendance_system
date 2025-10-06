# Security & Compliance

## Security

- All APIs are protected by JWT authentication.
- Role-based access control restricts sensitive endpoints to admin users.
- HTTPS/TLS is required in all production deployments.
- All sensitive actions are logged in the AuditLog table for traceability.

## GDPR

- Users can request deletion of their profile and attendance data.
- Data retention policy: raw_events are auto-deleted after 1 year.
- Attendance and user data can be deleted by admins as required.
- No raw images are stored; only embeddings for privacy.
- Audit logs track all modifications.

## End-to-End Encryption

- All API communication is encrypted via HTTPS.
- JWT tokens used for authentication.
- Optionally, client-side encryption can be layered for sensitive data.

## Audit

- All attendance/user/admin modifications are logged.
- Logs are accessible via the `/admin/audit` API endpoint.

## Privacy

- Face recognition stores only embeddings, not raw images.
- Data access is restricted by role.
