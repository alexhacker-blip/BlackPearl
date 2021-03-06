import pyfiglet

from pearl.utils import pearl_on_cmd, edit_or_reply, sudo_cmd


@pearl.on(pearl_on_cmd(pattern="figlet ?(.*)", outgoing=True))
@pearl.on(sudo_cmd(pattern="figlet ?(.*)", allow_sudo=True))
async def figlet(event):
    arjun = await edit_or_reply(event, "`Making This Text Eye Catchy...!`")
    if event.fwd_from:
        return
    CMD_FIG = {
        "slant": "slant",
        "3D": "3-d",
        "5line": "5lineoblique",
        "alpha": "alphabet",
        "banner": "banner3-D",
        "doh": "doh",
        "iso": "isometric1",
        "letter": "letters",
        "allig": "alligator",
        "dotm": "dotmatrix",
        "bubble": "bubble",
        "bulb": "bulbhead",
        "digi": "digital",
    }
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        text, cmd = input_str.split("|", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await arjun.edit("Please add some text to figlet")
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await arjun.edit("Invalid selected font.")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await arjun.edit("‌‌‎`{}`".format(result))
