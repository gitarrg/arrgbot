# -*- coding: utf-8 -*-

# IMPORT STANDARD LIBRARIES
import re
import os
from aiohttp import ClientSession

# IMPORT THIRD PARTY LIBRARIES
import stringcase
from arrgbot.utils import raider_io


WCL_API = "https://www.warcraftlogs.com/api/v2/client"
WCL_CLIENT_ID = os.getenv("WCL_CLIENT_ID")
WCL_CLIENT_SECRET = os.getenv("WCL_CLIENT_SECRET")
HEADERS = {"Authorization": None}


async def update_auth_token():
    """Request a new Auth Token from Warcraftlogs."""

    url = "https://www.warcraftlogs.com/oauth/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": WCL_CLIENT_ID,
        "client_secret": WCL_CLIENT_SECRET
    }
    async with ClientSession() as session:
        async with session.post(url=url, data=data) as resp:
            data = await resp.json()

    token = data.get("access_token", "")

    # a bit of dirty stuff here.. but w/e
    global HEADERS
    HEADERS["Authorization"] = "Bearer " + token


async def get_user_parses(char_id_or_name):

    match = re.search(r"((?P<name>.+)\-(?P<realm>.+))|(?P<id>\d+)", char_id_or_name)
    if not match:
        return

    values = match.groupdict()

    if values.get("id"):
        search = f"id: {values['id']}"
    elif values.get("name"):

        realm = values.get("realm") or ""
        realm = realm.replace("'", "")
        realm = stringcase.spinalcase(realm)
        realm = realm[1:] if realm.startswith("_") else realm

        search = f"serverRegion: \"eu\" serverSlug: \"{realm}\" name: \"{values['name']}\""
    else:
        return

    # format the query
    query = f"""
    {{
        characterData {{
            character({search}) {{
                classID
                name
                id
                server {{
                    name
                    normalizedName
                }}

                heroic: zoneRankings(difficulty: 4)
                mythic: zoneRankings(difficulty: 5)
            }}
        }}
    }}
    """
    if not HEADERS.get("Authorization"):
        await update_auth_token()

    async with ClientSession() as session:
        async with session.get(url=WCL_API, json={"query": query}, headers=HEADERS) as resp:
            return await resp.json()


async def build_wcl_embed(char_id_or_name):

    TIER_NAME = "sanctum-of-domination"

    data = await get_user_parses(char_id_or_name)
    if not data:
        return
    data = data.get("data", {})

    character = data["characterData"]["character"]
    if not character:
        return
    parses = character["heroic"]
    rankings = parses["rankings"]

    name = character.get("name")
    realm = character.get("server", {}).get("name")

    rio_info = await raider_io.get_booster_rio(name, realm)
    embed = raider_io.build_char_embed(rio_info)
    embed.url = f"https://www.warcraftlogs.com/character/id/{character['id']}#difficulty=4"

    progress = rio_info.get("raid_progression", {}).get(TIER_NAME, {}).get("summary", "-")
    total_kills = sum(boss.get("totalKills", 0) for boss in rankings)
    best_avg = parses.get("bestPerformanceAverage") or 0
    embed.add_field(name=f"Progress:", value=progress)
    embed.add_field(name=f"HC Kills:", value=total_kills)
    embed.add_field(name=f"Best Perf. Avg:", value=f"📈 {best_avg:.2f}%")

    return embed
