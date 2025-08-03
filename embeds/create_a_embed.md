import discord

def embed():
    embed = discord.Embed(
        title="",  # setTitle
        url="",  # setURL
        description="",  # setDescription
        color=0xFFFFFF  # setColor
    )

    # # setAuthor
    # embed.set_author(
    #     name="Author Name",
    #     icon_url="",
    #     url=""
    # )

    # setThumbnail
    embed.set_thumbnail(url="")

    # addFields
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="", value="@akiakyo", inline=True)
    embed.add_field(name="", value="@pretttboiakyo", inline=True)
    embed.add_field(name="", value="", inline=True)

    # setImage
    # embed.set_image(url="")

    # setTimestamp
    # embed.timestamp = discord.utils.utcnow()

    # setFooter
    # embed.set_footer(
    #     text="",
    #     icon_url=""
    # )

    return embed
