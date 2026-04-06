import requests, os

# TEMP test links (replace later with real firmware)
FIRMWARE_DB = {
    "SM-A205U": {
        "url": "https://speed.hetzner.de/100MB.bin"
    },
    "iPhone10,6": {
        "url": "https://speed.hetzner.de/100MB.bin"
    }
}

def download(url, path):
    r = requests.get(url)
    with open(path, "wb") as f:
        f.write(r.content)
    return path

def get_firmware(model):
    if model not in FIRMWARE_DB:
        return None

    os.makedirs("firmware", exist_ok=True)
    path = f"firmware/{model}.bin"

    print(f"[+] Downloading firmware for {model}")
    return download(FIRMWARE_DB[model]["url"], path)
