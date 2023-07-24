import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly apiURL = "http://127.0.0.1:8000/";

  constructor(private http: HttpClient) { }

  getProjects(): Observable<any[]> {
    return this.http.get<any[]>(this.apiURL + 'api/portfolio/projects');
  }

  getImageData(imageFileName: string): Observable<any> {
    // Assuming the server returns a direct image URL
    return this.http.get<any>(this.apiURL + 'api/portfolio/projects/getImage/' + imageFileName);
  }
}
