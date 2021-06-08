from collections import defaultdict
import datetime
import pandas as pd

def getRates(r,symbol):

    data_store = defaultdict(list)

    borrow_rates = r.json()['borrow_rates']
    supply_rates = r.json()['supply_rates']
    exchange_rates = r.json()['exchange_rates']
    prices_usd = r.json()['prices_usd']
    total_borrows_history = r.json()['total_borrows_history']
    total_supply_history = r.json()['total_supply_history']

    for i in range(len(borrow_rates)):

        #Block Number
        data_store['block_number'].append(borrow_rates[i]['block_number'])

        #Timestamp
        data_store['timestamp'].append(borrow_rates[i]['block_timestamp'])

        #Date
        timestamp = int(borrow_rates[i]['block_timestamp'])
        timestamp = datetime.datetime.fromtimestamp(timestamp)
        timestamp = timestamp.strftime('%d-%m-%Y')
        data_store['date'].append(timestamp)

        #Borrow rates
        data_store['borrow_rates'].append(borrow_rates[i]['rate'])
        #Supply rates
        data_store['supply_rates'].append(supply_rates[i]['rate'])
        #Exchange_rates
        data_store['exchange_rates'].append(float(exchange_rates[i]['rate']))
        #Prices USD
        data_store['prices_usd'].append(prices_usd[i]['price']['value'])
        #Total Supply History
        data_store['supply_value'].append(float(total_supply_history[i]['total']['value']))
        #Total Borrow History
        data_store['borrow_value'].append(float(total_borrows_history[i]['total']['value']))



    df = pd.DataFrame.from_dict(data_store)
    df['symbol'] = symbol
    
    return df