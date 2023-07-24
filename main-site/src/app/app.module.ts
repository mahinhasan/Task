import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeadersComponent } from './headers/headers.component';
import { FooterComponent } from './footer/footer.component';
import { SharedService } from './service/shared.service';
import {HttpClientModule} from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AccountComponent } from './account/account.component';
import { LoginComponent } from './account/login/login.component';
import { RegisterComponent } from './account/register/register.component';
import { MainComponent } from './main/main.component';
import { ProjectComponent } from './main/project/project.component';
import { ToursComponent } from './main/tours/tours.component';
import { AcedemicComponent } from './main/acedemic/acedemic.component';
import { IcortexComponent } from './main/icortex/icortex.component';
import { BlogComponent } from './main/icortex/blog/blog.component';
import { ServiceComponent } from './main/icortex/service/service.component';
import { TeamsComponent } from './main/icortex/teams/teams.component';
import { ContactComponent } from './main/icortex/contact/contact.component';
import { ProjectsCrudComponent } from './main/project/projects-crud/projects-crud.component';
import { ProjectsShowComponent } from './main/project/projects-show/projects-show.component';

@NgModule({
  declarations: [
    AppComponent,
    HeadersComponent,
    FooterComponent,
    AccountComponent,
    LoginComponent,
    RegisterComponent,
    MainComponent,
    ProjectComponent,
    ToursComponent,
    AcedemicComponent,
    IcortexComponent,
    BlogComponent,
    ServiceComponent,
    TeamsComponent,
    ContactComponent,
    ProjectsCrudComponent,
    ProjectsShowComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule

  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
