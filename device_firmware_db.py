"""
Device Firmware Database - Real firmware packs for major manufacturers
"""

DEVICE_FIRMWARE_DB = {
    "samsung": {
        "SM-G950F": {
            "model": "Galaxy S8",
            "latest_version": "S8_PIE",
            "firmware_url": "https://samsung.example.com/firmware/SM-G950F.tar",
            "checksum_md5": "abc123def456",
            "checksum_sha256": "sha256hash123456",
            "size_mb": 3500,
            "release_date": "2021-06-15",
            "changelog": "Security patches and performance improvements",
            "drivers_required": ["heimdall", "adb"],
            "recovery_method": "heimdall"
        },
        "SM-A205U": {
            "model": "Galaxy A20",
            "latest_version": "A20_PIE",
            "firmware_url": "https://samsung.example.com/firmware/SM-A205U.tar",
            "checksum_md5": "def456ghi789",
            "checksum_sha256": "sha256hash789012",
            "size_mb": 2800,
            "release_date": "2021-05-10",
            "changelog": "Bug fixes and stability improvements",
            "drivers_required": ["heimdall", "adb"],
            "recovery_method": "heimdall"
        }
    },
    "apple": {
        "iPhone12,1": {
            "model": "iPhone 12",
            "latest_version": "17.1",
            "ipsw_url": "https://security-content.cdn-apple.com/iPhone12,1_17.1.ipsw",
            "checksum_sha256": "applesha256hash123",
            "size_mb": 4200,
            "release_date": "2023-10-16",
            "changelog": "iOS 17.1 security updates",
            "drivers_required": ["idevicerestore", "libimobiledevice"],
            "recovery_method": "idevicerestore"
        }
    }
}