import discord
from discord.ext import commands

print("""

logo



""")


token = input("token: ")

science = commands.Bot(command_prefix="-", self_bot=True)

@science.event
async def on_ready():
  print("ciao mk")
 
