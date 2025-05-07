import discord
import json
import os

folder_name = "UserData"
current_directory = os.getcwd()
folder_path = os.path.join(current_directory, folder_name)

os.makedirs(folder_path, exist_ok=True)

with open("TOKEN.json", "r") as localToken:
    TOKEN = json.load(localToken)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

GameData = {
    "MaxHealth": 20,
    "Health": 20,
    "MaxAttack": 5,
    "MinAttack": 1,
    "Defense": 3}
admin_id = 0

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event  

async def on_message(message):
    
    user_id = message.author.id
    user_mention = message.author.mention
    
    if message.author == client.user:
        return

# List of commands below

    if message.content.startswith("$join"):
        if message.channel.id == 1369422305192837120:
            filename = os.path.join(folder_path, f"{user_id}.json")
            if os.path.exists(filename):
                await message.channel.send(f"You have already joined, {user_mention}")
            else:
                with open(filename, "w") as saveToFile:
                    json.dump(GameData, saveToFile)
                    print("User Data Written")
                await message.channel.send(f"You have now joined the RPG, {user_mention}")
client.run(TOKEN)
