## Questo file contiene opzioni che possono venire cambiate per personalizzare il gioco.

## Fondamentali

## Il nome del gioco in forma leggibile. E' usato per il titolo nella finestra e
## viene impiegato per i resoconti di errore e nell'interfaccia.

## La notazione _() che racchiude la stringa la segna come testo traducibile.

define config.name = _("La Fattoria")

## Determina se il titolo fornito più sopra è mostrato nel main menu. Imposta su
## 'False' per nascondere il titolo.

define gui.show_name = True

## La versione del gioco.

define config.version = "5.0"

## Testo che viene inserito nella schermata informazioni del gioco. Inserisci il
## testo tra triple virgolette e lascia una riga vuota tra i paragrafi.

define gui.about = """
La Fattoria di Nonno Peppino è l'opposto di una normale fattoria, siamo un rifugio dove gli animali non vengono acquistati, venduti, uccisi, mangiati o sfruttati in alcun modo.

In questo rifugio gli animali si riappropriano della loro vita riscoprendo cosa significa essere liberi. Questa libertà non è una concessione straordinaria, ma è un diritto fondamentale per l'esistenza di ogni essere vivente, diritto spesso violato.

Spesso si pensa che gli animali da allevamento non necessitano di attenzioni particolari, come affetto e premura, ma in realtà hanno le medesime esigenze di tutti gli altri animali da compagnia, tra cui vivere liberamente la propria vita. Questo senza che nessuno li consideri inferiori solo per avere il potere di ucciderli a proprio piacimento.

La "fattoria" ha tra le sue principali finalità quella di sviluppare iniziative di carattere sociale per la tutela e la valorizzazione del patrimonio storico, artistico, ambientale e naturale, nonché delle tradizioni e dei prodotti tipici locali. Tutto questo attraverso attività di ricerca e promozione culturale, comunicazione e sviluppo del turismo locale.

In particolare l'associazione si propone di:

- Promuovere attività di insegnamento e messa in pratica dei principi della non violenza, dell'antispecismo, della diffusione della biodiversità, dell'alimentazione a base vegetale (vegetarianismo e veganismo) e della tutela e della salvaguardia dei diritti degli animali;

- Organizzare laboratori didattici pubblici e per scuole;

- Organizzare incontri per la sensibilizzazione e la promozione delle tematiche connesse alla valorizzazione del patrimonio ambientale, naturale e delle tradizioni locali;

- Sensibilizzare sul salvataggio e il recupero di animali di qualsiasi specie, in modo permanente o temporaneo, garantendo allo stesso tempo di prendere cura le loro esigenze specifiche;

- Istituire eventi culturali e conviviali, produrre materiale informativo e svolgere tutte quelle attività atte a perseguire i fini sociali.

Per questi motivi è importante conoscere e diffondere l'esistenza dei rifugi come il nostro, dove protezione e cure sono antispeciste, dove vige il rispetto e l'uguaglianza. Qui nessuno ha paura aspettando una morte violenta, qui l'indifferenza non è contemplata, qui essere liberi è realtà.
"""

define gui.dona = """

Ci sono vari modi per poter supportare la fattoria e tutti gli animaletti che accoglie, clicca {a=https://tr.ee/xFR4VapD2w}qui{/a} per scoprire come.

Per conoscere i nostri animaletti e scoprire tutte le loro storie visita il nostro {a=https://lafattoriadinonnopeppino.wordpress.com}sito{/a} e seguici sui social!!
"""

define gui.credits = """Team:

- Merra Giuseppe - Project manager, Programmazione e Scrittura Dialoghi

- Pansini Giuseppe - Programmazione e Ricerche

- Mastrofrancesco Mattia - Art Director, Grafiche e Ricerche

- Pasquarelli Thomas Pio - Grafiche e Ricerche

Ringraziamento speciale a Sissi Solenne e Simone Mastrofrancesco per i design dei personaggi.

Progetto creato per il corso di Ingegneria del Software 2024/2025 presso il {a=https://www.poliba.it}Politecnico di Bari{/a}
"""

## Un nome abbreviato impiegato dagli eseguibili e dalle cartelle nelle
## distribuzioni compilate. Deve contenere solo caratteri ASCII e non può
## contenere spazi, due punti, o punti e virgole.

define build.name = "Fattoria"

## Suoni e musica

## Queste tre variabili controllano, tra le altre cose, quali mixer vengono
## mostrati al giocatore per impostazione predefinita. Impostando una di queste
## a False, si nasconde il mixer appropriato.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

## Togli # dalla linea seguente per impostare un file audio che sarà riprodotto
## durante il main menu. Continuerà a suonare fino a che non verrà interrotto o
## un altro file audio verrà suonato.

# define config.main_menu_music = "main-menu-theme.ogg"

## Transizioni

## Queste variabili impostano le transizioni che sono usate quando avvengono
## certi eventi. Ogni variabile deve essere impostata su una transizione, o su
## None per indicare che nessuna transizione deve venire usata.

## Entrare o uscire dal game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve

## Tra le schermate del menu di gioco.

define config.intra_transition = dissolve

## Transizione usata dopo che una partita viene caricata.

define config.after_load_transition = dissolve

## Usata quando si torna al main menu dopo che è finita una partita.

define config.end_game_transition = dissolve

## Non esiste una variabile per impostare la transizione da usare quando inizia
## il gioco. Usa un comando 'with' subito dopo aver mostrato la prima 'scene'.

## Gestione finestra

## Controlla come viene mostrata la finestra dei dialoghi. Con "show", viene
## mostrata sempre. Con "hide", è mostrata solo quando ci sono linee di dialogo.
## Con "auto", la finestra è nascosta prima di un comando 'scene' e mostrata di
## nuovo al successivo dialogo.

## Dopo che il gioco ha avuto inizio, questo può essere cambiato coi comandi
## "window show", "window hide", and "window auto".

define config.window = "auto"

## Transizioni usate per mostrare e nascondere la finestra dei dialoghi

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Opzioni predefinite #########################################################

## Controlla la velocità del testo predefinita. Lo standard, 0, è infinito,
## mentre qualunque altro numero indica il numero di caratteri al secondo da
## mostrare.

default preferences.text_cps = 0

## Il ritardo predefinito dell'avanzamento automatico. Numeri alti portano ad
## attese più lunghe, con un intervallo valido da 0 a 30.

default preferences.afm_time = 15

## Percorso Salvataggi

## Controlla dove ren'Py pone i file di salvataggio, secondo la piattaforma. I
## file possono essere posti in:

## Di solito questo non dovrebbe venire cambiato, ma se lo fosse deve sempre
## essere una stringa diretta e non un'espressione.

define config.save_directory = "LaFattoria-1728202575"

## Icona

## L'icona mostrata sulla dock o sulla barra applicazioni.

define config.window_icon = "gui/window_icon.png"

## Configura Compilazione

## Questa sezione controlla come Ren'Py trasforma il tuo progetto in file di
## distribuzione.

init python:

    ## Le funzioni seguenti richiedono schemi di nome. Questi schemi non
    ## differenziano maiuscole e minuscole, e corrispondono al percorso relativo
    ## alla cartella base, con e senza un segno / preposto. Se più schemi
    ## corrispondono, viene usato il primo.
    
    ## In uno schema:
    
    ## / è il separatore fra cartelle.
    
    ## * equivale a qualunque carattere tranne il separatore fra cartelle.
    
    ## ** equivale a qualunque carattere inclusi i separatori fra cartelle.
    
    ## Per esempio, "*.txt" indica file .txt nella cartella base, "game/**.ogg"
    ## indica file .ogg nella cartella base o qualunque sua sottocartella, e
    ## "**.psd" indica file .psd ovunque nel progetto.

    ## Classifica file come 'None' per escluderli dalla compilazione.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Per archiviare i file, classificali come 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## I file che corrispondono a schemi di documentazione sono duplicati nella
    ## compilazione di app Macintosh, quindi appariranno sia nella app che nel
    ## file zip.

    build.documentation('*.html')
    build.documentation('*.txt')

## Per eseguire gli acquisti in-app è necessaria una chiave di licenza
## Google Play. Si trova nella console per sviluppatori di Google Play, in
## "Monetizzazione" > "Impostazione monetizzazione" > "Licenze".

# define build.google_play_key = "..."

## L'username e project name associati a un progetto itch.io, separati da una
## slash.

# define build.itch_project = "renpytom/test-project"
