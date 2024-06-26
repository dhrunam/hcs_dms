import { HttpClient } from "@angular/common/http";
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

    downloadBarcode() {

    }

}