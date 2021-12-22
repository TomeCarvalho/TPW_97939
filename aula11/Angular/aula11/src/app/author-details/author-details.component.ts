import {Component, OnInit} from '@angular/core';
import {Author} from "../author";
import {Location} from "@angular/common";
import {ActivatedRoute} from "@angular/router";
import {AuthorService} from "../author.service";

@Component({
  selector: 'app-author-details',
  templateUrl: './author-details.component.html',
  styleUrls: ['./author-details.component.css']
})
export class AuthorDetailsComponent implements OnInit {
  author: Author | undefined

  constructor(
    private route: ActivatedRoute,
    private location: Location,
    private authorService: AuthorService
  ) {
  }

  ngOnInit() {
    this.getAuthor()
  }

  getAuthor(): void {
    console.log("paramMap:", this.route.snapshot.paramMap)
    const id = +<string>this.route.snapshot.paramMap.get('id')
    this.authorService.getAuthor(id).subscribe(author => this.author = author)
  }

  update(): void {
    this.authorService.updateAuthor(this.author).subscribe(() => this.goBack())
  }

  delete(): void {
    this.authorService.deleteAuthor(this.author).subscribe(() => this.goBack())
  }

  goBack(): void {
    this.location.back()
  }
}
