package core

var UtilityRegistrar func(u *Utility)

var NewBaseFeatureFunc func() Feature

var NewTestFeatureFunc func() Feature

var NewBookEntityFunc func(client *StephenKingSDK, entopts map[string]any) StephenKingEntity

var NewShortEntityFunc func(client *StephenKingSDK, entopts map[string]any) StephenKingEntity

var NewVillainEntityFunc func(client *StephenKingSDK, entopts map[string]any) StephenKingEntity

