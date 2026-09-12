# StephenKing SDK configuration


# The sekreto plugin DEFINITIONS the model selected per feature, imported
# above by name from the modules the catalogue's active `plugin.def`
# entries declare. Handed to each feature (secrets builds its Sekreto
# with them): a provider kind not listed here is unknown to that SDK.
FEATURE_PLUGINS = {
}


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
        "transport": "base",
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
        "id": {
          "field": "id",
          "name": "id",
        },
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
                "segments": [
                  {
                    "lit": "api",
                  },
                  {
                    "lit": "books",
                  },
                ],
                "select": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "parts": [
                  "api",
                  "books",
                ],
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
                "segments": [
                  {
                    "lit": "api",
                  },
                  {
                    "lit": "book",
                  },
                  {
                    "var": "id",
                  },
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
                "parts": [
                  "api",
                  "book",
                  "{id}",
                ],
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
        "id": {
          "field": "id",
          "name": "id",
        },
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
                "segments": [
                  {
                    "lit": "api",
                  },
                  {
                    "lit": "shorts",
                  },
                ],
                "select": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "parts": [
                  "api",
                  "shorts",
                ],
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
                "segments": [
                  {
                    "lit": "api",
                  },
                  {
                    "lit": "short",
                  },
                  {
                    "var": "id",
                  },
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
                "parts": [
                  "api",
                  "short",
                  "{id}",
                ],
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
        "id": {
          "field": "id",
          "name": "id",
        },
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
                "segments": [
                  {
                    "lit": "api",
                  },
                  {
                    "lit": "villains",
                  },
                ],
                "select": {},
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "parts": [
                  "api",
                  "villains",
                ],
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
                "segments": [
                  {
                    "lit": "api",
                  },
                  {
                    "lit": "villain",
                  },
                  {
                    "var": "id",
                  },
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
                "parts": [
                  "api",
                  "villain",
                  "{id}",
                ],
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
