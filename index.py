from asyncore import write
from dotenv import dotenv_values
import requests
import json
from csv import writer
config = dotenv_values(".env")

listed_date  = ""
sale_time = ""
highest_bid = ""
bid_time = ""
asking_price  = ""
address = ""
listing_url = ""
List = []

# with open('persons.csv', 'a') as csvfile:
#     global writer_object
#     writer_object = writer(csvfile)
        
# headers = {
#     "Accept": "application/json",
#     "X-API-KEY": config['API_KEY']
# }

# def invalid_ids(invalid_id):
#     with open("sample.txt", "a") as a_file:
#         a_file.write("\n")
#         a_file.write(invalid_id)

# def get_data():
#     with open('persons.csv', 'a') as csvfile:
#         global writer_object
#         writer_object = writer(csvfile)
#         for nft_id in range(3915, 3920):

#             global listed_date 
#             global sale_time
#             global highest_bid
#             global bid_time
#             global asking_price 
#             global address
#             global listing_url
#             global List

#             print(nft_id)
#             url = "https://api.opensea.io/api/v1/asset/0x1a92f7381b9f03921564a437210bb9396471050c/" + str(nft_id) + "/offers?limit=1"
#             response = requests.get(url, headers=headers)

#             offers = json.loads(response.text)
#             if(len(offers["seaport_offers"]) > 0):
#                 highest_bid = offers["seaport_offers"][0]["current_price"]
#                 address = offers["seaport_offers"][0]["protocol_data"]["parameters"]["offerer"]
#                 bid_time = offers["seaport_offers"][0]["created_date"]
#                 print(bid_time)
#             else: 
#                 print("No Offers")

#             url = "https://api.opensea.io/api/v1/assets?token_ids=" + str(nft_id) + "&order_direction=desc&asset_contract_address=0x1a92f7381b9f03921564a437210bb9396471050c&limit=20&include_orders=true"

#             response = requests.get(url, headers=headers)

#             asset = json.loads(response.text)
#             if(asset["assets"][0]["seaport_sell_orders"] != None):
#                 sale_time = asset["assets"][0]["last_sale"]["event_timestamp"]
#                 asking_price = asset["assets"][0]["seaport_sell_orders"][0]["current_price"]
#                 listed_date = asset["assets"][0]["seaport_sell_orders"][0]["created_date"]
#                 listing_url = "https://opensea.io/assets/ethereum/0x1a92f7381b9f03921564a437210bb9396471050c/" + str(nft_id)
#             else:
#                 print("No assets")
#                 invalid_ids(str(nft_id))
#             if(listed_date != ""):
#                 List = [str(nft_id), listed_date, sale_time, str(highest_bid), bid_time, asking_price, address, listing_url]
#                 print(List)
#                 # writer_object.writerow(List)
#             else:
#                 print("Don't Save!")
#             print(List)

#         else:
#             print("Finally finished!")

# get_data()


async def main():
    async def one_iteration():
        result = await first()
        print(result)
        result2 = await second()
        print(result2)
    coros = [one_iteration() for _ in range(2)]
    await asyncio.gather(*coros)