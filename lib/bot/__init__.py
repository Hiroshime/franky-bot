from discord import Intents
from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from glob import glob

PREFIX = "+"
OWNER_IDS = []
COGS = ["general"]


class Ready(object):
	def __init__(self):
		for cog in COGS:
			setattr(self, cog, False)

	def ready_up(self, cog):
		setattr(self, cog, True)
		print(f" {cog} cog ready")

	def all_ready(self):
		return all([getattr(self, cog) for cog in COGS])

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler =  AsyncIOScheduler()
        super().__init__(command_prefix=PREFIX,owner_ids=OWNER_IDS,intents=Intents.all())

    def setup(self):
        print(f"{COGS} passei aqui")
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} cog loaded")

        print("setup completo")

    def run(self, version):
        self.VERSION = version
        print("running setup...")
        self.setup()

        with open("/app/franky-bot/lib/bot/token.0", "r", encoding="utf-8") as tf:
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
#            channel = self.get_channel(760971404450856991)
#            await  channel.send("Frannky....Onlinee!")
        else:
            print("Bot reconectado")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

bot = Bot()

