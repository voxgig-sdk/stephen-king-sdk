# Typed models for the StephenKing SDK.
#
# GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
# params (op.<name>.points[].args.params[]). Field/param types come from the
# canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
# @voxgig/apidef VALID_CANON). Do not edit by hand.

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class Book:
    id: Optional[int] = None
    isbn: Optional[str] = None
    page: Optional[int] = None
    publisher: Optional[str] = None
    title: Optional[str] = None
    year: Optional[int] = None


@dataclass
class BookLoadMatch:
    id: int


@dataclass
class BookListMatch:
    id: Optional[int] = None
    isbn: Optional[str] = None
    page: Optional[int] = None
    publisher: Optional[str] = None
    title: Optional[str] = None
    year: Optional[int] = None


@dataclass
class Short:
    collection: Optional[str] = None
    id: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    year: Optional[int] = None


@dataclass
class ShortLoadMatch:
    id: int


@dataclass
class ShortListMatch:
    collection: Optional[str] = None
    id: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    year: Optional[int] = None


@dataclass
class Villain:
    gender: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    note: Optional[str] = None
    status: Optional[str] = None
    work: Optional[str] = None


@dataclass
class VillainLoadMatch:
    id: int


@dataclass
class VillainListMatch:
    gender: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    note: Optional[str] = None
    status: Optional[str] = None
    work: Optional[str] = None

