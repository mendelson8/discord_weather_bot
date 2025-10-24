import discord
import os
import time
from discord.permissions import permission_alias
import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
from dotenv import load_dotenv

# wczytaj zmienne z pliku .env
load_dotenv()

intents = discord.Intents()
intents.message_content = True
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f"Zalogowałem się jako {client.user}")


@client.event
async def on_message(message):
  print(message.content)

  if message.content.startswith("!pogoda"):
    print(message.content)
    miejscowosc_ok = message.content[8:]
    if not miejscowosc_ok.strip():
      await message.channel.send(
          "Podaj nazwę miejscowości po komendzie !pogoda")
      return

    miejscowosc = urllib.parse.quote(miejscowosc_ok)
    api_key = os.getenv("WEATHER_API_KEY")
    link = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={miejscowosc}"

    wez = requests.get(link)
    zupa = BeautifulSoup(wez.content, "html.parser")
    side  = json.loads(str(zupa))
    print(side)
    try:
      await message.channel.send(f"Temperatura wynosi: {side.get('current').get('temp_c')}°C")
    except AttributeError:
      await message.channel.send(
          "Nie udało się pobrać temperatury. Sprawdź nazwę miejscowości.")

token = os.getenv("DISCORD_TOKEN")
client.run(token)
