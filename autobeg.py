import discord, asyncio, time
from discord.ext import commands, tasks

token = ''
prefix = '+'

poop = discord.Client()
poop = commands.Bot(
    description='auto beg',
    command_prefix=prefix,
    self_bot=True
)

@poop.event
async def on_ready():
	print("ready! command = +beg")

@poop.command()
async def beg(ctx): 
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            await ctx.send('pls beg')           
            print(f'[AUTO-BEG] Beg sent: {count}')
            await asyncio.sleep(60)
        except Exception as e:
            print(f"[ERROR]: {e}")     

poop.run(token, bot=False)
