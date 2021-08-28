"""Main entry point to run the bot."""

# IMPORT STANDARD LIBRARIES
import os
import sys
import traceback

# IMPORT THIRD PARTY LIBRARIES
import discord
from discord.ext import commands

# IMPORT LOCAL LIBRARIES
from arrgbot import cogs # import debug


BOT_TOKEN = os.getenv("BOT_TOKEN")


COMMAND_PREFIX = ("!rcu ", "!")


intents = discord.Intents.all()
intents.bans = False
intents.integrations = False
intents.webhooks = False
intents.invites = False
intents.typing = False


EXTENSIONS = [
    "cogs.debug",
    "cogs.gifs",
    "cogs.users",
    "cogs.game_wow",
    "cogs.game_among_us",
    "cogs.jokes",
]


class ArrgBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(
            command_prefix=COMMAND_PREFIX,
            case_insensitive=True,
            intents=intents,
            *args, **kwargs
        )
        print("[ArrgBot] init")

        for extension in EXTENSIONS:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()


    async def on_ready(self):
        print("ArrgBot ready!")


def main():

    bot = ArrgBot()
    bot.run(BOT_TOKEN)


if __name__ == '__main__':
    main()


