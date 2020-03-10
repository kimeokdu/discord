import requests
import discord
import asyncio
import os
from json import loads

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("==========")
    game = discord.Game("$명령어")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "mongzi"
    name = "김설하"
    channel = client.get_channel(686968682219438126)
    a = 0
    while True:
        headers = {'Client-ID': 'vzk5u694hx7zfrm0sikibgnu7a71pv'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(name + "님이 방송중입니다.")
                a = 1
        except:
            a = 0
        await asyncio.sleep(60)


@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "$덕배":
        await message.channel.send("덕배님은 국산 A++ 돼지공주님입니다")
    if message.content == "$명령어":
            await message.channel.send("```$덕배  덕배 놀리기 전용 명령어                                               $충성  모두에게 충성충성                                               $놀아줘  심심할때 치는 명령어                                               $메이드 _ 메이드를 부르는 명령어                                               $좋은아침 _ 아침인사를 하는 명령어                                               $일정 _ 하루 일정을 보는 명령어                                               $선생님 _ 남궁필협 선생님을 호출하는 명령어                                               $5252 _ 한번 해보라구~ ```")
    if message.content == "$충성":
            await message.channel.send("충성충성~ ^^7")
    if message.content == "$놀아줘":
                await message.channel.send("어쩌라고^^")
    if message.content == "$메이드":
        await message.channel.send("하잇 고슈진사마~")
    if message.content == "$좋은아침":
        await message.channel.send("하잇 고슈진사마~ 좋은 아침입니다~")
    if message.content == "$일정":
            await message.channel.send("오늘은 가볍게 벤치프레스 300회만 하시면 됩니다^^")
    if message.content == "$5252":
        await message.channel.send("에엣~? 와타시..?///")
    if message.content == "$선생님":
        await message.channel.send("<@266128710908903425> 선생님!!! 빨리 오세요!!!")
        
        
access_token = os.environ["BOT_TOKEN"]
client.run("access_token")
