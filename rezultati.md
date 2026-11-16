# Vai pēc dziesmas skanējuma var paredzēt Spotify atskaņošanas saraksta žanru?

## Datu avots

Izmantoju TidyTuesday publicēto Spotify dziesmu datu kopu, ko lejupielādēju 2026. gada 16. novembrī. Sākotnējā tabulā ir 32 833 rindas un 23 kolonnas. Katra rinda apraksta dziesmu konkrētā atskaņošanas sarakstā, tāpēc viena dziesma tabulā var parādīties vairākas reizes. [Sākotnējais CSV fails](https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv)

## Datu tīrīšana

Pēc kolonnas `track_id` atradu 28 356 dažādas dziesmas. No tām 1 687 bija iekļautas dažādu žanru sarakstos. Piemēram, ja vienai dziesmai ir gan apzīmējums `pop`, gan `rock`, pirmās rindas izvēle padarītu atbildi atkarīgu no rindu secības failā.

| Solis | Iemesls | Izņemtās rindas | Atlikušās rindas |
|---|---|---:|---:|
| Izslēdzu dziesmas, kas parādījās vairākos žanros | Vienai un tai pašai dziesmai bija vairāki iespējamie mērķa žanri. | 4 519 | 28 314 |
| Katram atlikušajam `track_id` paturēju pirmo rindu | Viena dziesma varēja atkārtoties arī viena žanra sarakstos un vēlāk nonākt gan treniņa, gan testa datos. | 1 645 | 26 669 |

Kopā izņēmu 6 164 rindas. Failā `tirs.csv` katrai dziesmai palika viena rinda.

## Modeļa rezultāti

Lēmumu koks prognozēja vienu no sešiem saraksta žanriem (`pop`, `rock`, `rap`, `r&b`, `latin`, `edm`). Tas izmantoja piecas pazīmes — tempu, skaļumu, enerģiskumu, piemērotību dejošanai un runas izteiktību. Apmācībai izmantoju 21 335 dziesmas, pārbaudei — 5 334. Abās daļās saglabāju aptuveni vienādu katra žanra īpatsvaru.

Salīdzinot koka dziļumus 3, 5 un 9, izmantoju vienu un to pašu datu sadalījumu. Gan datu dalīšanai (`train_test_split`), gan lēmumu kokam (`DecisionTreeClassifier`) iestatīju `random_state=42`, lai eksperimentu varētu atkārtot.

| Prognozēšanas veids | Precizitāte testa datos |
|---|---:|
| Vienmēr izvēlēties treniņa datos biežāko žanru `rap` | 18,73 % |
| Lēmumu koks ar maksimālo dziļumu 3 | 37,68 % |
| Lēmumu koks ar maksimālo dziļumu 5 | 43,18 % |
| Lēmumu koks ar maksimālo dziļumu 9 | 47,32 % |

Izvēlējos dziļumu 9, jo no pārbaudītajiem variantiem tas šajā datu sadalījumā deva augstāko precizitāti. Starpība pret bāzes līniju bija 28,59 procentpunkti. Tas ir ievērojams uzlabojums, tomēr arī šis modelis kļūdījās vairāk nekā pusē testa piemēru.

## Divas svarīgākās pazīmes

Lielākā nozīme kokā bija tempam (`tempo`, 33,03 %) un runas izteiktībai (`speechiness`, 23,77 %). Šie skaitļi raksturo, cik lielu daļu no kopējā žanru nošķiršanas uzlabojuma apmācības laikā deva katra pazīme. Rezultāts šķiet loģisks, jo temps palīdz atšķirt ātrākus skaņdarbus no lēnākiem, savukārt izteikti ritmiska runa var būt raksturīga repam. Abas pazīmes var pārklāties dažādu žanru dziesmās.

## Vienas kļūdas analīze

| Dziesma | Rindas indekss | Temps (sitieni/min) | Skaļums (dB) | Enerģiskums | Piemērotība dejošanai | Runas izteiktība | Saraksta žanrs | Prognoze |
|---|---:|---:|---:|---:|---:|---:|---|---|
| B2K — *Bump, Bump, Bump* | 19599 | 95,48 | −6,028 | 0,681 | 0,833 | 0,215 | r&b | rap |

Pirmajā koka solī dziesmas runas izteiktība (0,215) pārsniedza slieksni aptuveni 0,164. Tālāk koks pārbaudīja arī enerģiskumu, piemērotību dejošanai un tempu un nonāca pie atbildes `rap`. Manuprāt, kļūda ir saprotama, jo arī R&B dziesmai var būt izteikti ritmiska runa, bet piecas skaitliskās pazīmes pilnībā neapraksta tās skanējumu.

## Modeļa ierobežojums

Šo modeli nevajadzētu izmantot, lai mūzikas katalogā katram ierakstam automātiski piešķirtu vienu oficiālu žanru. Apmācības atbilde bija atskaņošanas saraksta žanrs. Jau sākotnējos datos 1 687 dziesmas bija iekļautas dažādu žanru sarakstos, un šādus gadījumus no apmācības izslēdzu.

## Pašvērtējums

Man izdevās sagatavot datus tā, lai viena dziesma nevarētu nonākt gan treniņa, gan testa izlasē.
Ar izvēlētajām piecām pazīmēm man neizdevās pareizi paredzēt žanru vismaz pusei testa dziesmu.
Nākamreiz koka dziļumu izvēlētos atsevišķā validācijas izlasē un testa datus izmantotu tikai gala modeļa pārbaudei.
