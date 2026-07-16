<?php
declare(strict_types=1);

// StephenKing SDK base feature

class StephenKingBaseFeature
{
    public string $version;
    public string $name;
    public bool $active;

    // Positions this feature when added via the client `extend` option:
    // "__before__" / "__after__" / "__replace__" name an already-added
    // feature (mirrors the ts feature `_options`). Declared so setting it
    // on an extension instance avoids the dynamic-property deprecation.
    public ?array $_options = null;

    public function __construct()
    {
        $this->version = '0.0.1';
        $this->name = 'base';
        $this->active = true;
    }

    public function get_version(): string { return $this->version; }
    public function get_name(): string { return $this->name; }
    public function get_active(): bool { return $this->active; }

    public function init(StephenKingContext $ctx, array $options): void {}
    public function PostConstruct(StephenKingContext $ctx): void {}
    public function PostConstructEntity(StephenKingContext $ctx): void {}
    public function SetData(StephenKingContext $ctx): void {}
    public function GetData(StephenKingContext $ctx): void {}
    public function GetMatch(StephenKingContext $ctx): void {}
    public function SetMatch(StephenKingContext $ctx): void {}
    public function PrePoint(StephenKingContext $ctx): void {}
    public function PreSpec(StephenKingContext $ctx): void {}
    public function PreRequest(StephenKingContext $ctx): void {}
    public function PreResponse(StephenKingContext $ctx): void {}
    public function PreResult(StephenKingContext $ctx): void {}
    public function PreDone(StephenKingContext $ctx): void {}
    public function PreUnexpected(StephenKingContext $ctx): void {}
}
