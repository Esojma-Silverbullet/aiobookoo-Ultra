# aiobookoo-ultra

Unterstützt: **Bookoo Themis Ultra**

Dieses Repository stellt das asynchrone BLE-Protokoll der Themis Ultra bereit
und definiert genau ein Service-/Characteristic-Set (Ultra). Kompatible Wrapper
(`aiobookoo`) existieren nur für Altimporte; der einzig empfohlene Pfad ist
`aiobookoo_ultra`.

## Empfohlener Importpfad

```python
from aiobookoo_ultra import BookooScale
```

## Installation

* Veröffentlichung (PyPI): `pip install aiobookoo-ultra`
* Aus Git-Tag (z. B. 0.1.2):\
  `pip install git+https://github.com/Esojma-Silverbullet/aiobookoo-Ultra.git@0.1.2`

Nach der Installation steht das Modul ohne weitere Anpassungen zur Verfügung;
weitere Framework-spezifische Logik ist bewusst nicht enthalten.
