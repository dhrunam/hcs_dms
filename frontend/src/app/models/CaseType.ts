export class CaseType{
  caseTypeId:number;
  caseTypeName:string;
  
  constructor(caseTypeId:number, caseTypeName:string){
    this.caseTypeId=caseTypeId;
    this.caseTypeName=caseTypeName;
  }
  
    
}

export interface CaseTypeResponse{
      caseTypeId:number;
  caseTypeName:string;
}