# Deep Rock Galactic
# from sopel import plugin, formatting
from sopel import plugin
import random


@plugin.command("salute")
@plugin.search("!salute", "rock and stone")
def drg_salute(bot, trigger):
    if trigger.sender == "#drg":
        drg_salutes = [
            "By the beard!",
            "Come on, guys! Rock and Stone!",
            "Did I hear a Rock and Stone?",
            "For Karl!",
            "For Rock and Stone!",
            "If you don't Rock and Stone, you ain't coming home!",
            "Leave no dwarf behind!"
            "Like that! Rock and Stone!",
            "None can stand before us!",
            "Rock and roll!",
            "Rock and roll and Stone!",
            "Rock and Stone!",
            "Rock and Stone, brother!",
            "Rock and Stone, everyone!",
            "Rock and Stone forever!",
            "Rock and Stone in the heart!",
            "Rock and Stone - to the bone!",
            "Rock and Stone...yeeaah!",
            "ROCK......AND.... STONE!",
            "Rock on!",
            "Rock solid!",
            "That's it lads, Rock and Stone!",
            "We are UNBREAKABLE!",
            "We fight for Rock and Stone!",
            "We rock!",
            "Yaaaah, Rock and Stone!",
        ]
        bot.say(random.choice(drg_salutes))


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
            "Karl would approve of this.",
            "(drunk) ...K...Karl? Is...is that you?",
            "(drunk) Wait a minute...If all truths are knowable, then all truths must in fact be known.....but by whom? ...Karl would know!",
            "(drunk) I......I.......I know where Karl is! It's so bloody obvious! What...uhhh....hmmm....anyone up for playing the hoop game?",
            "Hmm...what Karl would choose?",
            "I'm gonna wear this in honor of Karl!",
            "People ask why we remember Karl. People ask what made him a legend. Rumor has it Skull Crusher Ale is at least partly to blame. Make of that what you will. Beware."
        ]
        bot.say(random.choice(karls))
