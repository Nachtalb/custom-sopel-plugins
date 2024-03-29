# custom-sopel-plugins

These are some [Sopel](https://github.com/sopel-irc/sopel) plugins I've written. While `custom.py` is very, very specific to my chat, the rest are pretty generic and a great addition to any IRC channel.

## [8ball.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/8ball.py)
Just a standard, run-of-the-mill [magic 8-ball](https://en.wikipedia.org/wiki/Magic_8-Ball). Never lies.

## [animals.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/animals.py)
Posts random animal pics from several different APIs.

## [base64coder.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/base64coder.py)
Encode or decode base64 data.

## [colors.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/colors.py)
Moved from [sopel-color-text](https://github.com/xnaas/sopel-color-text) — don't want to actually deal with publishing to pypi in the future.

## custom.py
Custom commands for [Action Sack](https://actionsack.com)'s Sopel bot. Many of these are highly inappropriate.

## [dadjokes.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/dadjokes.py)
Uses the [icanhazdadjoke API](https://icanhazdadjoke.com/api) to post dad jokes.

## [img.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/img.py)
Image searching with [DuckDuckGo Instant Answers API](https://duckduckgo.com/api) and [Google CSE](https://programmablesearchengine.google.com/about/).

## [insult.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/insult.py)
Uses the [Evil Insult Generator](https://evilinsult.com/api/) to insult other users.

## [isbn.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/isbn.py)
Uses the [Open Library Books API](https://openlibrary.org/dev/docs/api/books) to look up a book via ISBN.

## [nsfw.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/nsfw.py)
RNG of NSFW things.

## [random-apis.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/random-apis.py)
Adds some random APIs for fun.

## [smite_vgs.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/smite_vgs.py)
Adds [Smite's VGS](https://smite.gamepedia.com/Voice_Guided_System) to Sopel.

## [yourmom.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/yourmom.py)
Posts a random joke from [yourmom.txt](https://github.com/xnaas/custom-sopel-plugins/blob/master/yourmom.txt).

## [ytdl.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/ytdl.py)
Uses [youtube-dl](https://youtube-dl.org/) to download and share a video. Would require editing to be useful to anyone else.

---

### Deprecated Plugins

These plugins are deprecated and no longer used or updated.

#### [imgur.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/deprecated/imgur.py)
This was abandoned because the Imgur API isn't great for this purpose.

Use [img.py](https://github.com/xnaas/custom-sopel-plugins/blob/master/img.py) instead.

Used the [Imgur API](https://apidocs.imgur.com/) to post image results to chat.
