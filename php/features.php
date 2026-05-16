<?php
declare(strict_types=1);

// StephenKing SDK feature factory

require_once __DIR__ . '/feature/BaseFeature.php';
require_once __DIR__ . '/feature/TestFeature.php';


class StephenKingFeatures
{
    public static function make_feature(string $name)
    {
        switch ($name) {
            case "base":
                return new StephenKingBaseFeature();
            case "test":
                return new StephenKingTestFeature();
            default:
                return new StephenKingBaseFeature();
        }
    }
}
