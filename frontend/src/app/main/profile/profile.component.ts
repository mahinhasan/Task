import { Component } from '@angular/core';
import { SharedService } from 'src/app/service/shared.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {
  showInfo: boolean = false;
  navlist: boolean = false;
 

  myname : string = '' ;
  constructor(private _service : SharedService){

  }

  ngOnInit():void{
    this.superUser();
    
  
  }





  superUser(){
    this._service.getSuperUser().subscribe(data=>{
      if (data && data.length > 0) {
        this.myname = data[0].first_name +" "+ data[0].last_name; 
        console.log(this.myname);
      }
    });
  }


  downloadPdf() {
    const fileUrl = '../../assets/MehediHasanMahin.pdf';
    const link = document.createElement('a');
    link.href = fileUrl;
    link.download = 'sample.pdf'; // Replace with the desired filename for the downloaded PDF
    link.click();
  }


  navList(hover : boolean){
    this.navlist = hover;
  }

  OpenInfo(){
    this.showInfo = !this.showInfo;

  }

  showDropdown = false;

  toggleDropdown() {
    this.showDropdown = !this.showDropdown;
  }

  showMobileNav: boolean = false;

  toggleMobileNav() {
    this.showMobileNav = !this.showMobileNav;
  }

}
