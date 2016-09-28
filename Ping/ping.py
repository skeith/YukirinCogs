import discord
from discord.ext import commands
from cogs.utils.chat_formatting import *
from random import randint
from random import choice as randchoice
import datetime
import time
import aiohttp
import asyncio

class Pinger:
    """Pinger commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def ping(self):
        """Pong."""
        await self.bot.say("What?")


def setup(bot):
    n = Pinger(bot)
    bot.add_cog(n)