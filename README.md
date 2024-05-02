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
* [*Little book of Deep Learning*](https://fleuret.org/francois/lbdl.html), Francois Fleuret
* *Deep learning*, Ian Goodfellow and Yoshua Bengio and Aaron Courville
* *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, Aurélien Géron

### Kursy
* Kursy [stąd](https://www.deeplearning.ai/courses/)
* https://dlvu.github.io/
* [Karpathy's From zero to Hero](https://karpathy.ai/zero-to-hero.html)
* [Kurs DL z uniwersytetu w Genewie](https://fleuret.org/dlc/)

@author: Marcin Kostrzewa
