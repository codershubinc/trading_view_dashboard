import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime


def plot_to_base64():
    # Create figure and axis
    fig, ax = plt.subplots()

    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 9, 12]

    # Plot data
    ax.plot(x, y, marker='o', linestyle='-')

    # Set labels
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_title('Sample Plot')

    # Save to BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    # Encode in base64
    encoded_image = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{encoded_image}"


def plot_stock_high_prices():
    data = [
        {
            "date": "2025-01-06",
            "high": 247.33
        },
        {
            "date": "2025-01-07",
            "high": 245.55
        },
        {
            "date": "2025-01-08",
            "high": 243.71
        },
        {
            "date": "2025-01-10",
            "high": 240.16
        },
        {
            "date": "2025-01-13",
            "high": 234.67
        },
        {
            "date": "2025-01-14",
            "high": 236.12
        },
        {
            "date": "2025-01-15",
            "high": 238.96
        },
        {
            "date": "2025-01-16",
            "high": 238.01
        },
        {
            "date": "2025-01-17",
            "high": 232.29
        },
        {
            "date": "2025-01-21",
            "high": 224.42
        },
        {
            "date": "2025-01-22",
            "high": 224.12
        },
        {
            "date": "2025-01-23",
            "high": 227.03
        },
        {
            "date": "2025-01-24",
            "high": 225.63
        },
        {
            "date": "2025-01-27",
            "high": 232.15
        },
        {
            "date": "2025-01-28",
            "high": 240.19
        },
        {
            "date": "2025-01-29",
            "high": 239.86
        },
        {
            "date": "2025-01-30",
            "high": 240.79
        },
        {
            "date": "2025-01-31",
            "high": 247.19
        },
        {
            "date": "2025-02-03",
            "high": 231.83
        },
        {
            "date": "2025-02-04",
            "high": 233.13
        },
        {
            "date": "2025-02-05",
            "high": 232.67
        },
        {
            "date": "2025-02-06",
            "high": 233.8
        },
        {
            "date": "2025-02-07",
            "high": 234},

        {
            "date": "2025-02-10",
            "high": 230.59
        },
        {
            "date": "2025-02-11",
            "high": 235.23
        },
        {
            "date": "2025-02-12",
            "high": 236.96
        },
        {
            "date": "2025-02-13",
            "high": 242.34
        },
        {
            "date": "2025-02-14",
            "high": 245.55
        },
    ]
    # Extract dates and high prices
    dates = [datetime.strptime(entry["date"], "%Y-%m-%d") for entry in data]
    high_prices = [entry["high"] for entry in data]

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.plot(
        dates,
        high_prices,
        marker='o',
        linestyle='-', color='b', label='High Prices',
        markersize=5, linewidth=2
    )

    # Formatting the plot
    ax.set_xlabel("Date")
    ax.set_ylabel("High Price")
    ax.set_title("Stock High Prices vs Date")
    ax.legend()
    # ax.grid()
    plt.xticks(rotation=45)

    # Save to BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    # Encode in base64
    encoded_image = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{encoded_image}"
