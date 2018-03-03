import discord
from discord.ext import commands
from __main__ import send_cmd_help


class Animal:
    """Animal commands."""

    def __init__(self, bot):
        self.bot = bot
        self.session = self.bot.http.session

    @commands.command()
    async def cats(self):
        """Shows a cat"""
        search = "http://random.cat/meow"
        try:
            async with self.session.get(search) as r:
                result = await r.json()
            await self.bot.say(result['file'])
        except:
            await self.bot.say("Couldnt Get An Image")

    @commands.command()
    async def catsbomb(self, amount : int = 5):
        """Throws a cat bomb!

        Defaults to 5"""
        search = "http://random.cat/meow"
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(search) as r:
                    api_result = await r.json()
                    results.append(api_result['file'])
            await self.bot.say("\n".join(results)) # \o/ Thanks irdumb <3
        except:
            await self.bot.say("Couldnt Get An Image")

    @commands.command()
    async def pugs(self):
        """Shows a pug"""
        search = "http://pugme.herokuapp.com/random"
        try:
            async with self.session.get(search) as r:
                result = await r.json()
            await self.bot.say(result['pug'])
        except:
            await self.bot.say("Could Not Get An Image")

    @commands.command()
    async def pugsbomb(self, amount : int = 5):
        """Throws a pugs bomb!

        Defaults to 5"""
        search = "http://pugme.herokuapp.com/random"
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(search) as r:
                    api_result = await r.json()
                    results.append(api_result['pug'])
            await self.bot.say("\n".join(results)) # \o/ Thanks irdumb <3
        except:
            await self.bot.say("Couldnt Get An Image")

def setup(bot):
    n = Animal(bot)
    bot.add_cog(n)
