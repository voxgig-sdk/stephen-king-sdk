import { StephenKingEntityBase } from '../StephenKingEntityBase';
import type { StephenKingSDK } from '../StephenKingSDK';
import type { Control } from '../types';
import type { Villain, VillainLoadMatch, VillainListMatch } from '../StephenKingTypes';
declare class VillainEntity extends StephenKingEntityBase<Villain> {
    constructor(client: StephenKingSDK, entopts: any);
    make(this: VillainEntity): VillainEntity;
    load(this: any, reqmatch?: VillainLoadMatch, ctrl?: Control): Promise<VillainEntity>;
    list(this: any, reqmatch?: VillainListMatch, ctrl?: Control): Promise<VillainEntity[]>;
}
export { VillainEntity };
