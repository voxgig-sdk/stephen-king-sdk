// Typed models for the StephenKing SDK.
//
// GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
// params (op.<name>.points[].args.params[]). Field/param types come from the
// canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
// @voxgig/apidef VALID_CANON). Do not edit by hand.

export interface Book {
  id?: number
  isbn?: string
  page?: number
  publisher?: string
  title?: string
  year?: number
}

export interface BookLoadMatch {
  id: number
}

export type BookListMatch = Partial<Book>

export interface Short {
  collection?: string
  id?: number
  title?: string
  type?: string
  year?: number
}

export interface ShortLoadMatch {
  id: number
}

export type ShortListMatch = Partial<Short>

export interface Villain {
  gender?: string
  id?: number
  name?: string
  note?: string
  status?: string
  work?: string
}

export interface VillainLoadMatch {
  id: number
}

export type VillainListMatch = Partial<Villain>

