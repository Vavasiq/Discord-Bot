import discord
import requests
from replit import db
from keep_alive import keep_alive
import time

link='https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
db["key"] = "value"
def getCrypto(name_crypto):
  r = requests.get(link)
  response=r.json()
  for i in range (len(response)):
      if response[i].get("id") == name_crypto:
          print(response[i].get("name"), "-",response[i].get("current_price"))
          return  response[i].get("current_price")
      # elif response[i].get("id") == "solana":
      #     return d, e = response[i].get("name"), response[i].get("current_price")  
      #     print(response[i].get("name"), "-", response[i].get("current_price"))
      # elif response[i].get("id") == "ethereum":
      #     print(response[i].get("name"), "-",response[i].get("current_price"))
      #     return f, g = response[i].get("name"), response[i].get("current_price")



# instantiate a discord client
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$bitcoin'):
        crypto = getCrypto("bitcoin")
        await message.channel.send(crypto)
# @client.event
# async def on_ready():
#     print(f'You have logged in as {client}')
#     channel = discord.utils.get(client.get_all_channels(), name='crypto')

#     await client.get_channel(channel.id).send('bot is now online!')


# # called whether there is a message in the chat
# @client.event
# # async def on_message(message):
# #     if message.author == client.user:
# #         return

#     if message.content.startswith('ya'):
#         await message.channel.send('yeet')

#     # send crypto price directly
#     if message.content.lower() in db.keys():
#         await message.channel.send(
#             f'The current price of {message.content} is: {getCryptoPrices(message.content.lower())} USD')

#     # list all the available coins
#     if message.content.startswith('$list'):
#         db["key"] = "value"
#         cryptoSupportedList = [key for key in db.keys()]
#         await message.channel.send(cryptoSupportedList)

#     # check whether a coin is being supported
#     if message.content.startswith('$support '):
#         cryptoToBeChecked = message.content.split('$support ', 1)[1].lower()
#         await message.channel.send(isCryptoSupported(cryptoToBeChecked))

    # timing = time.time()
    # while (1):
    #     if time.time() - timing > 10.0:
    #         timing = time.time()
    #         print()


keep_alive()
BOT_TOKEN = 'OTY5MTg2ODI4NzIyNzk0NTc2.Ympvkg.zh2R5E_yJEJA4n7MUpZudW52feE'
client.run(BOT_TOKEN)