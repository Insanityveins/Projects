import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from random import randint

TOKEN = [token removed]
description = """Jah\'s totally cool, awesome custom build bot."""
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', description=description, intents=intents)


# how to make slash commands:
# https://stackoverflow.com/questions/72908362/how-to-convert-discord-bot-commands-to-hybrid-command

class TimeConversion(commands.Converter):
    #  converts given time and unit to seconds
    async def convert(self, ctx, argument):
        units = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400
        }

        length = int(argument[:-1])  # up to last index of the string
        unit = argument[-1]  # last index of string

        return length * units[unit]


@bot.command()
async def sync(ctx: commands.Context):
    if str(ctx.author) != "<insert tag>":
        return

    if ctx.channel.id != 668928426903601153:
        return

    try:
        synced = await bot.tree.sync()
        await ctx.send(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(e)


@bot.command()
async def timer(ctx, time: TimeConversion, *, message=None):
    await ctx.send("Timer set.")
    await asyncio.sleep(time)
    if message is None:
        await ctx.send(f"{ctx.author.mention}, your timer has ended.")
    else:
        await ctx.send(f"{ctx.author.mention}, your timer has ended. Remember,  \"{message}\".")
        # two spaces needed after remember for some reason


@bot.hybrid_command(name="flip", with_app_command=True)
async def flip(ctx):
    if randint(0, 1) == 0:
        await ctx.send("Heads.")
    else:
        await ctx.send("Tails.")


@bot.command(aliases=['avatar'])
async def avi(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
    avatar = user.avatar
    await ctx.send(avatar)


@bot.hybrid_command(name='random', with_app_command=True)
async def random(ctx):
    num = randint(0, 100)
    user = ctx.author.name
    await ctx.send(f"{user} rolled a {num}.")


@bot.command()
async def talk(ctx, channel_id: int, *, arg):
    # sends a message to the provided channel
    if str(ctx.author) != <insert tag>:
        await ctx.send("I don't fw you")
    else:
        channel = bot.get_channel(channel_id)
        await channel.send(arg)


@bot.hybrid_command(name="height_check", with_app_command=True)
async def height_check(ctx, *, member: discord.Member = None):
    length = randint(1, 12)
    if member is None:
        await ctx.send(f"{ctx.author.name} is {length} inches tall!")
    else:
        await ctx.send(f"{member.name} is {length} tall!")


@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    guild = member.guild
    if after.channel is not None:
        # create a new voice channel in the stream vcs
        # and move the user that created it to the voice channel
        if after.channel.name == 'stream queue':
            category = get(guild.categories, name='stream vcs')  # name of category to place channel in
            voiceChannelName = f"{member.name} stream"
            vc = await guild.create_voice_channel(voiceChannelName, category=category)
            await member.move_to(vc)

        # method to delete empty stream channel when users move to another vc
        # since if the people moved to another channel it wouldn't
        # delete the channel
        if before.channel is not None:
            if before.channel.category == get(guild.categories, name='stream vcs'):
                if not before.channel.members:
                    await before.channel.delete()

    # method to delete empty stream channels when everyone disconnects from channel
    elif before.channel is not None:
        if before.channel.category == get(guild.categories, name='stream vcs'):
            if not before.channel.members:
                await before.channel.delete()


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    #  allows commands to still be run
    await bot.process_commands(message)


bot.run(TOKEN)
