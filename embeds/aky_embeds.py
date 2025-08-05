import discord

class AboutMeView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(
            label="🔗akiakyo.github.io",
            style=discord.ButtonStyle.link,
            url="https://akiakyo.github.io"
        ))

def create_aboutme_embed():
    embed = discord.Embed(
        title="Hello, I'm aky | Minecraft Dev | Discord Bot Dev",  # setTitle
        url="https://akiakyo.github.io/",  # setURL
        description="Enthusiastic about building cool things for Minecraft server and Discord bots",  # setDescription
        color=0xFFFFFF  # setColor
    )

    # setThumbnail
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1386703646414209046/1401421265985863700/profile.png?ex=689036c2&is=688ee542&hm=93e78e7d5ad7c501242e78cbb8390750508b9b899583cf1ce22012d091e944bc&=&format=webp&quality=lossless&width=350&height=350")

    # addFields
    embed.add_field(name="About Me", value="I’m a minecraft developer & discord bot developer with experience building things for minecraft servers and discord bots.", inline=False)
    embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.add_field(name="Discord", value="@akiakyo", inline=True)
    embed.add_field(name="Instagram", value="@pretttboiakyo", inline=True)
    embed.add_field(name="Email", value="aquiokenzie37@gmail.com", inline=True)

    return embed

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

def create_services_embed():
    embed = discord.Embed(
        title="Services",  # setTitle
        url="https://akiakyo.github.io/",  # setURL
        description="These are the services that I offer ",  # setDescription
        color=0xFFFFFF  # setColor
    )

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

    return embed