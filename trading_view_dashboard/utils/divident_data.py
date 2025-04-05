from utils.fetch_util import fetch_data_from_api


def get_dividend_data(symbol: str) -> dict:

    fetched_data = fetch_data_from_api(
        f'https://raw.githubusercontent.com/codershubinc/trade_data/refs/heads/main/dividend/{symbol}.json'
    )
    if fetched_data is None:
        return demo_api_data

    dividend_payment_date = []
    payed_dividend_amount = []

    for item in fetched_data['data']:
        dividend_payment_date.append(item['payment_date'])
        payed_dividend_amount.append(item['amount'])
    dividend_data = {
        'dividend_payment_date': dividend_payment_date,
        'payed_dividend_amount': payed_dividend_amount
    }
    return dividend_data


demo_api_data = {
    "symbol": "IBM",
    "data": [
        {
            "ex_dividend_date": "2025-02-10",
            "declaration_date": "2025-01-28",
            "record_date": "2025-02-10",
            "payment_date": "2025-03-10",
            "amount": "1.67"
        },
        {
            "ex_dividend_date": "2024-11-12",
            "declaration_date": "2024-10-30",
            "record_date": "2024-11-12",
            "payment_date": "2024-12-10",
            "amount": "1.67"
        },
        {
            "ex_dividend_date": "2024-08-09",
            "declaration_date": "2024-07-29",
            "record_date": "2024-08-09",
            "payment_date": "2024-09-10",
            "amount": "1.67"
        },
        {
            "ex_dividend_date": "2024-05-09",
            "declaration_date": "2024-04-30",
            "record_date": "2024-05-10",
            "payment_date": "2024-06-10",
            "amount": "1.67"
        },
        {
            "ex_dividend_date": "2024-02-08",
            "declaration_date": "2024-01-30",
            "record_date": "2024-02-09",
            "payment_date": "2024-03-09",
            "amount": "1.66"
        },
        {
            "ex_dividend_date": "2023-11-09",
            "declaration_date": "2023-10-30",
            "record_date": "2023-11-10",
            "payment_date": "2023-12-09",
            "amount": "1.66"
        },
        {
            "ex_dividend_date": "2023-08-09",
            "declaration_date": "2023-07-24",
            "record_date": "2023-08-10",
            "payment_date": "2023-09-09",
            "amount": "1.66"
        },
        {
            "ex_dividend_date": "2023-05-09",
            "declaration_date": "2023-04-25",
            "record_date": "2023-05-10",
            "payment_date": "2023-06-10",
            "amount": "1.66"
        },
        {
            "ex_dividend_date": "2023-02-09",
            "declaration_date": "2023-01-31",
            "record_date": "2023-02-10",
            "payment_date": "2023-03-10",
            "amount": "1.65"
        },
        {
            "ex_dividend_date": "2022-11-09",
            "declaration_date": "2022-10-25",
            "record_date": "2022-11-10",
            "payment_date": "2022-12-10",
            "amount": "1.65"
        },
        {
            "ex_dividend_date": "2022-08-09",
            "declaration_date": "2022-07-25",
            "record_date": "2022-08-10",
            "payment_date": "2022-09-10",
            "amount": "1.65"
        },
        {
            "ex_dividend_date": "2022-05-09",
            "declaration_date": "2022-04-26",
            "record_date": "2022-05-10",
            "payment_date": "2022-06-10",
            "amount": "1.65"
        },
        {
            "ex_dividend_date": "2022-02-10",
            "declaration_date": "2022-02-01",
            "record_date": "2022-02-11",
            "payment_date": "2022-03-10",
            "amount": "1.64"
        },
        {
            "ex_dividend_date": "2021-11-09",
            "declaration_date": "2021-10-26",
            "record_date": "2021-11-10",
            "payment_date": "2021-12-10",
            "amount": "1.64"
        },
        {
            "ex_dividend_date": "2021-08-09",
            "declaration_date": "2021-07-27",
            "record_date": "2021-08-10",
            "payment_date": "2021-09-10",
            "amount": "1.64"
        },
        {
            "ex_dividend_date": "2021-05-07",
            "declaration_date": "2021-04-27",
            "record_date": "2021-05-10",
            "payment_date": "2021-06-10",
            "amount": "1.64"
        },
        {
            "ex_dividend_date": "2021-02-09",
            "declaration_date": "2021-01-26",
            "record_date": "2021-02-10",
            "payment_date": "2021-03-10",
            "amount": "1.63"
        },
        {
            "ex_dividend_date": "2020-11-09",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.63"
        },
        {
            "ex_dividend_date": "2020-08-07",
            "declaration_date": "2020-07-28",
            "record_date": "2020-08-10",
            "payment_date": "2020-09-10",
            "amount": "1.63"
        },
        {
            "ex_dividend_date": "2020-05-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.63"
        },
        {
            "ex_dividend_date": "2020-02-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.62"
        },
        {
            "ex_dividend_date": "2019-11-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.62"
        },
        {
            "ex_dividend_date": "2019-08-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.62"
        },
        {
            "ex_dividend_date": "2019-05-09",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.62"
        },
        {
            "ex_dividend_date": "2019-02-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.57"
        },
        {
            "ex_dividend_date": "2018-11-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.57"
        },
        {
            "ex_dividend_date": "2018-08-09",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.57"
        },
        {
            "ex_dividend_date": "2018-05-09",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.57"
        },
        {
            "ex_dividend_date": "2018-02-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.5"
        },
        {
            "ex_dividend_date": "2017-11-09",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.5"
        },
        {
            "ex_dividend_date": "2017-08-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.5"
        },
        {
            "ex_dividend_date": "2017-05-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.5"
        },
        {
            "ex_dividend_date": "2017-02-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.4"
        },
        {
            "ex_dividend_date": "2016-11-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.4"
        },
        {
            "ex_dividend_date": "2016-08-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.4"
        },
        {
            "ex_dividend_date": "2016-05-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.4"
        },
        {
            "ex_dividend_date": "2016-02-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.3"
        },
        {
            "ex_dividend_date": "2015-11-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.3"
        },
        {
            "ex_dividend_date": "2015-08-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.3"
        },
        {
            "ex_dividend_date": "2015-05-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.3"
        },
        {
            "ex_dividend_date": "2015-02-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.1"
        },
        {
            "ex_dividend_date": "2014-11-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.1"
        },
        {
            "ex_dividend_date": "2014-08-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.1"
        },
        {
            "ex_dividend_date": "2014-05-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "1.1"
        },
        {
            "ex_dividend_date": "2014-02-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.95"
        },
        {
            "ex_dividend_date": "2013-11-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.95"
        },
        {
            "ex_dividend_date": "2013-08-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.95"
        },
        {
            "ex_dividend_date": "2013-05-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.95"
        },
        {
            "ex_dividend_date": "2013-02-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.85"
        },
        {
            "ex_dividend_date": "2012-11-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.85"
        },
        {
            "ex_dividend_date": "2012-08-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.85"
        },
        {
            "ex_dividend_date": "2012-05-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.85"
        },
        {
            "ex_dividend_date": "2012-02-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.75"
        },
        {
            "ex_dividend_date": "2011-11-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.75"
        },
        {
            "ex_dividend_date": "2011-08-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.75"
        },
        {
            "ex_dividend_date": "2011-05-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.75"
        },
        {
            "ex_dividend_date": "2011-02-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.65"
        },
        {
            "ex_dividend_date": "2010-11-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.65"
        },
        {
            "ex_dividend_date": "2010-08-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.65"
        },
        {
            "ex_dividend_date": "2010-05-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.65"
        },
        {
            "ex_dividend_date": "2010-02-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.55"
        },
        {
            "ex_dividend_date": "2009-11-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.55"
        },
        {
            "ex_dividend_date": "2009-08-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.55"
        },
        {
            "ex_dividend_date": "2009-05-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.55"
        },
        {
            "ex_dividend_date": "2009-02-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.5"
        },
        {
            "ex_dividend_date": "2008-11-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.5"
        },
        {
            "ex_dividend_date": "2008-08-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.5"
        },
        {
            "ex_dividend_date": "2008-05-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.5"
        },
        {
            "ex_dividend_date": "2008-02-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.4"
        },
        {
            "ex_dividend_date": "2007-11-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.4"
        },
        {
            "ex_dividend_date": "2007-08-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.4"
        },
        {
            "ex_dividend_date": "2007-05-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.4"
        },
        {
            "ex_dividend_date": "2007-02-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.3"
        },
        {
            "ex_dividend_date": "2006-11-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.3"
        },
        {
            "ex_dividend_date": "2006-08-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.3"
        },
        {
            "ex_dividend_date": "2006-05-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.3"
        },
        {
            "ex_dividend_date": "2006-02-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.2"
        },
        {
            "ex_dividend_date": "2005-11-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.2"
        },
        {
            "ex_dividend_date": "2005-08-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.2"
        },
        {
            "ex_dividend_date": "2005-05-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.2"
        },
        {
            "ex_dividend_date": "2005-02-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.18"
        },
        {
            "ex_dividend_date": "2004-11-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.18"
        },
        {
            "ex_dividend_date": "2004-08-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.18"
        },
        {
            "ex_dividend_date": "2004-05-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.18"
        },
        {
            "ex_dividend_date": "2004-02-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.16"
        },
        {
            "ex_dividend_date": "2003-11-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.16"
        },
        {
            "ex_dividend_date": "2003-08-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.16"
        },
        {
            "ex_dividend_date": "2003-05-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.16"
        },
        {
            "ex_dividend_date": "2003-02-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.15"
        },
        {
            "ex_dividend_date": "2002-11-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.15"
        },
        {
            "ex_dividend_date": "2002-08-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.15"
        },
        {
            "ex_dividend_date": "2002-05-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.15"
        },
        {
            "ex_dividend_date": "2002-02-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.14"
        },
        {
            "ex_dividend_date": "2001-11-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.14"
        },
        {
            "ex_dividend_date": "2001-08-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.14"
        },
        {
            "ex_dividend_date": "2001-05-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.14"
        },
        {
            "ex_dividend_date": "2001-02-07",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.13"
        },
        {
            "ex_dividend_date": "2000-11-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.13"
        },
        {
            "ex_dividend_date": "2000-08-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.13"
        },
        {
            "ex_dividend_date": "2000-05-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.13"
        },
        {
            "ex_dividend_date": "2000-02-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.12"
        },
        {
            "ex_dividend_date": "1999-11-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.12"
        },
        {
            "ex_dividend_date": "1999-08-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.12"
        },
        {
            "ex_dividend_date": "1999-05-06",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.24"
        },
        {
            "ex_dividend_date": "1999-02-08",
            "declaration_date": "None",
            "record_date": "None",
            "payment_date": "None",
            "amount": "0.22"
        }
    ]
}
