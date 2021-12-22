import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterModule, Routes} from "@angular/router";
import {AuthorsComponent} from "./authors/authors.component";
import {BooksComponent} from "./books/books.component";
import {PublishersComponent} from "./publishers/publishers.component";
import {OverviewComponent} from "./overview/overview.component";
import {AuthorDetailsComponent} from "./author-details/author-details.component";

const routes: Routes = [
  {path: 'authors', component: AuthorsComponent},
  {path: 'books', component: BooksComponent},
  {path: 'publishers', component: PublishersComponent},
  {path: 'overview', component: OverviewComponent},
  {path: 'authordetails/:num', component: AuthorDetailsComponent}
]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ],
})
export class AppRoutingModule {
}
