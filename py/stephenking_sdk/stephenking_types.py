# Typed models for the StephenKing SDK.
#
# GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
# params (op.<name>.points[].args.params[]). Field/param types come from the
# canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
# @voxgig/apidef VALID_CANON). Do not edit by hand.
#
# These are TypedDicts, not dataclasses: the SDK ops return/accept plain dicts
# at runtime, and a TypedDict IS a dict shape, so the types match the runtime.
# Optional (req:false) keys are modelled as TypedDict key-optionality
# (total=False), split into a required base + total=False subclass when a type
# has both required and optional keys.

from __future__ import annotations

from typing import TypedDict, Any


class Book(TypedDict, total=False):
    id: int
    isbn: str
    pages: int
    publisher: str
    title: str
    year: int


class BookLoadMatch(TypedDict):
    id: int


class BookListMatch(TypedDict, total=False):
    id: int
    isbn: str
    pages: int
    publisher: str
    title: str
    year: int


class Short(TypedDict, total=False):
    collection: str
    id: int
    title: str
    type: str
    year: int


class ShortLoadMatch(TypedDict):
    id: int


class ShortListMatch(TypedDict, total=False):
    collection: str
    id: int
    title: str
    type: str
    year: int


class Villain(TypedDict, total=False):
    gender: str
    id: int
    name: str
    notes: str
    status: str
    work: str


class VillainLoadMatch(TypedDict):
    id: int


class VillainListMatch(TypedDict, total=False):
    gender: str
    id: int
    name: str
    notes: str
    status: str
    work: str
