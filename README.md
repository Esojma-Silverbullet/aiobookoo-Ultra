# aiobookoo-ultra

Dieses Repository stellt das asynchrone BLE-Protokoll der **Bookoo Themis Ultra**
bereit. Es dient als externe Abhängigkeit für andere Projekte und konzentriert
sich ausschließlich auf das Ultra-Protokoll (korrekte Service- und
Characteristic-UUIDs, Kommandoaufbau und Gewichts-Parsing).

## Empfohlener Importpfad

```python
from aiobookoo_ultra import BookooScale
```

## Installation

* Veröffentlichung (PyPI): `pip install aiobookoo-ultra`
* Aus Git-Tag (0.1.1):\
  `pip install git+https://github.com/Esojma-Silverbullet/aiobookoo-Ultra.git@0.1.1`

Nach der Installation steht das Modul ohne weitere Anpassungen zur Verfügung;
weitere Framework-spezifische Logik ist bewusst nicht enthalten.
