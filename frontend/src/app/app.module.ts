import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { SharedService } from './service/shared.service';
import { HttpClientModule } from '@angular/common/http';
import { ProfileComponent } from './main/profile/profile.component';
import { MainComponent } from './main/main.component';
import { SidenavComponent } from './sidenav/sidenav.component';
import { IcortexComponent } from './main/profile/icortex/icortex.component';
import { ToursComponent } from './main/profile/tours/tours.component';
import { ContactComponent } from './main/profile/contact/contact.component';
import { LoginComponent } from './account/login/login.component';
import { CrudProjectsComponent } from './main/profile/projects/crud-projects/crud-projects.component';
import { ShowProjectsComponent } from './main/profile/projects/show-projects/show-projects.component';
import { ProjectsComponent } from './main/profile/projects/projects.component';
import { AccountComponent } from './account/account.component';
import { HeaderComponent } from './header/header.component';
import { RegisterComponent } from './account/register/register.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';
@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    AccountComponent,
    SidenavComponent,
    HeaderComponent,
    ProjectsComponent,
    ShowProjectsComponent,
    CrudProjectsComponent,
    LoginComponent,
    RegisterComponent,
    ContactComponent,
    ToursComponent,
    IcortexComponent,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FontAwesomeModule,
    HttpClientModule,
    AppRoutingModule,

    BrowserAnimationsModule,
    FormsModule,
  
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
