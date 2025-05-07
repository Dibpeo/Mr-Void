import discord
import json

with json.load("TOKEN.json", "r") as localToken:
    TOKEN = json.load(localToken)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

admin_id = 1302049373294821406

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event  

async def on_message(message):
    
    user_id = message.author.id
    
    if message.author == client.user:
        return

#---SubCommand Test Command
    if message.content.startswith('$role'):
        dividedArgs = message.content.split()
        
        if len(dividedArgs) < 2:
            await message.channel.send('No Subcommand entered.\n Try --list')
            return
        subcommand = dividedArgs[1].lower()
        
        if subcommand == "--list":
            await message.channel.send('Roles:')

    if message.content.startswith('$adminTest'):
        if user_id == admin_id:
            await message.channel.send('You are an admin!')
        else:
            await message.channel.send('You are not an admin...')
    if message.content.startswith('$userBotTest'):
        await message.channel.send('Bot Functional')

    if message.content.startswith('$checkSave'):
        await message.channel.send('Functionality not implemented yet.')
    if message.content.startswith('$sendDM'):
        await message.author.send('Hello! I am currently under testing!')
        await message.channel.send(f'I have sent a dm! {message.author.mention}')
client.run(TOKEN)
