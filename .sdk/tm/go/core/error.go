package core

type StephenKingError struct {
	IsStephenKingError bool
	Sdk              string
	Code             string
	Msg              string
	Ctx              *Context
	Result           any
	Spec             any
}

func NewStephenKingError(code string, msg string, ctx *Context) *StephenKingError {
	return &StephenKingError{
		IsStephenKingError: true,
		Sdk:              "StephenKing",
		Code:             code,
		Msg:              msg,
		Ctx:              ctx,
	}
}

func (e *StephenKingError) Error() string {
	return e.Msg
}
