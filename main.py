#***************************************************************************#
#                                                                           #
# RNO Bot - A Discord Bot For Our Server.                                   #
# https://github.com/NoraHanegan/RNOBot                                     #
# Copyright (C) 2021 Nora Hanegan. All rights reserved.                     #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#

import aiohttp
import box
import datetime
import discord
import json
import random
import os
import platform
import requests
import time
import urllib

from dadjokes import Dadjoke
from discord.ext import commands
from datetime import datetime

from discord.ext.commands import CommandNotFound

prefix = "/"

intents = discord.Intents.default()
intents.members = True
playing = [
    "Mario Party", "Mario Kart"
]

client = commands.Bot(description="RNO Bot",
                      command_prefix=prefix,
                      intents=intents,
                      activity=discord.Game(name=random.choice(playing)))
client.remove_command('help')

#Owner ID
ownerID = 543576276108181506

@client.event
async def on_ready():
    memberCount = len(set(client.get_all_members()))
    serverCount = len(client.guilds)
    print("                                                                ")
    print("################################################################")
    print(f"            ____  _   ______     ____        __                ")
    print(f"           / __ \/ | / / __ \   / __ )____  / /_               ")
    print(f"          / /_/ /  |/ / / / /  / __  / __ \/ __/               ")
    print(f"         / _, _/ /|  / /_/ /  / /_/ / /_/ / /_                 ")
    print(f"        /_/ |_/_/ |_/\____/  /_____/\____/\__/                 ")
    print("                                                                ")
    print("################################################################")
    print("                                                                ")
    print("Running as: " + client.user.name + "#" + client.user.discriminator)
    print(f'With Client ID: {client.user.id}')
    print("\nBuilt With:")
    print("Python " + platform.python_version())
    print("Pycord " + discord.__version__)

#Join Logs
@client.event
async def on_member_join(member):
  welcomechannel = client.get_channel(742934220279775394)
  staffwelcomechannel = client.get_channel(743214119204683806)
  jl = [f"We've got cookies {member.mention}!",
    f"Isn't there a discord server for memes like {member.mention}?",
    f"October 31st, Halloween, November 1st, beginning of Hanukkah and Christmas, what is this {member.mention}!",
    f"{member.mention}, Do you like spooky? I like spooky, SPOOOOOKY!!!",
    f"The cake is a lie, or is it {member.mention}?",
    f"There’s a fire burning {member.mention}! Anybody got marshmallows?",
    f"Minecraft 1.13 is here {member.mention}! It took a long time for you guys to add water animals Mojang!",
    f"You like games {member.mention}? Hopefully!",
    f"Once you get here {member.mention}, you just keep going and going and going...!",
    f"Every {member.mention} is like a bird, they just fly in out of nowhere and poop on your head! Not really though!",
    f"Never enough {member.mention}'s, or maybe too many I don’t know!",
    f"Free Advice From Phantom_storm {member.mention} don't eat your mic, it's too...salty.",
    f"I see a message in the sky it says, “welcome {member.mention}!",
    f":notes:I see trees of green, {member.mention}  too:notes: and i think to myself what a wonderful sever!:notes:",
    f"{member.mention} came prepared, with absolutely nothing!",
    f"A new player has entered the ring, {member.mention} , show us what you can do!",
    f"We have free icecream {member.mention}! But it may melt, so hurry fast!",
    f"It’s time to do do do do do do do do do do do do DOOO ITTTT {member.mention}!!!!",
    f"Made with 100% dank memes {member.mention}!",
    f"This match will get red hot {member.mention}!",
    f"Wonder what this button does {member.mention}, oh, another member, amazing!!!",
    f"A brawl is surely brewing {member.mention}!",
    f"The Man, The Myth, The Legend, {member.mention} has entered the building!",
    f"Do you knew the wae {member.mention}? We do know the wae!",
    f"Old friends new friends like {member.mention} they’re all my friends!",
    f"We were expecting you {member.mention} ( ͡° ͜ʖ ͡°)",
    f"We count by friends not members {member.mention}!:grin:",
    f"I wonder how many people are on the server? Oh wait, here comes {member.mention}!",
    f"Obviously {member.mention} is not an alt account, am I right or am I right! :sunglasses:"
    ]
  jlrandom = random.choice(jl)
  await welcomechannel.send(f"{jlrandom}")
  await staffwelcomechannel.send(f"{member} Joined. Account created on {member.created_at}")

#Help Command
@client.command()
async def help(ctx):
  author = ctx.message.author
  embed = discord.Embed(color = discord.Color.orange())

  embed.set_author(name="Commands:")
  embed.add_field(name="General", value="!help - Shows This Message\n\n!ping - Says Pong Back To You\n\n!uptime - Bot Uptime Counter", inline=False)
  embed.add_field(name="Fun", value="!toss - Coin Flip\n\n!Dadjoke - Give a Dad Joke\n\n!dice - Roll 1-6", inline=False)

  await ctx.send(author, embed=embed)

#NES Command
@client.command()
async def nes(ctx):
  embed = discord.Embed(color = discord.Color.orange())
  embed.add_field(name="NES Emulators", value="!mesen - A New But Recently Discontinued Open Source Cycle Accurate NES Emulator with a Clean Interface and Compatibility. Supports Netplay\n\n!nestopia - A Open Source Cycle Accurate NES Emulator that has Excellant Compatibility and is Trusted for being around for a decade\n\n!fceux - FCEUX is an old Open Source Mid Accurate Emulator that has good Compatibility but was surpassed by alot of others. It has really good debugging tools.\n\n!punes - puNES is a Semi New Cycle Accurate NES Emulator. It has some really nice features like a excellant Rewind function.\n\n!virtuanes - VirtuaNES is an Open Source Low Accurate Japaneese Emulator. It is famous for its stupid amount of accessory support but should only be used by the games that require said accessories.", inline=False)
  await ctx.send(embed=embed)

#Uptime Command
@client.command()
async def uptime(ctx):
  delta_uptime = datetime.utcnow() - client.launch_time
  hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
  minutes, seconds = divmod(remainder, 60)
  days, hours = divmod(hours, 24)
  await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")

#Ping Command
@client.command()
async def ping(ctx):
    """Ping Pong"""
    await ctx.send('Pong!')


#Roll Dice Command
@client.command(aliases=["roll"])
async def dice(ctx):
    """Rolls the dice"""
    cont = random.randint(1, 6)
    await ctx.send("You Rolled **{}**".format(cont))


#Coin Flip Command
@client.command(aliases=["flip"])
async def toss(ctx):
    """Put the toss"""
    ch = ["Heads", "Tails"]
    rch = random.choice(ch)
    await ctx.send(f"You got **{rch}**")


#Reverse Text Command
@client.command()
async def reverse(ctx, *, text):
    """Reverse the given text"""
    await ctx.send("".join(list(reversed(str(text)))))


#Meme Command
@client.command()
async def meme(ctx):
    """Sends you random meme"""
    r = await aiohttp.ClientSession().get(
        "https://www.reddit.com/r/dankmemes/top.json?sort=new&t=day&limit=100")
    r = await r.json()
    r = box.Box(r)
    data = random.choice(r.data.children).data
    img = data.url
    title = data.title
    url_base = data.permalink
    url = "https://reddit.com" + url_base
    embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
    embed.set_image(url=img)
    await ctx.send(embed=embed)

#Dadjoke Command
@client.command(aliases=["dadjoke"])
async def joke(ctx):
    """Sends the dadjokes"""
    async with ctx.typing():
        await ctx.send(Dadjoke().joke)

#Server Command
@client.command("server")
async def s_info(ctx):
    server = ctx.guild
    icon = ("\uFEFF")
    embed = discord.Embed(title=f"Server info for {server.name}",
                          description='\uFEFF',
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=server.icon_url_as(size=256))
    embed.add_field(name="Name", value=server.name, inline=True)
    embed.add_field(name="Region", value=server.region, inline=True)
    embed.add_field(name="Member Count",
                    value=server.member_count,
                    inline=True)
    embed.add_field(name="Owner",
                    value="<@" + f"{server.owner_id}" + ">",
                    inline=True)
    embed.add_field(name="ID", value=server.id, inline=True)
    embed.add_field(name="Creation Date",
                    value=f"{server.created_at}",
                    inline=True)
    embed.add_field(name="Server Icon Url", value=server.icon_url, inline=True)
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    await ctx.send(content=None, embed=embed)


#Stats Command
@client.command()
async def stats(ctx):

    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))

    embed = discord.Embed(title=f'{client.user.name} Stats',
                          description='\uFEFF',
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.add_field(name='Python Version:',
                    value=f"{pythonVersion}",
                    inline=False)
    embed.add_field(name='Discord.py Version',
                    value=f"{dpyVersion}",
                    inline=False)
    embed.add_field(name='Total Guilds:', value=f"{serverCount}", inline=False)
    embed.add_field(name='Total Users:', value=f"{memberCount}", inline=False)
    embed.add_field(name='Bot Developer:',
                    value="<@" + f"{ownerID}" + ">, ",
                    inline=False)
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)


#Poll Command
@client.command(pass_context=True)
async def poll(ctx, *args):
    mesg = ' '.join(args)
    embed = discord.Embed(title='A Poll has Started !',
                          description='{0}'.format(mesg),
                          color=0x00FF00)

    embed.set_footer(text='Poll created by: {0} • React to vote!'.format(
        ctx.message.author))

    embed_message = await ctx.send(embed=embed)

    await embed_message.add_reaction('👍')
    await embed_message.add_reaction('👎')
    await embed_message.add_reaction('🤷')

#If Command Error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("That Command Was not found!")

#PSCX2 Emulator Command
@client.command()
async def pcsx2(ctx):
  """Sends a link to the PSCX2 Download Page and its Bios"""
  async with ctx.typing():
      await ctx.send('**PSCX2 Stable Builds: **\n<https://pcsx2.net/download.html>\n\n**PSCX2 Development Builds: **\n<https://buildbot.orphis.net/pcsx2/>\n\n**Bios:**\n<https://romsmania.cc/bios/pcsx2-playstation-2-bios-3>')

#RPCS3 Emulator Command
@client.command()
async def rpcs3(ctx):
  """Sends a link to the RPCS3 Download Page and its Bios"""
  async with ctx.typing():
      await ctx.send('**RPCS3 Stable Builds:**\n<https://rpcs3.net/download>\n\n**RPCS3 Development Builds:**\n<https://rpcs3.net/compatibility?b> \n\n**Firmware:**\n<https://www.playstation.com/en-us/support/system-updates/ps3>')

#Citra Emulator Command
@client.command()
async def citra(ctx):
  """Sends a link to the Citra Download Page"""
  async with ctx.typing():
      await ctx.send('**Citra Builds:**\n<https://citra-emu.org/download/>')

#Vita3k Emulator Command
@client.command()
async def vita3k(ctx):
  """Sends a link to the Vita3K Download Page and its Bios"""
  async with ctx.typing():
      await ctx.send('**Vita3K Development Builds:**\n<https://vita3k.org/#download>\n\n**Firmware:**\n<https://www.playstation.com/en-us/support/system-updates/ps-vita/>')

#PPSSPP Emulator Command
@client.command()
async def ppsspp(ctx):
  """Sends a link to the PPSSPP Download Page"""
  async with ctx.typing():
      await ctx.send('**PPSSPP Stable Builds:**\n<https://www.ppsspp.org/downloads.html>\n\n**PPSSPP Development Builds:**\n<https://buildbot.orphis.net/ppsspp/>')

#Mednafen Emulator Command
@client.command()
async def mednafen(ctx):
  """Sends a link to the Mednafen Download Page"""
  async with ctx.typing():
      await ctx.send('**Mednafen Stable Builds:**\n<https://mednafen.github.io/releases/>')

#Higan Emulator Command
@client.command()
async def higan(ctx):
  """Sends a link to the Higan Download Page"""
  async with ctx.typing():
      await ctx.send('**Higan Stable Builds:**\n<https://byuu.org/higan#download>\n\n**Higan Development Builds**\n<https://cirrus-ci.com/github/higan-emu/higan/master>')

#PuNES Emulator Command
@client.command()
async def punes(ctx):
  """Sends a link to the PuNES Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**PuNES Stable Builds:**\n<https://github.com/punesemu/puNES/releases>\n\n**PuNES Development Builds:**\n<https://ci.appveyor.com/project/punesemu/punes/build/artifacts>')

#FCEUX Emulator Command
@client.command()
async def fceux(ctx):
  """Sends a link to the FCEUX Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**FCEUX Stable Builds:**\n<http://www.fceux.com/web/download.html>\n\n**FCEUX Development Builds:**\n<https://ci.appveyor.com/project/zeromus/fceux/build/artifacts>')

#Mesen Emulator Command
@client.command()
async def mesen(ctx):
  """Sends a link to the Mesen Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**Mesen Stable Builds:**\n<https://www.mesen.ca/#Downloads>\n\n**Mesen Development Builds:**\n<https://ci.appveyor.com/project/Sour/mesen/build/artifacts>')

#VirtuaNES Emulator Command
@client.command()
async def virtuanes(ctx):
  """Sends a link to the VirtuaNES Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**VirtuaNES Stable Builds:**\n<http://virtuanes.s1.xrea.com/vnes_dl.php>')

#Nestopia Emulator Command
@client.command()
async def nestopia(ctx):
  """Sends a link to the Nestopia Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**Nestopia Stable Builds:**\n<https://sourceforge.net/projects/nestopiaue/files/>')

#Mesen-S Emulator Command
@client.command(aliases=['mesen-s'])
async def mesensnes(ctx):
  """Sends a link to the Mesen-S Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**Mesen-S Stable Builds:**\n<https://github.com/SourMesen/Mesen-S/releases>\n\n**Mesen-S Developement Builds:**\n<https://ci.appveyor.com/project/Sour/mesen-s/build/artifacts>')

#bsnes Emulator Command
@client.command()
async def bsnes(ctx):
  """Sends a link to the bsnes Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**bsnes Stable Builds:**\n<https://byuu.org/bsnes#download>\n\n**bsnes Builds Download:**\n<https://cirrus-ci.com/github/bsnes-emu/bsnes/master>')

#ZSNES Emulator Command
@client.command()
async def zsnes(ctx):
  """Sends a link to the zsnes Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**zsnes Stable Builds:**\n<https://www.zsnes.com/index.php?page=files>')

#ZSNES Emulator Command
@client.command()
async def snes9x(ctx):
  """Sends a link to the Snes9x Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**Snes9x Stable Builds:**\n<http://www.s9x-w32.de/dl/>\n\n**Snes9x Development Builds:**\n<https://ci.appveyor.com/project/snes9x/snes9x>')

#Project64 Emulator Command
@client.command()
async def project64(ctx):
  """Sends a link to the Project64 Download Page"""
  async with ctx.typing():
      await ctx.send('**Project64 Stable Builds:**\n<https://www.pj64-emu.com/public-releases>\n\n**Project64 Development Builds:**\nPlease Use These, The Stable Builds are Super Old\n<https://www.pj64-emu.com/nightly-builds>')

#Project64 Netplay Emulator Command
@client.command()
async def project64netplay(ctx):
  """Sends a link to the Project64 Netplay Download Page"""
  async with ctx.typing():
      await ctx.send('**Project64 Netplay Stable Builds:**\n<https://pj64netplay-emu.ml/download.html>')

#Mupen64Plus Emulator Command
@client.command(aliases=['mupen64'])
async def mupen64plus(ctx):
  """Sends a link to the Mupen64Plus Download Page"""
  async with ctx.typing():
      await ctx.send('**Mupen64 Stable Builds:**\nNot Recommended For The Average User\n<https://github.com/mupen64plus/mupen64plus-core/releases/>\n\n**m64p (Mupen64 Plus a GUI) Builds**:\nRecommended for its Custom Plugins that fits well with its GUI\n<https://github.com/loganmc10/m64p/releases>\n\n**M64Py (Mupen 64 Python) Builds**:\nHas a Decent GUI and good Plugin Support\n<https://sourceforge.net/projects/m64py/files/>')

#CEN64 Emulator Command
@client.command()
async def cen64(ctx):
  """Sends a link to the CEN64 Download Page"""
  async with ctx.typing():
      await ctx.send('**CEN64 Stable Builds:**\n<https://cen64.com/>\n\n**CEN64-QT Builds:**\nGUI for CEN64\n<https://github.com/dh4/cen64-qt/releases>')

#Nemu64 Emulator Command
@client.command()
async def nemu64(ctx):
  """Sends a link to the Nemu64 Download Page"""
  async with ctx.typing():
      await ctx.send('**Nemu64 0.8 Mirror lInk:**\nOnly Use for Its Extensive Set of Plugins. Offical Website is long dead\n<https://www.majorgeeks.com/files/details/nemu64.html/>')

#Dolphin Emulator Command
@client.command()
async def dolphin(ctx):
  """Sends a link to the Dolphin Emulator Download Page"""
  async with ctx.typing():
      await ctx.send('**Dolphin Stable 5.0:\n<https://dl-mirror.dolphin-emu.org/5.0/dolphin-x64-5.0.exe>\n\n**Dolphin Development Builds**\n<https://dolphin-emu.org/download/list/master/1/>')

#Cemu Emulator Command
@client.command()
async def cemu(ctx):
  """Sends a link to the Cemu Download Page"""
  async with ctx.typing():
      await ctx.send('**Cemu Stable Build:**\n<http://cemu.info/#download>')

#Kill Command
@client.command(aliases=['kill-doopliss'])
async def kill(ctx):
  await ctx.send("You want to kill WHO? Me.... What did I do to you")

#Board Command
@client.group()
async def board(ctx): pass

#1 Subcommand
@board.command(aliases=['1'])
async def one(ctx):

    boardList=["DK's Jungle Adventure", "Peach's Birthday Cake", "Yoshi's Tropical Island", "Mario's Rainbow Castle", "Wario's Battle Canyon", "Luigi's Engine Room", "Eternal Starm", "Bowser's Magma Mountain"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/1/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#2 Subcommand
@board.command(aliases=['2'])
async def two(ctx):

    boardList=["Western Land", "Space Land", "Mystery Land", "Pirate Land", "Horror Land", "Bowser Land"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/2/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#3 Subcommand
@board.command(aliases=['3'])
async def three(ctx):

    boardList=["Chilly Waters", "Deep Bloober Sea", "Woody Woods", "Creepy Cavern", "Spiny Desert", "Waluigi's Island"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/3/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#4 Subcommand
@board.command(aliases=['4'])
async def four(ctx):

    boardList=["Toad's Midway Madness", "Boo's Haunted Bash", "Koopa's Seaside Soiree", "Goomba's Greedy Gala", "Shy Guy's Jungle Jam", "Bowser's Gnarly Party"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/4/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#5 Subcommand
@board.command(aliases=['5'])
async def five(ctx):

    boardList=["Toy Dream", "Rainbow Dream", "Pirate Dream", "Future Dream", "Undersea Dream", "Sweet Dream", "Bowser's Nightmare"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/5/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#6 Subcommand
@board.command(aliases=['6'])
async def six(ctx):

    boardList=["Towering Treetop", "E Gadd's Garage", "Faire Square", "Snowflake Lake", "Castaway Bay", "Clockwork Castle"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/6/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#7 Subcommand
@board.command(aliases=['7'])
async def seven(ctx):

    boardList=["Grand Canal", "Pagoda Peak", "Pyramid Park", "Neon Heights", "Windmillville", "Bowser's Enchanted Inferno"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/7/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#8 Subcommand
@board.command(aliases=['7'])
async def seven(ctx):

    boardList=["DK's Treetop Temple", "Goomba's Booty Boardwalk", "King Boo's Haunted Hideaway", "Shy Guy's Perplex Express", "Koopa's Tycoon Town", "Bowser's Warped Orbit"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/8/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#9 Subcommand
@board.command(aliases=['9'])
async def nine(ctx):

    boardList=["Toad Road", "Blooper Beach", "Boo's Horror Castle", "DK's Jungle Ruins", "Bowser's Station", "Magma Mine", "Bob-omb Factory"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/9/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)
  
#10 Subcommand
@board.command(aliases=['10'])
async def ten(ctx):

    boardList=["Mushroom Park", "Whimsical Water", "Chaos Castle", "Airship Central", "Haunted Trail"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/10/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#DS Subcommand
@board.command()
async def ds(ctx):

    boardList=["Wiggler's Garden", "Kamek's Library", "Bowser's Pinball Machine", "Toadette's Music Room", "DK's Stone Statue"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/DS/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#Super Subcommand
@board.command(aliases=['s'])
async def super(ctx):

    boardList=["Whomp's Domino Ruins", "King Bob-omb's Powderkeg Mine", "Megafruit Paradise", "Kamek's Tantalizing Tower"]
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/Super/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#Superstars Subcommand
@board.command(aliases=['ss'])
async def superstars(ctx):

    boardList=["Yoshi's Tropical Island", "Peach's Birthday Cake", 'Space Land', 'Horror Land', 'Woody Woods']
    board=random.choice(boardList)
    boardParsed = urllib.parse.quote(board)

    embed = discord.Embed(title=board,
                          colour=0x98FB98,
                          timestamp=ctx.message.created_at)

    embed.set_image(url="https://raw.githubusercontent.com/UnicorNora/RNOBot/master/boards/Superstars/" + boardParsed + ".png")
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)

#Run Bot
client.run("NTU2ODQ0MzcwMTU0ODgxMDI0.XI5Xuw.S1wdhXbTTJ1lATrz5y_XKzqMOto")