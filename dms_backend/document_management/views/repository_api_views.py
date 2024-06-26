from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from accounts import serializers, models
from durin.auth import TokenAuthentication
from document_management import models
from document_management import serializers as dms_serializers
from django.core.signals import (
    request_finished,
    request_started
)
from django.contrib.postgres.search import SearchQuery
# from django.contrib.postgres.search import TrigramWordSimilarity


from django.dispatch import receiver
from django.db.models.signals import (
    post_delete,
    pre_delete,
    pre_save,
    post_save
)


def generate_case_unique_id(self, data):

    latest_record = models.OldCaseMaster.objects.last()
    sl_no = 1
    if latest_record:
        case_unique_id = latest_record.case_unique_id
        if case_unique_id:

            year = case_unique_id[3:7]

            sl_no = int(case_unique_id[7:11])
            if data['case_year'] == year:
                sl_no = sl_no+1
            else:
                sl_no = 1

            sl_no_string = str(sl_no)

            case_unique_id = 'DMS'+data['case_year']+f"{sl_no:04d}"
            return case_unique_id

        return 'DMS'+data['case_year']+f"{sl_no:04d}"

    return 'DMS'+data['case_year']+f"{sl_no:04d}"


class OldCaseMasterList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.OldCaseMaster.objects.all()
    serializer_class = dms_serializers.OldCaseMasterSerializers

    def post(self, request, *args, **kwargs):

        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        request.data['case_unique_id'] = generate_case_unique_id(
            self, request.data)
        request.data._mutable = False
        # request.data['created_by'] = 1
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
        This view should return a list of all the purchases item  received
        for the specified order .
        """
        queryset = models.OldCaseMaster.objects.all()

        search_text = self.request.query_params.get('search_text')
        if search_text:
            # queryset = models.OldCaseMaster.objects.annotate(
            #     search=search_vector).order_by('-similarity')
            # return models.OldCaseMaster.objects.annotate(similarity=TrigramWordSimilarity(
            #     search_text, 'judge_name')).order_by('-similarity')

            queryset = models.OldCaseMaster.objects.filter(
                search_vector=SearchQuery(search_text))

        user_group = self.request.user.groups.all()

        if user_group.filter(name='Approver').exists():
            queryset = queryset.filter(is_approved=False)
        if user_group.filter(name='Data Entry Operator').exists():
            queryset = queryset.filter(is_approved=False)
        if user_group.filter(name='General User').exists():
            queryset = queryset.filter(is_approved=True)

        return queryset.order_by('id')


class OldCaseMasterDetails(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = models.OldCaseMaster
    serializer_class = dms_serializers.OldCaseMasterSerializers

    def put(self, request, *args, **kwargs):

        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        request.data._mutable = False
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        request.data._mutable = False
        return self.partial_update(request, *args, **kwargs)


class OldCaseDocumentList(generics.ListCreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = models.OldCaseDocument.objects.all().order_by('id')
    serializer_class = dms_serializers.OldCaseDocumentSerializers

    def get_queryset(self):
        """
        This view should return a list of all the purchases item  received
        for the specified order .
        """

        # order_number = self.request.data['order_no']
        # search_text = self.request.query_params.get('search_text')
        case_id = self.request.query_params.get('case_id')

        if(case_id):
            return self.queryset.filter(case_id=case_id).order_by('id')
        return self.queryset


class OldCaseDocumentDetails(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = models.OldCaseDocument
    serializer_class = dms_serializers.OldCaseDocumentSerializers

    def update(self, request, *args, **kwargs):
        print('update..')
        request.data._mutable = True
        if request.data.get('is_approved') is not None:
            request.data['approved_by'] = request.user.id

        request.data._mutable = False
        return super().update(request, *args, **kwargs)

    @receiver(post_delete, sender=models.OldCaseDocument)
    def post_delete_document(sender, instance, *args, **kwargs):
        """ Clean Old document file """
        try:
            instance.document_url.delete(save=False)
        except:
            pass


class NewCaseMasterList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.NewCaseMaster.objects.all()
    serializer_class = dms_serializers.NewCaseMasterSerializers

    def post(self, request, *args, **kwargs):

        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id

        request.data['case_unique_id'] = generate_case_unique_id(
            self, request.data)
        request.data._mutable = False
        # request.data['created_by'] = 1
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
        This view should return a list of all the purchases item  received
        for the specified order .
        """
        queryset = models.NewCaseMaster.objects.all()

        search_text = self.request.query_params.get('search_text')
        if search_text:
            # queryset = models.OldCaseMaster.objects.annotate(
            #     search=search_vector).order_by('-similarity')
            # return models.OldCaseMaster.objects.annotate(similarity=TrigramWordSimilarity(
            #     search_text, 'judge_name')).order_by('-similarity')

            queryset = models.NewCaseMaster.objects.filter(
                search_vector=SearchQuery(search_text))

        user_group = self.request.user.groups.all()

        if user_group.filter(name='Approver').exists():
            queryset = queryset.filter(is_approved=False)
        if user_group.filter(name='Data Entry Operator').exists():
            queryset = queryset.filter(is_approved=False)
        if user_group.filter(name='General User').exists():
            queryset = queryset.filter(is_approved=True)

        return queryset.order_by('id')


class NewCaseMasterDetails(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = models.NewCaseMaster
    serializer_class = dms_serializers.NewCaseMasterSerializers

    def put(self, request, *args, **kwargs):

        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        request.data._mutable = False
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['created_by'] = request.user.id
        request.data['updated_by'] = request.user.id
        request.data._mutable = False
        return self.partial_update(request, *args, **kwargs)


class NewCaseDocumentList(generics.ListCreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = models.NewCaseDocument.objects.all().order_by('id')
    serializer_class = dms_serializers.NewCaseDocumentSerializers

    def get_queryset(self):
        """
        This view should return a list of all the purchases item  received
        for the specified order .
        """

        # order_number = self.request.data['order_no']
        # search_text = self.request.query_params.get('search_text')
        case_id = self.request.query_params.get('case_id')

        if(case_id):
            return self.queryset.filter(case_id=case_id).order_by('id')
        return self.queryset


class NewCaseDocumentDetails(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = models.NewCaseDocument
    serializer_class = dms_serializers.NewCaseDocumentSerializers

    def update(self, request, *args, **kwargs):
        print('update..')
        request.data._mutable = True
        if request.data.get('is_approved') is not None:
            request.data['approved_by'] = request.user.id

        request.data._mutable = False
        return super().update(request, *args, **kwargs)

    @receiver(post_delete, sender=models.NewCaseDocument)
    def post_delete_document(sender, instance, *args, **kwargs):
        """ Clean Old document file """
        try:
            instance.document_url.delete(save=False)
        except:
            pass
