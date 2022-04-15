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
  dataS: IBook[] = [];
  suggestions: IBook[] = [];
  visi = -1 ;


  constructor(public bookservice : BookService) { 

  }
  ngOnInit() {

  }

  getbooks(word){
    // this.bookservice.searchBook(word).then((response) => {
    // }
    this.data = []
    this.suggestions = []

    this.bookservice.searchBook(word).subscribe(res => {
      const obj = JSON.parse(JSON.stringify(res));
      this.data = obj.books;
      this.dataS = obj.books;
      this.suggestions = obj.neightboors;
      console.log(this.suggestions)
       
    },(err)=>{
      alert('failed loading json data');
      console.log(err);
    });
  }

  handleClick(){
    var e = (<HTMLInputElement>document.getElementById("toggle_checkbox")).checked;
    console.log(e)
    this.data = []
    this.suggestions = []

    if (e == true){
      
      this.visi = 1;
    } else {
      this.visi = -1;
    }
  }

  getbooksR(regex){
 
    this.bookservice.searchBookR(regex).subscribe(res => {
      const obj = JSON.parse(JSON.stringify(res));
      this.data = obj.books;
      this.dataS = obj.books;
      this.suggestions = obj.neightboors;
      console.log(this.suggestions)
       
    },(err)=>{
      alert('failed loading json data');
      console.log(err);
    });
  }

  numberOfBooks_res(){
    var e = (<HTMLInputElement>document.getElementById("numberbook_res")).value;
    if(e != "max"){
      this.data = this.dataS.slice(0, parseInt(e))

    }else{
      this.data = this.dataS
    }
    (<HTMLInputElement>document.getElementById("numberbook_res")).value = "def"


  }

  sortbyOccurence_res(){
    var e = (<HTMLInputElement>document.getElementById("occ_res")).value;

    if(e == "ON"){
      this.data.sort((book1, book2) => {
        if (book1.occurence > book2.occurence ) { return -1; }
        else if (book1.occurence < book2.occurence ) { return 1; }
        else { return 0; }
      });
    }else{
      this.data = this.dataS
    }
    (<HTMLInputElement>document.getElementById("occ_res")).value = "def"

  }

  sortbyPertinence_res(){
    var e = (<HTMLInputElement>document.getElementById("pert_res")).value;

    if(e == "ON"){
      this.data.sort((book1, book2) => {
        if (book1.crank < book2.crank ) { return -1; }
        else if (book1.crank > book2.crank ) { return 1; }
        else { return 0; }
      });

    }else{
      this.data = this.dataS
    }
    (<HTMLInputElement>document.getElementById("pert_res")).value = "def"


  }



}
