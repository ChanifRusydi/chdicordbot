import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

class music(commands.music):
    def __init__(self,bot):
        self.bot=bot

        self.is_play=False