# -*- coding: utf-8 -*-

# IMPORT STANDARD LIBRARIES
from collections import Counter
import typing

# IMPORT THIRD PARTY LIBRARIES
from discord.ext import commands
import discord

# IMPORT LOCAL LIBRARIES
from arrgbot import emotes



STATUS_ICONS = {
    discord.Status.online: "🟢",
    discord.Status.idle: "🟠",
    discord.Status.do_not_disturb: "🔴",
    discord.Status.offline: "⚫",
}
STATUS_LIST = list(STATUS_ICONS.keys())


def user_has_roles(user, roles):
    return all(role in user.roles for role in roles)


class UsersCog(commands.Cog):
    """"""
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def raw_msg(self, ctx, channel: typing.Optional[discord.TextChannel], message_id: int):
        """Print the raw content of a message."""
        channel = channel or ctx.channel
        message = await channel.fetch_message(message_id)
        await ctx.send(f"```{message.content}```")

    @commands.command()
    async def no_roles(self, ctx, limit=32):
        """List all Members without any roles."""
        # check for `len == 1` because @everyone is always in the list
        members = [member for member in ctx.guild.members if len(member.roles) == 1]

        text = f"found {len(members)} members without any roles."
        text += f" _(first {limit} members)_" if len(members) > limit else ""
        text += "\n"

        text += "\n".join([member.mention for member in members[:limit]])
        await ctx.channel.send(text)

    @commands.command(aliases=["role"])
    async def roles(self, ctx, *, names: str):
        """Lists a users based on a combination of roles.

        Note:
            If there are less than 10, it prints the user-names
            otherwise just the total count.

        Example:
            List everyone with "Tinker"

            >>> !rcu roles Tinker
            3 users have the role(s) "Tinker"
            Arrg
            Brrg
            Crrg

            List everyone with "Cloth", "Healer" and "High M+"

            >>> !rcu roles "Cloth,Healer,High M+ Booster"
            42 users have the role(s) "Cloth, Healer, High M+ Booster"

        """
        max_names = 32

        if not names:
            return await ctx.send_help(self.roles)

        list_users = names.startswith("list ")
        if list_users:
            names = names[5:]

        roles = [role for role in ctx.guild.roles if role.name.lower() in names.lower()]

        if not roles:
            embed = discord.Embed()
            embed.color = discord.Color.red()
            embed.description = f"{emotes.PEEPOSHRUG} no role like this found.\nRemember to add `\"` around names with spaces in it."
            return await ctx.channel.send(embed=embed)

        users = ctx.guild.members
        users = [user for user in users if not user.bot]
        users = [user for user in users if user_has_roles(user, roles)]
        users_count = len(users)

        embed = discord.Embed()
        embed.color = roles[0].color
        embed.description = f"Found **{users_count} users** with the role(s):\n"
        embed.description += " ".join([role.mention for role in roles])

        def user_status_line(user):
            status_icon = "\\" + STATUS_ICONS.get(user.status)  # add "\\" for the raw emotes
            stauts_name = str(user.status).title()
            return f"{status_icon} {stauts_name}"

        try:
            users = sorted(users, key=lambda user: (STATUS_LIST.index(user.status), user.display_name))
        except ValueError:  # in case someone has a status thats not in status_list
            pass

        by_status = "‎‎‎‎‏‏‎‏‏‎   ".join(f"{icon} {count}" for icon, count in Counter(STATUS_ICONS.get(user.status, "") for user in users).items())
        embed.set_footer(text=by_status)

        if list_users:
            users = users[:max_names]
            status = "\n".join(user_status_line(user) for user in users)
            names = "\n".join(user.mention for user in users)
            embed.add_field(name="status", value=status)
            embed.add_field(name="users", value=names)

        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(UsersCog(bot))
