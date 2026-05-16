<?php
declare(strict_types=1);

// StephenKing SDK utility: prepare_body

class StephenKingPrepareBody
{
    public static function call(StephenKingContext $ctx): mixed
    {
        if ($ctx->op->input === 'data') {
            return ($ctx->utility->transform_request)($ctx);
        }
        return null;
    }
}
