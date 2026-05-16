<?php
declare(strict_types=1);

// StephenKing SDK utility: result_body

class StephenKingResultBody
{
    public static function call(StephenKingContext $ctx): ?StephenKingResult
    {
        $response = $ctx->response;
        $result = $ctx->result;
        if ($result && $response && $response->json_func && $response->body) {
            $result->body = ($response->json_func)();
        }
        return $result;
    }
}
