from telethon.tl.types import (
    ChannelParticipantsKicked,
)

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.unbanall(?: |$)(.*)", groups_only=True)
async def _(event):
    await event.edit("`Sedang Mencari List Banning.`")
    p = 0
    (await event.get_chat()).title
    async for i in event.client.iter_participants(
        event.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await event.client.edit_permissions(event.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await event.edit("`Sukses Menghapus List Banning`")


CMD_HELP.update(
    {
        "unbanall": "📚 **Cmd** : `.unbanall`\
    \n📄 **Descriptions** : Membatalkan semua Ban Di Anggota Grup."
    }
)
