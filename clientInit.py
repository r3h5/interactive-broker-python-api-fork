from pprint import pprint
from ibw.client import IBClient
import csv

from configparser import ConfigParser


config = ConfigParser()

config.read('config/config.ini')

u = config.get('live', 'user')
a = config.get('live', 'account')
is_running_override=True #dont make it launch server. i always run it separately anyway

print('Using these creds (truncated): ', 'user: '+u[:4], 'account: '+a[:5])
ib_client = IBClient(
    username=u,
    account=a,
    is_server_running=is_running_override
)


# ib_client.get_live_orders()


order={

    "acctId": a,
    "conid": 265598,
    # "conidex": "conidex = 265598",
    # "secType": "secType = 265598:STK",
    # "cOID": "string",  see if this one can be commented out
    # "parentId": "string",
    "orderType": "LMT",
    "listingExchange": "SMART",
    # "isSingleGroup": true,
    # "outsideRTH": false,
    "price": 120,
    # "auxPrice": null,
    "side": "BUY",
    # "ticker": "string", see of this one can be commented out
    "tif": "GTC",
    "referrer": "QuickTrade",
    "quantity": 1,
    # "cashQty": 0,
    # "fxQty": 0,
    "useAdaptive": False,
    # "isCcyConv": False,
    # "allocationMethod": "string", probably can leave out
    # "strategy": "string",
    # "strategyParameters": { }
}

# orders = {'orders':[order]}


# f1 = open('order_allocation.csv')
# reader = csv.reader(f1)
# next(reader)

# percent_down_book = 0.983

# for row in reader:
#     ticker = row[0]
#     contId = row[4]
#     price = row[12] * percent_down_book



# with open('order_allocations.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['StockTicker'], row['con_id'])















