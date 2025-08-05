import discord
from discord.ext import commands
from mcstatus.server import JavaServer

class MagbungkalStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="magbungkal.net")
    async def check_magbungkal(self, ctx):
        domain = "play.magbungkal.net"
        try:
            server = JavaServer.lookup(domain)
            status = server.status()

            embed = discord.Embed(
                title="🟢 Magbungkal.net is Online",
                description=f"**{domain}** is up and running!",
                color=discord.Color.green()
            )
            embed.add_field(name="Online Players", value=f"{status.players.online}/{status.players.max}", inline=True)
            embed.add_field(name="Version", value=status.version.name, inline=True)
            embed.add_field(name="Ping", value=f"{round(status.latency)}ms", inline=True)
            embed.set_footer(
                text="AKY Services",
                icon_url="https://media.discordapp.net/attachments/1386703646414209046/1401424618543124500/ChatGPT_Image_Aug_3_2025_11_52_42_AM.png"
            )
            await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(
                title="🔴 Magbungkal.net is Offline or Unreachable",
                description=f"Unable to reach **{domain}**\n\n**Error:** `{e}`",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(MagbungkalStatus(bot))
