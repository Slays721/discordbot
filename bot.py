import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix ='skid')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Type “skidhelp” For Commands'))
    print("Bot is ready.")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ping(ctx):
    await ctx.send(f'Your Ping is {round(client.latency * 1000)}ms')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Color.dark_orange()
    )

    embed.set_author(name='Help Commands')
    embed.add_field(name="skidping\n", value="Returns your ping", inline=False)
    embed.add_field(name='skidclear', value='Removes a specified number of messages', inline=False)
    #embed.add_field(name='skidkick', value="Kicks a user from the server", inline=False)
    #embed.add_field(name='skidban', value="Bans a user from the discord", inline=False)

    await ctx.send(embed=embed)

client.run('NzAzNDU0MDM4ODIxNDM3NDYw.XqO0vA.ko8-l0uJYR57D7AXR_oq95QgknA')
