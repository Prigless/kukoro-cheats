from twitchio.ext import commands
import time
import random

with open('config.txt', 'r') as f:
    CONFIG=f.readlines()

CHANNEL=CONFIG[0][9:-2]
ACCESS_TOKEN=CONFIG[1][14:-1]

print(CHANNEL)
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix='', initial_channels=[CHANNEL])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

bot = Bot()

@bot.event()
async def event_message(msg):
    if msg.echo:
        return
    print(msg.author.name+': '+str(msg.content))
    if msg.author.name == CHANNEL:
        time.sleep(round(random.uniform(0.1, 0.4), 10))
        if msg.content == '☺ACTION [KUKORO] <<< YOU CAN MOVE! >>>☺':
            chan = bot.get_channel(CHANNEL)
            print('chan.send("!go")\n'*10)
            await chan.send("!go")
        elif msg.content == '☺ACTION [KUKORO] <<< STOP! >>>☺':
            chan = bot.get_channel(CHANNEL)
            print('chan.send("!stop")\n'*10)
            await chan.send("!stop")
    await bot.handle_commands(msg)

bot.run()


