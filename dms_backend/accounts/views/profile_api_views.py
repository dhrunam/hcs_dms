
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from accounts import serializers, models
from durin.auth import TokenAuthentication


class RegisteredUserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ResgisteredUserSerializer


class RegisteredUserDetails(generics.RetrieveUpdateAPIView):
    queryset = User
    serializer_class = serializers.ResgisteredUserPatchSerializer

    def update(self, request, *args, **kwargs):
        print('update..')
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print('patch..')
        kwargs['partial'] = True
        request.POST._mutable = True

        if request.data.get('email') is None:
            request.data.pop('email')
        if request.data.get('group') is None:
            request.data.pop('group')
        if request.data.get('password') is None:
            request.data.pop('password')
        if request.data.get('password2') is None:
            request.data.pop('password2')

        request.POST._mutable = False
        return super().update(request, *args, **kwargs)


class UserProfileList(generics.ListCreateAPIView):
    queryset = models.UserProfile.objects.all().order_by('id')
    serializer_class = serializers.UserProfileSerializer


class UserProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserProfile
    serializer_class = serializers.UserProfileSerializer


class UserRegisterList(generics.ListCreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('id')
    serializer_class = serializers.RegisterSerializer

    def post(self, request, *args, **kwargs):

        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        if 'employee_photo' in request.FILES:
            file_name_parts = request.data.get('employee_photo').name.split(
                '.')
            if len(file_name_parts) > 1:
                request.data['employee_photo'].name = 'profile_photo_' + request.data.get(
                    'username') + '.'+file_name_parts[len(file_name_parts)-1]
        else:
            print(request.data)
            pass
        # request.data['created_by'] = request.user.id
        # request.data['updated_by'] = request.user.id
        request.data._mutable = False
        # request.data['created_by'] = 1
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
        This view should return a list of all the purchases item  received
        for the specified order .
        """

        return self.queryset.filter(is_superuser=False).order_by('id')


class UserRegisterDetails(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = User
    serializer_class = serializers.RegisterSerializer

    def put(self, request, *args, **kwargs):

        request.data._mutable = True
        # request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        request.data._mutable = False
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        request.data._mutable = True
        # request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        request.data._mutable = False
        return self.partial_update(request, *args, **kwargs)


class UserGroupList(generics.ListCreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all().order_by('id')
    serializer_class = serializers.UserGroupSerializer


class UserGroupDetails(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Group
    serializer_class = serializers.UserGroupSerializer
