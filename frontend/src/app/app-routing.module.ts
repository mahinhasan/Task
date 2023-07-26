// app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main/main.component';
import { ProfileComponent } from './main/profile/profile.component';
import { ContactComponent } from './main/profile/contact/contact.component';
import { IcortexComponent } from './main/profile/icortex/icortex.component';
import { ProjectsComponent } from './main/profile/projects/projects.component';
import { CrudProjectsComponent } from './main/profile/projects/crud-projects/crud-projects.component';
import { ShowProjectsComponent } from './main/profile/projects/show-projects/show-projects.component';
import { ToursComponent } from './main/profile/tours/tours.component';
import { AccountComponent } from './account/account.component';
import { LoginComponent } from './account/login/login.component';
import { RegisterComponent } from './account/register/register.component';

const routes: Routes = [
  { path: '', redirectTo: '/main', pathMatch: 'full' },
  { path: 'main', component: MainComponent },
  {
    path: 'main/profile', component: ProfileComponent,
    children: [
      { path: 'contact', component: ContactComponent },
      { path: 'icortex', component: IcortexComponent },
      { path: 'projects', component: ProjectsComponent },
      { path: 'projects/crud', component: CrudProjectsComponent },
      { path: 'projects/show', component: ShowProjectsComponent },
      { path: 'tours', component: ToursComponent },
    ]
  },
  { path: 'account', component: AccountComponent },
  { path: 'account/login', component: LoginComponent },
  { path: 'account/register', component: RegisterComponent },
  // Add more routes as needed
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
