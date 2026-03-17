## Fastener OCR PDF → Markdown Aracı

Bu repo, fastener / bağlantı elemanı datasheet PDF’lerini **Docling** kullanarak toplu halde **Markdown (.md)** formatına çevirmek için hazırlanmış basit bir komut satırı aracını içerir.

Ana amaç:
- Seçtiğin PDF klasörünü Docling CLI ile işlemek,
- Her PDF için aynı isimde bir `.md` dosyası üretmek,
- Gerekirse **OCR**’yi (taranmış PDF’ler için) kolayca açabilmek.

---

### 1. Klasör yapısı

- `docling_fastener_tool/`  
  Asıl kod ve Windows script’leri:
  - `pdf_to_md_simple.py` → Docling ile PDF → MD dönüşümünün kalbi.
  - `python/pdf_to_md_cli.py` → CLI giriş noktası (Windows / Mac / Linux).
  - `windows_bundle/install_deps.bat` → Embedded Python + offline `.whl` ile bağımlılık kurulumu.
  - `windows_bundle/run_tool.bat` → Windows’ta basit PDF → MD çalıştırma (girdi/çıktı sorar).
  - `windows_bundle/run_cli_pdf_to_md.bat` → Tam CLI sürümünü (interaktif OCR seçimi ile) çalıştırır.
  - `requirements.txt` → Sadece `docling` bağımlılığı.

- `fasteners/` (örnek)  
  PDF’lerini koyabileceğin klasör (lokal ortamda).

- `output_md_simple/` veya `fasteners/output_md/` (örnek)  
  Üretilen `.md` dosyalarının yazıldığı klasörler.

---

### 2. Kurulum (Mac / Linux)

```bash
cd docling_fastener_tool
pip install -r requirements.txt
docling --help  # Docling CLI’nin çalıştığını kontrol et
```

---

### 3. Kullanım (Mac / Linux CLI)

**İnteraktif mod (PDF klasörü ve OCR seçimi sorulur):**

```bash
cd docling_fastener_tool
python python/pdf_to_md_cli.py
```

Adımlar:
1. Terminalde senden **PDF klasörü** yolunu ister.  
2. Sonra **OCR modu** için sorar:
   - `n` → normal (OCR kapalı),
   - `o` → `--ocr` (taranmış PDF’ler için),
   - `f` → `--force-ocr` (her sayfayı OCR ile oku).
3. Çıktı klasörü belirtmediysen, otomatik olarak `input_dir/output_md` kullanılır.

Her PDF için:
- `[i/N] İşleniyor: <dosya>.pdf` log’u görünür,
- Aynı isimde `<dosya>.md` oluşturulur.

---

### 4. Kullanım (Windows + Embedded Python)

Varsayılan klasör:
- `C:\fastener_tool\docling_fastener_tool\...`

Adımlar:
1. Embedded Python zip’ini `C:\fastener_tool\python_embed` içine aç.  
2. İnternet olan bir makinede `docling` için gerekli `.whl` dosyalarını indirip `C:\fastener_tool\wheels` içine koy.  
3. `C:\fastener_tool\docling_fastener_tool\windows_bundle\install_deps.bat` dosyasına çift tıkla (bağımlılıkları kurar).  
4. Sonra:
   - **Basit mod (girdi/çıktı sadece .bat üzerinden):**  
     `windows_bundle\run_tool.bat`
   - **Tam CLI + OCR seçimi ile:**  
     `windows_bundle\run_cli_pdf_to_md.bat`

Her iki `.bat` de öncelikle `python_embed\python.exe`’yi, yoksa sistem PATH’teki `python`’ı kullanır.

---

### 5. Lisans / Notlar

Bu repo temel bir kişisel yardımcı araçtır. Docling kütüphanesinin ve kullandığın diğer bağımlılıkların lisanslarını kendi repolarından kontrol etmen gerekir.

