# Import Discord Package
import discord

# Client (our bot)
client = discord.Client()


@client.event
async def on_ready():
    # DO STUFF....
    general_channel = client.get_channel(954399483943329872)
    await general_channel.send('Hi')


@client.event
async def on_disconnect():
    general_channel = client.get_channel(954399483943329872)
    await general_channel.send('Goodbye')


@client.event
async def on_message(message):

    if message.content == '!version':

        general_channel = client.get_channel(954399483943329872)

        myEmbed = discord.Embed(
            title="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released",
                          value="March 19th, 2022", inline=False)
        myEmbed.set_footer(text="This is a sample footer")
        myEmbed.set_author(name="Koala Boy")

        await general_channel.send(embed=myEmbed)

        await client.pcoress_commands(message)


# Run the client on the server
client.run('OTU0Mzk5NDgzOTQzMzI5ODcy.YjSjyA.lssAB6-N7rhNeY8aRJSIzpYRJpc')
