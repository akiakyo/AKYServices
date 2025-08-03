import discord

def create_project_embed():
    embed = discord.Embed(
        title="Projects",  # setTitle
        url="https://akiakyo.github.io/#projects",  # setURL
        description="Projects are on my Porfolio Site: (https://akiakyo.github.io/)",  # setDescription
        color=0xFFFFFF  # setColor
    )
    # setThumbnail
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1386703646414209046/1401424618543124500/ChatGPT_Image_Aug_3_2025_11_52_42_AM.png?ex=689039e2&is=688ee862&hm=fdc074e5f4c14122a3f8505f36e061dd1efb275b478d6317aa3c9c146682d9cb&=&format=webp&quality=lossless&width=960&height=960")

    return embed
