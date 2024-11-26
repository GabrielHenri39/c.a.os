import discord
from discord import app_commands
import random
from configparser import ConfigParser

confing = ConfigParser()
confing.read('config.ini')
token = confing.get('DISCORD', 'token')


class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"Logged in as {self.user}.")

   
     

bot = MyBot()
tree = app_commands.CommandTree(bot)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    d1 = list()

    

    comando:str = message.content
    #dado
    if '$' in comando:
        quantidade, faces = map(int, message.content.split('$'))
        if comando == f'{quantidade}${faces}':
            try:
                
                    for nq in range(1,quantidade+1):
                            nq = random.randint(1,faces)
                            d1.append(nq)
                    for nq in d1:
                        await message.channel.send(f" ` {nq} `  ⟵ 1d{faces}")
            except:pass
    if 'd' in comando:
        quantidade, faces = map(int, message.content.split('d'))
        if comando == f'{quantidade}d{faces}':
            try:

                for nq in range(1, quantidade+1):
                        nq = random.randint(1, faces)
                        d1.append(nq)
                await message.channel.send(f'{message.author.name}-> seu resultado foi: {sum(d1)} {d1}')

            except:pass
    

@tree.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@tree.command(name="calc")
async def calc(interaction: discord.Interaction, equantidadecao:str):
   

    try:
        resp = eval(equantidadecao)
        messagem=f"seu resultado foi: ´{resp}' na equantidadeção:{equantidadecao}"

    except:
        messagem=f"Não foi possivel calcular a equantidadeção"

    await  interaction.response.send_message(messagem)

#dado
@tree.command(name="dado")
async def dado(interaction: discord.Interaction, quantidadentidade:int =1, lados:int = 20):
    d1 = list()
    for nq in range(1, quantidadentidade+1):
        nq = random.randint(1, lados)
        d1.append(nq)
    await interaction.response.send_message(f'{interaction.user.name}-> seu resultado foi: {sum(d1)} {d1}')

#atributos
@tree.command(name="atributos")
async def atributos(interaction: discord.Interaction):
    """
    
    """
    d1 = list()
    """Força:47
    Inteligência:24
    Agilidade:1
    Resistência:32
    Carisma:39
"""
    for _ in range(1, 6):
        nq = random.randint(1, 50)
        d1.append(nq)
    
    embed = discord.Embed(title="Atributos", color=discord.Color.red())
    embed.add_field(name="Força", value=d1[0], inline=False)
    embed.add_field(name="Inteligência", value=d1[1], inline=False)
    embed.add_field(name="Agilidade", value=d1[2], inline=False)
    embed.add_field(name="Resistência", value=d1[3], inline=False)
    embed.add_field(name="Carisma", value=d1[4], inline=False)
    await interaction.response.send_message(embed=embed)

# quero opção de  Cenário e colocar  uma dificudade aradorio
# @ree.command(name="set_environment")
# async def set_environment(interaction: discord.Interaction, local:str):
#     local = local.lower()
#     if local == "floresta":
#         await interaction.response.send_message("Você está em uma floresta")


    

@tree.command(name="help")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="Comandos", color=discord.Color.blue())
    embed.add_field(name="$", value="rola um dado de x  vezes com y lados ex:3$30", inline=False)
    embed.add_field(name="d", value="rola um dado de x  vezes com y lados ex:3d30", inline=False)
    embed.add_field(name="atributos", value="rola os atributos de um personagem", inline=False)
    embed.add_field(name="calc", value="calcula uma equantidadeção ex: 2+2", inline=False)
    await interaction.response.send_message(embed=embed)


bot.run(token)