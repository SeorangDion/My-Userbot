from .. import ubot
from telethon import events


@ubot.on(events.NewMessage(outgoing=True, pattern="^[.!]alive$"))
async def _(event):
    await event.edit("I'm Online, Master!")
