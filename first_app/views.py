from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Contact


# Create your views here.


def index(request):
    return HttpResponse("Hello Django!")


def home(request):
    return render(request, "first_app/home.html")


def insert_data(request):
    Contact.objects.create(name="Tim", \
        phone_number="123", passwd="root")
    return HttpResponse("数据创建成功！")


def search_contact(request):
    contact_list = Contact.objects.all()
    return render(request, "first_app/index.html", context={"contact_list": contact_list})


def delete_contact(request, pk):
    c1 = Contact.objects.get(id=pk)
    c1.delete()
    return HttpResponse("删除成功！")


def detail(request, id):
    c = Contact.objects.get(id=id)
    return render(request, "first_app/detail.html", context={"contact": c})


def register(request):
    return render(request, 'first_app/register.html')



def deal_register(request):
    username = request.POST.get("username")
    phone_number = request.POST.get("phone_number")
    passwd = request.POST.get("passwd")
    print(username, phone_number, passwd)
    return HttpResponse("注册成功！")