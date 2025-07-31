import discord
from discord.ext import commands

LOG_CHANNEL_ID = 1400563290979045376

async def send_log(guild: discord.Guild, embed: discord.Embed):
    channel = guild.get_channel(LOG_CHANNEL_ID)
    if channel:
        await channel.send(embed=embed)

# user joins
async def log_member_jon(member):
    embed = discord.Embed(
        title="📥 User Joins",
        description=f"{member.mention} (`{member}`)",
        color=discord.Color.green()
    )
    embed.add_field(name="User ID", value=str(member.id))
    embed.set_footer(text=f"Account Created: {member.created_at}")
    await send_log(member.guild, embed)

# message deleted
async def log_message_delete(message):
    if message.author.bot:
        return
    embed = discord.Embed(
        title="🗑️ Message Deleted",
        description=f"**Author:** {message.author.mention} in {message.channel.mention}",
        color=discord.Color.red()
    )
    embed.add_field(name="Content", value=message.content or "*Empty*", inline=False)
    await send_log(message.guild, embed)

# message modified
async def log_message_edit(before, after):
    if before.author.bot or before.content == after.content:
        return
    embed = discord.Embed(
        title="✏️ Message Modified",
        description=f"**Author:** {before.author.mention} in {before.channel.mention}",
        color=discord.Color.orange()
    )
    embed.add_field(name="Before", value=before.content or "*Empty*", inline=False)
    embed.add_field(name="After", value=after.content or "*Empty*", inline=False)
    await send_log(before.guild, embed)

# nickname modified
async def log_nickname_change(before, after):
    if before.nick != after.nick:
        embed = discord.Embed(
            title="🔄 Nickname Changed",
            description=f"**User:** {after.mention}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Before", value=before.nick or "*None*")
        embed.add_field(name="After", value=after.nick or "*None*")
        await send_log(after.guild, embed)