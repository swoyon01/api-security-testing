# 03 · curl Commands

> `curl` sends HTTP requests from the terminal. It is quick for repeating a request, for scripts, and for checking headers.

---

## Core options

| Option | Meaning | Example |
|--------|---------|---------|
| `-X` | Choose the method | `-X DELETE` |
| `-H` | Add a header | `-H "Authorization: Bearer TOKEN"` |
| `-d` | Send a body | `-d '{"name":"Jane"}'` |
| `-i` | Show response headers | `curl -i URL` |
| `-I` | Headers only (HEAD) | `curl -I URL` |
| `-v` | Verbose (full request and response) | `curl -v URL` |
| `-s` | Silent (no progress bar) | `curl -s URL` |
| `-o` | Save output to a file | `-o out.json` |
| `--proxy` | Send through Burp | `--proxy http://127.0.0.1:8080` |
| `-k` | Skip certificate checks (labs only) | `curl -k https://localhost:8443` |

## Practice commands (public API)

```bash
# GET
curl -i https://jsonplaceholder.typicode.com/posts/1

# POST with JSON body
curl -i -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"userId":1,"title":"Learning curl","body":"Testing POST"}'

# PUT
curl -i -X PUT https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"id":1,"userId":1,"title":"Updated","body":"Updated body"}'

# PATCH
curl -i -X PATCH https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Only the title changed"}'

# DELETE
curl -i -X DELETE https://jsonplaceholder.typicode.com/posts/1

# HEAD (headers only)
curl -I https://jsonplaceholder.typicode.com/posts/1

# OPTIONS (allowed methods)
curl -i -X OPTIONS https://jsonplaceholder.typicode.com/posts
```

## Testing with a token

```bash
TOKEN="paste-your-token-here"
curl -i http://localhost:8888/api/some-endpoint \
  -H "Authorization: Bearer $TOKEN"
```

Keep real tokens out of your notes and screenshots. Use a variable, as shown above.

## Read the output

- The first line is the status code, such as `HTTP/2 200`.
- `-i` shows headers. Look at `Content-Type`, `Allow`, and `Server`.
- Save the response to a file with `-o` when you want to inspect it later.

## Setup checklist

- [x] `curl --version` works in your terminal
- [x] GET, POST, PUT, PATCH, DELETE, and HEAD commands above all run
- [x] You can add an `Authorization` header to a request

---

## 🔗 References
- [curl manual](https://curl.se/docs/manpage.html)
