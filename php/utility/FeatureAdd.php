<?php
declare(strict_types=1);

// StephenKing SDK utility: feature_add

class StephenKingFeatureAdd
{
    public static function call(StephenKingContext $ctx, mixed $f): void
    {
        $ctx->client->features[] = $f;
    }
}
