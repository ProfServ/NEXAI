import subprocess

def flash_samsung():
    print("[*] Flash Samsung (Heimdall)")
    subprocess.call([
        "heimdall", "detect"
    ])

def flash_mediatek():
    print("[*] Launch SP Flash Tool (manual)")
    subprocess.Popen(["./tools/spflash/flash_tool"])

def restore_iphone():
    print("[*] Restore iPhone")
    subprocess.call([
        "idevicerestore", "-e"
    ])
