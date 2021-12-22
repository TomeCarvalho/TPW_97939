import {Component, OnInit} from '@angular/core';
import {Author} from "../author";
import {Location} from "@angular/common";
import {ActivatedRoute} from "@angular/router";
import {AUTHORS} from "../authorslist";

@Component({
  selector: 'app-author-details',
  templateUrl: './author-details.component.html',
  styleUrls: ['./author-details.component.css']
})
export class AuthorDetailsComponent implements OnInit {
  author: Author | undefined

  constructor(
    private route: ActivatedRoute,
    private location: Location
  ) {
  }

  ngOnInit() {
    this.getAuthor()
  }

  getAuthor(): void {
    const num = + <string> this.route.snapshot.paramMap.get('num')
    this.author = AUTHORS.find(author => author.num === num)
  }

  goBack(): void {
    this.location.back()
  }

}
