from utils.fetch_util import fetch_data_from_api


def data():
    fetched_data = fetch_data_from_api(
        'https://raw.githubusercontent.com/codershubinc/trade_data/refs/heads/main/high_low/ETF_profile.json')

    if fetched_data is None:
        return demo_api_data

    # Extract relevant data

    sectors = fetched_data['sectors']
    holdings = fetched_data['holdings']

    return {
        'sectors': sectors,
        'holdings': holdings,
    }


demo_api_data = {
    "net_assets": "323800000000",
    "net_expense_ratio": "0.002",
    "portfolio_turnover": "0.08",
    "dividend_yield": "0.0055",
    "inception_date": "1999-03-10",
    "leveraged": "NO",
    "sectors": [
        {
            "sector": "INFORMATION TECHNOLOGY",
            "weight": "0.488"
        },
        {
            "sector": "COMMUNICATION SERVICES",
            "weight": "0.162"
        },
        {
            "sector": "CONSUMER DISCRETIONARY",
            "weight": "0.127"
        },
        {
            "sector": "CONSUMER STAPLES",
            "weight": "0.056"
        },
        {
            "sector": "HEALTHCARE",
            "weight": "0.054"
        },
        {
            "sector": "INDUSTRIALS",
            "weight": "0.049"
        },
        {
            "sector": "MATERIALS",
            "weight": "0.015"
        },
        {
            "sector": "UTILITIES",
            "weight": "0.014"
        },
        {
            "sector": "ENERGY",
            "weight": "0.006"
        },
        {
            "sector": "FINANCIALS",
            "weight": "0.005"
        }
    ],
    "holdings": [
        {
            "symbol": "AAPL",
            "description": "APPLE INC",
            "weight": "0.0906"
        },
        {
            "symbol": "MSFT",
            "description": "MICROSOFT CORP",
            "weight": "0.0789"
        },
        {
            "symbol": "NVDA",
            "description": "NVIDIA CORP",
            "weight": "0.0756"
        },
        {
            "symbol": "AMZN",
            "description": "AMAZON.COM INC",
            "weight": "0.058"
        },
        {
            "symbol": "AVGO",
            "description": "BROADCOM INC",
            "weight": "0.0378"
        },
        {
            "symbol": "META",
            "description": "META PLATFORMS INC CLASS A",
            "weight": "0.0364"
        },
        {
            "symbol": "NFLX",
            "description": "NETFLIX INC",
            "weight": "0.0278"
        },
        {
            "symbol": "COST",
            "description": "COSTCO WHOLESALE CORP",
            "weight": "0.0276"
        },
        {
            "symbol": "TSLA",
            "description": "TESLA INC",
            "weight": "0.0269"
        },
        {
            "symbol": "GOOGL",
            "description": "ALPHABET INC CLASS A",
            "weight": "0.0262"
        },
        {
            "symbol": "GOOG",
            "description": "ALPHABET INC CLASS C",
            "weight": "0.025"
        },
        {
            "symbol": "TMUS",
            "description": "T-MOBILE US INC",
            "weight": "0.0201"
        },
        {
            "symbol": "CSCO",
            "description": "CISCO SYSTEMS INC",
            "weight": "0.0165"
        },
        {
            "symbol": "LIN",
            "description": "LINDE PLC",
            "weight": "0.0146"
        },
        {
            "symbol": "PLTR",
            "description": "n/a",
            "weight": "0.0139"
        },
        {
            "symbol": "PEP",
            "description": "PEPSICO INC",
            "weight": "0.0137"
        },
        {
            "symbol": "ISRG",
            "description": "INTUITIVE SURGICAL INC",
            "weight": "0.0122"
        },
        {
            "symbol": "AMD",
            "description": "ADVANCED MICRO DEVICES INC",
            "weight": "0.012"
        },
        {
            "symbol": "QCOM",
            "description": "QUALCOMM INC",
            "weight": "0.0117"
        },
        {
            "symbol": "ADBE",
            "description": "ADOBE INC",
            "weight": "0.0116"
        },
        {
            "symbol": "INTU",
            "description": "INTUIT INC",
            "weight": "0.0115"
        },
        {
            "symbol": "TXN",
            "description": "TEXAS INSTRUMENTS INC",
            "weight": "0.0112"
        },
        {
            "symbol": "AMGN",
            "description": "AMGEN INC",
            "weight": "0.011"
        },
        {
            "symbol": "BKNG",
            "description": "BOOKING HOLDINGS INC",
            "weight": "0.0105"
        },
        {
            "symbol": "CMCSA",
            "description": "COMCAST CORP CLASS A",
            "weight": "0.0094"
        },
        {
            "symbol": "HON",
            "description": "HONEYWELL INTERNATIONAL INC",
            "weight": "0.0093"
        },
        {
            "symbol": "GILD",
            "description": "GILEAD SCIENCES INC",
            "weight": "0.0091"
        },
        {
            "symbol": "VRTX",
            "description": "VERTEX PHARMACEUTICALS INC",
            "weight": "0.0086"
        },
        {
            "symbol": "ADP",
            "description": "AUTOMATIC DATA PROCESSING INC",
            "weight": "0.0082"
        },
        {
            "symbol": "AMAT",
            "description": "APPLIED MATERIALS INC",
            "weight": "0.0082"
        },
        {
            "symbol": "PANW",
            "description": "PALO ALTO NETWORKS INC",
            "weight": "0.0082"
        },
        {
            "symbol": "SBUX",
            "description": "STARBUCKS CORP",
            "weight": "0.0075"
        },
        {
            "symbol": "ADI",
            "description": "ANALOG DEVICES INC",
            "weight": "0.007"
        },
        {
            "symbol": "MELI",
            "description": "MERCADOLIBRE INC",
            "weight": "0.007"
        },
        {
            "symbol": "MU",
            "description": "MICRON TECHNOLOGY INC",
            "weight": "0.0069"
        },
        {
            "symbol": "APP",
            "description": "APPLOVIN CORP ORDINARY SHARES CLASS A",
            "weight": "0.0068"
        },
        {
            "symbol": "INTC",
            "description": "INTEL CORP",
            "weight": "0.0068"
        },
        {
            "symbol": "LRCX",
            "description": "LAM RESEARCH CORP",
            "weight": "0.0065"
        },
        {
            "symbol": "KLAC",
            "description": "KLA CORP",
            "weight": "0.0063"
        },
        {
            "symbol": "CRWD",
            "description": "CROWDSTRIKE HOLDINGS INC CLASS A",
            "weight": "0.0058"
        },
        {
            "symbol": "MDLZ",
            "description": "MONDELEZ INTERNATIONAL INC CLASS A",
            "weight": "0.0057"
        },
        {
            "symbol": "PDD",
            "description": "PDD HOLDINGS INC ADR",
            "weight": "0.0055"
        },
        {
            "symbol": "CTAS",
            "description": "CINTAS CORP",
            "weight": "0.0055"
        },
        {
            "symbol": "ORLY",
            "description": "O'REILLY AUTOMOTIVE INC",
            "weight": "0.0053"
        },
        {
            "symbol": "MSTR",
            "description": "MICROSTRATEGY INC CLASS A",
            "weight": "0.0052"
        },
        {
            "symbol": "FTNT",
            "description": "FORTINET INC",
            "weight": "0.0052"
        },
        {
            "symbol": "DASH",
            "description": "DOORDASH INC ORDINARY SHARES CLASS A",
            "weight": "0.0051"
        },
        {
            "symbol": "CDNS",
            "description": "CADENCE DESIGN SYSTEMS INC",
            "weight": "0.0048"
        },
        {
            "symbol": "SNPS",
            "description": "SYNOPSYS INC",
            "weight": "0.0047"
        },
        {
            "symbol": "PYPL",
            "description": "PAYPAL HOLDINGS INC",
            "weight": "0.0046"
        },
        {
            "symbol": "REGN",
            "description": "REGENERON PHARMACEUTICALS INC",
            "weight": "0.0046"
        },
        {
            "symbol": "MAR",
            "description": "MARRIOTT INTERNATIONAL INC CLASS A",
            "weight": "0.0046"
        },
        {
            "symbol": "CEG",
            "description": "CONSTELLATION ENERGY CORP",
            "weight": "0.0045"
        },
        {
            "symbol": "ASML",
            "description": "ASML HOLDING NV ADR",
            "weight": "0.0043"
        },
        {
            "symbol": "ROP",
            "description": "ROPER TECHNOLOGIES INC",
            "weight": "0.0042"
        },
        {
            "symbol": "MRVL",
            "description": "MARVELL TECHNOLOGY INC",
            "weight": "0.0039"
        },
        {
            "symbol": "ADSK",
            "description": "AUTODESK INC",
            "weight": "0.0039"
        },
        {
            "symbol": "CSX",
            "description": "CSX CORP",
            "weight": "0.0038"
        },
        {
            "symbol": "MNST",
            "description": "MONSTER BEVERAGE CORP",
            "weight": "0.0038"
        },
        {
            "symbol": "ABNB",
            "description": "AIRBNB INC ORDINARY SHARES CLASS A",
            "weight": "0.0037"
        },
        {
            "symbol": "AEP",
            "description": "AMERICAN ELECTRIC POWER CO INC",
            "weight": "0.0037"
        },
        {
            "symbol": "CHTR",
            "description": "CHARTER COMMUNICATIONS INC CLASS A",
            "weight": "0.0037"
        },
        {
            "symbol": "PAYX",
            "description": "PAYCHEX INC",
            "weight": "0.0036"
        },
        {
            "symbol": "WDAY",
            "description": "WORKDAY INC CLASS A",
            "weight": "0.0036"
        },
        {
            "symbol": "CPRT",
            "description": "COPART INC",
            "weight": "0.0036"
        },
        {
            "symbol": "PCAR",
            "description": "PACCAR INC",
            "weight": "0.0035"
        },
        {
            "symbol": "NXPI",
            "description": "NXP SEMICONDUCTORS NV",
            "weight": "0.0035"
        },
        {
            "symbol": "FANG",
            "description": "DIAMONDBACK ENERGY INC",
            "weight": "0.0032"
        },
        {
            "symbol": "KDP",
            "description": "KEURIG DR PEPPER INC",
            "weight": "0.0031"
        },
        {
            "symbol": "FAST",
            "description": "FASTENAL CO",
            "weight": "0.003"
        },
        {
            "symbol": "EXC",
            "description": "EXELON CORP",
            "weight": "0.003"
        },
        {
            "symbol": "BKR",
            "description": "BAKER HUGHES CO CLASS A",
            "weight": "0.0029"
        },
        {
            "symbol": "AXON",
            "description": "AXON ENTERPRISE INC",
            "weight": "0.0029"
        },
        {
            "symbol": "AZN",
            "description": "ASTRAZENECA PLC ADR",
            "weight": "0.0028"
        },
        {
            "symbol": "ROST",
            "description": "ROSS STORES INC",
            "weight": "0.0028"
        },
        {
            "symbol": "VRSK",
            "description": "VERISK ANALYTICS INC",
            "weight": "0.0027"
        },
        {
            "symbol": "CCEP",
            "description": "COCA-COLA EUROPACIFIC PARTNERS PLC",
            "weight": "0.0026"
        },
        {
            "symbol": "TTWO",
            "description": "TAKE-TWO INTERACTIVE SOFTWARE INC",
            "weight": "0.0026"
        },
        {
            "symbol": "XEL",
            "description": "XCEL ENERGY INC",
            "weight": "0.0026"
        },
        {
            "symbol": "CTSH",
            "description": "COGNIZANT TECHNOLOGY SOLUTIONS CORP CLASS A",
            "weight": "0.0026"
        },
        {
            "symbol": "LULU",
            "description": "LULULEMON ATHLETICA INC",
            "weight": "0.0026"
        },
        {
            "symbol": "EA",
            "description": "ELECTRONIC ARTS INC",
            "weight": "0.0025"
        },
        {
            "symbol": "TEAM",
            "description": "ATLASSIAN CORP A",
            "weight": "0.0025"
        },
        {
            "symbol": "GEHC",
            "description": "GE HEALTHCARE TECHNOLOGIES INC COMMON STOCK",
            "weight": "0.0025"
        },
        {
            "symbol": "KHC",
            "description": "THE KRAFT HEINZ CO",
            "weight": "0.0024"
        },
        {
            "symbol": "ODFL",
            "description": "OLD DOMINION FREIGHT LINE INC ORDINARY SHARES",
            "weight": "0.0024"
        },
        {
            "symbol": "IDXX",
            "description": "IDEXX LABORATORIES INC",
            "weight": "0.0023"
        },
        {
            "symbol": "DDOG",
            "description": "DATADOG INC CLASS A",
            "weight": "0.0023"
        },
        {
            "symbol": "ZS",
            "description": "ZSCALER INC",
            "weight": "0.0022"
        },
        {
            "symbol": "CSGP",
            "description": "COSTAR GROUP INC",
            "weight": "0.0022"
        },
        {
            "symbol": "MCHP",
            "description": "MICROCHIP TECHNOLOGY INC",
            "weight": "0.0019"
        },
        {
            "symbol": "DXCM",
            "description": "DEXCOM INC",
            "weight": "0.0019"
        },
        {
            "symbol": "ANSS",
            "description": "ANSYS INC",
            "weight": "0.0019"
        },
        {
            "symbol": "WBD",
            "description": "WARNER BROS. DISCOVERY INC ORDINARY SHARES CLASS A",
            "weight": "0.0018"
        },
        {
            "symbol": "TTD",
            "description": "THE TRADE DESK INC CLASS A",
            "weight": "0.0018"
        },
        {
            "symbol": "CDW",
            "description": "CDW CORP",
            "weight": "0.0015"
        },
        {
            "symbol": "BIIB",
            "description": "BIOGEN INC",
            "weight": "0.0014"
        },
        {
            "symbol": "GFS",
            "description": "GLOBALFOUNDRIES INC",
            "weight": "0.0014"
        },
        {
            "symbol": "ON",
            "description": "ON SEMICONDUCTOR CORP",
            "weight": "0.0013"
        },
        {
            "symbol": "ARM",
            "description": "ARM HOLDINGS PLC ADR",
            "weight": "0.001"
        },
        {
            "symbol": "MDB",
            "description": "MONGODB INC CLASS A",
            "weight": "0.001"
        }
    ]
}
