# 01 · HTTP Methods

> HTTP methods (also called verbs) tell the server what action to perform on a resource.
> In API security testing, each method has different risks, so each one needs its own test.

---

## 📋 Overview

| Method | Purpose | Safe | Idempotent | Main security risk |
|--------|---------|:----:|:----------:|--------------------|
| **GET** | Retrieve data | ✅ | ✅ | Data exposure in the URL |
| **POST** | Create a resource | ❌ | ❌ | CSRF, injection, mass assignment |
| **PUT** | Replace a resource | ❌ | ✅ | Unauthorized modification |
| **PATCH** | Partially update a resource | ❌ | Not guaranteed | Mass assignment |
| **DELETE** | Remove a resource | ❌ | ✅ | Unauthorized deletion |
| **OPTIONS** | List supported methods (CORS preflight) | ✅ | ✅ | Information disclosure, CORS misconfiguration |
| **HEAD** | Same as GET, headers only | ✅ | ✅ | Fingerprinting, auth inconsistencies |

**Terms used in this table**
- **Safe:** the method should not change data on the server.
- **Idempotent:** sending the same request several times gives the same final result.

---

## 1️⃣ GET

**What it does:** requests data from a resource.

```http
GET /api/users/1 HTTP/1.1
Host: example.com
Authorization: Bearer eyJhbGci...
```

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Security notes**
- ⚠️ Do not send sensitive data in GET requests. The data can appear in browser history, server logs, and the `Referer` header.
- ⚠️ GET responses can be cached by browsers and proxies. Check that private responses use `Cache-Control: no-store` or `private`.
- URLs have practical length limits (around 2,048 characters in many browsers).

**Testing tip**
```
GET /api/users/1      → 200 OK (your own user)
GET /api/users/2      → 200 OK?  (BOLA/IDOR test)
GET /api/users/9999   → 404 Not Found?
GET /api/admin/users  → 403 Forbidden?  (BFLA test)
```

---

## 2️⃣ POST

**What it does:** sends data to be processed, usually to create a new resource.

```http
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer eyJhbGci...

{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "role": "user"
}
```

```json
{
  "id": 101,
  "name": "Jane Doe",
  "email": "jane@example.com",
  "role": "user",
  "created_at": "2024-01-15T10:30:00Z"
}
```

**Security notes**
- ✅ Data travels in the body, not the URL, so it is better for sensitive data.
- ⚠️ **Mass assignment:** the server may accept extra fields such as `"role": "admin"`.
- ⚠️ **CSRF:** check whether the API requires a token or a custom header.
- ⚠️ **Injection:** SQL and NoSQL injection can occur in body parameters.

**Testing tip**
```json
// Normal request
{ "name": "Jane", "email": "jane@test.com" }

// Mass assignment test
{ "name": "Jane", "email": "jane@test.com", "role": "admin", "is_admin": true, "id": 1 }
```

---

## 3️⃣ PUT

**What it does:** replaces the entire resource with the payload you send.

```http
PUT /api/users/1 HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer eyJhbGci...

{
  "id": 1,
  "name": "John Updated",
  "email": "john.updated@example.com",
  "role": "user"
}
```

**PUT vs PATCH**

| PUT | PATCH |
|-----|-------|
| Replaces the **entire** resource | Updates **only the fields you send** |
| You must send all fields | You can send one field |
| Idempotent | Not guaranteed to be idempotent |

**Security notes**
- ⚠️ Fields you leave out may be reset to `null` or defaults, which can cause data loss.
- ⚠️ If the ID in the URL and the ID in the body don't match, the server may update the wrong object (IDOR).
- ⚠️ If the server does not check ownership, one user can overwrite another user's data.

**Testing tip**
```
PUT /api/users/1   (logged in as User 2)
→ Expected: 403 Forbidden
→ If 200 OK: BOLA vulnerability
```

---

## 4️⃣ PATCH

**What it does:** applies a partial change to a resource.

```http
PATCH /api/users/1 HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer eyJhbGci...

{
  "email": "new.email@example.com"
}
```

**Security notes**
- ⚠️ **Mass assignment is the main risk here.** Developers often forget to restrict which fields can be updated.
- ⚠️ **JSON Patch (RFC 6902)** uses operations such as `{ "op": "replace", "path": "/role", "value": "admin" }`. If the server applies these without checks, it may bypass validation.

**Testing tip**
```json
// Try changing read-only or privileged fields
{ "id": 999, "role": "admin", "password": "hacked", "created_at": "2010-01-01" }
```

---

## 5️⃣ DELETE

**What it does:** removes a resource.

```http
DELETE /api/users/1 HTTP/1.1
Host: example.com
Authorization: Bearer eyJhbGci...
```

```http
HTTP/1.1 204 No Content
```

**Security notes**
- ⚠️ No confirmation is usually required. One request permanently deletes the resource.
- ⚠️ Check that the server verifies ownership before deleting.
- ⚠️ Cascade deletion: deleting a user may also delete their posts, orders, or files.

**Testing tip**
```http
DELETE /api/users/1        (logged in as User 2)
→ Expected: 403 Forbidden
→ If 204: critical vulnerability

DELETE /api/admin/users/1  (logged in as a normal user)
→ Expected: 403 Forbidden
→ If 204: BFLA vulnerability
```

---

## 6️⃣ OPTIONS

**What it does:** returns the methods the server supports for a URL. Browsers also send OPTIONS automatically before some cross-origin requests (CORS preflight).

```http
OPTIONS /api/users HTTP/1.1
Host: example.com
```

```http
HTTP/1.1 204 No Content
Allow: GET, POST, HEAD, OPTIONS
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
```

**Security notes**
- ℹ️ It can reveal which methods are allowed, which helps you plan tests.
- ℹ️ Browsers send OPTIONS as a CORS preflight before some requests.
- ⚠️ **CORS risk:** browsers block `Access-Control-Allow-Origin: *` when credentials are included. The real risk is when the server reflects any origin in `Access-Control-Allow-Origin` and also sets `Access-Control-Allow-Credentials: true`. Test this by sending an `Origin` header with a foreign value.

**Testing tip**
```http
OPTIONS /api/admin/users
→ If DELETE is listed in Allow: check whether it is actually authorized.
```

---

## 7️⃣ HEAD

**What it does:** works like GET, but the server returns only the headers, with no body. Load balancers and monitoring tools often use it for health checks.

```http
HEAD /api/users/1 HTTP/1.1
Host: example.com
Authorization: Bearer eyJhbGci...
```

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 84
Server: nginx/1.18.0
X-Powered-By: Express
```

**Security notes**
- ⚠️ **Fingerprinting:** headers like `Server` and `X-Powered-By` reveal the software stack. Good security practice is to remove them.
- ⚠️ **Inconsistent authorization:** some frameworks route HEAD to the GET handler, but some apps check auth only in the GET code. Test whether HEAD returns the same status as GET for protected resources.

**Testing tip**
```
GET  /api/admin/users → 403 Forbidden
HEAD /api/admin/users → 200 OK?  (auth inconsistency)
```

---

## 🎯 Method-Based Access Control Testing

Sometimes an API checks authorization for GET but forgets it for other methods:

```http
GET    /api/users/1   → 200 OK      (you can read)
PUT    /api/users/1   → 200 OK?     (can you modify?)
PATCH  /api/users/1   → 200 OK?     (can you partially update?)
DELETE /api/users/1   → 204?        (can you delete?)
```

**If GET requires authentication but PUT, PATCH, or DELETE does not, that is a serious bug.**

---

## 🔁 Method Override Headers

Some frameworks let a client send a POST and ask the server to treat it as another method:

```http
POST /api/users/1 HTTP/1.1
X-HTTP-Method-Override: DELETE
```

Other names to try: `X-Method-Override`, and the `_method` form field used by Rails and Laravel.

**Why it matters:** a proxy or firewall rule that blocks DELETE may not block POST with an override header. Test whether the server honors the header, and whether the override bypasses the authorization rules that apply to DELETE.

---

## 🚦 Status Codes That Matter for Method Testing

| Code | Meaning | What it tells you |
|:----:|---------|-------------------|
| 200 / 201 / 204 | Success | The action worked |
| 401 | Unauthorized | You are not logged in, or your token is invalid |
| 403 | Forbidden | You are logged in, but you are not allowed to do this |
| 404 | Not Found | The resource does not exist, or the server is hiding it |
| 405 | Method Not Allowed | The resource exists, but this method is not supported |

**Note:** some APIs return 404 instead of 403 so attackers cannot tell that a resource exists. Treat 404 as a hint, not as proof.

---

## 📝 Practice Log

All practice used the public API at `https://jsonplaceholder.typicode.com`. This is a fake API for practice, so no real data is at risk.

### Day 1 — GET

**Request**
```
GET https://jsonplaceholder.typicode.com/posts/1
```
<img width="2560" height="1368" alt="image" src="https://github.com/user-attachments/assets/808a33ed-10ff-45ab-9361-d046bfa1922d" />

**Result:** `200 OK`, response time 650 ms, JSON body returned.

**Observations**
- GET retrieves existing data.
- The request has no body.
- The ID is visible in the URL.

---

### Day 2 — POST

**Request**
```http
POST https://jsonplaceholder.typicode.com/posts
Content-Type: application/json

{
  "userId": 1,
  "title": "Learning Postman",
  "body": "Understanding HTTP METHODS and API testing with Postman"
}
```

<img width="1280" height="684" alt="image" src="https://github.com/user-attachments/assets/da9294b9-b58d-4950-8216-0a6190cfd4e1" />

**Result:** `201 Created`, response time 655 ms, new `id: 101` assigned by the server.

**Observations**
- POST creates a new resource.
- The data is in the body, so it is not visible in the URL.
- `201` confirms that a resource was created.

---

### Day 3 — PUT

**Request**
```http
PUT https://jsonplaceholder.typicode.com/posts/10
Content-Type: application/json

{
  "userId": 1,
  "title": "Postman Basics",
  "body": "Learning HTTP methods: GET, POST, PUT, DELETE"
}
```

<img width="1280" height="684" alt="Screenshot 2026-09-03 050322" src="https://github.com/user-attachments/assets/4fc0845d-76ec-443c-8027-9b20ed7d01f3" />

**Result:** `200 OK`, response time 1.10 s, `id` stayed 10.

**Observations**
- PUT replaces the whole resource, so every field must be sent.
- The response returns the full updated object.

**Security notes**
- ⚠️ **IDOR risk:** if User A can PUT to `/posts/11` (User B's post), that is unauthorized modification.
- ⚠️ **Missing fields:** check what happens to fields you do not send.

---

### Day 4 — PATCH

**Request**
```http
PATCH https://jsonplaceholder.typicode.com/posts/10
Content-Type: application/json

{
  "title": "Postman Basics & API testing"
}
```

<img width="1280" height="684" alt="Screenshot 2026-09-03 051517" src="https://github.com/user-attachments/assets/aa5f7a78-6e77-40bb-bfb3-e504c1958ce3" />

**Result:** `200 OK`, response time 1.10 s.

**Observations**
- Only `title` changed. `body`, `userId`, and `id` stayed the same.
- PATCH is safer than PUT for small updates.

**Security notes**
- ⚠️ **Mass assignment:** try sending `"role": "admin"` or `"isAdmin": true`.
- ⚠️ JSON Patch operations can bypass validation if the server applies them without checks.

---

### Day 5 — DELETE

**Request**
```http
DELETE https://jsonplaceholder.typicode.com/posts/10
```

<img width="1280" height="684" alt="Screenshot 2026-09-03 052246" src="https://github.com/user-attachments/assets/24fab316-2699-4c3c-b56a-2650f55d1f2b" />

**Result:** `200 OK`, response body `{}`, response time 974 ms.

**Observations**
- DELETE removes the resource and needs no body.
- The response body is empty.

**Security notes**
- ⚠️ No confirmation is required. One request deletes the resource.
- ⚠️ Check ownership before allowing DELETE.
- ⚠️ Cascade delete: deleting a user may remove their related data.
- ⚠️ BFLA test: can a normal user DELETE `/admin/posts/1`?

---

### Day 6 — OPTIONS and HEAD

**OPTIONS request**
```
OPTIONS https://jsonplaceholder.typicode.com/posts
```

**Observed `Allow` header:** `GET, POST, HEAD, OPTIONS`

**Observation:** PUT and DELETE are not listed, so this endpoint does not accept them.

**HEAD request**
```bash
curl -I https://jsonplaceholder.typicode.com/posts/1
```

**Result:** headers only, no body. Record the status code and the headers you see.

| Check | Result |
|-------|--------|
| Status code | `[fill in from your response]` |
| `Content-Type` | `[fill in]` |
| Server or framework headers | `[fill in]` |

---

## 🧪 To Do: Method Testing on a Real Lab

These tasks need a lab running locally, such as crAPI. Record the results here when you finish them.

### Task 1 — Method tampering

1. Find a request that works with GET on a crAPI endpoint.
2. Send it to Burp Repeater.
3. Change the method to PUT, PATCH, and DELETE.
4. Record the results below.

| Method | Status code | Vulnerable? |
|--------|:-----------:|:-----------:|
| GET | `[fill in]` | — |
| PUT | `[fill in]` | `[yes / no]` |
| PATCH | `[fill in]` | `[yes / no]` |
| DELETE | `[fill in]` | `[yes / no]` |

### Task 2 — Method override

1. Send a POST to an endpoint that normally rejects DELETE.
2. Add `X-HTTP-Method-Override: DELETE`.
3. Record whether the server honors it, and the status code.

---

## ✅ Method Testing Summary

| Method | What to test | Secure result | Vulnerable result |
|--------|-------------|---------------|-------------------|
| GET | Access to another user's object | 403 or 404 | 200 with data |
| POST | Mass assignment, injection | Extra fields ignored or rejected | Privileged fields accepted |
| PUT | Overwriting another user's object | 403 | 200 with changes |
| PATCH | Changing privileged fields | Only allowed fields change | Role or ID changed |
| DELETE | Deleting another user's object | 403 | 204 |
| OPTIONS | Allowed methods, CORS | Only needed methods listed, origin checked | Any origin reflected with credentials |
| HEAD | Auth consistency, fingerprinting | Same auth as GET, no stack details | 200 where GET returns 403 |

---

## 🔗 References

- [MDN: HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 6902: JSON Patch](https://www.rfc-editor.org/rfc/rfc6902)
- [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x00-header/)
