# ticket_system.py

import discord
from discord.ext import commands
from discord import ui
from datetime import datetime
import os

TICKET_CATEGORY_ID = 1400572687591538790
SUPPORT_ROLE_ID = 1400557978943488061

class TicketModal(discord.ui.Modal):
    def __init__(self, title, fields, custom_id):
        super().__init__(title=title, custom_id=custom_id)
        self.fields_data = {}
        for field in fields:
            self.add_item(field)

    async def on_submit(self, interaction: discord.Interaction):
        self.fields_data = {item.label: item.value for item in self.children}
        username = interaction.user.name.lower().replace(" ", "-")
        guild = interaction.guild

        category = discord.utils.get(guild.categories, id=TICKET_CATEGORY_ID)
        channel = await guild.create_text_channel(
            name=f"ticket-{username}",
            category=category,
            topic=f"Ticket by {interaction.user}",
            overwrites={
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                guild.get_role(SUPPORT_ROLE_ID): discord.PermissionOverwrite(view_channel=True, send_messages=True)
            }
        )

        embed = discord.Embed(
            title="📉 New Support Ticket",
            description="\n".join([f"**{k}:** {v}" for k, v in self.fields_data.items()]),
            color=discord.Color.green(),
            timestamp=datetime.utcnow()
        )
        embed.set_author(name=interaction.user, icon_url=interaction.user.display_avatar.url)

        await channel.send(f"<@&{SUPPORT_ROLE_ID}>", embed=embed, view=CloseTicketView(ticket_owner=interaction.user, ticket_channel=channel, form_data=self.fields_data))
        await interaction.response.send_message(f"✅ Ticket created: {channel.mention}", ephemeral=True)

class CloseTicketView(discord.ui.View):
    def __init__(self, ticket_owner: discord.User, ticket_channel: discord.TextChannel, form_data: dict):
        super().__init__(timeout=None)
        self.ticket_owner = ticket_owner
        self.ticket_channel = ticket_channel
        self.form_data = form_data

    @discord.ui.button(label="Close Ticket", style=discord.ButtonStyle.danger)
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = self.ticket_channel
        messages = [message async for message in channel.history(limit=100)]

        conversation = ""
        for msg in reversed(messages):
            if msg.author.bot:
                continue
            timestamp = msg.created_at.strftime('%Y-%m-%d %H:%M:%S')
            conversation += f"[{timestamp}] {msg.author}: {msg.content}\n"

        embed = discord.Embed(
            title="📁 Support Ticket Closed",
            color=discord.Color.orange(),
            timestamp=datetime.utcnow()
        )
        embed.add_field(name="Client Name", value=self.form_data.get("Client Name", "N/A"), inline=False)
        embed.add_field(name="Service", value=self.form_data.get("Service", self.form_data.get("Concern", "N/A")), inline=False)
        embed.add_field(name="Date", value=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'), inline=False)
        embed.add_field(name="Transcript", value=f"```\n{conversation or 'No messages recorded.'}```", inline=False)
        embed.set_footer(text=f"Closed by {interaction.user}", icon_url=interaction.user.display_avatar.url)

        await channel.send(embed=embed)

        try:
            await self.ticket_owner.send(embed=embed)
        except discord.Forbidden:
            await channel.send(f"❌ Couldn't DM {self.ticket_owner.mention} the transcript.")

        await channel.delete()

class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        # Add a link button manually
        self.add_item(discord.ui.Button(
            label="🔗akiakyo.github.io",
            style=discord.ButtonStyle.link,
            url="https://akiakyo.github.io"
        ))

    @discord.ui.button(label="Hire Me", style=discord.ButtonStyle.primary, custom_id="hire_me")
    async def hire_me(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = TicketModal(
            title="Hire Me",
            custom_id="hire_modal",
            fields=[
                ui.TextInput(label="Client Name", required=True),
                ui.TextInput(label="Service", required=True, placeholder="(eg. Minecraft Development, Discord Bot Development etc.)"),
                ui.TextInput(label="Tell me more", required=True, style=discord.TextStyle.paragraph),
            ]
        )
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="Concerns / Issues", style=discord.ButtonStyle.secondary, custom_id="concerns")
    async def concerns(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = TicketModal(
            title="Concern / Issues",
            custom_id="concerns_modal",
            fields=[
                ui.TextInput(label="Client Name", required=True),
                ui.TextInput(label="Concern", required=True, style=discord.TextStyle.paragraph),
                # Removed invalid link field
            ]
        )
        await interaction.response.send_modal(modal)


def setup(bot: commands.Bot):
    @bot.command()
    async def ticket(ctx):
        """Sends the ticket system buttons."""
        view = TicketView()
        embed = discord.Embed(
            title="📬 Need help or want to hire?",
            description="Click a button below to create a ticket.",
            color=0x2F3136
        )
        await ctx.send(embed=embed, view=view)
