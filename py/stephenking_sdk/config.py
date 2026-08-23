# StephenKing SDK configuration


_shared_config = None


def shared_config():
    """Return the process-wide config, built once on first use.

    The SDK reads the config on every request and never writes to it, so one
    instance is shared by every client rather than rebuilt per client.

    The returned dict is shared: treat it as read-only. Callers that need to
    mutate should use make_config, which always returns a fresh copy.
    """
    global _shared_config
    if _shared_config is None:
        _shared_config = make_config()
    return _shared_config


def make_config():
    """Build a fresh, fully materialised config dict.

    Every call rebuilds the whole structure, so prefer shared_config unless
    you need a private copy you intend to mutate.
    """
    return {
        "main": {
            "name": "StephenKing",
            "slug": "stephen-king",
            "version": "0.0.1",
            "target": "py",
        },
        "feature": {
            "test": {
        "options": {
          "active": False,
        },
      },
        },
        "options": {
            "base": "https://stephen-king-api.onrender.com",
            "headers": {
        "content-type": "application/json",
      },
            "entity": {
                "book": {},
                "short": {},
                "villain": {},
            },
        },
        "entity": {
      "book": {
        "fields": [
          {
            "name": "id",
            "short": "Unique identifier for the book",
            "type": "`$INTEGER`",
          },
          {
            "name": "isbn",
            "short": "ISBN of the book",
            "type": "`$STRING`",
          },
          {
            "name": "pages",
            "short": "Number of pages",
            "type": "`$INTEGER`",
          },
          {
            "name": "publisher",
            "short": "Publisher of the book",
            "type": "`$STRING`",
          },
          {
            "name": "title",
            "short": "Title of the book",
            "type": "`$STRING`",
          },
          {
            "name": "year",
            "short": "Year of publication",
            "type": "`$INTEGER`",
          },
        ],
        "name": "book",
        "op": {
          "list": {
            "input": "data",
            "name": "list",
            "points": [
              {
                "args": {},
                "kind": "http",
                "method": "GET",
                "orig": "/api/books",
                "parts": [
                  "api",
                  "books",
                ],
                "select": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "example": 19,
                      "kind": "param",
                      "name": "id",
                      "orig": "id",
                      "reqd": True,
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/api/book/{id}",
                "parts": [
                  "api",
                  "book",
                  "{id}",
                ],
                "select": {
                  "exist": [
                    "id",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
      "short": {
        "fields": [
          {
            "name": "collection",
            "short": "Collection the short story appears in",
            "type": "`$STRING`",
          },
          {
            "name": "id",
            "short": "Unique identifier for the short story",
            "type": "`$INTEGER`",
          },
          {
            "name": "title",
            "short": "Title of the short story",
            "type": "`$STRING`",
          },
          {
            "name": "type",
            "short": "Type of short story",
            "type": "`$STRING`",
          },
          {
            "name": "year",
            "short": "Year of publication",
            "type": "`$INTEGER`",
          },
        ],
        "name": "short",
        "op": {
          "list": {
            "input": "data",
            "name": "list",
            "points": [
              {
                "args": {},
                "kind": "http",
                "method": "GET",
                "orig": "/api/shorts",
                "parts": [
                  "api",
                  "shorts",
                ],
                "select": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "example": 19,
                      "kind": "param",
                      "name": "id",
                      "orig": "id",
                      "reqd": True,
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/api/short/{id}",
                "parts": [
                  "api",
                  "short",
                  "{id}",
                ],
                "select": {
                  "exist": [
                    "id",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
      "villain": {
        "fields": [
          {
            "name": "gender",
            "short": "Gender of the villain",
            "type": "`$STRING`",
          },
          {
            "name": "id",
            "short": "Unique identifier for the villain",
            "type": "`$INTEGER`",
          },
          {
            "name": "name",
            "short": "Name of the villain",
            "type": "`$STRING`",
          },
          {
            "name": "notes",
            "short": "Additional notes about the villain",
            "type": "`$STRING`",
          },
          {
            "name": "status",
            "short": "Current status of the villain",
            "type": "`$STRING`",
          },
          {
            "name": "work",
            "short": "Book or story the villain appears in",
            "type": "`$STRING`",
          },
        ],
        "name": "villain",
        "op": {
          "list": {
            "input": "data",
            "name": "list",
            "points": [
              {
                "args": {},
                "kind": "http",
                "method": "GET",
                "orig": "/api/villains",
                "parts": [
                  "api",
                  "villains",
                ],
                "select": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
          "load": {
            "input": "data",
            "name": "load",
            "points": [
              {
                "args": {
                  "params": [
                    {
                      "example": 19,
                      "kind": "param",
                      "name": "id",
                      "orig": "id",
                      "reqd": True,
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/api/villain/{id}",
                "parts": [
                  "api",
                  "villain",
                  "{id}",
                ],
                "select": {
                  "exist": [
                    "id",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
              },
            ],
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
    },
    }
