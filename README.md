![paperback](https://i.imgur.com/EyZXqrD.jpg)
# Przewodnik po teorii węzłów
Polskie tłumaczenie znakomitych notatek francuskich topologów C. Allarda, A. Gauthier poświęconych teorii węzłów
Wyszło coś pomiędzy pracą przeglądową, skryptem do wykładu oraz podręcznikiem.

Opowiada o...
1. ruchach Reidemeistera, dwóch głównych problemach tego działu matematyki (klasyfikacja i rozróżnianie węzłów, w szczególności wykrywanie niewęzła), hipotezach Taita, różnych notacjach dla splotów (Dowkera-Thistlethwaite'a, Alexandera-Briggsa, Conwaya), operacjach na splotach (lustrze, rewersie, różnych typach symetrii wywodzących się z tych dwóch; sumie spójnej i jej uogólnieniach), węzłach pierwszych, całkowitoliczbowych niezmiennikach (indeks skrzyżowaniowy, liczba gordyjska, liczba mostowa, indeks zaczepienia, spin, liczba patykowa, długość sznurowa);
2. niezmiennikach, które mają coś wspólnego z kolorowaniem łuków na diagramie: trójkolorowaniu, n-kolorowaniu, etykietowaniu elementami grupy, etykietowaniu elementami kwandla; macierzy oraz grupie kolorującej, wyznaczniku i defekcie;
3. niezmiennikach wielomianowych: Alexandera, Jonesa, HOMFLY-PT, BLM/Ho, Kauffmana (jest nawet jego wersja z Dubrownika :D) i świeżych niezmiennikach Wasiljewa (skończonego typu, pojawia się przez to m.in. całka Koncewicza);
4. przydatnych narzędziach z topologii algebraicznej, takich jak grupa podstawowa dopełnienia, prezentacji Wirtingera, powierzchniach Seiferta oraz niezmiennikach przez nie wyznaczanych: sygnaturze, genusie; są wreszcie homologie Chowanowa;
5. ostatni rozdział przedstawia konkretne rodziny węzłów i splotów: warkocze, supły, sploty wymierne, mutanty, precle, węzły Lissajous, torusowe, satelitarne, hiperboliczne.

Na końcu jest trochę diagramów o niskim indeksie skrzyżowaniowym; tablice z wartościami niezmienników, żeby nie musieć ich szukać jeszcze raz; słowniczek polsko-angielski i całkiem długa bibliografia.

## Budowanie ze źródeł

**UWAGA**: Wydania (dostępne w sekcji Releases, np. wersja 0.1 albo 0.2 albo późniejsze) szybko się deaktualizują, najnowsze notatki są dostępne zawsze pod [tym samym adresem](http://www.math.uni.wroc.pl/~s265342/files/knot-theory.pdf).
Lepiej korzystać z nich, ewentualnie budować projekt samemu:
```
make all                 # w głównym katalogu
```
lub jeśli coś powstrzymuje przed użyciem Make,
```
pdflatex knot-theory.tex # wewnątrz src/
bibtex knot-theory
makeindex knot-theory
pdflatex knot-theory.tex
pdflatex knot-theory.tex
```

## Do zrobienia
Naprawić `./src/merridew/bibliography_sort.py --bib src/knot_theory.bib`:
```
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in brittenham06 (@misc)
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in cha18 (@misc)
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in chmutov05 (@misc)
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in gruber03 (@misc)
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in kneissler97 (@misc)
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in malyutin16 (@misc)
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in malyutin19 (@misc)
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in musick12 (@misc)
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in purcell20 (@misc)
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in stoimenow07 (@misc)
WARNING: Found unexpected fields: ['archiveprefix', 'eprint', 'primaryclass'] in zirbel06 (@misc)

WARNING: Found unexpected fields: ['copyright', 'keywords', 'publisher'] in schleimer21 (@misc)
WARNING: Found unexpected fields: ['eprint'] in zanellati16 (@article)
WARNING: Found unexpected fields: ['fjournal', 'journal'] in lambropoulou97 (@incollection)
WARNING: Found unexpected fields: ['fjournal', 'journal'] in murakami90 (@inproceedings)
WARNING: Found unexpected fields: ['fjournal', 'journal'] in perko82 (@inproceedings)
WARNING: Found unexpected fields: ['fjournal', 'journal'] in scharlemann98 (@incollection)
WARNING: Found unexpected fields: ['volume'] in cerf98 (@misc)
```

Zaimplementować aspell w make test.

Wyjaśnić, jaka jest różnica między dowodem i niedowodem.

I would advise to use the @misc type, as it officially allows the fields eprint, eprintclass, and eprinttype, as opposed to @unpublished, and @online. @article requires journaltitle, as @Jonathan pointed out. See biblatex documentation (2.1 Entry Types and 3.12. Electronic Publishing Information) – https://tex.stackexchange.com/questions/3833/how-to-cite-an-article-from-arxiv-using-bibtex

Cytowania z ArXiV nie wyświetlają hiperłącza w bibliografii, poprawić styl. (Usunąć In: oraz Pages: na rzecz W: oraz Stron:)