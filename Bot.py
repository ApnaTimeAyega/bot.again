import discord

import asyncio

import time

import colorsys

import random

from discord.ext import commands

client = commands.Bot(description="HeloMis", command_prefix="!!", pm_help = False) 

client.remove_command('help')

@client.event

async def on_ready():

    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')

    print('Created By AnDrOiD#3309')

    print('--------')

    print('Started AndroBot')

    return await client.change_presence(game=discord.Game(name='READY BUT TESTING'))

        

def is_owner(ctx):

    return ctx.message.author.id == "367230353993236480"

@client.command(pass_context=True)

async def ping(ctx): 

    await client.say("Hi Guys The Bot is STILL under developement After finish creating it i will add image of it")

@client.command(pass_context = True)

@commands.has_permissions(administrator=True) 

async def announce(ctx, channel: discord.Channel=None, *, msg: str):

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))

    await client.send_message(channel, embed=embed)

    await client.delete_message(ctx.message)

@client.command(pass_context = True)

async def meme(ctx):

    choices = ['https://img.memecdn.com/english_o_869587.webp', 'https://img.memecdn.com/everybody-knows-muricans-don-amp-039-t-speak-english-the-same-way-mexicans-don-amp-039-t-speak-spanish_c_7233205.webp', 'https://img.memecdn.com/english-reaction-when-they-heard-about-eu_c_6994013.webp', 'https://images3.memedroid.com/images/UPLOADED393/5b0c3ee92799f.jpeg' , 'https://images7.memedroid.com/images/UPLOADED850/5b0c2d7dd6049.jpeg', 'https://images7.memedroid.com/images/UPLOADED905/5b0c30c468fa8.jpeg', 'https://images7.memedroid.com/images/UPLOADED726/5b0c2d4c5f288.jpeg', 'https://images7.memedroid.com/images/UPLOADED936/5b0c2a90adbe7.jpeg', 'https://images7.memedroid.com/images/UPLOADED764/5b0c1e491c669.jpeg', 'https://images3.memedroid.com/images/UPLOADED922/5b0c284b71cd0.jpeg', 'https://images3.memedroid.com/images/UPLOADED207/5b0c265a58cf4.jpeg', 'https://images7.memedroid.com/images/UPLOADED920/5b0c06813741a.jpeg', 'https://images3.memedroid.com/images/UPLOADED46/5a91c871e61f1.jpeg', 'https://images7.memedroid.com/images/UPLOADED737/5a91c7f234bd2.jpeg', 'https://images7.memedroid.com/images/UPLOADED757/5a91bd39e1323.jpeg', 'https://images7.memedroid.com/images/UPLOADED963/5a91b4f7aba7e.jpeg', 'https://images7.memedroid.com/images/UPLOADED794/5a91ac0900506.jpeg', 'https://images3.memedroid.com/images/UPLOADED188/5a91aa326ad4e.jpeg']

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed = discord.Embed(title='Meme', description='For more memes check- https://www.memedroid.com', color = discord.Color((r << 16) + (g << 8) + b))

    embed.set_thumbnail(url='<www.youtube.com/') 

    embed.set_image(url = random.choice(choices))

    await client.send_typing(ctx.message.channel)

    await client.send_message(ctx.message.channel, embed=embed) 

    

@client.command(pass_context = True)

@commands.check(is_owner)

async def servers(ctx):

  servers = list(client.servers)

  await client.say(f"Connected on {str(len(servers))} servers:")

  await client.say('\n'.join(server.name for server in servers))

@client.command(pass_context = True)

async def help(ctx):

    author = ctx.message.author

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))

    embed.set_author(name='Help')

    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')

    embed.add_field(name = '``Our Help Server Link`` ',value ='https://discord.gg/vMvv5rr',inline = False)

    embed.add_field(name = '!!modhelp ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)

    embed.add_field(name = '!!generalhelp ',value ='Explaines all the commands which are usable by everyone.',inline = False)

    await client.send_message(author,embed=embed)

    await client.say('📨 Check DMs For Information')

    

@client.command(pass_context = True)

@commands.has_permissions(kick_members=True) 

async def mute(ctx, member: discord.Member=None, mutetime=None):

    if member is None:

        await client.say('Please specify member i.e. Mention a member to mute. Example-``!!mute @user <time in minutes>``')

        return

    if mutetime is None:

        await client.say('Please specify time i.e. Mention a member to mute with time. Example-``!!mute @user <time in minutes>``')

        return

    if member.server_permissions.kick_members:

        await client.say('**You cannot mute admin/moderator!**')

        return

    if ctx.message.author.bot:

      return

    else:

      mutetime =int(mutetime)

      mutetime = mutetime * 60

      output = mutetime/60

      role = discord.utils.get(member.server.roles, name='Muted')

      await client.add_roles(member, role)

      await client.say("Muted **{}**".format(member.name))

      await client.send_message(member, "You are muted by {0} for {1} Minutes".format(ctx.message.author, output))

      for channel in member.server.channels:

        if channel.name == '#official_log':

            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}** for {2} minutes!".format(member, ctx.message.author, output), color=0x37F60A)

            await client.send_message(channel, embed=embed)

            await asyncio.sleep(mutetime)

            await client.remove_roles(member, role)

            await client.say("Unmuted **{}**".format(member.name))

            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted!".format(member, ctx.message.author), color=0xFD1600)

            await client.send_message(channel, embed=embed)

            

            

@client.command(pass_context = True)

@commands.has_permissions(kick_members=True) 

async def unmute(ctx, member: discord.Member=None):

    if member is None:

      await client.say('Please specify member i.e. Mention a member to unmute. Example- ``!!unmute @user``')

    if ctx.message.author.bot:

      return

    else:

      role = discord.utils.get(member.server.roles, name='Muted')

      await client.remove_roles(member, role)

      await client.say("Unmuted **{}**".format(member))

      for channel in member.server.channels:

        if channel.name == 'official_log':

            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xFD1600)

            await client.send_message(channel, embed=embed)

            

@client.event

async def on_member_join(member):

    role = discord.utils.get(member.server.roles, name='Members')

    await client.add_roles(member, role)

    

client.run('NDM4NjI4NzY3MjgwMTM2MjAz.D2kxmQ.wN_ZrDeJ130Bs23U4DwEF4zYd4Y
