# alt_mgr.py – Auto-join 12 alts instantly (Xeno compatible)
import subprocess
import time
import random
import os

def auto_join_alts(link):
    try:
        with open("alts.txt", "r") as f:
            all_alts = [line.strip() for line in f if ":" in line]
    except:
        print("alts.txt not found!")
        return

    selected = random.sample(all_alts, min(12, len(all_alts)))
    for alt in selected:
        try:
            user, pw = alt.split(":")
            # Launch Roblox with alt cookie
            subprocess.Popen([
                "RobloxPlayerBeta.exe", "--app",
                f"-a \"{link}\"",
                "--cookie", f".ROBLOSECURITY={pw}"
            ])
            print(f"Auto-joined with {user}")
            time.sleep(2.5)  # Stagger to avoid detection
        except Exception as e:
            print(f"Alt failed: {e}")
