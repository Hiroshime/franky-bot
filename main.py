# FrankyBot.py
import os
import random
import urllib
import urllib.request
import discord
import json
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import CommandNotFound

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN2 = os.getenv('CLIMA_TOKEN')
client = discord.Client()

def get_city_weather(city):
    url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/"+str(city)+"/days/15?token="+TOKEN2
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0')
    response = urllib.request.urlopen(req)
    data = response.read()
    values = json.loads(data)
    return format_city_weather(values)

def format_city_weather(retorno):
   clima = retorno["data"]
   final = "Cidade: "+retorno["name"]+"\n"

   for item in clima:
    final += "\n"
    final += "Data: "
    final += item["date"]
    final += "\nPrevisao: "
    final += item["text_icon"]["text"]["pt"]
    final += "\nTemperatura Max: : "
    final += str(item["temperature"]["max"])
    final += "\nTemperatura Min:: "
    final += str(item["temperature"]["min"])
    final += "\n\n\n"
   return final

@client.event
async def on_ready():
    print(f'{client.user.name} Conectado ao discord!')

@client.event
async def on_member_join(member):
    await client.get_channel('876544266254561370').send(f"Bem vindo ao {member.guild.name} {member.mention} .")
    await member.add_roles(*(member.guild.get_role(id_) for id_ in (693615866612547645)))
 #   await member.create_dm()
 #   await member.dm_channel.send(
 #       f'Ola {member.name}, bem vindo ao XorumisHouse !'
 #  )

bot = commands.Bot(command_prefix='!')

@bot.command(name='salve', help='Responde seu salve')
async def salve(ctx):
        await ctx.send('SALVE. Eu sou o FraaaaankyBot a seu dispor.')

@bot.command(name='funcao', help='Nao faz literalmente nada')
async def funcaovazia(ctx):
        await ctx.send('Eu não tenho funcao nenhuma, culpa do Hiroshime que me fez assim!')

@bot.command(name='teste', help='Nao faz literalmente nada')
async def funcaoteste(ctx):
        await ctx.send('Seu teste rolou')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('Este comando ainda não esta disponivel.')
 

#@client.event
#async def on_message(message):
##    if message.author == client.user:
#        return
#    if message.content == '!ola':
#        await message.channel.send('Ola eu sou o FraaaankyBot a seu dispor!')#
#
#    if message.content == '!funcao':
#        await message.channel.send('Eu não tenho funcao nenhuma, culpa do Hiroshime que me fez assim!')
#    if message.content == '!clima':
#        await message.channel.send(get_city_weather(4008))

bot.run(TOKEN)
