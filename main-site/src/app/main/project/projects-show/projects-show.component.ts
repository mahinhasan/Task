import { Component } from '@angular/core';
import { SharedService } from 'src/app/service/shared.service';

@Component({
  selector: 'app-projects-show',
  templateUrl: './projects-show.component.html',
  styleUrls: ['./projects-show.component.css']
})
export class ProjectsShowComponent {

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
