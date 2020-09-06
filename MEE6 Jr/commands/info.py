import discord
from discord.ext import commands

class infocommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_version = bot.bot_version
        self.bot_name = bot.bot_name
        self.author = bot.author
        self.icon_url = bot.icon_url
        self.getDeviceOs = bot.getDeviceOs

    @commands.command()
    async def info(self, message):
        embed = discord.Embed(color=0xff0000)
        embed.set_author(name="Boomer", url="https://github.com/woosal1337", icon_url="https://i.imgur.com/SxH7Ctg.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/SxH7Ctg.jpg")
        embed.add_field(name="Boomer", value="A BOT who is a Boomer AF", inline=True)
        embed.add_field(name="Github", value="[@woosal1337](https://github.com/woosal1337)", inline=True)
        embed.add_field(name="Instagram", value="[@woosal1337](https://www.instagram.com/woosal1337/)", inline=True)
        embed.add_field(name="Twitter", value="[@woosal1337](https://twitter.com/woosal1337)", inline=True)
        embed.add_field(name="Reddit", value="[@woosal1337](https://www.reddit.com/user/woosal1337)", inline=True)
        embed.add_field(name="Telegram", value="[@woosal1337](https://t.me/woosal1337)", inline=True)
        embed.add_field(name="Author", value=self.author, inline=True)
        embed.add_field(name="Website", value="[woosal1337.me](http://woosal1337.me)", inline=True)
        embed.set_footer(icon_url=self.icon_url, text="A real Boomer BOT")
        await message.send(embed=embed)


def setup(bot):
    bot.add_cog(infocommands(bot))
