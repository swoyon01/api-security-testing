# 01 · API Keys and Basic Auth

> Both are simple ways to prove identity to an API. Both are easy to get wrong.

---

## 🔑 API Keys

An API key is a long random string that identifies a client (an app, a script, or a partner).

### Where keys are sent

| Placement | Example | Risk |
|-----------|---------|------|
| Header (best) | `X-API-Key: abc123...` | Visible in traffic, so use HTTPS |
| Query string | `GET /api/data?api_key=abc123` | Stored in browser history, server logs, and the `Referer` header |
| Cookie | `Cookie: api_key=abc123` | Sent automatically by the browser, so CSRF is possible |
| Request body | `{"api_key":"abc123"}` | Easy to leak through logs and error messages |

### What to test

- **Key in the URL:** look for `api_key=`, `key=`, `token=` in URLs in Burp's HTTP history.
- **Key in client code:** search JavaScript files for strings that look like keys.
- **No key needed:** remove the key header completely and resend. A `200` means the check is missing.
- **Weak key:** check whether the key is short, predictable, or reused across users.
- **Key not revoked:** after you rotate or delete a key, test whether the old key still works.
- **Key scope:** a read-only key should not be able to write.

### Secure practice

- Send keys only in a header, over HTTPS.
- Give each client its own key, with the least privilege it needs.
- Store keys in a secrets manager, not in source code.
- Rotate keys and revoke them when they leak.

---

## 🔐 Basic Auth

Basic Auth sends the username and password, joined by a colon and encoded in Base64, with every request:

```http
Authorization: Basic d2llbmVyOnBldGVy
```

`d2llbmVyOnBldGVy` decodes to `wiener:peter`.

> **Base64 is not encryption.** Anyone who sees the header can decode it immediately.

### What to test

- **Decode the header:** in Burp, use **Decoder** or run `echo "d2llbmVyOnBldGVy" | base64 -d` in the terminal.
- **Sent over plain HTTP:** if the header travels without TLS, the credentials are exposed.
- **No rate limit:** Basic Auth is checked on every request, so brute force is easy if nothing limits attempts. Test this in Intruder on a lab only.
- **Different error messages:** a message such as "user not found" versus "wrong password" enables username enumeration.

### Secure practice

- Use Basic Auth only over HTTPS.
- Add rate limiting and lockout.
- Prefer tokens (see the sessions note) for APIs used by apps and mobile clients.

---

## 🧪 Practice Ideas

- Decode a sample Basic Auth header with `base64 -d` and write down the credentials.
- Send a request to crAPI or VAmPI with and without the `Authorization` header, and record the status codes.
- Search the HTTP history of one lab for `key`, `token`, or `api` in the URL.

---

## 🔗 References

- [OWASP API2:2023 — Broken Authentication](https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/)
- [MDN: Authorization header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
