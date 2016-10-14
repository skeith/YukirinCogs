import discord
from discord.ext import commands
from cogs.utils.chat_formatting import *
from random import randint
from random import choice as randchoice
import datetime
import time
import aiohttp
import asyncio
from __main__ import send_cmd_help

class Pinger:
    """Pinger commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="tool", pass_context=True, invoke_without_command=True)
    async def group_cmd(self, ctx):
        """Grouped command to avoid conflict"""
        await send_cmd_help(ctx)

    @group_cmd.command(hidden=True)
    async def ping(self):
        """Reply here"""
        await self.bot.say("What?")

    @group_cmd.command(hidden=True)
    async def pingt(self,ctx):
        """pseudo-ping time"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        await self.bot.say("{}ms \n¯\_(ツ)_/¯".format(round((t2-t1)*1000)))        


def setup(bot):
    n = Pinger(bot)
    bot.add_cog(n)
