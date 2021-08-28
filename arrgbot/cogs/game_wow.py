"""Commands related to World of Warcraft."""

# IMPORT STANDARD LIBRARIES
import re
import math
import typing
import datetime

# IMPORT THIRD PARTY LIBRARIES
import arrow
import discord
from discord.ext import commands

# IMPORT LOCAL LIBRARIES
from arrgbot import emotes
from arrgbot.utils import discord_utils
from arrgbot import wow_data
from arrgbot.utils import raider_io
from arrgbot.utils import utils_warcraftlogs
from arrgbot.utils import wow_constants


BRONJAHM_START_TIME = arrow.get("2020-11-16T18:10:00+01:00")
SKADI_START_TIME = arrow.get("2020-11-16T17:30:00+01:00")

ICECROWN_RESPAWN = 200 * 60  # respwan time in seconds (= 3h 20m)


def get_next_icecrown_spawn(start, respwan=ICECROWN_RESPAWN, offset=0):

    time_since_first = arrow.utcnow() - start
    number_of_spawns = time_since_first.total_seconds() / respwan
    next_spawn_seconds = (math.ceil(number_of_spawns) + offset) * respwan
    next_spawn = start.shift(seconds=next_spawn_seconds)
    return next_spawn


################################################################################
# Functions to help get the current wow reset
#

ONE_WEEK = datetime.timedelta(weeks=1)
HALFWEEK = ONE_WEEK / 2.0  # aka 3d 12h

def get_last_reset():
    now = arrow.utcnow().to("Europe/Berlin")
    reset = now
    reset = reset.floor("week")            # => Monday 0:00
    reset = reset.shift(days=2, hours=9)   # => Wednesday 9:00
    if reset > now:
        reset = reset.shift(days=-7)
    return reset


def get_next_reset():
    return get_last_reset().shift(days=7)


def get_week_id():
    reset = get_last_reset()
    week = reset.isocalendar()[1]
    return week


def get_time_until_halfweek():
    time_until_reset = get_next_reset() - arrow.utcnow().to("Europe/Berlin")
    if time_until_reset > HALFWEEK:
        time_until_reset -= HALFWEEK
    return time_until_reset


def get_halfweek_id():
    halfweek_id = get_week_id() * 2  # 2 half weeks per week (5 head)
    if (arrow.utcnow().to("Europe/Berlin") - get_last_reset()) > HALFWEEK:
        halfweek_id += 1 # we are in the second half of the week

    halfweek_id = halfweek_id - 41 # initial offset
    return halfweek_id

def get_vendor_corruptions(set_id=None):

    if set_id == None:
        set_id = get_halfweek_id()
    set_id = set_id % 8
    return wow_constants.CORRUPTION_VENDOR_SETS.get(set_id, [])


################################################################################
# Character Name/Realm Utils
#

class NicknameMention(commands.MemberConverter):

    async def convert(self, ctx, argument):

        try:
            member = await super().convert(ctx, argument)
        except commands.errors.BadArgument:
            nickname = argument
        else:
            nickname = member.display_name

        return nickname


def get_name_realm(nickname):
    """Get the Name and Realm from a Discord Nickname."""
    if "]" in nickname:  # in case there is a "-" inside the [tag]-part
        nickname = nickname.split("]")[-1]

    user_name_re_exrp = r"(?P<name>\w+)-(?P<realm>\w+)"
    match = re.search(user_name_re_exrp, nickname, flags=re.IGNORECASE)

    values = match.groupdict() if match else {}
    return  values.get("name", match), values.get("realm", "")


################################################################################


class WowCog(commands.Cog):
    """Cog for some World of Warcraft related commands."""

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        raise error

    ################################
    # Expansion Release Dates
    #

    def _wow_expansion_release(self, expansion):
        embed = discord.Embed()
        embed.color = discord.Colour.from_rgb(255, 180, 0)
        embed.title = f"{expansion.name} Release"
        embed.description = expansion.release.humanize(granularity=["day", "hour", "minute"])
        embed.set_image(url=expansion.img)
        embed.set_footer(text=f"release on {expansion.release:DD MMMM HH:mm}")
        return embed

    @commands.command()
    async def bfa(self, ctx):
        """Show time until/since BFA Release."""
        embed = self._wow_expansion_release(wow_data.BFA)
        return await ctx.send(embed=embed)

    @commands.command(aliases=["sl"])
    async def shadowlands(self, ctx):
        """Show time until/since Shadowlands Release."""
        embed = self._wow_expansion_release(wow_data.SHADOWLANDS)
        return await ctx.send(embed=embed)

    ################################
    # Shadowlands: Prepatch Event
    #
    #
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

    ############################################################################
    # Character/RIO Info
    #

    @commands.command()
    async def rio(self, ctx, nickname: typing.Optional[NicknameMention]):
        """Lookup someones RIO Profile."""
        nickname = nickname or ctx.author.display_name
        name, realm = get_name_realm(nickname)
        if not (name and realm):
            return await ctx.send("unable to detect your character name and realm.\nuse `!rio Name-Realm` to lookup a char.")

        message = await ctx.send(embed=discord_utils.EMBED_LOADING)

        rio_info = await raider_io.get_booster_rio(name, realm)
        if not rio_info.get("url"):
            return await ctx.send("Character not found... u drunk?")

        embed = raider_io.build_rio_embed(rio_info)
        return await message.edit(embed=embed)

    @commands.command()
    async def logs(self, ctx, nickname: typing.Optional[NicknameMention]):
        """Lookup someones RIO Profile."""

        nickname = nickname or ctx.author.display_name
        name, realm = get_name_realm(nickname)
        if not (name and realm):
            return await ctx.send("unable to detect your character name and realm.\nuse `!rio Name-Realm` to lookup a char.")

        message = await ctx.send(embed=discord_utils.EMBED_LOADING)

        embed = await utils_warcraftlogs.build_wcl_embed(f"{name}-{realm}")
        if not embed:
            return await message.edit(content="Character not found... u drunk?", embed=None)

        return await message.edit(embed=embed)

    ############################
    # Reset/ID
    #
    @commands.group(pass_context=True, aliases=["v", "vendor", "cv"], case_insensitive=True)
    async def corruption_vendor(self, ctx, set_id: typing.Optional[int]): #, item_set: int = None):
        if ctx.invoked_subcommand:
            return

        set_id = set_id or get_halfweek_id()
        set_id = set_id % 8 if set_id > 8 else set_id

        items = get_vendor_corruptions(set_id)
        if not items:
            return await ctx.send("<:peepoShrug:685432244349042688>")


        names = "\n".join([f"{item.icon} {item.name} {item.rank_str}" for item in items])
        prices = "\n".join([f"{emotes.ECHOES} {item.price}" for item in items])
        infos = "\n".join([f"+{item.corruption} | {item.info}" for item in items])

        embed = discord.Embed(title="💰 Corruption Vendor:")
        embed.description = f"Set: **{set_id}**" if set_id else ""
        embed.add_field(name="Corruption:", value=names)
        embed.add_field(name="Echoes:", value=prices)
        embed.add_field(name="Info:", value=infos)
        embed.set_footer(text="use `!vendor rotation` to see the full schedule.")
        await ctx.send(embed=embed)

    @corruption_vendor.command(name="rotation", aliases=["r", "all", "a"])
    async def corruption_vendor_rotation(self, ctx):

        now = arrow.utcnow().to("Europe/Berlin")
        embed = discord.Embed(title="💰 Corruption Vendor Rotation:")
        halfweek = get_halfweek_id()

        for i in range(8):
            set_id = halfweek + i
            items = get_vendor_corruptions(set_id)
            set_id = set_id % 8 if set_id > 8 else set_id


            start = now + (get_time_until_halfweek() + ((i-1) * HALFWEEK))
            end = start + HALFWEEK

            if i == 0:
                when = "Now"
            elif i in [1, 2]:
                when = start.humanize(granularity=["day", "hour"])
            else:
                when = start.humanize(granularity=["week", "day"])

            if items:
                names_1 = "\n".join([item.icon_and_name for item in items[0:2]])
                names_2 = "\n".join([item.icon_and_name for item in items[2:4]])
                names_3 = "\n".join([item.icon_and_name for item in items[4:6]])
            else:
                names_1 = f"{emotes.PEEPOSHRUG}"
                names_2 = f"{emotes.PEEPOSHRUG}"
                names_3 = f"{emotes.PEEPOSHRUG}"

            line = "** **\n"
            embed.add_field(value=names_1, name=line + "**" + when + "**")
            embed.add_field(value=names_2, name=f"{line}{start:DD.MMM}- {end:DD.MMM}")
            embed.add_field(value=names_3, name=f"{line}Set Nr.: {set_id}")

            embed.set_footer(text=f"rotation confirmed {emotes.PEPESALUTE}")

        return await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(WowCog(bot))
