# Grāmatu Cenu Salīdzināšanas Automatizācija izmantojot Python Selenium bibliotēku


## Satura rādītājs

1. [Projekta Uzdevums](#projekta-uzdevums)
2. [Programmatūras darbība](#programmatūras-darbība)
3. [Izmantotās Bibliotēkas](#izmantotās-bibliotēkas)
4. [Iestatīšana un izpilde](#iestatīšana-un-izpilde)
5. [Programmatūras Izmantošanas Metodes](#programmatūras-izmantošanas-metodes)


## Projekta uzdevums

Šī projekta mērķis ir izveidot skriptu, kas palīdzēs grāmatu lasīšanas un pirkšanas cienītājiem (tādiem kā es) automatizēt labākā piedāvājuma meklēšanu 3 populārās Latvijā tiešsaistes grāmatnīcās : [janisroze.lv](https://www.janisroze.lv/lv/), [eglobuss.lv](https://eglobuss.lv/), [valtersunrapa.lv](https://www.valtersunrapa.lv/). Skriptam ir jāņem teksta dokuments ar grāmatu nosaukumiem un jāizvada cits dokuments ar labākajiem piedāvājumiem.

## Programmatūras darbība

Šī programma nolasa grāmatu nosaukumus no teksta dokumenta "books.txt" un pievieno tos sarakstā *books_list*. Pēc tam, programma izmanto trīs, iepriekš definētas funkcijas : *janisroze_price*, *eglobuss_price*, *valtersunrapa_price*. Šīs funkcijas kā argumentu pieņēm sarastu no grāmatām *books_list* un izmantojot `Selenium` bibliotēku simulē pārlūka darbību, automātiski veicot pieprasījumus attiecīgos internet veikalos (janisroze.lv, eglobuss.lv, valtersunrapa.lv), skrāpē no tīmekļa grāmatas cēnu un veido no tiem sarakstus. Tālāk programma rada vai notīra teksta dokumentu "result.txt", kur ar cikla *for* palidzību programma atrod labāko cenu katrai grāmatai un teksta dokumentam pievieno grāmatas numuru, nosaukumu, labāko cenu un internet veikalu ar labāko cenu.

## Izmantotās Bibliotēkas

### `Selenium`
- **Apraksts**: `Selenium` ir Python bibliotēka, kas ļauj veikt darbības pārlūkprogrammā, kā to darītu cilvēks. Tas ir plaši izmantots testēšanā un mājas lapu automātiskajā izstrādē. Šī bibliotēka piedāvā dažādas iespējas, sākot no interaktīvas pārlūkošanas līdz mājas lapu testēšanai.
- **Izmantošana šajā projektā**: `Selenium` tiek izmantots grāmatu cenu iegūšanai no trīs dažādiem interneta veikaliem. Katrai grāmatnīcai tiek izveidota atsevišķa funkcija, kas simulē pārlūka darbību un iegūst konkrētā veikala grāmatu cenas. Šīs funkcijas tiek izsauktas galvenajā programmas daļā.

### `Time`
- **Apraksts**: `Time` ir iebūvēta Python bibliotēka, kas nodrošina funkcijas laika aizkavēšanai un pārtraukumiem.
- **Izmantošana šajā projektā**: `Time` tiek izmantots, lai programmai piešķirtu gaidīšanas laiku starp pārlūka darbībām, nodrošinot, ka lapas ir pareizi ielādētas pirms tās satura iegūšanas.

## Iestatīšana un izpilde

Pirms skriptu palaišanas pārliecinieties, ka jūsu sistēmā ir instalēts Python, Selenium bibliotēka un konfigurēts Chrome WebDriver.
1. Ja jums nav Python, varat to lejupielādēt no [Python oficiālās vietnes](https://www.python.org/downloads/).
2. Lejupielādējiet Selenium:
   ```
   pip install selenium
   ```
3. Lejupielādējiet un iestatiet Chrome WebDriver: [Saite uz WebDriver](https://sites.google.com/a/chromium.org/chromedriver/)


## Programmatūras Izmantošanas Metodes

- *Grāmatu Nosaukumu Ievietošana:* Ievietojiet grāmatu nosaukumus teksta dokumentā "books.txt", katrs nosaukums jaunā rindiņā.
- *Programmas Palaišana:* Palaidiet Python skriptu, un tas automātiski nolasīs grāmatu nosaukumus un veiks cenu meklēšanu katrai grāmatai pie norādītajiem interneta veikaliem.
- *Rezultātu Apskatīšana:* Pēc izpildes rezultāti tiks saglabāti teksta dokumentā "result.txt". Šeit būs redzams katras grāmatas numurs, nosaukums, cena un veikals ar zemāko cenu.

---

Šī programma piedāvā ērtu veidu, kā salīdzināt grāmatu cenas dažādās interneta veikalos, palīdzot jums atrast visizdevīgāko piedāvājumu.
