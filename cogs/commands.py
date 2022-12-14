import discord
from discord import guild
from discord.ext import commands
import asyncio , random
import psutil
from datetime import datetime
from discord_components import *
import time , math
import os

botavatar = 'https://cdn.discordapp.com/attachments/994606989319602318/1006249361396740137/-1.png'
ver = '0.0.17'

class Core(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            embed=discord.Embed(title=f'',description=f'π₯ {member.mention} [`{member.guild} ({str(len(member.guild.members))}λͺ)`]',color=0xe99fee)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            embed.set_author(name=f"νμν©λλ€!!",  url=member.avatar_url, icon_url=member.avatar_url)
            await member.guild.system_channel.send(embed=embed)
        except:
            pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        try:
            embed=discord.Embed(title=f'',description=f'π€ {member.mention} [`{member.guild} ({str(len(member.guild.members))}λͺ)`]',color=0xe99fee)
            embed.set_author(name=f"μλνκ°μΈμ..!",  url=member.avatar_url, icon_url=member.avatar_url)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            await member.guild.system_channel.send(embed=embed)
        except:
            pass

    @commands.command(name = 'μ λ³΄', pass_context = True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.guild_only()
    async def info(self,ctx, member: discord.Member = None):
        if member == None:
            memory_usage_dict = dict(psutil.virtual_memory()._asdict())
            memory_usage_percent = memory_usage_dict['percent']
            now = datetime.utcnow()
            elapsed = now - starttime
            seconds = elapsed.seconds
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
                
            help = "```\nπ  - κΈ°λ³Έ\nπ - LINA\nπΆ - LINA MUSIC\nπ - ANTI LINA\n```"
            emb = discord.Embed(color = 0xe99fee)
            emb.set_author(name=f'λ¦¬λμ μ λ³΄ κ΅¬μ±μ€..!')
            emb.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)

            editer = await ctx.send(embed=emb)
            em = discord.Embed(description = help, color = 0xe99fee)
            em.set_author(name=f'λ¦¬λμ μ λ³΄μμ!')
            em.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)

            mainMessage = await editer.edit(content=None,
                embed = em,
                components = [
                    [
                        Button(style = ButtonStyle.grey, emoji = 'π ', id = 'home'),
                        Button(style = ButtonStyle.grey, emoji = 'π', id = 'lina'),
                        Button(style = ButtonStyle.grey, emoji = 'π', id = 'antil')],[
                        Button(label = f"{len(self.bot.guilds)+1}λ²μ§Έλ‘ λ¦¬λ μ΄λνκΈ°", style = 5 , url = "https://discord.com/api/oauth2/authorize?client_id=860130066913296394&permissions=8&scope=bot%20applications.commands",emoji='π₯', id = 'invite')]
                ]
            )

            while True:
                try:
                    interaction = await self.bot.wait_for(
                        "button_click",
                        timeout = 20
                        )

                    help1 = f"> **λͺ¨λ** - discord py `V1.7.6`\n> **μλ²μ** - `{len(self.bot.guilds)}`\n> **λ°νμ** - `{days}μΌ {hours}μκ° {minutes}λΆ {seconds}μ΄`\n> **λ©λͺ¨λ¦¬ μ¬μ©λ** - `{memory_usage_percent}%`"
                    help2 = f"> **λ²μ ** - `{ver}`\n> **κ°λ°μ** - `pgr#8588`"
                    help4 = f"> **λ²μ ** - `0.3`\n> **κ°λ°μ** - `pgr#8588`"

                    if interaction.component.id == 'home':
                        generalem = discord.Embed(description = help1, color = 0xe99fee)
                        generalem.set_author(name=f'π  λ¦¬λμ κΈ°λ³Έμ λ³΄')
                        generalem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                        await interaction.respond(type = 7, embed = generalem)

                    if interaction.component.id == 'lina':
                        modem = discord.Embed(description = help2, color = 0xe99fee)
                        modem.set_author(name=f'π LINA μ λ³΄')
                        modem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                        await interaction.respond(type = 7, embed = modem)

                    if interaction.component.id == 'antil':
                        minecem = discord.Embed(description = help4, color = 0xe99fee)
                        minecem.set_author(name=f'π ANTI LINA μ λ³΄')
                        minecem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                        await interaction.respond(type = 7, embed = minecem)

                except asyncio.TimeoutError:
                    await editer.edit(
                        components = [
                            [
                                Button(
                                    label = "β",
                                    id = "home",
                                    style = ButtonStyle.red,
                                    disabled = True
                                ),
                                Button(
                                    label = "β",
                                    id = "lina",
                                    style = ButtonStyle.red,
                                    disabled = True
                                ),
                                Button(
                                    label = "β",
                                    id = "antil",
                                    style = ButtonStyle.red,
                                    disabled = True
                                )
                            ]
                        ]
                    )
                    break
        else:
            member = ctx.author if not member else member
            user = member
            date = datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            server = user.joined_at.isoformat().split("T")[0]
            embed = discord.Embed(title="", description=f"```cs\nλλ€μ - '{user.display_name}'\nμ¬μ©μλͺ - '{user}'\nλμ½ κ°μλ μ§ - {str(date.year)}-{str(date.month)}-{str(date.day)}\nμλ² κ°μλ μ§ - {server}\n```", color=0xe99fee)
            embed.set_author(name=f"{user}λμ μ λ³΄μμ!",  url=member.avatar_url, icon_url=member.avatar_url)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            await ctx.send(embed=embed)
            
    @info.error
    async def info_error(self,ctx, err):
        embed1 = discord.Embed(title="", description="```ini\nλ¦¬λμΌ μ λ³΄ [ μ μ  ]\n```", color=0xe99fee)
        embed1.set_author(name="μμ½κ²λ μλ μ μ μΈκ² κ°μμ..",  icon_url=botavatar)
        embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
        await ctx.send(embed=embed1)

        if isinstance(err, commands.CommandOnCooldown):
            embed = discord.Embed(title='',description=f"μ΄ λͺλ Ήμ΄λ {math.ceil(round(err.retry_after, 2))}μ΄λ€μ μ¬μ©νμ€μ μμ΅λλ€", color=0xe99fee)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            await ctx.message.reply(embed=embed)

    @commands.command(name = 'λμλ§')
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.guild_only()
    async def hhee(self,ctx):
        help = "```\nβοΈ - μΌλ° λͺλ Ήμ΄\nπ? - κ²μ λͺλ Ήμ΄\nπ§± - λ§ν¬ λͺλ Ήμ΄\nπ§ - μλ²κ΄λ¦¬μ€μ \n```"
        emb = discord.Embed(color = 0xe99fee)
        emb.set_author(name=f'λ¦¬λμ λμλ§ κ΅¬μ±μ€..!')
        emb.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)

        editer = await ctx.send(embed=emb)
        em = discord.Embed(description = help, color = 0xe99fee)
        em.set_author(name=f'λ¦¬λμ λμλ§μ΄μμ!')
        em.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)

        mainMessage = await editer.edit(content=None,
            embed = em,
            components = [
                [
                    Button(style = ButtonStyle.grey, emoji = 'βοΈ', id = 'general'),
                    Button(style = ButtonStyle.grey, emoji = 'π?', id = 'game'),
                    Button(style = ButtonStyle.grey, emoji = 'π§±', id = 'minec'),
                    Button(style = ButtonStyle.grey, emoji = 'π§', id = 'tool')]
            ]
        )

        while True:
            try:
                interaction = await self.bot.wait_for(
                    "button_click",
                    timeout = 10
                    )

                help1 = "```ini\nλ¦¬λμΌ λ°΄ [ μ μ  ] [ μ¬μ  ]\nλ¦¬λμΌ μΈλ°΄ [ μ μ  ]\nλ¦¬λμΌ μ λ³΄ [ μ μ  ]\nλ¦¬λμΌ νλ‘ν [ μ μ  ]\nλ¦¬λμΌ ν₯ [ μ μ  ] [ μ¬μ  ]\nλ¦¬λμΌ ν\nλ¦¬λμΌ μλλ‘κ·Έ\n```"
                help3 = "```ini\n[ νμ¬ λ‘€ λͺλ Ήμ΄μ μ€λ₯κ° μμ΅λλ€. ]\nλ¦¬λμΌ λ‘€ ν°μ΄ [ μ μ  ] \nλ¦¬λμΌ λ‘€ μ λ³΄ [ μ μ  ]\nλ¦¬λμΌ λ‘€ μ μ  [ μ μ  ] [ κ²μμ ]\nλ¦¬λμΌ μΏ ν°μ μ²΄ [ κ³μ  ]\n```"
                help4 = "```ini\nλ¦¬λμΌ μλ²μν [ IP or μ£Όμ ] [ PORT ]\n```"
                help5 = "```cs\n> #ANTICO νκ·Έ\nμμ€&λΉμμ΄ κ°μ§λμ\n> #ANTIIM νκ·Έ\nνμΌ,μ΄λ―Έμ§ μ€ν¬μΌλ¬ λμ\n> #ANTIURL νκ·Έ\nλ³΄λ΄λ μ¬μ΄νΈκ° κ°λ €μ§λ λμ```"

                if interaction.component.id == 'general':
                    generalem = discord.Embed(description = help1, color = 0xe99fee)
                    generalem.set_author(name=f'βοΈ λ¦¬λμ μΌλ° λͺλ Ήμ΄')
                    generalem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                    await interaction.respond(type = 7, embed = generalem)

                if interaction.component.id == 'game':
                    gameem = discord.Embed(description = help3, color = 0xe99fee)
                    gameem.set_author(name=f'π? λ¦¬λμ κ²μ λͺλ Ήμ΄')
                    gameem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                    await interaction.respond(type = 7, embed = gameem)

                if interaction.component.id == 'minec':
                    minecem = discord.Embed(description = help4, color = 0xe99fee)
                    minecem.set_author(name=f'π§± λ¦¬λμ λ§ν¬ λͺλ Ήμ΄')
                    minecem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                    await interaction.respond(type = 7, embed = minecem)

                if interaction.component.id == 'tool':
                    toolem = discord.Embed(description = help5, color = 0xe99fee)
                    toolem.set_author(name=f'π§ λ¦¬λμ μλ²κ΄λ¦¬μ€μ ')
                    toolem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                    await interaction.respond(type = 7, embed = toolem)

            except asyncio.TimeoutError:
                await editer.edit(
                    components = [
                        [
                            Button(
                                label = "β",
                                id = "general",
                                style = ButtonStyle.red,
                                disabled = True
                            ),
                            Button(
                                label = "β",
                                id = "game",
                                style = ButtonStyle.red,
                                disabled = True
                            ),
                            Button(
                                label = "β",
                                id = "minec",
                                style = ButtonStyle.red,
                                disabled = True
                            ),
                            Button(
                                label = "β",
                                id = "tool",
                                style = ButtonStyle.red,
                                disabled = True
                            )
                        ]
                    ]
                )
                break

    @hhee.error
    async def hhee_error(self, ctx, err):
        if isinstance(err, commands.CommandOnCooldown):
            embed = discord.Embed(title='',description=f"μ΄ λͺλ Ήμ΄λ {math.ceil(round(err.retry_after, 2))}μ΄λ€μ μ¬μ©νμ€μ μμ΅λλ€", color=0xe99fee)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            await ctx.message.reply(embed=embed)

    @commands.command(name='ν' , pass_context = True)
    async def pingg(self,ctx):
        embed = discord.Embed(title="", description=f"νμ¬ λ¦¬λμ νμ **{round(self.bot.latency*1000)}ms** μλλ€!", color=0xe99fee)
        embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
        await ctx.send(embed=embed)

    @commands.command(name="νλ‘ν")
    async def profile(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(colour=0xe99fee)
        embed.set_author(name=f"{member} μ νλ‘νμ΄μμ!", url=member.avatar_url, icon_url=member.avatar_url)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @profile.error
    async def pro_error(self,ctx, error):
        embed1 = discord.Embed(title="", description="```ini\nλ¦¬λμΌ νλ‘ν [ μ μ  ]\n```", color=0xe99fee)
        embed1.set_author(name="μμ½κ²λ μλ μ μ μΈκ² κ°μμ..",  icon_url=botavatar)
        embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
        await ctx.send(embed=embed1)
        

    @commands.command(name="μλλ‘κ·Έ" , pass_context = True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def updatelog(self ,ctx):
        contents = [
        discord.Embed(description='λ¦¬λμ μ€λλ μ­μ¬λ€μ λ³΄μΈμ!\n`βοΈ` μ `βΆοΈ` λ‘ νμ΄μ§λ₯Ό λκΈ°μΈμ', color = 0xe99fee).set_author(name=f'λ¦¬λμ μλ°μ΄νΈ λ‘κ·Έ', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}"),
        discord.Embed(description="```cs\n#2021-9-10\n1. 'λ¦¬λμΆμ'\n2. 'κΈ°λ³Έ' λͺλ Ήμ΄λ€ μΆκ°\n3. 'κ°μ±'μλ μλ² λλ‘ μμ ```", color = 0xe99fee).set_author(name=f'LINA 0.0.01 Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar),
        discord.Embed(description="```cs\n#2022-3-17\n1. 'μ λ³΄' λͺλ Ήμ΄ μΆκ°\n2. 'νλ‘ν' λͺλ Ήμ΄ μΆκ°\n3. μΌλΆ 'λͺλ Ήμ΄' μμ \n4. 'μν° νκ·Έ'κΈ°λ₯ μΆκ°```", color = 0xe99fee).set_author(name=f'LINA 0.0.03 Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar),
        discord.Embed(description="```cs\n#2022-4-23\n1. 'ν₯,λ°΄,μΈλ°΄' λͺλ Ήμ΄ λ¦¬λͺ¨λΈλ§ λ° κΈ°λ₯μΆκ°\n2. 'λ§ν¬ μλ² μν'νμΈ λͺλ Ήμ΄ μΆκ°\n3. μΌλΆ λͺλ Ήμ΄ 'μμ°μ€λ¬μ΄' λ§ν¬λ‘ λ¦¬λͺ¨λΈλ§\n4. 'μν΄μ₯' λ‘κ·Έ μΆκ°```", color = 0xe99fee).set_author(name=f'LINA 0.0.05 Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar),
        discord.Embed(description="```cs\n#2022-5-12\n1. '(μ­μ λ¨)' λͺλ Ήμ΄ μ€μ¬ λκ·λͺ¨ μλ°μ΄νΈ\n2. 'μΌλΆ' λͺλ Ήμ΄ λ¦¬λͺ¨λΈλ§```", color = 0xe99fee).set_author(name=f'LINA 0.0.1B Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar),
        discord.Embed(description="```cs\n#2022-6-3\n1. 'μΌλΆ λͺλ Ήμ΄' 'λ²νΌ'μ νμ©ν λͺλ Ήμ΄λ‘ λ¦¬λͺ¨λΈλ§\n2. 'λλ°° λ°©μ§'κΈ°λ₯ μΆκ°```", color = 0xe99fee).set_author(name=f'LINA 0.0.15 Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar),
        discord.Embed(description="```cs\n#2022-6-5\n1. 'μΏ ν€λ° νΉλ€' κ΄λ ¨ λͺλ Ήμ΄ 1μ’ μΆκ°```", color = 0xe99fee).set_author(name=f'LINA 0.0.17 Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
        ]
        
        pages = 7
        cur_page = 1
        message = await ctx.send(embed=contents[cur_page-1])

        await message.add_reaction("βοΈ")
        await message.add_reaction("βΆοΈ")
        def check(reaction, user):
            if reaction.message.id == message.id:
                return user == ctx.author and str(reaction.emoji) in ["βοΈ", "βΆοΈ"]
            else:
                pass

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)

                if str(reaction.emoji) == "βΆοΈ" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "βοΈ" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)
            except discord.errors.Forbidden:
                embed = discord.Embed(title="", description="λ©μμ§ κ΄λ¦¬ κΆνμ λ£μ΄μ£ΌμΈμ!", color=0xe99fee)
                embed.set_author(name="λ©μμ§ κ΄λ¦¬ κΆνμ΄ μμ΄μ..!",  icon_url=botavatar)
                embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                await ctx.send(embed = embed)
                return
            except asyncio.TimeoutError:
                await message.clear_reactions()
                break

    @updatelog.error
    async def updatelog_error(self, ctx, err):
        if isinstance(err, commands.CommandOnCooldown):
            embed = discord.Embed(title='',description=f"μ΄ λͺλ Ήμ΄λ {math.ceil(round(err.retry_after, 2))}μ΄λ€μ μ¬μ©νμ€μ μμ΅λλ€", color=0xe99fee)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            await ctx.message.reply(embed=embed)

    @commands.command(name="ν₯")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, message=None):
                try:
                     if member is None:
                            embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ ν₯ [ μ μ  ] [ μ¬μ  ]\n```", color=0xe99fee)
                            embed.set_author(name="μΆλ°©ν  μ μ λ₯Ό μ μ΄μ£ΌμΈμ!",  icon_url=botavatar)
                            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                            await ctx.send(embed=embed)
                     else:
                          if member is ctx.author:
                               embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ ν₯ [ μ μ  ] [ μ¬μ  ]\n```", color=0xe99fee)
                               embed.set_author(name="μκΈ°μμ μ μΆλ°© ν  μ μμ΄μ!",  icon_url=botavatar)
                               embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                               await ctx.send(embed=embed)
                          elif member.guild_permissions.administrator is True:
                               embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ ν₯ [ μ μ  ] [ μ¬μ  ]\n```", color=0xe99fee)
                               embed.set_author(name="κ΄λ¦¬μλ μΆλ°© ν  μ μμ΄μ!",  icon_url=botavatar)
                               embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                               return await ctx.send(embed=embed)
                          elif message is None:
                                embed=discord.Embed(title=f'',description=f'> `μ¬μ  : μμ`',color=0xe99fee)
                                embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                embed.set_author(name=f"{member.name} λμ΄ μΆλ°©λμμ΄μ.",  url=member.avatar_url, icon_url=member.avatar_url)
                                await ctx.send(embed=embed)
                                embed1=discord.Embed(title=f'',description=f'> `μ¬μ  : μμ`',color=0xe99fee)
                                embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                embed1.set_author(name=f"{ctx.author}λμ μν΄ ν₯μ΄ λμμ΄μ.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                channel = await member.create_dm()
                                await channel.send(embed=embed1)
                                await member.kick(reason=f"{ctx.author}λμ μν΄ μΆλ°©λΉνμ΄μ..")
                          else:
                               try:
                                    embed=discord.Embed(title=f'',description=f'> `μ¬μ  : {message}`',color=0xe99fee)
                                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed.set_author(name=f"{member.name} λμ΄ μΆλ°©λμμ΄μ.",  url=member.avatar_url, icon_url=member.avatar_url)
                                    embed1=discord.Embed(title=f'',description=f'> `μ¬μ  : {message}`',color=0xe99fee)
                                    embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed1.set_author(name=f"{ctx.author}λμ μν΄ ν₯μ΄ λμμ΄μ.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                    channel = await member.create_dm()
                                    await channel.send(embed=embed1)
                                    await member.kick(reason=f"{ctx.author}λμ μν΄ μΆλ°©λΉνμ΄μ..\nμ¬μ  : {message}")
                                    await ctx.send(embed=embed)
                               except:
                                    embed=discord.Embed(title=f'',description=f'> `μ¬μ  : μ μ μμ`',color=0xe99fee)
                                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed.set_author(name=f"{member.name} λμ΄ μΆλ°©λμμ΄μ.",  url=member.avatar_url, icon_url=member.avatar_url)
                                    embed1=discord.Embed(title=f'',description=f'> `μ¬μ  : μ μ μμ`',color=0xe99fee)
                                    embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed1.set_author(name=f"{ctx.author}λμ μν΄ ν₯μ΄ λμμ΄μ.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                    channel = await member.create_dm()
                                    await channel.send(embed=embed1)
                                    await member.kick(reason=f"{ctx.author}λμ μν΄ μΆλ°©λΉνμ΄μ.")
                                    await ctx.send(embed=embed)

                except discord.ext.commands.MissingPermissions:
                     embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ ν₯ [ μ μ  ] [ μ¬μ  ]\n```", color=0xe99fee)
                     embed.set_author(name="κΆνμ΄ μμ΄μ μΆλ°© ν  μ μμ΄μ!",  icon_url=botavatar)
                     embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
                     await ctx.send(embed=embed)

                except discord.Forbidden as owo:
                    embed = discord.Embed(title="", description="λ§΄λ² μΆλ°© κΆνμ λ£μ΄μ£ΌμΈμ!", color=0xe99fee)
                    embed.set_author(name="μΆλ°© κΆνμ΄ μμ΄μ!",  icon_url=botavatar)
                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
                    await ctx.send(embed = embed)
    @kick.error
    async def unban_error(self, ctx, err):
            embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ ν₯ [ μ μ  ] [ μ¬μ  ]\n```", color=0xe99fee)
            embed.set_author(name="ν΄λΉνλ μ μ κ° μλ²μ μμ΄μ!",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)


    @commands.command(name="λ°΄")
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, message=None):
                user: discord.Member
                try:
                     if member is None:
                            embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ λ°΄ [ μ μ  ] [ μ¬μ  ]\n```", color=0xe99fee)
                            embed.set_author(name="λ°΄ν  μ μ λ₯Ό μ μ΄μ£ΌμΈμ!",  icon_url=botavatar)
                            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                            await ctx.send(embed=embed)
                     else:
                          if member is ctx.author:
                               embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ λ°΄ [ μ μ  ] [ μ¬μ  ]\n```", color=0xe99fee)
                               embed.set_author(name="μκΈ°μμ μ λ°΄ ν  μ μμ΄μ!",  icon_url=botavatar)
                               embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                               await ctx.send(embed=embed)
                          elif member.guild_permissions.administrator is True:
                               embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ λ°΄ [ μ μ  ] [ μ¬μ  ]\n```", color=0xe99fee)
                               embed.set_author(name="κ΄λ¦¬μλ λ°΄ ν  μ μμ΄μ!",  icon_url=botavatar)
                               embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                               return await ctx.send(embed=embed)
                          elif message is None:
                                    embed=discord.Embed(title=f'',description=f'> `μ¬μ  : μμ`',color=0xe99fee)
                                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed.set_author(name=f"{member.name} λμ΄ λ°΄ λμμ΄μ.",  url=member.avatar_url, icon_url=member.avatar_url)
                                    await ctx.send(embed=embed)
                                    embed1=discord.Embed(title=f'',description=f'> `μ¬μ  : μμ`',color=0xe99fee)
                                    embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed1.set_author(name=f"{ctx.author}λμ μν΄ λ°΄μ΄ λμμ΄μ.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                    channel = await member.create_dm()
                                    await channel.send(embed=embed1)
                                    await member.ban(reason=f"{ctx.author}λμ μν΄ λ°΄ , μ¬μ  : μμ")
                          else:
                               try:
                                    embed=discord.Embed(title=f'',description=f'> `μ¬μ  : {message}`',color=0xe99fee)
                                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed.set_author(name=f"{member.name} λμ΄ λ°΄ λμμ΄μ.",  url=member.avatar_url, icon_url=member.avatar_url)
                                    await ctx.send(embed=embed)
                                    embed1=discord.Embed(title=f'',description=f'> `μ¬μ  : {message}`',color=0xe99fee)
                                    embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed1.set_author(name=f"{ctx.author}λμ μν΄ λ°΄μ΄ λμμ΄μ.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                    channel = await member.create_dm()
                                    await channel.send(embed=embed1)
                                    await member.ban(reason=f"{ctx.author}λμ μν΄ λ°΄ , μ¬μ  : {message}")
                               except:
                                    embed=discord.Embed(title=f'',description=f'> `μ¬μ  : μ μ μμ`',color=0xe99fee)
                                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed.set_author(name=f"{member.name} λμ΄ λ°΄ λμμ΄μ.",  url=member.avatar_url, icon_url=member.avatar_url)
                                    await ctx.send(embed=embed)
                                    embed1=discord.Embed(title=f'',description=f'> `μ¬μ  : μ μ μμ`',color=0xe99fee)
                                    embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed1.set_author(name=f"{ctx.author}λμ μν΄ λ°΄μ΄ λμμ΄μ.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                    channel = await member.create_dm()
                                    await channel.send(embed=embed1)
                                    await member.ban(reason=f"{ctx.author}λμ μν΄ λ°΄ , μ¬μ  : μ μ μμ")

                except discord.ext.commands.MissingPermissions:
                     embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ λ°΄ [ μ μ  ] [ μ¬μ  ]\n```", color=0xe99fee)
                     embed.set_author(name="κΆνμ΄ μμ΄μ μΆλ°© ν  μ μμ΄μ!",  icon_url=botavatar)
                     embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
                     await ctx.send(embed=embed)

                except discord.Forbidden as owo:
                    embed = discord.Embed(title="", description="λ§΄λ² λ°΄ κΆνμ λ£μ΄μ£ΌμΈμ!", color=0xe99fee)
                    embed.set_author(name="λ°΄ κΆνμ΄ μμ΄μ!",  icon_url=botavatar)
                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
                    await ctx.send(embed = embed)
    @ban.error
    async def unban_error(self, ctx, err):
            embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ λ°΄ [ μ μ  ] [ μ¬μ  ]\n```", color=0xe99fee)
            embed.set_author(name="ν΄λΉνλ μ μ κ° μλ²μ μμ΄μ!",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)

    @commands.command(name="μΈλ°΄")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,member):
        banned_users = await ctx.guild.bans()
        found = False
        try:
            member_name,member_id = member.split("#")
        except ValueError:
            embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ μΈλ°΄ [ μ μ  ]\n```", color=0xe99fee)
            embed.set_author(name="μ μ μ μμ΄λλ₯Ό μ¨μ£ΌμΈμ! (OOO#1111)",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)
            return

        if member_id.isnumeric() == False or len(member_id) >4:
            embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ μΈλ°΄ [ μ μ  ]\n```", color=0xe99fee)
            embed.set_author(name="μ μ λ₯Ό μ ννκ² μ¨μ£ΌμΈμ! (OOO#1111)",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)
            return

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name,user.discriminator) == (member_name,member_id):
                embed=discord.Embed(title=f'',description=f'',color=0xe99fee)
                embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                embed.set_author(name=f"{user.name} λμ λ°΄μ΄ νλ Έμ΄μ!!",  url=user.avatar_url, icon_url=user.avatar_url)
                await ctx.send(embed=embed)
                await ctx.guild.unban(user)
                found = True
                return
                    
        if found == False:
            embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ μΈλ°΄ [ μ μ  ]n```", color=0xe99fee)
            embed.set_author(name="μΈκΈλ μ μ κ° λ°΄ λ¦¬μ€νΈμ μμ΄μ!",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)
            return

    @unban.error
    async def unban_error(self, ctx, err):
        if isinstance(err, commands.MissingRequiredArgument):
            embed = discord.Embed(title="", description="```ini\nλ¦¬λμΌ μΈλ°΄ [ μ μ  ]\n```", color=0xe99fee)
            embed.set_author(name="μΈλ°΄ν  μ μ λ₯Ό μ μ΄μ£ΌμΈμ!",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title="", description="λ§΄λ² λ°΄ κΆνμ λ£μ΄μ£ΌμΈμ!", color=0xe99fee)
            embed.set_author(name="μΈλ°΄ κΆνμ΄ μμ΄μ!",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)

starttime = datetime.utcnow()
def setup(bot):
    bot.add_cog(Core(bot))
