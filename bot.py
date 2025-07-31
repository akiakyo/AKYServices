import discord
from discord.ext import commands
import config
import logs_events as log_events
import ticket_system
from ticket_system import setup as setup_tickets

# AKY Services command is "aky"
intents = discord.Intents.all()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("aky "), intents=intents)

# Register ticket system
setup_tickets(bot)

@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} is now Online")
    bot.add_view(ticket_system.TicketView())

# You had this twice — remove the duplicate
@bot.event
async def on_member_join(member):
    await log_events.log_member_join(member)

@bot.event
async def on_message_delete(message):
    await log_events.log_message_delete(message)

@bot.event
async def on_message_edit(before, after):
    await log_events.log_message_edit(before, after)

@bot.event
async def on_member_update(before, after):
    await log_events.log_nickname_change(before, after)

@bot.command()
async def test(ctx):
    await ctx.send(f"{bot.user.mention} is working")  # Fix: f-string wasn't properly used

bot.run(config.TOKEN)
