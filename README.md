# DM-warsztat

Warsztat z tworzenia różnych sieci neuronowych z okazji Dnia Matematyki na Wydziale Matematyki Pwr.


To co najbardziej interesujące znajduje się w `notebook.ipynb`, który omówimy sobie w trakcie warsztatu.

Bedziemy bazować na kilku datasetach zebranych w folderze `data`:
- `linear.npz`,  `nonlinear.npz`, `time_series.npz` &mdash; wygenerowane przeze mnie zbiory danych
- `nasa.csv` &mdash; dane o asteoroidach, które mogą stanowić zagrożenie ([źródło](https://www.kaggle.com/datasets/lovishbansal123/nasa-asteroids-classification)),
- obrazki przedstawiające 4 zjawiska pogodowe ([źródło](https://data.mendeley.com/datasets/4drtyfjtfy/1))




## Instalacja

Notebooka i dane można wrzucić na Colaba i w sumie nie powinno być większych problemów.
W razie kłopotów w code chunku notatnika uruchamiamy:

```
!pip install <nazwa paczki>
```

i po sprawie.

Jeżeli ktoś chciałby powalczyć lokalnie, to tworzymy środowisko wirtualne czy anacondowe i instalujemy paczki z pliku `requirements.txt`. Polecam skorzystanie z `uv`, a nie standardowego `pip`-a, czyli porobić coś takiego:

```bash
uv venv venv

venv\Scripts\actviate (windows)
source venv/bin/activate (linux)

uv pip install -r requirements.txt
```

Różnica między `uv` a `pip` jest wyrażnie zauważalna.


## Materiały do nauki

### Książki

### Kursy


@author: Marcin Kostrzewa
