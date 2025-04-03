import matplotlib.pyplot as plt
import io
import base64
import numpy as np
from datetime import datetime


def plot(
        color: str = 'blue',
        marker: str = 'o',
        x_axis_data: list = None,
        y_axis_data: list = None,
        x_label: str = 'X Axis',
        y_label: str = 'Y Axis',
        title: str = 'Sample Plot',
        grid: bool = True,
        linestyle: str = 'x',
):
    if x_axis_data is None or y_axis_data is None:
        raise ValueError("x_axis_data and y_axis_data cannot be None")

    # Ensure x_axis_data and y_axis_data are cast to appropriate types
    try:
        x_axis_data = [float(x) if isinstance(x, str) and x.replace(
            '.', '', 1).isdigit() else x for x in x_axis_data]
        y_axis_data = [float(y) if isinstance(y, str) and y.replace(
            '.', '', 1).isdigit() else y for y in y_axis_data]
    except ValueError:
        raise ValueError(
            "Ensure x_axis_data and y_axis_data contain numeric or datetime-compatible values.")

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(16, 9))

    # Plot data
    ax.plot(
        x_axis_data,
        y_axis_data,
        color=color,
        marker=marker,
        linestyle=linestyle,
        markersize=5,
        linewidth=2,

    )

    # Set labels and title
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    # Format x-axis ticks dynamically
    ax.set_xticks(range(len(x_axis_data)))
    ax.set_xticklabels(x_axis_data, rotation=45)

    # Add grid if enabled
    if grid:
        ax.grid()

    # Save plot to BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    # Encode image in base64
    encoded_image = base64.b64encode(buffer.getvalue()).decode()
    return f"data:image/png;base64,{encoded_image}"
