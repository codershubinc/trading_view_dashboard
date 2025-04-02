from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from utils.fetch_util import fetch_data_from_api
from utils.matplotlib import plot_to_base64, plot_stock_high_prices


def home(request):
    return render(request, 'index.html')


def about(request):
    data = fetch_data_from_api(
        'https://eodhd.com/api/eod/AAPL.US?period=d&api_token=demo&format=json&from=2025-01-05&to2025-03-01')
    return JsonResponse(data, safe=False)


def contact(request):
    data = fetch_data_from_api(
        'https://openapi.codershubinc.tech/v0.1/random_user')
    # Extract avatar URL from the API response
    avatar_url = data['data']['user']['avatar']
    return HttpResponse(f"<img src='{avatar_url}' alt='Contact' />")


def plot_template_view(request):
    image_data = plot_stock_high_prices()
    return render(request, 'plot/plot.html', {'image': image_data})
