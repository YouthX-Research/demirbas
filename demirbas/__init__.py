"""DemirBaş Türkçe metin denetleme kütüphanesi.

Bu paket, Türkçe için temel NLP altyapısını (Stanza + spaCy) ve
metin kuralı denetleme fonksiyonlarını sağlar.

Örnek kullanım:
    from demirbas import load_engine, analyze, check_text

    nlp, morphology = load_engine()
    print(analyze("Merhaba dünya", nlp, morphology))
    print(check_text("Tam eminim"))
"""

from .engine import load_engine
from .analysis import analyze, analyze_and_print
from .rules import check_text

__all__ = [
    "load_engine",
    "analyze",
    "analyze_and_print",
    "check_text",
]
