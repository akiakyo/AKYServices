import discord
from discord.ext import commands

# Constants
ROLES_CHANNEL = 1402350416225898567
AKY_DISCORD = 1386703644853932083
ANNOUNCEMENT_PING = 1402356238519373995
EMERGENCY_PING = 1402356273114120264
CRITICAL_PING = 1402356307767591023

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setup_reaction_roles")
    async def setup_reaction_roles(self, ctx):
        guild = ctx.guild
        channel = guild.get_channel(ROLES_CHANNEL)

        if channel is None:
            await ctx.send("❌ I couldn't find the roles channel. Please check the channel ID or permissions.")
            return

        try:
            embed = discord.Embed(
                title="Choose Your Notifications",
                description="React to get a role:\n\n🔔 - Announcement Ping\n⛑️ - Emergency Ping\n‼️ - Critical Ping",
                color=0x2F3136
            )
            message = await channel.send(embed=embed)

            emojis = {
                "🔔": ANNOUNCEMENT_PING,
                "⛑️": EMERGENCY_PING,
                "‼️": CRITICAL_PING,
            }

            for emoji in emojis:
                await message.add_reaction(emoji)

            await ctx.send(f"✅ Reaction roles message successfully sent in {channel.mention}!")

        except Exception as e:
            await ctx.send(f"❌ Something went wrong: `{e}`")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.guild_id != AKY_DISCORD or payload.channel_id != ROLES_CHANNEL:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return

        try:
            member = await guild.fetch_member(payload.user_id)
        except discord.NotFound:
            return

        emoji = str(payload.emoji)
        print(f"[REACTION ADD] Emoji used: {emoji}")

        role_map = {
            "🔔": ANNOUNCEMENT_PING,
            "⛑️": EMERGENCY_PING,
            "‼️": CRITICAL_PING,
        }

        role_id = role_map.get(emoji)
        if role_id:
            role = guild.get_role(role_id)
            if role and member:
                try:
                    await member.add_roles(role, reason="Reaction role added")
                    print(f"✅ Added role '{role.name}' to {member.display_name}")

                    # Send embed to user
                    embed = discord.Embed(
                        title="✅ Role Added",
                        description=f"You've been given the **{role.name}** role!",
                        color=0x00FF00
                    )
                    await member.send(embed=embed)

                except Exception as e:
                    print(f"❌ Failed to add role: {e}")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.guild_id != AKY_DISCORD or payload.channel_id != ROLES_CHANNEL:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return

        try:
            member = await guild.fetch_member(payload.user_id)
        except discord.NotFound:
            return

        emoji = str(payload.emoji)
        print(f"[REACTION REMOVE] Emoji used: {emoji}")

        role_map = {
            "🔔": ANNOUNCEMENT_PING,
            "⛑️": EMERGENCY_PING,
            "‼️": CRITICAL_PING,
        }

        role_id = role_map.get(emoji)
        if role_id:
            role = guild.get_role(role_id)
            if role and member:
                try:
                    await member.remove_roles(role, reason="Reaction role removed")
                    print(f"🗑️ Removed role '{role.name}' from {member.display_name}")

                    # Send embed to user
                    embed = discord.Embed(
                        title="🗑️ Role Removed",
                        description=f"The **{role.name}** role has been removed from you.",
                        color=0xFF0000
                    )
                    await member.send(embed=embed)

                except Exception as e:
                    print(f"❌ Failed to remove role: {e}")

# Required for loading as a cog
async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))
