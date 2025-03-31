import requests


def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.json()  # Return JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
