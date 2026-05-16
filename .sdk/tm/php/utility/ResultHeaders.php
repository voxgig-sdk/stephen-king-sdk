<?php
declare(strict_types=1);

// StephenKing SDK utility: result_headers

class StephenKingResultHeaders
{
    public static function call(StephenKingContext $ctx): ?StephenKingResult
    {
        $response = $ctx->response;
        $result = $ctx->result;
        if ($result) {
            if ($response && is_array($response->headers)) {
                $result->headers = $response->headers;
            } else {
                $result->headers = [];
            }
        }
        return $result;
    }
}
