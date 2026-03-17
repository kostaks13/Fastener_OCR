from pathlib import Path
import runpy


def main() -> None:
    """
    Basit PDF -> MD CLI giriş noktası.
    Kök dizindeki pdf_to_md_simple.py dosyasını __main__ olarak çalıştırır.
    """
    here = Path(__file__).resolve().parent
    root = here.parent
    target = root / "pdf_to_md_simple.py"
    runpy.run_path(str(target), run_name="__main__")


if __name__ == "__main__":
    main()

