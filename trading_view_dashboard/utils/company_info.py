from utils.fetch_util import fetch_data_from_api


def get_company_info(symbol: str):
    # Fetch data from the API
    data = fetch_data_from_api(
        f'https://raw.githubusercontent.com/codershubinc/trade_data/refs/heads/main/overview/{symbol}.json')
    return data


demo_data = {
    "Symbol": "AAME",
    "AssetType": "Common Stock",
    "Name": "Atlantic American Corporation",
    "Description": "Atlantic American Corporation provides life and health insurance and property and casualty products in the United States. The company is headquartered in Atlanta, Georgia.",
    "CIK": "8177",
    "Exchange": "NASDAQ",
    "Currency": "USD",
    "Country": "USA",
    "Sector": "FINANCE",
    "Industry": "LIFE INSURANCE",
    "Address": "4370 PEACHTREE RD NE, ATLANTA, GA, US",
    "OfficialSite": "https://www.atlam.com",
    "FiscalYearEnd": "December",
    "LatestQuarter": "2024-09-30",
    "MarketCapitalization": "32639700",
    "EBITDA": "-352000",
    "PERatio": "None",
    "PEGRatio": "0",
    "BookValue": "5.25",
    "DividendPerShare": "0",
    "DividendYield": "0.0118",
    "EPS": "-0.36",
    "RevenuePerShareTTM": "9.12",
    "ProfitMargin": "-0.0169",
    "OperatingMarginTTM": "0.0004",
    "ReturnOnAssetsTTM": "-0.0015",
    "ReturnOnEquityTTM": "-0.0309",
    "RevenueTTM": "186001000",
    "GrossProfitTTM": "20364000",
    "DilutedEPSTTM": "-0.36",
    "QuarterlyEarningsGrowthYOY": "-0.784",
    "QuarterlyRevenueGrowthYOY": "-0.031",
    "AnalystTargetPrice": "None",
    "AnalystRatingStrongBuy": "-",
    "AnalystRatingBuy": "-",
    "AnalystRatingHold": "-",
    "AnalystRatingSell": "-",
    "AnalystRatingStrongSell": "-",
    "TrailingPE": "-",
    "ForwardPE": "-",
    "PriceToSalesRatioTTM": "0.169",
    "PriceToBookRatio": "0.32",
    "EVToRevenue": "0.181",
    "EVToEBITDA": "-",
    "Beta": "0.462",
    "52WeekHigh": "2.304",
    "52WeekLow": "1.248",
    "50DayMovingAverage": "1.648",
    "200DayMovingAverage": "1.89",
    "SharesOutstanding": "20399800",
    "DividendDate": "2024-04-26",
    "ExDividendDate": "2024-04-11"
}
