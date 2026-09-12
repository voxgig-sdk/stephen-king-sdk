"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.FEATURE_PLUGINS = exports.config = void 0;
const TestFeature_1 = require("./feature/test/TestFeature");
const FEATURE_CLASS = {
    test: TestFeature_1.TestFeature,
};
// Per-feature plugin DEFINITIONS (voxgig/plugin `Definition` values), from
// the model's active plugin groups. A feature that takes a `plugins` option
// (secrets over sekreto) reads its own entry; a feature with no plugins has
// none. Named imports above make each definition statically reachable, so
// an SDK carries exactly the plugin modules its model selects — the same
// leanness the old side-effect registry imports bought, without a registry.
const FEATURE_PLUGINS = {};
exports.FEATURE_PLUGINS = FEATURE_PLUGINS;
class Config {
    makeFeature(fn) {
        const fc = FEATURE_CLASS[fn];
        const fi = new fc();
        // TODO: errors etc
        return fi;
    }
    // False for a feature added at runtime via options.extend (station's
    // adopt path) - the constructor uses this to skip makeFeature for names
    // no generated class backs.
    hasFeature(fn) {
        return null != FEATURE_CLASS[fn];
    }
    main = {
        name: 'StephenKing',
        slug: "stephen-king",
        version: "0.0.1",
        target: "ts",
    };
    feature = {
        test: {
            "options": {
                "active": false
            },
            "transport": "base"
        },
    };
    options = {
        base: "https://stephen-king-api.onrender.com",
        headers: {
            "content-type": "application/json"
        },
        entity: {
            book: {},
            short: {},
            villain: {},
        }
    };
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
            "id": {
                "field": "id",
                "name": "id"
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
                                    "lit": "api"
                                },
                                {
                                    "lit": "books"
                                }
                            ],
                            "select": {},
                            "transform": {
                                "req": "`reqdata`",
                                "res": "`body`"
                            },
                            "parts": [
                                "api",
                                "books"
                            ]
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
                            "segments": [
                                {
                                    "lit": "api"
                                },
                                {
                                    "lit": "book"
                                },
                                {
                                    "var": "id"
                                }
                            ],
                            "select": {
                                "exist": [
                                    "id"
                                ]
                            },
                            "transform": {
                                "req": "`reqdata`",
                                "res": "`body`"
                            },
                            "parts": [
                                "api",
                                "book",
                                "{id}"
                            ]
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
            "id": {
                "field": "id",
                "name": "id"
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
                                    "lit": "api"
                                },
                                {
                                    "lit": "shorts"
                                }
                            ],
                            "select": {},
                            "transform": {
                                "req": "`reqdata`",
                                "res": "`body`"
                            },
                            "parts": [
                                "api",
                                "shorts"
                            ]
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
                            "segments": [
                                {
                                    "lit": "api"
                                },
                                {
                                    "lit": "short"
                                },
                                {
                                    "var": "id"
                                }
                            ],
                            "select": {
                                "exist": [
                                    "id"
                                ]
                            },
                            "transform": {
                                "req": "`reqdata`",
                                "res": "`body`"
                            },
                            "parts": [
                                "api",
                                "short",
                                "{id}"
                            ]
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
            "id": {
                "field": "id",
                "name": "id"
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
                                    "lit": "api"
                                },
                                {
                                    "lit": "villains"
                                }
                            ],
                            "select": {},
                            "transform": {
                                "req": "`reqdata`",
                                "res": "`body`"
                            },
                            "parts": [
                                "api",
                                "villains"
                            ]
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
                            "segments": [
                                {
                                    "lit": "api"
                                },
                                {
                                    "lit": "villain"
                                },
                                {
                                    "var": "id"
                                }
                            ],
                            "select": {
                                "exist": [
                                    "id"
                                ]
                            },
                            "transform": {
                                "req": "`reqdata`",
                                "res": "`body`"
                            },
                            "parts": [
                                "api",
                                "villain",
                                "{id}"
                            ]
                        }
                    ]
                }
            },
            "relations": {
                "ancestors": []
            }
        }
    };
}
const config = new Config();
exports.config = config;
//# sourceMappingURL=Config.js.map