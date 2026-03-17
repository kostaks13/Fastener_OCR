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

### 4. Kurulum ve kullanım (Windows + Embedded Python)

#### 4.1. Klasör yapısı

Önerilen yapı:

```text
C:\
  fastener_tool\
    python_embed\          # Windows embeddable Python buraya açılacak
    wheels\                # offline .whl paketleri
    docling_fastener_tool\ # bu repo
      windows_bundle\
      python\
      pdf_to_md_simple.py
      requirements.txt
      ...
```

#### 4.2. Embedded Python’u hazırlama

1. Microsoft’tan **Windows embeddable Python** zip’ini indir (ör. Python 3.11).  
2. Zip içeriğini `C:\fastener_tool\python_embed` klasörüne aç.  
   - İçinde `python.exe` ve birkaç `.pyd`/`.zip` dosyası olmalı.

#### 4.3. Gerekli `.whl` paketlerini indirme (internet olan makinede)

1. Herhangi bir Windows makinede (veya uygun ortamda) bu repoyu aynı yapıda kullan:  
   ```bash
   cd docling_fastener_tool
   pip download -r requirements.txt -d ../wheels
   ```
2. Bu komut, `docling` ve bağımlılıklarını `.whl` olarak `wheels` klasörüne indirir.  
3. `wheels` klasörünü **hedef offline Windows makineye** `C:\fastener_tool\wheels` olarak kopyala.

#### 4.4. Bağımlılıkları embedded Python’a kurma

1. Offline Windows makinede şu klasöre git:  
   `C:\fastener_tool\docling_fastener_tool\windows_bundle`
2. `install_deps.bat` dosyasına çift tıkla:
   - Önce `C:\fastener_tool\python_embed\python.exe`’i bulur,
   - Sonra:
     ```bat
     python.exe -m pip install --no-index --find-links=..\wheels -r ..\requirements.txt
     ```
     komutunu çalıştırarak **internet olmadan** `docling`’i kurar.

Kurulum bittikten sonra, Docling CLI’nin çalıştığını şu komutla test edebilirsin:

```bat
C:\fastener_tool\python_embed\python.exe -m docling --help
```

#### 4.5. PDF → MD çalıştırma (Windows)

İki yolun var:

- **A) Basit mod (girdi/çıktı sadece .bat üzerinden)**  
  1. `C:\fastener_tool\docling_fastener_tool\windows_bundle\run_tool.bat` dosyasına çift tıkla.  
  2. Konsolda:
     - PDF klasörünü (ör. `C:\fasteners`) sorar,
     - Çıktı klasörünü (ör. `C:\fasteners_output_md`) sorar.
  3. `pdf_to_md_simple.py` normal (OCR kapalı) modda çalışır ve çıktı klasörüne `.md` dosyaları yazar.

- **B) Tam CLI + OCR seçimi ile**  
  1. `C:\fastener_tool\docling_fastener_tool\windows_bundle\run_cli_pdf_to_md.bat` dosyasına çift tıkla.  
  2. Açılan konsolda:
     - Senden **PDF klasörü** yolunu ister (ör. `C:\fasteners`).  
     - Sonra **OCR modu** sorar:
       - `n` → normal (OCR kapalı),
       - `o` → `--ocr` (taranmış PDF’ler için),
       - `f` → `--force-ocr` (her sayfayı OCR ile oku).
     - Çıktı klasörü belirtmediysen, otomatik olarak `C:\fasteners\output_md` oluşturur ve oraya yazar.

Her iki `.bat` dosyası da önce `python_embed\python.exe`’yi, yoksa PATH’teki `python`’ı kullanır; bu sayede istersen normal kurulu Python ile de çalıştırabilirsin.

---

### 5. Lisans / Notlar

Bu repo temel bir kişisel yardımcı araçtır. Docling kütüphanesinin ve kullandığın diğer bağımlılıkların lisanslarını kendi repolarından kontrol etmen gerekir.

