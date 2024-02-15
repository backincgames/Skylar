import discord
import json

def LoadEmbedData(embedT):
  with open("embeds.json", "r") as json_file:
    data = json.load(json_file)
  embed = discord.Embed()
  
  # Embed creation
  if "title" in data[embedT]:
    embed.title = data[embedT]["title"]

  if "url" in data[embedT]:
    embed.url = data[embedT]["url"]

  if "description" in data[embedT]:
    embed.description = data[embedT]["description"]

  # Set the color of the embed using from_rgb()
  if "colour" in data[embedT]:
    embed.color = discord.Colour.purple()


  # Handle nested dictionaries in the JSON data for "author"
  if "author" in data[embedT]:
    author_data = data[embedT]["author"]
    embed.set_author(
      name=author_data.get("name", None),
      url=author_data.get("url", None),
      icon_url=author_data.get("icon_url", None)
    )

  # Handle "fields" in the JSON data
  if "fields" in data[embedT]:
    for field in data[embedT]["fields"]:
      embed.add_field(name=field["name"], value=field["value"], inline=field["inline"])

  # Handle "thumbnail" in the JSON data
  if "thumbnail" in data[embedT]:
    embed.set_thumbnail(url=data[embedT]["thumbnail"].get("url", None))

  # Handle "footer" in the JSON data
  if "footer" in data[embedT]:
    footer_data = data[embedT]["footer"]
    embed.set_footer(text=footer_data.get("text", None), icon_url=footer_data.get("icon_url", None))
  return embed
