
import { BaseFeature } from './feature/base/BaseFeature'
import { TestFeature } from './feature/test/TestFeature'



const FEATURE_CLASS: Record<string, typeof BaseFeature> = {
   test: TestFeature,

}


class Config {

  makeFeature(this: any, fn: string) {
    const fc = FEATURE_CLASS[fn]
    const fi = new fc()
    // TODO: errors etc
    return fi
  }

  // False for a feature added at runtime via options.extend (station's
  // adopt path) - the constructor uses this to skip makeFeature for names
  // no generated class backs.
  hasFeature(this: any, fn: string) {
    return null != FEATURE_CLASS[fn]
  }


  main = {
    name: 'StephenKing',
        slug: "stephen-king",
    version: "0.0.1",
    target: "ts",

  }


  feature = {
     test:     {
      "options": {
        "active": false
      },
      "transport": "base"
    },

  }


  options = {
    base: "https://stephen-king-api.onrender.com",

    headers: {
      "content-type": "application/json"
    },

    entity: {
      
      book: {
      },

      short: {
      },

      villain: {
      },

    }
  }


  entity = {
    "book": {
      "fields": [
        {
          "name": "id",
          "short": "Unique identifier for the book",
          "type": "`$INTEGER`"
        },
        {
          "name": "isbn",
          "short": "ISBN of the book",
          "type": "`$STRING`"
        },
        {
          "name": "pages",
          "short": "Number of pages",
          "type": "`$INTEGER`"
        },
        {
          "name": "publisher",
          "short": "Publisher of the book",
          "type": "`$STRING`"
        },
        {
          "name": "title",
          "short": "Title of the book",
          "type": "`$STRING`"
        },
        {
          "name": "year",
          "short": "Year of publication",
          "type": "`$INTEGER`"
        }
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
                "books"
              ],
              "select": {},
              "transform": {
                "req": "`reqdata`",
                "res": "`body`"
              }
            }
          ]
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
                    "reqd": true,
                    "type": "`$INTEGER`"
                  }
                ]
              },
              "kind": "http",
              "method": "GET",
              "orig": "/api/book/{id}",
              "parts": [
                "api",
                "book",
                "{id}"
              ],
              "select": {
                "exist": [
                  "id"
                ]
              },
              "transform": {
                "req": "`reqdata`",
                "res": "`body`"
              }
            }
          ]
        }
      },
      "relations": {
        "ancestors": []
      }
    },
    "short": {
      "fields": [
        {
          "name": "collection",
          "short": "Collection the short story appears in",
          "type": "`$STRING`"
        },
        {
          "name": "id",
          "short": "Unique identifier for the short story",
          "type": "`$INTEGER`"
        },
        {
          "name": "title",
          "short": "Title of the short story",
          "type": "`$STRING`"
        },
        {
          "name": "type",
          "short": "Type of short story",
          "type": "`$STRING`"
        },
        {
          "name": "year",
          "short": "Year of publication",
          "type": "`$INTEGER`"
        }
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
                "shorts"
              ],
              "select": {},
              "transform": {
                "req": "`reqdata`",
                "res": "`body`"
              }
            }
          ]
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
                    "reqd": true,
                    "type": "`$INTEGER`"
                  }
                ]
              },
              "kind": "http",
              "method": "GET",
              "orig": "/api/short/{id}",
              "parts": [
                "api",
                "short",
                "{id}"
              ],
              "select": {
                "exist": [
                  "id"
                ]
              },
              "transform": {
                "req": "`reqdata`",
                "res": "`body`"
              }
            }
          ]
        }
      },
      "relations": {
        "ancestors": []
      }
    },
    "villain": {
      "fields": [
        {
          "name": "gender",
          "short": "Gender of the villain",
          "type": "`$STRING`"
        },
        {
          "name": "id",
          "short": "Unique identifier for the villain",
          "type": "`$INTEGER`"
        },
        {
          "name": "name",
          "short": "Name of the villain",
          "type": "`$STRING`"
        },
        {
          "name": "notes",
          "short": "Additional notes about the villain",
          "type": "`$STRING`"
        },
        {
          "name": "status",
          "short": "Current status of the villain",
          "type": "`$STRING`"
        },
        {
          "name": "work",
          "short": "Book or story the villain appears in",
          "type": "`$STRING`"
        }
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
                "villains"
              ],
              "select": {},
              "transform": {
                "req": "`reqdata`",
                "res": "`body`"
              }
            }
          ]
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
                    "reqd": true,
                    "type": "`$INTEGER`"
                  }
                ]
              },
              "kind": "http",
              "method": "GET",
              "orig": "/api/villain/{id}",
              "parts": [
                "api",
                "villain",
                "{id}"
              ],
              "select": {
                "exist": [
                  "id"
                ]
              },
              "transform": {
                "req": "`reqdata`",
                "res": "`body`"
              }
            }
          ]
        }
      },
      "relations": {
        "ancestors": []
      }
    }
  }
}


const config = new Config()

export {
  config
}

