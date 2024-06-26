import { Routes } from '@angular/router';

export const routes: Routes = [


    { path: '', loadComponent: () => import('./barcode/barcode.component').then(c => c.BarcodeComponent) }
];
