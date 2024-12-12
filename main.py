import discord
from config import TOKEN, SERVERS, PUBLIC_CHANNEL_ID
from classes import Bot, BotEmbed

bot = Bot()

#################### BASICS ####################

@bot.event
async def on_ready() -> None:
	print("\nZingbot connected and ready to Rock n' Roll!\n")

@bot.slash_command(guild_ids=SERVERS, name="ping", description="PONG !")
async def ping(interaction: discord.Interaction) -> None:
	print(f"COMMAND : /ping used by @{interaction.user.name} in {interaction.guild.name} (#{interaction.channel.name})")
	await interaction.response.send_message(embed=BotEmbed(title="PONG !", colour=discord.Colour.green()).remove_footer(), ephemeral=True)

##################### CORE #####################

@bot.slash_command(guild_ids=SERVERS, name="public_dr", description="Send a message in the public channel")
async def public_dr(interaction: discord.Interaction, message: str) -> None:
	print(f"COMMAND : /public_dr used by @{interaction.user.name} in {interaction.guild.name} (#{interaction.channel.name})")
	public_channel = interaction.guild.get_channel(PUBLIC_CHANNEL_ID)
	await public_channel.send(embed=BotEmbed(title="PUBLIC DIARY ROOM <:PUBLICDR:1267682346925035540>", description=f"{interaction.user.mention} <a:BLUEALERT:1267593451059413002>").add_field(name="Message :", value=f"{message}", inline=False))
	return await interaction.response.send_message(embed=BotEmbed(title="MESSAGE SENT", description="Your message has been successfully sent to the public channel.", colour=discord.Colour.green()).add_field(name="Your message :", value=f"{message}", inline=False))

@bot.message_command(guild_ids=SERVERS, name="Send to Diary Room")
async def send_to_dr(interaction: discord.Interaction, message: discord.Message) -> None:
	print(f"MESSAGE COMMAND : /send_to_dr used by {interaction.user.name} in {interaction.guild.name} (#{interaction.channel.name})")
	embed = BotEmbed(title="PUBLIC DIARY ROOM <:PUBLICDR:1267682346925035540>", description=f"{interaction.user.mention} <a:BLUEALERT:1267593451059413002>").add_field(name="Message :", value=f"{message.content}")
	public_channel = interaction.guild.get_channel(PUBLIC_CHANNEL_ID)
	await public_channel.send(embed=embed)
	return await interaction.response.send_message(embed=BotEmbed(title="MESSAGE SENT", description="Your message has been successfully sent to the public channel.", colour=discord.Colour.green()).add_field(name="Your message :", value=f"{message.content}", inline=False))

bot.run(TOKEN)