import arrow
import discord
from discord.ext import commands


AFFIXES = {
    # level 2
    9:   discord.PartialEmoji(id=718570191729983540, name="Tyrannical"),
    10:  discord.PartialEmoji(id=718570099329597520, name="Fortified"),

    # level 4
    6:   discord.PartialEmoji(id=718570145462616163, name="Raging"),
    7:   discord.PartialEmoji(id=718570070921707650, name="Bolstering"),
    8:   discord.PartialEmoji(id=718570158389592094, name="Sanguine"),
    11:  discord.PartialEmoji(id=718570079922684018, name="Bursting"),
    122: discord.PartialEmoji(id=1023997191804690492, name="Inspiring"),
    123: discord.PartialEmoji(id=1023997271269982208, name="Spiteful"),

    # Level 8
    2:   discord.PartialEmoji(id=718570169680527501, name="Skittish"),
    5:   discord.PartialEmoji(id=718570180007034971, name="Teeming"),
    3:   discord.PartialEmoji(id=718570203327365193, name="Volcanic"),
    4:   discord.PartialEmoji(id=718570127813115939, name="Necrotic"),
    12:  discord.PartialEmoji(id=718570108145893448, name="Grievous"),
    13:  discord.PartialEmoji(id=718570089196290170, name="Explosive"),
    14:  discord.PartialEmoji(id=718570136801640621, name="Quaking"),
    124: discord.PartialEmoji(id=1023997637944410223, name="Storming"),

    # Seasonal Affix
    131: discord.PartialEmoji(id=1023997867867787375, name="Shrouded"),
}


# https://www.wowhead.com/affixes
AFFIX_WEEKS = {
    1: [9, 122, 14, 131],
    2: [10, 8, 12, 131],
    3: [9, 7, 13, 131],
    4: [10, 11, 124, 131],
    5: [9, 6, 3, 131],
    6: [10, 122, 12, 131],
    7: [9, 123, 4, 131],
    8: [10, 7, 14, 131],
    9: [9, 8, 124, 131],
    10: [10, 6, 13, 131],
    11: [9, 11, 3, 131],
    12: [10, 123, 4, 131],
}


# "week 1" of the current season
SEASON_START = arrow.get("2022.08.03 07:00:00+00:00")


################################################################################
# Functions to help get the current wow reset
#


def get_weeks_since(date):
    diff = arrow.utcnow() - date
    return diff.days // 7 # number of weeks passed


@commands.command(aliases=["affix", "a"])
async def affixes(self, ctx, n: int = 3):
    """Shows the Affixes for the next 3 Weeks."""
    n = min(n, 12)

    current_week =  get_weeks_since(SEASON_START)

    embed = discord.Embed()
    embed.title = "M+ Affixes"
    embed.color = discord.Colour.from_rgb(60, 170, 180)


    col1, col2, col3 = [], [], []
    for i in range(n):
        week = (current_week + i) % 12
        week += 1 
        col1.append(f"**{week}**" if i == 0 else str(week))

        affixes = AFFIX_WEEKS[week]
        emotes = [str(AFFIXES[a]) for a in affixes]
        emotes = "".join(emotes)
        col2.append(emotes)


        week_start = SEASON_START.shift(weeks=current_week + i)
        week_end = SEASON_START.shift(weeks=current_week + i + 1)
        when_ts = f"{week_start.format('DD.MM')} - {week_end.format('DD.MM')} (<t:{week_start.timestamp():.0f}:R>)"
        if i == 0:
            when_ts = f"**{when_ts}**"
        col3.append(when_ts)


    embed.add_field(name="Week:", value="\n".join(col1))
    embed.add_field(name="Affixes:", value="\n".join(col2))
    embed.add_field(name="When:", value="\n".join(col3))

    await ctx.send(embed=embed)
