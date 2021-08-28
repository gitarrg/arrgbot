# -*- coding: utf-8 -*-

# IMPORT STANDARD LIBRARIES
from aiohttp import ClientSession

# IMPORT THIRD PARTY LIBRARIES
import discord

# IMPORT LOCAL LIBRARIES
from arrgbot import emotes
from arrgbot.utils import wow_constants


###################################
# API Requests
#


async def get_booster_rio(name, realm, region="eu", fields=""):
    url = f"https://raider.io/api/v1/characters/profile"
    fields = fields or "mythic_plus_scores_by_season:current,guild,raid_progression,gear"
    params = {
        "region": region,
        "realm": realm,
        "name": name,
        "fields": fields,
    }
    async with ClientSession() as session:
        async with session.get(url=url, params=params) as resp:
            data = await resp.json()
    info = {}
    info.update(data)
    info["raw"] = data
    info["url"] = data.get("profile_url", "")

    try:
        data["mythic_plus_scores_by_season"][0]["scores"].get("all", -1)
    except (IndexError, KeyError):
        info["score"] = -1

    info["guild"] = info.get("guild") or {}  # ensure guild-dict is there

    return info


###################################
# Embeds
#


def build_char_embed(rio_info):
    embed = discord.Embed()
    embed.color = wow_constants.CLASS_COLOR.get(rio_info.get("class")) or embed.Empty

    embed.title = f"**{rio_info['name']}**"
    guild_name = rio_info.get("guild", {}).get("name", "")
    if guild_name:
        embed.title += f" <{guild_name}>"

    embed.url = rio_info.get("url")
    embed.description = ""
    embed.description += f"\n{rio_info['race']} **{rio_info['active_spec_name']} {rio_info['class']}**"
    embed.description += f"\n{rio_info['realm']}"
    embed.set_thumbnail(url=rio_info.get("thumbnail_url"))

    return embed


def build_rio_embed(rio_info):

    if not rio_info.get("name"):
        return

    embed = build_char_embed(rio_info)
    try:
        scores = rio_info["mythic_plus_scores_by_season"][0]["scores"]
    except (IndexError, KeyError):
        scores = {}

    for spec in wow_constants.ROLES:
        spec_score = scores.get(spec.lower(), 0)
        spec_emote = emotes.get(spec)
        embed.add_field(name=f"{spec}:", value=f"{spec_emote} {spec_score:.0f}")

    return embed


