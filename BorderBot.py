#!/usr/bin/env python
# coding: utf-8

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord_components import Button


from PIL import Image
import urllib.request

import config
import os
from youtube_client import YouTubeClient

#login
bot = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name)
    print("ID: " + str(bot.user.id))
    print('------')

@bot.command(aliases=['b','thumbnail'], name="border",description="Creates a border around your inputted thumbnail")
async def border(ctx):
    message = ctx.message.content
    video_id = (message.split("/video/")[1].split("/")[0] if message.split("/video/")[0] != message else message.split("/shorts/")[1].split("/")[0] if message.split("/shorts/")[0] != message else message.split("/watch?v=")[1] if message.split("/watch?v=")[0] != message else message.split(".be/")[1] if message.split(".be/")[0] != message else "ERROR")
    if video_id == "ERROR":
        await ctx.send("Invalid URL")
    else:
        img_link = "https://i1.ytimg.com/vi/" + video_id + "/maxresdefault.jpg"
        urllib.request.urlretrieve(
            img_link,
            "original_thumbnail.png"
        )
        img = Image.open("original_thumbnail.png")
        border_img = Image.open("border.png")
        # crop the img to the size of border.png
        img = img.crop((((img.width/2) - (border_img.width/2)), 0, ((img.width/2) + (border_img.width/2)), img.height))
        # resize by a percent
        # img = img.resize((int(img.width*99), int(img.height*99)))
        img.paste(border_img, (0, 0), border_img)
        # save the image
        img.save("thumbnail_"+video_id+".png")
        # send the image
        await ctx.send(file=discord.File("thumbnail_"+video_id+".png"))

        await ctx.send(components=[Button(label="Set This As Thumbnail?",style="3")])

@bot.event
async def on_button_click(interaction):
    youtube_client = YouTubeClient('./client_secret.json')
    await ctx.send(youtube_client.get_video_info(video_id))
    response = youtube_client.set_thumbnail(video_id, thumbnail)
    await interaction.response("Thumbnail Set!")

bot.run(config.token)