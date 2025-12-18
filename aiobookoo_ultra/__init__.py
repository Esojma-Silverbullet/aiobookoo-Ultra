"""Kompatibilitäts-Package für aiobookoo.

Diese Datei erlaubt Imports über ``aiobookoo_ultra`` und reicht alle
öffentlichen Klassen/Funktionen aus dem bisherigen ``aiobookoo`` weiter.
Dadurch funktionieren bestehende Integrationen (z.B. Themis Ultra für
Home Assistant), ohne den Integrationscode anpassen zu müssen.
"""

from aiobookoo.bookooscale import BookooDeviceState, BookooScale
from aiobookoo.const import (
    CHARACTERISTIC_UUID_COMMAND,
    CHARACTERISTIC_UUID_WEIGHT,
    CMD_BYTE1_PRODUCT_NUMBER,
    CMD_BYTE2_TYPE,
    SCALE_START_NAMES,
    SERVICE_UUID,
    UnitMass,
    WEIGHT_BYTE1,
    WEIGHT_BYTE2,
)
from aiobookoo.decode import BookooMessage, decode
from aiobookoo.exceptions import (
    BookooDeviceNotFound,
    BookooError,
    BookooMessageError,
    BookooMessageTooLong,
    BookooMessageTooShort,
    BookooScaleException,
    BookooUnknownDevice,
)
from aiobookoo.helpers import find_bookoo_devices, is_bookoo_scale, scan

__all__ = [
    "BookooDeviceState",
    "BookooScale",
    "CHARACTERISTIC_UUID_COMMAND",
    "CHARACTERISTIC_UUID_WEIGHT",
    "CMD_BYTE1_PRODUCT_NUMBER",
    "CMD_BYTE2_TYPE",
    "SCALE_START_NAMES",
    "SERVICE_UUID",
    "UnitMass",
    "WEIGHT_BYTE1",
    "WEIGHT_BYTE2",
    "BookooMessage",
    "decode",
    "BookooDeviceNotFound",
    "BookooError",
    "BookooMessageError",
    "BookooMessageTooLong",
    "BookooMessageTooShort",
    "BookooScaleException",
    "BookooUnknownDevice",
    "find_bookoo_devices",
    "is_bookoo_scale",
    "scan",
]
