from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module, tools
import requests
import html


@module.commands("insult")
@module.require_chanmsg
def insult(bot, trigger):
    """Insults another user."""
    url = "https://evilinsult.com/generate_insult.php"
    params = {"lang": "en", "type": "json"}
    target = trigger.group(3)

    if not target:
        bot.reply("I need someone to insult, dipshit.")
        return
    target = tools.Identifier(target)

    if target == bot.nick:
        bot.reply("Nice try, retard.")
        return

    if target not in bot.channels[trigger.sender].privileges:
        bot.reply("I need someone to insult, dipshit.")
        return

    try:
        insult = requests.get(url, params=params).json()['insult']
        insult_escaped = html.unescape(insult)
        bot.say("{}: {}".format(target, insult_escaped))
    except BaseException:
        bot.reply("There was an error. Fuck you.")
