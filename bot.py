import discord
from discord.ext import commands
import config
import logs_events as log_events
import ticket_system
from ticket_system import setup as setup_tickets
from embed_creator import EmbedModal
from embeds.aboutme_embed import create_aboutme_embed
from embeds.services_embed import create_services_embed
from embeds.projects_embed import create_project_embed

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("aky "), intents=intents)

# Register the ticket view
setup_tickets(bot)

@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} is now Online")
    
    try:
        bot.add_view(ticket_system.TicketView())
    except Exception as e:
        print(f"Error adding view: {e}")
    
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} command(s): {[cmd.name for cmd in synced]}")
    except Exception as e:
        print(f"❌ Slash command sync failed: {e}")

@bot.tree.command(name="embed", description="Create a custom embed")
async def embed_command(interaction: discord.Interaction):
    await interaction.response.send_modal(EmbedModal())

# Log events
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

@bot.command(name="support")
async def help_command(ctx):
    embed = create_help_embed()
    await ctx.send(embed=embed)

@bot.command(name="about_me")
async def aboutme_command(ctx):
    embed = create_aboutme_embed()
    await ctx.send(embed=embed)

@bot.command(name="services")
async def services_command(ctx):
    embed = create_services_embed()
    await ctx.send(embed=embed)

@bot.command(name="projects")
async def projects_command(ctx):
    embed = create_project_embed()
    await ctx.send(embed=embed)

bot.run(config.TOKEN)
