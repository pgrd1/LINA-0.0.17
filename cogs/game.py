import discord
from discord.ext import commands
from mcstatus import MinecraftServer, server

botavatar = 'https://cdn.discordapp.com/attachments/994606989319602318/1006249361396740137/-1.png'
ver = '0.0.17'
class lol(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def μλ²μν(self, ctx, ip, port=25565):
        def t_ip(ip, port):
            return "{0}:{1}".format(ip,port)
        try:
            server = MinecraftServer.lookup("{0}:{1}".format(ip,port))
            status = server.status()
            if status.players.online == status.players.max:
                embed=discord.Embed(title=f'', description="π΄ μλ²μΈμμ΄ λ€μ°Όμ΄μ! ({0}/{1})".format(status.players.online,status.players.max), color=0xe99fee)
                embed.set_author(name=f"μ ννμ  μλ²μ μλ²μνμμ!")
                embed.set_footer(text=f"LINA BOT {ver} / ({t_ip(ip,port)})", icon_url=botavatar)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title=f'', description="π’ μ¨λΌμΈμ΄μμ! ({0}/{1})".format(status.players.online,status.players.max), color=0xe99fee)
                embed.set_author(name=f"μ ννμ  μλ²μ μλ²μνμμ!")
                embed.set_footer(text=f"LINA BOT {ver} / ({t_ip(ip,port)})", icon_url=botavatar)
                await ctx.send(embed=embed)
        except:
            embed=discord.Embed(title=f'', description="βͺοΈ μ΄ μλ²λ μ€νλΌμΈμ΄λ€μ..", color=0xe99fee)
            embed.set_author(name=f"μ ννμ  μλ²μ μλ²μνμμ!")
            embed.set_footer(text=f"LINA BOT {ver} / ({t_ip(ip,port)})", icon_url=botavatar)
            await ctx.send(embed=embed)
    @μλ²μν.error
    async def μλ²μν_error(self,ctx, error):
        embed1 = discord.Embed(title="", description="```ini\nλ¦¬λμΌ μλ²μν [ μ£Όμ ] [ ν¬νΈ ]\n```", color=0xe99fee)
        embed1.set_author(name="IPλλ μ£Όμλ₯Ό μλ ₯ν΄μ£ΌμΈμ!",  icon_url=botavatar)
        embed1.set_footer(text=f"LINA BOT {ver}", icon_url=botavatar)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embed1)

def setup(bot):
    bot.add_cog(lol(bot))
