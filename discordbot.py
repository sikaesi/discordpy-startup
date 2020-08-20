from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

if not discord.opus.is_loaded(): 
    #もし未ロードだったら
    discord.opus.load_opus("heroku-buildpack-libopus")
    
bot.run(token)
