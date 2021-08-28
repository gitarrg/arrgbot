
# IMPORT THIRD PARTY LIBRARIES
import discord
from discord.ext import commands


class AmongUsCog(commands.Cog):
    """docstring for DebugCog"""
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.group(pass_context=True, aliases=["au"])
    async def among_us(self, ctx):
        if ctx.invoked_subcommand is None:
            return await ctx.send_help(self.among_us)

    @among_us.command(aliases=["map"])
    async def maps(self, ctx, *names):

        AMONG_US_MAPS = {}
        AMONG_US_MAPS["skeld"] = "https://i.redd.it/tv8ef4iqszh41.png"
        AMONG_US_MAPS["polus"] = "https://i.redd.it/knmus9a2vgj51.png"
        AMONG_US_MAPS["mira"] = "https://i.redd.it/8i1kd1mp9ij51.png"
        names = names or AMONG_US_MAPS.keys()

        for name in names:
            url = AMONG_US_MAPS.get(name)
            if url:
                await ctx.send(url)

def setup(bot):
    bot.add_cog(AmongUsCog(bot))
