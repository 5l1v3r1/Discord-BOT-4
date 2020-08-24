import discord
from discord.ext import commands
import time

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

    @commands.command()
    async def clean(self, message, value:int):
        min = 0
        max = 100

        if(message.author.guild_permissions.administrator):
            if(value > min and value <= max):
                channel = message.channel
                messages = await channel.history(limit = value).flatten()

                sendMessage = await message.send("{} messages were found".format(value))
                time.sleep(1)

                await sendMessage.edit(content="{} messages are being deleted!".format(value))
                time.sleep(0.5)

                await channel.delete_messages(messages)
                sendMessage.edit(content=":white_check_mark: {} messages were deleted! :white_check_mark:".format(value))
                time.sleep(1)

                lastMessage = channel.history(limit=1).flatten()
                await channel.delete_messages(lastMessage)

            else:
                await message.send(":x: Message amount should be between {} and {}!".format(min, max))
        else:
            await message.send(":x: What da Fuq you tryin' to do biach? :x:")


def setup(bot):
    bot.add_cog(adminCommand(bot))