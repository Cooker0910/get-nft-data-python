from dotenv import dotenv_values
import requests
import json

config = dotenv_values(".env")

# url = "https://api.opensea.io/api/v1/asset/0x1a92f7381b9f03921564a437210bb9396471050c/3917/offers?limit=1"

headers = {
    "Accept": "application/json",
    "X-API-KEY": config['API_KEY']
}

# response = requests.get(url, headers=headers)

# offers = json.loads(response.text)
# listing_URL = "https://opensea.io/assets/ethereum/0x1a92f7381b9f03921564a437210bb9396471050c/3917" 
# current_price = offers["seaport_offers"][0]["current_price"]
# address = offers["seaport_offers"][0]["protocol_data"]["parameters"]["offerer"]
# created_date = offers["seaport_offers"][0]["created_date"]
# print(created_date)
# print(address)
# print(current_price)

# url = "https://api.opensea.io/api/v1/assets?token_ids=3917&order_direction=desc&asset_contract_address=0x1a92f7381b9f03921564a437210bb9396471050c&limit=20&include_orders=false"

# response = requests.get(url, headers=headers)

# asset = json.loads(response.text)
# last_sale_time = asset["assets"][0]["last_sale"]["event_timestamp"]
# nft_Id = asset["assets"][0]["token_id"]
# print(last_sale_time)

def obj_dict(obj):
    return obj.__dict__


url = "https://api.opensea.io/api/v1/asset/0x1a92f7381b9f03921564a437210bb9396471050c/3917/listings?limit=20"

response = requests.get(url, headers=headers)

seaport_listings = json.loads(response.text)
asking_price = seaport_listings["listings"]
# json_string = json.dumps(asking_price, default=obj_dict)
print(asking_price)