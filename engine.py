import subprocess

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode().strip()
    except:
        return ""

def get_android_model():
    return run("adb shell getprop ro.product.model")

def get_ios_model():
    output = run("ideviceinfo")
    for line in output.split("\n"):
        if "ProductType" in line:
            return line.split(":")[1].strip()
    return None

def detect_device():
    model = get_android_model()
    if model:
        return {"type": "android", "model": model}

    model = get_ios_model()
    if model:
        return {"type": "iphone", "model": model}

    return {"type": "none", "model": None}

def identify_brand(model):
    if not model:
        return None
    if "SM-" in model:
        return "samsung"
    if "iPhone" in model:
        return "apple"
    return "mediatek"
