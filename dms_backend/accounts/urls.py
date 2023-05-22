
from importlib.resources import path
from django.db import router
from django.urls import include, path
from rest_framework import routers
from durin import views as durin_views
from accounts import views

urlpatterns = [

    # path(r'refresh/', durin_views.RefreshView.as_view(), name='durin_refresh'),
    # path(r'logout/', durin_views.LogoutView.as_view(), name='durin_logout'),
    # path(r'logoutall/', durin_views.LogoutAllView.as_view(), name='durin_logoutall'),
    path('api/user/group', views.UserGroupList.as_view()),
    path('api/user/group/<int:pk>', views.UserGroupDetails.as_view()),


    path('api/complex', views.ComplexList.as_view()),
    path('api/complex/<int:pk>', views.ComplexDetails.as_view()),

    path('api/designation', views.DesignationList.as_view()),
    path('api/designation/<int:pk>', views.DesignationDetails.as_view()),

    path('api/department', views.DepartmentList.as_view()),
    path('api/department/<int:pk>', views.DepartmentDetails.as_view()),

    path('api/designation/allocation', views.DesignationAllocationList.as_view()),
    path('api/designation/allocation/<int:pk>',
         views.DesignationAllocationDetails.as_view()),

    path('api/duty/allocation', views.DutyAllocationList.as_view()),
    path('api/duty/allocation/<int:pk>',
         views.DutyAllocationDetails.as_view()),

    path('api/attendance', views.DutyAllocationList.as_view()),
    path('api/attendance/<int:pk>',
         views.DutyAllocationDetails.as_view()),

    # path('api/user/profile', views.UserProfileList.as_view()),
    # path('api/user/profile/<int:pk>', views.UserProfileDetails.as_view()),

    path('api/user/standalone/reg', views.RegisteredUserList.as_view()),
    path('api/user/standalone/reg/<int:pk>',
         views.RegisteredUserDetails.as_view()),

    path('api/user/reg', views.UserRegisterList.as_view()),
    path('api/user/reg/<int:pk>', views.UserRegisterDetails.as_view()),

    path('api/user/profile', views.UserProfileList.as_view()),
    path('api/user/profile/<int:pk>', views.UserProfileDetails.as_view()),

    path('api/auth/', include('durin.urls'))
]
