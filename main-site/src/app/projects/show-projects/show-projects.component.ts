import { Component } from '@angular/core';
import { SharedService } from 'src/app/service/shared.service';

@Component({
  selector: 'app-show-projects',
  templateUrl: './show-projects.component.html',
  styleUrls: ['./show-projects.component.css']
})
export class ShowProjectsComponent {

ProjectList : any = [];
selectedImageUrl = `https://cataas.com/cat`;


constructor(private _service : SharedService){}

ngOnInit():void{
  this.refreshProjects();
  

}

refreshProjects(){
  this._service.getProjects().subscribe(data=>{
     this.ProjectList=data;
  })
  console.log(this.ProjectList);
}




}
