import argparse
import subprocess
from pathlib import Path


def convert_folder(
    input_dir: Path,
    output_dir: Path,
    *,
    ocr: bool = False,
    force_ocr: bool = False,
) -> None:
    """
    Verilen klasördeki TÜM .pdf dosyalarını
    Docling CLI kullanarak Markdown'a çevirir.
    - Girdi:  *.pdf
    - Çıktı:  her PDF için aynı isimde *.md
    """
    pdf_files = sorted(input_dir.glob("*.pdf"))
    if not pdf_files:
        raise SystemExit(f"PDF bulunamadı: {input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    total = len(pdf_files)
    for idx, pdf_path in enumerate(pdf_files, start=1):
        md_path = output_dir / f"{pdf_path.stem}.md"
        print(f"[{idx}/{total}] İşleniyor: {pdf_path.name}")

        cmd = [
            "docling",
            str(pdf_path),
            "--from",
            "pdf",
            "--to",
            "md",
            "--output",
            str(output_dir),
        ]

        if force_ocr:
            cmd.append("--force-ocr")
        elif ocr:
            cmd.append("--ocr")

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"Docling hata kodu {result.returncode}: {result.stderr.strip()}"
            )

        if not md_path.exists():
            raise RuntimeError(f"Beklenen MD dosyası oluşmadı: {md_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Seçilen klasördeki PDF'leri Docling ile Markdown'a çevir.",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        help="PDF dosyalarının bulunduğu klasör (boş bırakılırsa CLI sorar)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Markdown çıktılarının yazılacağı klasör (varsayılan: input_dir/output_md)",
    )
    parser.add_argument(
        "--ocr",
        action="store_true",
        help="Taranmış PDF'ler için Docling OCR modunu aç.",
    )
    parser.add_argument(
        "--force-ocr",
        action="store_true",
        help="Var olan metni yok sayıp tüm sayfaları OCR ile oku.",
    )

    args = parser.parse_args()

    # Eğer parametre verilmemişse, kullanıcıdan interaktif olarak iste.
    if args.input_dir is None:
        input_str = input("PDF klasörünün tam yolu: ").strip()
        if not input_str:
            raise SystemExit("Girdi klasörü belirtilmedi.")
        input_dir = Path(input_str).expanduser()
    else:
        input_dir = args.input_dir

    # OCR modu interaktif seçilsin (bayrak verilmediyse)
    ocr = bool(args.ocr)
    force_ocr = bool(args.force_ocr)
    if not ocr and not force_ocr:
        choice = input("OCR modu? (n = normal, o = OCR, f = force-OCR) [n/o/f]: ").strip().lower()
        if choice == "o":
            ocr = True
        elif choice == "f":
            force_ocr = True

    if args.output_dir is None:
        # Kullanıcının istediği gibi, girdi klasörü altında alt bir klasör oluştur.
        output_dir = input_dir / "output_md"
        print(f"Çıktı klasörü belirtilmedi, şuraya yazılacak: {output_dir}")
    else:
        output_dir = args.output_dir

    convert_folder(
        input_dir,
        output_dir,
        ocr=ocr,
        force_ocr=force_ocr,
    )


if __name__ == "__main__":
    main()

