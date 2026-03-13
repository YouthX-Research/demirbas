"""Komut satırından DemirBaş çalıştırmak için basit bir giriş noktası."""

from __future__ import annotations

import argparse
import sys

from .analysis import analyze_and_print
from .engine import load_engine
from .rules import check_text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="demirbas")
    parser.add_argument(
        "metin",
        nargs="?",
        default="DemirBaş projesi başarıyla çalışıyor.",
        help="Denetlenecek metin",
    )
    parser.add_argument(
        "--download-models",
        action="store_true",
        help="Stanza modellerini indirir (ilk kullanımda gerekebilir).",
    )

    args = parser.parse_args(argv)

    try:
        nlp, morphology = load_engine(download_models=args.download_models)
    except Exception as e:
        print(f"❌ Başlatma hatası: {e}")
        return 1

    analyze_and_print(args.metin, nlp, morphology)

    report = check_text(args.metin, nlp)
    if report["hatalar"]:
        print("\nBulunan hatalar:")
        for h in report["hatalar"]:
            print(h)
    else:
        print("\n✅ Bu cümlede bir sorun bulunamadı.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
