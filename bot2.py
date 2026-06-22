import discord
import random
from discord.ext import commands

from bot_logic import gen_pass

from bot_logic import caraoucoroa

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
async def melhorjogo(ctx):
    await ctx.send("hollow knight")

@bot.command()
async def gerarsenha(ctx , tamanho = 10):
    senha = gen_pass(tamanho)
    await ctx.send(f"Senha gerada: {senha}")

@bot.command()
async def caraoucoroa(ctx):
    await ctx.send(caraoucoroa())   

@bot.command()
async def pedrapapeltesoura(ctx , player):
    comp = random.randint(1,3)
    
    if comp == 1:
        comp = "pedra"
    if comp == 2:
        comp = "tesoura"
    if comp == 3:
        comp = "papel"
    
    if (player == "pedra" and comp == "tesoura") or (player == "tesoura" and comp == "papel") or (player == "papel" and comp == "pedra") :
        await ctx.send(f"{comp} - O jogador ganhou!")
            
    elif player == comp :
        await ctx.send(f"{comp} - Empate!")
    
    else:
        await ctx.send(f"{comp} - O computador ganhou!")

@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

bot.run("COLOQUE SEU TOKEN AQUI")
