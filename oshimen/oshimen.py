import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
import os

PATH = 'data/oshimen/'
OJSON = PATH + 'oshimen.json'


class Oshimen:
    """Oshimen Card"""

    def __init__(self, bot):
        self.bot = bot
        self.oshi = dataIO.load_json(OJSON)

    @commands.command(name="wota", pass_context=True,
                      invoke_without_command=True, no_pm=True)
    async def _wota(self, ctx):
        """Joins the wota and embrace 48G grace!"""

        server = ctx.message.server
        user = ctx.message.author

        if server.id not in self.oshi:
            self.oshi[server.id] = {}
        else:
            pass

        if user.id not in self.oshi[server.id]:
            self.oshi[server.id][user.id] = {}
            dataIO.save_json(OJSON, self.oshi)
            data = discord.Embed(colour=discord.Color(0xffb6c1))
            data.add_field(
                name="Ohayou! :tada:",
                value=("Your Oshimen card is") +
                ("succesfully generated, {}.").format(user) +
                ("Use {}write to start adding").format(ctx.prefix) +
                ("your Oshimen on the card"))
            await self.bot.say(embed=data)
        else:
            data = discord.Embed(colour=discord.Color(0xffb6c1))
            data.add_field(
                name="Ara~!",
                value=("Yuihan said you already have")
                ("an Oshimen card, {}.").format(user) +
                ("Use {}write to add Oshimen").format(ctx.prefix) +
                ("onto your card"))
            await self.bot.say(embed=data)

    @commands.command(name="oshimen", pass_context=True,
                      invoke_without_command=True, no_pm=True)
    async def _oshimen(self, ctx, user: discord.Member=None):
        """View Oshimen Card"""

        server = ctx.message.server

        if server.id not in self.oshi:
            self.oshi[server.id] = {}
        else:
            pass

        if not user:
            user = ctx.message.author
            if user.id in self.oshi[server.id]:
                data = discord.Embed(
                    description=("**{}'s Oshimen Card").format(user) +
                    (" on {}**").format(server),
                    colour=discord.Color(0xffb6c1))
                if "Oshimen" in self.oshi[server.id][user.id]:
                    oshimen = self.oshi[server.id][user.id]["Oshimen"]
                    data.add_field(name="Oshimen:", value=oshimen)
                else:
                    pass
                if "Support Type" in self.oshi[server.id][user.id]:
                    support_type = self.oshi[server.id][
                        user.id]["Support Type"]
                    data.add_field(name="Support type:", value=support_type)
                else:
                    pass

                await self.bot.say(embed=data)
            else:
                prefix = ctx.prefix
                data = discord.Embed(colour=discord.Color(0xffb6c1))
                data.add_field(
                    name="Gomen ne~!",
                    value=("You'll need to apply for an Oshimen card to use") +
                    ("this feature. Type {}wota to apply for").format(prefix) +
                    (" one."))
                await self.bot.say(embed=data)
        else:
            server = ctx.message.server
            if user.id in self.oshi[server.id]:
                data = discord.Embed(
                    description=("**{}'s Oshimen Card").format(user) +
                    (" on {}**").format(server),
                    colour=discord.Color(0xffb6c1))
                if "Oshimen" in self.oshi[server.id][user.id]:
                    oshimen = self.oshi[server.id][user.id]["Oshimen"]
                    data.add_field(name="Oshimen:", value=oshimen)
                else:
                    pass
                if "Support Type" in self.oshi[server.id][user.id]:
                    support_type = self.oshi[server.id][
                        user.id]["Support Type"]
                    data.add_field(name="Support type:", value=support_type)
                else:
                    pass

                await self.bot.say(embed=data)
            else:
                prefix = ctx.prefix
                data = discord.Embed(colour=discord.Color(0xffb6c1))
                data.add_field(name="Buuu~!",
                               value=("Looks like {}").format(user) +
                               ("haven't apply for a card. Tell that poor ") +
                               ("soul to apply using {}wota").format(prefix))
                await self.bot.say(embed=data)

    @commands.group(name="write", pass_context=True,
                    invoke_without_command=True, no_pm=True)
    async def write(self, ctx):
        """Writes on your Oshimen card"""
        await self.bot.send_cmd_help(ctx)

    @write.command(pass_context=True, no_pm=True)
    async def oshimen(self, ctx, *, oshimen):
        """Who is your oshi?
        Please write the full name with the format of Familyname Givenname
        e.g. [p]write oshimen Kashiwagi Yuki

        [p] = prefix"""

        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in self.oshi:
            self.oshi[server.id] = {}
        else:
            pass

        if user.id not in self.oshi[server.id]:
            data = discord.Embed(colour=discord.Color(0xffb6c1))
            data.add_field(
                name="Gomen ne~!",
                value=("You'll need to apply for an Oshimen card to use") +
                ("this feature. Type {}wota").format(prefix) +
                (" to apply for one."))
            await self.bot.say(embed=data)
        else:
            self.oshi[server.id][user.id].update({"Oshimen": oshimen})
            dataIO.save_json(OJSON, self.oshi)
            data = discord.Embed(colour=discord.Color(0xffb6c1))
            data.add_field(name="Yatta! :sparkling_heart:",
                           value=("I am sure {} is very ").format(oshimen) +
                           ("thankful for your support"))
            await self.bot.say(embed=data)

    @write.command(pass_context=True, no_pm=True)
    async def supporttype(self, ctx, *, support_type):
        """How devoted are you?
        Support types are : Kami-Oshi, Oshi, DD or Daredemo Daisuki,
         MD or Minna Daisuki or write anything you like"""

        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in self.oshi:
            self.oshi[server.id] = {}
        else:
            pass

        if user.id not in self.oshi[server.id]:
            data = discord.Embed(colour=discord.Color(0xffb6c1))
            data.add_field(
                name="Gomen ne~!",
                value=("You'll need to apply for an Oshimen card to use") +
                ("this feature. Type {}wota").format(prefix) +
                (" to apply for one."))
            await self.bot.say(embed=data)
        else:
            self.oshi[server.id][user.id].update(
                {"Support Type": support_type})
            dataIO.save_json(OJSON, self.oshi)
            data = discord.Embed(colour=discord.Color(0xffb6c1))
            data.add_field(name="Arigatou! :bow:",
                           value=("We are very grateful of your support. ") +
                           ("The support type {} ").format(support_type) +
                           ("has been saved"))
            await self.bot.say(embed=data)


def check_folder():
    if not os.path.exists(PATH):
        print("Creating data/oshimen folder...")
        os.makedirs(PATH)


def check_file():
    if not dataIO.is_valid_json(OJSON):
        print("Creating empty json file")
        dataIO.save_json(OJSON)


def setup(bot):
    check_folder()
    check_file()
    bot.add_cog(Oshimen(bot))
