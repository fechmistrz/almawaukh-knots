# Przewodnik po kodzie źródłowym
Ważne rzeczy pojawiające się raz trafiają do indeksu linijkę po zdaniu, gdzie się pojawiły:
```
Niech $f: X \to X$ będzie bulbulatorem.
\index{bulbulator}%
```
Ważne osoby też, ale one mają swój własny indeks.
```
Kosta \cite{kosta95} zapytał, kiedy ciąg $f^n$ jest zbieżny w $*$-topologii.
\index[persons]{Kosta, Stjepan}%
```
Procent na końcu jest potrzebny, żeby nie zepsuć odstępów między wyrazami.
Ważne rzeczy pojawiające się na wielu stronach trafiają do indeksu tak samo:
```
\index{bukszpan!gwieździsty!\(}%
(Dużo tekstu)
\index{bukszpan!gwieździsty!\)}%
```

Terminy specyficzne dla teorii węzłów powinny mieć wspomniane angielskie odpowiedniki:
```
% DICTIONARY;whoofwhoofizer;bulbulator;-
Bulbulator, który jest jednocześnie jagodowy i truskawkowy nazywamy smacznym.
% DICTIONARY;yummy;smaczny;bulbulator
```

Wszystkie diagramy węzłów w TikZ używają grubości ultra thick, chyba że mówimy o dowodach z sekcji o klamrze Kauffmana - wtedy musi być thick.

Wyszukiwanie tego samego nazwiska z roznie zapisanymi imionami:
```
grep AUTHOR ./src/knot_theory.bib | grep -Eo '\{.*\}' | sed -r 's/ and /\n/g' | tr -d '{}' | sort | uniq > tmp.txt
awk 'NR==FNR{c[$1]++;next} c[$1]>1' tmp.txt tmp.txt
```

Wyszukiwanie dawno nieedytowanych plików:
```
find src/[12345]* -name '*.tex' | while read -r line; do echo $(git log --format=format:%cs -n 1 -- $line) $line; done | sort -V
```

Pokazywanie indeksu jako przypis:
```
find src/ -type f | grep tex | grep -E 'src/[12345]' | sort -V | while read -r line; do
    cat "$line" | sed -r 's_\\index\{(.*)\}_\\footnote{INDEKS: \1}_g' | sed -r 's_\\index(\[[^]]+\])\{(.*)\}_\\footnote{INDEKS KWADRATOWY: \2}_g' > x && mv x "$line";
done
```
