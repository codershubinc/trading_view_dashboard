import matplotlib.pyplot as plt
import io
import base64


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
