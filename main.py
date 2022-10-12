import selfcord
import json
import sys
from aioconsole import aprint

from selfcord.models import message


sys.dont_write_bytecode = True

bot = selfcord.Bot(prefixes=["!", "o.", "o!"])

with open("./config.json", "r") as f:
    config = json.load(f)

token = config.get("token")



@bot.on("ready")
async def ball(time):
    print(f"{bot.user.name}\nTook {time * 1000:0.2f}ms to start up")


@bot.cmd(description="Displays the latency of the gateway")
async def latency(ctx):
    await ctx.message.delete()
    await ctx.send(f"```diff\n+ Ping is {bot.latency * 1000:0.2f}ms```")

@bot.cmd(description="Spams messages")
async def spam(ctx, amount: int, *, message: str) :
    await ctx.message.delete()
    await ctx.spam(amount, message)



bot.run(token)


