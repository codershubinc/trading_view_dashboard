from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to trading_view_dashboard Project: <br/> Home page</h1>")


def about(request):
    return HttpResponse("<h1>Welcome to trading_view_dashboard Project: <br/> About page</h1>")


def contact(request):
    return HttpResponse("<h1 style='color:red' >Welcome to trading_view_dashboard Project: <br/> Contact page</h1>")
