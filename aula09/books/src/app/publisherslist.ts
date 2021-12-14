import {Author} from "./author"
import {Publisher} from "./publisher";
import {AUTHORS} from "./authorslist";

export const PUBLISHERS: Publisher[] = [
  {num: 0, name: 'Publisher 0', city: 'City 0', country: 'Country 0', website: 'Website 0', authors: [AUTHORS[0], AUTHORS[1]]},
  {num: 1, name: 'Publisher 1', city: 'City 1', country: 'Country 1', website: 'Website 1', authors: [AUTHORS[1], AUTHORS[3], AUTHORS[4]]},
  {num: 2, name: 'Publisher 2', city: 'City 2', country: 'Country 2', website: 'Website 2', authors: [AUTHORS[2]]},
  {num: 3, name: 'Publisher 3', city: 'City 3', country: 'Country 3', website: 'Website 3', authors: [AUTHORS[2], AUTHORS[3]]},
  {num: 4, name: 'Publisher 4', city: 'City 4', country: 'Country 4', website: 'Website 4', authors: [AUTHORS[0], AUTHORS[4]]},
]
