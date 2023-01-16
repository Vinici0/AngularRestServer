import { Injectable } from '@angular/core';
import { Usuario } from '../interfaces/usuario';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  url = 'http://localhost:8080/api/clientes/';


  constructor(private http: HttpClient) { }

  cargarUsuarios(): Observable<any>{
    return this.http.get(this.url);
  }


  guardarUsuario(usuario: Usuario) {
    return this.http.post(this.url, usuario);
  }

}
