"""DemirBaş dil kurallarını ve kontrol fonksiyonlarını sağlar."""

from __future__ import annotations

from typing import Any, Dict, List, Tuple


DEFAULT_RULES = {
    "gereksiz_sozcukler": [("geri", "iade")],
    "celisen_sozcukler": [("tam", "yaklaşık"), ("eminim", "belki")],
}


def check_text(text: str, nlp: Any = None, rules: Dict[str, List[Tuple[str, str]]] = None) -> Dict[str, Any]:
    """Metin üzerinde DemirBaş kurallarını çalıştırır.

    Args:
        text: Denetlenecek metin.
        nlp: İsteğe bağlı olarak spaCy/ Stanza boru hattı (tokenizasyon için).
        rules: Denetleme için kullanılacak kural seti.

    Returns:
        Sözlük içinde metin, bulunan hatalar ve isteğe bağlı analiz.
    """

    rules = rules or DEFAULT_RULES

    if nlp is not None:
        doc = nlp(text)
        tokens = [t.text.lower() for t in doc]
    else:
        tokens = text.lower().split()

    errors: List[str] = []

    for first, second in rules.get("gereksiz_sozcukler", []):
        if first in tokens and second in tokens:
            errors.append(
                f"⚠️ Gereksiz sözcük kullanımı: '{second}' zaten '{first}' anlamını taşır."
            )

    for first, second in rules.get("celisen_sozcukler", []):
        if first in tokens and second in tokens:
            errors.append(
                f"⚠️ Çelişen sözcüklerin kullanımı: '{first}' kesinlik, '{second}' ihtimal bildirir."
            )

    return {"metin": text, "hatalar": errors}
