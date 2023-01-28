import discord
from apscheduler.triggers.cron import CronTrigger
from discord import Intents

from discord.ext.commands import command
from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import traceback
import sys

import cfg

PREFIX = ""


class Bot(BotBase):
    def __init__(self, token):
        self.token = token
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, intents=Intents.all())

        self.ready = False

    def run(self):
        print("Running bot...")
        super().run(self.token, reconnect=True)

    async def unload_cogs(self):
        pass
        #  await self.unload_extension("cog.AdminCommands")

    async def load_cogs(self):
        pass
        #  await self.load_extension("cog.AdminCommands")

    async def on_connect(self):
        await self.load_cogs()
        print("Bot connected.")

    async def on_disconnect(self):
        print("Bot disconnected.")

    async def on_ready(self):
        if not self.ready:
            self.ready = True

        self.guild = self.get_guild(cfg.GUILD_ID)

        self.scheduler.start()

    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            print(f"{ctx.author.name} no tiene permisos para ejecutar el comando {ctx.command}.")
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

