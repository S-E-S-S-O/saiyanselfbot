import discord; from discord.ext import commands; import requests; import os

Saiyan = commands.Bot(command_prefix="tk!", self_bot=True); t=input("Insert your token > "); os.system("cls")

form = "base"

@Saiyan.command()
async def menu(ctx):
    await ctx.message.delete()
    if form == "base":
        embed=discord.Embed(title="**Base Form**", description="""
**Commands**
```
- transform (Form)
```
""", color=0x00bfff)
        embed.set_image(url="https://i.imgur.com/afVYk0d.gif")
    elif form == "ssj":
        embed=discord.Embed(title="**Super Saiyan**", description="""
**Commands**
```
- transform (Form)
- sesso
```
"This is the Super Saiyan."
""", color=0xffff00)
        embed.set_image(url="https://i.pinimg.com/originals/88/30/f2/8830f281c8b2f7c71e4c76eb0c3d7786.gif")
    elif form == "ssj2":
        embed=discord.Embed(title="**Super Saiyan 2**", description="""
**Commands**
```
- transform (Form)
- sesso
- oscuro
```
"Super Saiyan 2 is all about power.."
""", color=0xffff00)
        embed.set_image(url="https://gifimage.net/wp-content/uploads/2017/11/goku-ssj2-gif-10.gif")
    elif form == "ssj3":
        embed=discord.Embed(title="**Super Saiyan 3**", description="""
**Commands**
```
- transform (Form)
- sesso
- oscuro
- scimmia
```
"I can't keep this form for too long."
""", color=0xffa500)
        embed.set_image(url="https://i.makeagif.com/media/3-01-2015/4b0LoJ.gif")
    elif form == "omnikkx100":
        embed=discord.Embed(title="**Omni God Kaioken x100!**", description="""
**Commands**
```
- transform (Form)
- final_toxx (100%. ban chance toxx.)
- god_spam (Spam that bypasses rate limit.)
- light_speed_nuke (The name says it all.)
- audithang_boosted (Better audithang.)
- thread_flood (Name says it all.)
- anti_toxx (Makes your acc impossible to be banned.)
- token_gen (Generates tokens.)
```
"TIMES X100!!!!"
""", color=0xffffff)
        embed.set_image(url="https://c.tenor.com/pNbQ0-4D4ogAAAAd/power-dragon-ball-z.gif")
    await ctx.send(embed=embed, delete_after=20)
    

@Saiyan.command()
async def transform(ctx, arg):
    await ctx.message.delete()
    global form
    if arg == "base":
        embed=discord.Embed(title="**Untransformation**", description="""
""", color=0x000000)
        form = "base"
        embed.set_image(url="https://cdn.discordapp.com/attachments/912364264772235286/919289148479782972/2hqt3RM.gif")
    elif arg == "ssj":
        embed=discord.Embed(title="**SSJ transformation.**", description="""
""", color=0xffff00)
        embed.set_image(url="https://thumbs.gfycat.com/FearlessYoungFlies-max-1mb.gif")
        form = "ssj"
    elif arg == "ssj2":
        embed=discord.Embed(title="**SSJ2 transformation.**", description="""
""", color=0xffff00)
        embed.set_image(url="https://c.tenor.com/2DtkZM_5B9gAAAAC/goku-son-goku.gif")
        form = "ssj2"
    elif arg == "ssj3":
        embed=discord.Embed(title="**SSJ3 transformation.**", description="""
""", color=0xffff00)
        embed.set_image(url="https://thumbs.gfycat.com/BabyishDistantAttwatersprairiechicken-size_restricted.gif")
        form = "ssj3"
    elif arg == "omnikkx100":
        embed=discord.Embed(title="**Omni God Kaioken x100 transformation.**", description="""
""", color=0xffffff)
        embed.set_image(url="https://i.makeagif.com/media/4-21-2018/yFNPX3.gif")
        form = "omnikkx100"
    await ctx.send(embed=embed, delete_after=40)

Saiyan.run("", bot=False)

