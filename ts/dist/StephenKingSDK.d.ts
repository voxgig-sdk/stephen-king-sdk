import { BookEntity } from './entity/BookEntity';
import { ShortEntity } from './entity/ShortEntity';
import { VillainEntity } from './entity/VillainEntity';
export type * from './StephenKingTypes';
import { inspect } from 'node:util';
import type { Context, Feature } from './types';
import { config } from './Config';
import { StephenKingEntityBase } from './StephenKingEntityBase';
import { Utility } from './utility/Utility';
import { BaseFeature } from './feature/base/BaseFeature';
declare const stdutil: Utility;
declare class StephenKingSDK {
    _mode: string;
    _options: any;
    _utility: Utility;
    _features: Feature[];
    _rootctx: Context;
    constructor(options?: any);
    options(): any;
    utility(): any;
    prepare(fetchargs?: any): Promise<any>;
    direct(fetchargs?: any): Promise<Error | {
        ok: boolean;
        status: number;
        headers: any;
        data: any;
        err?: undefined;
    } | {
        ok: boolean;
        err: any;
        status?: undefined;
        headers?: undefined;
        data?: undefined;
    }>;
    _rawRequest(fetchargs?: any): Promise<Error | {
        ok: boolean;
        status: number;
        headers: any;
        data: any;
        err?: undefined;
    } | {
        ok: boolean;
        err: any;
        status?: undefined;
        headers?: undefined;
        data?: undefined;
    }>;
    graphql(query: string, variables?: any, ctrl?: any): Promise<any>;
    Book(entopts?: Record<string, any>): BookEntity;
    Short(entopts?: Record<string, any>): ShortEntity;
    Villain(entopts?: Record<string, any>): VillainEntity;
    static test(testoptsarg?: any, sdkoptsarg?: any): StephenKingSDK;
    tester(testopts?: any, sdkopts?: any): StephenKingSDK;
    toJSON(): {
        name: string;
    };
    toString(): string;
    [inspect.custom](): string;
}
declare const SDK: typeof StephenKingSDK;
export { stdutil, config, BaseFeature, StephenKingEntityBase, StephenKingSDK, SDK, };
