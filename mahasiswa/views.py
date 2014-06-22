from django.shortcuts import render
from django.http import HttpResponse
from mahasiswa.models import Pemohon_Terpilih
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404
from django_tables2 import RequestConfig


def index(request):
    return render(request, "penerima-beasiswa.html", {"index": Pemohon_Terpilih.objects.all()})