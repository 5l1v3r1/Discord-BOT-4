import discord
from discord.ext import commands
import platform

token = "NzQ2ODU2MzU4OTUwODYyODQ4.X0GaLw.Yp_PirBQKD_K1Qlm4Ypp05EnaSE"


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="boomer!", pm_help=None, description="A real Boomer")
        self.bot_version = "1.0.0"
        self.bot_name = "Boomer"
        self.author = "woosal#1337"
        self.icon_url = "https://i.imgur.com/SxH7Ctg.jpg"
        self.getDeviceOs = platform.system()

        self.load_extension("commands.info")
        self.load_extension("commands.admin")
        self.load_extension("commands.seviliyorsun")

    async def on_ready(self):
        print("Boomer is wakin up...")
        print("{} has woken up!".format(self.user.name))
        print("Boomer's ID: {}".format(self.user.id))
        #print("Boomer is active on " + str(len(set(self.servers()))) + " servers!")
        print("Boomer is accessing to " + str(len(set(self.get_all_members())) - 1) + " other boomers!")

    async def on_command_error(self, context, exception):
        if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
            await context.send("Use `boomer!help` to see the real boomer commands you dumbass!")


bot = Bot()
bot.run(token)