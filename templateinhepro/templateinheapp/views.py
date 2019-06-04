from django.shortcuts import render


def base_page_view(request):
    return render (request,'base_home.html')


def home_page_view(request):
    return render(request,'base_home_page.html')


def contact_page_view(request):
    return render(request,'base_contact_page.html')


def services_page_view(request):
    return render(request,'base_services_page.html')


def feedback_page_view(request):
    return render(request,'base_feedback_page.html')