from doctest import debug_script
import discord
from discord import app_commands
from discord.ext import commands
from utils.config_loader import Config

config = Config()
GUILD_ID = config.load_value('GUILD_ID')

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command( # command name and description
        name = "sum",
        description= "sum of two numbers"
        )
    @app_commands.describe( # parameter descriptions
        num1= "first number",
        num2= "second number" 
        )
    async def sum(
        self,
        interaction: discord.Interaction,
        num1:int,
        num2:int ) -> None:
        await interaction.response.send_message(f"The sum of {num1} and {num2} is {num1+num2}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Test(bot),
        guilds = [discord.Object(id = GUILD_ID)]
    )