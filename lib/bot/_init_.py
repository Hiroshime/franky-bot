from _typeshed import Self
from discord import Intents
from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsysncIOScheduler

PREFIX = "+"
OWNER_IDS = []


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler =  AsysncIOScheduler()
        super().__init__(
            commands_prefix=PREFIX,
            owner_ids=OWNER_IDS
            intents=Intents.all()
            )

    def run(self, version):
        self.VERSION = version
        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("rodando o bot...")
        super().run(self.TOKEN, reconnect=True)


    async def on_connect():
        print("Bot conectado")

    async def on_disconnect():
        print("Bot desconectado")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            print("Bot pronto")
        else:
            print("Bot reconectado")

    async def on_message(self, message):
        pass

bot = Bot()

