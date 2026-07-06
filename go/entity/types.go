// Typed models for the StephenKing SDK.
//
// GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
// params (op.<name>.points[].args.params[]). Field/param types come from the
// canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
// @voxgig/apidef VALID_CANON). Do not edit by hand.
package entity

import "encoding/json"

// Book is the typed data model for the book entity.
type Book struct {
	Id *int `json:"id,omitempty"`
	Isbn *string `json:"isbn,omitempty"`
	Page *int `json:"page,omitempty"`
	Publisher *string `json:"publisher,omitempty"`
	Title *string `json:"title,omitempty"`
	Year *int `json:"year,omitempty"`
}

// BookLoadMatch is the typed request payload for Book.LoadTyped.
type BookLoadMatch struct {
	Id int `json:"id"`
}

// BookListMatch is the typed request payload for Book.ListTyped.
type BookListMatch struct {
	Id *int `json:"id,omitempty"`
	Isbn *string `json:"isbn,omitempty"`
	Page *int `json:"page,omitempty"`
	Publisher *string `json:"publisher,omitempty"`
	Title *string `json:"title,omitempty"`
	Year *int `json:"year,omitempty"`
}

// Short is the typed data model for the short entity.
type Short struct {
	Collection *string `json:"collection,omitempty"`
	Id *int `json:"id,omitempty"`
	Title *string `json:"title,omitempty"`
	Type *string `json:"type,omitempty"`
	Year *int `json:"year,omitempty"`
}

// ShortLoadMatch is the typed request payload for Short.LoadTyped.
type ShortLoadMatch struct {
	Id int `json:"id"`
}

// ShortListMatch is the typed request payload for Short.ListTyped.
type ShortListMatch struct {
	Collection *string `json:"collection,omitempty"`
	Id *int `json:"id,omitempty"`
	Title *string `json:"title,omitempty"`
	Type *string `json:"type,omitempty"`
	Year *int `json:"year,omitempty"`
}

// Villain is the typed data model for the villain entity.
type Villain struct {
	Gender *string `json:"gender,omitempty"`
	Id *int `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Note *string `json:"note,omitempty"`
	Status *string `json:"status,omitempty"`
	Work *string `json:"work,omitempty"`
}

// VillainLoadMatch is the typed request payload for Villain.LoadTyped.
type VillainLoadMatch struct {
	Id int `json:"id"`
}

// VillainListMatch is the typed request payload for Villain.ListTyped.
type VillainListMatch struct {
	Gender *string `json:"gender,omitempty"`
	Id *int `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Note *string `json:"note,omitempty"`
	Status *string `json:"status,omitempty"`
	Work *string `json:"work,omitempty"`
}

// asMap turns a typed request/data struct into the map[string]any the
// runtime op pipeline consumes, honouring the json tags above.
func asMap(v any) map[string]any {
	out := map[string]any{}
	b, err := json.Marshal(v)
	if err != nil {
		return out
	}
	_ = json.Unmarshal(b, &out)
	return out
}

// typedFrom decodes a runtime value (a map[string]any produced by the op
// pipeline) into a typed model T via a JSON round-trip. On any error it
// returns the zero value of T; the op's own (value, error) tuple carries the
// real error.
func typedFrom[T any](v any) T {
	var out T
	if v == nil {
		return out
	}
	b, err := json.Marshal(v)
	if err != nil {
		return out
	}
	_ = json.Unmarshal(b, &out)
	return out
}

// typedSliceFrom decodes a runtime list value ([]any of maps) into a typed
// slice []T via a JSON round-trip, for list ops.
func typedSliceFrom[T any](v any) []T {
	var out []T
	if v == nil {
		return out
	}
	b, err := json.Marshal(v)
	if err != nil {
		return out
	}
	_ = json.Unmarshal(b, &out)
	return out
}
