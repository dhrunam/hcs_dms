import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { baseUrl } from "../../environment/environment";
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { CaseType ,CaseTypeResponse} from "../models/CaseType";

@Injectable({
    providedIn: 'root'
})

export class BarcodeServices {

    constructor(private http: HttpClient) { }


    getCaseTypes(): Observable<{ results: CaseTypeResponse[] }> {
        return this.http.get<any>(`${baseUrl}/api/cis/case_type`);
    }

    downloadBarcode(case_type: string, case_number: string, case_year: string): Observable<Blob> {
        const url = `${baseUrl}/api/cis/qrcode/data?case_type=${case_type}&case_no=${case_number}&case_year=${case_year}`;
        console.log(url); 
        return this.http.post(url, null, { responseType: 'blob' });
    }

}