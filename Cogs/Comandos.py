import discord

import discord.ext.commands
from discord.ext.commands import Cog
from discord.ext.commands import command
import asyncio

import cfg


class Comandos(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("Cog is working!")

    async def cog_check(self, ctx):
        pass
        # return discord.utils.get(ctx.guild.roles, id=cfg.ADMINROLEID) in ctx.author.roles

    # @command()
    # async def probarverificacion(self, ctx):
    #


async def setup(bot):
    await bot.add_cog(Comandos(bot))