"""Metin analizi ve çıktıları sağlayan fonksiyonlar."""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Tuple


def analyze(text: str, nlp: Any, morphology: Any) -> List[Tuple[str, str, str]]:
    """Metni analiz eder ve her token için (text, stem, pos) döner."""

    doc = nlp(text)

    z_results = morphology.analyze_sentence(text)
    z_best = morphology.disambiguate(text, z_results).best_analysis()

    return [
        (token.text, z_analysis.get_stem(), token.pos_)
        for token, z_analysis in zip(doc, z_best)
    ]


def analyze_and_print(text: str, nlp: Any, morphology: Any) -> None:
    """Analiz sonucunu ekrana yazdırır."""

    print(f"\nAnaliz Sonucu ({text}):\n" + "=" * 30)
    for token, stem, pos in analyze(text, nlp, morphology):
        print(f"📍 {token} -> Kök: {stem}, Tür: {pos}")
