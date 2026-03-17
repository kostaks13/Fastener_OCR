## PDF → Markdown (Docling)

Bu araç, seçtiğin klasördeki **tüm PDF dosyalarını** Docling CLI kullanarak **Markdown (.md)** formatına çevirir.  
Amaç: sadece PDF → MD; ek JSON/CSV/LLM işlemi yok.

---

### 1. Dosyalar ve klasörler

- `pdf_to_md_simple.py`  
  Klasördeki tüm `.pdf` dosyalarını Docling ile **Markdown**’a çevirir.

- `python/pdf_to_md_cli.py`  
  Windows embeddable Python veya sistem Python’u için küçük bir “wrapper” CLI; asıl işi `pdf_to_md_simple.py` çalıştırır.

- `requirements.txt`  
  - `docling`

- `windows_bundle/` (sadece Windows için)  
  - `install_deps.bat` → Bağımlılıkları `python_embed` + `wheels` ile kurar.  
  - `run_tool.bat` → Senden PDF ve çıktı klasörü alıp `pdf_to_md_simple.py`’yi çalıştırır.  
  - `python_embed/` → Windows embeddable Python (zip’ten açtığın klasör).  
  - `wheels/` → İnternet varken indirdiğin `.whl` dosyaları (offline kurulum için).

---

### 2. Mac / Linux için kullanım

**A. Kurulum**

1. Proje klasörüne gir:
   ```bash
   cd docling_fastener_tool
   ```
2. Gerekli Python paketini kur:
   ```bash
   pip install -r requirements.txt
   ```
3. Docling CLI’nin çalıştığını test et:
   ```bash
   docling --help
   ```

**B. PDF → MD**

1. PDF dosyalarını bir klasöre koy (ör. `/path/to/pdfs`).
2. Çıktı için bir klasör belirle (ör. `/path/to/output_md`).
3. Komut satırından çalıştır (proje kökünde, yani `docling_fastener_tool` dizininde):
   ```bash
   python python/pdf_to_md_cli.py --input-dir /path/to/pdfs --output-dir /path/to/output_md
   ```
4. Çıktı klasöründe her PDF için şu dosya oluşur:
   - `isim.md`

---

### 3. Performans ve kalite notları

- Bu basit araç, Docling’in **varsayılan hızlı pipeline**’ını kullanır:
  - **Sadece `md` çıktısı** üretir (JSON/VLM/OCR yok).
  - Çoğu dijital PDF için yeterli doğruluk + yüksek hız sağlar.
- Eğer:
  - **Taranmış (scan) PDF** veya
  - Çok karmaşık / bozuk tablolar
  gibi daha zor dokümanlar için **daha yüksek kalite** istersen,
  önce bu aracı kullan, sorunlu PDF’ler için ayrı bir Docling komutu veya gelişmiş aracı kullanarak
  OCR / VLM gibi ek özellikleri açman gerekebilir.

---

### 4. Windows’ta embed Python ile çalışma (özet)

1. `docling_fastener_tool` klasörünü örneğin `C:\fastener_tool` altına kopyala.  
2. Python embeddable zip’ini indirip `C:\fastener_tool\python_embed` içine aç.  
3. İnternet olan bir makinede gerekli `.whl` dosyalarını indirip `C:\fastener_tool\wheels` klasörüne koy.  
4. `C:\fastener_tool\docling_fastener_tool\windows_bundle\install_deps.bat` dosyasına çift tıkla (bağımlılıkları kurar).  
5. `windows_bundle\run_tool.bat` dosyasına çift tıkla:
   - PDF klasörü (ör. `C:\fasteners`)
   - Çıktı klasörü (ör. `C:\output_md`)

Artık bu projede yalnızca **PDF → MD** dönüşümü vardır; JSON/CSV/LLM ve GUI bileşenleri kaldırılmıştır.
