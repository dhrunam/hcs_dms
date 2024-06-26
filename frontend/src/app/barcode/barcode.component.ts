import { Component, OnInit } from '@angular/core';
import { BarcodeServices } from '../services/barcode.service';
import { CaseType, CaseTypeResponse } from '../models/CaseType';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { NgForm } from '@angular/forms';
import { baseUrl } from "../../environment/environment";

@Component({
  selector: 'app-barcode',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './barcode.component.html',
  styleUrl: './barcode.component.css'
})
export class BarcodeComponent implements OnInit {

  caseTypeData: Array<CaseTypeResponse> = [];// Variable to store the fetched data

  constructor(private barcodeService: BarcodeServices) { }

  getCaseTypes() {
    this.barcodeService.getCaseTypes().subscribe(
      (response) => {
        this.caseTypeData = response.results;
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


  onSubmit(data: NgForm) {

    console.log(data.value);
    console.log('Here');

    if (!data.invalid) {
      const url = `${baseUrl}/api/cis/qrcode/download?case_type=${data.value.caseType}&case_no=${data.value.caseNumber}&case_year=${data.value.caseYear}`;

      window.open(url, '')
    }
    else{
      console.log('Data is invalid');
    }


  }


}
