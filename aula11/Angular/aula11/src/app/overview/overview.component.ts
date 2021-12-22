import {Component, OnInit} from '@angular/core';
import {Author} from "../author";
import {AuthorService} from "../author.service";

@Component({
  selector: 'app-overview',
  templateUrl: './overview.component.html',
  styleUrls: ['./overview.component.css']
})
export class OverviewComponent implements OnInit {
  authors: Author[] | undefined

  constructor(private authorService: AuthorService) {
  }

  ngOnInit(): void {
    this.getAuthors()
  }

  getAuthors(): void {
    this.authorService.getAuthors().subscribe(authors => this.authors = authors)
  }
}
