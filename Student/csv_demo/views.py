from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.views import View
from .models import Examination
import io, csv
import time


class StudentUploadView(View):
    def get(self, request):
        template_name = 'employee/importemployee.html'
        return render(request, template_name)

    def post(self, request):
        start_time = time.time()
        paramFile = io.TextIOWrapper(request.FILES['employeefile'].file)
        #print(paramFile,"paramFile")
        portfolio1 = csv.DictReader(paramFile)
        #print(portfolio1,"portfolio1")
        list_of_dict = list(portfolio1)
        #print(list_of_dict,"list_of_dict")
        objs = [
            Examination(
                rollnumber=row['rollnumber'],
                first=row['first'],
                last=row['last'],
                marks=row['marks'],
            )
            for row in list_of_dict
        ]
        try:
            msg = Examination.objects.bulk_create(objs)
           # Examination.objects.all().delete()
            returnmsg = {"status_code": 200}
            print('imported successfully')
        except Exception as e:
            print('Error While Importing Data: ', e)
            returnmsg = {"status_code": 500}
        print("--- %s seconds ---" % (time.time() - start_time))
        return JsonResponse(returnmsg)