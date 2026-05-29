# Imports
import discord
from discord import app_commands
from discord.ext import commands
import requests
from config import token, apikey

# Bot Configuration
intents = discord.Intents.default() 
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='/')

#Sync
@bot.event
async def on_ready():
    await bot.tree.sync()
    print('Bot is running and has synced.')

# Establish Command Name and Description 
@bot.tree.command(name='mvr_lookup', description='cree par mvr xz, le bot donne des informations précises sur une adresse IP')

# Bot Prompt, API Call, and Response Functionality
@app_commands.describe(user_input = "***met ici une adresse IP***: ")                 # Prompt User for Input
async def MVR Lookup (interaction: discord.Interaction, user_input: str):                 

    # Use Requests to Obtain Data from API
    API_KEY
    url = f'https://api.geolocation.io/ipgeo?apiKey={apikey}&ip-{user_input}'
    response = requests.get(url)
    json_response = response.json()

    # Send Message Containing Requested Data to User
    await interaction.response.send_message(f'IP: {json_response["ip"]}\nCountry:{json_response["country_name"]}\nISP:{json_response["isp"]}', ephemeral=True)
    return

bot.run(token) # Run Bot
