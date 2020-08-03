import django_filters
from django.http import HttpRequest, HttpResponse
from rest_framework import generics
from rest_framework.renderers import JSONOpenAPIRenderer, AdminRenderer
from rest_framework.response import Response

from .models import Users
from .serializers import UserSerializer
import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
class UserView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['RegistrationDate', ]
    renderer_classes = [AdminRenderer, JSONOpenAPIRenderer]


    @login_required(login_url='/api-auth/login/')
    def upload_csv(request):
        # declaring template
        template = "user_upload.html"
        data = Users.objects.all()
        prompt = {
            'order': 'Order of the CSV should be FirstName, LastName, BirthDate, RegistrationDate (date in YYYY/MM/DD format)',
            'profiles': data
        }

        if request.method == "GET":
            return render(request, template, prompt)
        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
            return render(request, template)

        try:
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=','):
                user = Users(
                    FirstName=column[0],
                    LastName=column[1],
                    BirthDate=column[2].replace('/', '-'),
                    RegistrationDate=column[3].replace('/', '-'))
                user.save(force_insert=True)
            return render(request, template)

        except Exception:
            messages.error(request, 'Cannot parse file')
            return render(request, template)
