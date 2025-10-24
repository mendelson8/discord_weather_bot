Discord Weather Bot

A simple Discord bot that allows users to check the current weather in any city using the WeatherAPI.

------------------------------------------------------------
Features

- Command !pogoda <city> — returns the current temperature in the selected city.
- Error handling: the bot will notify if no city is provided or if data retrieval fails.
- Console logging for easier debugging.

------------------------------------------------------------
Requirements

- Python 3.8 or higher
- Discord account and a created bot with a valid token
- API key from WeatherAPI (https://www.weatherapi.com/)
- A .env file for secure storage of tokens and keys

------------------------------------------------------------
Installation

1. Clone the repository:
   git clone https://github.com/mendelson8/discord_weather_bot.git
   
   cd discord-weather-bot

2. Install the required packages:
   
   pip install discord.py requests beautifulsoup4 python-dotenv

3. Create a .env file in the same directory and add:
   
   DISCORD_TOKEN=your_discord_token

   WEATHER_API_KEY=your_weatherapi_key

4. Run the bot:
   
   python bot.py
