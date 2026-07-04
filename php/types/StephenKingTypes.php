<?php
declare(strict_types=1);

// Typed models for the StephenKing SDK.
//
// GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
// params (op.<name>.points[].args.params[]). Field/param types come from the
// canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
// @voxgig/apidef VALID_CANON). Do not edit by hand.
//
// These are documentation-grade value objects (PHP 8 typed properties),
// registered on the composer classmap autoload. The SDK boundary exchanges
// assoc-arrays; these classes name the shapes for tooling and typed callers.

/** Book entity data model. */
class Book
{
    public ?int $id = null;
    public ?string $isbn = null;
    public ?int $page = null;
    public ?string $publisher = null;
    public ?string $title = null;
    public ?int $year = null;
}

/** Request payload for Book#load. */
class BookLoadMatch
{
    public int $id;
}

/** Match filter for Book#list (any subset of Book fields). */
class BookListMatch
{
    public ?int $id = null;
    public ?string $isbn = null;
    public ?int $page = null;
    public ?string $publisher = null;
    public ?string $title = null;
    public ?int $year = null;
}

/** Short entity data model. */
class Short
{
    public ?string $collection = null;
    public ?int $id = null;
    public ?string $title = null;
    public ?string $type = null;
    public ?int $year = null;
}

/** Request payload for Short#load. */
class ShortLoadMatch
{
    public int $id;
}

/** Match filter for Short#list (any subset of Short fields). */
class ShortListMatch
{
    public ?string $collection = null;
    public ?int $id = null;
    public ?string $title = null;
    public ?string $type = null;
    public ?int $year = null;
}

/** Villain entity data model. */
class Villain
{
    public ?string $gender = null;
    public ?int $id = null;
    public ?string $name = null;
    public ?string $note = null;
    public ?string $status = null;
    public ?string $work = null;
}

/** Request payload for Villain#load. */
class VillainLoadMatch
{
    public int $id;
}

/** Match filter for Villain#list (any subset of Villain fields). */
class VillainListMatch
{
    public ?string $gender = null;
    public ?int $id = null;
    public ?string $name = null;
    public ?string $note = null;
    public ?string $status = null;
    public ?string $work = null;
}

