import { StephenKingEntityBase } from '../StephenKingEntityBase';
import type { StephenKingSDK } from '../StephenKingSDK';
import type { Control } from '../types';
import type { Short, ShortLoadMatch, ShortListMatch } from '../StephenKingTypes';
declare class ShortEntity extends StephenKingEntityBase<Short> {
    constructor(client: StephenKingSDK, entopts: any);
    make(this: ShortEntity): ShortEntity;
    load(this: any, reqmatch?: ShortLoadMatch, ctrl?: Control): Promise<ShortEntity>;
    list(this: any, reqmatch?: ShortListMatch, ctrl?: Control): Promise<ShortEntity[]>;
}
export { ShortEntity };
