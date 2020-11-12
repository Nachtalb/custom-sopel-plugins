from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module, formatting
import random

@module.commands("nod")
def nod(bot, trigger):
  """Nod."""
  bot.say("https://actionsack.com/img/trek/nod.gif")

@module.commands("spok")
def spok(bot, trigger):
  """Summon SPOK"""
  bot.say("https://actionsack.com/img/trek/spok.gif")

@module.rule("^Hello(\?|!)$")
def hi(bot, trigger):
  bot.say("Hello, %s!" %trigger.nick)

@module.rule("^nice\.$")
def nice(bot, trigger):
  bot.say("Nice.")

@module.rule("^yeah!$")
def yeah(bot, trigger):
  bot.say("https://actionsack.com/img/misc/yeah!.gif")

@module.rule("^retard.*")
def retarded(bot, trigger):
  retard = ["https://actionsack.com/img/retard/catarded.png", "https://actionsack.com/img/retard/retarded.gif", "https://actionsack.com/img/retard/△.gif"]
  bot.say(random.choice(retard))

@module.rule("rekt", ".*get\srekt.*")
def rekt(bot, trigger):
  rekt = ["https://actionsack.com/img/rekt/baseball.gif", "https://actionsack.com/img/rekt/beachdive.mp4", "https://actionsack.com/img/rekt/beachskillz.mp4", "https://actionsack.com/img/rekt/bf1revenge.mp4", "https://actionsack.com/img/rekt/bf1sniper.mp4", "https://actionsack.com/img/rekt/blackman.mp4", "https://actionsack.com/img/rekt/botw-sled.mp4", "https://actionsack.com/img/rekt/bridgedive.mp4", "https://actionsack.com/img/rekt/carcrash.gif", "https://actionsack.com/img/rekt/gta-bike.mp4", "https://actionsack.com/img/rekt/gta-flight.mp4", "https://actionsack.com/img/rekt/gta-phone.mp4", "https://actionsack.com/img/rekt/gta-post.mp4", "https://actionsack.com/img/rekt/gta-rekt.mp4", "https://actionsack.com/img/rekt/gta-stomp.gif", "https://actionsack.com/img/rekt/jeep.gif", "https://actionsack.com/img/rekt/leap!.mp4", "https://actionsack.com/img/rekt/LOLOLOLOL.gif", "https://actionsack.com/img/rekt/poolgirl.gif", "https://actionsack.com/img/rekt/rekt.png", "https://actionsack.com/img/rekt/running.gif", "https://actionsack.com/img/rekt/skateit.mp4", "https://actionsack.com/img/rekt/slammin.mp4", "https://actionsack.com/img/rekt/smash.mp4", "https://actionsack.com/img/rekt/sniped.mp4", "https://actionsack.com/img/rekt/walkbot.mp4", "https://actionsack.com/img/rekt/walkitoff.mp4", "https://actionsack.com/img/rekt/watergun.mp4"]
  bot.say(random.choice(rekt))

@module.rule("^420.*")
def fourtwenty(bot, trigger):
  fourtwozero = ["https://actionsack.com/img/420/birb.png", "https://actionsack.com/img/420/champions.png", "https://actionsack.com/img/420/claim.png", "https://actionsack.com/img/420/coma.png", "https://actionsack.com/img/420/comrade.png", "https://actionsack.com/img/420/dr.png", "https://actionsack.com/img/420/exp.png", "https://actionsack.com/img/420/gravityfalls.png", "https://actionsack.com/img/420/highnoon.gif", "https://actionsack.com/img/420/highnoon.png", "https://actionsack.com/img/420/lisa.png", "https://actionsack.com/img/420/mowing.png", "https://actionsack.com/img/420/old.png", "https://actionsack.com/img/420/pikachu.png", "https://actionsack.com/img/420/🍩.png", "https://actionsack.com/img/420/pokemon.png", "https://actionsack.com/img/420/realdanger.png", "https://actionsack.com/img/420/sealab.png", "https://actionsack.com/img/420/telluhwat.png", "https://actionsack.com/img/420/thomas.png", "https://actionsack.com/img/420/thomasrust.png", "https://actionsack.com/img/420/timesheet.png", "https://actionsack.com/img/420/toasted.gif", "https://actionsack.com/img/420/toystory.png", "https://actionsack.com/img/420/wednesday.png"]
  bot.say(random.choice(fourtwozero))

@module.rule(":retardeyes:")
def retardeyes(bot, trigger):
  bot.say("https://cdn.discordapp.com/emojis/286222898836799488.png")

@module.rule("^thx.*")
def thx(bot, trigger):
  bot.say("https://actionsack.com/img/thx/thx.png")

@module.rule("^(thanks.*|thank\syou.*)")
def thanks(bot, trigger):
  thanks = ["https://actionsack.com/img/thx/h3h3.webm", "https://actionsack.com/img/thx/t.hanks.mp4", "https://actionsack.com/img/thx/thankyou.mp4"]
  bot.say(random.choice(thanks))

@module.rule("^😢$")
def crying(bot, trigger):
  crying = ["https://actionsack.com/img/QQ/QQ001.gif", "https://actionsack.com/img/QQ/QQ002.gif", "https://actionsack.com/img/QQ/QQ003.gif", "https://actionsack.com/img/QQ/QQ004.gif", "https://actionsack.com/img/QQ/QQ005.gif"]
  bot.say(random.choice(crying))

@module.rule(".*!xms.*")
def xms(bot, trigger):
  bot.say("https://w2g.tv/rooms/actionsack-csurhbl9dkwvwnk91a")

@module.rule(".*📖.*")
def book(bot, trigger):
  book = ["https://actionsack.com/img/mike/📖/📖.gif", "https://actionsack.com/img/mike/📖/📖.jpg", "https://actionsack.com/img/mike/📖/📖+.jpg", "https://actionsack.com/img/mike/📖/📖🐇.jpg"]
  bot.say(random.choice(book))

@module.rule("^8D$")
def greg(bot, trigger):
  bot.say("Greg was never in IRC...")

@module.rule("^FOAD.*")
def foad(bot, trigger):
  bot.say("https://actionsack.com/img/misc/foad.png")

@module.rule(".*adapters.*")
def adapters(bot, trigger):
  adapters = ["https://actionsack.com/img/misc/adapters01.png", "https://actionsack.com/img/misc/adapters02.png"]
  bot.say(random.choice(adapters))

@module.rule(".*accident\W")
def accident(bot, trigger):
  bot.say("https://actionsack.com/img/misc/accident.png")

@module.rule(".*14nm.*")
def fourteennm(bot, trigger):
  bot.say("https://p.xnaas.info/zz-misc/14nm+++++.mp4")

@module.rule("^bait.*")
def bait(bot, trigger):
  bait = ["https://actionsack.com/img/bait/404bait.png", "https://actionsack.com/img/bait/all-bait.gif", "https://actionsack.com/img/bait/b8.png", "https://actionsack.com/img/bait/bai--what.png", "https://actionsack.com/img/bait/bait-g.gif", "https://actionsack.com/img/bait/bait-krunk.jpg", "https://actionsack.com/img/bait/bait-pole.png", "https://actionsack.com/img/bait/bait-sim.png", "https://actionsack.com/img/bait/bait-therapy.png", "https://actionsack.com/img/bait/bait.gif", "https://actionsack.com/img/bait/bait.png", "https://actionsack.com/img/bait/bait001.jpg", "https://actionsack.com/img/bait/bait002.png", "https://actionsack.com/img/bait/bait003.jpg", "https://actionsack.com/img/bait/bait004.jpg", "https://actionsack.com/img/bait/bait005.jpg", "https://actionsack.com/img/bait/bait006.png", "https://actionsack.com/img/bait/bait007.png", "https://actionsack.com/img/bait/bait008.png", "https://actionsack.com/img/bait/bait009.jpg", "https://actionsack.com/img/bait/bait010.jpg", "https://actionsack.com/img/bait/bait011.jpg", "https://actionsack.com/img/bait/bait012.jpg", "https://actionsack.com/img/bait/bait013.jpg", "https://actionsack.com/img/bait/bait014.jpg", "https://actionsack.com/img/bait/bait015.jpg", "https://actionsack.com/img/bait/bait016.jpg", "https://actionsack.com/img/bait/bait017.png", "https://actionsack.com/img/bait/bait018.png", "https://actionsack.com/img/bait/bait019.png", "https://actionsack.com/img/bait/bait020.jpg", "https://actionsack.com/img/bait/bait021.jpg", "https://actionsack.com/img/bait/bait022.png", "https://actionsack.com/img/bait/bait023.jpg", "https://actionsack.com/img/bait/bait024.jpg", "https://actionsack.com/img/bait/bait025.png", "https://actionsack.com/img/bait/bait026.png", "https://actionsack.com/img/bait/bait027.png", "https://actionsack.com/img/bait/baitkakke.jpg", "https://actionsack.com/img/bait/baitku.png", "https://actionsack.com/img/bait/baitnado.jpg", "https://actionsack.com/img/bait/baito.png", "https://actionsack.com/img/bait/changed-bait.jpg", "https://actionsack.com/img/bait/chosen-bait.png", "https://actionsack.com/img/bait/debait.png", "https://actionsack.com/img/bait/hq-bait.jpg", "https://actionsack.com/img/bait/MBGA.jpg", "https://actionsack.com/img/bait/mikes-bait.jpg", "https://actionsack.com/img/bait/poke-bait.png", "https://actionsack.com/img/bait/teach-bait.jpg", "https://actionsack.com/img/bait/whose-bait.jpg", "https://actionsack.com/img/bait/wtf-bait.jpg", "https://actionsack.com/img/bait/"]
  bot.say(random.choice(bait))

@module.rule(".*backhand.*")
def backhand(bot, trigger):
  bot.say("https://actionsack.com/img/misc/backhand.mp4")

@module.rule("^😠$")
def angryeyes(bot, trigger):
  bot.say("https://actionsack.com/img/misc/angryeyes.gif")

@module.rule(".*alot.*")
def alot(bot, trigger):
  bot.say("https://actionsack.com/img/alot/")

@module.rule(".*♿.*")
def handicap(bot, trigger):
  bot.say("https://actionsack.com/img/♿/♿.mp4")

@module.rule(".*⤵️.*")
def down(bot, trigger):
  bot.say("https://actionsack.com/img/mike/down.gif")

@module.rule("^\.\.\.$")
def dotdotdot(bot, trigger):
  bot.say("...")

@module.rule("^\.dz$")
def deeznutz(bot, trigger):
  bot.say(formatting.bold("DEEZ NUTZ!"))

@module.rule("^\s\/lenny$")
def lenny(bot, trigger):
  lenny = ["https://actionsack.com/img/lenny/lenny-anime.gif", "https://actionsack.com/img/lenny/lenny-crazy.mp4", "https://actionsack.com/img/lenny/lenny-spiral.gif"]
  bot.say(random.choice(lenny))

@module.rule("^pranked!")
def prank(bot, trigger):
  prank = ["https://actionsack.com/img/prank/prank01.png", "https://actionsack.com/img/prank/prank02.png"]
  bot.say(random.choice(prank))

@module.rule("^\?\?\?$")
def que(bot, trigger):
  bot.say("https://actionsack.com/img/misc/¿¿¿.png")

@module.rule("^\\\o/$")
def handsup(bot, trigger):
  bot.say("\\o/")

@module.rule("^¯\\\_\(ツ\)_\/¯")
def shrug(bot, trigger):
  bot.say("¯\\_(ツ)_/¯")

@module.rule("^🦏$")
def rhino(bot, trigger):
  bot.say("https://actionsack.com/img/🦏/🦏.gif")

@module.rule("^🧀$")
def cheese(bot, trigger):
  bot.say("https://actionsack.com/img/🧀/🧀.mp4")

@module.rule("^🦄$")
def unicorn(bot, trigger):
  bot.say("https://actionsack.com/img/🦄/🦄.jpg")

@module.rule("^🙃$")
def upsidedown(bot, trigger):
  bot.say("🙃")

@module.rule("^(🖕|🖕🏻|🖕🏼|🖕🏽|🖕🏾|🖕🏿)$")
def fuckyouback(bot, trigger):
  bot.say("Fuck you, " + trigger.nick + "!")

@module.rule("^👏$")
def clap(bot, trigger):
  bot.say("👏🏻👏🏼👏🏽👏🏾👏🏿")

@module.rule("^👍$")
def thumbsup(bot, trigger):
  bot.say("👍🏻👍🏼👍🏽👍🏾👍🏿")

@module.rule("^👋$")
def wave(bot, trigger):
  bot.say("👋🏻👋🏼👋🏽👋🏾👋🏿")

@module.rule(".*(🌎|🌍|🌏).*")
def earthchan(bot, trigger):
  bot.say("https://actionsack.com/img/🌎/water.png")

@module.rule("^🐉$")
def dragon(bot, trigger):
  bot.say("https://p.xnaas.info/dragon.gif")

@module.rule("^🏈$")
def football(bot, trigger):
  football = ["D'Marcus Williums", "T.J. Juckson", "T'varisuness King", "Jackmerius Tacktheritrix", "D'Squarius Green, Jr.", "Dan Smith", "The Player Formerly Known as Mousecop", "Ibrahim Moizoos", "D'Isiah T. Billings-Clyde", "D'Jasper Probincrux III", "Leoz Maxwell Jilliumz", "Javaris Jamar Javarison-Lamar", "Davoin Shower-Handel", "Hingle McCringleberry", "L'Carpetron Dookmarriot", "J'Dinkalage Morgoone", "Xmus Jaxon Flaxon-Waxon", "Saggitariutt Jefferspin", "D'Glester Hardunkichud", "Swirvithan L'Goodling-Splatt", "Quatro Quatro", "Ozamataz Buckshank", "Beezer Twelve Washingbeard", "Shakiraquan T.G.I.F. Carter", "X-Wing @Aliciousness", "Sequester Grundelplith M.D.", "Scoish Velociraptor Maloish", "T.J. A.J. R.J. Backslashinfourth V", "Eeeee Eeeeeeeee", "Donkey Teeth", "Torque [Construction Noise] Lewith", "Tyroil Smoochie-Wallace"]
  bot.say(random.choice(football))

@module.rule(".*🍍🍕.*")
def sin(bot, trigger):
  bot.say("This is a sin.")

@module.rule(".*xfiles.*")
def xfiles(bot, trigger):
  bot.say("Did you know that the X-Files is going to have 6 new episodes this summer on FOX, Aegisfate?")

@module.rule(".*triggered.*")
def triggered(bot, trigger):
  triggered = ["https://actionsack.com/img/triggered/beaker.gif", "https://actionsack.com/img/triggered/triggered.gif", "https://actionsack.com/img/triggered/feek.gif"]
  bot.say(random.choice(triggered))

@module.rule(".*to be fair.*")
def tobefair(bot, trigger):
  bot.say("https://actionsack.com/img/misc/tobefair.mp4")

@module.rule("^This is The Way\.($|\s$)")
def theway(bot, trigger):
  bot.say("This is The Way.")

@module.rule("^stop being poor.*")
def stopbeingpoor(bot, trigger):
  bot.say("https://actionsack.com/img/misc/stopbeingpoor.jpg")

@module.commands("tb")
def tb(bot, trigger):
  """Spout technobabble."""
  tb = ["When you account for the nm offset variable, the difference between 32-bit and 64-bit CPUs really only matters when calculating differential sub-routine pipeline algorithms.", "high 32-bit TOS encrypted voIP", "remote access through TeamSpeak", "if you reboot it may cement the command scripts that the virus is using to distribute DDOS variants", "When the biometrics of the boot sector exceeds the buffer cache then clock-cycles reroute to the LAN thus creating  a load balancing markup stack.", "I'll start on a GUI in Visual Basic to backtrack the mainframe.", "You can use the ps commands to redirect you to the home directory provided you used the subversion syntax correctly.", "The Internet is like water in pipes: when one pipe gets cut the Internet pressure drops because it is leaking uncontrollably from the open pipe. The Internet through WiFi, however, is like a swimming pool. If you open a hole in the building or pool the wifi starts flooding out and the wifi starts to lower. That's the reasoning behind revolving doors. Since they're compartmentalized, the building loses a smaller, fixed amount of internet per entry/exit, which reduces costs and allows more consistency for planning an office's WiFi needs.", "I JSON SQL DBs all the time!", "Lol you a pussyyyyy when I pull your IP address I'm gonna take your account then you gonna have to make a new account bc you cant get it back", "Can't leave without your processor? Clone it! You can copy the processor operating code wirelessly with a sniffer device.", "Then they do a triple worm blue cobalt IP hack.", "That's how the hacking's done. Satellite telemetry.", "SECURITY UPDATES CAUSE AUTISM. WON'T SOMEBODY THINK OF THE CHILDREN???", "The asymmetrical phase splitter is offline. We need to compensate for the gravimetric charge imbalance by re-routing power through the electron plasma injector port.", "Overheating weak partitions inverts the critical protocols.", "Higher numbered ports are always faster, because they travel nearer the outside of the wire, and the 'skin effect' means that that type of transmission is more reliable. So port 80 is going to be slower. If you want to connect with a very fast speed, you might want to try port 3389. This is why when you connect to port 22 you're probably only going to get some kind of text interface, if you connect to port 80 you might get some images along with it, and if you connect to port 3389, you'll get to see and interact with the whole operating system.", "That's a node brainer!", "Laptops generally don't need to take as many breaks/pauses as desktops, so they don't need that key. Sometimes, the larger laptops like yours w/ a numpad will have it, but only if the laptop hasn't worked out in a while, and gets winded easily.", "In order to hack a laptop's battery you need to initiate a GET request from an HTML page then use CSS to parse the DOS command XPLDBTRY.EXE that will make the battery's cooling fail, and then explode.", "Atlas Seeds contain zonally-shifted quasi-stellar substrate. WARNING: do not allow matrix to commune with this dimensional space.", "Sending packets is reserved to level 1337 hackers only. If you really want to do this you would need to bypass the FireWire's mainframe on your computer. Then you would need to encrypt and enumerate the firewall of whatever server you are trying to send the packet to. Then you would need to exploit the server's hypervisor root code to overflow the VGA interface. After that, all you need to do is code a VPN in Visual Basic and you should be able to do it without any problems.", "You should rebuild the kernel but only after rebooting your router. It gets a bit tricky with the buttons 'cause you need to press ctrl + alt + printscreen for 5 seconds and at the same time the reset button on your router. Last time I used my hands for the keyboard and reached for the router with one foot and managed to send the packet, although I also installed a firewall on Winamp and now I can only play Nickelback songs.", "Yeah but quantum info extraction was patched by the NSA last month, you gotta entangle the data stream to a local area network loop now.", "Don't worry, you'll just need to use a Raspberry Pi to enable four-factor authentication VPN firewalls and he won't be able to get into the mainframe!", "Uh oh, his friend is good with Linux! Better watch out! He might grep into your sudoers file and DDoS your hard drive!", "We reverse engineered Amazo's operating system and whipped up a virus to wipe his CPU.", "He's got a better grasp on Python 6 malware encryption than anybody at the DEO.", "I don't want to say the computer is old, but its IP address was 1.", "Are you coding in SQL or Java?", "Your UI is open-source JPEGs you got from MP3s off the web.", "Software running slow? Just decompile it!", "The secondary gyrodyne relays of the propulsion field intermatrix have depolarized!", "The Enterprise computer system is controlled by three primary main processing cores, cross-linked with a redundant melacortz ramistat. Fourteen kiloquad interface modules. The core element is based on an FTL nanoprocessor with twenty five bilateral kelilactirals, with twenty of those being slaved into the primary heisenfram terminal.", "Shunt plasma from the buzzard collectors into the Heisenberg compensators in order to generate sufficient tachyon emissions to disperse neutrino buildup around the warp core, thereby establishing a static warp bubble!"]
  bot.say(random.choice(tb), max_messages=2)

@module.commands("jolly")
def jolly(bot, trigger):
  """Nothing tops The Jolly Rancher story."""
  bot.say("Nothing tops The Jolly Rancher story: pastebin.com/qnHyYZuV")

@module.commands("hg")
def hg(bot, trigger):
  """I've got the highground now!"""
  bot.say("https://actionsack.com/img/misc/highground.jpg")

@module.commands("fgr")
def fgr(bot, trigger):
  """Family Guy reference!!!!!"""
  fgr = ["https://actionsack.com/img/fgr/gay.jpg", "https://actionsack.com/img/fgr/gears.jpg", "https://actionsack.com/img/fgr/hang.gif", "https://actionsack.com/img/fgr/stewie-gun.jpg"]
  bot.say(random.choice(fgr))

@module.commands("adr")
def adr(bot, trigger):
  """American Dad reference!"""
  bot.say("https://actionsack.com/img/fgr/ADR.jpg")

@module.commands("csr")
def csr(bot, trigger):
  """Cleveland Show reference!"""
  bot.say("https://actionsack.com/img/fgr/CSR.jpg")

@module.commands("aegislive")
def aegislive(bot, trigger):
  """Aegisfate's YouTube livestream link."""
  bot.say("https://youtube.com/user/mac2486/live")

@module.rule(".*!!banebread.*")
def banebread(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/banebread.png")

@module.rule(".*!!bread.*")
def bread(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/🍞.png")

@module.rule(".*!!datascii.*")
def datascii(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/datascii.gif")

@module.rule(".*!!dickaroo.*")
def dickaroo(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/dickaroo.gif")

@module.rule(".*!!fgr.*")
def fgrnsfw(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/chris-in-brian.png")

@module.rule(".*!!ghostbabies.*")
def ghostbabies(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/ghostbabies.gif")

@module.rule(".*!!gimp.*")
def gimp(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/gimp.gif")

@module.rule(".*!!ponies.*")
def ponies(bot, trigger):
  bot.say("https://actionsack.com/img/nsfw/ponies.mp4")

@module.rule(".*!!jordan.*")
def jordan(bot, trigger):
  jordan = ["https://actionsack.com/img/jordan/ddosvariants.png", "https://actionsack.com/img/jordan/littledick.png"]
  bot.say(random.choice(jordan))

@module.rule("^!b8$")
def beight(bot, trigger):
  bot.say("steam://install/567090")

@module.rule(".*kristen.*")
def kristen(bot, trigger):
  kristen = ["https://actionsack.com/img/kristen/keith.png", "https://actionsack.com/img/kristen/pins.png", "https://actionsack.com/img/kristen/racist.png", "https://actionsack.com/img/kristen/rekt.png", "https://actionsack.com/img/kristen/repost.png", "https://actionsack.com/img/kristen/top.png"]
  bot.say(random.choice(kristen))

@module.rule("^Tasian loves pickles\.($|\s)")
def tasianpickles(bot, trigger):
  bot.say("https://actionsack.com/img/tasian/pickles.png")

@module.commands("asg")
def allsystemsgo(bot, trigger):
  """All systems go!"""
  bot.say("https://actionsack.com/img/misc/allsystemsgo.png")

@module.commands("murica")
def murica(bot, trigger):
  """Delivers pure Freedom™ into chat."""
  murica = ["https://actionsack.com/img/murica/clapping.mp4", "https://actionsack.com/img/murica/kiss.gif", "https://actionsack.com/img/murica/knockknock.gif", "https://actionsack.com/img/murica/freedomaf.mp4"]
  bot.say(random.choice(murica))

@module.commands("pledge")
def pledge(bot, trigger):
  """Say US Pledge of Allegiance."""
  bot.say("I pledge allegiance to the flag of the United States of America. Thank you very very much for letting us little kids live here. It really really was nice of you. You didn't have to do it. And it's really not creepy to have little little kids mindlessly recite this anthem every day and pledge their life to a government before theyre old enough to really think about what they're saying.")
  bot.say("This is not a form of brainwashing. This is not a form of brainwashing. This is not a form of brainwashing.")
  bot.say("This is really the greatest country in the whole world. All the other countries suck. And if this country ever goes to go to war, as its often wont to do, I promise to help go and kill all the other country's kids.")
  bot.say("God bless Johnson & Johnson. God bless GE. God bless Citigroup.")

@module.commands("mushkin")
def mushkin(bot, trigger):
  """Broken promises suck."""
  bot.say("Hey xnaas and feek, did you know that Mushkin announced a 4TB SSD for $500 at CES 2016 and never fuckin' delivered? How neat is that?")

@module.commands("mirai")
def mirai(bot, trigger):
  """Gone but not forgotten, noble soviet bear."""
  bot.say("https://actionsack.com/img/putin/🐻.mp4")

@module.commands("putin")
def putin(bot, trigger):
  """'President' of Russia."""
  putin = ["https://actionsack.com/img/putin/dance.mp4", "https://actionsack.com/img/putin/pigeon.mp4", "https://actionsack.com/img/putin/ritz.gif", "https://actionsack.com/img/putin/🐻.mp4"]
  bot.say(random.choice(putin))

@module.commands("aidsclub")
def aidsclub(bot, trigger):
  """Welcome to the club, loser."""
  bot.say("https://actionsack.com/img/misc/aidsclub.png")

@module.commands("barometer")
def barometer(bot, trigger):
  """Look to Steve Harvey for moral support and understanding."""
  bot.say("https://actionsack.com/img/misc/barometer.png")

@module.rule("^Oh,\syou!($|\s$)")
def ohyou(bot, trigger):
  bot.say("https://actionsack.com/img/misc/Oh,you!.jpg")

@module.commands("battletoad")
def battletoad(bot, trigger):
  """Deploy a battletoad!"""
  bot.say("https://actionsack.com/img/misc/battletoad.mp4")

@module.commands("beaker")
def beaker(bot, trigger):
  bot.say("https://actionsack.com/img/misc/beaker.mp4")

@module.commands("bomb")
def bomb(bot, trigger):
  """Nuke 'em out of existence!"""
  bot.say("https://actionsack.com/img/misc/bomb.mp4")

@module.commands("broden")
def broden(bot, trigger):
  """Deploy Broden...👀"""
  bot.say("https://actionsack.com/img/misc/broden.mp4")

@module.rule(".*mikey\sbikey.*")
def mikeybikey(bot, trigger):
  bot.say("https://actionsack.com/img/as/mikeybikey.png")

@module.rule(".*meal\swith\sit.*")
def mealwithit(bot, trigger):
  bot.say("https://actionsack.com/img/deal/mealwithit.gif")

@module.commands("mindjack")
def mindjack(bot, trigger):
  bot.say("https://actionsack.com/img/misc/mindjack.png")

@module.commands("music")
def listentomusic(bot, trigger):
  bot.say("https://actionsack.com/img/kys/music.gif")

@module.commands("doge")
def doge(bot, trigger):
  """Doge memes! (There's not very many...)"""
  doge = ["https://actionsack.com/img/doge/batdoge.gif", "https://actionsack.com/img/doge/dogemine.gif", "https://actionsack.com/img/doge/skeledoge.gif"]
  bot.say(random.choice(doge))

@module.rule(".*!dogemine.*")
def dogemine(bot, trigger):
  bot.say("https://actionsack.com/img/doge/dogemine.gif")

@module.rule(".*!skeledoge.*")
def skeledoge(bot, trigger):
  bot.say("https://actionsack.com/img/doge/skeledoge.gif")

@module.rule(".*!batdoge.*")
def batdoge(bot, trigger):
  bot.say("https://actionsack.com/img/doge/batdoge.gif")

@module.rule(".*slow\sdown.*")
def slowdown(bot, trigger):
  bot.say("https://www.youtube.com/watch?v=fJdqw-JzW08")

@require_admin
@module.commands("smmcb")
def smmcb(bot, trigger):
  bot.say("https://actionsack.com/img/misc/smmcb.gif")

@module.rule("^noice$")
def noice(bot, trigger):
  bot.say("noice")

@module.rule(".*sockbot.*")
def sockbot(bot, trigger):
  sockbot = ["https://actionsack.com/img/sockbot/headsortails.png", "https://actionsack.com/img/sockbot/L337.png", "https://actionsack.com/img/sockbot/phone.png"]
  bot.say(random.choice(sockbot))

@module.commands("brony")
def brony(bot, trigger):
  bot.say("https://actionsack.com/img/mike/brony.png")

@module.rule("^banned.*")
def banned(bot, trigger):
  banned = ["https://actionsack.com/img/banned/beetlejuice.mp4", "https://actionsack.com/img/banned/carryon.png", "https://actionsack.com/img/banned/clapping.gif", "https://actionsack.com/img/banned/hanging.gif", "https://actionsack.com/img/banned/samuel.gif", "https://actionsack.com/img/banned/slapbeavis.gif", "https://actionsack.com/img/banned/slap.gif", "https://actionsack.com/img/banned/tasian.gif", "https://actionsack.com/img/banned/trash.png", "https://actionsack.com/img/banned/trump.gif", "https://actionsack.com/img/banned/voodoo.png", "https://actionsack.com/img/banned/xbox.png", "https://actionsack.com/img/banned/xnaas.gif"]
  bot.say(random.choice(banned))

@module.rule(".*boycott.*")
def boycott(bot, trigger):
  bot.say("https://actionsack.com/img/misc/boycott.jpg")

@module.rule(".*censor.*")
def censor(bot, trigger):
  censor = ["https://actionsack.com/img/censored/bunny.png", "https://actionsack.com/img/censored/censored.png", "https://actionsack.com/img/censored/eyesored.png", "https://actionsack.com/img/censored/fox.gif", "https://actionsack.com/img/censored/fren.png", "https://actionsack.com/img/censored/nose.png", "https://actionsack.com/img/censored/spider.png", "https://actionsack.com/img/censored/tasian.png"]
  bot.say(random.choice(censor))

@module.rule("^Ping!($|\s$)")
def pingpong(bot, trigger):
  bot.say("Pong!")

@module.rule("^Bing!($|\s$)")
def bingbong(bot, trigger):
  bot.say("Bong!")

@module.rule("^Ching!($|\s$)")
def chingchong(bot, trigger):
  bot.say("Chong!")

@module.rule("^Ding!($|\s$)")
def dingdong(bot, trigger):
  bot.say("Dong!")

@module.rule("^Wing!($|\s$)")
def wingwong(bot, trigger):
  bot.say("Wong!")

@module.commands("work")
def worktoday(bot, trigger):
  """I don't really wanna do the work today..."""
  bot.say("https://actionsack.com/img/misc/work.webm")

@module.rule(".*stbyn.*")
def stbyn(bot, trigger):
  bot.say("Sucks to be you, %s!" %formatting.italic("nerd"))

@module.rule(".*🥓.*")
def bacon(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🥓.mp4")

@module.rule(".*🍜.*")
def soupbowl(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🍜.mp4")

@module.rule(".*🍞.*")
def breadchan(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🍞.png")

@module.rule(".*(🎅|🎅🏻|🎅🏼|🎅🏽|🎅🏾|🎅🏿).*")
def santa(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🎅.png")

@module.rule(".*🎧.*")
def headphones(bot, trigger):
  bot.say("https://actionsack.com/img/misc/🎧.png")

@module.rule(".*fuck you(?!r).*")
def fuckyou(bot, trigger):
  fuckyou = ["https://actionsack.com/img/fuck/01_Two_Feet-Go_Fuck_Yourself.mp3", "https://actionsack.com/img/fuck/airline.mp4", "https://actionsack.com/img/fuck/anime.webm", "https://actionsack.com/img/fuck/anime.mp4", "https://actionsack.com/img/fuck/ape.png", "https://actionsack.com/img/fuck/aquaman.gif", "https://actionsack.com/img/fuck/arms.gif", "https://actionsack.com/img/fuck/arrow.mp4", "https://actionsack.com/img/fuck/bb8.gif", "https://actionsack.com/img/fuck/bird.gif", "https://actionsack.com/img/fuck/bot.mp4", "https://actionsack.com/img/fuck/buzz.webm", "https://actionsack.com/img/fuck/card.gif", "https://actionsack.com/img/fuck/climb.gif", "https://actionsack.com/img/fuck/compilation.mp4", "https://actionsack.com/img/fuck/cunt.mp4", "https://actionsack.com/img/fuck/cutout.mp4", "https://actionsack.com/img/fuck/deaf.mp4", "https://actionsack.com/img/fuck/deer.mp4", "https://actionsack.com/img/fuck/disney.gif", "https://actionsack.com/img/fuck/doggogfy.mp4", "https://actionsack.com/img/fuck/driving.mp4", "https://actionsack.com/img/fuck/drums.mp4", "https://actionsack.com/img/fuck/enthusiastic.mp4", "https://actionsack.com/img/fuck/faoy.mp4", "https://actionsack.com/img/fuck/friday.mp4", "https://actionsack.com/img/fuck/fuckeverything.mp4", "https://actionsack.com/img/fuck/fuckyeah!.mp4", "https://actionsack.com/img/fuck/fuku.png", "https://actionsack.com/img/fuck/fur.mp4", "https://actionsack.com/img/fuck/godzilla.mp4", "https://actionsack.com/img/fuck/gofuckyourself.mp4", "https://actionsack.com/img/fuck/goldenboye.mp4", "https://actionsack.com/img/fuck/grow.mp4", "https://actionsack.com/img/fuck/h3h3.mp4", "https://actionsack.com/img/fuck/hook.png", "https://actionsack.com/img/fuck/idgaf.mp4", "https://actionsack.com/img/fuck/jacket.gif", "https://actionsack.com/img/fuck/juliemao.mp4", "https://actionsack.com/img/fuck/kraken.gif", "https://actionsack.com/img/fuck/loop.gif", "https://actionsack.com/img/fuck/peaceamongworlds.gif", "https://actionsack.com/img/fuck/pigeon.mp4", "https://actionsack.com/img/fuck/pocketcat.gif", "https://actionsack.com/img/fuck/pocket.gif", "https://actionsack.com/img/fuck/ragnarok.mp4", "https://actionsack.com/img/fuck/rudy.png", "https://actionsack.com/img/fuck/rugrats.gif", "https://actionsack.com/img/fuck/samuel.mp4", "https://actionsack.com/img/fuck/samueltransparent.mp4", "https://actionsack.com/img/fuck/sayan.gif", "https://actionsack.com/img/fuck/sciencegfy.mp4", "https://actionsack.com/img/fuck/skating.mp4", "https://actionsack.com/img/fuck/square.gif", "https://actionsack.com/img/fuck/tommydoor.mp4", "https://actionsack.com/img/fuck/trumpet.mp4", "https://actionsack.com/img/fuck/westworld.mp4", "https://actionsack.com/img/fuck/ww-mib.mp4", "https://actionsack.com/img/fuck/☂.gif"]
  bot.say(random.choice(fuckyou))

@module.rule(".*(gfy[^c]|go fuck yourself).*")
def gfy(bot, trigger):
  gfy = ["https://actionsack.com/img/fuck/animegfy.mp4", "https://actionsack.com/img/fuck/gofuckyourself.mp4", "https://actionsack.com/img/fuck/doggogfy.mp4", "https://actionsack.com/img/fuck/sciencegfy.mp4"]
  bot.say(random.choice(gfy))

@module.rule("^Fuck!.*")
def fuckexclamation(bot, trigger):
  bot.say("https://actionsack.com/img/fuck/fuck!.gif")