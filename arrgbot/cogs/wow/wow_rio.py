# IMPORT STANDARD LIBRARIES
from aiohttp import ClientSession


################################################################################
# API Helpers
#
RAIDER_IO_API = "https://raider.io/api/v1"

async def fetch_data(url, **params):
    async with ClientSession() as session:
        async with session.get(url=url, params=params) as resp:
            return await resp.json()


################################################################################
# Commands
#

async def get_cutoff(season="season-sl-4", region="eu", faction="all"):
    """Returns the Score Cutoff for the 0.1% Title."""
    url = "https://raider.io/api/v1/mythic-plus/season-cutoffs"
    data = await fetch_data(url, region=region, season=season)
    data = data or {}
    data = data.get("cutoffs", {}).get("p999", {})
    data = data.get(faction, {}).get("quantileMinValue", 0)
    return data
