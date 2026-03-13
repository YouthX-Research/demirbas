"""DemirBaş için NLP altyapısı.

Bu modül Stanza/ spaCy-Stanza boru hattını yükler ve
Stanza model indirme ile PyTorch güvenlik yamalarını içerir.
"""

from __future__ import annotations

import logging


def patch_torch_for_stanza() -> None:
    """Stanza modeli yüklerken PyTorch 2.6+ ile ortaya çıkan güvenlik uyarılarını gider."""

    try:
        import torch
        import numpy
    except ImportError:  # pragma: no cover
        return

    try:
        # PyTorch 2.6+ "safe globals" listesinde eksik isimler nedeniyle
        # stanza model yükleme sırasında hata alabiliyoruz.
        safe_globals = [
            numpy.core.multiarray._reconstruct,
            numpy.core.multiarray.scalar,
            numpy.ndarray,
            numpy.dtype,
        ]

        # Bazı numpy sürümlerinde _core alt modülü vardır.
        try:
            import numpy._core.multiarray

            safe_globals += [
                numpy._core.multiarray._reconstruct,
                numpy._core.multiarray.scalar,
            ]
        except (ImportError, AttributeError):
            pass

        torch.serialization.add_safe_globals(safe_globals)
    except Exception:  # pragma: no cover
        logging.getLogger(__name__).exception("Torch / NumPy patch uygulanamadı")


def load_engine(
    language: str = "tr",
    download_models: bool = False,
):
    """spaCy-Stanza boru hattını yükler.

    Bu fonksiyon:
    - torch için gerekli yamaları uygular
    - isteğe bağlı olarak Stanza modelini indirir
    - spaCy-Stanza boru hattını oluşturur

    Returns:
        (nlp, morphology): spaCy `nlp` class ve Zemberek `TurkishMorphology`
    """

    patch_torch_for_stanza()

    if download_models:
        try:
            import stanza

            stanza.download(language)
        except Exception as e:
            raise RuntimeError(
                f"Stanza modelleri indirilemedi ({language}): {e}"
            ) from e

    try:
        import spacy_stanza
        from zemberek import TurkishMorphology
    except ImportError as e:
        raise ImportError(
            "Gerekli paketler yüklenmemiş. `pip install stanza spacy-stanza zemberek-python` "
            "komutunu çalıştırın."
        ) from e

    nlp = spacy_stanza.load_pipeline(language, download_method=None)
    morphology = TurkishMorphology.create_with_defaults()
    return nlp, morphology
