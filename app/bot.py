from email.mime import application
import discord
from discord.ext import commands
from utils.config_loader import Config

config = Config()
TOKEN = config.load_value('BOT_TOKEN')
PREFIX = config.load_value('BOT_PREFIX')
APP_ID = config.load_value('APP_ID')
GUILD_ID = config.load_value('GUILD_ID')

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            intents = discord.Intents.all(),
            application_id = APP_ID )

    async def setup_hook(self):
        await self.load_extension("cogs.test")
        await bot.tree.sync(guild = discord.Object(id = GUILD_ID))
    
    async def on_ready(self):
        print(f"{self.user} has been connected to Discord!")

bot=Bot()
bot.run(TOKEN)