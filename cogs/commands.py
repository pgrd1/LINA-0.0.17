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
            embed=discord.Embed(title=f'',description=f'📥 {member.mention} [`{member.guild} ({str(len(member.guild.members))}명)`]',color=0xe99fee)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            embed.set_author(name=f"환영합니다!!",  url=member.avatar_url, icon_url=member.avatar_url)
            await member.guild.system_channel.send(embed=embed)
        except:
            pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        try:
            embed=discord.Embed(title=f'',description=f'📤 {member.mention} [`{member.guild} ({str(len(member.guild.members))}명)`]',color=0xe99fee)
            embed.set_author(name=f"안녕히가세요..!",  url=member.avatar_url, icon_url=member.avatar_url)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            await member.guild.system_channel.send(embed=embed)
        except:
            pass

    @commands.command(name = '정보', pass_context = True)
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
                
            help = "```\n🏠 - 기본\n😀 - LINA\n🎶 - LINA MUSIC\n🔒 - ANTI LINA\n```"
            emb = discord.Embed(color = 0xe99fee)
            emb.set_author(name=f'리나의 정보 구성중..!')
            emb.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)

            editer = await ctx.send(embed=emb)
            em = discord.Embed(description = help, color = 0xe99fee)
            em.set_author(name=f'리나의 정보에요!')
            em.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)

            mainMessage = await editer.edit(content=None,
                embed = em,
                components = [
                    [
                        Button(style = ButtonStyle.grey, emoji = '🏠', id = 'home'),
                        Button(style = ButtonStyle.grey, emoji = '😀', id = 'lina'),
                        Button(style = ButtonStyle.grey, emoji = '🔒', id = 'antil')],[
                        Button(label = f"{len(self.bot.guilds)+1}번째로 리나 초대하기", style = 5 , url = "https://discord.com/api/oauth2/authorize?client_id=860130066913296394&permissions=8&scope=bot%20applications.commands",emoji='📥', id = 'invite')]
                ]
            )

            while True:
                try:
                    interaction = await self.bot.wait_for(
                        "button_click",
                        timeout = 20
                        )

                    help1 = f"> **모듈** - discord py `V1.7.6`\n> **서버수** - `{len(self.bot.guilds)}`\n> **런타임** - `{days}일 {hours}시간 {minutes}분 {seconds}초`\n> **메모리 사용량** - `{memory_usage_percent}%`"
                    help2 = f"> **버전** - `{ver}`\n> **개발자** - `pgr#8588`"
                    help4 = f"> **버전** - `0.3`\n> **개발자** - `pgr#8588`"

                    if interaction.component.id == 'home':
                        generalem = discord.Embed(description = help1, color = 0xe99fee)
                        generalem.set_author(name=f'🏠 리나의 기본정보')
                        generalem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                        await interaction.respond(type = 7, embed = generalem)

                    if interaction.component.id == 'lina':
                        modem = discord.Embed(description = help2, color = 0xe99fee)
                        modem.set_author(name=f'😀 LINA 정보')
                        modem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                        await interaction.respond(type = 7, embed = modem)

                    if interaction.component.id == 'antil':
                        minecem = discord.Embed(description = help4, color = 0xe99fee)
                        minecem.set_author(name=f'🔒 ANTI LINA 정보')
                        minecem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                        await interaction.respond(type = 7, embed = minecem)

                except asyncio.TimeoutError:
                    await editer.edit(
                        components = [
                            [
                                Button(
                                    label = "❌",
                                    id = "home",
                                    style = ButtonStyle.red,
                                    disabled = True
                                ),
                                Button(
                                    label = "❌",
                                    id = "lina",
                                    style = ButtonStyle.red,
                                    disabled = True
                                ),
                                Button(
                                    label = "❌",
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
            embed = discord.Embed(title="", description=f"```cs\n닉네임 - '{user.display_name}'\n사용자명 - '{user}'\n디코 가입날짜 - {str(date.year)}-{str(date.month)}-{str(date.day)}\n서버 가입날짜 - {server}\n```", color=0xe99fee)
            embed.set_author(name=f"{user}님의 정보에요!",  url=member.avatar_url, icon_url=member.avatar_url)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            await ctx.send(embed=embed)
            
    @info.error
    async def info_error(self,ctx, err):
        embed1 = discord.Embed(title="", description="```ini\n리나야 정보 [ 유저 ]\n```", color=0xe99fee)
        embed1.set_author(name="아쉽게도 없는 유저인것 같아요..",  icon_url=botavatar)
        embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
        await ctx.send(embed=embed1)

        if isinstance(err, commands.CommandOnCooldown):
            embed = discord.Embed(title='',description=f"이 명령어는 {math.ceil(round(err.retry_after, 2))}초뒤에 사용하실수 있습니다", color=0xe99fee)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            await ctx.message.reply(embed=embed)

    @commands.command(name = '도움말')
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.guild_only()
    async def hhee(self,ctx):
        help = "```\n⚙️ - 일반 명령어\n🎮 - 게임 명령어\n🧱 - 마크 명령어\n🔧 - 서버관리설정\n```"
        emb = discord.Embed(color = 0xe99fee)
        emb.set_author(name=f'리나의 도움말 구성중..!')
        emb.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)

        editer = await ctx.send(embed=emb)
        em = discord.Embed(description = help, color = 0xe99fee)
        em.set_author(name=f'리나의 도움말이에요!')
        em.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)

        mainMessage = await editer.edit(content=None,
            embed = em,
            components = [
                [
                    Button(style = ButtonStyle.grey, emoji = '⚙️', id = 'general'),
                    Button(style = ButtonStyle.grey, emoji = '🎮', id = 'game'),
                    Button(style = ButtonStyle.grey, emoji = '🧱', id = 'minec'),
                    Button(style = ButtonStyle.grey, emoji = '🔧', id = 'tool')]
            ]
        )

        while True:
            try:
                interaction = await self.bot.wait_for(
                    "button_click",
                    timeout = 10
                    )

                help1 = "```ini\n리나야 밴 [ 유저 ] [ 사유 ]\n리나야 언밴 [ 유저 ]\n리나야 정보 [ 유저 ]\n리나야 프로필 [ 유저 ]\n리나야 킥 [ 유저 ] [ 사유 ]\n리나야 핑\n리나야 업뎃로그\n```"
                help3 = "```ini\n[ 현재 롤 명령어에 오류가 있습니다. ]\n리나야 롤 티어 [ 유저 ] \n리나야 롤 정보 [ 유저 ]\n리나야 롤 전적 [ 유저 ] [ 게임수 ]\n리나야 쿠폰전체 [ 계정 ]\n```"
                help4 = "```ini\n리나야 서버상태 [ IP or 주소 ] [ PORT ]\n```"
                help5 = "```cs\n> #ANTICO 태그\n욕설&비속어 감지대상\n> #ANTIIM 태그\n파일,이미지 스포일러 대상\n> #ANTIURL 태그\n보내는 사이트가 가려지는 대상```"

                if interaction.component.id == 'general':
                    generalem = discord.Embed(description = help1, color = 0xe99fee)
                    generalem.set_author(name=f'⚙️ 리나의 일반 명령어')
                    generalem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                    await interaction.respond(type = 7, embed = generalem)

                if interaction.component.id == 'game':
                    gameem = discord.Embed(description = help3, color = 0xe99fee)
                    gameem.set_author(name=f'🎮 리나의 게임 명령어')
                    gameem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                    await interaction.respond(type = 7, embed = gameem)

                if interaction.component.id == 'minec':
                    minecem = discord.Embed(description = help4, color = 0xe99fee)
                    minecem.set_author(name=f'🧱 리나의 마크 명령어')
                    minecem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                    await interaction.respond(type = 7, embed = minecem)

                if interaction.component.id == 'tool':
                    toolem = discord.Embed(description = help5, color = 0xe99fee)
                    toolem.set_author(name=f'🔧 리나의 서버관리설정')
                    toolem.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                    await interaction.respond(type = 7, embed = toolem)

            except asyncio.TimeoutError:
                await editer.edit(
                    components = [
                        [
                            Button(
                                label = "❌",
                                id = "general",
                                style = ButtonStyle.red,
                                disabled = True
                            ),
                            Button(
                                label = "❌",
                                id = "game",
                                style = ButtonStyle.red,
                                disabled = True
                            ),
                            Button(
                                label = "❌",
                                id = "minec",
                                style = ButtonStyle.red,
                                disabled = True
                            ),
                            Button(
                                label = "❌",
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
            embed = discord.Embed(title='',description=f"이 명령어는 {math.ceil(round(err.retry_after, 2))}초뒤에 사용하실수 있습니다", color=0xe99fee)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            await ctx.message.reply(embed=embed)

    @commands.command(name='핑' , pass_context = True)
    async def pingg(self,ctx):
        embed = discord.Embed(title="", description=f"현재 리나의 핑은 **{round(self.bot.latency*1000)}ms** 입니다!", color=0xe99fee)
        embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
        await ctx.send(embed=embed)

    @commands.command(name="프로필")
    async def profile(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(colour=0xe99fee)
        embed.set_author(name=f"{member} 의 프로필이에요!", url=member.avatar_url, icon_url=member.avatar_url)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @profile.error
    async def pro_error(self,ctx, error):
        embed1 = discord.Embed(title="", description="```ini\n리나야 프로필 [ 유저 ]\n```", color=0xe99fee)
        embed1.set_author(name="아쉽게도 없는 유저인것 같아요..",  icon_url=botavatar)
        embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
        await ctx.send(embed=embed1)
        

    @commands.command(name="업뎃로그" , pass_context = True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def updatelog(self ,ctx):
        contents = [
        discord.Embed(description='리나의 오래된 역사들을 보세요!\n`◀️` 와 `▶️` 로 페이지를 넘기세요', color = 0xe99fee).set_author(name=f'리나의 업데이트 로그', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}"),
        discord.Embed(description="```cs\n#2021-9-10\n1. '리나출시'\n2. '기본' 명령어들 추가\n3. '개성'있는 임베드로 수정```", color = 0xe99fee).set_author(name=f'LINA 0.0.01 Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar),
        discord.Embed(description="```cs\n#2022-3-17\n1. '정보' 명령어 추가\n2. '프로필' 명령어 추가\n3. 일부 '명령어' 수정\n4. '안티 태그'기능 추가```", color = 0xe99fee).set_author(name=f'LINA 0.0.03 Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar),
        discord.Embed(description="```cs\n#2022-4-23\n1. '킥,밴,언밴' 명령어 리모델링 및 기능추가\n2. '마크 서버 상태'확인 명령어 추가\n3. 일부 명령어 '자연스러운' 말투로 리모델링\n4. '입퇴장' 로그 추가```", color = 0xe99fee).set_author(name=f'LINA 0.0.05 Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar),
        discord.Embed(description="```cs\n#2022-5-12\n1. '(삭제됨)' 명령어 중심 대규모 업데이트\n2. '일부' 명령어 리모델링```", color = 0xe99fee).set_author(name=f'LINA 0.0.1B Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar),
        discord.Embed(description="```cs\n#2022-6-3\n1. '일부 명령어' '버튼'을 활용한 명령어로 리모델링\n2. '도배 방지'기능 추가```", color = 0xe99fee).set_author(name=f'LINA 0.0.15 Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar),
        discord.Embed(description="```cs\n#2022-6-5\n1. '쿠키런 킹덤' 관련 명령어 1종 추가```", color = 0xe99fee).set_author(name=f'LINA 0.0.17 Ver Log', icon_url=botavatar).set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
        ]
        
        pages = 7
        cur_page = 1
        message = await ctx.send(embed=contents[cur_page-1])

        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        def check(reaction, user):
            if reaction.message.id == message.id:
                return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
            else:
                pass

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=contents[cur_page-1])
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)
            except discord.errors.Forbidden:
                embed = discord.Embed(title="", description="메시지 관리 권한을 넣어주세요!", color=0xe99fee)
                embed.set_author(name="메시지 관리 권한이 없어요..!",  icon_url=botavatar)
                embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                await ctx.send(embed = embed)
                return
            except asyncio.TimeoutError:
                await message.clear_reactions()
                break

    @updatelog.error
    async def updatelog_error(self, ctx, err):
        if isinstance(err, commands.CommandOnCooldown):
            embed = discord.Embed(title='',description=f"이 명령어는 {math.ceil(round(err.retry_after, 2))}초뒤에 사용하실수 있습니다", color=0xe99fee)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
            await ctx.message.reply(embed=embed)

    @commands.command(name="킥")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, message=None):
                try:
                     if member is None:
                            embed = discord.Embed(title="", description="```ini\n리나야 킥 [ 유저 ] [ 사유 ]\n```", color=0xe99fee)
                            embed.set_author(name="추방할 유저를 적어주세요!",  icon_url=botavatar)
                            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                            await ctx.send(embed=embed)
                     else:
                          if member is ctx.author:
                               embed = discord.Embed(title="", description="```ini\n리나야 킥 [ 유저 ] [ 사유 ]\n```", color=0xe99fee)
                               embed.set_author(name="자기자신은 추방 할 수 없어요!",  icon_url=botavatar)
                               embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                               await ctx.send(embed=embed)
                          elif member.guild_permissions.administrator is True:
                               embed = discord.Embed(title="", description="```ini\n리나야 킥 [ 유저 ] [ 사유 ]\n```", color=0xe99fee)
                               embed.set_author(name="관리자는 추방 할 수 없어요!",  icon_url=botavatar)
                               embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                               return await ctx.send(embed=embed)
                          elif message is None:
                                embed=discord.Embed(title=f'',description=f'> `사유 : 없음`',color=0xe99fee)
                                embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                embed.set_author(name=f"{member.name} 님이 추방되었어요.",  url=member.avatar_url, icon_url=member.avatar_url)
                                await ctx.send(embed=embed)
                                embed1=discord.Embed(title=f'',description=f'> `사유 : 없음`',color=0xe99fee)
                                embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                embed1.set_author(name=f"{ctx.author}님에 의해 킥이 되었어요.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                channel = await member.create_dm()
                                await channel.send(embed=embed1)
                                await member.kick(reason=f"{ctx.author}님에 의해 추방당했어요..")
                          else:
                               try:
                                    embed=discord.Embed(title=f'',description=f'> `사유 : {message}`',color=0xe99fee)
                                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed.set_author(name=f"{member.name} 님이 추방되었어요.",  url=member.avatar_url, icon_url=member.avatar_url)
                                    embed1=discord.Embed(title=f'',description=f'> `사유 : {message}`',color=0xe99fee)
                                    embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed1.set_author(name=f"{ctx.author}님에 의해 킥이 되었어요.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                    channel = await member.create_dm()
                                    await channel.send(embed=embed1)
                                    await member.kick(reason=f"{ctx.author}님에 의해 추방당했어요..\n사유 : {message}")
                                    await ctx.send(embed=embed)
                               except:
                                    embed=discord.Embed(title=f'',description=f'> `사유 : 알 수 없음`',color=0xe99fee)
                                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed.set_author(name=f"{member.name} 님이 추방되었어요.",  url=member.avatar_url, icon_url=member.avatar_url)
                                    embed1=discord.Embed(title=f'',description=f'> `사유 : 알 수 없음`',color=0xe99fee)
                                    embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed1.set_author(name=f"{ctx.author}님에 의해 킥이 되었어요.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                    channel = await member.create_dm()
                                    await channel.send(embed=embed1)
                                    await member.kick(reason=f"{ctx.author}님에 의해 추방당했어요.")
                                    await ctx.send(embed=embed)

                except discord.ext.commands.MissingPermissions:
                     embed = discord.Embed(title="", description="```ini\n리나야 킥 [ 유저 ] [ 사유 ]\n```", color=0xe99fee)
                     embed.set_author(name="권한이 없어서 추방 할 수 없어요!",  icon_url=botavatar)
                     embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
                     await ctx.send(embed=embed)

                except discord.Forbidden as owo:
                    embed = discord.Embed(title="", description="맴버 추방 권한을 넣어주세요!", color=0xe99fee)
                    embed.set_author(name="추방 권한이 없어요!",  icon_url=botavatar)
                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
                    await ctx.send(embed = embed)
    @kick.error
    async def unban_error(self, ctx, err):
            embed = discord.Embed(title="", description="```ini\n리나야 킥 [ 유저 ] [ 사유 ]\n```", color=0xe99fee)
            embed.set_author(name="해당하는 유저가 서버에 없어요!",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)


    @commands.command(name="밴")
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, message=None):
                user: discord.Member
                try:
                     if member is None:
                            embed = discord.Embed(title="", description="```ini\n리나야 밴 [ 유저 ] [ 사유 ]\n```", color=0xe99fee)
                            embed.set_author(name="밴할 유저를 적어주세요!",  icon_url=botavatar)
                            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                            await ctx.send(embed=embed)
                     else:
                          if member is ctx.author:
                               embed = discord.Embed(title="", description="```ini\n리나야 밴 [ 유저 ] [ 사유 ]\n```", color=0xe99fee)
                               embed.set_author(name="자기자신은 밴 할 수 없어요!",  icon_url=botavatar)
                               embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                               await ctx.send(embed=embed)
                          elif member.guild_permissions.administrator is True:
                               embed = discord.Embed(title="", description="```ini\n리나야 밴 [ 유저 ] [ 사유 ]\n```", color=0xe99fee)
                               embed.set_author(name="관리자는 밴 할 수 없어요!",  icon_url=botavatar)
                               embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                               return await ctx.send(embed=embed)
                          elif message is None:
                                    embed=discord.Embed(title=f'',description=f'> `사유 : 없음`',color=0xe99fee)
                                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed.set_author(name=f"{member.name} 님이 밴 되었어요.",  url=member.avatar_url, icon_url=member.avatar_url)
                                    await ctx.send(embed=embed)
                                    embed1=discord.Embed(title=f'',description=f'> `사유 : 없음`',color=0xe99fee)
                                    embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed1.set_author(name=f"{ctx.author}님에 의해 밴이 되었어요.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                    channel = await member.create_dm()
                                    await channel.send(embed=embed1)
                                    await member.ban(reason=f"{ctx.author}님에 의해 밴 , 사유 : 없음")
                          else:
                               try:
                                    embed=discord.Embed(title=f'',description=f'> `사유 : {message}`',color=0xe99fee)
                                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed.set_author(name=f"{member.name} 님이 밴 되었어요.",  url=member.avatar_url, icon_url=member.avatar_url)
                                    await ctx.send(embed=embed)
                                    embed1=discord.Embed(title=f'',description=f'> `사유 : {message}`',color=0xe99fee)
                                    embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed1.set_author(name=f"{ctx.author}님에 의해 밴이 되었어요.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                    channel = await member.create_dm()
                                    await channel.send(embed=embed1)
                                    await member.ban(reason=f"{ctx.author}님에 의해 밴 , 사유 : {message}")
                               except:
                                    embed=discord.Embed(title=f'',description=f'> `사유 : 알 수 없음`',color=0xe99fee)
                                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed.set_author(name=f"{member.name} 님이 밴 되었어요.",  url=member.avatar_url, icon_url=member.avatar_url)
                                    await ctx.send(embed=embed)
                                    embed1=discord.Embed(title=f'',description=f'> `사유 : 알 수 없음`',color=0xe99fee)
                                    embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                                    embed1.set_author(name=f"{ctx.author}님에 의해 밴이 되었어요.",  url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
                                    channel = await member.create_dm()
                                    await channel.send(embed=embed1)
                                    await member.ban(reason=f"{ctx.author}님에 의해 밴 , 사유 : 알 수 없음")

                except discord.ext.commands.MissingPermissions:
                     embed = discord.Embed(title="", description="```ini\n리나야 밴 [ 유저 ] [ 사유 ]\n```", color=0xe99fee)
                     embed.set_author(name="권한이 없어서 추방 할 수 없어요!",  icon_url=botavatar)
                     embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
                     await ctx.send(embed=embed)

                except discord.Forbidden as owo:
                    embed = discord.Embed(title="", description="맴버 밴 권한을 넣어주세요!", color=0xe99fee)
                    embed.set_author(name="밴 권한이 없어요!",  icon_url=botavatar)
                    embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
                    await ctx.send(embed = embed)
    @ban.error
    async def unban_error(self, ctx, err):
            embed = discord.Embed(title="", description="```ini\n리나야 밴 [ 유저 ] [ 사유 ]\n```", color=0xe99fee)
            embed.set_author(name="해당하는 유저가 서버에 없어요!",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)

    @commands.command(name="언밴")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,member):
        banned_users = await ctx.guild.bans()
        found = False
        try:
            member_name,member_id = member.split("#")
        except ValueError:
            embed = discord.Embed(title="", description="```ini\n리나야 언밴 [ 유저 ]\n```", color=0xe99fee)
            embed.set_author(name="유저의 아이디를 써주세요! (OOO#1111)",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)
            return

        if member_id.isnumeric() == False or len(member_id) >4:
            embed = discord.Embed(title="", description="```ini\n리나야 언밴 [ 유저 ]\n```", color=0xe99fee)
            embed.set_author(name="유저를 정확하게 써주세요! (OOO#1111)",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)
            return

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name,user.discriminator) == (member_name,member_id):
                embed=discord.Embed(title=f'',description=f'',color=0xe99fee)
                embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
                embed.set_author(name=f"{user.name} 님의 밴이 풀렸어요!!",  url=user.avatar_url, icon_url=user.avatar_url)
                await ctx.send(embed=embed)
                await ctx.guild.unban(user)
                found = True
                return
                    
        if found == False:
            embed = discord.Embed(title="", description="```ini\n리나야 언밴 [ 유저 ]n```", color=0xe99fee)
            embed.set_author(name="언급된 유저가 밴 리스트에 없어요!",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)
            return

    @unban.error
    async def unban_error(self, ctx, err):
        if isinstance(err, commands.MissingRequiredArgument):
            embed = discord.Embed(title="", description="```ini\n리나야 언밴 [ 유저 ]\n```", color=0xe99fee)
            embed.set_author(name="언밴할 유저를 적어주세요!",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title="", description="맴버 밴 권한을 넣어주세요!", color=0xe99fee)
            embed.set_author(name="언밴 권한이 없어요!",  icon_url=botavatar)
            embed.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar) 
            await ctx.send(embed = embed)

starttime = datetime.utcnow()
def setup(bot):
    bot.add_cog(Core(bot))
