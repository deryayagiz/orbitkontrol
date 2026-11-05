"""TCMB gösterge kurlarından (Döviz Alış) USD, EUR ve RUB'u çekip kur.json'a yazar."""
import json, urllib.request, xml.etree.ElementTree as ET

URL = "https://www.tcmb.gov.tr/kurlar/today.xml"
req = urllib.request.Request(URL, headers={"User-Agent": "orbitkontrol-kur-guncelleyici"})
root = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())

out = {"date": root.get("Tarih"), "source": "TCMB ForexBuying"}
for cur in root.findall("Currency"):
    code = cur.get("CurrencyCode")
    if code in ("USD", "EUR", "RUB"):
        unit = float(cur.findtext("Unit") or 1)
        out[code] = round(float(cur.findtext("ForexBuying")) / unit, 6)

if all(k in out for k in ("USD", "EUR", "RUB")):
    with open("kur.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    print("kur.json güncellendi:", out)
else:
    raise SystemExit("Kurlar okunamadı, kur.json değiştirilmedi.")
