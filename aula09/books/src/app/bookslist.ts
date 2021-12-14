import {Author} from "./author"
import {Book} from "./book";
import {AUTHORS} from "./authorslist";
import {PUBLISHERS} from "./publisherslist";

export const BOOKS: Book[] = [
  {num: 1, title: 'Book 0', publisher: PUBLISHERS[0], authors: [AUTHORS[0], AUTHORS[3]]},
  {num: 2, title: 'Book 1', publisher: PUBLISHERS[1], authors: [AUTHORS[2], AUTHORS[4]]},
  {num: 3, title: 'Book 2', publisher: PUBLISHERS[2], authors: [AUTHORS[0], AUTHORS[1]]},
  {num: 4, title: 'Book 3', publisher: PUBLISHERS[3], authors: [AUTHORS[0]]},
  {num: 5, title: 'Book 4', publisher: PUBLISHERS[4], authors: [AUTHORS[2]]},
]
