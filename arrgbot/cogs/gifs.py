# -*- coding: utf-8 -*-

# IMPORT STANDARD LIBRARIES
import asyncio
import io
import os
import requests

# IMPORT THIRD PARTY LIBRARIES
from discord.ext import commands
from PIL import Image
import discord

# IMPORT LOCAL LIBRARIES
from arrgbot.utils import async_utils


DIR = os.path.dirname(__file__) + "/gifs_imgs/"


@async_utils.run_in_executor
def make_bonk_gif(avatar_url):
    # Get Avatar
    response = requests.get(avatar_url)
    avatar = Image.open(io.BytesIO(response.content))
    # avatar = avatar.convert("RGB")  # to make sure we have RGBA (eg.: when input is RGB only)
    avatar = avatar.resize((55, 55))

    HEIGHTS = [
        1.0, 0.7, 0.6, 0.8, 1.0,   # 0-4
        1.0, 0.8, 0.8, 1.1, 1.0,   # 5-9
        0.7, 0.7, 1.0, 0.9, 0.7,   # 10-14
        0.6, 1.0, 1.0, 0.6, 0.7,   # 15-19
        1.0, 1.0, 0.8, 0.7, 1.0,   # 20-24
    ]

    # Base Image
    img = Image.new(mode="RGBA", size=(100, 100), color=(54, 57, 63, 0))

    frames = []
    for i in range(25):
        frame = img.copy()

        # Avatar
        h = int(55 * HEIGHTS[i])
        avatar_f = avatar.copy().resize((55, h))

        y = 55 - h  # diff to full scale (0 if scale = 1.0)
        pos = (42, 44+y)

        mask = avatar_f if avatar_f.mode == "RGBA" else None
        frame.paste(avatar_f, pos, mask=mask)

        # newspaper
        overlay = Image.open(f"{DIR}/bonk.{i}.png")
        overlay = overlay.resize((100, 100))
        frame.paste(overlay, mask=overlay)

        # add to list
        frames.append(frame)

    image_binary = io.BytesIO()
    frames[0].save(
        image_binary,
        format="GIF",
        append_images=frames[1:],
        save_all=True,
        duration=25,
        loop=0,
        transparency=0,
        disposal=2
    )
    image_binary.seek(0)
    return image_binary


@async_utils.run_in_executor
def make_pet_gif(avatar_url):
    # Get Avatar
    response = requests.get(avatar_url)
    avatar = Image.open(io.BytesIO(response.content))
    avatar = avatar.resize((55, 55))

    HEIGHTS = [
        1.1, 1.1, 1.0, 1.0, 1.0,   # 0-4
        1.0, 0.9, 0.9, 1.0, 1.0,   # 5-9
    ]
    WIDTHS = [
        1.0, 1.0, 1.1, 1.1, 1.2,   # 0-4
        1.2, 1.2, 1.2, 1.1, 1.1,   # 5-9
    ]
    AVATAR_SIZE = 45

    # Base Image
    img = Image.new(mode="RGBA", size=(66, 66), color=(54, 57, 63, 0))

    frames = []
    for i in range(10):
        frame = img.copy()

        # Avatar
        h = int(AVATAR_SIZE * HEIGHTS[i])
        w = int(AVATAR_SIZE * WIDTHS[i])
        avatar_f = avatar.copy().resize((w, h))

        x = int(16 + (AVATAR_SIZE - w) / 2.0)
        y = int(22 + (AVATAR_SIZE - h))  # diff to full scale (0 if scale = 1.0)
        pos = (x, y)

        mask = avatar_f if avatar_f.mode == "RGBA" else None
        frame.paste(avatar_f, pos, mask=mask)

        # newspaper
        overlay = Image.open(f"{DIR}/pet.{i}.png")
        overlay = overlay.resize((66, 66))
        frame.paste(overlay, mask=overlay)

        # add to list
        frames.append(frame)

    image_binary = io.BytesIO()
    frames[0].save(
        image_binary,
        format="GIF",
        append_images=frames[1:],
        save_all=True,
        duration=25,
        loop=0,
        transparency=0,
        disposal=2
    )
    image_binary.seek(0)
    return image_binary


class GifsCog(commands.Cog):
    """docstring for DebugCog"""
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandOnCooldown):
            return await ctx.send(f"The command is on cooldown. Try again in {error.retry_after:0.0f}s.")

        raise error

    @commands.cooldown(rate=2, per=60, type=commands.BucketType.user)  # 5x per minute per user
    @commands.command()
    async def bonk(self, ctx, user: discord.Member):

        embed = discord.Embed()
        embed.description = f"preparing to bonk {user.display_name}."
        embed.color = discord.Color.blue()
        message = await ctx.send(embed=embed)


        # Get Avatar
        avatar_url = user.avatar_url_as(format="png", size=64)
        if not avatar_url:
            return await ctx.send("user has no profile picture.. Immune to !bonk.")

        # make gif
        bonk_gif = await make_bonk_gif(avatar_url)
        bonk_gif = discord.File(fp=bonk_gif, filename=f"Bonk.gif")

        # send
        await ctx.send(file=bonk_gif)
        await message.delete()

    @commands.cooldown(rate=2, per=60, type=commands.BucketType.user)  # 5x per minute per user
    @commands.command()
    async def pet(self, ctx, user: discord.Member):

        embed = discord.Embed()
        embed.description = f"preparing to pet {user.display_name}."
        embed.color = discord.Color.blue()
        message = await ctx.send(embed=embed)

        # Get Avatar
        avatar_url = user.avatar_url_as(format="png", size=64)
        if not avatar_url:
            return await ctx.send("user has no profile picture.. Immune to !pet.")

        # make gif
        pet_gif = await make_pet_gif(avatar_url)
        pet_gif = discord.File(fp=pet_gif, filename=f"Pet.gif")

        # send
        await ctx.send(file=pet_gif)
        await message.delete()

def setup(bot):
    bot.add_cog(GifsCog(bot))
