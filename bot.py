import discord
from discord.ext import commands
import config
import logs_events as log_events
import ticket_system
from ticket_system import setup as setup_tickets
from embed_creator import EmbedModal
from embeds.aky_embeds import create_aboutme_embed, create_project_embed, create_services_embed, AboutMeView

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("aky "), intents=intents)

# Events
@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} is now Online")

    try:
        bot.add_view(ticket_system.TicketView())
    except Exception as e:
        print(f"❌ Error adding ticket view: {e}")

    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} command(s): {[cmd.name for cmd in synced]}")
    except Exception as e:
        print(f"❌ Slash command sync failed: {e}")

# Modal Embed Slash Command
@bot.tree.command(name="embed", description="Create a custom embed")
async def embed_command(interaction: discord.Interaction):
    await interaction.response.send_modal(EmbedModal())

# Logging Events
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

# Classic Text Commands
@bot.command(name="about_me")
async def aboutme_command(ctx):
    embed = create_aboutme_embed()
    view = AboutMeView()
    await ctx.send(embed=embed, view=view)

@bot.command(name="services")
async def services_command(ctx):
    embed = create_services_embed()
    await ctx.send(embed=embed)

@bot.command(name="projects")
async def projects_command(ctx):
    embed = create_project_embed()
    await ctx.send(embed=embed)

# Main startup
async def main():
    async with bot:
        try:
            await bot.load_extension("cogs.reaction_roles")
            print("✅ Loaded cogs.reaction_roles")
        except Exception as e:
            print(f"❌ Failed to load reaction_roles cog: {e}")

        try:
            await bot.load_extension("minecraftServers.magbungkal_net")
            print("✅ Loaded MagbungkalStatus cog")
        except Exception as e:
            print(f"❌ Failed to load MagbungkalStatus cog: {e}")

        # Setup ticket system
        setup_tickets(bot)

        await bot.start(config.TOKEN)

# Run
import asyncio
asyncio.run(main())
