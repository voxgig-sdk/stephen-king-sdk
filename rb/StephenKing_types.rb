# frozen_string_literal: true

# Typed models for the StephenKing SDK.
#
# GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
# params (op.<name>.points[].args.params[]). Member types come from the
# canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
# @voxgig/apidef VALID_CANON). Ruby types are unenforced; these YARD
# annotations document the shapes. Do not edit by hand.

# Book entity data model.
#
# @!attribute [rw] id
#   @return [Integer, nil]
#
# @!attribute [rw] isbn
#   @return [String, nil]
#
# @!attribute [rw] page
#   @return [Integer, nil]
#
# @!attribute [rw] publisher
#   @return [String, nil]
#
# @!attribute [rw] title
#   @return [String, nil]
#
# @!attribute [rw] year
#   @return [Integer, nil]
Book = Struct.new(
  :id,
  :isbn,
  :page,
  :publisher,
  :title,
  :year,
  keyword_init: true
)

# Request payload for Book#load.
#
# @!attribute [rw] id
#   @return [Integer]
BookLoadMatch = Struct.new(
  :id,
  keyword_init: true
)

# Request payload for Book#list.
#
# @!attribute [rw] id
#   @return [Integer, nil]
#
# @!attribute [rw] isbn
#   @return [String, nil]
#
# @!attribute [rw] page
#   @return [Integer, nil]
#
# @!attribute [rw] publisher
#   @return [String, nil]
#
# @!attribute [rw] title
#   @return [String, nil]
#
# @!attribute [rw] year
#   @return [Integer, nil]
BookListMatch = Struct.new(
  :id,
  :isbn,
  :page,
  :publisher,
  :title,
  :year,
  keyword_init: true
)

# Short entity data model.
#
# @!attribute [rw] collection
#   @return [String, nil]
#
# @!attribute [rw] id
#   @return [Integer, nil]
#
# @!attribute [rw] title
#   @return [String, nil]
#
# @!attribute [rw] type
#   @return [String, nil]
#
# @!attribute [rw] year
#   @return [Integer, nil]
Short = Struct.new(
  :collection,
  :id,
  :title,
  :type,
  :year,
  keyword_init: true
)

# Request payload for Short#load.
#
# @!attribute [rw] id
#   @return [Integer]
ShortLoadMatch = Struct.new(
  :id,
  keyword_init: true
)

# Request payload for Short#list.
#
# @!attribute [rw] collection
#   @return [String, nil]
#
# @!attribute [rw] id
#   @return [Integer, nil]
#
# @!attribute [rw] title
#   @return [String, nil]
#
# @!attribute [rw] type
#   @return [String, nil]
#
# @!attribute [rw] year
#   @return [Integer, nil]
ShortListMatch = Struct.new(
  :collection,
  :id,
  :title,
  :type,
  :year,
  keyword_init: true
)

# Villain entity data model.
#
# @!attribute [rw] gender
#   @return [String, nil]
#
# @!attribute [rw] id
#   @return [Integer, nil]
#
# @!attribute [rw] name
#   @return [String, nil]
#
# @!attribute [rw] note
#   @return [String, nil]
#
# @!attribute [rw] status
#   @return [String, nil]
#
# @!attribute [rw] work
#   @return [String, nil]
Villain = Struct.new(
  :gender,
  :id,
  :name,
  :note,
  :status,
  :work,
  keyword_init: true
)

# Request payload for Villain#load.
#
# @!attribute [rw] id
#   @return [Integer]
VillainLoadMatch = Struct.new(
  :id,
  keyword_init: true
)

# Request payload for Villain#list.
#
# @!attribute [rw] gender
#   @return [String, nil]
#
# @!attribute [rw] id
#   @return [Integer, nil]
#
# @!attribute [rw] name
#   @return [String, nil]
#
# @!attribute [rw] note
#   @return [String, nil]
#
# @!attribute [rw] status
#   @return [String, nil]
#
# @!attribute [rw] work
#   @return [String, nil]
VillainListMatch = Struct.new(
  :gender,
  :id,
  :name,
  :note,
  :status,
  :work,
  keyword_init: true
)

