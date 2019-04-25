import discord
from discord.ext import commands


PREFIX = '>'


bot = commands.Bot(command_prefix=PREFIX)


@bot.command()
async def ping(ctx):
    '''reply with pong'''
    await ctx.send('pong')

@bot.command()
async def whoami(ctx):
    # msg = 'You are: ' + ctx.author.name + ' and ' + str(ctx.author.id)
    # msg = 'You are: {name} and {id}'.format(
    #     name=ctx.author.name, id=ctx.author.id
    # )
    msg = f'You are: {ctx.author.name} and {ctx.author.id}'

    await ctx.send(msg)


@bot.command()
async def who(ctx):
    pass


bot.run('YOUR_DISCORD_TOKEN_GOES_HERE')
