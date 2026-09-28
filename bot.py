import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ON: {bot.user}")
    await bot.tree.sync()

@bot.tree.command(name="loja", description="Ver loja")
async def loja(interaction: discord.Interaction):
    embed = discord.Embed(title="LOJA VIP", description="**1 DIA R$18**\n**7 DIAS R$55**\n**15 DIAS R$82**\n**30 DIAS R$102**", color=0x9b59b6)
    await interaction.response.send_message(embed=embed)

bot.run(os.getenv("TOKEN"))
