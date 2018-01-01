from django.shortcuts import render
from core.serializers import AccountSerializer, BranchSerializer, VolunteerSerializer
from rest_framework import generics
from core.models import Account, Branch, Volunteer

import logging

# Create your views here.
log = logging.getLogger(__name__)


def index(request):
    context = {}
    context['page'] = 'profiles'
    context['accounts'] = Account.objects.all()

    return render(request, 'core/index.html', context)


class AccountList(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        """
        This view should return a list of all the accounts
        for the currently authenticated user.
        """
        user = self.request.user
        return Account.objects.filter()


class BranchList(generics.ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        """
        This view should return a list of all the accounts
        for the currently authenticated user.
        """
        # user = self.request.user
        return Branch.objects.filter()


from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


class VolunteerViewSet(viewsets.ViewSet):
    """
    A ViewSet for listing Volunteers.
    """
    def list(self, request):
        # todo filter institution Transactions
        queryset = Volunteer.objects.all()
        serializer = VolunteerSerializer(queryset, many=True)
        return Response(serializer.data)

    """
    A ViewSet for retrieving A Volunteer.
    """
    def retrieve(self, request, pk=None):
        queryset = Volunteer.objects.all()
        child = get_object_or_404(queryset, pk=pk)
        serializer = VolunteerSerializer(child)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        Volunteer = Volunteer()
        Volunteer.dob = data['date_of_birth']
        Volunteer.Branch_id = data['Branch']
        # Volunteer.picture
        Volunteer.gender = data['gender']
        Volunteer.guardians = data['guardians']
        Volunteer.contact_number = data['contact_number']
        Volunteer.residence = data['residence']
        Volunteer.address = data['address']
        Volunteer.save()

def new_member(request):
    # pass
    return render(request, 'core/new_member.html', {})

def edit_member(request):
    # pass
    return render(request, 'core/edit_member.html', {})

def list_member(request):
    # pass
    return render(request, 'core/members.html', {})

def member_details(request):
    # pass
    return render(request, 'core/member_details.html', {})

def new_user(request):
    # pass
    return render(request, 'core/new_user.html', {})

def edit_user(request):
    # pass
    return render(request, 'core/edit_user.html', {})

def list_user(request):
    # pass
    return render(request, 'core/users.html', {})

def user_details(request):
    # pass
    return render(request, 'core/user_details.html', {})





