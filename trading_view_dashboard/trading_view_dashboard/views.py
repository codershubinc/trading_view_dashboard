from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from utils.fetch_util import fetch_data_from_api
from utils.matplotlib_util import plot
from utils.company_info import get_company_info
from utils.graph_util import high_low_price_graph
from constants.shares_symbols import symbols


def home(request):
    return render(request, 'main.html', {
        'symbols': symbols
    })


def about(request, sym):
    data = fetch_data_from_api(
        'https://raw.githubusercontent.com/codershubinc/trade_data/refs/heads/main/high_low/{sym}.json')
    return JsonResponse(data, safe=False)


def contact(request):
    data = fetch_data_from_api(
        'https://openapi.codershubinc.tech/v0.1/random_user')
    # Extract avatar URL from the API response
    avatar_url = data['data']['user']['avatar']
    return HttpResponse(f"<img src='{avatar_url}' alt='Contact' />")


def plot_template_view(request, symbol):
    days = request.GET.get('days', 10)
    graph_type = request.GET.get('graph', 'high')  # Default to 'high' graph

    # Fetch company information (using demo_data for now)
    company_info = get_company_info(symbol)

    # Generate the appropriate graph based on the graph_type
    plot_image = high_low_price_graph(
        symbol,
        days,
        graph_type
    )

    return render(request, "plot/plot.html", {
        "plot_image": plot_image,
        "symbol": symbol,
        "company_info": company_info,
        "graph_type": graph_type,
    })
