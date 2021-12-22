import { Component, OnInit } from '@angular/core';
import {Book} from "../book";

@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css']
})
export class BooksComponent implements OnInit {

  books: Book[] | undefined
  selectedBook: Book | undefined

  constructor() {
  }

  ngOnInit(): void {
  }

  onSelect(book: Book) {
    this.selectedBook = book
  }

}
