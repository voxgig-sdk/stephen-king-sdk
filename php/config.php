<?php
declare(strict_types=1);

// StephenKing SDK configuration

class StephenKingConfig
{
    /** @var array<string,mixed>|null */
    private static ?array $shared_config = null;

    /**
     * Return the process-wide config, built once on first use. The SDK reads
     * the config on every request and never writes to it, so one instance is
     * shared by every client rather than rebuilt per client.
     *
     * PHP arrays are copy-on-write, so callers that do mutate the result get
     * their own copy and cannot disturb the shared one.
     */
    public static function shared_config(): array
    {
        if (self::$shared_config === null) {
            self::$shared_config = self::make_config();
        }
        return self::$shared_config;
    }

    /**
     * Build a fresh, fully materialised config array. Every call rebuilds the
     * whole structure, so prefer shared_config unless you need a private copy.
     */
    public static function make_config(): array
    {
        return [
            "main" => [
                "name" => "StephenKing",
                "slug" => "stephen-king",
                "version" => "0.0.1",
                "target" => "php",
            ],
            "feature" => [
                "test" => [
          'options' => [
            'active' => false,
          ],
          'transport' => 'base',
        ],
            ],
            "options" => [
                "base" => "https://stephen-king-api.onrender.com",
                "headers" => [
          'content-type' => 'application/json',
        ],
                "entity" => [
                    "book" => [],
                    "short" => [],
                    "villain" => [],
                ],
            ],
            "entity" => [
        'book' => [
          'fields' => [
            [
              'name' => 'id',
              'short' => 'Unique identifier for the book',
              'type' => '`$INTEGER`',
            ],
            [
              'name' => 'isbn',
              'short' => 'ISBN of the book',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'pages',
              'short' => 'Number of pages',
              'type' => '`$INTEGER`',
            ],
            [
              'name' => 'publisher',
              'short' => 'Publisher of the book',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'title',
              'short' => 'Title of the book',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'year',
              'short' => 'Year of publication',
              'type' => '`$INTEGER`',
            ],
          ],
          'name' => 'book',
          'op' => [
            'list' => [
              'input' => 'data',
              'name' => 'list',
              'points' => [
                [
                  'args' => [],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/api/books',
                  'parts' => [
                    'api',
                    'books',
                  ],
                  'select' => [],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                ],
              ],
            ],
            'load' => [
              'input' => 'data',
              'name' => 'load',
              'points' => [
                [
                  'args' => [
                    'params' => [
                      [
                        'example' => 19,
                        'kind' => 'param',
                        'name' => 'id',
                        'orig' => 'id',
                        'reqd' => true,
                        'type' => '`$INTEGER`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/api/book/{id}',
                  'parts' => [
                    'api',
                    'book',
                    '{id}',
                  ],
                  'select' => [
                    'exist' => [
                      'id',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                ],
              ],
            ],
          ],
          'relations' => [
            'ancestors' => [],
          ],
        ],
        'short' => [
          'fields' => [
            [
              'name' => 'collection',
              'short' => 'Collection the short story appears in',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'id',
              'short' => 'Unique identifier for the short story',
              'type' => '`$INTEGER`',
            ],
            [
              'name' => 'title',
              'short' => 'Title of the short story',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'type',
              'short' => 'Type of short story',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'year',
              'short' => 'Year of publication',
              'type' => '`$INTEGER`',
            ],
          ],
          'name' => 'short',
          'op' => [
            'list' => [
              'input' => 'data',
              'name' => 'list',
              'points' => [
                [
                  'args' => [],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/api/shorts',
                  'parts' => [
                    'api',
                    'shorts',
                  ],
                  'select' => [],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                ],
              ],
            ],
            'load' => [
              'input' => 'data',
              'name' => 'load',
              'points' => [
                [
                  'args' => [
                    'params' => [
                      [
                        'example' => 19,
                        'kind' => 'param',
                        'name' => 'id',
                        'orig' => 'id',
                        'reqd' => true,
                        'type' => '`$INTEGER`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/api/short/{id}',
                  'parts' => [
                    'api',
                    'short',
                    '{id}',
                  ],
                  'select' => [
                    'exist' => [
                      'id',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                ],
              ],
            ],
          ],
          'relations' => [
            'ancestors' => [],
          ],
        ],
        'villain' => [
          'fields' => [
            [
              'name' => 'gender',
              'short' => 'Gender of the villain',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'id',
              'short' => 'Unique identifier for the villain',
              'type' => '`$INTEGER`',
            ],
            [
              'name' => 'name',
              'short' => 'Name of the villain',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'notes',
              'short' => 'Additional notes about the villain',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'status',
              'short' => 'Current status of the villain',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'work',
              'short' => 'Book or story the villain appears in',
              'type' => '`$STRING`',
            ],
          ],
          'name' => 'villain',
          'op' => [
            'list' => [
              'input' => 'data',
              'name' => 'list',
              'points' => [
                [
                  'args' => [],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/api/villains',
                  'parts' => [
                    'api',
                    'villains',
                  ],
                  'select' => [],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                ],
              ],
            ],
            'load' => [
              'input' => 'data',
              'name' => 'load',
              'points' => [
                [
                  'args' => [
                    'params' => [
                      [
                        'example' => 19,
                        'kind' => 'param',
                        'name' => 'id',
                        'orig' => 'id',
                        'reqd' => true,
                        'type' => '`$INTEGER`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/api/villain/{id}',
                  'parts' => [
                    'api',
                    'villain',
                    '{id}',
                  ],
                  'select' => [
                    'exist' => [
                      'id',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body`',
                  ],
                ],
              ],
            ],
          ],
          'relations' => [
            'ancestors' => [],
          ],
        ],
      ],
        ];
    }


    public static function make_feature(string $name)
    {
        require_once __DIR__ . '/features.php';
        return StephenKingFeatures::make_feature($name);
    }
}
