from discord.ext.commands import Cog
from discord import Member
from discord.ext.commands import command

class General(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="salve")
    async def salve(self, ctx):
        await ctx.send(f"SALVEE {ctx.author.mention}! Eu sou o FraaaaankyBot a seu dispor.")

    @command(name="funcao")
    async def salve(self, ctx):
        await ctx.send(f"Eu não tenho funcao nenhuma, culpa do Hiroshime que me fez assim!")

    @command(name="tapa")
    async def tapa(self, ctx, member: Member, *, reason: Optional[str] = "sem razao aparente"):
        await ctx.send(f"{ctx.author.display_name} mandou um tapa bem na cara do {member.mention} {reason}!" )

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.corgs_ready.ready_up("general")


    def setup(bot):
        bot.add_cog(General(bot))
