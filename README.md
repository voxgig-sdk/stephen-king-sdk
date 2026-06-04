# StephenKing SDK

Look up Stephen King's books, short stories, and villains by ID

> TypeScript, Python, PHP, Golang, Ruby, Lua SDKs, a CLI, an interactive REPL, and an MCP server for AI agents — all generated from one OpenAPI spec by [@voxgig/sdkgen](https://github.com/voxgig/sdkgen).

## About Stephen King API

The [Stephen King API](https://stephen-king-api.onrender.com) is a small, community-run REST service that catalogues Stephen King's literary universe. It is built and hosted by [Hunter Van Lear](https://github.com/hvanlear) on Render, and is also indexed on [Free Public APIs](https://freepublicapis.com/stephen-king-api).

What you get from the API:

- Books — id, `Year`, `Title`, `handle`, `Publisher`, `ISBN`, `Pages`, `Notes`, related `villains`, `created_at`.
- Short stories — id, `title`, `type`, `handle`, `originallyPublishedIn`, `collectedIn`, `notes`, `year`, related `villains`, `created_at`.
- Villains — id, `name`, `gender`, `status`, `types_id`, `notes`, related `books` and `shorts`, `created_at`.
- List endpoints support optional pagination via `page` and `limit` query parameters (used together; `limit` capped at 100).

The API is read-only (GET requests only), returns JSON, and requires no authentication. CORS is enabled, so browser clients can call it directly. As a free service hosted on Render's free tier, cold-start latency on first request is common; no formal rate limits are published.

## Try it

**TypeScript**
```bash
npm install stephen-king
```

**Python**
```bash
pip install stephen-king-sdk
```

**PHP**
```bash
composer require voxgig/stephen-king-sdk
```

**Golang**
```bash
go get github.com/voxgig-sdk/stephen-king-sdk/go
```

**Ruby**
```bash
gem install stephen-king-sdk
```

**Lua**
```bash
luarocks install stephen-king-sdk
```

## 30-second quickstart

### TypeScript

```ts
import { StephenKingSDK } from 'stephen-king'

const client = new StephenKingSDK({})

// List all books
const books = await client.Book().list()
```

See the [TypeScript README](ts/README.md) for the
full guide, or scroll down for the same example in other languages.

## What's in the box

| Surface | Use it for | Path |
| --- | --- | --- |
| **SDK** (TypeScript, Python, PHP, Golang, Ruby, Lua) | App integration | `ts/` `py/` `php/` `go/` `rb/` `lua/` |
| **CLI** | Scripts, CI, ops, one-off API calls | `go-cli/` |
| **MCP server** | AI agents (Claude, Cursor, Cline) | `go-mcp/` |

## Use it from an AI agent (MCP)

The generated MCP server exposes every operation in this SDK as an
[MCP](https://modelcontextprotocol.io) tool that Claude, Cursor or Cline
can call directly. Build and register it:

```bash
cd go-mcp && go build -o stephen-king-mcp .
```

Then add it to your agent's MCP config (Claude Desktop, Cursor, etc.):

```json
{
  "mcpServers": {
    "stephen-king": {
      "command": "/abs/path/to/stephen-king-mcp"
    }
  }
}
```

## Entities

The API exposes 3 entities:

| Entity | Description | API path |
| --- | --- | --- |
| **Book** | A Stephen King book entry with bibliographic fields (title, year, publisher, ISBN, pages) and linked villains; available at `/api/books` and `/api/books/{id}`. | `/api/books` |
| **Short** | A Stephen King short story with title, type, year, original publication, collection it appears in, and linked villains; available at `/api/shorts` and `/api/short/{id}`. | `/api/shorts` |
| **Villain** | An antagonist or monster from King's works with name, gender, status, notes, and back-references to the books and shorts they appear in; available at `/api/villains` and `/api/villain/{id}`. | `/api/villains` |

Each entity supports the following operations where available: **load**,
**list**, **create**, **update**, and **remove**.

## Quickstart in other languages

### Python

```python
from stephenking_sdk import StephenKingSDK

client = StephenKingSDK({})

# List all books
books, err = client.Book(None).list(None, None)

# Load a specific book
book, err = client.Book(None).load(
    {"id": "example_id"}, None
)
```

### PHP

```php
<?php
require_once 'stephenking_sdk.php';

$client = new StephenKingSDK([]);

// List all books
[$books, $err] = $client->Book(null)->list(null, null);

// Load a specific book
[$book, $err] = $client->Book(null)->load(
    ["id" => "example_id"], null
);
```

### Golang

```go
import sdk "github.com/voxgig-sdk/stephen-king-sdk/go"

client := sdk.NewStephenKingSDK(map[string]any{})

// List all books
books, err := client.Book(nil).List(nil, nil)
```

### Ruby

```ruby
require_relative "StephenKing_sdk"

client = StephenKingSDK.new({})

# List all books
books, err = client.Book(nil).list(nil, nil)

# Load a specific book
book, err = client.Book(nil).load(
  { "id" => "example_id" }, nil
)
```

### Lua

```lua
local sdk = require("stephen-king_sdk")

local client = sdk.new({})

-- List all books
local books, err = client:Book(nil):list(nil, nil)

-- Load a specific book
local book, err = client:Book(nil):load(
  { id = "example_id" }, nil
)
```

## Unit testing in offline mode

Every SDK ships a test mode that swaps the HTTP transport for an
in-memory mock, so unit tests run offline.

### TypeScript

```ts
const client = StephenKingSDK.test()
const result = await client.Book().load({ id: 'test01' })
// result.ok === true, result.data contains mock data
```

### Python

```python
client = StephenKingSDK.test(None, None)
result, err = client.Book(None).load(
    {"id": "test01"}, None
)
```

### PHP

```php
$client = StephenKingSDK::test(null, null);
[$result, $err] = $client->Book(null)->load(
    ["id" => "test01"], null
);
```

### Golang

```go
client := sdk.TestSDK(nil, nil)
result, err := client.Book(nil).Load(
    map[string]any{"id": "test01"}, nil,
)
```

### Ruby

```ruby
client = StephenKingSDK.test(nil, nil)
result, err = client.Book(nil).load(
  { "id" => "test01" }, nil
)
```

### Lua

```lua
local client = sdk.test(nil, nil)
local result, err = client:Book(nil):load(
  { id = "test01" }, nil
)
```

## How it works

Every SDK call runs the same five-stage pipeline:

1. **Point** — resolve the API endpoint from the operation definition.
2. **Spec** — build the HTTP specification (URL, method, headers, body).
3. **Request** — send the HTTP request.
4. **Response** — receive and parse the response.
5. **Result** — extract the result data for the caller.

A feature hook fires at each stage (e.g. `PrePoint`, `PreSpec`,
`PreRequest`), so features can inspect or modify the pipeline without
forking the SDK.

### Features

| Feature | Purpose |
| --- | --- |
| **TestFeature** | In-memory mock transport for testing without a live server |

Pass custom features via the `extend` option at construction time.

### Direct and Prepare

For endpoints the entity model doesn't cover, use the low-level methods:

- **`direct(fetchargs)`** — build and send an HTTP request in one step.
- **`prepare(fetchargs)`** — build the request without sending it.

Both accept a map with `path`, `method`, `params`, `query`,
`headers`, and `body`. See the [How-to guides](#how-to-guides) below.

## How-to guides

### Make a direct API call

When the entity interface does not cover an endpoint, use `direct`:

**TypeScript:**
```ts
const result = await client.direct({
  path: '/api/resource/{id}',
  method: 'GET',
  params: { id: 'example' },
})
console.log(result.data)
```

**Python:**
```python
result, err = client.direct({
    "path": "/api/resource/{id}",
    "method": "GET",
    "params": {"id": "example"},
})
```

**PHP:**
```php
[$result, $err] = $client->direct([
    "path" => "/api/resource/{id}",
    "method" => "GET",
    "params" => ["id" => "example"],
]);
```

**Go:**
```go
result, err := client.Direct(map[string]any{
    "path":   "/api/resource/{id}",
    "method": "GET",
    "params": map[string]any{"id": "example"},
})
```

**Ruby:**
```ruby
result, err = client.direct({
  "path" => "/api/resource/{id}",
  "method" => "GET",
  "params" => { "id" => "example" },
})
```

**Lua:**
```lua
local result, err = client:direct({
  path = "/api/resource/{id}",
  method = "GET",
  params = { id = "example" },
})
```

## Per-language documentation

- [TypeScript](ts/README.md)
- [Python](py/README.md)
- [PHP](php/README.md)
- [Golang](go/README.md)
- [Ruby](rb/README.md)
- [Lua](lua/README.md)

## Using the Stephen King API

- Upstream: [https://stephen-king-api.onrender.com](https://stephen-king-api.onrender.com)
- API docs: [https://stephen-king-api.onrender.com/docs](https://stephen-king-api.onrender.com/docs)

- Described by the maintainer as "free, open-source"; no formal licence text is published alongside the API.
- Created and maintained by Hunter Van Lear ([hvanlear](https://github.com/hvanlear) on GitHub) — see the [Stephen-King-API repository](https://github.com/hvanlear/Stephen-King-API).
- Stephen King's works and characters remain the intellectual property of their respective rights holders; treat returned data as catalogue metadata for fan/educational use.
- No specific attribution requirement is stated, but a courtesy credit to the project is appropriate.

---

Generated from the Stephen King API OpenAPI spec by [@voxgig/sdkgen](https://github.com/voxgig/sdkgen).
