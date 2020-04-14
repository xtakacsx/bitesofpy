import requests

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap: str):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == "n/a":
        return 0

    capital = cap.lstrip("$")

    if capital[-1] == "M":
        return float(capital.replace("M", ""))

    if capital[-1] == "B":
        return float(capital.replace("B", "")) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    industry_capital = sum(
        _cap_str_to_mln_float(company["cap"])
        for company in data
        if industry == company["industry"]
    )
    return round(industry_capital, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    capital = {}
    for company in data:
        if company["symbol"] not in capital:
            capital[company["symbol"]] = 0
        capital[company["symbol"]] += _cap_str_to_mln_float(company["cap"])
    return list({k: v for k, v in sorted(capital.items(), key=lambda item: item[1])}.keys())[-1]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sectors = {}
    for company in data:
        if 'n/a' in company['sector']:
            continue
        if company['sector'] not in sectors:
            sectors[company['sector']] = 1
        sectors[company['sector']] += 1
    return max(sectors.items(), key=lambda item: item[1])[0], min(sectors.items(), key=lambda item: item[1])[0]
