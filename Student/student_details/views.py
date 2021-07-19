from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    return render(request, 'students/register.html')




#
# from django.shortcuts import HttpResponse
# from .models import Student, Qualification
#
# def student_form(request):
#     if request.POST:
#         data = request.POST
#         required_fields=["name","email_id","address","ph_no","gender","age"]
#         for r_data in required_fields:
#             if r_data not in data:
#                 return HttpResponse(f"(r_data) is missing")
#             if r_data == "name":
#                 if len(data(r_data)) < 3 and len(data(r_data) > 100):
#                     return HttpResponse("name length between 3 and 100")
#                 if type("name")!= str:
#                     return HttpResponse("name must be in string format")
#             if r_data == "emaild_id":
#                 if data[r_data].split(".")[l] not in ["com", "net"]:
#                     return HttpResponse("email id is not in email format")
#                 if Student.objects.filter(email_id = data["email_id"]).exists():
#                     return HttpResponse("email id already exists")
#             if r_data == "ph_no":
#                 if len(data[r_data]) != 10:
#                     return HttpResponse(f"(r_data) length must be in 10 char only")
#                 if not data[r_data].isnumber():
#                     return HttpResponse(f"(r_data) must be in number format only")
#                 if data[r_data][0] not in ["6","7","8","9"]:
#                     return HttpResponse(f"(r_data) starting digit 6 7 8 9")
#             if r_data == "age":
#                 if data(r_data)<18 and data(r_data)>40:
#                     return HttpResponse("age between 18 and 40")\
#
#
#         student=Student()
#         student.name=data["name"]
#         student.address=data["address"]
#         student.email_id =data["email_id"]
