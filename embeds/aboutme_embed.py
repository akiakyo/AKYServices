import discord

def create_aboutme_embed():
    embed = discord.Embed(
        title="Hello, I'm aky | Minecraft Dev | Discord Bot Dev",  # setTitle
        url="https://akiakyo.github.io/",  # setURL
        description="Enthusiastic about building cool things for Minecraft server and Discord bots",  # setDescription
        color=0xFFFFFF  # setColor
    )

    # # setAuthor
    # embed.set_author(
    #     name="Author Name",
    #     icon_url="https://i.imgur.com/AfFp7pu.png",
    #     url="https://discord.com"
    # )

    # setThumbnail
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1386703646414209046/1401421265985863700/profile.png?ex=689036c2&is=688ee542&hm=93e78e7d5ad7c501242e78cbb8390750508b9b899583cf1ce22012d091e944bc&=&format=webp&quality=lossless&width=350&height=350")

    # addFields
    embed.add_field(name="About Me", value="I’m a minecraft developer & discord bot developer with experience building things for minecraft servers and discord bots.", inline=False)
    embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.add_field(name="Discord", value="@akiakyo", inline=True)
    embed.add_field(name="Instagram", value="@pretttboiakyo", inline=True)
    embed.add_field(name="Email", value="aquiokenzie37@gmail.com", inline=True)

    # setImage
    # embed.set_image(url="https://i.imgur.com/AfFp7pu.png")

    # setTimestamp
    # embed.timestamp = discord.utils.utcnow()

    # setFooter
    # embed.set_footer(
    #     text="Some footer text here",
    #     icon_url="https://i.imgur.com/AfFp7pu.png"
    # )

    return embed
