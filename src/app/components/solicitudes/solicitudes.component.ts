import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Usuario } from 'src/app/interfaces/usuario';
import { UsuarioService } from 'src/app/services/usuario.service';


@Component({
  selector: 'app-solicitudes',
  templateUrl: './solicitudes.component.html',
  styleUrls: ['./solicitudes.component.scss'],
})
export class SolicitudesComponent implements OnInit {

  listUsuarios: Usuario[] = [];

  displayedColumns: string[] = ['position', 'nombre', 'apellido', 'cedula', 'correo', 'acciones'];
  dataSource = new MatTableDataSource<any>(this.listUsuarios);

  constructor(private _usuarioService: UsuarioService) {

  }

  ngOnInit(): void {
    this.cargarUsuarios();
    this.obtenerUsuario();
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  toggle = true;
  status = 'Aprobado';

  toggle1 = true;
  status1 = 'Aprobado';

  toggle2 = true;
  status2 = 'Aprobado';

  enableDisableRule() {
    this.toggle = !this.toggle;
    this.status = this.toggle ? 'Aprobado' : 'Pendiente';
  }

  enableDisableRule1() {
    this.toggle1 = !this.toggle1;
    this.status1 = this.toggle1 ? 'Aprobado' : 'Pendiente';
  }

  enableDisableRule2() {
    this.toggle2 = !this.toggle2;
    this.status2 = this.toggle2 ? 'Aprobado' : 'Pendiente';
  }

  cargarUsuarios() {
    // this.listUsuarios = this._usuarioService.getUsuarios();
    // this.dataSource = new MatTableDataSource<any>(this.listUsuarios);
  }

  obtenerUsuario() {
    this._usuarioService.cargarUsuarios().subscribe(resp => {
      const {clientes} = resp;
      this.listUsuarios = clientes;
      this.dataSource = new MatTableDataSource<any>(this.listUsuarios);
    });
  }


}
