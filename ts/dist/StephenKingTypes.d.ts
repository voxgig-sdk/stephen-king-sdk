export interface Book {
    id?: number;
    isbn?: string;
    pages?: number;
    publisher?: string;
    title?: string;
    year?: number;
}
export interface BookLoadMatch {
    id: number;
}
export interface BookListMatch {
    id?: number;
    isbn?: string;
    pages?: number;
    publisher?: string;
    title?: string;
    year?: number;
}
export interface Short {
    collection?: string;
    id?: number;
    title?: string;
    type?: string;
    year?: number;
}
export interface ShortLoadMatch {
    id: number;
}
export interface ShortListMatch {
    collection?: string;
    id?: number;
    title?: string;
    type?: string;
    year?: number;
}
export interface Villain {
    gender?: string;
    id?: number;
    name?: string;
    notes?: string;
    status?: string;
    work?: string;
}
export interface VillainLoadMatch {
    id: number;
}
export interface VillainListMatch {
    gender?: string;
    id?: number;
    name?: string;
    notes?: string;
    status?: string;
    work?: string;
}
