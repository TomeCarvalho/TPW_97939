import {Publisher} from "./publisher";
import {Author} from "./author";

export class Book {
  num: number | undefined
  title: string | undefined
  publisher: Publisher | undefined
  authors: Author[] | undefined
}
