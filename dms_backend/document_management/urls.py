from django.urls import include, path
from document_management.views import (
    CaseTypeList,
    CaseTypeDetails,
    DocumentTypeList,
    DocumentTypeDetails,
    OldCaseMasterDetails,
    OldCaseMasterList,
    OldCaseDocumentList,
    OldCaseDocumentDetails,
    NewCaseMasterDetails,
    NewCaseMasterList,
    NewCaseDocumentList,
    NewCaseDocumentDetails,


)

urlpatterns = [

    path('api/case_type', CaseTypeList.as_view()),
    path('api/case_type/<int:pk>', CaseTypeDetails.as_view()),

    path('api/document_type', DocumentTypeList.as_view()),
    path('api/document_type/<int:pk>', DocumentTypeDetails.as_view()),

    path('api/old_case_master', OldCaseMasterList.as_view()),
    path('api/old_case_master/<int:pk>', OldCaseMasterDetails.as_view()),

    path('api/old_case_document', OldCaseDocumentList.as_view()),
    path('api/old_case_document/<int:pk>', OldCaseDocumentDetails.as_view()),

    path('api/new_case_master', NewCaseMasterList.as_view()),
    path('api/new_case_master/<int:pk>', NewCaseMasterDetails.as_view()),

    path('api/new_case_document', NewCaseDocumentList.as_view()),
    path('api/new_case_document/<int:pk>', NewCaseDocumentDetails.as_view()),


]
