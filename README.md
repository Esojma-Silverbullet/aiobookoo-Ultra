# aiobookoo-ultra

Bookoo-Implementierung basierend auf [aioacaia](https://github.com/zweckj/aioacaia),
`asyncio` und `bleak`. Dieses Package stellt zusätzlich den Import-Pfad
`aiobookoo_ultra` bereit, damit die Themis-Ultra-Integration für Home Assistant
ohne Codeänderungen funktioniert.

## Nutzung

* Installation (lokal): `pip install .`
* Import im Integrationscode: `from aiobookoo_ultra.bookooscale import BookooScale`
  (oder weiterhin `from aiobookoo.bookooscale import BookooScale`)
* Für Home Assistant: Das Package im `manifest.json` der Integration als
  Abhängigkeit (`aiobookoo-ultra==0.1.1`) eintragen, damit HA das Modul bereitstellt.
