
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from crs import serializers, models
from durin.auth import TokenAuthentication


# Create your views here.
class CaseTypeList(generics.ListCreateAPIView):
    queryset = models.CaseTypeT.objects.all().order_by('case_type')
    serializer_class = serializers.CaseTypeTSerializer

    def post(self, request, *args, **kwargs):
        # Not allowing insert for time being
        return queryset


class CaseTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CaseTypeT
    serializer_class = serializers.CaseTypeTSerializer


class ExtraPartyList(generics.ListCreateAPIView):
    queryset = models.CivAddressTA.objects.all().order_by('cino')
    serializer_class = serializers.CivAddressTSerializer

    def post(self, request, *args, **kwargs):
        # Not allowing insert for time being
        return queryset

    def get_queryset(self):
        """
        This view should return a list of all the purchases item  received
        for the specified order .
        """
        queryset = models.CivAddressTA.objects.all().order_by('cino')

        cino = self.request.query_params.get('cino')
        # petioner = self.request.query_params.get('type')

        if cino:

            queryset = queryset.filter(cino=cino)

        return queryset.order_by('case_no')


class ExtraAdvocateList(generics.ListCreateAPIView):
    queryset = models.ExtraAdvT.objects.all().order_by('cino')
    serializer_class = serializers.ExtraAdvTSerializer

    def post(self, request, *args, **kwargs):
        # Not allowing insert for time being
        return queryset

    def get_queryset(self):
        """
        This view should return a list of all the purchases item  received
        for the specified order .
        """
        queryset = models.ExtraAdvT.objects.all().order_by('cino')

        cino = self.request.query_params.get('cino')
        # petioner = self.request.query_params.get('type')

        if cino:

            queryset = queryset.filter(cino=cino)

        return queryset.order_by('case_no')


class CivilTList(generics.ListAPIView):
    queryset = models.CivilTA.objects.all().order_by('case_no')
    serializer_class = serializers.CivilTSerializer
    # Not allowing insert for time being

    # def post(self, request, *args, **kwargs):
    #     return queryset

    def get_queryset(self):
        """
        This view should return a list of all the purchases item  received
        for the specified order .
        """
        queryset = models.CivilTA.objects.all()

        case_type = self.request.query_params.get('case_type')
        case_no = self.request.query_params.get('case_no')
        case_year = self.request.query_params.get('case_year')
        if case_type and case_no and case_year:
            print('Test...')
            queryset = queryset.filter(
                reg_no=case_no).filter(regcase_type=case_type).filter(reg_year=case_year)

        return queryset.order_by('case_no')


class CivilTDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CivilTA
    serializer_class = serializers.CivilTSerializer


class JudgeNameTList(generics.ListCreateAPIView):
    queryset = models.JudgeNameT.objects.all().order_by('judge_code')
    serializer_class = serializers.JudgeNameTSerilaizer

    def get_queryset(self):
        """
        This view should return a list of all the purchases item  received
        for the specified order .
        """
        queryset = models.JudgeNameT.objects.all()

        judge_code = self.request.query_params.get('judge_code')

        if judge_code:
            print('Test...')

            queryset = queryset.filter(judge_code__in=judge_code.split(","))

        return queryset.order_by('judge_code')
