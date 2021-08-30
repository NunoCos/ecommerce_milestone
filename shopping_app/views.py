from django.shortcuts import render


def homePageView(request):
    return render(request, 'site/index.html')
