from django.urls import include, path
from crs.views import (
    CaseTypeList,
    CaseTypeDetails,
    CivilTList,
    CivilTDetails,
    ExtraPartyList,
    ExtraAdvocateList,
    JudgeNameTList,
    QRCodeDownloadView,
)

urlpatterns = [
    path('api/cis/case_type', CaseTypeList.as_view()),
    path('api/cis/extra_party', ExtraPartyList.as_view()),
    path('api/cis/extra_advocate', ExtraAdvocateList.as_view()),
    path('api/cis/civil_t', CivilTList.as_view()),
    path('api/cis/judges', JudgeNameTList().as_view()),
    path('api/cis/qrcode/download', QRCodeDownloadView.as_view()),
    # path('api/cis/civil_t/<pk:id>', CivilTDetails.as_view()),
]
