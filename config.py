# config.py – FULL BRAINROT LIST + SETTINGS (Dec 2025)
WEBHOOK_URL = "https://discord.com/api/webhooks/1447027171401928825/JsF4HEaG3DB6SB8NVdKaEJdNJEIEklLR-_BIh4qryw-DwYTDPtV1AViBX5E8yGQoGoC5"
DISCORD_TOKEN = "MTQ0NzAyNzU4NjYwODc5NTcyOQ.GzdabD.YDOiEyBEo4hBWQ83-ec-vHsKreoOlQ_rOPY_tI"
DISCORD_CHANNEL_ID = "1447043030916927510"  # Channel where people post private links
PLACE_ID = "109983668079237"
NUM_ALTS = 10

# ALL 30+ BRAINROTS (Secrets/OGs + High God – Dec 2025)
TARGET_BRAINROTS = [
    "DragonCannelloni", "FestiveDragonCannelloni", "StrawberryElephant", "LaVaccaSaturnoSaturnita",
    "SantaLaVacca", "LosTralaleritos", "Meowl", "SmurfCat", "HeadlessHorseman", "NuclearoDinossauro",
    "TungTungTungSahur", "HoHoHoSahur", "LosHotspotsitos", "KingsColeslaw", "SpaghettiTualetti",
    "LaGrandeCombinasion", "LaSupremeCombinasion", "LosOrcalitos", "LosSpyderini", "PopPopPopSahur",
    "PiccioneMacchina", "UnclitoSamito", "TipiTopiTaco", "TartarugaCisterna", "CocofantoElefanto",
    "TobTobiTobi", "TeTeTeSahur", "BulbitoBanditoTraktorito", "GummyBearTrap", "LosMatteos"
]

# Load alts & proxies
with open("alts.txt") as f:
    ALTS = [line.strip() for line in f if ":" in line]
with open("proxies.txt") as f:
    PROXIES = [line.strip() for line in f if line.strip()]
