from yahooquery import Ticker

msft = Ticker("MSFT")

# get all stock info
msft_info = msft.summary_detail

# get historical market data
hist = msft.history(period="1mo")
print('Historical market data')
print(hist)

# get year-to-date historical market data including dividends
msft_actions = msft.history(period='ytd')

print('Year-to-date historical market data including dividends')
print(msft_actions)

# Please note that the 'dividends' and 'splits' keys might not be present in the DataFrame.
# You should check if they exist before trying to access them.
if 'dividends' in msft_actions:
    msft_dividends = msft_actions['dividends']
    print('Dividends')
    print(msft_dividends)
if 'splits' in msft_actions:
    msft_splits = msft_actions['splits']
    print('Splits')
    print(msft_splits)

# Other parts of your code...



# show financials:
# - income statement
msft_income_stmt = msft.income_statement()
print('Income statement')
print(msft_income_stmt)
# - balance sheet
msft_balance_sheet = msft.balance_sheet()
print('Balance sheet')
print(msft_balance_sheet)

# - cash flow statement
msft_cashflow = msft.cash_flow()
print('Cash flow statement')
print(msft_cashflow)


# show holders
msft_major_holders = msft.major_holders
print('Major holders')
print(msft_major_holders)
msft_institutional_holders = msft.institution_ownership
print('Institutional holders')
print(msft_institutional_holders)
# show earnings
msft_earnings = msft.earnings
print('Earnings')
print(msft_earnings)


# show analysts recommendations
msft_recommendations = msft.recommendations
print('Recommendations')
print(msft_recommendations)

# show next event (earnings, etc)
msft_calendar = msft.calendar_events

print('Calendar events')
print(msft_calendar)
# show options expirations

msft_options = msft.option_chain
print('Options')
print(msft_options)

# show news
msft_news = msft.news(count=5)
print('News')
print(msft_news)




