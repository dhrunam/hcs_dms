import { Component, OnInit } from '@angular/core';
import { BarcodeServices } from '../services/barcode.service';
import { CaseType } from '../models/CaseType';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgForm } from '@angular/forms';


@Component({
  selector: 'app-barcode',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './barcode.component.html',
  styleUrl: './barcode.component.css'
})
export class BarcodeComponent implements OnInit {

  caseTypeData: CaseType[] = [];// Variable to store the fetched data

  constructor(private barcodeService: BarcodeServices) { }

  getCaseTypes() {
    this.barcodeService.getCaseTypes().subscribe(
      (response) => {
        this.caseTypeData = response.results.map(item => new CaseType(item.caseTypeId, item.caseTypeName));
        console.log('Case Type Data:', this.caseTypeData);
      },
      (error) => {
        console.error('Error fetching case type data:', error);
      }
    );
  }

  ngOnInit() {
    this.getCaseTypes();
  }


  onSubmit(data:NgForm){}


}
