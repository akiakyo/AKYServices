import discord

def create_services_embed():
    embed = discord.Embed(
        title="Services",  # setTitle
        url="https://akiakyo.github.io/",  # setURL
        description="These are the services that I offer ",  # setDescription
        color=0xFFFFFF  # setColor
    )

    # # setAuthor
    # embed.set_author(
    #     name="Author Name",
    #     icon_url="https://i.imgur.com/AfFp7pu.png",
    #     url="https://discord.com"
    # )

    # setThumbnail
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1386703646414209046/1401424618543124500/ChatGPT_Image_Aug_3_2025_11_52_42_AM.png?ex=689039e2&is=688ee862&hm=fdc074e5f4c14122a3f8505f36e061dd1efb275b478d6317aa3c9c146682d9cb&=&format=webp&quality=lossless&width=960&height=960")

    # addFields
    embed.add_field(name="Denizen Scripting", value="Automate Minecraft with custom scripts", inline=True)
    embed.add_field(name="Plugin Configuration", value="Perfect settings for every plugin", inline=True)
    embed.add_field(name="Paper Configuration", value="Optimize performance with Paper tweaks", inline=True)
    embed.add_field(name="Nexo Setups (Custom Models)", value="Install Nexo models with ease", inline=True)
    embed.add_field(name="Oraxen Setups (Custom Models)", value="Customize gameplay using Oraxen models", inline=True)
    embed.add_field(name="Discord Bot (Development)", value="Custom bots built for communities", inline=True)
    embed.add_field(name="Minecraft Server (Development)", value="I develop advanced Minecraft servers", inline=True)
    embed.add_field(name="Spark Reading", value="Analyze lag using Spark reports", inline=True)
    embed.add_field(name="LuckPerms (Permissions Management)", value="Manage permissions with LuckPerms easily", inline=True)

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
