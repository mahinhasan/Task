import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProjectsComponent } from './projects/projects.component';
import { ShowProjectsComponent } from './projects/show-projects/show-projects.component';

const routes: Routes = [
  {
    path:'projects',
    component: ProjectsComponent
  },
  {
    path : 'projects/showProject',
    component : ShowProjectsComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
