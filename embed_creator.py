import discord

class EmbedModal(discord.ui.Modal, title="Create a Custom Embed"):

    setTitle = discord.ui.TextInput(label="Title", required=False)
    setDescription = discord.ui.TextInput(label="Description", required=True, style=discord.TextStyle.paragraph)
    setColor = discord.ui.TextInput(label="Color (hex, e.g. #808080)", required=False, placeholder="#808080")
    setAuthor = discord.ui.TextInput(label="Author Name", required=False)
    setFooter = discord.ui.TextInput(label="Footer text", required=False)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            color_value = int(self.setColor.value.replace("#", "0x"), 16) if self.setColor.value else 0x808080
        except ValueError:
            color_value = 0x808080

        embed = discord.Embed(
            title=self.setTitle.value or None,
            description=self.setDescription.value,
            color=color_value
        )

        if self.setAuthor.value:
            embed.set_author(name=self.setAuthor.value)

        if self.setFooter.value:
            embed.set_footer(text=self.setFooter.value)

        await interaction.response.send_message(embed=embed)
