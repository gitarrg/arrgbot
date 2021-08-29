"""Fake RCU Commands."""

# IMPORT STANDARD LIBRARIES
import random

# IMPORT THIRD PARTY LIBRARIES
import discord
from discord.ext import commands

# IMPORT LOCAL LIBRARIES
from arrgbot import emotes


def get_balance():

    # get max
    f = random.random()
    m = 10
    if f > 0.05:
        m = 100
    if f > 0.4:
        m = 500000 # 500k
    if f > 0.9:
        m = 10000000 # 10m
    if f > 0.95:
        m = 100000000 # 100m

    return random.randint(0, m)


class RCUCog(commands.Cog):
    """docstring for DebugCog"""
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return

        cmd = message.content.lower().split(" ")[0]
        if cmd in (".b", ".balance"):
            message.content = "!" + message.content[1:]

            ctx = await self.bot.get_context(message)
            await self.bot.process_commands(message)

    @commands.command(aliases=["b", "bal"])
    async def balance(self, ctx, member: discord.Member = None):
        """Command to check balance for the given member."""
        member = member or ctx.author

        b_cycle1 = get_balance()
        b_cycle2 = get_balance()
        b_total = b_cycle1 + b_cycle2

        embed = discord.Embed()
        embed.color = discord.Color.gold()
        embed.title = f"{member.display_name}'s Balance"
        embed.set_thumbnail(url=member.avatar_url_as())
        embed.add_field(name="Total Balance", value=f"{emotes.GOLD2} {b_total:,}", inline=False)
        embed.add_field(name="Cycle 1", value=f"{emotes.GOLD2} {b_cycle1:,}", inline=False)
        embed.add_field(name="Cycle 2", value=f"{emotes.GOLD2} {b_cycle2:,}", inline=False)
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(RCUCog(bot))
