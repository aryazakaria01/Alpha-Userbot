from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.gsend ?(.*)")
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("`Pesan Di Di Teruskan Ke Grup Tujuan`")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("Pesan Di Di Teruskan Ke Grup Tujuan`")
    except BaseException:
        await event.edit("** Gagal Mengirim Pesan, Emang Lu Join Grup Nya Njing ? **")

CMD_HELP.update(
    {
        "grouplink": "📚 **Cmd** : `.gsend`\
    \n📄 **Descriptions** : Mengirim Pesan Jarak Jauh Ke Grup Lain .gsend <link grup> <pesan>."
    })
