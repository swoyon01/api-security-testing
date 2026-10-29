# 02 · Postman Setup

> Postman is the tool for building and sending API requests in an organized way. You use it to explore an API before you test it in Burp.

---

## 1. Install

1. Download **Postman** from `postman.com/downloads` and install it.
2. Sign in or use Postman without an account (Postman offers both).

## 2. Core ideas

| Term | Meaning |
|------|---------|
| **Collection** | A folder of saved requests for one API |
| **Environment** | A set of variables for one target, such as `dev` or `lab` |
| **Variable** | A value you reuse, written as `{{baseUrl}}` |
| **Tests** | JavaScript that checks the response automatically |

## 3. Create a collection

1. Click **New → Collection** and name it `API Practice`.
2. Add a folder called `jsonplaceholder` for the public practice API.
3. Save these requests in the folder:

| Name | Method | URL |
|------|--------|-----|
| Get post | GET | `https://jsonplaceholder.typicode.com/posts/1` |
| Create post | POST | `https://jsonplaceholder.typicode.com/posts` |
| Update post | PUT | `https://jsonplaceholder.typicode.com/posts/1` |
| Patch post | PATCH | `https://jsonplaceholder.typicode.com/posts/1` |
| Delete post | DELETE | `https://jsonplaceholder.typicode.com/posts/1` |

## 4. Create an environment

1. Click **Environments → Create**, name it `lab`.
2. Add a variable:

| Variable | Initial value |
|----------|---------------|
| `baseUrl` | `https://jsonplaceholder.typicode.com` |

3. Change the request URLs to `{{baseUrl}}/posts/1`.
4. Select the `lab` environment in the top-right dropdown.

**Why it matters:** for crAPI you only change `baseUrl` to `http://localhost:8888`, and every request follows.

## 5. Add a simple test

In a request, open the **Tests** tab and add:

```javascript
pm.test("status is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("response is JSON with an id", function () {
  const body = pm.response.json();
  pm.expect(body).to.have.property("id");
});
```

Send the request. Both tests should pass.

## 6. Send traffic through Burp (optional)

1. In Postman: **Settings → Proxy → Use custom proxy configuration**.
2. Proxy: `http://127.0.0.1:8080`.
3. Turn off SSL certificate verification only for local labs, and only if needed.

**Note:** keep this off for public APIs unless you need to capture the traffic.

## 7. Setup checklist

- [x] Postman is installed and opens
- [x] A `API Practice` collection exists with the five methods
- [x] The `lab` environment uses `{{baseUrl}}`
- [x] A test passes on the GET request
- [x] Requests can be sent through Burp (optional)

---

## 🔗 References
- [Postman Learning Center](https://learning.postman.com/)
