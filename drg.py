# Deep Rock Galactic
# from sopel import plugin, formatting
from sopel import plugin
import random
# import unicodedata


@plugin.search("rock and stone")
def rock_and_stone(bot, trigger):
    if trigger.sender == "#drg":
        rocks_and_stones = [
            "ROCK and STONE!",
            "For rock and stone!"
        ]
        bot.say(random.choice(rocks_and_stones))


@plugin.search("karl")
def karl(bot, trigger):
    if trigger.sender == "#drg":
        karls = [
            "This one's for Karl!",
            "For Karl!",
            "To Karl!",
            "That thing ate bullets, like Karl drank beers!",
            "We got it! Karl would be proud!",
            "By Karl! Look at all that pretty sparkly...!",
            "I'll beat your record this time, just watch me!",
            "Karl would approve of this.",
            "...K...Karl? Is...is that you?",
            "Wait a minute...If all truths are knowable, then all truths must in fact be known.....but by whom? ...Karl would know!",
            "I......I.......I know where Karl is! It's so bloody obvious! What...uhhh....hmmm....anyone up for playing the hoop game?",
            "Hmm...what Karl would choose?",
            "I'm gonna wear this in honor of Karl!",
            "People ask why we remember Karl. People ask what made him a legend. Rumor has it Skull Crusher Ale is at least partly to blame. Make of that what you will. Beware."
        ]
        bot.say(random.choice(karls))
