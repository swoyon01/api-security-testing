# 01 · Burp Suite Community Setup

> Burp Suite is an intercepting proxy. It sits between your browser and the server, so you can see, change, and resend every request. It is the main tool for this journey.

---

## 1. Install

1. Download **Burp Suite Community Edition** from the official PortSwigger site (`portswigger.net/burp/communitydownload`).
2. Install it and start it. Choose **Temporary project** and **Use Burp defaults** for a quick start.

## 2. Check the proxy listener

1. Go to **Proxy → Proxy settings** (or **Settings → Tools → Proxy**).
2. Confirm there is a listener on **127.0.0.1:8080**.

| Setting | Value |
|---------|-------|
| Listener address | `127.0.0.1` |
| Port | `8080` |

## 3. Route Firefox through Burp

Use FoxyProxy (see [`02-firefox-foxyproxy.md`](02-firefox-foxyproxy.md) if you have it, or set it manually):

1. **Settings → Network Settings → Manual proxy configuration**
2. HTTP Proxy: `127.0.0.1`, Port: `8080`
3. Tick **Also use this proxy for HTTPS**.

## 4. Install the Burp CA certificate

Without this, HTTPS sites show certificate warnings and Burp cannot read the traffic.

1. With the proxy on, open `http://burp` in Firefox.
2. Click **CA Certificate** and save the file.
3. In Firefox: **Settings → Privacy & Security → Certificates → View Certificates → Authorities → Import**, then select the file. Tick **Trust this CA to identify websites**.

## 5. Test the setup

1. In Burp, open **Proxy → Intercept** and turn **Intercept is on**.
2. In Firefox, visit `https://jsonplaceholder.typicode.com/posts/1`.
3. Burp should catch the request. Click **Forward** to let it through.
4. Turn intercept off when you are done.

**Expected result:** the request appears in **Proxy → HTTP history**, and the page loads after you forward it.

## 6. The tabs you will use most

| Tab | Use it for |
|-----|-----------|
| **Proxy → HTTP history** | Review every request your browser sent |
| **Repeater** | Resend one request with changes, the main testing tool |
| **Intruder** | Automate changes (IDs, passwords), use carefully in labs only |
| **Target → Scope** | Limit traffic to the lab host so you don't capture other sites |
| **Logger** / **Proxy history** filters | Find API calls quickly by filtering on `/api/` |

## 7. Setup checklist

- [x] Burp Community starts and the proxy listens on `127.0.0.1:8080`
- [x] Firefox uses the proxy
- [x] CA certificate is installed and trusted
- [x] A request to `jsonplaceholder.typicode.com` shows in HTTP history
- [x] A request sent to Repeater can be resent with a changed value

---

## 🔗 References
- [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload)
- [PortSwigger: Configuring a browser to work with Burp](https://portswigger.net/burp/documentation/desktop/getting-started/proxy-setup)
