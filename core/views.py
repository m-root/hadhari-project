from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from pyproj import Proj, transform
from django.conf import settings

from core.forms import DaycareForm,OwnerForm
from core.models import Daycare,Organisation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
import logging


logger = logging.getLogger('prj')


# def index(request):
#     context = {
#         'google_maps_key': settings.GOOGLE_MAPS_API_KEY,
#         'form' : DaycareForm()
#     }
#
#     return render(request,'core/map.html',context)

def index(request):
    context = {
        'google_maps_key': settings.GOOGLE_MAPS_API_KEY,
        'form' : DaycareForm()
    }
    return render(request,'core/index.html',context)

def details(request):
    context = {
        'google_maps_key': settings.GOOGLE_MAPS_API_KEY,
        'form' : DaycareForm()
    }
    return render(request,'core/details.html',context)


def listing(request):

    page = request.GET.get('page', 1)

    daycares = Daycare.objects.all()

    paginator = Paginator(daycares, 20)
    try:
        daycares = paginator.page(page)
    except PageNotAnInteger:
        daycares = paginator.page(1)
    except EmptyPage:
        daycares = paginator.page(paginator.num_pages)

    context = {
        'daycare' : daycare_view,
        'daycares' : daycares,
        'google_maps_key': settings.GOOGLE_MAPS_API_KEY,
        'form' : DaycareForm()
    }
    return render(request,'core/listing.html',context)


def create_daycare(request):
    if request.method == "POST":
        form = DaycareForm(data=request.POST)
        if form.is_valid():
            daycare = form.save()

            return redirect('/daycares/')
    else:
        form = DaycareForm()

    return render(request, 'core/daycare/create.html', {'form':form,'google_maps_key':settings.GOOGLE_MAPS_API_KEY})


def daycare_edit(request,pk):
    daycare = Daycare.objects.get(pk=pk)

    if request.method == "POST":
        form = DaycareForm(data=request.POST)
        if form.is_valid():
            daycare = form.save()

            return redirect('/')
    else:
        form = DaycareForm(instance=daycare)

    return render(request, 'core/daycare/create.html', {'form':form,'google_maps_key':settings.GOOGLE_MAPS_API_KEY})


def daycare_delete(request,pk):
    daycare = Daycare.objects.get(pk=pk)
    if request.method == "POST":
        daycare.delete()
        # todo add success message
        return redirect('/')

    return render(request, 'core/daycare/delete.html', {
        'daycare':daycare,
        'google_maps_key':settings.GOOGLE_MAPS_API_KEY
    })


def daycare_contact_create(request,pk):
    if request.method == "POST":
        form = DaycareForm(data=request.POST)
        if form.is_valid():
            daycare = form.save()


            return redirect('/daycares/')
    else:
        form = DaycareForm()

    return render(request, 'core/daycare/create.html', {'form':form})


def daycare_owner_edit(request,pk):
    daycare = Daycare.objects.get(pk=pk)

    return render(request, 'core/owner/detail.html',{'owner':daycare.owner})


def daycare_view(request, pk):
    daycare = get_object_or_404(Daycare, pk=pk)


    in_projection = Proj(init='epsg:4326')
    out_projection = Proj(init='epsg:3857')

    x, y = transform(in_projection, out_projection, daycare.location.coordinate.x, daycare.location.coordinate.y)

    context = {
        'daycare': daycare,
        'lat': y,
        'lng': x
    }

    return render(request, 'core/daycare/detail.html', context)


def daycare_images(request, pk):
    context = {
        'daycare': get_object_or_404(Daycare, pk=pk)
    }

    return render(request, 'core/daycare/images.html', context)


def daycare_contacts(request, pk):
    context = {
        'daycare': get_object_or_404(Daycare, pk=pk)
    }

    return render(request, 'core/daycare/contacts.html', context)


def daycare_list(request,sub_domain=None):

    in_projection = Proj(init='epsg:4326')
    out_projection = Proj(init='epsg:3857')

    if sub_domain:
        daycares = Daycare.objects.filter(organisation=request.organisation)
    else:
        daycares = Daycare.objects.filter()

    data = []

    # data = { 'data': data }
    for daycare in daycares:
        daycare_ = dict()

        x, y = transform(in_projection, out_projection, daycare.location.coordinate.x, daycare.location.coordinate.y)

        daycare_['lat'] = y
        daycare_['lng'] = x

        daycare_['id'] = daycare.pk
        daycare_['name'] = daycare.name

        data.append(daycare_)

    # contact_groups = ContactGroup.objects.all().order_by('-id')
    # return render(request, 'core/daycare/daycare_list.html', data)
    return JsonResponse(data,safe=False)

from core.forms import AdminForm


def admin_create(request):
    if request.method == "POST":
        form = AdminForm(data=request.POST)

        if form.is_valid():
            admin = form.save()

            return redirect('/')
    else:
        form = AdminForm()

    return render(request, 'core/admin/create.html', {'form':form})

from core.forms import OrganisationForm


def organisation_create(request):
    if request.method == "POST":
        form = OrganisationForm(data=request.POST)
        if form.is_valid():
            organisation = form.save()

            return redirect('/organisations/')
    else:
        form = OrganisationForm()

    return render(request, 'core/organisation/create.html', {'form':form})


def organisation_list(request):

    return render(request, 'core/organisation/list.html', {'organisations':Organisation.objects.all()})
