import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { IBook } from 'src/models/book';

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.scss'],
})
export class BookComponent implements OnInit {
  @Input() book: IBook;

  constructor(private router: Router) { }

  ngOnInit():void {}

  poPup(){
    document.getElementById("popup-1").classList.toggle("active");
  }

}
