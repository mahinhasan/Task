import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly apiURL = "http://127.0.0.1:8000/";

  constructor(private http: HttpClient) { }

  getProjects(): Observable<any[]> {
    let x = this.http.get<any[]>(this.apiURL + 'api/portfolio/projects');
    console.log(x);
    return x;
  }

  getImageData(imageFileName: string): Observable<any> {
    return this.http.get<any>(this.apiURL + 'api/portfolio/projects/getImage/' + imageFileName);
  }
}
