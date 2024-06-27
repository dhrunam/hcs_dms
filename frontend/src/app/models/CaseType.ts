export class CaseType{
  case_type: number;
  type_name: string;
  
  constructor(caseTypeId:number, caseTypeName:string){
    this.case_type = caseTypeId;
    this.type_name = caseTypeName;
  }
}

export interface CaseTypeResponse{
  case_type: number;
  type_name: string;
}