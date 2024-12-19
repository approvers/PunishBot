from typing import Any

from discord import Client, Member, Intents

from config import PunishBotConfig

INTENTS = Intents.default()
INTENTS.members = True


class PunishBot(Client):
    def __init__(self, config: PunishBotConfig, **options: Any) -> None:
        self.__config: PunishBotConfig = config

        super().__init__(intents=INTENTS, **options)

    def launch(self) -> None:
        self.run(self.__config.DISCORD_TOKEN)

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")

    async def on_member_update(self, before: Member, after: Member) -> None:
        if before.id != self.__config.DISCORD_PUNISHMENT_TARGET_USER_ID:
            return

        if before.nick == after.nick:
            return

        if after.nick == self.__config.NICKNAME_TO_ENFORCE:
            return

        print(f"Detected nickname change from {before.nick} to {after.nick}")

        await after.edit(nick=self.__config.NICKNAME_TO_ENFORCE)
