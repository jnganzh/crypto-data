import requests
import pandas as pd
from collections import defaultdict
import datetime

account_store = defaultdict(list)

starting_url = "https://api.compound.finance/api/v2/account?page_size=100&page_number=3655"
starting_r = requests.get(starting_url)
total_pages = int(starting_r.json()['pagination_summary']['total_pages'])

for i in range(1,total_pages+1):
    print(i)

    url = """https://api.compound.finance/api/v2/account?page_size=100&page_number={_pagenum_}""".format(_pagenum_ = i)
    r = requests.get(url)

    for item in r.json()['accounts']:

        for idx,token in enumerate(item['tokens']):

            account_store['address'].append(item['address'])
            account_store['block_updated'].append(item['block_updated'])
            account_store['health'].append(item['health'])
            account_store['tokenAddress'].append(item['tokens'][idx]['address'])
            account_store['borrow_balance_underlying'].append(item['tokens'][idx]['borrow_balance_underlying']['value'])
            account_store['lifetime_borrow_interest_accrued'].append(item['tokens'][idx]['lifetime_borrow_interest_accrued']['value'])
            account_store['lifetime_supply_interest_accrued'].append(item['tokens'][idx]['lifetime_supply_interest_accrued']['value'])
            account_store['safe_withdraw_amount_underlying'].append(item['tokens'][idx]['safe_withdraw_amount_underlying']['value'])
            account_store['supply_balance_underlying'].append(item['tokens'][idx]['supply_balance_underlying']['value'])
            account_store['symbol'].append(item['tokens'][idx]['symbol'])
            account_store['total_borrow_value_in_eth'].append(item['total_borrow_value_in_eth']['value'])
            account_store['total_collateral_value_in_eth'].append(item['total_collateral_value_in_eth']['value'])
    
account_df = pd.DataFrame.from_dict(account_store)
account_df.to_csv('user_accounts.csv')