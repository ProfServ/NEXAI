from engine import detect_device, identify_brand
from downloader import get_firmware
from flasher import flash_samsung, flash_mediatek, restore_iphone

def run():
    device = detect_device()
    model = device["model"]

    print("Detected:", model)

    if not model:
        print("No device connected")
        return

    brand = identify_brand(model)
    fw = get_firmware(model)

    print("Firmware:", fw)

    if brand == "samsung":
        flash_samsung()
    elif brand == "apple":
        restore_iphone()
    else:
        flash_mediatek()

if __name__ == "__main__":
    run()
