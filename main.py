from telethon import TelegramClient
import asyncio
import os
from datetime import datetime

TELEGRAM_API_KEY=os.environ.get("API_KEY")
TELEGRAM_API_HASH=os.environ.get("API_HASH")

time_id=-5120372402
time_message="Bom dia time!"
instancia_id=-5119706180
instanca_message="Bom dia instâncias!"
coord_id=-5131368441
coord_message="Bom dia meus caros!"
eex_id=-5243425224
eex_message="Bom dia meus senhores!"

async def main():
    dia=datetime.now().weekday()
    if dia<5:
        client = TelegramClient("bdmej",TELEGRAM_API_KEY,TELEGRAM_API_HASH)
        await client.start(phone="5547997892968")
        
        #teste = await client.get_entity("@Gabriel_WK04")
        #await client.send_message("me","Tu é cobaia para eu testar se programar o horario ta funcionando")
        
        
        time = await client.get_entity(time_id)
        await client.send_message(time,time_message)
        instancia = await client.get_entity(instancia_id)
        await client.send_message(instancia,instanca_message)
        coord = await client.get_entity(coord_id)
        await client.send_message(coord,coord_message)
        eex = await client.get_entity(eex_id)
        await client.send_message(eex,eex_message)
        
    
    return