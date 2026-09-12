import { StephenKingEntityBase } from '../StephenKingEntityBase';
import type { StephenKingSDK } from '../StephenKingSDK';
import type { Control } from '../types';
import type { Book, BookLoadMatch, BookListMatch } from '../StephenKingTypes';
declare class BookEntity extends StephenKingEntityBase<Book> {
    constructor(client: StephenKingSDK, entopts: any);
    make(this: BookEntity): BookEntity;
    load(this: any, reqmatch?: BookLoadMatch, ctrl?: Control): Promise<BookEntity>;
    list(this: any, reqmatch?: BookListMatch, ctrl?: Control): Promise<BookEntity[]>;
}
export { BookEntity };
