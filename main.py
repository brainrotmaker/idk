# main.py – FINAL BASE SCANNER + PRIVATE LINKS + AUTO-JOIN (Dec 2025)
import aiohttp
import asyncio
import random
import subprocess
import time
import logging
from datetime import datetime
from config import *
from alt_mgr import auto_join_and_inject
from webhook_sender import send_brainrot_found
from proxy_mgr import get_proxy

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='brainrot.log')

async def scan_private_link(session, link):
    try:
        code = link.split("privateServerLinkCode=")[1].split("&")[0]
        url = f"https://games.roblox.com/v1/games/{PLACE_ID}/private-servers?privateServerLinkCode={code}"
        proxy = await get_proxy()
        async with session.get(url, proxy=f"http://{proxy}" if proxy else None, timeout=10) as resp:
            if resp.status == 200:
                data = await resp.json()
                server = data.get("data", [{}])[0]
                if server and server.get("playing", 0) > 0:  # Only servers with players
                    return link
    except: pass
    return None

async def scanner():
    async with aiohttp.ClientSession() as session:
        while True:
            # 1. Brute private servers (for backup)
            tasks = []
            for _ in range(80):
                code = "".join(random.choices("0123456789abcdef", k=32))
                url = f"https://games.roblox.com/v1/games/{PLACE_ID}/private-servers?privateServerLinkCode={code}"
                task = session.get(url, proxy=f"http://{await get_proxy()}" if PROXIES else None, timeout=10)
                tasks.append((task, code))
            
            # 2. Check Discord for new private links (from your server)
            try:
                headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}
                async with session.get(f"https://discord.com/api/v10/channels/{DISCORD_CHANNEL_ID}/messages?limit=50", headers=headers) as resp:
                    if resp.status == 200:
                        msgs = await resp.json()
                        for msg in msgs:
                            if "privateServerLinkCode=" in msg["content"]:
                                link = msg["content"].split("https://")[1] if "https://" in msg["content"] else None
                                if link:
                                    tasks.append((session.get(f"https://www.roblox.com{link}"), None))
            except: pass

            for task, _ in tasks:
                try:
                    resp = await task
                    if resp.status == 200:
                        data = await resp.json()
                        server = data.get("data", [{}])[0]
                        if server and server.get("playing", 0) > 0:  # Has players = has base
                            link = f"https://www.roblox.com/games/{PLACE_ID}/?privateServerLinkCode={server['privateServerLinkCode']}"
                            auto_join_and_inject(link)
                            await send_brainrot_found(session, link)
                            logging.info(f"RAIDED BASE → {link}")
                except: pass
            await asyncio.sleep(25)

if __name__ == "__main__":
    print("BRAINROT BASE SCANNER v13 – SCANNING PEOPLE'S BASES (Dec 2025)")
    asyncio.run(scanner())
