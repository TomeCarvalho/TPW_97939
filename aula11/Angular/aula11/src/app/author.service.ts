import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {Author} from "./author";

const httpOptions = {
  headers: new HttpHeaders({'Content-Type': 'application/json'})
}

@Injectable({
  providedIn: 'root'
})
export class AuthorService {
  private baseURL = 'http://localhost:8000/ws/'

  constructor(private http: HttpClient) {
  }

  getAuthor(id: number): Observable<Author> {
    const url = this.baseURL + 'author?id=' + id
    return this.http.get<Author>(url)
  }

  getAuthors(): Observable<Author[]> {
    const url = this.baseURL + 'authors'
    return this.http.get<Author[]>(url)
  }

  getAuthorsN(num: number): Observable<Author[]> {
    const url = this.baseURL + 'authors?num=' + num
    return this.http.get<Author[]>(url)
  }

  createAuthor(au: Author): Observable<any> {
    const url = this.baseURL + 'authorcre'
    return this.http.post(url, au, httpOptions)
  }

  updateAuthor(au: Author | undefined): Observable<any> {
    const url = this.baseURL + 'authorupd'
    return this.http.put(url, au, httpOptions)
  }

  deleteAuthor(au: Author | undefined): Observable<any> {
    // @ts-ignore
    const url = this.baseURL + 'authordel' + au.id
    return this.http.delete(url, httpOptions)
  }
}
