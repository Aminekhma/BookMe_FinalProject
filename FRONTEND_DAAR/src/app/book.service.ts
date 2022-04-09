import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'; 


@Injectable({
  providedIn: 'root'
})
export class BookService {

  urlApi;

  constructor(public http: HttpClient) {
    this.urlApi = "http://127.0.0.1:8000";  
  }


  searchBook(word){
    return this.http.get(this.urlApi+"/Search/" + word +"/");
  }

}
