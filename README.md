# Orbit Kontrol

orbitkontrol.com web sitesi.

- `index.html` — sitenin tamamı (TR / EN / DE / RU / AR)
- `kur.json` — TCMB döviz alış kurları (site bunu okur)
- `scripts/kur_guncelle.py` ve `.github/workflows/kur.yml` — kurları hafta içi her gün 15:50'de (İstanbul) TCMB'den çekip `kur.json`'u günceller
