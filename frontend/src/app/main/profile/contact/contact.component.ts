import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SharedService } from 'src/app/service/shared.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit{

  constructor(private contact : SharedService,private _router : Router){}


  ngOnInit(): void {
      
  }
  contactForm(data : object){
    console.warn(data);
    this.contact.submitContact(data).subscribe((result)=>{
      this._router.navigate(['']);
    });
  }

}
