import { NgModule } from '@angular/core';
import { Routes, RouterModule, CanActivate } from '@angular/router';
import { SolicitudesComponent } from './components/solicitudes/solicitudes.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HomeComponent } from './home/home.component';
import { ClientesComponent } from './components/clientes/clientes.component';
import { ProductosComponent } from './components/productos/productos.component';
import { AuthGuard } from './auth.guard';
import { SignupComponent } from './signup/signup.component';
import { PadreComponent } from './padre/padre.component';

const routes: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  { path: '',
  component: PadreComponent,
  children: [
    { path: 'solicitudes', component: SolicitudesComponent },
    { path: 'clientes', component: ClientesComponent },
    { path: 'producto', component: ProductosComponent },
    { path: 'dashboard', component: DashboardComponent },
  ],
  canActivate: [AuthGuard],
 },
  { path: 'login',
   component: SignupComponent,
  },
  { path: '**', redirectTo: 'dashboard'}// ** significa cualquier ruta que no este definida
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
