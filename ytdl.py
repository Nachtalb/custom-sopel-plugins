from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module
import os
import youtube_dl


ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4",
    "noplaylist": True,
    "forcejson": True,
    "outtmpl": "/mnt/media/ShareX/Screenshots/temp/%(title)s.%(ext)s"
}


@module.commands("ytdl")
def ytdl(bot, trigger):
    """Uses youtube-dl to download a video and post it to chat."""
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(trigger.group(3), download=False)
            title = meta["title"].replace(" ", "%20")
            ext = meta["ext"]
            ydl.download([trigger.group(3)])
            bot.say("https://actionsack.com/tmp/{}.{}".format(title, ext))
    except youtube_dl.utils.DownloadError:
        bot.say("Please submit a valid link.")
