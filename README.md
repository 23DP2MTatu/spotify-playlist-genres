# Spotify atskaņošanas sarakstu žanru prognozēšana

Vai pēc dziesmas tempa, skaļuma, enerģiskuma, piemērotības dejošanai un runas izteiktības var noteikt tās atskaņošanas saraksta žanru? Projekts apmāca lēmumu koku un salīdzina tā precizitāti ar vienkāršu prognozi, kas katrai dziesmai izvēlas treniņa datos biežāko žanru.

## Palaišana

Nepieciešams Python 3 un bibliotēkas `pandas` un `scikit-learn`. Atver termināli projekta mapē un izpildi komandas norādītajā secībā.

```shell
python -m pip install pandas scikit-learn
python 01_tirisana.py
python 02_modelis.py
```

Pirmais skripts nolasa [sākotnējos datus](dati/spotify_songs.csv), izslēdz dziesmas ar vairākiem atskaņošanas sarakstu žanriem un katru atlikušo dziesmu saglabā vienreiz failā `tirs.csv`. Terminālī var redzēt, cik rindu izņemts katrā solī.

Otrais skripts nolasa `tirs.csv`, apmāca modeli un testa datos salīdzina modeļa precizitāti ar bāzes līniju. Tas parāda arī divas svarīgākās pazīmes un vienu kļūdainas prognozes piemēru. Rezultāti un secinājumi ir aprakstīti [darba pārskatā](rezultati.md).
