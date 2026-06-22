import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")


@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

bot.run("COLOQUE SEU TOKEN AQUI")
