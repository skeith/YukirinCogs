import discord
from discord.ext import commands
from __main__ import send_cmd_help
from cogs.utils.chat_formatting import *
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils import chat_formatting
from random import randint
from random import choice as randchoice
import datetime
import time
import aiohttp
import asyncio
import inspect
import subprocess
import sys


class Pinger:
    """Pinger commands."""

    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.group(name="tool", pass_context=True, invoke_without_command=True)
    async def group_cmd(self, ctx):
        """Set of command used by Yukirin"""
        await send_cmd_help(ctx)

    @checks.is_owner()
    @group_cmd.command(hidden=True)
    async def ping(self):
        """Reply here"""
        await self.bot.say("What?")

    @checks.is_owner()
    @group_cmd.command(hidden=True, pass_context=True)
    async def pingt(self,ctx):
        """pseudo-ping time"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        await self.bot.say("{}ms \n\n¯\_(ツ)_/¯".format(round((t2-t1)*1000)))

    @checks.is_owner()
    @group_cmd.command(pass_context=True)
    async def purge(self, ctx):
        """Deletes the past ~100 mesages"""
        messages = []
        async for message in self.bot.logs_from(ctx.message.channel, limit=100):
            messages.append(message)
        for message in messages:
            if message.author.id == self.bot.user.id:
                await self.bot.delete_message(message)

    @group_cmd.command()
    async def fox(self):
        """Your Description"""
        search = "http://wohlsoft.ru/images/foxybot/randomfox.php"
        try:
            async with aiohttp.get(search) as r:
                result = await r.json()
            await self.bot.say(result['file'])
        except:
            await self.bot.say("Couldnt Get An Image")


def setup(bot):
    n = Pinger(bot)
    bot.add_cog(n)
