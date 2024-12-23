import discord
from discord.ext import commands
from config import VERSION

class Bot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix="!", intents=discord.Intents.all(), description=f"Zingbot v{VERSION} by @matezzi75.", help_command=None)

#==================== COLOURS & INFOS ===================
BOT_EMBED_RGB = discord.Colour.from_rgb(77, 225, 222)

#======================== EMBEDS ========================
class BotEmbed(discord.Embed):
    def __init__(self, *, colour=BOT_EMBED_RGB, color=BOT_EMBED_RGB, title="TITLE", type='rich', url=None, description=None, timestamp=None):
        super().__init__(
            colour=colour,
            color=color,
            title=title,
            type=type,
            url=url,
            description=description,
            timestamp=timestamp)
        self.set_footer(text=f"Zingbot v{VERSION} by @matezzi75", icon_url="https://avatars.githubusercontent.com/u/146573782?s=400&u=a8b68f52dded16bbbb8b9dcce5004aff0a092b8c&v=4")