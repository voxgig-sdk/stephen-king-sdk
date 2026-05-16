<?php
declare(strict_types=1);

// StephenKing SDK utility: make_context

require_once __DIR__ . '/../core/Context.php';

class StephenKingMakeContext
{
    public static function call(array $ctxmap, ?StephenKingContext $basectx): StephenKingContext
    {
        return new StephenKingContext($ctxmap, $basectx);
    }
}
