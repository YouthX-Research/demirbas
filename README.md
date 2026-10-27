# DemirBaş

Türkçe metin denetleme kütüphanesi. Metni [Stanza](https://stanfordnlp.github.io/stanza/) ve [Zemberek](https://github.com/Loodos/zemberek-python) ile çözümler, ardından anlatım bozukluklarını kurallarla yakalar.

A rule-based Turkish text checker built on Stanza and Zemberek.

## Ne yapar

- **Çözümleme:** Her sözcük için kökü (Zemberek) ve sözcük türünü (Stanza) verir.
- **Denetim:** İki tür anlatım bozukluğunu yakalar:
  - Gereksiz sözcük kullanımı, örneğin *geri iade*. İade zaten geri vermek demektir.
  - Çelişen sözcükler, örneğin *tam … yaklaşık* ya da *eminim … belki*.

Kurallar `demirbas/rules.py` içindeki `DEFAULT_RULES` sözlüğünde. Yeni kural eklemek için oraya bir sözcük çifti eklemeniz yeterli.

## Kurulum

Python 3.10 veya üstü gerekir.

```sh
git clone https://github.com/YouthX-Research/demirbas.git
cd demirbas
pip install -r requirements.txt
```

## Kullanım

Komut satırından. İlk çalıştırmada `--download-models` Stanza'nın Türkçe modelini indirir:

```sh
python -m demirbas --download-models "Ürünü geri iade ettim."
```

Python'dan:

```python
from demirbas import load_engine, analyze, check_text

nlp, morphology = load_engine()
print(analyze("Kitapları okudum.", nlp, morphology))
print(check_text("Tam eminim ama belki yanılıyorum.", nlp))
```

`check_text` şu yapıda bir sözlük döner:

```python
{"metin": "...", "hatalar": ["⚠️ Çelişen sözcüklerin kullanımı: ..."]}
```

## Dosyalar

| Dosya | İçerik |
| --- | --- |
| `demirbas/engine.py` | Stanza ve Zemberek boru hattını yükler |
| `demirbas/analysis.py` | Kök ve sözcük türü çözümlemesi |
| `demirbas/rules.py` | Denetim kuralları |
| `demirbas/cli.py` | Komut satırı arayüzü |
| `colab/demirbas_colab.py` | Projenin ilk Colab sürümü, başvuru için duruyor |

## Lisans

[GPL-3.0](LICENSE). [YouthX Research](https://github.com/YouthX-Research) projesidir.
