import requests
from bs4 import BeautifulSoup

# url = 'https://www.londonstockexchange.com/stock/93XH/ades-international-holding-plc/company-page'
# url = 'https://www.londonstockexchange.com/stock/ADV/advance-energy-plc/company-page'
def scrape_data(link):
    url = link
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    table_data = soup.find('table', class_ = 'full-width trades-table swipable-table')
    for data in table_data.find_all('tbody'):
        rows = data.find_all('tr')
        for row in rows:
            date = row.find_all('td')[0].text.strip()
            time = row.find_all('td')[1].text.strip()
            price = row.find_all('td')[2].text.strip()
            currency = row.find_all('td')[3].text.strip()
            volume = row.find_all('td')[4].text.strip()
            tradeValue = row.find_all('td')[5].text.strip()
            tradeType = row.find_all('td')[6].text.strip()
            tradeFlag = row.find_all('td')[7].text.strip()
            venueOfPublication = row.find_all('td')[8].text.strip()
            mic = row.find_all('td')[9].text.strip()
            context = {
                'date': date,
                'time': time,
                'price': price,
                'currency': currency,
                'volume': volume,
                'tradeValue': tradeValue,
                'tradeType': tradeType,
                'tradeFlag': tradeFlag,
                'venueOfPublication': venueOfPublication,
                'mic': mic,
                'link': link
            }
            return context
            # print(context.date)
            # first = context[list(context.keys())[0]]
            # print(first)



            # print("****************************")

# url = 'https://www.londonstockexchange.com/stock/88E/88-energy-limited/company-page'
# scrape_data(url)