from sopel import plugin, formatting


@plugin.search("ya('|’)ll")
def yall(bot, trigger):
    bot.reply("It's {}, you fucking moron.".format(formatting.bold("y'all")))
