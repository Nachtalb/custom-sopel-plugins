from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module
import re
import requests


@module.commands("isbn")
def isbn(bot, trigger):
    """Look up a book by its ISBN."""
    if not re.match(
        r"((978[\--– ])?[0-9][0-9\--– ]{10}[\--– ][0-9xX])|((978)?[0-9]{9}[0-9Xx])",
            trigger.group(2)):
        bot.reply("I need a valid ISBN.")
        return

    isbn_sanitized = trigger.group(2).replace(" ", "").replace("-", "")
    url = "https://openlibrary.org/isbn/{}".format(isbn_sanitized)
    try:
        book = requests.get(url).url
        bot.say(book)
    except BaseException:
        bot.reply("Error reaching API, probably.")
