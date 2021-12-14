import { Component, OnInit } from '@angular/core';
import {Book} from "../book";
import {BOOKS} from "../bookslist";

@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css']
})
export class BooksComponent implements OnInit {

  books: Book[]
  selectedBook: Book | undefined

  constructor() {
    this.books = BOOKS
  }

  ngOnInit(): void {
  }

  onSelect(book: Book) {
    this.selectedBook = book
  }

}
