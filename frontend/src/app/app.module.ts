import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { AccountComponent } from './account/account.component';
import { SidenavComponent } from './sidenav/sidenav.component';
import { HeaderComponent } from './header/header.component';
import { ProjectsComponent } from './main/projects/projects.component';
import { ShowProjectsComponent } from './main/projects/show-projects/show-projects.component';
import { CrudProjectsComponent } from './main/projects/crud-projects/crud-projects.component';
import { LoginComponent } from './account/login/login.component';
import { RegisterComponent } from './account/register/register.component';
import { ContactComponent } from './main/contact/contact.component';
import { ToursComponent } from './main/tours/tours.component';
import { IcortexComponent } from './main/icortex/icortex.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { SharedService } from './service/shared.service';
import { HttpClientModule } from '@angular/common/http';
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
    IcortexComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FontAwesomeModule,
    HttpClientModule,
  
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
