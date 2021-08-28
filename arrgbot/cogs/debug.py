

# IMPORT THIRD PARTY LIBRARIES
from discord.ext import commands
import discord
import arrow


SERVER_TIME = "Europe/Berlin"

def current_server_time():
    """Server Time."""
    return arrow.utcnow().to(SERVER_TIME)


class DebugCog(commands.Cog):
    """docstring for DebugCog"""
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.boottime = arrow.utcnow()

    @commands.Cog.listener()
    async def on_ready(self):
        print("[DebugCog] ready!")

    @commands.command()
    async def uptime(self, ctx):
        """Print DebugInf about uptime, latency and current day of the week."""
        now = arrow.utcnow()
        st = now.to(SERVER_TIME)
        uptime = now - self.boottime
        uptime = str(uptime)
        uptime = uptime.split(".")[0]
        latency = self.bot.latency * 1000 # convert from s to ms

        await ctx.send(
            f"uptime: `{uptime}`\n"
            f"latency: `{latency:0.2f}ms`\n"
            f"weekday: `{st:dddd}`\n"
        )

    ##########################################
    # DATE / TIME Commands
    #

    @commands.command()
    async def time(self, ctx):
        """Just prints the current time."""
        now = current_server_time()
        await ctx.send(f"🕥 Its **{now:HH:mm}**.")

    @commands.command()
    async def day(self, ctx):
        """Just prints the current day of the week."""
        now = current_server_time()
        await ctx.send(f"Today is {now:dddd}.")

    @commands.command(aliases=["monat", "månad"])
    async def month(self, ctx):
        """Just prints the current year."""
        now = current_server_time()
        await ctx.send(f"It is {now:MMMM}.")

    @commands.command()
    async def year(self, ctx):
        """Just prints the current year."""
        now = current_server_time()
        await ctx.send(f"Its {now:YYYY}.")


def setup(bot):
    bot.add_cog(DebugCog(bot))

