# 02 · API vs Website

> A **website** sends HTML pages to a browser. An **API** sends data, usually JSON, to a program. Both run on HTTP, but the way they are built, used, and attacked is different.

---

## Quick comparison

| Point | Website | API |
|-------|---------|-----|
| **Main output** | HTML, CSS, images | JSON or XML data |
| **Main client** | A web browser | Apps, scripts, other servers, mobile apps |
| **Who uses it** | People, through a screen | Programs, often without a screen |
| **Typical URL** | `/products`, `/login` | `/api/v1/products`, `/api/users/1` |
| **Authentication** | Login form, session cookie | Bearer tokens, API keys, JWT, OAuth |
| **Interface** | Buttons, forms, links | Endpoints, methods, parameters |
| **Usual attack surface** | XSS, CSRF, clickjacking, UI logic | BOLA, BFLA, mass assignment, excessive data |

---

## What is different for a tester

### 1. There is no user interface to hide things

On a website, the buttons only show what the developer wants you to see. An API has no buttons, so every endpoint is visible to anyone who finds it. A hidden admin button on a website may still be an open endpoint in the API.

**Test:** do not trust what the app shows. Map every endpoint in the API documentation or in the traffic.

### 2. Authorization is checked per request

Websites often check permissions on the page and in the menus. APIs need the server to check each object and each action. If the server checks only the login and forgets the object owner, BOLA is possible.

**Test:** use one account's token to request another account's data by changing IDs.

### 3. Data comes back in structured form

A website shows a rendered page. An API returns raw data, which can include fields the UI never displays, such as `internal_notes`, `password_hash`, or `is_admin`.

**Test:** compare what the UI shows with the full JSON response in Burp.

### 4. Input is often JSON, not form fields

Websites usually send form data. APIs send JSON objects, which can contain nested fields and extra properties. This creates mass assignment risks.

**Test:** add extra fields to a request body and see whether the server accepts them.

### 5. Clients are not always browsers

A browser enforces some rules, such as same-origin policy and CORS. Scripts and mobile apps do not, so a request that a browser blocks can still reach the API.

**Test:** send requests with `curl` or Burp, not only through the browser.

### 6. Many versions and hidden endpoints

Websites usually have one current version. APIs often keep old versions (`/api/v1/`, `/api/v2/`) and internal endpoints (`/internal/`, `/debug/`). Old versions may lack the security fixes added to the new one.

**Test:** check older versions of the same endpoint for missing authorization or rate limits.

### 7. Documentation is often public

Many APIs publish Swagger or OpenAPI files at paths such as `/swagger`, `/api-docs`, or `/openapi.json`. This gives you a map of the attack surface, which websites rarely provide.

**Test:** search for documentation paths, then import the file into Postman or Burp.

---

## Example: the same action on a website and an API

**On a website**, a user changes a password through a form:

```
POST /account/password
(form fields: current_password, new_password)
```

**Through the API**, the same action may be:

```http
PUT /api/v1/users/1042/password
Authorization: Bearer eyJhbGci...
Content-Type: application/json

{ "current_password": "old", "new_password": "new" }
```

**What to test in the API version:**
- Can user 1043 send a PUT to `/users/1042/password`? (BOLA)
- Can the body include `"role": "admin"` and be accepted? (Mass assignment)
- Does `/api/v1/users/1042/password` still work after the team moved to `/api/v2/`? (Old version)

---

## Key takeaways

- An API is the back end that website and mobile apps use to get and send data.
- Every API endpoint is a separate entry point. Test each one.
- Authorization must be checked on every request, not only at login.
- Documentation, old versions, and hidden endpoints are common sources of bugs.

---

## 🔗 References

- [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x00-header/)
- [MDN: Introduction to HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
