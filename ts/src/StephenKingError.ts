
import { Context } from './Context'


class StephenKingError extends Error {

  isStephenKingError = true

  sdk = 'StephenKing'

  code: string
  ctx: Context

  constructor(code: string, msg: string, ctx: Context) {
    super(msg)
    this.code = code
    this.ctx = ctx
  }

}

export {
  StephenKingError
}

