import { Component, OnInit } from '@angular/core';
import { IBook } from 'src/models/book';
import { BookService } from '../book.service'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {

  data: IBook[] = [];

  constructor(public bookservice : BookService) { 

  }
  ngOnInit() {

  }

  getbooks(word){
    // this.bookservice.searchBook(word).then((response) => {
    // }

    this.bookservice.searchBook(word).subscribe(res => {
      const obj = JSON.parse(JSON.stringify(res));

      this.data = obj.books;

      console.log(this.data)
       
    },(err)=>{
      alert('failed loading json data');
      console.log(err);
    });
  }

}
