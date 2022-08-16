import discord
from discord.ext import commands
from discord.ext.commands import bot
import os
from discord_components import *
client = discord.Client()
token = "TOKEN"

bot = commands.Bot(command_prefix="리나야 ")

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print(f"{len(client.guilds)}섭 참여")    
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f'LINA 0.0.17 | 리나야 도움말'))

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_guild_join(guild: discord.Guild):
    embed = discord.Embed(title='', description='**리나야 도움말** 로 명령어를 확인해주세요!', color=0xe99fee)
    embed.set_author(name=f'저를 초대해주셔서 정말 감사합니다!', icon_url='https://cdn.discordapp.com/attachments/994606989319602318/1006249361396740137/-1.png')
    await guild.system_channel.send(embed=embed)

bot.run(token)
