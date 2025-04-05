import seaborn as sns
import io
import base64
import matplotlib.pyplot as plt


def pie_plot(
        data=None,
        labels=None,
        title='Pie Chart',
        colors=None,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True,
):
    if data is None or labels is None:
        raise ValueError("data and labels cannot be None")

    # Create figure and axis
    fig, ax = sns.subplots(figsize=(16, 9))

    # Plot pie chart
    ax.pie(
        data,
        labels=labels,
        colors=colors,
        autopct=autopct,
        startangle=startangle,
        shadow=shadow
    )

    # Set title
    ax.set_title(title)

    # Save plot to BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    # Encode image in base64
    encoded_image = base64.b64encode(buffer.getvalue()).decode(
        'utf-8',
        'replace'
    )

    return f"data:image/png;base64,{encoded_image}"


def line_plot_both(
        labels=None,
        title='Line Chart',
        y_label='Y Axis',
        y_2_label='Y 2 Axis',
        x_data=None,
        y_data=None,
        y_2_data=None,
):

    # Set Seaborn theme
    # sns.set_theme(style="darkgrid")

    # Create figure and axis with specified size
    fig, ax = plt.subplots(figsize=(20, 10))
    # sns.set(rc={'figure.figsize': (20, 6)})
    # Create a line plot with two lines
    ax.plot(x_data, y_data, label=y_label or 'X Axis', color='blue')
    ax.plot(x_data, y_2_data, label=y_2_label or 'Y Axis', color='orange')

    # Add legend and labels
    ax.legend()
    ax.set_title(title)

    # Save plot to BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    # Encode image in base64
    encoded_image = base64.b64encode(
        buffer.getvalue()).decode('utf-8', 'replace')

    return f"data:image/png;base64,{encoded_image}"
