
# IMPORT STANDARD LIBRARIES
import aiohttp

# IMPORT THIRD PARTY LIBRARIES
import arrow
import discord
from discord.ext import commands


DADJOKE_URL = "https://icanhazdadjoke.com/"

class JokesCog(commands.Cog):
    """docstring for DebugCog"""
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    def _dadjoke_embed(self, data):
        embed = discord.Embed()
        embed.title = data.get("joke")
        embed.color = discord.Color.dark_blue()
        embed.set_footer(text=f"🆔 {data.get('id')}")
        return embed

    @commands.group(aliases=["dj"])
    async def dadjoke(self, ctx):
        """Gives you a random dadjoke."""
        if ctx.invoked_subcommand:
            return

        url = DADJOKE_URL

        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        async with aiohttp.ClientSession(loop=self.bot.loop) as session:
            async with session.get(url, headers=headers) as resp:
                data = await resp.json()

        if data.get("status") != 200:
            return await ctx.send("something went wrong... :/")

        # send
        embed = self._dadjoke_embed(data)
        return await ctx.send(embed=embed)

    @dadjoke.command(name="id")
    async def dadjoke_id(self, ctx, joke_id):

        url = f"{DADJOKE_URL}/j/{joke_id}"

        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        async with aiohttp.ClientSession(loop=self.bot.loop) as session:
            async with session.get(url, headers=headers) as resp:
                data = await resp.json()

        # send
        embed = self._dadjoke_embed(data)
        return await ctx.send(embed=embed)

    @dadjoke.command(name="find", aliases=["f", "search", "s"])
    async def dadjoke_find(self, ctx, search_term=""):

        url = f"{DADJOKE_URL}/search"

        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        params = {"term": search_term, "limit": 1}
        async with aiohttp.ClientSession(loop=self.bot.loop) as session:
            async with session.get(url, headers=headers, params=params) as resp:
                data = await resp.json()

        matches = data.get("total_jokes", 0)
        if not matches:
            return await ctx.send("Nothing found.. :(")

        data = data.get("results", [])[0]

        # send
        embed = self._dadjoke_embed(data)
        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(JokesCog(bot))