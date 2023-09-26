from discord.ext import commands
import discord
import json
import pygsheets

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents = intents)

gc = pygsheets.authorize(service_account_file='credentials.json')
survey_url = 'https://docs.google.com/spreadsheets/d/1Vz33H7t4555XJWnm8GsJgt9UqV4N55RdylpGIUBxlSk/'
sh = gc.open_by_url(survey_url)
sheet_test01 = sh.worksheet_by_title("test1")
sheet_test02 = sh.sheet1

with open('token.json' ,  "r", encoding = "utf-8") as file:
    data = json.load(file)

donate_id = 0
donate_channel_id = 0

@bot.event
async def on_ready():
    print(f"Bot is ready --> {bot.user}")
    for guild in bot.guilds:
        for channel in guild.channels:
            if isinstance(channel, discord.ForumChannel):
                if "捐獻紀錄" in channel.name:
                    donate_channel_id = channel.id
                    print(f'channel: {channel.name} - id: {channel.id}')
                    for thread in channel.threads:
                        if "捐獻紀錄" in thread.name:
                            donate_id = thread.id
                            print(f'thread: {thread.name} - id: {thread.id}')

@bot.event
async def on_message(message):
    if message.channel.id == 1156136935572635689:
        print(f'{message.author.name} : {message.content}')
        msg = [[message.content]]
        sheet_test02.append_table(msg)
    
bot.run(data['token'])


