
import json

# on importe le module discord.py
import discord

from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands


# créer le bot
bot = commands.Bot(command_prefix='/')



# détecter quand le bot est pret ("allumé") statut online / idle / dnd / invisible
@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(status=discord.Status.dnd,
                              activity=discord.Game("pour la sécurité du serveur tout les commande son désactiver"))

# clear chat
@bot.command()
async def clear(ctx, nombre : int):
  await ctx.channel.purge(limit = nombre + 1)

# ban
@bot.command()
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"**{user}** `à été ban pour la raison suivante :` **{reason}.**")


# kick
@bot.command()
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"**{user}** `à été kick du serveur pour la raison suivante :`  **{reason}.**")


# unban
@bot.command()
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"**{user}** `à été unban.`")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"`L'utilisateur` **{user}** `n'est pas dans la liste des bans`")


# créer la commande /bienvenue @pseudo
@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):
    # recupere le nom
    pseudo = nouveau_membre.mention

    # executer le message de bienvenue
    await ctx.send(f"**:tada: Bienvenue à {pseudo} sur le serveur AMICITIA ! :tada:**")

# verifier l'erreur
@bienvenue.error
async def on_command_error(ctx, error):
    # detecter cette erreur
    if isinstance(error, commands.MissingRequiredArgument):
        # envoyer un message
        await ctx.send("Tu dois faire /bienvenue @pseudo")


# parler dans le serveur avec le bot

# embed

# phrase
print("Lancement du bot...")

# connecter au serveur
bot.run("NjYxNzc2NTcwNTA3MDY3NDEy.XsrTUw.eHsjk6JQjx2LAwW1xovMqMenPVU")
