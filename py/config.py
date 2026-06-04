# StephenKing SDK configuration


def make_config():
    return {
        "main": {
            "name": "StephenKing",
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
            "req": False,
            "type": "`$INTEGER`",
            "active": True,
            "index$": 0,
          },
          {
            "name": "isbn",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 1,
          },
          {
            "name": "page",
            "req": False,
            "type": "`$INTEGER`",
            "active": True,
            "index$": 2,
          },
          {
            "name": "publisher",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 3,
          },
          {
            "name": "title",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 4,
          },
          {
            "name": "year",
            "req": False,
            "type": "`$INTEGER`",
            "active": True,
            "index$": 5,
          },
        ],
        "name": "book",
        "op": {
          "list": {
            "name": "list",
            "points": [
              {
                "method": "GET",
                "orig": "/api/books",
                "parts": [
                  "api",
                  "books",
                ],
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "active": True,
                "args": {},
                "select": {},
                "index$": 0,
              },
            ],
            "input": "data",
            "key$": "list",
          },
          "load": {
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 0,
              },
            ],
            "input": "data",
            "key$": "load",
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
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 0,
          },
          {
            "name": "id",
            "req": False,
            "type": "`$INTEGER`",
            "active": True,
            "index$": 1,
          },
          {
            "name": "title",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 2,
          },
          {
            "name": "type",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 3,
          },
          {
            "name": "year",
            "req": False,
            "type": "`$INTEGER`",
            "active": True,
            "index$": 4,
          },
        ],
        "name": "short",
        "op": {
          "list": {
            "name": "list",
            "points": [
              {
                "method": "GET",
                "orig": "/api/shorts",
                "parts": [
                  "api",
                  "shorts",
                ],
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "active": True,
                "args": {},
                "select": {},
                "index$": 0,
              },
            ],
            "input": "data",
            "key$": "list",
          },
          "load": {
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 0,
              },
            ],
            "input": "data",
            "key$": "load",
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
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 0,
          },
          {
            "name": "id",
            "req": False,
            "type": "`$INTEGER`",
            "active": True,
            "index$": 1,
          },
          {
            "name": "name",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 2,
          },
          {
            "name": "note",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 3,
          },
          {
            "name": "status",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 4,
          },
          {
            "name": "work",
            "req": False,
            "type": "`$STRING`",
            "active": True,
            "index$": 5,
          },
        ],
        "name": "villain",
        "op": {
          "list": {
            "name": "list",
            "points": [
              {
                "method": "GET",
                "orig": "/api/villains",
                "parts": [
                  "api",
                  "villains",
                ],
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body`",
                },
                "active": True,
                "args": {},
                "select": {},
                "index$": 0,
              },
            ],
            "input": "data",
            "key$": "list",
          },
          "load": {
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
                      "active": True,
                    },
                  ],
                },
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
                "active": True,
                "index$": 0,
              },
            ],
            "input": "data",
            "key$": "load",
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
    },
    }
