import discord
from discord.ext import commands

class seviliyorsuncommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version
        self.bot_name = bot.bot_name
        self.author = bot.author
        self.icon_url = bot.icon_url
        self.getDeviceOs = bot.getDeviceOs

    @commands.command()
    async def seviliyorsun(self, message):
        await message.send("Sen de Boomer, sen de <3 !")


def setup(bot):
    bot.add_cog(seviliyorsuncommands(bot))
