import discord
from discord.ext import commands
from mcstatus import MinecraftServer, server

botavatar = 'https://cdn.discordapp.com/attachments/994606989319602318/1006249361396740137/-1.png'
ver = '0.0.17'
class lol(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def 서버상태(self, ctx, ip, port=25565):
        def t_ip(ip, port):
            return "{0}:{1}".format(ip,port)
        try:
            server = MinecraftServer.lookup("{0}:{1}".format(ip,port))
            status = server.status()
            if status.players.online == status.players.max:
                embed=discord.Embed(title=f'', description="🔴 서버인원이 다찼어요! ({0}/{1})".format(status.players.online,status.players.max), color=0xe99fee)
                embed.set_author(name=f"선택하신 서버의 서버상태에요!")
                embed.set_footer(text=f"LINA BOT {ver} / ({t_ip(ip,port)})", icon_url=botavatar)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title=f'', description="🟢 온라인이에요! ({0}/{1})".format(status.players.online,status.players.max), color=0xe99fee)
                embed.set_author(name=f"선택하신 서버의 서버상태에요!")
                embed.set_footer(text=f"LINA BOT {ver} / ({t_ip(ip,port)})", icon_url=botavatar)
                await ctx.send(embed=embed)
        except:
            embed=discord.Embed(title=f'', description="⚪️ 이 서버는 오프라인이네요..", color=0xe99fee)
            embed.set_author(name=f"선택하신 서버의 서버상태에요!")
            embed.set_footer(text=f"LINA BOT {ver} / ({t_ip(ip,port)})", icon_url=botavatar)
            await ctx.send(embed=embed)
    @서버상태.error
    async def 서버상태_error(self,ctx, error):
        embed1 = discord.Embed(title="", description="```ini\n리나야 서버상태 [ 주소 ] [ 포트 ]\n```", color=0xe99fee)
        embed1.set_author(name="IP또는 주소를 입력해주세요!",  icon_url=botavatar)
        embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embed1)

def setup(bot):
    bot.add_cog(lol(bot))
