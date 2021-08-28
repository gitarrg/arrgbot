

import math

# IMPORT THIRD PARTY LIBRARIES
import arrow
import discord
from discord.ext import commands


SHADOWLANDS_RELEASE = arrow.get("2020-11-24T00:00:00+01:00")

BRONJAHM_START_TIME = arrow.get("2020-11-16T18:10:00+01:00")
SKADI_START_TIME = arrow.get("2020-11-16T17:30:00+01:00")

ICECROWN_RESPAWN = 200 * 60  # respwan time in seconds (= 3h 20m)


def get_next_icecrown_spawn(start, respwan=ICECROWN_RESPAWN, offset=0):

    time_since_first = arrow.utcnow() - start
    number_of_spawns = time_since_first.total_seconds() / respwan
    next_spawn_seconds = (math.ceil(number_of_spawns) + offset) * respwan
    next_spawn = start.shift(seconds=next_spawn_seconds)
    return next_spawn


class WowCog(commands.Cog):
    """docstring for DebugCog"""
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def bfa(self, ctx):
        """Show time until BFA Release."""
        bfa_release = arrow.get("2018-08-14T00:00:00+01:00")
        time_left = bfa_release.humanize(granularity=["day", "hour", "minute"])
        banner_url = "https://wow.zamimg.com/uploads/blog/images/13411-world-of-warcraft-battle-for-azeroth-release-date-is-august-14th.jpg"

        embed = discord.Embed()
        embed.color = discord.Colour.from_rgb(255, 180, 0)
        embed.title = f"BFA Release"
        embed.description = time_left
        embed.set_image(url=banner_url)
        embed.set_footer(text=f"release on {bfa_release:DD MMMM HH:mm}")
        return await ctx.send(embed=embed)

    @commands.command(aliases=["sl"])
    async def shadowlands(self, ctx):
        """Show time until Shadowlands Release."""
        time_left = SHADOWLANDS_RELEASE.humanize(granularity=["day", "hour", "minute"])
        SHADOWLANDS_BANNER_URL = "https://i.gyazo.com/d3e1650b8d21b2d1720d43a37d59da24.jpg"

        embed = discord.Embed()
        embed.color = discord.Colour.from_rgb(255, 180, 0)
        embed.title = f"Shadowlands Release"
        embed.description = time_left
        embed.set_image(url=SHADOWLANDS_BANNER_URL)
        embed.set_footer(text=f"release on {SHADOWLANDS_RELEASE:DD MMMM HH:mm}")
        return await ctx.send(embed=embed)


    @commands.command(aliases=["bagboss", "bagman", "bagboi", "baglady"])
    async def bronjahm(self, ctx):
        embed = discord.Embed()
        embed.title = "Bronjahm Spawn Timers:"
        embed.color = discord.Colour.from_rgb(140, 60, 150)
        embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/icons/large/inv_misc_bag_26_spellfire.jpg")

        for i in range(3):
            spawn = get_next_icecrown_spawn(start=BRONJAHM_START_TIME, offset=i)
            spawn_fmt = spawn.strftime("%d.%m.%Y %H:%M ST")
            spawn_dur = spawn.humanize(granularity=["hour", "minute"])
            embed.add_field(name=spawn_fmt, value=spawn_dur, inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=["blueproto"])
    async def skadi(self, ctx):
        embed = discord.Embed()
        embed.title = "Skadi the Ruthless Spawn Timers:"
        embed.color = discord.Colour.from_rgb(10, 222, 230)
        embed.set_thumbnail(url="https://wow.zamimg.com/images/wow/icons/large/ability_mount_drake_proto.jpg")

        for i in range(3):
            spawn = get_next_icecrown_spawn(start=SKADI_START_TIME, offset=i)
            spawn_fmt = spawn.strftime("%d.%m.%Y %H:%M ST")
            spawn_dur = spawn.humanize(granularity=["hour", "minute"])
            embed.add_field(name=spawn_fmt, value=spawn_dur, inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(WowCog(bot))
