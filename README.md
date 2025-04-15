# Trading View Dashboard

## Description
The Trading View Dashboard is a web application that allows users to view and analyze stock data. It provides various graph types and stock symbols for users to select and visualize.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/codershubinc/trading_view_dashboard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd trading_view_dashboard
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Set up the environment variables:
   - Create a `.env` file in the project root directory and add the following line:
     ```
     ALPHA_VANTAGE_API_KEY=YOUR_API_KEY
     ```
   - Replace `YOUR_API_KEY` with your actual Alpha Vantage API key.

## Usage Instructions
1. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
2. Open your web browser and navigate to `http://localhost:8000`.
3. Select a stock symbol from the dropdown menu and click "View Plot" to see the stock data visualization.

## Contributing Guidelines
We welcome contributions to the Trading View Dashboard project. To contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them with a descriptive commit message:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push your changes to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request to the main repository.

## License Information
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
