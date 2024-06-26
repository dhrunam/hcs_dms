
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from crs import serializers, models
from durin.auth import TokenAuthentication

from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse


import qrcode
from io import BytesIO



def generate_qrcode(data: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


class QRCodeDownloadView(views.APIView):
    def get(self, request, *args, **kwargs):
        data = request.query_params.get('data', 'default data')
        qr_code_buffer = generate_qrcode(data)
        response = HttpResponse(qr_code_buffer, content_type="image/png")
        response['Content-Disposition'] = f'attachment; filename="qrcode.png"'
        return response


# Create your views here.
class CaseTypeList(generics.ListCreateAPIView):
    queryset = models.CaseTypeT.objects.all().order_by('case_type')
    serializer_class = serializers.CaseTypeTSerializer

    def post(self, request, *args, **kwargs):
        # Not allowing insert for time being
        return self.queryset


class CaseTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CaseTypeT
    serializer_class = serializers.CaseTypeTSerializer


class ExtraPartyList(generics.ListCreateAPIView):
    queryset = models.CivAddressTA.objects.all().order_by('cino')
    serializer_class = serializers.CivAddressTSerializer

    def post(self, request, *args, **kwargs):
        # Not allowing insert for time being
        pass

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
        pass

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

    def post(self, request, *args, **kwargs):
        pass

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
