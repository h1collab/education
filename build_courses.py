from pathlib import Path
from html import escape

ROOT = Path(__file__).parent

grades = {
  "prima": ("Prima media", "01", "Fondamenti"),
  "seconda": ("Seconda media", "02", "Relazioni"),
  "terza": ("Terza media", "03", "Complessità"),
}

subjects = {
"matematica": {
 "name":"Matematica","icon":"∑",
 "prima":[
  ("Numeri naturali e decimali","Valore posizionale, confronto, quattro operazioni e proprietà. Le espressioni si risolvono rispettando parentesi, moltiplicazioni e divisioni, poi addizioni e sottrazioni.","Calcola 48 − 3 × (7 + 1): prima 7 + 1 = 8, poi 3 × 8 = 24, infine 48 − 24 = 24.","Confondere l'ordine delle operazioni; dimenticare di stimare il risultato."),
  ("Potenze e divisibilità","Una potenza abbrevia una moltiplicazione ripetuta. Si studiano multipli, divisori, criteri di divisibilità, numeri primi, MCD e mcm.","84 = 2² × 3 × 7. La scomposizione permette di trovare MCD e mcm.","Credere che 3² sia 3 × 2; includere 1 tra i numeri primi."),
  ("Frazioni","La frazione esprime parte-tutto, quoziente e rapporto. Frazioni equivalenti rappresentano lo stesso numero; si semplifica dividendo numeratore e denominatore per lo stesso fattore.","3/4 + 1/6 = 9/12 + 2/12 = 11/12.","Sommare direttamente i denominatori; semplificare solo uno dei due termini."),
  ("Dati e problemi","Tabelle, grafici, media aritmetica e strategie di problem solving: dati, domanda, piano, calcolo e controllo.","Per 4, 6, 6, 8 la media è 24/4 = 6.","Usare tutti i numeri del testo senza capire la relazione.")
 ],
 "seconda":[
  ("Numeri razionali e radici","Frazioni, decimali finiti e periodici appartengono ai razionali. La radice quadrata è l'operazione inversa del quadrato.","√144 = 12 perché 12² = 144; √50 è compresa tra 7 e 8.","Trattare √(a+b) come √a+√b."),
  ("Rapporti, proporzioni e percentuali","Un rapporto confronta grandezze; una proporzione è un'uguaglianza tra rapporti. Percentuale significa «su cento».","15% di 240 = 0,15 × 240 = 36. Se 3:5=x:20, x=12.","Applicare una percentuale al valore sbagliato; invertire solo un rapporto."),
  ("Proporzionalità e funzioni","Nella proporzionalità diretta y=kx; in quella inversa xy=k. Tabelle e grafici mostrano come variano due grandezze.","A 12 €/kg, 2,5 kg costano y=12×2,5=30 €.","Scambiare una relazione crescente qualsiasi per proporzionalità diretta."),
  ("Probabilità elementare","La probabilità classica è casi favorevoli/casi possibili, quando gli esiti sono equiprobabili.","Con un dado, P(numero pari)=3/6=1/2.","Contare esiti non equiprobabili come se lo fossero.")
 ],
 "terza":[
  ("Numeri relativi","Positivi e negativi descrivono grandezze rispetto a uno zero. Valore assoluto, confronto e operazioni seguono regole dei segni.","−4−(−7)=−4+7=3; (−3)×(−5)=15.","Applicare la regola dei segni anche alle addizioni."),
  ("Calcolo letterale","Monomi e polinomi generalizzano i calcoli. Termini simili si sommano; proprietà distributiva e prodotti notevoli semplificano espressioni.","3x+2x−4=5x−4; (a+b)²=a²+2ab+b².","Sommare termini non simili; dimenticare il termine doppio."),
  ("Equazioni","Un'equazione è un'uguaglianza con incognita. I principi di equivalenza mantengono l'equilibrio tra i membri.","3x−5=16 → 3x=21 → x=7; verifica: 21−5=16.","Cambiare lato cambiando segno senza comprenderne il motivo."),
  ("Statistica e probabilità","Frequenze, media, mediana, moda e campo di variazione descrivono dati. La probabilità confronta eventi e modelli.","In 2,3,3,9 la mediana è 3, la media 4,25: descrivono aspetti diversi.","Usare la media con valori estremi senza commentarla.")
 ]},
"geometria":{"name":"Geometria","icon":"△",
 "prima":[
  ("Enti fondamentali","Punto, retta e piano sono enti primitivi. Segmenti, semirette, rette parallele e perpendicolari costruiscono il linguaggio geometrico.","Due rette perpendicolari formano quattro angoli retti.","Confondere lunghezza del segmento e retta infinita."),
  ("Angoli","Angoli acuti, retti, ottusi, piatti e giro; complementari, supplementari e opposti al vertice.","Se un angolo misura 68°, il suo complementare misura 22°.","Confondere complementare (90°) e supplementare (180°)."),
  ("Poligoni e triangoli","Classificazione per lati e angoli, somma degli angoli interni, altezze, mediane, bisettrici e assi.","In ogni triangolo gli angoli interni sommano 180°.","Pensare che altezza e mediana coincidano sempre."),
  ("Perimetro e area","Il perimetro misura il contorno; l'area misura la superficie. Rettangolo A=b×h, triangolo A=b×h/2.","Triangolo con b=10 cm e h=6 cm: A=30 cm².","Usare unità lineari per l'area.")
 ],
 "seconda":[
  ("Equivalenza delle figure","Figure equiestese hanno la stessa area, anche se forma e perimetro differiscono. Scomposizione e ricomposizione aiutano a dimostrarlo.","Un parallelogramma si trasforma in rettangolo spostando un triangolo laterale.","Concludere che stessa area significa stessa forma."),
  ("Teorema di Pitagora","In un triangolo rettangolo il quadrato dell'ipotenusa equivale alla somma dei quadrati dei cateti.","Cateti 6 e 8: c=√(36+64)=10.","Applicarlo a triangoli non rettangoli; scegliere il lato sbagliato come ipotenusa."),
  ("Similitudine e scala","Figure simili hanno angoli corrispondenti uguali e lati proporzionali. Le aree variano con il quadrato del rapporto.","Scala 1:100: 3 cm nel disegno sono 3 m reali.","Applicare il rapporto lineare direttamente alle aree."),
  ("Circonferenza e cerchio","La circonferenza è il bordo, il cerchio la superficie. C=2πr; A=πr². Archi, corde e angoli al centro.","Con r=5 cm: C=10π cm, A=25π cm².","Confondere r e diametro o circonferenza e area.")
 ],
 "terza":[
  ("Piano cartesiano","Coordinate, distanza tra punti allineati, punto medio e rappresentazione di rette y=mx+q.","La retta y=2x+1 passa per (0,1) e (2,5).","Invertire ascissa e ordinata; usare scale incoerenti."),
  ("Geometria solida","Prismi, piramidi, cilindri, coni e sfere; sviluppo piano, area laterale, totale e volume.","Cilindro: V=πr²h. Con r=3,h=5, V=45π.","Confondere area con volume; dimenticare le basi nell'area totale."),
  ("Peso specifico e solidi","Massa, volume e densità collegano geometria e scienze: d=m/V. I solidi composti si scompongono in forme note.","Un oggetto di 240 g e 80 cm³ ha densità 3 g/cm³.","Mescolare unità non compatibili."),
  ("Trasformazioni e dimostrazione","Traslazioni, rotazioni, simmetrie e omotetie. Una dimostrazione procede da ipotesi note a una tesi con passaggi giustificati.","La simmetria assiale conserva distanze e angoli ma inverte l'orientamento.","Usare il disegno come prova invece di argomentare.")
 ]},
"italiano":{"name":"Italiano","icon":"Aa",
 "prima":[
  ("Grammatica e verbo","Articolo, nome, aggettivo, pronome, preposizione, avverbio, congiunzione e interiezione. Modi, tempi, persona e forma del verbo.","«Avremmo studiato» è condizionale passato, prima persona plurale.","Classificare una parola senza considerare la funzione nella frase."),
  ("Frase semplice","Soggetto, predicato verbale e nominale; attributo, apposizione e primi complementi.","«Luca è felice»: predicato nominale; «Luca corre»: predicato verbale.","Cercare il soggetto solo prima del verbo."),
  ("Testo narrativo","Fabula, intreccio, sequenze, narratore, focalizzazione, personaggi, spazio e tempo.","Un flashback interrompe l'ordine cronologico per raccontare il passato.","Confondere autore reale e narratore."),
  ("Scrittura e lessico","Pianificazione, scaletta, paragrafi, coesione, punteggiatura, revisione; sinonimi, contrari e campi semantici.","Sostituire ripetizioni con sinonimi solo quando il significato resta preciso.","Scrivere senza rileggere o usare connettivi casuali.")
 ],
 "seconda":[
  ("Analisi logica","Complemento oggetto, specificazione, termine, luogo, tempo, causa, fine, mezzo, modo, compagnia e agente.","«Scrivo una lettera a Sara»: una lettera=oggetto; a Sara=termine.","Decidere il complemento dalla sola preposizione."),
  ("Poesia","Verso, strofa, rima, ritmo, enjambement; similitudine, metafora, personificazione, anafora e allitterazione.","«Il mare è uno specchio» è metafora: elimina il «come».","Ridurre la poesia a parafrasi senza analizzare forma e suono."),
  ("Generi e scrittura personale","Diario, lettera, autobiografia, racconto d'avventura, giallo e fantasy hanno scopi e convenzioni differenti.","Una lettera formale richiede destinatario, registro e formule coerenti.","Cambiare registro o tempo verbale senza motivo."),
  ("Letteratura dalle origini al Settecento","Dalla poesia religiosa e stilnovista a Dante, Petrarca, Boccaccio; Rinascimento, teatro e Illuminismo.","Contestualizzare significa collegare opera, lingua, società e intenzione.","Elencare biografie senza leggere i testi.")
 ],
 "terza":[
  ("Analisi del periodo","Proposizione principale, coordinate e subordinate: soggettive, oggettive, relative, temporali, causali, finali, consecutive, concessive e ipotetiche.","«Studio perché voglio capire»: subordinata causale esplicita.","Contare i verbi senza distinguere forme servili o fraseologiche."),
  ("Testo argomentativo","Tema, tesi, argomenti, prove, antitesi, confutazione e conclusione; fonti attendibili e connettivi logici.","Una statistica pertinente sostiene una tesi, ma va citata e interpretata.","Presentare un'opinione come fatto; attaccare la persona invece dell'argomento."),
  ("Letteratura Otto-Novecento","Romanticismo, Verismo, Decadentismo, Ermetismo e narrativa contemporanea; Manzoni, Verga, Pascoli, Pirandello, Ungaretti e altri autori.","Confrontare un tema tra testi è più efficace di riassumere trame separate.","Memorizzare etichette senza evidenze testuali."),
  ("Esame e colloquio","Comprensione, produzione scritta, sintesi e presentazione interdisciplinare. La mappa collega concetti, non solo materie.","Per ogni collegamento formula: idea comune, prova, spiegazione e passaggio.","Creare collegamenti forzati o leggere le slide.")
 ]},
"biologia":{"name":"Biologia","icon":"◉",
 "prima":[
  ("Metodo e viventi","Osservazione, ipotesi, esperimento, dati e conclusione. I viventi sono organizzati, usano energia, rispondono e si riproducono.","Una variabile indipendente viene modificata; quella dipendente viene misurata.","Confondere correlazione e causa."),
  ("Cellula","Membrana, citoplasma e DNA; nucleo e organuli negli eucarioti. Differenze tra cellula animale, vegetale e batterica.","Cloroplasti e parete cellulare caratterizzano la cellula vegetale.","Dire che tutte le cellule hanno nucleo."),
  ("Classificazione","Domini e regni, specie e nomenclatura binomiale; chiavi dicotomiche basate su caratteri osservabili.","Homo sapiens: genere con maiuscola, specie con minuscola.","Classificare solo per ambiente o aspetto."),
  ("Ecologia di base","Habitat, nicchia, popolazione, comunità, ecosistema, catene e reti alimentari.","L'energia fluisce dai produttori ai consumatori e diminuisce a ogni livello.","Dire che la materia «sparisce» lungo la catena.")
 ],
 "seconda":[
  ("Tessuti e apparati","Cellule specializzate formano tessuti, organi e apparati. Struttura e funzione sono collegate.","I villi intestinali aumentano la superficie di assorbimento.","Studiare ogni apparato come sistema isolato."),
  ("Digestione e nutrizione","Nutrienti, enzimi, digestione meccanica e chimica, assorbimento e dieta equilibrata.","L'amido inizia a essere digerito nella bocca dall'amilasi.","Confondere alimento, nutriente e caloria."),
  ("Respirazione e circolazione","Scambi gassosi negli alveoli; cuore, vasi, sangue, piccola e grande circolazione.","Le arterie portano sangue via dal cuore, non sempre ossigenato.","Definire arterie e vene dal contenuto di ossigeno."),
  ("Sistema locomotore e salute","Ossa, articolazioni, muscoli antagonisti, postura, prevenzione e stili di vita.","Bicipite e tricipite lavorano in coppia per flettere ed estendere.","Pensare che il muscolo «spinga» l'osso.")
 ],
 "terza":[
  ("Sistema nervoso ed endocrino","Neuroni, sinapsi, encefalo, midollo e nervi; ormoni e ghiandole coordinano risposte più lente.","Il riflesso può essere elaborato dal midollo prima della percezione cosciente.","Equiparare ogni risposta del corpo a una scelta volontaria."),
  ("Riproduzione e sviluppo","Gametogenesi, fecondazione, ciclo mestruale, gravidanza, pubertà e prevenzione responsabile.","I gameti hanno metà del corredo cromosomico delle cellule somatiche.","Confondere contraccezione e protezione dalle infezioni."),
  ("Genetica","DNA, gene, cromosoma, allele, genotipo e fenotipo; mitosi, meiosi e semplici incroci mendeliani.","Aa × Aa produce rapporti probabilistici, non destini individuali.","Credere che dominante significhi più comune o migliore."),
  ("Evoluzione","Variabilità, selezione naturale, adattamento, speciazione e prove evolutive.","La selezione agisce sulle variazioni presenti; non crea tratti perché necessari.","Pensare che evolvano i singoli individui.")
 ]},
"chimica":{"name":"Chimica","icon":"⚗",
 "prima":[
  ("Materia e misure","Massa, volume, densità, temperatura e strumenti. Proprietà intensive ed estensive descrivono i materiali.","d=m/V: 100 g in 50 cm³ corrispondono a 2 g/cm³.","Confondere massa e peso o leggere male il menisco."),
  ("Stati e passaggi","Solido, liquido, gas e modello particellare; fusione, solidificazione, evaporazione, condensazione e sublimazione.","Durante un passaggio di stato la temperatura può restare costante.","Pensare che le particelle si dilatino invece di aumentare la distanza."),
  ("Miscele e separazioni","Sostanze pure, miscugli omogenei ed eterogenei; filtrazione, decantazione, distillazione, cromatografia.","La distillazione separa componenti con diversi punti di ebollizione.","Credere che una soluzione sia sempre liquida."),
  ("Sicurezza in laboratorio","Pittogrammi, dispositivi di protezione, etichette, procedure e smaltimento.","Si aggiunge l'acido all'acqua, seguendo le istruzioni del laboratorio.","Annusare direttamente o mescolare sostanze senza indicazioni.")
 ],
 "seconda":[
  ("Atomi ed elementi","Protoni, neutroni, elettroni; numero atomico, massa e tavola periodica. Un elemento è definito dai protoni.","Carbonio Z=6: ogni suo atomo ha 6 protoni.","Confondere atomo, elemento e molecola."),
  ("Molecole e composti","Legami formano molecole e reticoli. Le formule indicano tipo e rapporto degli atomi.","H₂O contiene due H per ogni O, non «due grammi e uno».","Cambiare gli indici per bilanciare una reazione."),
  ("Trasformazioni chimiche","Reagenti, prodotti, conservazione della massa e bilanciamento semplice.","2H₂ + O₂ → 2H₂O conserva 4 H e 2 O.","Confondere cambiamento di stato e reazione."),
  ("Soluzioni","Soluto, solvente, solubilità e concentrazione; effetti di temperatura e agitazione.","10 g in 100 mL corrispondono a 0,1 g/mL.","Dire che agitare aumenta sempre la solubilità finale.")
 ],
 "terza":[
  ("Tavola periodica e legami","Gruppi e periodi, metalli e non metalli, elettroni di valenza; legame ionico e covalente a livello introduttivo.","NaCl è descritto come reticolo ionico, non come singola molecola isolata.","Ricavare proprietà solo dalla posizione senza motivarle."),
  ("Acidi, basi e pH","pH, indicatori, neutralizzazione e uso sicuro. Acido e base reagiscono formando sale e acqua in casi semplici.","pH 3 è più acido di pH 5; la scala è logaritmica.","Pensare che «forte» significhi concentrato."),
  ("Reazioni ed energia","Reazioni eso- ed endotermiche, combustione, ossidazione, catalizzatori e velocità di reazione.","Un catalizzatore accelera senza essere consumato nel bilancio complessivo.","Dire che una reazione esotermica «contiene calore»."),
  ("Carbonio e ambiente","Idrocarburi, gruppi organici essenziali, polimeri, ciclo del carbonio, combustibili e impatti.","Bruciare carbonio trasferisce carbonio ai gas atmosferici come CO₂.","Confondere buco dell'ozono ed effetto serra.")
 ]},
"inglese":{"name":"Inglese","icon":"EN",
 "prima":[
  ("Present simple e be","Pronomi soggetto, be, have got, present simple, avverbi di frequenza e forma interrogativa/negativa.","She usually walks to school. Does she walk? Yes, she does.","Aggiungere -s anche dopo does; usare do con be."),
  ("Lessico quotidiano","Family, school, home, routines, hobbies, food, dates, time and weather.","I have breakfast at half past seven.","Tradurre parola per parola espressioni idiomatiche."),
  ("There is e can","There is/are, some/any, preposizioni di luogo, can per abilità e permesso, imperativo.","There are some books, but there isn't any milk.","Usare some in ogni domanda senza considerarne lo scopo."),
  ("Competenze A1","Comprendere messaggi brevi, presentarsi, descrivere persone e routine, scrivere una semplice email.","Hi Alex, I'm writing to tell you about my school...","Omettere saluto, paragrafi e chiusura.")
 ],
 "seconda":[
  ("Past simple","Past simple di be e verbi regolari/irregolari; ago, last, yesterday; domande con did.","We went to Rome last year. Did you go?","Usare il passato dopo did."),
  ("Present continuous e futuro","Azioni in corso; confronto con present simple; be going to e present continuous per piani.","I'm studying now. We're meeting Sam tomorrow.","Usare il continuous con ogni verbo di stato."),
  ("Comparativi e quantità","Comparative, superlative, much/many, a lot of, a few/a little, too/enough.","This route is shorter but more difficult.","Formare more easier; confondere few e little."),
  ("Competenze A1–A2","Raccontare eventi, fare proposte, chiedere informazioni, comprendere testi adattati e scrivere resoconti.","Why don't we visit the museum? That sounds good.","Rispondere senza riprendere tutte le parti della consegna.")
 ],
 "terza":[
  ("Present perfect","Esperienze e risultati collegati al presente; ever, never, just, already, yet, for e since; confronto col past simple.","I've lived here for three years. I moved here in 2023.","Usare un tempo passato finito con present perfect."),
  ("Futuro e condizionale","Will per previsioni/decisioni, going to per intenzioni, first conditional per condizioni possibili.","If we recycle more, we will reduce waste.","Usare will nella proposizione con if."),
  ("Passivo e relativi","Forma passiva introduttiva; who, which, that, where; modali should, must, might.","The book was written in 1949. A person who inspires me...","Dimenticare il participio nel passivo."),
  ("Competenze A2","Comprendere idee principali, interagire in situazioni note, esprimere opinioni motivate e produrre testi connessi.","In my opinion..., however..., for example..., therefore...","Elencare frasi senza connettivi o prove.")
 ]},
"francese":{"name":"Francese","icon":"FR",
 "prima":[
  ("Présent et identité","Pronoms sujets, être, avoir, verbes en -er, articles, genre et pluriel; présentations.","Je m'appelle Léa, j'ai douze ans et j'habite à Lyon.","Dire «je suis douze ans»; dimenticare l'accordo."),
  ("Questions et négation","Est-ce que, intonazione, mots interrogatifs; ne...pas; c'est/ce sont, il y a.","Est-ce que tu aimes le sport ? Je n'aime pas le tennis.","Omettere ne nella scrittura formale."),
  ("Lexique quotidien","Famille, école, maison, jours, mois, nombres, goûts et activités.","Le lundi, je vais au collège à huit heures.","Confondere à, au, aux e en."),
  ("Compétences A1","Comprendre istruzioni semplici, salutare, presentarsi, descrivere e scrivere un messaggio breve.","Bonjour Paul, merci pour ton message... À bientôt !","Usare lo stesso registro con amici e adulti.")
 ],
 "seconda":[
  ("Passé composé","Auxiliaire avoir/être + participe passé; accordo con être; indicatori temporali.","Elle est arrivée hier. Nous avons visité le musée.","Dimenticare l'accordo con être."),
  ("Futur proche et impératif","Aller + infinitif per progetti; imperativo per istruzioni e consigli; pronomi tonici.","Nous allons partir demain. Prenez la deuxième rue !","Coniugare l'infinito dopo aller."),
  ("Comparaison et quantité","Plus/moins/aussi... que, superlatif, partitivi, beaucoup de, peu de.","Cette ville est plus calme que Paris.","Usare des dopo beaucoup."),
  ("Compétences A1–A2","Comprare, ordinare, chiedere indicazioni, raccontare un evento e descrivere un progetto.","Je voudrais un sandwich, s'il vous plaît.","Tradurre «voglio» in modo troppo diretto.")
 ],
 "terza":[
  ("Imparfait et récit","Imparfait per descrizioni/abitudini, passé composé per eventi; connettivi narrativi.","Il faisait froid quand le train est arrivé.","Usare un solo tempo in tutto il racconto."),
  ("Futur simple et conditionnel","Futuro per previsioni e condizionale di cortesia; si + présent, futur.","Si nous agissons, la situation changera. Je voudrais...","Mettere il futuro dopo si."),
  ("Pronoms et relatifs","COD/COI di base, y, en, qui, que, où; posizione dei pronomi.","J'y vais. Le livre que j'ai lu est passionnant.","Scegliere qui/que dal significato italiano anziché dalla funzione."),
  ("Compétences A2","Esprimere opinioni, confrontare culture, comprendere testi autentici brevi e presentare un tema.","À mon avis..., pourtant..., d'une part..., en conclusion...","Memorizzare un testo senza saper rispondere a domande.")
 ]},
"educazione-fisica":{"name":"Educazione fisica","icon":"↗",
 "prima":[
  ("Schemi motori","Camminare, correre, saltare, lanciare, afferrare, rotolare; combinazioni e adattamento allo spazio.","Un percorso combina equilibrio, cambio di direzione e precisione.","Eseguire velocemente prima di controllare il gesto."),
  ("Capacità coordinative","Equilibrio, ritmo, orientamento, reazione e differenziazione; apprendimento motorio.","Variare ritmo e direzione aumenta la capacità di adattamento.","Confondere coordinazione e forza."),
  ("Regole e fair play","Regole essenziali, ruoli, arbitraggio, rispetto e gestione del risultato.","Segnalare correttamente un proprio fallo tutela il gioco.","Considerare l'avversario un nemico."),
  ("Sicurezza","Riscaldamento, abbigliamento, spazi, idratazione e segnalazione del dolore.","Il riscaldamento passa da movimenti generali a specifici.","Allenarsi sul dolore acuto.")
 ],
 "seconda":[
  ("Capacità condizionali","Forza, resistenza, velocità e mobilità; carico, recupero e progressione.","Nella resistenza si aumenta gradualmente durata o intensità.","Aumentare volume e intensità insieme senza recupero."),
  ("Sport di squadra","Fondamentali e tattiche di pallavolo, pallacanestro, calcio o pallamano; occupazione dello spazio.","Passare e smarcarsi crea una nuova linea di gioco.","Seguire tutti la palla e perdere la posizione."),
  ("Atletica e ginnastica","Corsa, salti, lanci, elementi a corpo libero e controllo posturale.","Nel salto, rincorsa, stacco, volo e atterraggio sono fasi collegate.","Trascurare l'atterraggio e la sicurezza."),
  ("Corpo e benessere","Frequenza cardiaca, respirazione, alimentazione, sonno e recupero.","La frequenza cresce con l'intensità e cala nel recupero.","Usare sudore e fatica come unici indicatori di efficacia.")
 ],
 "terza":[
  ("Allenamento","Principi di specificità, gradualità, continuità, individualizzazione e supercompensazione.","Un obiettivo SMART definisce cosa, quanto e quando.","Copiare il programma di un atleta senza adattarlo."),
  ("Tattica e decisione","Leggere spazio, tempo, compagni e avversari; scegliere rapidamente soluzioni efficaci.","Creare superiorità numerica prima di attaccare lo spazio.","Confondere schema rigido e principio tattico."),
  ("Primo soccorso e prevenzione","Condotta PAS: proteggere, allertare, soccorrere nei limiti della formazione; prevenzione degli infortuni.","In emergenza si chiama il numero appropriato e si seguono le istruzioni.","Muovere una persona traumatizzata senza necessità."),
  ("Sport, società ed etica","Doping, inclusione, paralimpiadi, media, stereotipi e valore educativo dello sport.","Valutare una fonte su integratori e prestazioni prima di crederla.","Pensare che «naturale» significhi sempre sicuro.")
 ]},
"storia-geografia":{"name":"Storia e geografia","icon":"◎",
 "prima":[
  ("Alto Medioevo","Caduta dell'Impero romano d'Occidente, regni romano-germanici, Bisanzio, Islam e Carlo Magno.","Una causa politica si collega a trasformazioni economiche, militari e sociali.","Spiegare un evento con una sola causa."),
  ("Feudalesimo e città","Signoria fondiaria, vassallaggio, rinascita dopo il Mille, Comuni, Chiesa e Impero.","Il feudalesimo non è un unico sistema identico in tutta Europa.","Usare termini moderni senza contestualizzarli."),
  ("Geografia fisica d'Europa","Carte, coordinate, rilievi, fiumi, climi, biomi e paesaggi europei.","La scala collega distanza sulla carta e distanza reale.","Confondere meteo e clima."),
  ("Popolazione europea","Densità, migrazioni, urbanizzazione, lingue, religioni e indicatori demografici.","Alta densità non significa automaticamente alta qualità della vita.","Leggere una carta senza legenda e fonte.")
 ],
 "seconda":[
  ("Età moderna","Umanesimo, Rinascimento, esplorazioni, imperi coloniali, Riforma e guerre di religione.","Le esplorazioni collegano innovazioni, interessi e violenze coloniali.","Raccontare la colonizzazione solo dal punto di vista europeo."),
  ("Rivoluzioni","Rivoluzione scientifica, Illuminismo, rivoluzioni americana, francese e industriale.","Confrontare libertà proclamate e gruppi inizialmente esclusi.","Confondere cronologia e causalità."),
  ("Stati europei","Territorio, popolazione, capitale, istituzioni, economia e reti dell'Unione europea.","Confrontare indicatori in rapporto alla popolazione, non solo valori assoluti.","Ridurre uno Stato a stereotipi culturali."),
  ("Cittadinanza europea","Istituzioni UE, diritti, mobilità, moneta per gli Stati aderenti e sfide comuni.","Parlamento, Commissione e Consiglio hanno funzioni diverse.","Confondere Europa geografica e Unione europea.")
 ],
 "terza":[
  ("Ottocento e imperialismo","Industrializzazione, questione sociale, nazionalismi, Unità d'Italia, colonialismo e imperialismo.","Distinguere motivazioni dichiarate e interessi economico-politici.","Descrivere il progresso senza costi sociali."),
  ("Novecento","Guerre mondiali, rivoluzione russa, fascismo, nazismo, Shoah, Resistenza, Repubblica, Guerra fredda e decolonizzazione.","Confrontare fonti, distinguendo testimonianza, documento e interpretazione.","Equiparare fenomeni diversi senza criteri."),
  ("Geografia mondiale","Continenti, popolazione, risorse, reti globali, sviluppo umano, migrazioni, conflitti e sostenibilità.","PIL pro capite e ISU misurano aspetti diversi dello sviluppo.","Usare «Africa» o «Asia» come realtà uniformi."),
  ("Costituzione e cittadinanza","Principi fondamentali, diritti e doveri, separazione dei poteri, istituzioni italiane, ONU e Agenda 2030.","Un diritto richiede istituzioni e responsabilità che lo rendano effettivo.","Confondere legalità, giustizia e opinione personale.")
 ]}
}

def logo():
 return '''<svg class="logo" width="160" height="160" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs><linearGradient id="zorixCore" x1="32" y1="24" x2="130" y2="136" gradientUnits="userSpaceOnUse"><stop offset="0%" stop-color="#2563EB"/><stop offset="45%" stop-color="#06B6D4"/><stop offset="100%" stop-color="#22C55E"/></linearGradient><linearGradient id="zorixZ" x1="45" y1="42" x2="115" y2="118" gradientUnits="userSpaceOnUse"><stop offset="0%" stop-color="#FFF"/><stop offset="100%" stop-color="#E0F2FE"/></linearGradient></defs><rect x="20" y="20" width="120" height="120" rx="34" fill="url(#zorixCore)"/><path d="M48 50H112L92 73H108L55 112L76 86H52L72 63H48Z" fill="url(#zorixZ)"/><path d="M38 92C52 118 91 128 120 96" fill="none" stroke="#FFF" stroke-width="8" stroke-linecap="round" opacity=".35"/><circle cx="116" cy="42" r="7" fill="#FFF" opacity=".9"/><circle cx="42" cy="118" r="5" fill="#FFF" opacity=".65"/></svg>'''

def header():
 return f'''<header class="topbar"><a class="brand" href="index.html">{logo()}<span>zorix education</span></a><nav><a href="index.html">Indice</a><a href="index.html#prima">Prima</a><a href="index.html#seconda">Seconda</a><a href="index.html#terza">Terza</a></nav></header>'''

def page(grade, slug, subject):
 gname, num, phase=grades[grade]; data=subject[grade]
 sections=[]
 for i,(title,theory,example,error) in enumerate(data,1):
  sections.append(f'''<section class="unit" id="unita-{i}"><div class="unit-number">{i:02}</div><div class="unit-body"><p class="eyebrow">Unità {i}</p><h2>{escape(title)}</h2><h3>Teoria essenziale</h3><p>{escape(theory)}</p><div class="example"><strong>Esempio ragionato</strong><p>{escape(example)}</p></div><div class="warning"><strong>Errore da evitare</strong><p>{escape(error)}</p></div><details><summary>Domande di autoverifica</summary><ol><li>Spiega il concetto con parole tue.</li><li>Crea un esempio diverso da quello proposto.</li><li>Quale errore frequente devi saper riconoscere?</li></ol></details></div></section>''')
 checklist=''.join(f'<li><a href="#unita-{i}">{escape(x[0])}</a></li>' for i,x in enumerate(data,1))
 return f'''<!doctype html><html lang="it"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{subject["name"]} · {gname} — Zorix Education</title><meta name="description" content="Corso completo di {subject["name"]} per la {gname}."><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="course.css"></head><body>{header()}<main><section class="course-hero"><a class="back" href="index.html#{grade}">← Torna all'indice</a><div class="course-code">{num} / {subject["icon"]}</div><p class="eyebrow">{gname} · {phase}</p><h1>{subject["name"]}</h1><p class="course-lead">Percorso completo per padroneggiare i nuclei fondamentali, applicarli negli esercizi e prepararli per verifiche ed esame.</p></section><div class="course-layout"><aside><p class="eyebrow">In questa pagina</p><ol>{checklist}</ol><div class="exam-box"><strong>Metodo d'esame</strong><p>Leggi la consegna, individua i dati, spiega il procedimento, controlla il risultato e usa il lessico specifico.</p></div></aside><div class="units">{''.join(sections)}<section class="review"><p class="eyebrow">Ripasso finale</p><h2>Checklist di padronanza</h2><ul><li>So definire i termini senza imparare frasi a memoria.</li><li>So applicare ogni idea a un caso nuovo.</li><li>So motivare i passaggi e correggere gli errori tipici.</li><li>So collegare almeno due unità della materia.</li><li>So spiegare il tema oralmente in tre minuti.</li></ul></section></div></div></main><footer><span>© Zorix Education</span><a href="index.html">Indice generale</a></footer></body></html>'''

def index():
 groups=[]
 for grade,(gname,num,phase) in grades.items():
  cards=''.join(f'''<a class="catalog-card" href="{grade}-{slug}.html"><span class="catalog-icon">{sub["icon"]}</span><div><h3>{sub["name"]}</h3><p>4 unità · teoria, esempi, errori e autoverifica</p></div><span>↗</span></a>''' for slug,sub in subjects.items())
  groups.append(f'''<section class="catalog-year" id="{grade}"><div class="catalog-heading"><p class="eyebrow">{num} · {phase}</p><h2>{gname}</h2><p>Programma organizzato per materia. Ogni scheda apre una pagina HTML indipendente e completa.</p></div><div class="catalog-grid">{cards}</div></section>''')
 return f'''<!doctype html><html lang="it"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Indice completo dei corsi Zorix Education per prima, seconda e terza media."><title>Zorix Education — Indice completo</title><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="course.css"></head><body>{header()}<main><section class="catalog-hero"><p class="eyebrow">Biblioteca dei corsi · 27 pagine</p><h1>Tutto ciò che serve,<br><em>anno per anno.</em></h1><p>Matematica, geometria, italiano, biologia, chimica, inglese, francese, educazione fisica, storia e geografia. Ogni corso è separato, navigabile e pronto per lo studio.</p><div class="quick"><a href="#prima">Prima media</a><a href="#seconda">Seconda media</a><a href="#terza">Terza media</a></div></section>{''.join(groups)}</main><footer><span>© Zorix Education</span><a href="#">Torna su ↑</a></footer></body></html>'''

for grade in grades:
 for slug,subject in subjects.items():
  (ROOT/f"{grade}-{slug}.html").write_text(page(grade,slug,subject),encoding="utf-8")
(ROOT/"index.html").write_text(index(),encoding="utf-8")
print(f"Creati {1+len(grades)*len(subjects)} file HTML.")
