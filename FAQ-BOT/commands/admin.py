import discord
from discord.ext import commands

class adminCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def refresh(self, message, value:str):
        source = "commands."

        try:
            if(message.author.guild_permissions.administrator):
                self.bot.unload_extension(source + value)
                self.bot.load_extension(source + value)
                await message.send(value + " file has been refreshed!")
            else:
                await message.send("You do not have access to use this command!")

        except ImportError as e:
            print(e)

def setup(bot):
    bot.add_cog(adminCommand(bot))