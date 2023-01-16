import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private URL = 'http://localhost:8080/api';

  constructor(private http: HttpClient,private router: Router) { }

  signIn(user) {
    return this.http.post<any>(this.URL + '/usuarios', user);
  }

  loggedIn(): boolean {
    return !!localStorage.getItem('token');//Si existe el token retorna true
  }

  logout() {
    localStorage.removeItem('token');
    this.router.navigate(['/login']);
  }

}
