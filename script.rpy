#  Lo script di gioco va in questo file.

#Dichiarazione i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.
define Io = Character ("Player", color="#000000")
define Vito = Character("Vito", color="#5900ff93")
define Sara = Character("Sara", color="#ff00009e")

#Dichiarazione alias per Vito e Sara
define Duo = Character("Vito & Sara", color="#ea00ffca")

#Dichiarazione Guide
define Fiorello = Character("Fiorello", color="#464343")
define Totò = Character("Totò", color="#7b0633")
define Pinpin = Character("Pinpin", color="#d2691e")

#Dichiarazione Personaggi Percorsi
define Luna = Character("Luna", color="#553700")
define Micia = Character("Micia", color="#de73a5")
define Valerio = Character("Valerio", color="#000000")
define Marco = Character("Marco", color="#aba000")
define Vita = Character("Vita", color="#2e5f86")
define Iside = Character("Iside", color="#00ffc89c")
define Wonder = Character("Wonder", color="#26e214a3")

#Dichiarazione flag
default fiorelloflag=False
default totoflag=False
default pinpinflag=False

#Dichiarazione counter per il test
default countertest=0

#Dichiarazione video
image video = Movie(play="images/mv/valerio.webm", size=(549, 684), loop=True)

#Dimensione Sprite 800x1000

#Partenza gioco
label start:

    "Ciao, benvenuto nel gioco!"
    "Come ti chiami?"

    # Chiediamo il nome al giocatore 
    $ player_name = renpy.input("") 
    $ player_name = player_name.strip() 
    if player_name == "": 
        $ player_name = "Io"

    "Perfetto, ora scegli il colore che preferisci tra questi!"

    menu:
        "Rosso":
            $ colore = "#d51919ff"
        "Verde":
            $ colore = "#14b85e8e"
        "Blu":
            $ colore = "#2727b4"     

    $ Io = Character(player_name, color=colore)
            
    "Bene [player_name], ecco che inizia la tua avventura!"

    scene bg neutral with fade
    play music "audio/start.mp3" volume 1
    show text "Nel mezzo delle campagne di Cerignola si trova un luogo veramente magico..." with dissolve
    pause 2.5
    hide text with dissolve
    show text "...un luogo dove ogni animaletto viene rispettato e amato..." with dissolve
    pause 2.5
    hide text with dissolve
    show text "...ma soprattutto un luogo dove ognuno può vivere la propria vita in libertà." with dissolve
    pause 2.5
    hide text with dissolve
    show text "Questo speciale posto si chiama..." with dissolve
    pause 1.5
    hide text with dissolve

    play music "audio/intro.mp3" volume 0.7 loop

    scene bg entrata with fade
    Io "La Fattoria di Nonno Peppino!"
    scene bg cartello
    Io "Finalmente siamo arrivati."
    scene bg cancello
    Io "Che aspettiamo entriamo!"

    menu:
        "Entra":
            jump presentazione

label presentazione:

    scene bg inizio viale with fade

    "???" "Ciao!"
    show vito smile at right with dissolve
    "???" "Benvenuti alla Fattoria di Nonno Peppino."
    show vito normal
    show ph vitosara with dissolve
    Vito "Piacere, io mi chiamo Vito e insieme a mia moglie gestisco questo rifugio."
    show vito smile
    Vito "A proposito, eccola qui!"
    hide ph vitosara with dissolve
    show sara smile at left with dissolve
    Sara "Salve a tutti, mi chiamo Sara, è un piacere conoscervi!"
    show sara normal 
    Sara "Conoscete già il rifugio o è la prima volta che venite a trovarci?"

    menu:
        "Si, conosciamo già la storia del rifugio.":
            Io "Si, conosciamo già la storia del rifugio."
            show sara smile
            show vito normal
            Sara "Perfetto, allora non mi dilungherei sul spiegarvi dove vi trovate."
            show vito smile
            Vito "Però ora vediamo se siete a conoscenza anche di questo fatto."
            jump evento

        "No, è la prima volta che veniamo.":
            Io "No, è la prima volta che veniamo."
            Sara "Allora è giusto spiegarvi dove vi trovate."
            Sara "La Fattoria di Nonno Peppino è un rifugio per animali liberi."
            Sara "Ma un rifugio oltre ad essere un luogo dove gli animali trovano riparo, cibo e cure per tutta la vita è soprattutto uno stato d'animo."
            show sara smile
            Sara "Qui, tutti gli esseri viventi ritrovano serenità e fiducia."
            Sara "Possono essere sè stessi liberamente e vengono aiutati a superare i loro traumi psicologici."
            show sara normal  
            Sara "L'armonia con la natura si percepisce non appena entri, per questo motivo, i rifugi come il nostro prendono il nome di 'Santuario'."
            show sara smile 
            show vito normal
            show ph nonno with dissolve
            Vito "La nostra storia è iniziata nel 2011, quando nonno Peppino ha salvato la cavalla Luna e la pony Bruna da un camion diretto al macello."
            show vito smile 
            show sara normal 
            Vito "Quei due animali sono stati i primi ad arrivare nel terreno che oggi è il nostro rifugio."
            hide ph nonno with dissolve
            Vito "Dopo due anni, ci siamo trasferiti qui, continuando l'attività agricola e accogliendo le prime galline e pecore."
            Vito "All'inizio pensavamo di ricreare una fattoria come quella dei nostri nonni, ma abbiamo vissuto una vera e propria rivoluzione."
            show vito sad 
            show sara sad 
            Vito "Questa esperienza ci ha fatto capire l'ipocrisia e la violenza che ci sono dietro il commercio degli animali."
            show vito normal 
            show sara normal 
            Sara "Da quel momento, abbiamo accolto molti altri animali tra cui asini, capre, maiali, cani, gatti, oche, papere, conigli e pony."
            show sara smile 
            Sara "Oggi, ospitiamo circa un centinaio di animali salvati da allevamenti intensivi, abbandoni e maltrattamenti."
            Sara "Nel 2017, abbiamo fondato un'associazione di promozione sociale per raccogliere fondi e sostenere il nostro lavoro."
            Sara "Grazie a questo impegno, e abbracciando già da anni la carta dei valori della rete dei santuari, il nostro rifugio è stato riconosciuto come il primo santuario del sud Italia."
            show sara normal 
            show vito smile 
            Vito "Le nostre principali finalità sono la promozione della nonviolenza e dell'antispecismo, oltre alla tutela dei diritti degli animali."
            Vito "Crediamo anche nella diffusione della biodiversità e dell'alimentazione naturale e vegetale."
            Vito "Per questo, organizziamo eventi di sensibilizzazione su queste tematiche e coinvolgiamo la comunità."
            show vito normal 
            Sara "Vogliamo che le persone comprendano quanto sia importante prendersi cura degli animali e rispettarli."
            show vito smile 
            show sara smile 
            Sara "Ogni animale qui ha una storia e merita di essere ascoltato e amato, e noi siamo qui per farlo."
            Sara "La Fattoria di Nonno Peppino non è solo un rifugio, è un simbolo di speranza ed amore per gli animali."
            show vito normal 
            Vito "Ora che abbiamo finito le introduzioni è arrivato il momento di parlarvi di una cosa molto importante."
            jump evento
    
label evento:
    show vito rage at right
    show sara sad at left
    Vito "Sapevate che il 50\% della terra abitabile è dedicato all'agricoltura, e di questa, il 77\% è destinato all'allevamento di animali?"
    Vito "Eppure, queste terre producono solo il 18\% del cibo totale per l'umanità."
    show vito sad 
    show sara rage 
    Vito "Con la popolazione mondiale che raggiungerà i 9 miliardi di persone, si prevede che entro il 2050 dovremo aumentare la produzione agricola del 70-110\%."
    Vito "Questo è un problema enorme, perché la terra disponibile è limitata e sempre più terreni vengono disboscati per fare spazio per gli allevamenti e le loro agricolture."
    show vito normal 
    show sara normal 
    Sara "Ma c'è anche un altro aspetto importante, studi recenti hanno messo a confronto l'impatto ambientale di vari prodotti alimentari."
    Sara "Ad esempio, il latte di soia ha un impatto inferiore del 79\% rispetto al latte vaccino, il che lo rende una scelta molto più sostenibile."
    Sara "E non solo il latte: anche il seitan e i legumi hanno un impatto molto minore rispetto alla carne, la quale ha un impatto 6 volte maggiore"
    Sara "In altre parole, a parità di proteine, un chilo di carne è molto più dannoso per l'ambiente rispetto a un chilo di legumi."
    show sara smile 
    Sara "Secondo gli studi, cambiare le abitudini alimentari e ridurre il consumo di carne potrebbe essere uno degli interventi più efficaci per ridurre l'impatto sull'ambiente."
    Sara "Anche solo sostituire una piccola parte degli alimenti di origine animale con quelli vegetali potrebbe migliorare significativamente la sostenibilità del nostro sistema alimentare."
    show sara normal 
    show vito smile 
    Vito "Alla Fattoria di Nonno Peppino, ci impegniamo a sensibilizzare le persone su queste tematiche e a promuovere scelte alimentari più responsabili e sostenibili."
    show sara smile 
    Vito "Oggi siete proprio fortunati, abbiamo organizzato un evento speciale."
    Sara "Sarete guidati in un tour per la fattoria."
    Vito "Conoscerete le storie di alcuni dei nostri ospiti."
    Sara "Ma soprattutto imparerete tante cose nuove su questi importanti temi."
    Vito "Non perdiamoci in chiacchiere, venite con me."
    stop music fadeout 1.0
    jump guide
    
label guide:
    scene bg centro with fade
    play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
    show vito smile at right with dissolve
    Vito "Per il nostro tour evento, avrai il piacere di essere accompagnato da tre guide speciali ed esperte."
    Vito "La prima guida è Fiorello, che vi parlerà di come l'allevamento di animali sia uno dei principali responsabili dei cambiamenti climatici."
    show vito normal
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello smile at left with dissolve
    Fiorello "Ciao, benvenuto! Sarà un piacere spiegarvi come possiamo fare la differenza per il nostro pianeta."
    show fiorello normal
    hide fiorello with dissolve
    show vito smile 
    Vito "Poi, incontrerai Pinpin, che vi guiderà attraverso il mondo dell'alimentazione sostenibile, con un focus sulla dieta plant-based e i suoi benefici per la salute."
    show vito normal
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin smile at left with dissolve
    Pinpin "Ciao! Non vedo l'ora di mostrarvi come tutti possiamo scegliere un'alimentazione più sana e sostenibile."
    show pinpin normal
    hide pinpin with dissolve
    show vito smile 
    Vito "Infine, ci sarà Totò, che ti parlerà di ciò che davvero è il benessere animale."
    show vito normal
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto smile at left with dissolve
    Totò "Ciao! Sarà un piacere mostrarvi quanto è importante rispettare e prendersi cura degli animali."
    show toto normal
    hide toto with dissolve
    show vito smile    
    Vito "Spero che vi divertirete e che imparerete tantissimo oggi! Ogni guida ha preparato un percorso speciale per voi."
    jump scelta
        
label scelta:
    scene bg canestro with fade
    if fiorelloflag==False and pinpinflag==False and totoflag==False:
        show vito smile with dissolve
        Vito "Con quale percorso perferite partire?" 
        menu:
            "Fiorello":
                show vito normal
                Vito "Perfetto! Potrai trovare Fiorello vicino il suo recinto."
                Vito "Vai pure, io ti aspetterò qui!"
                jump fiorello                   
            
            "Pinpin":
                show vito normal
                Vito "Ottimo! Pinpin è nell'area relax, vai pure a trovarlo."
                Vito "Sarò qui ad aspettarti!"
                jump pinpin
            
            "Totò":
                show vito normal
                Vito "Grande! Totò si trova sicuramente nel parcogiochi. Lo conosco bene."
                Vito "Quando avrai finito con lui torna pure qui, ti aspetto!"
                jump toto

    if fiorelloflag==True:

        if totoflag==True and pinpinflag==False:
            play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
            show vito smile with dissolve
            Vito "Bentornato, con che percorso vuoi continuare?"
            menu:
                "Pinpin":
                    show vito normal
                    Vito "Ottimo! Pinpin è nell'area relax, vai pure a trovarlo."
                    Vito "Sarò qui ad aspettarti!"
                    jump pinpin

        elif pinpinflag==True and totoflag==False:
            play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
            show vito smile with dissolve
            Vito "Bentornato, con che percorso vuoi continuare?"
            menu:
                "Totò":
                    show vito normal
                    Vito "Grande! Totò si trova sicuramente nel parcogiochi. Lo conosco bene."
                    Vito "Quando avrai finito con lui torna pure qui, ti aspetto!"
                    jump toto

        elif totoflag==False and pinpinflag==False:
            play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
            show vito smile with dissolve
            Vito "Bentornato, con che percorso vuoi continuare?"
            menu:                 
                "Pinpin":
                    show vito normal
                    Vito "Ottimo! Pinpin è nell'area relax, vai pure a trovarlo."
                    Vito "Sarò qui ad aspettarti!"
                    jump pinpin
            
                "Totò":
                    show vito normal
                    Vito "Grande! Totò si trova sicuramente nel parcogiochi. Lo conosco bene."
                    Vito "Quando avrai finito con lui torna pure qui, ti aspetto!"
                    jump toto

    elif totoflag==True:

        if fiorelloflag==True and pinpinflag==False:
            play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
            show vito smile with dissolve
            Vito "Bentornato, con che percorso vuoi continuare?"
            menu:
                "Pinpin":
                    show vito normal
                    Vito "Ottimo! Pinpin è nell'area relax, vai pure a trovarlo."
                    Vito "Sarò qui ad aspettarti!"
                    jump pinpin

        elif pinpinflag==True and fiorelloflag==False:
            play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
            show vito smile with dissolve
            Vito "Bentornato, con che percorso vuoi continuare?"
            menu:
                "Fiorello":
                    show vito normal
                    Vito "Perfetto! Potrai trovare Fiorello vicino il suo recinto."
                    Vito "Vai pure, io ti aspetterò qui!"
                    jump fiorello

        elif pinpinflag==False and fiorelloflag==False:
            play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
            show vito smile with dissolve
            Vito "Bentornato, con che percorso vuoi continuare?"
            menu:                 
                "Fiorello":
                    show vito normal
                    Vito "Perfetto! Potrai trovare Fiorello vicino il suo recinto."
                    Vito "Vai pure, io ti aspetterò qui!"
                    jump fiorello

                "Pinpin":
                    show vito normal
                    Vito "Ottimo! Pinpin è nell'area relax, vai pure a trovarlo."
                    Vito "Sarò qui ad aspettarti!"
                    jump pinpin
            
    else:

        if fiorelloflag==True and totoflag==False:
            play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
            show vito smile with dissolve
            Vito "Bentornato, con che percorso vuoi continuare?"
            menu:
                "Totò":
                    show vito normal
                    Vito "Grande! Totò si trova sicuramente nel parcogiochi. Lo conosco bene."
                    Vito "Quando avrai finito con lui torna pure qui, ti aspetto!"
                    jump toto

        elif totoflag==True and fiorelloflag==False:
            play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
            show vito smile with dissolve
            Vito "Bentornato, con che percorso vuoi continuare?"
            menu:
                "Fiorello":
                    show vito normal
                    Vito "Perfetto! Potrai trovare Fiorello vicino il suo recinto."
                    Vito "Vai pure, io ti aspetterò qui!"
                    jump fiorello

        elif totoflag==False and fiorelloflag==False:
            play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
            show vito smile with dissolve
            Vito "Bentornato, con che percorso vuoi continuare?"
            menu:                 
                "Fiorello":
                    show vito normal
                    Vito "Perfetto! Potrai trovare Fiorello vicino il suo recinto."
                    Vito "Vai pure, io ti aspetterò qui!"
                    jump fiorello

                "Totò":
                    show vito normal
                    Vito "Grande! Totò si trova sicuramente nel parcogiochi. Lo conosco bene."
                    Vito "Quando avrai finito con lui torna pure qui, ti aspetto!"
                    jump toto        

    if fiorelloflag==True and pinpinflag==True and totoflag==True:
        play music "audio/guide.mp3" volume 0.7 fadein 1.0 loop
        show vito smile with dissolve
        Vito "Congratulazione! Avete completato tutti i percorsi."
        show vito normal
        Vito "Venite con me ora, c'è Sara che vi aspetta."
        stop music fadeout 1.0
        jump test

label fiorello:
    stop music fadeout 1.0
    scene bg cerchio with fade
    play music "audio/fiorello.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello smile at left with dissolve
    Fiorello "Benvenuti a tutti al nostro santuario! È un vero piacere vedervi qui oggi."
    show fiorello normal
    show ph fiore 0 with dissolve
    Fiorello "Io sono Fiorello, un bue un po' speciale: sono cieco, ma non per questo meno curioso di scoprire il mondo attraverso i vostri racconti e le emozioni che condividiamo."
    hide ph fiore 0 with dissolve
    show fiorello smile
    Fiorello "Oggi inizieremo insieme un viaggio per comprendere meglio il nostro pianeta, i cambiamenti climatici e i danni che l'uomo ha causato all'ambiente."
    Fiorello "È un tema importante, e sono certo che, insieme, potremo riflettere su come fare la differenza."
    show fiorello normal
    Fiorello "Prima di iniziare, però, vorrei raccontarvi una piccola parte della mia storia."
    Fiorello "Credo che conoscere un po' di me vi aiuterà a capire meglio perché sono qui a parlarvi di queste cose."
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show fiorello sad
    Fiorello "All'inizio della mia vita, le cose non sono state facili. Il mio allevatore non aveva molta pazienza con me e, visto che non vedevo, pensava che fossi solo un peso."
    show fiorello normal
    show ph fiore 1 with dissolve
    Fiorello "Quando avevo solo pochi mesi, voleva sbarazzarsi di me, ma fortunatamente Vito e Sara sono venuti in mio soccorso."
    hide ph fiore 1 with dissolve
    show fiorello smile
    show ph fiore 2 with dissolve
    Fiorello "Invece di darmi il latte in polvere hanno scelto di comprare il latte della mia mamma, per farmi crescere come dovevo."
    hide ph fiore 2 with dissolve
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show ph fiore 3 with dissolve
    Fiorello "Grazie a questa scelta, sono cresciuto sano e forte nonostante la mia cecità. Ora ho 5 anni e vivo tranquillamente alla Fattoria di Nonno Peppino."
    hide ph fiore 3 with dissolve
    show fiorello normal
    show ph fiore 4 with dissolve
    Fiorello "Mi sono adattato molto bene al mio ambiente, so esattamente dove sono il cibo e l'acqua, e mi sposto con sicurezza, anche se ogni tanto mi capita ancora di sbattere le corna."
    Fiorello "Molti visitatori non si accorgono nemmeno che sono cieco, perché non mi fermo mai e sono sempre gentile e affettuoso con tutti."
    hide ph fiore 4 with dissolve
    show fiorello smile
    show ph fiore 5 with dissolve
    play sound "audio/sfx/fiore 2.mp3" volume 1
    Fiorello "La mia cecità, in fondo, non mi impedisce di vivere una vita piena."
    Fiorello "Dicono che 'io vedo con il cuore', ed è proprio così."
    Fiorello "Mi piace essere un esempio di come la gentilezza e l'empatia possano superare qualsiasi difficoltà."
    hide ph fiore 5 with dissolve
    show fiorello normal
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show ph fiore 6 with dissolve
    Fiorello "Da un anno, inoltre, sono diventato il fratellone adottivo di Valerio, il bufalino, che è un po' più giovane di me."
    Fiorello "Ci prendiamo cura l'uno dell'altro, come una vera famiglia."
    hide ph fiore 6 with dissolve
    show fiorello smile
    show ph fiore 7 with dissolve
    Fiorello "Quindi, anche se non posso vedere come voi, vedo ogni giorno l'importanza dell'amore e della compassione."
    Fiorello "E questa è la mia visione del mondo!"
    hide ph fiore 7 with dissolve
    play sound "audio/sfx/fiore 2.mp3" volume 0.8
    show fiorello normal
    Fiorello "Detto questo c'è un'altra cosa importante che vorrei raccontarti, e riguarda le mucche come me e il cambiamento climatico."
    Fiorello "Insieme ad altri animali da pascolo, noi bovini, contribuiamo in modo significativo alla produzione di gas serra."
    Fiorello "Sapete che gas produciamo?"

    menu:
        "Metano":
            Io "Dovrebbe essere il metano."
            play sound "audio/sfx/fiore 1.mp3" volume 0.8
            show fiorello smile
            Fiorello "Esatto, produciamo metano attraverso il nostro processo di digestione."
        "Ossigeno":
            Io "Dovrebbe essere l'ossigeno."
            play sound "audio/sfx/fiore 1.mp3" volume 0.8
            show fiorello normal
            Fiorello "Eh no, l'ossigeno è vitale per gli esseri umani. La risposta corretta è il metano."
            Fiorello "Lo produciamo attraverso il nostro processo di digestione."
        "Elio":
            Io "Dovrebbe essere l'elio."
            play sound "audio/sfx/fiore 1.mp3" volume 0.8
            show fiorello normal
            Fiorello "Eh no, l'elio si trova nelle stelle. La risposta corretta è il metano."
            Fiorello "Lo produciamo attraverso il nostro processo di digestione."

    show fiorello normal
    Fiorello "Noi bovini abbiamo uno stomaco speciale, suddiviso in più parti."
    Fiorello "La prima è il rumine, dove dei batteri fermentano il cibo per aiutarmi a digerire le piante che mangio."
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show fiorello sad
    Fiorello "Ma questo processo produce metano, che viene rilasciato quando ... beh, facciamo un po' di 'rumori'! E non finisce qui."
    Fiorello "Anche il nostro letame, se viene conservato senza ossigeno, può generare metano e protossido di azoto, un altro gas serra che peggiora il cambiamento climatico."
    show fiorello rage
    Fiorello "La produzione di cibo in generale causa più di 17 miliardi di tonnellate di emissioni di CO2 all'anno!"
    Fiorello "Il 57\% di queste viene dalla produzione di alimenti di origine animale, come carne e latte."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    Fiorello "Il metano però è 34 volte più efficace della CO2 nel trattenere calore, anche se resta meno tempo nell'atmosfera."
    Fiorello "Circa il 34\% del metano totale prodotto dall'uomo viene dall'estrazione di combustibili fossili, come gas e petrolio."
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show fiorello sad
    Fiorello "Noi animali allevati per il cibo, invece, ne produciamo il 27\%."
    Fiorello "Alcuni paesi, come l'Irlanda, stanno considerando misure drastiche per ridurre queste emissioni, addirittura riducendo il numero di bovini di migliaia di capi."
    Fiorello "Queste decisioni però sono completamente prive di eticità e moralità."
    Fiorello "Dopo tutto, siamo esseri viventi e abbiamo diritto di vivere."
    show fiorello rage
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    Fiorello "Qui in Italia le emissioni degli allevamenti rappresentano il 14,5\% del totale, ma in altre parti del mondo la situazione è molto più grave."
    show fiorello normal
    Fiorello "Resta molto da fare per ridurre ulteriormente l'impatto ambientale degli allevamenti."
    Fiorello "E se vi state chiedendo cosa potremmo fare tutti insieme per migliorare la situazione, ci sono vari modi!"
    show fiorello smile
    play sound "audio/sfx/fiore 2.mp3" volume 1
    Fiorello "Ridurre il consumo di carne e latticini, per esempio, può aiutare a diminuire la domanda e l'impatto ambientale."
    Fiorello "Oppure potremmo incentivare alternative alle proteine animali, come le proteine vegetali o la carne sintetica, che producono molti meno gas serra."
    Fiorello "Infine, è importante anche richiedere cambiamenti nelle politiche. Supportare leggi e regolamenti per ridurre le emissioni degli allevamenti può fare una grande differenza."
    show fiorello normal
    Fiorello "Dopotutto, proteggere l'ambiente è una responsabilità di tutti, e ogni piccolo gesto conta!"
    Fiorello "Adesso però  vieni con me, ti presenterò un'ospite del rifugio davvero speciale. La sua storia è incredibile."
    stop music fadeout 1.0
    jump luna

label luna:
    scene bg stalla with fade
    play music "audio/luna.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello smile at left with dissolve
    Fiorello "Ciao, Luna! Come stai oggi? Tutto bene?"
    show fiorello normal
    show luna smile at right with dissolve
    play sound "audio/sfx/luna 2.mp3" volume 1
    Luna "Ciao Fiorello, sto bene, grazie! Solo un po' di acciacchi qui e là, dovuti all'età, ma niente di grave."
    Fiorello "Sono molto felice di sentire che stai bene!"
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show luna normal 
    Fiorello "Ragazzi, vi presento Luna."
    Fiorello "Lei è stata una delle prime a venire qui al rifugio."
    show fiorello sad 
    Fiorello "Arrivò insieme a Bruna, una pony che purtroppo è venuta a mancare nel 2017."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello normal 
    Fiorello "Erano qui all'inizio, nel 2011, quando nonno Peppino ha preso una decisione che ha cambiato le loro vite."
    Fiorello "Racconta un po' la tua storia a questi nostri nuovi amici, ti ascoltiamo con tanto affetto."
    hide fiorello with dissolve
    play sound "audio/sfx/luna 1.mp3" volume 0.8
    show luna smile 
    Luna "Salve a tutti, è un piacere poter fare la vostra conoscenza."
    show luna normal
    show ph luna 0 with dissolve
    Luna "Come avete sentito mi chiamo Luna e, beh, la mia storia è un po' lunga, ma ci provo a raccontarla."
    hide ph luna 0 with dissolve
    show ph bruna with dissolve
    Luna "Nonno Peppino mi ha visto per la prima volta quando ero molto giovane, insieme alla mia amica Bruna."
    hide ph bruna with dissolve
    play sound "audio/sfx/luna 2.mp3" volume 1
    show luna sad 
    Luna "Eravamo su un camion diretto al macello, proprio come tanti altri cavalli." 
    show luna smile 
    Luna "Ma lui, che era un uomo di cuore, ha visto qualcosa in noi."
    show luna normal
    show ph luna 1 with dissolve
    Luna "Mi ricordo che nonno Peppino mi ha guardato e sembrava ricordarsi di un cavallo che aveva avuto quando era bambino."
    Luna "In quel momento, decise che non ci avrebbe mai lasciato finire in un macello."
    hide ph luna 1 with dissolve
    play sound "audio/sfx/luna 1.mp3" volume 0.8
    Luna "Il signore che ci trasportava gli doveva dei soldi per dei lavori in agricoltura, ma Peppino ci rinunciò per chiedergli di liberarci."
    show luna smile
    Luna "Non lo dimenticherò mai."
    show luna normal
    show ph luna 2 with dissolve
    Luna "Quando arrivai qui al rifugio, sentii per la prima volta di essere davvero libera."
    hide ph luna 2 with dissolve
    show ph luna 3 with dissolve
    Luna "Non c'erano più né camion né paure, solo la compagnia di nuovi amici, tutti liberi di vivere in pace."
    hide ph luna 3 with dissolve
    play sound "audio/sfx/luna 2.mp3" volume 1
    show ph luna 4 with dissolve
    Luna "Ora ho 14 anni, e devo dire che sono abbastanza vecchietta. Ma qui sto benissimo, sempre coccolata e protetta."
    hide ph luna 4 with dissolve
    show ph luna 5 with dissolve
    Luna "Ogni tanto mi sento come una nonnina che racconta storie ai più giovani, ma è bello sentirsi così amata."
    hide ph luna 5 with dissolve
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello smile at left with dissolve 
    Fiorello "La storia di Luna è un esempio di come la gentilezza e l'amore possano cambiare la vita di un animale."
    Fiorello "Ogni volta che ci fermiamo a riflettere, possiamo fare la differenza, come ha fatto nonno Peppino per lei."
    show fiorello normal
    Fiorello "Luna, grazie per aver condiviso la tua storia. È davvero speciale sentire quanto amore hai trovato qui."
    Fiorello "Sono davvero felice che tu possa vivere i tuoi anni da 'nonnina' circondata da chi ti vuole bene."
    show fiorello smile 
    Fiorello "È un privilegio raro per noi animali, e tu te lo meriti tutto."
    play sound "audio/sfx/luna 2.mp3" volume 1
    show luna smile
    Luna "Oh, grazie Fiorello caro, è sempre un piacere chiacchierare con te. Sei così gentile!"

    play sound "audio/sfx/fiore 2.mp3" volume 1
    show fiorello normal
    Fiorello "Di nulla, ma adesso dimmi Luna, che cosa hai mangiato oggi a colazione? Un po' di fieno magari?"
    play sound "audio/sfx/luna 1.mp3" volume 0.8
    show luna normal
    Luna "Oh, sì, certo! Mangio sempre i miei soliti mangimi, un po' di fieno e qualcosa di speciale ogni tanto."
    show luna smile
    Luna "Mi piace tanto quando il mio piatto è ben pieno."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    Fiorello "Già, ma sai, Luna, a volte i mangimi che mangiamo non sono così semplici come sembrano."
    Fiorello "Spesso ci sono anche altri ingredienti, come la soia. Un legume che viene usato tantissimo nei mangimi per animali, come noi."
    show luna surprised 
    Luna "La soia? Non mi è mai venuto in mente che possa avere effetti negativi... che cosa c'è di sbagliato nella soia?" 
    show fiorello rage
    show luna sad
    Fiorello "La soia è una delle fonti proteiche principali nei mangimi per gli animali da allevamento." 
    Fiorello "In pratica, quando gli esseri umani mangiano carne o latticini, una gran parte della soia che viene coltivata nel mondo finisce nei mangimi degli animali."
    play sound "audio/sfx/luna 2.mp3" volume 1
    Luna "Quindi più carne mangiano le persone, più cresce la domanda di soia?"
    show fiorello sad 
    play sound "audio/sfx/fiore 2.mp3" volume 1
    Fiorello "Esattamente! Più la domanda di carne e latticini cresce, più c'è bisogno di mangimi a base di soia, e quindi la coltivazione della soia esplode."
    Fiorello "Questo crea un circolo vizioso più mangiamo carne, più la deforestazione aumenta."
    Luna "Oh cielo come la deforestazione aumenta... la soia è davvero così dannosa per le foreste?"
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello rage 
    Fiorello "Purtroppo si. La soia, per poter essere coltivata in grandi quantità, viene piantata in enormi campi, spesso su terreni sottratti alle foreste."
    Fiorello "La soia è diventata il secondo principale responsabile della deforestazione globale, dopo gli allevamenti di bovini."
    Fiorello "Dal 1990 vengono abbattute foreste immense, come quelle in Brasile, in Amazzonia."
    Fiorello "Pensate che in meno di 10 anni, la produzione di soia in alcuni paesi sudamericani è aumentata del 123\%!"
    play sound "audio/sfx/luna 1.mp3" volume 0.8
    show luna surprised 
    Luna "E cosa succede dopo che abbattono la foresta?"
    show fiorello sad
    show luna sad
    Fiorello "Purtroppo, una volta abbattute le foreste, il terreno viene bruciato per prepararlo alla coltivazione."
    show fiorello rage 
    Fiorello "Questo sistema, che si chiama 'taglia e brucia', è devastante. Non solo distrugge le piante, ma crea anche incendi che si propagano velocemente."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello sad
    show luna surprised
    Fiorello "Nel solo mese di giugno 2020, in Amazzonia ci sono stati più di 2.200 incendi, un numero molto alto, e ogni anno la situazione peggiora."
    show luna sad
    Fiorello "Gli incendi e l'uso di pesticidi danneggiano l'ecosistema in maniera enorme. I pesticidi contaminano il suolo e l'acqua, che poi finisce nei fiumi, anche nel Rio delle Amazzoni."
    Fiorello "Le piante e gli animali che vivono lì non sopravvivono, e tutto il sistema naturale viene inquinato."
    play sound "audio/sfx/luna 2.mp3" volume 1
    Luna "Oh, poveri animali... ma la soia si usa solo per creare i nostri mangimi?"
    show fiorello rage
    Fiorello "L'80\% della soia prodotta nel mondo viene usata come mangime per gli animali, mentre solo il 6\% viene consumato direttamente dagli esseri umani."
    Fiorello "Ogni anno, vengono distrutti oltre 1,5 milioni di ettari di foresta per far posto alle piantagioni di soia."
    play sound "audio/sfx/fiore 2.mp3" volume 1
    Fiorello "Ma c'è anche un'altra causa: l'espansione dei pascoli per gli allevamenti intensivi. Il Brasile è anche uno dei maggiori esportatori di carne."
    show fiorello sad
    show luna surprised
    Fiorello "Nel 2018, il Brasile ha esportato circa 1,64 milioni di tonnellate di carne, l'11\% in più rispetto all'anno precedente."
    show luna sad
    Fiorello "E le zone dove si coltiva la soia sono le stesse dove vengono creati pascoli per gli animali. E tutte queste terre sono quelle più colpite da incendi devastanti."
    play sound "audio/sfx/luna 1.mp3" volume 0.8
    Luna "Non pensavo che tutto fosse collegato in questo modo, povera Amazzonia. Non mi piace pensare a quanta foresta se ne va ogni anno..."
    Fiorello "Ad oggi, l'Amazzonia è stata disboscata del 15\% rispetto al suo stato originale."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello rage 
    Fiorello "Ma il problema è che, se la deforestazione supera il 25\%, l'intero ciclo dell'acqua della regione potrebbe crollare."
    Fiorello "La foresta potrebbe trasformarsi in una savana, e il cambiamento climatico peggiorerebbe ulteriormente."
    show luna sad
    Luna "Quindi l'acqua che scorre lì, che tiene viva la foresta, potrebbe sparire?"
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show fiorello sad 
    Fiorello "Esattamente, e non solo l'ambiente ne risentirebbe."
    show luna surprised
    Fiorello "Le popolazioni indigene che vivono nella foresta sono anche vittime di questa politica di sfruttamento, i quali sono costretti a vedere le loro terre occupate e distrutte."
    show luna sad
    Fiorello "E l'Italia, purtroppo, contribuisce a tutto questo."
    Fiorello "Nonostante il governo brasiliano non protegga né l'ambiente né i diritti umani, l'Italia è uno dei maggiori importatori di soia dal Brasile."
    play sound "audio/sfx/luna 2.mp3" volume 1
    Luna "Davvero? L'talia importa così tanta soia dal Brasile?"
    show fiorello rage
    show luna surprised
    Fiorello "Sì. Dal 2020 al 2024, l'Italia ha importato il 10\% della soia che è arrivata in Europa, pari a oltre 4 milioni di tonnellate."
    Fiorello "La maggior parte di questa soia arriva dal Brasile, nonostante tutti i danni ambientali e i diritti umani violati."
    show fiorello sad
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show luna sad
    Fiorello "E la nostra importazione di soia brasiliana è ancora aumentata."
    Fiorello "È davvero triste pensare che, mentre noi facciamo il possibile per proteggere la natura, altre persone continuano a favorire la distruzione."
    play sound "audio/sfx/luna 1.mp3" volume 0.8
    Luna "Ma cosa possiamo fare noi per fermare questa catastrofe?"
    show fiorello normal
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show luna normal 
    Fiorello "Beh, si potrebbe iniziare riducendo il consumo di derivati animali, perché meno animali alleviamo, meno soia serve per nutrirli."
    Fiorello "Anche mangiare più verdure e cercare alternative vegetali può fare una grande differenza!"
    play sound "audio/sfx/luna 2.mp3" volume 1
    show luna smile
    Luna "Quindi, cambiando alimentazione, si può davvero aiutare l'ambiente!"
    show fiorello smile
    Fiorello "Esattamente, Luna! E poi, possiamo educare le persone, farle capire che le scelte che fanno influenzano anche ciò che succede nei paesi lontani. Informarsi è il primo passo."
    show luna normal 
    Luna "Se più persone sapessero, forse la situazione potrebbe migliorare."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello normal
    Fiorello "Proprio così. E se più persone decidono di comprare prodotti che non provengono da fonti distruttive per l'ambiente, possiamo fare davvero la differenza."
    Fiorello "Ogni scelta che facciamo conta. Se tutti facciamo la nostra parte, possiamo fermare la distruzione e proteggere il nostro pianeta."
    play sound "audio/sfx/luna 1.mp3" volume 0.8
    Luna "Non è mai troppo tardi per cambiare, vero?"
    show fiorello smile
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show luna smile 
    Fiorello "Mai troppo tardi, Luna. Ogni piccola azione può portare a grandi risultati. E noi possiamo fare la differenza, insieme."
    show fiorello normal 
    Fiorello "Grazie mille per il tuo tempo, è stato davvero bello parlare con te."
    Fiorello "Purtroppo, è ora che io e i visitatori andiamo altrove nel rifugio."
    play sound "audio/sfx/luna 2.mp3" volume 1
    show luna normal 
    Luna "Grazie a te, Fiorello, è stato davvero bello chiacchierare."
    Luna "Spero che vi divertiate esplorando il rifugio! A presto, cari amici!"
    hide luna with dissolve
    show fiorello smile 
    Fiorello "Venite con me ragazzi, vi mostrerò quanto è davvero bello qui!"
    stop music fadeout 1.0
    jump micia

label micia:
    scene bg laboratorio with fade
    play music "audio/micia.mp3" volume 0.7 fadein 1.0 loop
    show fiorello normal at left with dissolve
    Fiorello "Ci sono tanti animaletti speciali in questa fattoria, ognuno con la sua storia da raccontare."
    Fiorello "Come Micia, che è la mamma di tutti i gatti qui al rifugio!"
    show fiorello smile
    Fiorello "Dovrebbe essere da queste parti, è sempre nel laboratorio a fare dolci."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    Fiorello "Micia esci fuori se ci sei!"
    show micia smile at right with dissolve
    play sound "audio/sfx/micia 2.mp3" volume 2
    Micia "Eccomi! Ciao Fiore, è sempre un piacere vedere il tuo testone."
    Fiorello "Ciao Micia! Come va oggi?"
    show micia normal
    Micia "Sto bene grazie, mi prendo cura dei miei piccoli e preparo squisiti dolci per loro."
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show fiorello normal
    Fiorello "Sono felice di sentirlo, vieni, stavamo giusto parlando di te!"
    Fiorello "Ti va di raccontare la tua storia a questi nuovi amici. Siamo tutti curiosi di ascoltarti con attenzione."
    show micia smile
    Micia "Certo, va bene!"
    hide fiorello with dissolve
    play sound "audio/sfx/micia 1.mp3" volume 0.5
    show ph micia 0 with dissolve
    Micia "Ciao a tutti, mi chiamo Micia e, come tutti gli altri animaletti che abitano qui, anch'io devo tanto a questo rifugio."
    hide ph micia 0 with dissolve
    show micia normal
    show ph micia 1 with dissolve
    Micia "Tanto tempo fa ero solo una gattina randagia che vagava per le campagne, finché un giorno sono finita, fortunatamente, qui."
    Micia "Mi venne subito offerto riparo e del cibo, ma avevo paura di affezionarmi troppo."
    hide ph micia 1 with dissolve
    show micia sad
    play sound "audio/sfx/micia 2.mp3" volume 2
    show ph micia 2 with dissolve
    Micia "C'erano tanti cani, e la strada lì vicino era pericolosa per me. Non volevo correre rischi."
    hide ph micia 2 with dissolve
    show micia smile
    show ph micia 3 with dissolve
    Micia "Poi, però, è successo qualcosa di speciale."
    Micia "Dopo essere rimasta incinta, ho deciso di partorire i miei piccoli nel pollaio del rifugio, un posto tranquillo dove poterli allattare senza preoccupazioni."
    hide ph micia 3 with dissolve
    play sound "audio/sfx/micia 1.mp3" volume 0.5
    show micia normal  
    Micia "Subito dopo, Vito e Sara hanno adottato me e i miei piccoli."
    Micia "Per proteggermi avevano intenzione di sterilizzarmi, ma quando mi hanno portato dal veterinario hanno scoperto che ero di nuovo incinta!"
    show micia smile
    show ph micia 4 with dissolve
    Micia "Così, ho fatto nascere la mia seconda cucciolata."
    Micia "È stato un periodo difficile ma anche pieno di amore e speranza."
    hide ph micia 4 with dissolve
    show micia normal
    play sound "audio/sfx/micia 2.mp3" volume 2
    show ph micia 5 with dissolve
    Micia "Da allora vivo qui con i miei gattini e non potrei essere più felice di far parte di questa famiglia che mi ha accolta."
    hide ph micia 5 with dissolve
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello smile at left with dissolve
    Fiorello "Sono così felice che tu e i tuoi piccoli abbiate trovato un posto sicuro e pieno d'amore qui al rifugio."
    Fiorello "Non è sempre facile, ma è bello sapere che ci sono persone come Vito e Sara pronte a fare la differenza."
    show fiorello normal
    Fiorello "Grazie di cuore, Micia, per aver condiviso la tua storia con noi."
    Fiorello "Credo che tutti, qui, abbiano apprezzato il tuo racconto e la forza che dimostri ogni giorno."
    play sound "audio/sfx/micia 1.mp3" volume 0.5
    show micia smile
    Micia "Non devi ringraziarmi Fiore, è sempre bello parlare con te!"

    play sound "audio/sfx/fiore 2.mp3" volume 1
    Fiorello "A proposito, oggi sto facendo da guida e sto parlando ai visitatori dei cambiamenti climatici."
    Fiorello "Hai mai sentito parlare di come tutto questo stia influenzando anche gli animali?"
    play sound "audio/sfx/micia 2.mp3" volume 2
    show micia sad 
    Micia "Oh, sì... I miei amici pesci, che vivono nel vascone, mi raccontano spesso di come i loro simili stiano soffrendo nel mondo."
    Micia "Mi hanno detto che i loro habitat vengono distrutti e che l'acqua sta diventando sempre più inquinata, a volte non riescono più a respirare bene."
    Micia "È davvero triste vedere quanto le azioni degli esseri umani stiano danneggiando l'ambiente in cui vivono. I miei amici pesci sono così preoccupati..."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello sad 
    Fiorello "Conosco bene il problema di cui parlano i tuoi amici pesci, Micia."
    Fiorello "Sai, una delle pratiche peggiori è la pesca a strascico."
    show micia surprised
    Fiorello "Immagina una gigantesca rete trascinata sul fondo del mare: raccoglie tutto quello che trova, causando grandi danni e uccidendo anche animali che non servono ai pescatori."
    show fiorello rage
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show micia sad
    Fiorello "Come le tartarughe marine, che possono soffocare nella rete."
    Fiorello "Anche se vengono rilasciate, spesso è troppo tardi per salvarle."
    play sound "audio/sfx/micia 2.mp3" volume 2
    Micia "Oh no, povere tartarughine."
    show fiorello sad 
    Fiorello "E non si distruggono solo gli animali: le reti devastano il fondale marino, lasciandolo così danneggiato che fatica a rigenerarsi. "
    Fiorello "Quando i pescherecci esauriscono una zona, si spostano più in profondità, causando ancora più danni soprattutto ai coralli."
    play sound "audio/sfx/micia 1.mp3" volume 0.5
    Micia "I miei amici pesci mi hanno detto che sono come case per tanti piccoli animali."
    Micia "Non è giusto distruggerli così..."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello rage 
    Fiorello "Esattamente! E pensa che i coralli di profondità, che crescono molto lentamente, possono impiegare centinaia di anni per formarsi."
    Fiorello "Alcune barriere coralline hanno più di 4.500 anni!"
    Fiorello "Quando vengono distrutte, ci vogliono secoli per riparare il danno... se mai si riesce."
    play sound "audio/sfx/micia 2.mp3" volume 2
    Micia "È davvero terribile. Mi sembra come se si strappasse via la storia e la vita del mare."
    show fiorello sad
    Fiorello "Ma non è solo questo. C'è anche il problema della sovrapesca."
    show micia surprised 
    Micia "Cos'è la sovrapesca?"
    play sound "audio/sfx/fiore 2.mp3" volume 1
    Fiorello "Per tanto tempo, le persone hanno pensato che il mare potesse dare pesce all'infinito."
    Fiorello "Ma oggi sappiamo che circa il 58\% degli stock ittici è sfruttato al massimo delle sue possibilità, e un altro 31\% è addirittura sovrasfruttato."
    play sound "audio/sfx/micia 1.mp3" volume 0.5
    show micia surprised 
    Micia "E nonostante questo i pesci riescono ancora a riprodursi?"
    show fiorello rage
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show micia sad  
    Fiorello "È questo il punto: non ci riescono più come prima. La pesca intensiva e la distruzione degli habitat rendono impossibile per molte specie recuperare le loro popolazioni."
    show fiorello sad 
    Fiorello "Prendi il tonno rosso del Pacifico: una volta era abbondante, ma ora è quasi sparito. È un disastro per la biodiversità marina."
    play sound "audio/sfx/fiore 2.mp3" volume 1
    Fiorello "Anche l'acquacoltura, che potrebbe essere una soluzione, a volte peggiora la situazione."
    show fiorello rage 
    Fiorello "In alcuni posti le foreste di mangrovie, che sono aree di riproduzione essenziali per tanti pesci, vengono distrutte per costruire impianti di allevamento"
    Fiorello "E inoltre l'allevamento intensivo di pesci può portare a condizioni di acque tossiche a causa di ammoniaca, nitrati e parassiti."
    play sound "audio/sfx/micia 2.mp3" volume 2
    Micia "Che tristezza... Ma perché succede questo? Perché nessuno fa nulla?"
    show fiorello sad 
    Fiorello "Ci sono alcune iniziative, ma non sempre bastano. Per esempio, l'Unione Europea sta cercando di vietare la pesca a strascico entro il 2030."
    Fiorello "Su 27 Paesi, 26 hanno votato a favore, ma l'Italia ha votato contro."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello rage 
    Fiorello "Questo perché molte aziende del settore temono di perdere profitti, mentre nel frattempo le barriere coralline e numerose specie marine continuano a soffrire gravemente."
    Micia "Non capisco perché scegliere il guadagno a breve termine invece di proteggere il mare per il futuro. È così triste."
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show fiorello sad 
    Fiorello "Hai ragione, Micia. E poi c'è l'inquinamento: ogni anno finiscono in mare tra 4,8 e 12,7 milioni  di tonnellate di plastica."
    Fiorello "Una volta in acqua, molti animali come tartarughe, balene e gabbiani possono ingerirli, rischiando di soffocare o bloccarsi il tratto digerente."
    play sound "audio/sfx/micia 2.mp3" volume 2
    show micia surprised 
    Micia "Plastica? Anche i miei amici me ne hanno parlato... È così crudele..."
    show fiorello rage
    show micia sad 
    Fiorello "Purtroppo sì, e non sono solo le grandi plastiche."
    play sound "audio/sfx/fiore 1.mp3" volume 0
    Fiorello "La plastica non è biodegradabile, si scompone in pezzi sempre più piccoli chiamati microplastiche." 
    Fiorello "Queste particelle derivano anche dai nostri vestiti, dai pneumatici e persino dai cosmetici, come creme o shampoo."
    show fiorello sad 
    Fiorello "Attraverso i fiumi, finiscono in mare e vengono ingerite dagli organismi marini, entrando nella catena alimentare."
    play sound "audio/sfx/micia 2.mp3" volume 2
    Micia "È davvero spaventoso, Fiorello..."
    show fiorello rage 
    Fiorello "E c'è dell'altro, dagli anni '70, gli oceani sono stati usati come discariche per pesticidi, agenti chimici e perfino rifiuti radioattivi."
    Fiorello "Si pensava che il mare potesse diluire tutto, ma quelle sostanze sono ancora lì. Peggio, tornano agli umani attraverso i pesci contaminati che mangiano."
    show fiorello sad
    play sound "audio/sfx/micia 1.mp3" volume 0.5
    show micia sad 
    Micia "È una catastrofe. Possiamo fare qualcosa per aiutare il mare?"
    show fiorello normal
    play sound "audio/sfx/fiore 2.mp3" volume 1
    Fiorello "Una delle prime cose che possiamo fare è sostenere leggi che limitino o vietino la pesca a strascico, specialmente nelle aree delicate come le barriere coralline."
    Fiorello "E possiamo fare la nostra parte anche riducendo il consumo di plastica."
    Fiorello "Usare borracce, borse riutilizzabili e contenitori ecologici può sembrare un piccolo gesto, ma aiuta moltissimo a evitare che la plastica finisca in mare."
    show micia surprised 
    Micia "Wow, non pensavo che delle semplici abitudini quotidiane potessero fare una differenza così grande!"
    show fiorello smile
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show micia normal 
    Fiorello "E sai cos'altro possiamo fare? Partecipare a giornate di pulizia delle spiagge o sostenere associazioni come Plastic Free."
    Fiorello "Questi eventi non solo aiutano a rimuovere i rifiuti dai mari, ma sensibilizzano le persone a rispettare l'ambiente."
    show fiorello normal 
    Fiorello "E infine, possiamo anche fare scelte alimentari consapevoli."
    Fiorello "Mangiare meno pesce aiuta a ridurre la pressione sull'industria della pesca, che spesso adotta pratiche dannose per gli ecosistemi marini"
    Fiorello "Ogni piccola decisione che prendiamo può proteggere il mare e il nostro pianeta."
    play sound "audio/sfx/micia 2.mp3" volume 2
    show micia smile 
    Micia "Mi piace questa idea! Anch'io voglio fare qualcosa per i miei amici pesci e per il mare."
    Micia "Grazie per avermi spiegato tutto, Fiorello!"
    show fiorello smile 
    Fiorello "Non c'è di che, Micia! Sono felice che tu voglia fare la tua parte per aiutare il mare e i tuoi amici pesci."
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show fiorello normal
    Fiorello "Se tutti ci impegnassimo un po' di più, potremmo davvero fare una grande differenza per il nostro pianeta!"
    show micia normal 
    Micia "Lo farò sicuramente! E magari potrò insegnare anche agli altri quello che ho imparato oggi."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    Fiorello "Questo è lo spirito giusto!"
    Fiorello "Ora, però, è arrivato il momento di riportare i nostri visitatori al punto di partenza."
    show fiorello smile 
    Fiorello "È stata una bellissima esperienza, e sono sicuro che tutti porteranno a casa qualcosa di utile da quello che abbiamo condiviso."
    play sound "audio/sfx/micia 1.mp3" volume 0.5
    show micia smile 
    Micia "Grazie ancora, Fiorello! E grazie a tutti per avermi ascoltato."
    show micia normal 
    Micia "Ora vado prima che si bruci la torta che ho messo in forno. Alla prossima amici!"
    hide micia with dissolve
    Fiorello "Micia è sempre adorabile."
    Fiorello "Ora andiamo, il nostro viaggio insieme è quasi finito."
    stop music fadeout 1.0
    jump finefiorello

label finefiorello:
    scene bg centro with fade
    play music "audio/fiorello.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello smile at left with dissolve
    Fiorello "Grazie a tutti per avermi seguito oggi lungo questo percorso!"
    show fiorello normal
    Fiorello "È stato davvero bello condividere con voi l'importanza di proteggere il nostro ambiente e le creature che lo abitano."
    Fiorello "Spero che questo viaggio vi abbia fatto riflettere su come le nostre azioni quotidiane possano avere un impatto enorme sul pianeta."
    play sound "audio/sfx/fiore 2.mp3" volume 1
    show fiorello smile
    Fiorello "Ricordate: ogni passo che facciamo verso uno stile di vita più rispettoso della natura è un passo verso un futuro migliore per noi e per tutte le specie che condividono questa casa con noi."
    show fiorello normal
    Fiorello "Grazie ancora per la vostra attenzione e per l'interesse che avete dimostrato."
    Fiorello "Sono certo che ognuno di voi, a modo suo, contribuirà a rendere il mondo un posto migliore."
    Fiorello "Vi auguro una splendida continuazione della giornata qui al rifugio! Godetevi il resto delle meraviglie che questo posto ha da offrire."
    play sound "audio/sfx/fiore 1.mp3" volume 0.8
    show fiorello smile
    Fiorello "Alla prossima!"
    hide fiorello with dissolve
    stop music fadeout 1.0
    $ fiorelloflag = True
    jump scelta

label pinpin:
    stop music fadeout 1.0
    scene bg relax with fade
    play music "audio/pinpin.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal2 at left with dissolve
    Pinpin "Howdy, amici! Benvenuti alla Fattoria di Nonno Peppino, il posto dove noi animali troviamo finalmente un po' di pace e rispetto."
    show pinpin smile
    show ph pinpin 0 with dissolve
    Pinpin "Io sono Pinpin, un tacchino americano doc."
    Pinpin "Sì, esatto, uno di quei tacchini che vedete sulle tavole di milioni di persone... ma, come potete vedere, io ho avuto un colpo di fortuna!"
    hide ph pinpin 0 with dissolve
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal
    Pinpin "Oggi vi porterò in un percorso speciale per scoprire come possiamo vivere meglio tutti quanti, animali e umani, grazie a un'alimentazione più sostenibile."
    Pinpin "Ma prima di entrare nel vivo, lasciate che vi racconti un po' della mia storia, alright?"
    show pinpin sad
    Pinpin "Ascoltate bene, ragazzi! La vita nei grandi allevamenti di tacchini? Not a walk in the park, ve lo assicuro."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin rage 
    Pinpin "Ci ingrassano a tutta velocità per farci arrivare al peso giusto."
    Pinpin "Ma quando arriva il momento della 'raccolta', alcuni di noi sono troppo piccoli, malati, o semplicemente non crescono abbastanza in fretta, e... guess what?"
    Pinpin "Finiamo scartati, gettati via come se fossimo spazzatura... proprio in un bidone."
    show pinpin smile
    Pinpin "But hey, ogni tanto, persone con un cuore grande decidono di salvarci. That's what I call a miracle!"
    show ph pinpin 1 with dissolve
    Pinpin "Nel mio caso, è stata una signora. Mi ha trovato, ero piccolissimo e fragile, e mi ha preso sotto la sua ala."
    hide ph pinpin 1 with dissolve
    show pinpin normal
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show ph pinpin 2 with dissolve
    Pinpin "Mi ha chiamato Pinpin, come il più piccolo uomo del mondo, perché ero davvero minuscolo!"
    Pinpin "Mi ha curato, fatto crescere forte e mi ha dato una chance."
    hide ph pinpin 2 with dissolve
    Pinpin "Però, quando ha dovuto trasferirsi in un'altra città, ha pensato che la cosa migliore per me fosse portarmi qui, dove sarei stato al sicuro."
    show pinpin smile
    show ph pinpin 3 with dissolve
    Pinpin "And so, eccomi qui, alla Fattoria di Nonno Peppino."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin sad
    hide ph pinpin 3 with dissolve
    Pinpin "Ma pensateci, questa è solo una delle tante storie di salvataggi."
    Pinpin "Noi tacchini, spesso trattati come oggetti, subiamo ingiustizie e sofferenze che non dovremmo mai conoscere."
    show pinpin normal
    Pinpin "Sapete per che evento vengono sacrificati più tacchini?"

    menu:
        "San Valentino":
            Io "Dovrebbe essere per San Valentino."
            play sound "audio/sfx/pinpin 2.mp3" volume 1
            Pinpin "Nope, a San Valentino ci si danno i kisses. La risposta esatta è il giorno del Ringraziamento"
        "Natale":
            Io "Dovrebbe essere per Natale."
            play sound "audio/sfx/pinpin 2.mp3" volume 1
            Pinpin "No guys, a Natale si aprono i christmas presents. La risposta esatta è il giorno del Ringraziamento"
        "Il giorno del Ringraziamento":
            Io "Dovrebbe essere per il giorno del Ringraziamento."
            play sound "audio/sfx/pinpin 1.mp3" volume 1.4
            Pinpin "That's right, è il giorno del Ringraziamento"

    
    show pinpin rage
    Pinpin "La maggior parte dei tacchini come me vengono sacrificati ogni anno proprio per il Thanksgiving."
    Pinpin "Ogni anno, 45 milioni di tacchini negli Stati Uniti vengono uccisi per quella festa."
    Pinpin "È un numero assurdo! E, indovinate? Non si tratta di una festa 'dove siamo grati', no, not for us. Noi siamo visti solo come cibo."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin sad
    Pinpin "In quegli allevamenti, siamo trattati davvero male."
    Pinpin "Come ho detto ci fanno crescere super in fretta, ma questo ci fa soffrire tantissimo."
    Pinpin "Molti di noi si ammalano, soffriamo di dolori alle gambe, problemi al cuore... It's not natural!"
    show pinpin rage
    Pinpin "La nostra vita? Total nightmare."
    Pinpin "Siamo rinchiusi in spazi strettissimi, ci feriamo spesso, e la maggior parte di noi non vedrà mai la luce del sole."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal
    Pinpin "Eppure, siamo animali intelligenti, curiosi, con personalità tutte diverse. Abbiamo sogni come tutti, just like you!"
    show pinpin rage
    Pinpin "E non siamo solo noi tacchini a soffrire per una festività. In Italia c'è un'altra tradizione che fa soffrire tantissimo: mangiare gli agnelli a Pasqua."
    show pinpin sad
    Pinpin "Ogni anno, più di 2 milioni di agnelli vengono uccisi, con ben 375.000 solo per Pasqua."
    Pinpin "Gli agnelli, così piccoli e innocenti, vengono strappati dalle loro mamme. La loro sofferenza è immensa."
    Pinpin "Ma, proprio come noi, non sono mai visti come esseri viventi, solo come carne."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin rage
    Pinpin "E non è finita li, prima del macello, vengono pesati e, a volte, appesi per le zampe per minuti interi."
    Pinpin "È doloroso, ed è anche illegale! But sadly, succede spesso."
    show pinpin sad
    Pinpin "Milioni di animali in tutto il mondo vengono sacrificati ogni anno per tradizioni che potremmo ripensare. Come si fa a festeggiare, causando così tanto dolore?"
    show pinpin normal
    Pinpin "Quando guardiamo alle tradizioni, dovremmo chiederci: 'Is this right?' o 'Possiamo festeggiare in un altro modo?'."
    show pinpin normal2
    Pinpin "Le scelte alimentari, guys, possono davvero fare la differenza. Possiamo decidere di dire no a queste tradizioni che fanno male agli animali."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal
    Pinpin "Ecco perché oggi voglio parlarvi di alimentazione sostenibile e dei benefici di una dieta plant-based."
    Pinpin "Se tutti sapessero quanta sofferenza c'è dietro i prodotti animali, maybe qualcuno cambierebbe idea"
    Pinpin "Vi porterò a conoscere alcuni ospiti del rifugio che vi mostreranno il vero impatto della produzione dei derivati animali."
    show pinpin smile
    Pinpin "Alright, ragazzi! È arrivato il momento di muoverci."
    Pinpin "La storia del prossimo rifugiato è davvero toccante."
    stop music fadeout 1.0
    jump valerio

label valerio:
    scene bg cavancello with fade
    play music "audio/valerio.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal2 at left with dissolve
    Pinpin "Eccoci qui, guys! Venite, venite, vi presento un mio caro amico."
    show pinpin normal
    Pinpin "Il suo nome è Valerio, anche se noi lo chiamiamo 'Ciccio'. È un tipo simpatico, vi piacerà."
    show pinpin smile
    Pinpin "Ciccio, come stai? Tutto ok? Stai mangiando delle buone verdure, eh?"
    play sound "audio/sfx/valerio 1.mp3" volume 0.8
    show valerio smile at right with dissolve
    Valerio "Ciao Pinpin, sto bene! Sì, sto mangiando delle verdure, sono proprio buone! Mmm..."
    show pinpin normal 
    Pinpin "Bene, bene! Senti un po', sto portando questi visitatori in giro e mi piacerebbe che ascoltassero la tua storia, Ciccio."
    show valerio normal
    Valerio "Oh si certo, va benissimo!"
    Pinpin "Go ahead allora, racconta come sei arrivato qui."
    hide pinpin with dissolve
    show valerio smile
    play sound "audio/sfx/valerio 2.mp3" volume 0.9
    show ph valerio 0 with dissolve 
    Valerio "Ciao a tutti, io sono Valerio il bufalino d'acqua!"
    hide ph valerio 0 with dissolve 
    show valerio sad 
    Valerio "La mia storia è un po' triste..."
    Valerio "Dovete sapere che i bufalini maschi non producono latte, e la loro carne non si vende tanto. Così, molti vengono scartati appena nati."
    Valerio "Alcuni vengono abbandonati in posti brutti, come fiumi o crepacci, perché così si risparmiano i soldi per farli crescere."
    play sound "audio/sfx/valerio 1.mp3" volume 0.8
    show ph valerio 1 with dissolve 
    Valerio "Io ero proprio stato abbandonato in un crepaccio. Ero piccolo, tutto solo e non potevo uscire da lì, avrei fatto sicuramente una brutta fine."
    hide ph valerio 1 with dissolve 

    show valerio smile
    show video at Position(xalign=0.10, yalign=0.07, xoffset=-20, yoffset=-10) with dissolve 
    Valerio "Ma poi è arrivato qualcuno che mi ha trovato e mi ha portato al rifugio. Mi hanno salvato la vita!"
    hide video with dissolve

    show valerio normal
    show ph valerio 2 with dissolve 
    Valerio "Mi sono subito sentito al sicuro, avevo trovato finalmente una famiglia che mi voleva bene."
    hide ph valerio 2 with dissolve 
    play sound "audio/sfx/valerio 1.mp3" volume 0.8
    show valerio smile 
    show ph valerio 3 with dissolve 
    Valerio "Ho iniziato a bere tantissimo dal mio biberon e a fare amicizia con tutti."
    hide ph valerio 3 with dissolve
    show ph valerio 4 with dissolve 
    Valerio "Mi sono subito legato tanto a Fiorello, lui è come un fratello maggiore per me."
    hide ph valerio 4 with dissolve 
    show valerio normal
    show ph valerio 5 with dissolve 
    Valerio "Adesso che ho compiuto un anno, mi sento bene!"
    play sound "audio/sfx/valerio 2.mp3" volume 0.9
    Valerio "Sono un tipo tranquillo, ma mi piace anche tanto correre, saltare e soprattutto giocare con l'acqua."
    hide ph valerio 5 with dissolve 
    show valerio smile
    show ph valerio 6 with dissolve 
    Valerio "Qui al rifugio sono proprio felice, perché non devo più preoccuparmi... ho finalmente trovato un posto dove posso essere me stesso."
    hide ph valerio 6 with dissolve
    show ph valerio 7 with dissolve 
    Valerio "Adesso sono forte e sano, e posso divertirmi ogni giorno senza pensare ai brutti momenti che ho passato."
    hide ph valerio 7 with dissolve 
    show valerio normal
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin smile at left with dissolve
    Pinpin "Grazie per aver condiviso la tua storia. Sei davvero forte, little buddy, e ci ricordi quanto coraggio ci vuole per superare certe cose."
    show pinpin normal
    Pinpin "Per fortuna, Valerio è stato salvato, ma tanti altri non hanno questa chance. That's why dobbiamo fermarci a pensare a cosa c'è dietro quello che consumiamo."
    show pinpin rage
    Pinpin "La sua esperienza ci mostra quanto l'industria del latte possa essere crudele e immorale"

    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal 
    Pinpin "Lo sapete che le mucche, come gli umani, producono latte solo dopo una gravidanza?"
    Pinpin "Exactly, per farlo devono avere un vitellino."
    show valerio surprised 
    show pinpin rage 
    Pinpin "Ma c'è un problema gigante, like... enorme. Nell'industria del latte, i vitellini vengono portati via dalle mamme appena nati. Non possono stare insieme!"
    play sound "audio/sfx/valerio 1.mp3" volume 0.9
    show valerio sad
    Valerio "Ma... ma loro vogliono stare con le loro mamme, vero? Si vogliono bene..."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin sad
    Pinpin "Sì, buddy, vogliono stare insieme. Ma nell'industria non c'è spazio per l'amore tra mamma e vitellino."
    Pinpin "Il latte? Lo prendono per gli umani, non per i vitellini."
    show valerio sad
    show pinpin rage
    Pinpin "E sai cosa succede ai vitellini maschi, Ciccio? Non servono per fare latte, così vengono mandati via o, peggio, uccisi."
    play sound "audio/sfx/valerio 2.mp3" volume 0.9
    Valerio "Come me, che ero in quel crepaccio... poveri vitellini."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin sad 
    Pinpin "Esatto, Ciccio. E la mamma? Rimane lì da sola."
    Pinpin "E ogni anno questo ciclo si ripete. Gravide, partoriscono, latte rubato e via i piccoli. Over and over again."
    Pinpin "Le mucche, inoltre, vengono inseminate artificialmente per farle rimanere incinte. È tutto un sistema che non pensa alla loro sofferenza."
    show valerio surprised 
    Valerio "Insem... cosa?"
    show pinpin rage
    show valerio sad
    Pinpin "È come dire che le costringono a fare i vitellini, senza scelta. Una cosa davvero crudele, non trovi?"
    play sound "audio/sfx/valerio 1.mp3" volume 0.8
    Valerio "Ma è una cosa brutta, non voglio che succeda!"
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin sad 
    Pinpin "I know, little buddy. E sai una cosa? Dopo anni e anni di gravidanze e allattamenti, quando non producono più latte... le mandano al macello."
    Pinpin "È così che finisce per tutte loro."
    show pinpin rage
    Pinpin "E la loro vita naturale sarebbe di 20, 25 anni, ma nell'industria del latte, puff, le uccidono dopo pochi anni, quando non servono più"
    Valerio "Anche quando sono stanche e vecchie? Non le lasciano riposare mai?"
    Pinpin "Mai, Ciccio. Loro vogliono solo il latte."
    Pinpin "E sai un'altra cosa? I vitellini maschi, quando vengono portati via, li mettono in gabbie piccole, strettissime."
    play sound "audio/sfx/valerio 2.mp3" volume 0.9
    show valerio surprised 
    Valerio "Oh no! Devono stare lì dentro da soli?"
    show valerio sad
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin rage 
    Pinpin "Yeah, da soli, per mesi. Non possono neanche giocare."
    Pinpin "E li nutrono con cose strane per far diventare la loro carne chiara, perché è quella che piace agli umani."
    show pinpin sad 
    Pinpin "E parlando di latte, lo sapete quanta acqua serve per farne un litro? Una quantità pazzesca, migliaia di litri di acqua per ogni litro di latte."
    show valerio surprised 
    Valerio "Acqua? Ma noi qui la usiamo per annaffiare le verdure, non per il latte, giusto?"
    show valerio sad
    play sound "audio/sfx/pinpin 2.mp3" volume 1 
    show pinpin rage 
    Pinpin "Esatto. Ma fuori da qui, le risorse idriche vengono sprecate e spesso inquinate dai caseifici. È un vero disastro per l'ambiente."
    Pinpin "E non è solo l'acqua. Gli antibiotici che usano per curare le mucche finiscono nel latte and... guess what? Gli umani li bevono!"
    Pinpin "Quei residui di antibiotici nel latte possono causare un grosso problema: la resistenza agli antibiotici."
    play sound "audio/sfx/valerio 2.mp3" volume 0.9
    show valerio surprised 
    Valerio "Resistenza... che vuol dire?"
    show valerio sad 
    show pinpin normal2
    Pinpin "Cos'è la resistenza agli antibiotici, eh? Well è quando i batteri diventano così furbi che gli antibiotici non riescono più a fermarli."
    Pinpin "Gli umani li bevono tutti i giorni, senza nemmeno saperlo!"
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal 
    Pinpin "E il problema sta crescendo. È una minaccia globale, amici miei."
    Pinpin "Se non la fermiamo, entro il 2050, potrebbero esserci 10 milioni di morti l'anno."
    Pinpin "E sai che ci sono anche altri rischi per la salute? Il latte vaccino è stato collegato a certi tipi di tumori, come quello al seno e alla prostata."
    Pinpin "Non è così sano come dicono."
    play sound "audio/sfx/valerio 1.mp3" volume 0.8
    show valerio smile 
    Valerio "Io mangio solo verdure e fieno. E sono forte come un leone!"
    show pinpin normal2
    Pinpin "You betcha! E il calcio? Chi dice che serve il latte per avere ossa forti si sbaglia. Le verdure a foglia verde sono un'ottima fonte."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal
    Pinpin "Dobbiamo sensibilizzare le persone, far capire loro che c'è un'alternativa migliore e che possiamo fare la differenza."
    Pinpin "È ora di cambiare, ya know!"
    show valerio normal
    Valerio "Ma perché non bevono qualcosa di più sano allora, tipo il latte di mandorle?"
    show pinpin smile 
    Pinpin "That's right, Ciccio! Le alternative vegetali sono così buone. Latte di soia, avena, cocco... tutte cruelty-free e molto più sostenibili."
    play sound "audio/sfx/valerio 2.mp3" volume 0.9
    show valerio smile
    Valerio "Sì! Dobbiamo dire a tutti di non bere più il latte delle mucche!"
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    Pinpin "That's the spirit! You're totally on the right track!"
    show pinpin normal2
    Pinpin "Anche fare ricette fatte in casa è un'ottima idea, tipo fare burro vegetale o formaggio vegano. È facile, basta un po' di creatività."
    show valerio normal
    Valerio "Mi sembra facile, posso farlo anche io!"
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal
    Pinpin "E possiamo anche unirci a gruppi che si occupano di protezione animale, o partecipare a eventi e fiere che promuovono uno stile di vita più sostenibile."
    Pinpin "Non dimenticate poi i rifugi per animali! Possiamo fare una donazione o fare volontariato in santuari che aiutano gli animali, come noi!"
    play sound "audio/sfx/valerio 1.mp3" volume 0.8
    show valerio smile
    Valerio "Sì, dobbiamo aiutarli!"
    show pinpin normal2
    Pinpin "Well, grazie per il tuo tempo Ciccio. Sei un vero campione!"
    show valerio normal
    Valerio "Grazie a te, Pinpin. È stato bellissimo parlare con te!"
    show valerio smile
    play sound "audio/sfx/valerio 2.mp3" volume 0.9
    show pinpin normal
    Valerio "E grazie a voi per essere venuti qui al rifugio oggi. Tornate a trovarmi così giocheremo un pò insieme!"
    Valerio "Alla prossima!"
    hide valerio with dissolve
    Pinpin "Va bene, ragazzi, è ora di andare avanti. Vi porto ad incontrare un altro ospite del santuario. Follow me!"
    stop music fadeout 1.0
    jump marco

label marco:
    scene bg capre with fade
    play music "audio/marco.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal2 at left with dissolve
    Pinpin "Here we are! Siamo arrivati.."
    show pinpin normal 
    Pinpin "E ora, guardate lì, vedete quella capra bianca davvero imponente? It's our guy!."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin smile
    Pinpin "Hey, Marco! Come stai, big guy?"
    play sound "audio/sfx/marco 1.mp3" volume 0.8
    show marco smile at right with dissolve
    Marco "Ciao, Pinpin! Sto bene, grazie, è sempre bello vederti."
    show pinpin normal 
    Pinpin "Sono contento di sentire che stai bene!"
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    Pinpin "Vedi, oggi stiamo facendo un percorso per sensibilizzare le persone sull'alimentazione e su quanto la produzione di derivati animali possa essere crudele, ya know?"
    show marco rage
    Marco "Oh si, so bene di cosa stai parlando"
    show marco normal 
    Pinpin "Ecco io pensavo che tu potessi raccontare la tua storia ai nostri visitatori, quella che ti ha portato qui con noi."
    show pinpin sad 
    Pinpin "So che hai vissuto delle esperienze davvero difficili, quindi sarebbe importante se ci raccontassi un po' di te."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal
    Pinpin "Che ne dici, amico?"
    play sound "audio/sfx/marco 2.mp3" volume 0.9
    show marco smile 
    Marco "Certo sono sempre a disposizione."
    hide pinpin with dissolve
    show marco normal
    show ph marco 0 with dissolve 
    Marco "Ciao a tutti! Sono Marco, una capretta ionica, e sono felice di incontrarvi."
    hide ph marco 0 with dissolve
    show ph marco 1 with dissolve 
    Marco "La mia storia inizia in Puglia, nel leccese, con me e la mia sorellina Lina."
    hide ph marco 1 with dissolve
    play sound "audio/sfx/marco 1.mp3" volume 0.8
    show marco sad 
    Marco "Eravamo in una gabbia fuori da un centro commerciale, per mostrare a chi veniva che tipo di carne il nostro allevatore vendeva all'interno."
    show marco normal
    show ph marco 2 with dissolve  
    Marco "Degli attivisti ci hanno visti e sono riusciti a ottenere la nostra consegna, minacciando di denunciarlo per maltrattamenti."
    hide ph marco 2 with dissolve
    show ph marco 3 with dissolve 
    Marco "E per fortuna poco prima di Pasqua, siamo arrivati qui al rifugio anche se all'inizio non è stato facile."
    hide ph marco 3 with dissolve
    play sound "audio/sfx/marco 2.mp3" volume 0.9
    show marco sad 
    Marco "Purtroppo, Lina non ce l'ha fatta... aveva un soffio al cuore e poco dopo è venuta a mancare."
    show ph marco 4 with dissolve 
    Marco "Io, invece, ho avuto dei problemi alle ossa, perché non avevo bevuto abbastanza latte dalla mamma. Mi sono fratturato la gamba."
    hide ph marco 4 with dissolve 
    show marco smile
    play sound "audio/sfx/marco 2.mp3" volume 0.9
    show ph marco 5 with dissolve 
    Marco "Ma qui mi hanno curato e ora sto molto bene."
    Marco "Mi sento davvero fortunato ad essere arrivato alla fattoria."
    Marco "Qui ho trovato una nuova famiglia che mi ha accolto e curato con amore."
    hide ph marco 5 with dissolve
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin sad at left with dissolve
    Pinpin "Mi dispiace tanto per la tua perdita, Marco. Sei stato davvero forte a superare tutto."
    show marco normal
    Marco "Grazie, Pinpin. Anche se Lina non è più con noi fisicamente vive ancora nei cuori di tutti e attraverso me."
    play sound "audio/sfx/marco 1.mp3" volume 0.8
    show pinpin smile
    Marco "Sono sicuro che sarebbe fiera di vedere come la fattoria si è evoluta e quanto amore e dedizione ci sono qui per gli animali."
    
    show pinpin rage
    show marco normal
    Pinpin "You know, Marco, sentendo la tua storia non posso fare a meno di pensare a quanto sia folle l'industria della carne."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show marco rage
    Pinpin "Non solo tratta gli animali come te con crudeltà, ma sta anche distruggendo il nostro pianeta."
    show pinpin sad
    show marco sad
    Pinpin "La carne ha un costo ambientale e sociale enorme."
    Pinpin "È così dannosa per il pianeta che, se smettessimo di mangiarla o ne riducessimo il consumo, potremmo lasciare un mondo migliore for the next generations."
    show pinpin normal2
    Pinpin "Ma guardiamo i numeri: negli ultimi cinquant'anni, la produzione di carne è quadruplicata."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal
    Pinpin "E il consumo medio? È passato da 20 chili a testa negli anni '60 a quasi 40 chili nel 2014. It's crazy right!"
    play sound "audio/sfx/marco 2.mp3" volume 0.9
    show marco rage 
    Marco "Lo so bene, Pinpin. Ma racconta di più, così i nostri visitatori possono capire meglio."
    show pinpin rage 
    Pinpin "Lasciate che vi faccia un esempio. Per produrre un solo chilo di manzo servono circa 2.350 litri d'acqua."
    Pinpin "Do you have any idea di quanta sia?"
    Pinpin "Una persona che beve otto bicchieri d'acqua al giorno consuma questa quantità in tre anni. Tre anni d'acqua, solo per una bistecca!"
    show marco sad 
    Marco "È davvero assurdo sprecare così tanto... e solo per mangiare carne."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal2
    Pinpin "Non è solo una questione di risorse. Pensate al lato sociale."
    show pinpin normal
    Pinpin "È come se, durante una cena di famiglia con quattro persone, per mangiare un chilo di bistecche di manzo, consumassimo oltre 2.000 litri d'acqua."
    Pinpin "You understand the paradox?"
    play sound "audio/sfx/marco 1.mp3" volume 0.8
    show marco rage 
    Marco "Quindi, mentre noi soffriamo per mancanza di risorse, l'acqua viene sprecata così?. Che rabbia."
    show pinpin rage 
    Pinpin "Esatto. È come riempire una piscina ogni volta che mangi una bistecca."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    Pinpin "Le persone preferiscono spesso ignorare l'impatto della cosa."
    Pinpin "Ma la cosa più assurda è che possiamo vivere senza carne con qualche accorgimento, ma senza acqua? No way."
    show pinpin sad
    Pinpin "E questi numeri non tengono nemmeno conto di tutto il resto, come l'inquinamento delle acque, la deforestazione per i pascoli e le coltivazioni di mangimi."
    play sound "audio/sfx/marco 2.mp3" volume 0.9
    show marco rage 
    Marco "E poi c'è anche il problema delle malattie, vero?"
    show marco normal
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal
    Pinpin "Right. La carne non è solo una questione ambientale. Studi medici hanno dimostrato che le diete ricche di carne rossa e lavorata aumentano il rischio di malattie gravi: diabete, obesità, infarti, e persino tumori."
    show pinpin normal2
    Pinpin "Non ve lo dico io, eh, lo dicono gli studi, con numeri e fatti."
    show marco rage
    Marco "Mi sembra già abbastanza per farci pensare, ma continua. Cosa dicono esattamente?"
    show marco normal
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal
    Pinpin "Beh, l'International Agency for Research on Cancer ha classificato la carne rossa come 'probabilmente cancerogena' e quella lavorata come 'sicuramente cancerogena'."
    show pinpin normal2
    Pinpin "Le conclusioni derivano dall'analisi di oltre 800 studi scientifici."
    show pinpin normal
    Pinpin "Tutto questo è molto serio, folks. Parliamo di problemi gastrointestinali, ma anche di tumori legati agli ormoni come al seno o alla prostata."
    play sound "audio/sfx/marco 1.mp3" volume 0.8
    show marco sad
    Marco "E la gente continua a mangiarla come se nulla fosse..."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal 
    Pinpin "Purtroppo sì. Ma c'è una cosa che possiamo fare: parlarne, sensibilizzare, e scegliere alternative. È un primo passo importante."
    show marco normal
    Marco "Sembra proprio una questione di scelte... ma cosa succede con il pesce? Anche lì ci sono problemi, vero?"
    show pinpin sad 
    Pinpin "Oh, you bet! La produzione di pesce è un altro disastro su tutta la linea. Ma lasciami spiegare bene come stanno le cose."
    show pinpin rage
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show marco rage 
    Pinpin "Prendi i pesci allevati. Vivono in acque piene di ammoniaca e nitrati."
    Pinpin "È come essere intrappolati in una vasca di sporco senza mai poterne uscire."
    Pinpin "Inoltre non ci sono leggi che regolano come vengono trattati o macellati."
    Pinpin "Quando li tirano fuori dall'acqua, li lasciano soffocare. Si agitano, provano a scappare, ma non possono farlo. È puro terrore."
    show pinpin sad 
    Pinpin "E non parliamo dei grandi pesci come il tonno. Vengono bastonati a morte. Repeatedly. È un processo brutale, senza pietà."
    play sound "audio/sfx/marco 2.mp3" volume 0.9
    show marco sad
    Marco "E nessuno si ferma a pensare che sentono dolore? Anche loro provano ansia, non sono diversi da noi."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin rage
    Pinpin "Yeah, e c'è di più. In Italia, il 12\% dei prodotti ittici viene dagli allevamenti."
    Pinpin "Sono circa 185.000 tonnellate all'anno. Siamo il terzo produttore europeo."
    show pinpin sad 
    Pinpin "È un business gigantesco, e nessuno parla delle sofferenze dietro quei numeri."
    play sound "audio/sfx/marco 1.mp3" volume 0.8
    show marco rage
    Marco "Numeri. Solo numeri. E intanto loro muoiono in silenzio."
    Pinpin "Esatto. E poi ci sono i rischi per chi mangia il pesce. I grandi, come il tonno e il pesce spada, sono pieni di mercurio."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal 
    Pinpin "Non è solo pericoloso, è straight up toxic! Può colpire il sistema nervoso, soprattutto di bambini e donne incinte."
    show marco sad
    Marco "E gli altri inquinanti? Ho sentito parlare di diossine e altre sostanze pericolose."
    Pinpin "Yep, PCB e diossine. Collegate a tumori e problemi riproduttivi."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin rage
    Pinpin "Ma ehi, non è finita qui. Sai quanti pezzi di plastica ingerisce chi mangia pesce? Circa 11.000 all'anno. Crazy, huh?"
    play sound "audio/sfx/marco 2.mp3" volume 0.9
    show marco rage
    Marco "Plastica. Dentro di noi?. E nessuno si chiede quali saranno le conseguenze." 
    show pinpin normal
    Pinpin "Sembra proprio di no. Parliamo di infiammazioni, degenerazione muscolare. Effetti che ancora non comprendiamo del tutto, ma di sicuro non sono buoni."
    show marco sad
    Marco "E tutto questo solo per riempire i piatti di gente che non sa, o non vuole sapere, cosa succede davvero."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal2
    Pinpin "Right on point! Cambiare le abitudini alimentari è the game-changer."
    show marco normal
    show pinpin normal
    Pinpin "Il consumo di prodotti di origine animale non solo mette a rischio di avere infarti, ictus e diabete, ma toglie anche anni di vita."
    show pinpin smile 
    Pinpin "Chi segue una dieta plant-based invece ha il 12\% di probabilità in meno di morire rispetto ai consumatori di carne. Non è un dato da poco."
    show marco smile
    Marco "E non si parla solo della nostra salute. È una scelta che può fare bene al pianeta, giusto?"
    show pinpin normal2
    Pinpin "You got it! Una dieta a base vegetale richiede meno risorse naturali: meno acqua, meno inquinamento e un big cut alle emissioni di gas serra."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal
    Pinpin "E sai qual è la parte migliore? Non è solo una questione di rinuncia. È un modo per costruire qualcosa di meglio. A better future."
    play sound "audio/sfx/marco 1.mp3" volume 0.8
    show marco normal
    Marco "Con un cambiamento relativamente semplice, si può ridurre l'impatto sul pianeta e vivere anche meglio. È incoraggiante."
    show pinpin smile 
    Pinpin "Exactamente! Ogni scelta che facciamo conta. Quando scegli un pasto senza carne o pesce, stai dicendo: 'Io ci tengo a me stesso, al pianeta e alle generazioni future.'"
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    Pinpin "Non è solo un passo verso la salute, è un atto di responsabilità. E hey, it's delicious!"
    Pinpin "Gli alimenti vegetali possono essere davvero gustosi."
    show marco smile
    Marco "È vero. Qui al santuario abbiamo visto che è possibile vivere bene senza sfruttare nessuno."
    play sound "audio/sfx/marco 2.mp3" volume 0.9
    Marco "Mi piace pensare che ogni piatto possa essere un messaggio di speranza."
    show pinpin normal2
    Pinpin "Damn right, buddy! Cambiare il mondo non è mai stato così tasty e pieno di possibilità."
    Pinpin "Facciamolo insieme, un boccone alla volta."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal
    Pinpin "Grazie, Marco, per il tuo tempo e per la tua saggezza. Sei stato fantastico!"
    Marco "Grazie a te, Pinpin, e grazie a tutti voi per avermi ascoltato. Spero che la mia storia vi abbia fatto riflettere."
    play sound "audio/sfx/marco 1.mp3" volume 0.8
    show marco normal
    Marco "Ora è tempo che io torni dai miei amici. Alla prossima!"
    hide marco with dissolve
    Pinpin "Ci mancherai, Marco! Ma adesso tocca a me. Vi accompagnerò all'ultima tappa del vostro percorso."
    Pinpin "Un posto che mi sta davvero a cuore. È il momento di mostrarvelo!"
    stop music fadeout 1.0
    jump maria

label maria:
    scene bg portapollaio with fade
    play music "audio/maria.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal2 at left with dissolve
    Pinpin "Alright, folks, benvenuti al pollaio del rifugio!"
    Pinpin "Questo è il posto dove passo la maggior parte del mio tempo con i miei amici pennuti."
    Pinpin "Venite, entriamo dentro!"

    scene bg pollaio with fade
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal at left with dissolve
    Pinpin "Non vi ho portato qui oggi per mostrarvi la mia casa... no-no, c'è qualcosa di molto più importante da raccontarvi."
    Pinpin "Voglio raccontarvi la storia di una rifugiata davvero speciale, una gallinella che ha fatto la differenza in questo posto."
    show ph maria 1 with dissolve
    Pinpin "Il suo nome era Maria."
    Pinpin "Arrivò da un passato che nessuno dovrebbe vivere, ma nonostante tutto, aveva una forza e un cuore così grandi."
    show pinpin smile
    Pinpin "Era sempre pronta ad aiutare gli altri, a dare amore anche quando le cose erano difficili."
    Pinpin "Una vera fighter, se mi chiedete!"
    hide ph maria 1 with dissolve
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin sad
    Pinpin "Purtroppo, Maria non c'è più con noi, ma il suo ricordo è vivo. In ogni angolo di questo pollaio, in ogni respiro di aria fresca, qui c'è un po' di lei."
    show pinpin normal 
    Pinpin "Ma ora, è il momento di raccontarvi la sua storia."
    show pinpin sad
    Pinpin "Lei era una gallina, e come tante altre, era destinata a una vita in un allevamento industriale."
    Pinpin "Sadly, la sua esistenza era ridotta a una macchina per produrre uova."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin smile
    Pinpin "Un gruppo di ragazzi coraggiosi, chiamato Alf, si è infilato in uno di questi allevamenti e l'ha liberata insieme a tante altre galline."
    Pinpin "È così che è arrivata qui, nel nostro santuario."
    show ph maria 2 with dissolve
    show pinpin sad
    Pinpin "But when we found her, Maria era in condizioni davvero brutte."
    Pinpin "Senza piume, con il corpo segnato dalla sofferenza e le ali che le avevano tagliato per impedire che potesse farsi del male o difendersi."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin rage
    Pinpin "La sua vita era stata una lotta per produrre uova a un ritmo insostenibile. In due anni aveva prodotto ciò che altre galline fanno in otto."
    hide ph maria 2 with dissolve
    show ph maria 3 with dissolve
    show pinpin normal
    Pinpin "But despite it all, quando è arrivata qui, ha finalmente potuto respirare, correre, vivere senza paura."
    Pinpin "Ha vissuto con noi per un anno e mezzo, godendo della libertà che le era stata negata."
    hide ph maria 3 with dissolve
    show pinpin smile
    show ph maria 4 with dissolve
    Pinpin "E sì, nonostante tutto, è riuscita a essere felice."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin sad
    Pinpin "La sua storia, purtroppo, è solo una delle tante."
    hide ph maria 4 with dissolve
    Pinpin "E, ragazzi, è proprio questo che succede dietro le quinte dell'industria delle uova e del pollame."
    show pinpin rage
    Pinpin "Everyday milioni di animali, proprio come lei, vengono sfruttati e costretti a vivere in condizioni terribili."
    Pinpin "E mentre loro lottano per sopravvivere, le persone si godono il 'prodotto' senza nemmeno sapere che prezzo stanno pagando, man. Ma è una realtà che dobbiamo affrontare."
    show pinpin normal
    Pinpin "Alright, guys, facciamo un bel salto nel mondo degli allevamenti di galline."

    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin sad
    Pinpin "Le galline per la produzione di uova vivono in gabbie minuscole, senza spazio per muoversi o fare quello che farebbero in natura, come razzolare."
    Pinpin "E sai cosa succede? Le galline soffrono di malattie come l'osteoporosi, le ossa si fanno deboli perché non possono muoversi."
    Pinpin "La loro vita è una tortura, con stress e sofferenza fisica e psicologica che non puoi nemmeno immaginare."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin rage
    Pinpin "Inoltre in Europa, ogni anno, vengono uccisi milioni di pulcini appena nati."
    Pinpin "I maschi, che non depongono uova e sono considerati inutili, vengono buttati via come fossero spazzatura."
    Pinpin "Il sesso del pulcino viene determinato pochi ore dopo la nascita, e quelli maschi? 'Next!'"
    show pinpin sad
    Pinpin "E se pensate che non possano soffrire di più, pensateci due volte."
    Pinpin "Per prevenire il piccacismo, gli operai bruciano o tagliano il becco delle galline senza anestesia."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    Pinpin "È una pratica brutale, man, e tutto per risparmiare. Se non è crudeltà, non so cosa lo sia!"
    show pinpin rage
    Pinpin "Poi ci sono i polli per la carne, quelli che vengono stipati come sardine in capannoni."
    Pinpin "Vengono cresciuti così velocemente che le loro zampe si spezzano sotto il loro stesso peso."
    Pinpin "Unfortunately, non vivono abbastanza a lungo per vedere altro che sofferenza."
    Pinpin "È un business spietato, capito?"
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin sad
    Pinpin "E, ragazzi, non è solo una questione di come vivono questi animali."
    Pinpin "L'industria delle uova inquina pure l'ambiente, con gas serra e inquinamento dell'acqua."
    Pinpin "Ogni uovo che mangiate it's like a little bomb per il nostro pianeta."
    show pinpin normal
    Pinpin "E sapete che, nonostante tutto ciò, mangiare uova porta anche dei rischi per la salute?"
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal2
    Pinpin "Alright, listen up, folks. Prima di tutto, c'è la Salmonella, un batterio che può contaminare l'interno dell'uovo, anche se il guscio sembra proteggerlo."
    Pinpin "Mangiare uova contaminate può causare intossicazioni alimentari, con sintomi che vanno dalla diarrea alla febbre e, in alcuni casi, a complicazioni gravi, come la sepsi."
    show pinpin normal
    Pinpin "And there's more. Le uova sono piene di colina e grassi saturi."
    Pinpin "Se mangiate troppe uova, queste sostanze possono aumentare il rischio di malattie cardiovascolari, ictus e diabete di tipo 2."
    Pinpin "Certo, le uova avranno anche proteine e colesterolo buono, ma, ragazzi, un consumo eccessivo? Non è certo un colpo di fortuna per il cuore."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin rage
    Pinpin "Ah, e non dimentichiamo le malattie zoonotiche, quelle che passano dagli animali agli esseri umani."
    Pinpin "Especially, la carne di pollo dagli allevamenti intensivi è una bomba di batteri come Campylobacter, e Escherichia Coli."
    Pinpin "Tutto questo è ovviamente favorito dalle condizioni igienico-sanitarie pessime degli allevamenti."
    Pinpin "Con un ambiente così sporco, it's easy per i batteri proliferare."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal
    Pinpin "Chi fa consumo di carne infetta rischia infezioni che portano a vomito, febbre, e nei casi più gravi, anche alla morte."
    Pinpin "Non voglio spaventarvi, ma è importante sapere che dietro a ogni boccone c'è un rischio per la salute, e non solo per gli animali."
    show pinpin smile
    Pinpin "Ma adesso, vi spiegherò come possiamo fare la differenza. Come with me!"
    stop music fadeout 1.0
    jump plantbased

label plantbased:
    scene bg stradapollaio with fade
    play music "audio/plantbased.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal2 with dissolve
    Pinpin "Ok guys, ora sapete tutto quello che succede dietro le quinte nei macelli."
    show pinpin normal
    Pinpin "Devo dirvi che c'è una sola vera soluzione per aiutare a fare la differenza in tutto questo: l'alimentazione plant-based."
    Pinpin "È davvero l'unico modo per mangiare in modo più sostenibile, per proteggere gli animali, e per dare una mano alla nostra salute."
    show pinpin smile
    Pinpin "E vi dirò una cosa: quando si sceglie la strada vegetale, si fa davvero la differenza."
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal2
    Pinpin "Alright, folks! Quando parliamo di una dieta plant-based, vogliamo dire mangiare solo roba che viene dalle piante, senza proteine animali."
    Pinpin "Niente carne, ne uova, ne latte."
    show pinpin normal
    Pinpin "Non è solo mangiare verdure, ragazzi. È una questione di scelte consapevoli. Mangiare cibi freschi, naturali, niente roba trattata."
    Pinpin "Siamo qui per nutrirci davvero, ya know?"
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin smile
    Pinpin "Promuove anche il consumo di prodotti locali, stagionali e a km zero, baby. È la chiave per ridurre l'impatto sull'ambiente e sostenere i produttori locali. È win-win per tutti!"
    Pinpin "E parliamo anche di sostenibilità! Ogni piatto che prepariamo deve rispettare la terra e la biodiversità, senza tutti quei cibi ultra-processati che fanno solo danni."
    show pinpin normal
    Pinpin "Immaginate un mondo dove tutti mangiano cibo che fa bene al corpo e fa bene al pianeta! It's not a dream, è una possibilità che possiamo realizzare, guys!"
    show pinpin smile
    Pinpin "Una dieta plant-based non è solo salutare per noi, ma è anche un grande favore per gli animali. Non più sfruttamento, non più sofferenza. È il vero modo di vivere in armonia!"
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    Pinpin "La dieta plant-based è tipo un superpotere. Ti fa sentire meglio, ti dà energia e fa bene alla salute."
    show pinpin normal2
    Pinpin "E sentite, non è nemmeno un sacrificio. C'è una marea di cibo super buono che possiamo mangiare: frutta, verdura, legumi... ogni pasto è un'esplosione di sapori!"
    show pinpin normal
    Pinpin "E ragazzi, non preoccupatevi, c'è tutto quello che ci serve in una dieta plant-based! Tipo quinoa, avena, e riso integrale."
    Pinpin "E poi legumi come lenticchie e fagioli. Sono pieni di proteine, fibre, ferro e magnesio. Una vera bomba per il corpo, capito?"
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin smile
    Pinpin "E non dimentichiamoci dei grassi sani, tipo olio extravergine d'oliva, che è top per il cuore!"
    Pinpin "Avocado, semi di chia, noci... sono pieni di omega-3, perfetti per cervello e pelle. Straight up, questi sono i migliori!"
    show pinpin normal
    Pinpin "Frutta e verdura di stagione? È tutta roba super! Spinaci, cavolo riccio, e bacche. Cariche di vitamine e antiossidanti."
    Pinpin "E il calcio per ossa e denti, proprio quello che ci serve!"
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin normal2
    Pinpin "E per i golosi come me, niente paura! I dolci plant-based sono da paura. Banane, semi di lino, bevande vegetali e miele d'agave, davvero! No stress per il dessert!"
    Pinpin "Quando si tratta di spuntini, abbiamo un sacco di scelte! Barrette fatte in casa con avena e frutta secca, hummus con verdure crude, frullati di frutta e semi."
    Pinpin "Così non ci si annoia mai e si è sempre full of energy!"
    show pinpin normal
    Pinpin "E con questa dieta, ragazzi, siamo a posto. È sana, completa e super nutriente. E i vantaggi? Oh, those are comin' up next!"
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin smile
    Pinpin "Prima di tutto, è una bomba per la salute del nostro sistema digestivo, grazie all'elevato apporto di fibre. Il nostro intestino ringrazia, trust me!"
    Pinpin "Poi, il corpo riceve un sacco di macronutrienti e antiossidanti, grazie alla varietà di vegetali di stagione che possiamo mangiare."
    Pinpin "È un boost di energia naturale ogni giorno!"
    show pinpin normal
    Pinpin "E, guys, la parte migliore: ci permette di sperimentare! Cucina creativa a manetta."
    Pinpin "Piatti classici rivisitati, come formaggi vegani, ragù di soia, burger di legumi... è un viaggio di sapori, and the best is yet to come!"
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin smile
    Pinpin "Senza dimenticare può essere super utile per migliorare la salute cardiovascolare, combattere il diabete, l'ipertensione, e l'infiammazione. Semplicemente fantastico!"
    show pinpin normal2
    Pinpin "Ovviamente, bisogna essere attenti e informarsi come si deve. Conoscere cosa mangiamo is the key."
    Pinpin "Vogliamo essere sicuri di fare scelte consapevoli, sia per il nostro corpo che per il pianeta."
    show pinpin normal
    Pinpin "E seguire la stagionalità è un altro punto forte. Mangiare zucca in ottobre e anguria in luglio, è così che si fa!"
    Pinpin "Evitiamo la produzione intensiva in serra che fa male a noi e all'ambiente!"
    Pinpin "Mangiare locale è il nostro superpotere!"   
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin rage
    Pinpin "Non dobbiamo farci ingannare dai cibi importati che arrivano con costi altissimi in termini di risorse e sfruttamento di animali, come nel caso delle scimmie usate per raccogliere noci di cocco in Thailandia."
    Pinpin "I macachi sono costretti a raccogliere noci in modo brutale, e molti subiscono abusi terribili."
    show pinpin normal
    Pinpin "Questo non è qualcosa che vogliamo supportare, vero? È proprio per questo che le scelte consapevoli sono fondamentali."
    show pinpin smile
    Pinpin "Quindi, guys, mangiare plant-based non è solo una questione di cibo, è una questione di scelte etiche che possono fare una grande differenza per tutti, animali e pianeta compresi!"
    play sound "audio/sfx/pinpin 1.mp3" volume 1.4
    show pinpin smile
    Pinpin "Prima di andare, voglio ringraziarvi di cuore per aver ascoltato tutte le nostre storie, come quella di Maria che ci ha insegnato tanto."
    Pinpin "È stato un piacere condividere un po' della nostra vita con voi!"
    show pinpin normal2
    Pinpin "Spero che vi siate divertiti e che, magari, qualche semino di consapevolezza sia germogliato nelle vostre teste."
    play sound "audio/sfx/pinpin 2.mp3" volume 1
    show pinpin normal
    Pinpin "Adesso, vi auguro una giornata fantastica, piena di buone vibrazioni e, chissà, magari di qualche piatto super gustoso!"
    show pinpin smile
    Pinpin "Vi saluto con un bel 'stay cool', e ricordate sempre: ogni piccola scelta conta. Peace out!"
    stop music fadeout 1.0
    $ pinpinflag = True
    jump scelta

label toto:
    stop music fadeout 1.0
    scene bg pgiochi with fade
    play music "audio/toto.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto smile at left with dissolve
    Totò "Ciao a tutti e benvenuti nella nostra fattoria!"
    show ph toto 0 with dissolve
    Totò "Io sono Totò, e sono felice di essere la vostra guida oggi."
    hide ph toto 0 with dissolve
    Totò "Come avete capito, questo è un posto speciale, pieno di storie che parlano di seconde possibilità."
    Totò "E oggi vi guiderò proprio in un percorso per scoprire cos'è davvero il benessere animale."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto normal
    Totò "Per capirlo, però, dobbiamo partire dalle basi. E la mia storia è un buon punto di inizio."
    show ph toto 1 with dissolve
    Totò "Mi hanno trovato a fine luglio del 2023, nel centro di una città caotica chiamata Foggia. Ero debole, affamato e spaventato."
    show toto sad
    Totò "Non ricordo bene come ci sono finito, ma probabilmente ero su un camion che mi portava chissà dove. Forse a un allevamento, o magari a un laboratorio."
    hide ph toto 1 with dissolve
    show toto normal
    Totò "Poi, per fortuna o per destino, sono caduto dal camion. Mi sono nascosto tra le auto parcheggiate, tremando e cercando di sopravvivere."
    Totò "Un passante mi ha visto e ha deciso di aiutarmi. Non vi mentirò, ero terrorizzato, ma quella è stata la mia salvezza."
    show toto smile
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show ph toto 2 with dissolve
    Totò "Dopo qualche giorno, sono arrivato qui, al santuario. All'inizio non sapevo cosa aspettarmi, ma presto ho capito che era un posto sicuro."
    hide ph toto 2 with dissolve
    show ph toto 3 with dissolve
    Totò "Ora, da un anno e mezzo, vivo qui con tanti altri animali. Ho fatto amicizia con tutti e mi sento parte di una grande famiglia."
    hide ph toto 3 with dissolve
    show toto normal
    show ph toto 4 with dissolve
    Totò "Le mie giornate sono semplici e piene di cose belle."
    Totò "L'unica preoccupazione? Trovare il posto più comodo per dormire e non perdere nemmeno una coccola!"
    hide ph toto 2 with dissolve
    show toto smile
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show ph toto 5 with dissolve
    Totò "Mi sembra di vivere in un paradiso terrestre. Qui sono felice."
    hide ph toto 5 with dissolve
    show toto sad
    Totò "Ma non tutti gli animali sono così fortunati."
    Totò "Molti animali vivono in condizioni terribili, costretti a soffrire in modo che noi umani spesso nemmeno vediamo."
    Totò "Sapete qual è il principale modo in cui gli esseri umani sfruttano gli animali?"
    
    menu:
        "Produzione di carne":
            Io "Dovrebbe essere per la produzione di carne."
            play sound "audio/sfx/toto 1.mp3" volume 2.5
            show toto rage
            Totò "È vero, nella produzione di carne molti animali sono allevati in condizioni di sofferenza estrema."
        "Ricerca scientifica":
            Io "Dovrebbe essere per la ricerca scientifica."
            play sound "audio/sfx/toto 1.mp3" volume 2.5
            show toto rage
            Totò "Verissimo, milioni di animali sono usati ogni anno per esperimenti scientifici che causano loro grande sofferenza."
        "Commercio illegale":
            Io "Dovrebbe essere per il commercio illegale."
            play sound "audio/sfx/toto 1.mp3" volume 2.5
            show toto rage
            Totò "Assolutamente, il commercio illegale di animali porta spesso a condizioni disumane per le creature catturate e vendute."  
    
    show toto sad
    Totò "Ma ad essere sincero, tutte le risposte erano corrette."
    show toto rage
    Totò "Alcuni sono sfruttati per la produzione alimentare, altri usati per esperimenti scientifici senza mai conoscere la libertà o la gentilezza."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto sad
    Totò "Io stesso sono un maialino di Göttingen, una razza che viene allevata apposta per la ricerca scientifica."
    Totò "I maiali di questa razza sono speciali perché il nostro sistema fisiologico e immunitario è sorprendentemente simile a quello degli esseri umani."
    show toto rage 
    Totò "Siamo spesso utilizzati per testare trattamenti su malattie come il diabete, le patologie cardiovascolari e le malattie infettive."
    Totò "Un esempio particolare è l'uso di noi Göttingen per testare vaccini pediatrici, come quelli contro la pertosse."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto sad
    Totò "Il nostro sistema immunitario risponde in modo molto simile a quello di un bambino, il che aiuta a capire l'efficacia e la sicurezza di questi trattamenti prima che vengano somministrati agli esseri umani."
    show toto rage
    Totò "Ma c'è un aspetto che non viene mai raccontato: questa ricerca scientifica comporta un'enorme sofferenza per noi."
    Totò "Anche se esistono leggi che stabiliscono norme severe per la protezione degli animali usati a fini scientifici, la realtà è che spesso siamo sottoposti a grande stress fisico e psicologico nei laboratori."
    show toto sad
    Totò "Molte volte, le condizioni di detenzione non sono trasparenti e noi animali viviamo in un continuo stato di sofferenza, senza possibilità di scappare da quella che è una vera e propria prigione."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    Totò "Questa situazione solleva questioni etiche importanti, e non sono solo i maiali come me a soffrire."
    show toto rage
    Totò "In Italia, ogni anno vengono allevati oltre 550 milioni di polli Broiler, animali selezionati per crescere velocemente, ma a spese della loro salute."
    Totò "Questi polli sono geneticamente modificati per produrre carne, specialmente petto e cosce, ma questa crescita rapida causa gravi problemi fisiologici."
    show toto sad
    Totò "Molti di loro sviluppano difficoltà a camminare a causa del peso eccessivo, hanno problemi respiratori e spesso soffrono di insufficienza circolatoria, che li porta a morire prematuramente."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    Totò "E non è tutto. Vengono tenuti in spazi angusti, senza nessuno stimolo, in un ciclo di vita che dura al massimo 40-60 giorni."
    Totò "Un'esistenza che non è neanche un vero e proprio 'vivere'."
    Totò "La velocità con cui vengono cresciuti non solo danneggia i loro corpi, ma mette anche in discussione l'etica di un sistema che tratta gli animali come numeri in un processo produttivo."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "Anche topi, conigli e beagle sono sfruttati in esperimenti scientifici, vivendo sofferenze che non possono capire."
    Totò "I topi e i ratti sono tra gli animali più usati nei laboratori, perché si riproducono rapidamente e sono facili da gestire."
    show toto sad
    Totò "Sono utilizzati per studi genetici, ricerca su malattie come Alzheimer, Parkinson e anche per test oncologici sui farmaci."
    Totò "In molti casi, vengono geneticamente modificati per studiare malattie specifiche e sottoposti a trattamenti invasivi che danneggiano i loro corpi e le loro menti."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto rage
    Totò "I conigli, poi, sono usati soprattutto per test dermatologici e tossicologici."
    Totò "E anche se in Europa sono vietati i test cosmetici, in altre parti del mondo soffrono ancora a causa di pratiche crudeli come il Draize test, che provoca dolore agli occhi."
    Totò "Questi conigli vengono anche usati per testare vaccini e farmaci, ma spesso il loro corpo non riesce a tollerare queste sostanze, portandoli a sofferenze insostenibili."
    show toto sad
    Totò "I Beagle, una razza di cani molto docile, invece sono usati per testare pesticidi e sostanze chimiche."
    Totò "Sono scelti per il loro temperamento, ma subiscono trattamenti invasivi e condizioni di vita spaventose."
    Totò "Questi cani sono spesso tenuti in gabbie anguste per tutta la vita, separati dalla loro natura e dai loro istinti, e usati come cavie per testare prodotti che possono danneggiarli gravemente."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "Molti beagle sono costretti a sopportare esperimenti dolorosi, come test chirurgici invasivi, senza che ci sia una vera protezione per il loro benessere."
    Totò "Le loro vite sono ridotte a numeri e dati, senza che si tenga conto di quanto soffrono per esperimenti che potrebbero essere evitati."
    show toto sad
    Totò "Eppure, l'uso degli animali nella ricerca scientifica è difeso da molti per i benefici che porta alla salute umana."
    Totò "Ma sappiamo tutti che questo non giustifica la sofferenza che gli animali devono sopportare."
    show toto smile
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    Totò "Per fortuna, la comunità scientifica sta cercando nuovi modi per ridurre la dipendenza dagli animali."
    Totò "Oggi esistono tecnologie come organoidi umani e modelli in vitro, che potrebbero sostituire gli esperimenti sugli animali."
    show toto sad
    Totò "Ma c'è il bisogno soprattutto di una revisione globale delle normative, affinché si possa finalmente dire basta alla sofferenza degli animali nei laboratori."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto smile
    Totò "Io sono fortunato, perché sono qui al rifugio, dove posso vivere finalmente libero, senza paura, senza dolore."
    Totò "E non dimentico mai quanto è stato prezioso per me il mio nuovo inizio, e quanto invece tanti altri animali stanno ancora soffrendo."
    Totò "Ora vi invito a seguirmi nella prima tappa del nostro percorso e ricordate, ogni passo che faremo insieme sarà anche un passo per rendere il mondo un posto migliore per tutti gli animali."
    stop music fadeout 1.0
    jump vitaeiside

label vitaeiside:
    scene bg cani with fade
    play music "audio/vitaeiside.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto smile at left with dissolve
    Totò "Nel nostro rifugio, sono tanti gli animali che hanno vissuto storie molto tristi. Alcuni sono stati maltrattati, altri hanno vissuto in condizioni terribili."
    Totò "Oggi però, avremo l'occasione di conoscere qualcuno di loro, per aiutarvi a capire davvero cosa significa beness..."
    show toto normal
    "(Totò si ferma all'improvviso dopo essere stato travolto da qualcosa... o meglio qualcuno.)"
    play sound "audio/sfx/vita 1.mp3" volume 5
    "???" "Ehi, guarda chi c'è! Ciao Totò!"
    show vita smile at right with dissolve
    play sound "audio/sfx/iside 1.mp3" volume 1
    "???" "Ciao, ciao! Stavamo giocando a rincorrerci!" 
    show iside smile at right with dissolve
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto smile
    Totò "Eccole qui, le due cagnoline più energetiche della fattoria! Ciao Vita, ciao Iside!"
    Vita "Ciao a tutti! Come ha detto Iside stavamo giocando ad acchiapparella. Io però sono più veloce di lei!"
    Iside "Beh, certo, ma io so anche dove correre, non è solo questione di velocità."
    show toto normal
    show vita normal 
    show iside normal
    Totò "Ok, ok, fermiamoci un attimo! Ci siamo un po' distratti, eh?"
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    Totò "Sentite voi due, noi stiamo facendo un percorso per scoprire cos'è davvero il benessere animale."
    Totò "Volete raccontare un po' della vostra storia, per far capire anche ai visitatori cosa significa per voi?"
    hide toto with dissolve
    hide vita with dissolve
    play sound "audio/sfx/iside 2.mp3" volume 0.8
    show iside sad
    Iside "Oh, beh! La mia storia? È stata un po'... movimentata. Non è proprio un inizio tranquillo quello che mi è toccato!"
    show ph iside 0 with dissolve
    Iside "Un giorno sono arrivata da sola al cancello della fattoria che dà sulla vigna. Ero un cane da caccia, ma ero così spaventata!"
    hide ph iside 0 with dissolve
    show ph iside 1 with dissolve
    Iside "Mi sono allontanata dai miei padroni perché ero terrorizzata dagli spari, ed ero troppo piccola per quella vita."
    hide ph iside 1 with dissolve
    show ph iside 2 with dissolve
    Iside "Quando ci sono rumori forti, come fuochi d'artificio o colpi, mi paralizzo ancora dalla paura. È qualcosa che non riesco a controllare."
    hide ph iside 2 with dissolve
    play sound "audio/sfx/iside 1.mp3" volume 1
    show iside smile
    show ph iside 3 with dissolve
    Iside "Fortunatamente, sono arrivata al rifugio, dove mi sento al sicuro."
    Iside "Ora la paura è meno forte, ma ogni tanto torna."
    hide ph iside 3 with dissolve
    hide iside with dissolve
    play sound "audio/sfx/vita 2.mp3" volume 2.5
    show vita sad at right with dissolve
    Vita "Anche la mia storia, purtroppo, non è per niente divertente..."
    show ph vita 0 with dissolve
    Vita "Sono stata abbandonata vicino al rifugio, probabilmente anch'io perché non ero più utile per la caccia." 
    hide ph vita 0 with dissolve
    show ph vita 1 with dissolve
    Vita "Quando sono arrivata qui ero piccola, e avevo una paura tremenda. Mi sentivo sola e senza nessuno."
    hide ph vita 1 with dissolve
    show ph vita 2 with dissolve
    Vita "Non riuscivo a capire cosa stesse succedendo, e la mia paura mi faceva agire in modo distruttivo."
    hide ph vita 2 with dissolve
    show vita smile
    play sound "audio/sfx/vita 1.mp3" volume 5
    show ph vita 3 with dissolve
    Vita "Ora, anche se sono cresciuta, sono ancora la piccola monella della fattoria." 
    hide ph vita 3 with dissolve
    show ph vita 4 with dissolve
    Vita "Ma ho trovato finalmente un posto dove stare."
    hide ph vita 4 with dissolve
    show ph vita 5 with dissolve
    Vita "Mi sento fortunata ad essere qui, ma non dimentico mai quanto è stato difficile all'inizio."
    hide ph vita 5 with dissolve
    play sound "audio/sfx/iside 1.mp3" volume 1
    show iside smile at right with dissolve
    Iside "Adesso però posso dire per entrambe che ci sentiamo davvero felici e fortunate ad essere ospiti di questo santuario."
    Iside "Vivo qui da tre anni e ho stretto una gran bella amicizia con Vita, che è sempre lì per me."
    show iside normal
    Iside "Non so come sarebbe stata la mia vita se non fossi arrivata qui. Ma sono grata di poter vivere in pace."
    play sound "audio/sfx/vita 1.mp3" volume 5
    show vita normal 
    Vita "Anche io, come Iside, ho trovato il mio posto qui. Un luogo dove posso essere me stessa, senza paura e senza essere abbandonata."
    Vita "Ogni giorno è un'avventura, e anche se continuo a fare la monella, so che sono al sicuro."
    show vita smile 
    Vita "È il posto dove posso essere libera, senza più paura. E questo vale più di qualsiasi cosa."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto smile at left with dissolve
    Totò "Ragazze, ascoltarvi mi scalda sempre il cuore."
    Totò "Sapere che qui avete trovato la pace e la felicità mi rende ancora più orgoglioso di vivere in questo santuario."
    show vita normal 
    Vita "E poi diciamolo, Totò: la felicità si sente ovunque! Persino quando qualcuno, tipo me, fa piccoli disastri, giusto?"
    Totò "Ah, Vita, il tuo spirito ci fa sorridere tutti i giorni!"
    Totò "Però, parlando seriamente, abbandono e caccia restano problemi enormi per tanti animali."
    show iside sad
    show vita sad
    play sound "audio/sfx/iside 2.mp3" volume 0.8
    Iside "Purtroppo è vero, Totò. Ma sapere che possiamo fare qualcosa qui, anche solo raccontando le nostre storie, è importante."
    Totò "E c'è ancora tanto da dire sull'argomento. Forse è il momento giusto per parlarne."

    show vita normal 
    show iside normal
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "Quando si parla di abbandono degli animali domestici, ci si trova davanti a un problema tanto complesso quanto doloroso."
    Totò "In Italia, i numeri sono spaventosi: ogni anno si acuisce particolarmente nei mesi estivi."
    Totò "In questi periodi, molte persone scelgono di partire per le vacanze e si ritrovano a considerare gli animali come un peso. La soluzione più facile? Lasciarli per strada."
    show iside surprised
    play sound "audio/sfx/vita 1.mp3" volume 5
    show vita surprised 
    Vita "Ma come si può anche solo pensare una cosa del genere? Noi non siamo oggetti che si possono buttare via quando fa comodo."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    Totò "Esatto, Vita. Ed è proprio questo il problema: c'è chi vede gli animali come beni di consumo temporanei."
    show iside sad
    show vita sad 
    show toto sad 
    Totò "Un esempio? Durante il periodo del COVID-19, molti li hanno presi solo per avere una scusa per uscire di casa, salvo poi abbandonarli."
    show toto rage
    Totò "Nel 2023, si stima che in Italia siano stati abbandonati circa 384 animali domestici al giorno."
    Totò "Un trend purtroppo in crescita, che ci racconta una realtà davvero triste."
    play sound "audio/sfx/iside 2.mp3" volume 0.8
    Iside "Ogni giorno così tanti animali finiscono soli, senza sapere cosa fare o dove andare... mi si stringe il cuore solo a pensarci."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto sad 
    Totò "Gli animali abbandonati si trovano in una situazione disperata: rischiano incidenti stradali, fame, malattie, e possono persino essere sfruttati per attività illegali, come i combattimenti clandestini."
    show toto rage
    Totò "E non si tratta solo di un problema morale: abbandonare un animale è un reato penale in Italia."
    Totò "Chi lo fa rischia fino a un anno di carcere o multe salate, tra 1.000 e 10.000 euro."
    play sound "audio/sfx/vita 1.mp3" volume 5
    Vita "Serve molto di più di una multa per fermare certe persone!"
    show toto normal
    show vita normal
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto normal 
    Totò "Vero. Per fortuna, molte organizzazioni si impegnano a sensibilizzare le persone e a promuovere il possesso responsabile degli animali."
    Totò "E ci sono soluzioni per chi pensa di non farcela."
    play sound "audio/sfx/iside 1.mp3" volume 1
    Iside "Se solo tutti capissero quanto amore e fedeltà un animale può dare, forse ci sarebbero meno storie tristi come le nostre."
    show toto sad
    Totò "Hai ragione, Iside. Ma le campagne di sensibilizzazione da sole non bastano. Serve un cambiamento culturale, un impegno sociale per fermare questo fenomeno."
    show toto smile
    Totò "La responsabilità verso un animale non è qualcosa di temporaneo: è un impegno che dura tutta la vita, proprio come un'amicizia o un legame familiare."
    show iside smile
    play sound "audio/sfx/vita 1.mp3" volume 5
    show vita smile 
    Vita "Qui al santuario abbiamo trovato persone che capiscono questo."
    Vita "Per fortuna esistono posti così, ma non dovrebbero essere l'ultima speranza per nessuno."
    show iside normal
    show vita normal
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto normal
    Totò "Ed è importante ricordare che non stiamo parlando solo di cani o gatti. Tutti gli animali meritano rispetto e cura, indipendentemente dalla loro razza o ruolo."
    Totò "Un caso particolare, però, riguarda i cani da caccia proprio come voi. Sono tra le vittime più frequenti dell'abbandono."
    show vita sad
    play sound "audio/sfx/iside 2.mp3" volume 0.8
    show iside sad
    Iside "È una realtà davvero dura e io lo so bene. Sentire certi racconti fa venire i brividi."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto rage
    Totò "Infatti, venite trattati come strumenti, buoni solo finché utili. Ma il vostro abbandono è un dramma che non possiamo ignorare."
    Totò "Molti cacciatori scelgono di abbandonarli, spesso in luoghi remoti o lungo le strade, senza preoccuparsi minimamente di cosa succederà a loro."
    Iside "Non riesco a capire come qualcuno possa trattarci così dopo tutto quello che facciamo per loro."
    show toto sad
    Totò "Il trattamento dei cani da caccia durante l'addestramento è altrettanto drammatico. In alcune zone rurali, si usano tecniche brutali, come i collari elettrici, per 'correggere' il loro comportamento."
    Totò "Queste pratiche causano danni psicologici enormi. I cani diventano spaventati, ansiosi e spesso non riescono più a fidarsi degli umani."
    play sound "audio/sfx/vita 2.mp3" volume 2.5
    Vita "Mi chiedo come possano essere così crudeli con animali che darebbero tutto per loro."
    Vita "È come tradire un amico che ti è sempre leale."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "Nonostante in Italia esistano leggi severe contro il maltrattamento e l'abbandono, l'applicazione è spesso difficile, soprattutto nelle zone rurali."
    Totò "La tradizione venatoria, molto radicata in certe regioni, rende complicato intervenire."
    Totò "C'è una sorta di omertà che protegge chi maltratta o abbandona questi animali."
    show vita surprised
    play sound "audio/sfx/iside 1.mp3" volume 1
    show iside surprised
    Iside "È come se la loro sofferenza fosse invisibile per molti. Ma ogni vita ha valore, anche quella di un cane da caccia."
    show iside normal
    show vita normal
    play sound "audio/sfx/toto 1.mp3" volume 2.5 
    show toto normal
    Totò "Per fortuna, ci sono organizzazioni animaliste che si battono per cambiare le cose. Chiedono pene più severe per chi abbandona o maltratta questi cani."
    show toto rage
    Totò "Ma è un problema che riguarda non solo i cacciatori, ma tutta la società. Dobbiamo cambiare il modo in cui pensiamo agli animali."
    show iside sad
    show vita sad 
    Totò "E proprio a proposito di caccia, dobbiamo riflettere su quanto questa pratica sia immorale e distruttiva, non solo per i cani, ma per ogni animale coinvolto."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    Totò "La caccia, che molti chiamano tradizione, è in realtà una pratica che danneggia profondamente l'ambiente e le specie animali."
    show vita surprised
    show iside surprised
    show toto sad
    Totò "Ogni anno, intere popolazioni di uccelli e mammiferi vengono decimate, portando alcune specie vulnerabili sempre più vicine all'estinzione."
    Totò "E il danno non è solo per gli animali, ma anche per gli ecosistemi. Ogni specie ha un ruolo importante nell'equilibrio della natura."
    show iside sad
    show vita sad 
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto rage
    Totò "Un esempio evidente è la caccia agli ungulati, come cervi e caprioli, che spesso altera gli habitat naturali in cui essi vivono."
    Totò "Poi c'è la questione delle specie considerate invasive, come i cinghiali. Vengono cacciati in massa, ma senza valutare davvero se questo risolva i problemi."
    play sound "audio/sfx/vita 2.mp3" volume 2.5
    Vita "E non è strano? Prima li introducono per la caccia, poi li accusano di essere un problema."
    Vita "È un circolo vizioso che non porta a niente di buono."
    show toto sad
    Totò "Giusto, Vita. Molte specie sono state introdotte dall'uomo e ora sono percepite come un problema." 
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    Totò "Ma la risposta della caccia è spesso sproporzionata e basata su interessi economici, più che su una vera necessità di equilibrio ecologico."
    Iside "Questo dimostra quanto l'uomo possa essere contraddittorio. Prima provoca il problema, poi usa gli animali come capro espiatorio."
    show toto rage
    Totò "Spesso, i cacciatori giustificano l'abbattimento di animali come il cinghiale parlando di danni alle coltivazioni. Ma non considerano le alternative."
    Totò "Ad esempio, esistono metodi più sostenibili per gestire le popolazioni animali, senza dover ricorrere alla caccia indiscriminata."
    show toto normal
    show vita normal
    play sound "audio/sfx/iside 1.mp3" volume 1
    show iside normal
    Iside "La soluzione più efficace sarebbe non introdurre specie invasive, in primo luogo, invece di doverli cacciare quando diventano un 'problema'."
    Totò "Hai ragione, Iside. La vera sfida è cambiare la mentalità alla base, ogni azione dell'uomo sull'ambiente ha conseguenze che si ripercuotono su tutto il sistema naturale."
    play sound "audio/sfx/vita 1.mp3" volume 5
    Vita "Ed è una lezione che continuano a ignorare, causando danni non solo agli animali, ma anche a loro stessi."
    Totò "Ma facciamo un esempio concreto: le nutrie. Sono originarie del Sud America e sono arrivate qui in Italia perché l'uomo le ha importate per allevare pellicce."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    Totò "Quando il mercato delle pellicce è crollato, molti esemplari sono stati liberati o sono scappati, iniziando a proliferare in ambienti che non erano i loro naturali."
    Totò "Le nutrie, infatti, scavano tane lungo gli argini dei fiumi e danneggiano le coltivazioni nelle zone umide, causando problemi anche alla biodiversità locale."
    show vita sad
    show iside sad
    Iside "E ora vengono viste come nemiche, ma non sono state loro a decidere di venire qui."
    show toto rage
    Totò "Il caso della Disfida delle Nutrie a Parma è emblematico. Si è scelto di invogliare i cittadini a cacciare queste creature per ridurne la popolazione."
    show iside sad
    play sound "audio/sfx/vita 2.mp3" volume 2.5
    show vita sad        
    Vita "Un'idea davvero crudele. Invitare le persone a uccidere per risolvere un problema che hanno causato loro stessi è ingiusto."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    Totò "E non ha risolto nulla. Le associazioni animaliste hanno criticato duramente questa scelta, proponendo invece metodi più etici come la sterilizzazione."
    Totò "Purtroppo, la caccia alle nutrie è solo un sintomo di un problema più grande: l'idea che si possano risolvere gli errori umani uccidendo gli animali."
    Totò "Il vero errore è stato importarli per scopi economici senza pensare alle conseguenze. E ora sono loro a pagare per le nostre decisioni."
    show toto sad
    Totò "E questa dinamica si ripete per molte specie, non solo per le nutrie. L'uomo introduce, sfrutta e poi elimina, ignorando l'impatto sul loro e nostro futuro."
    Totò "Spesso, purtroppo, non ci si limita nemmeno a soluzioni legali o regolamentate."
    play sound "audio/sfx/iside 2.mp3" volume 0.8
    Iside "Alcuni non si fermano davanti a nulla, nemmeno alla legge. Ed è così che nascono pratiche ancora più crudeli..."
    show iside surprised
    show vita surprised
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage        
    Totò "Come il bracconaggio, che è una forma di sfruttamento ancora più brutale e pericolosa, sia per gli animali sia per l'ambiente."
    Totò "È un problema globale che colpisce specie iconiche come elefanti, rinoceronti e tigri."
    Totò "Questi animali vengono uccisi per i loro denti, ossa, pelli e corna, che alimentano un mercato illegale che ha un impatto devastante su di loro e sugli ecosistemi."
    show iside sad
    play sound "audio/sfx/vita 1.mp3" volume 5
    show vita sad 
    Vita "Devastante è un eufemismo! La gente uccide questi animali solo per ricavarci un profitto."
    Vita "E questo succede in un mercato gestito dalla criminalità?"
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto sad
    Totò "Purtroppo, non si tratta solo di pochi individui. Ogni anno, circa 35.000 elefanti vengono uccisi per l'avorio, e molte specie stanno diventando sempre più vulnerabili."
    Totò "E il peggio è che non c'è solo il commercio dell'avorio. La medicina tradizionale asiatica è responsabile della caccia a tigri e rinoceronti per le loro ossa e pelle."
    Totò "La tigre del Bengala è a rischio estinzione, con meno di 4.000 esemplari rimasti. Ogni pezzo del loro corpo è venduto a un prezzo altissimo."
    show toto rage  
    Totò "Questo mercato spinge sempre più animali verso l'estinzione."
    play sound "audio/sfx/iside 2.mp3" volume 0.8
    Iside "Ed è una tragedia che non si ferma! Non si tratta solo di perdere una specie, ma di danneggiare un intero ecosistema, che perde un predatore fondamentale."
    show toto sad
    Totò "Sì, e in molte aree del mondo, come l'Africa, la povertà spinge le persone a diventare bracconieri, alimentando questo ciclo senza fine."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "Ma c'è anche un altro problema: nonostante la creazione di riserve naturali protette, i bracconieri continuano ad entrare e uccidere animali protetti, come i rinoceronti."
    Totò "E quando vediamo che specie come il pangolino, uno degli animali più bracconati al mondo, vengono cacciate a ritmi devastanti, la situazione diventa ancora più tragica."
    Totò "Per non parlare della vaquita, un piccolo delfino che vive nel Golfo della California."
    Totò "Il bracconaggio per la pesca illegale di totani sta riducendo la sua popolazione a meno di dieci esemplari!"
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto sad
    Totò "Eppure, nonostante tutto ciò, la domanda di questi prodotti non cala, ed è questa domanda che alimenta la distruzione della fauna selvaggia."
    Vita "La gente non si ferma nemmeno di fronte all'estinzione, non si rendono conto che un mondo senza queste creature non sarà più lo stesso."
    Iside "E allora, quale sarà la vera soluzione? Solo fermando la domanda e creando un mondo dove gli animali sono protetti, possiamo fare la differenza."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "Per fermare la crudeltà e il disprezzo verso la fauna, dobbiamo cambiare la nostra visione della vita animale."
    Totò "Abbandonare animali, praticare la caccia indiscriminata e bracconare sono sintomi di un egoismo che non possiamo più ignorare."
    Totò "L'uomo, con il suo comportamento utilitaristico, è la causa di tanta sofferenza."
    Totò "La verità è che le leggi, purtroppo, non sono abbastanza forti per fermare questi abusi."
    play sound "audio/sfx/vita 2.mp3" volume 2.5
    Vita "È un po' come quando ci dimentichiamo dei cani da caccia abbandonati, come se non meritassero di essere trattati con dignità."
    show toto sad
    Totò "Esatto, Vita. Se non cambiamo la nostra mentalità e ci impegniamo concretamente, non potremo mai proteggere gli animali e il nostro ecosistema."
    Totò "È fondamentale educare le persone, sensibilizzarle sull'importanza di rispettare tutte le forme di vita."
    show vita normal
    show toto normal
    play sound "audio/sfx/iside 1.mp3" volume 1
    show iside normal
    Iside "La sensibilizzazione è davvero importante."
    Iside "Bisogna far capire che ogni essere vivente ha un valore intrinseco, non deve essere visto solo come un mezzo per un guadagno."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    Totò "Sono d'accordo, Iside. Solo con politiche più severe e comportamenti rispettosi possiamo fermare tutto questo."
    Totò "Il bracconaggio non è solo un crimine contro gli animali, ma anche contro l'ambiente."
    Totò "Dobbiamo anche lottare contro l'indifferenza. Non possiamo rimanere in silenzio mentre altre specie rischiano di scomparire per sempre."
    Totò "Ogni passo conta. Anche educare i più giovani a rispettare la natura e gli animali può fare la differenza. Un cambiamento di mentalità è fondamentale."     
    play sound "audio/sfx/vita 1.mp3" volume 5
    Vita "E non dobbiamo dimenticare che ogni animale salvato è un piccolo successo."
    Vita "Non possiamo permettere che la sofferenza continui, dobbiamo agire ora!"
    show toto smile
    Totò "Abbiamo il potere di cambiare le cose, se solo ci uniamo. Ogni battaglia conta, e ogni azione, anche piccola, è un passo verso un futuro migliore."
    play sound "audio/sfx/iside 1.mp3" volume 1
    Iside "Giusto, e bisogna farlo insieme. Ogni cittadino, ogni organizzazione, ogni governo: tutti devono lavorare per un mondo più giusto per gli animali."
    show toto normal 
    Totò "La strada è lunga, ma con educazione, sensibilizzazione e azioni concrete, possiamo arrivare alla fine. Il nostro impegno è ciò che fa la differenza."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto smile
    Totò "Voglio davvero ringraziarvi, Vita e Iside. È stato un onore poter condividere questo momento con voi."
    Totò "La vostra energia e la vostra passione sono contagiose, e vedere come, nonostante il vostro passato, siete riuscite a diventare così forti e felici è davvero ispirante."
    show iside smile
    play sound "audio/sfx/vita 1.mp3" volume 5
    show vita smile       
    Vita "Grazie, Totò! È stato molto costruttivo parlare di queste cose con te!"
    Iside "Anche per me, grazie di cuore. È sempre un piacere parlare di cose che ci stanno tanto a cuore."
    show toto normal
    Vita "Ora però basta chiacchiere! È il momento di ricominciare a giocare! Prova a prendermi Iside!" 
    hide vita with dissolve
    play sound "audio/sfx/iside 1.mp3" volume 1
    Iside "Aspetta un attimo, Vita, devo salutare Totò e gli ospiti."
    Iside "Grazie per averci ascoltato, è stato davvero bello."
    Iside "Ora scusatemi, ho un cagnolino da rincorrere e non posso lasciarmelo scappare. Ciao, Ciao!"
    hide iside with dissolve
    show toto smile
    Totò "Ah, la vostra energia è davvero incredibile. Non vi fate male!"
    Totò "Beh, sembra proprio giunto il momento di andare avanti nel nostro percorso. Seguitemi!"
    stop music fadeout 1.0
    jump wonder

label wonder:
    scene bg fieno with fade
    play music "audio/wonder.mp3" volume 0.7 fadein 1.0 loop
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto smile at left with dissolve
    Totò "Eccoci arrivati! Ora, voglio presentarvi un'altra mascotte del nostro santuario"
    Totò "Si tratta di una pecorella molto speciale che ha fatto breccia nei cuori di tutti. È un po' timido, ma è una vera star qui!"
    show toto normal
    Totò "Scusate un attimo, devo chiamarlo... Wonder, puoi venire un attimo qui?"
    play sound "audio/sfx/wonder 1.mp3" volume 1
    "Si eccomi... sto arrivando!" 
    show toto smile 
    Totò "Vi chiedo di avere un po' di pazienza, ci mette sempre un po' ad arrivare"
    play sound "audio/sfx/wonder 2.mp3" volume 2
    show wonder normal at right with dissolve
    Wonder "Ciao, Totò... ehm, scusa, perché mi hai chiamato?"
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto normal
    Totò "Ciao Wonder, ti ho chiamato perché oggi abbiamo degli ospiti speciali, e volevo presentarti a loro."
    Totò "Stiamo facendo un percorso per far capire cos'è il vero benessere animale, e sarebbe fantastico se potessi raccontare la tua storia."
    Totò "La tua è una testimonianza importante della seconda chance che hai avuto qui al santuario."
    hide toto with dissolve
    play sound "audio/sfx/wonder 1.mp3" volume 1
    show ph wonder 0 with dissolve
    Wonder "Oh... ehm ok, ciao a tutti... io sono Wonder. "
    Wonder "Mi fa un po' imbarazzo parlare così... però, sì, posso raccontarvi la mia storia."
    hide ph wonder 0 with dissolve
    show wonder sad 
    Wonder "Prima di arrivare al santuario, stavo... stavo in un posto davvero brutto. Un allevamento... dove facevano cose orribili."
    Wonder "Per esempio, quando ci sono troppi agnellini, li... li smaltiscono, capite? Li seppelliscono vivi..."
    play sound "audio/sfx/wonder 2.mp3" volume 2
    show wonder normal 
    Wonder "Una ragazza ha sentito parlare di quello che succedeva e ha deciso di fare qualcosa."
    Wonder "È riuscita a parlare con un operaio e a convincerlo a salvarmi. Io ero appena nato, non avevo nemmeno poche ore... e... e mi hanno portato fuori dal recinto."
    Wonder "Era così strano... ma c'era lei, la ragazza. Mi ha preso e mi ha avvolto in un asciugamano. Mi ha portato subito al santuario."
    show wonder sad
    show ph wonder 1 with dissolve
    Wonder "Quando sono arrivato qui, ero davvero spaventato... e debole... Non volevo mangiare, non riuscivo a calmarmi."
    hide ph wonder 1 with dissolve
    show wonder smile
    play sound "audio/sfx/wonder 1.mp3" volume 1
    show ph wonder 2 with dissolve
    Wonder "Ma Sara e Vito mi sono stati vicini, mi hanno fatto sentire al sicuro."
    hide ph wonder 2 with dissolve
    show wonder normal
    show ph wonder 3 with dissolve
    Wonder "Sono stati gentili con me, e mi hanno anche dormito accanto per un mese. Sì, sono rimasto vicino a loro per tutto quel tempo."
    hide ph wonder 3 with dissolve
    show ph wonder 4 with dissolve
    Wonder "Mi sentivo così al sicuro con papà Vito che lo seguivo ovunque... anche nei lavori in vigna."
    hide ph wonder 4 with dissolve
    show wonder smile
    play sound "audio/sfx/wonder 2.mp3" volume 2
    show ph wonder 5 with dissolve 
    Wonder "E, ehm... sapete una cosa? Quando hanno fatto il primo vino del santuario, l'hanno dedicato a me. Si chiama 'Wonder Wine'."
    Wonder "Io non credo che sia così speciale, ma loro dicono che lo è e io sono felice di aver avuto un posto speciale nel loro cuore."
    hide ph wonder 5 with dissolve
    show wonder normal
    show ph wonder 6 with dissolve 
    Wonder "Oggi sono... sono uno degli animali più grandi qui, ma sono ancora un po' timido."
    hide ph wonder 6 with dissolve
    play sound "audio/sfx/wonder 1.mp3" volume 1
    show ph wonder 7 with dissolve
    Wonder "Mi spavento facilmente, ma... se qualcuno mi fa una carezza, piano piano riesco a fidarmi."
    Wonder "È così che funziona per me."
    hide ph wonder 7 with dissolve
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto smile at left with dissolve
    Totò "Grazie per aver condiviso la tua storia con noi Wonder."
    Totò "La tua esperienza è un bellissimo esempio di quanto possano essere ingiuste le condizioni che alcuni animali devono affrontare."
    Totò "La tua vita, fortunatamente, è cambiata, ma non tutti hanno la stessa fortuna."
    Totò "La mercificazione degli animali è uno dei problemi più gravi che dobbiamo affrontare e si estende ben oltre l'allevamento industriale..."
    
    show toto sad 
    show wonder sad 
    Totò "Molto spesso gli animali vengono visti come beni di consumo, oggetti da sfruttare per soddisfare i bisogni dell'uomo, anziché esseri viventi con emozioni e necessità proprie."
    Totò "Uno dei settori più colpiti da questa mentalità è sicuramente la moda, dove pellicce e pelli vengono utilizzate come simboli di lusso."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage 
    Totò "Gli animali, come i visoni, vengono allevati in gabbie piccolissime e uccisi in modo cruento per estrarre il loro pelo."
    Totò "Fino a poco tempo fa, in Italia esistevano numerosi allevamenti di visoni, in cui gli animali vivevano in condizioni disumane, malati e stressati."
    Totò "Nonostante le leggi abbiano fatto qualche passo avanti, il problema persiste ancora in molte zone del mondo."
    play sound "audio/sfx/wonder 2.mp3" volume 2
    Wonder "Uhm... è davvero difficile pensare che alcuni animali vengano trattati in questo modo... Mi sembra... così ingiusto."
    show toto sad 
    Totò "E non si tratta solo della moda. Anche gli zoo e i circhi sono luoghi dove gli animali vengono trattati come attrazioni."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto rage 
    Totò "In questi ambienti, molte specie selvatiche sono costrette a vivere lontano dai loro habitat naturali, rinunciando a comportamenti naturali come cacciare o spostarsi liberamente."
    Totò "Nei circhi, gli animali sono addestrati a compiere azioni che non farebbero mai in natura."
    Totò "Per esempio, devono eseguire numeri acrobatici che richiedono comportamenti innaturali, come saltare attraverso cerchi infuocati o stare in equilibrio su piccole piattaforme."
    show wonder surprised
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto sad
    Totò "Per ottenere questi risultati, spesso vengono usate punizioni fisiche o tecniche psicologiche estremamente cruente."
    Totò "L'addestramento può includere collari elettrici, scosse per costringere l'animale a eseguire un comportamento, o l'uso di cibo come ricompensa in modo da manipolare il loro comportamento."
    show wonder sad 
    Totò "Questo crea uno stato di paura costante, che minaccia il benessere psicologico dell'animale."
    play sound "audio/sfx/wonder 1.mp3" volume 1
    Wonder "Io... io non so come facciano. Quando qualcuno mi tocca o mi fa paura, mi nascondo subito."
    Wonder "Non posso immaginare vivere in un posto dove non posso fare quello che mi viene naturale..."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto rage 
    Totò "Sì, Wonder. È terribile, ma succede. E la situazione negli zoo non è molto diversa."
    Totò "Sebbene possano sembrare posti dove gli animali sono più 'liberi', la realtà è che sono ancora privati della possibilità di vivere come farebbero in natura."
    Totò "Molti zoo mettono gli animali in spazi troppo piccoli, lontano dai loro habitat naturali."
    show toto sad
    Totò "Le specie selvatiche, ad esempio, vengono costrette a vivere in ambienti artificiali che non sono affatto adatti alla loro specie."
    show wonder sad 
    Totò "Non possono cacciare, esplorare, o comportarsi come farebbero nel loro ambiente naturale."
    play sound "audio/sfx/wonder 2.mp3" volume 2
    Wonder "Dev'essere davvero difficile per loro... quando si sentono chiusi, senza poter fare ciò che vogliono."
    Wonder "Mi rendo conto che... anche se il santuario è un posto tranquillo, io non mi sentirei mai a mio agio se fossi in una gabbia tutto il giorno."
    Totò "E purtroppo, il problema non si limita solo al mondo fisico. Anche nel mondo digitale, l'uso illecito di animali per l'intrattenimento è in aumento."
    show toto rage
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show wonder surprised
    Totò "Un esempio recente è lo scandalo del sito 'Hatemonkeys', dove delle povere scimmie venivano utilizzati in video e foto per attrarre visitatori e guadagni, spesso in condizioni terribili."
    Totò "Molti di questi animali erano costretti a esibirsi in situazioni violente e innaturali, spesso ripresi senza alcun rispetto per la loro sicurezza o benessere."
    show toto sad
    show wonder sad
    Totò "Questo è diventato un enorme problema online, dove il profitto è messo davanti alla vita degli animali."
    Totò "E la cosa peggiore è che certi contenuti vengono visualizzati da milioni di persone, contribuendo a normalizzare l'idea che gli animali possano essere trattati come oggetti per il nostro intrattenimento."
    Totò "Questo tipo di sfruttamento non solo danneggia gli animali, ma incide anche sulla nostra cultura, facendo sembrare normale l'uso di esseri viventi come strumenti per il guadagno."
    play sound "audio/sfx/wonder 1.mp3" volume 1
    show wonder surprised 
    Wonder "E... e nessuno sembra pensarci... come se non fosse davvero un problema..."
    Wonder "È orribile sapere che qualcuno ha fatto queste cose... e... e io, che avevo bisogno di qualcuno che mi aiutasse, non posso immaginare cosa abbiano passato loro."
    show wonder normal
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto normal        
    Totò "Esattamente, Wonder. Dobbiamo imparare a vedere gli animali come individui con sentimenti e bisogni."
    Totò "Ecco perché è così importante fermare la mercificazione degli animali, per dare loro una vita che non sia segnata dallo sfruttamento."
    show wonder smile
    Wonder "Sì... sì, sarebbe bello... vedere più persone che si prendono cura di noi."
    show toto normal
    Totò "E questo cambiamento dipende da tutti noi. Ogni scelta che facciamo può fare la differenza."
    Totò "Bisogna smettere di pensare che gli animali non abbiano emozioni."
    show wonder surprised
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "Molti credono ancora che gli animali non provino emozioni complesse, come se fossero esseri inferiori a noi, incapaci di gioire o soffrire."
    show wonder sad
    Totò "Ma questo è un errore enorme, che purtroppo ha radici profonde nella nostra cultura."
    Totò "In realtà, ogni giorno ci insegnano che siamo più simili di quanto pensiamo."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto sad 
    Totò "Eppure, molti ancora li considerano solo come esseri privi di emozioni, incapaci di soffrire o di gioire."
    Totò "Studi scientifici inoltre hanno ampiamente dimostrato che gli animali sono capaci di emozioni simili alle nostre: possono sentirsi felici, tristi, spaventati e anche mostrare empatia verso gli altri."
    show toto rage
    show wonder surprised
    Totò "Ma ancora oggi, cè chi nega questa evidenza per giustificare sfruttamenti terribili."
    show wonder sad
    Totò "Questa visione sbagliata non solo alimenta la mercificazione degli animali, ma minaccia anche il nostro stesso concetto di compassione."
    Totò "Quando trattiamo gli animali come oggetti, ci dimentichiamo che anche loro hanno diritti e sentimenti che meritano rispetto."
    play sound "audio/sfx/wonder 2.mp3" volume 2
    show wonder normal
    Wonder "Oh... io... io non so, ma... quando... quando qualcuno si avvicina a me... posso sentire la sua gentilezza, anche se sono timido."
    Wonder "È come se... sentissi una connessione, come se potessi capire... che mi vuole bene."
    show wonder sad
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto sad
    Totò "Eppure, non tutti vedono gli animali così, come esseri che meritano rispetto. La sofferenza degli animali è invisibile per molti, perché l'unica cosa che conta è il profitto che ne può derivare."
    Totò "Ma la verità è che non possiamo ignorare il loro dolore. Le loro emozioni, le loro paure, il loro piacere... sono reali."
    Totò "E quando non li consideriamo come esseri viventi con diritti, non facciamo altro che alimentare un ciclo di violenza che danneggia tutti."
    Wonder "Mi... mi fa tristezza pensare a tutto ciò. Non sono un esperto, ma... posso sentire che... che gli animali soffrono, proprio come me a volte."
    Wonder "E se potessero parlare, forse racconterebbero la loro sofferenza."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto normal
    Totò "Se vogliamo un mondo più giusto, bisogna riconoscere l'intrinseco valore degli animali."
    Totò "Dobbiamo smettere di considerarli merce e iniziare a trattarli come esseri viventi con emozioni e diritti."
    show wonder surprised 
    play sound "audio/sfx/wonder 1.mp3" volume 1
    Wonder "Io... io non riesco a capire come possano far loro del male... non so... ma so che voglio vivere in un mondo dove nessuno faccia soffrire nessuno... per guadagnare."
    show wonder normal 
    Totò "Esattamente, Wonder. Non possiamo più ignorare la sofferenza. È tempo di agire, di rendere il benessere degli animali una priorità."
    Wonder "Sì... sì, credo che dovremmo tutti pensare a quello che provano... anche se sono solo... pecore come me."
    Wonder "E... e forse, allora, gli altri smetteranno di trattarci come se fossimo solo... cose. Ma... è un passo che dobbiamo fare insieme, tutti."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto smile 
    Totò "Esatto, Wonder. È un cammino che dobbiamo percorrere insieme, un passo alla volta, per un mondo dove tutti gli esseri viventi possano essere rispettati."
    show wonder smile
    Wonder "È... è bello pensarlo, ma dobbiamo ricordarci che... ogni piccolo gesto conta, no?"
    Totò "Ogni gesto fa la differenza, Wonder. Ed è per questo che dobbiamo continuare a lottare, insieme."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto normal 
    Totò "Detto questo grazie davvero, Wonder, per il tuo tempo e per aver condiviso la tua storia con noi."
    show wonder normal 
    Totò "È stato davvero un piacere sentire la tua testimonianza e vedere quanto sei cambiato."
    play sound "audio/sfx/wonder 2.mp3" volume 2
    Wonder "Oh, ehm... grazie a voi. È stato davvero bello anche per me. Scusate se sono stato così... ma sento che c'è del bene in voi."
    show wonder smile 
    Wonder "Non vedo l'ora di rivedervi alla fattoria. Magari ci sarà un altro momento per stare insieme."
    Wonder "Comunque, devo proprio andare... la mia amica Luisa mi sta aspettando per uno spuntino, e non voglio farla aspettare troppo."
    Wonder "Arrivederci a tutti, spero di rivedervi presto! Grazie per avermi ascoltato!" 
    hide wonder with dissolve
    show toto smile 
    Totò "Che anima incredibile, Wonder. Siamo davvero fortunati ad avere persone... ehm, animali come lui con noi. È una benedizione."
    show toto normal 
    Totò "Ma adesso è il momento di andare avanti."
    Totò "Vi accompagnerò in un posto speciale per me, dove ci sono i miei amici maialini. Venite, seguitemi!"
    stop music fadeout 1.0
    jump mariarosa

label mariarosa:
    scene bg maiali with fade
    play music "audio/mrosa.mp3" volume 0.7 fadein 1.0 loop
    pause 1.5
    scene bg maialini with fade
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto smile at left with dissolve
    Totò "Eccoci qui, questo è il recinto dei maialini!"
    show toto normal
    Totò "Non vi ho portati qui per raccontarvi la storia di uno dei miei compagni, anche se ci sarebbe da parlarne per ore."
    Totò "Come della scatenata Tilly o di Sara, che ormai è la nonnina più saggia del gruppo."
    show toto smile
    Totò "Ma oggi non sono loro le protagoniste. Vi ho portati qui per farvi conoscere una storia davvero speciale."
    show toto normal
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show ph mrosa 0 with dissolve
    Totò "Si tratta della storia di Mariarosa, una rifugiata che ha avuto un ruolo fondamentale nel far diventare il santuario quello che è oggi." 
    Totò "Sapete, tempo fa viveva proprio qui, nello stesso posto dove oggi abitano tutti questi maialini."
    hide ph mrosa 0 with dissolve
    show toto sad
    Totò "Mariarosa era una maialina della razza Piétrain. Ha vissuto tutta la sua vita in un allevamento, vedendo i suoi piccoli portati via ogni volta."
    Totò "La sua vita era già stata decisa: doveva ingrassare per poi finire al macello."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show ph mrosa 1 with dissolve
    Totò "Quando quel giorno arrivò e si trovò sul camion diretto al macello, Mariarosa capì cosa l'aspettava."
    Totò "Presa dal panico, si lanciò giù, ferendosi gravemente alla gamba destra."
    Totò "È rimasta lì, a terra, per quasi un giorno e mezzo."
    hide ph mrosa 1 with dissolve
    show toto normal
    show ph mrosa 2 with dissolve
    Totò "Ma poi, per fortuna, un signore che passava di lì ha visto questo grosso maiale di quasi trecento chili."
    hide ph mrosa 2 with dissolve
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto sad
    Totò "Quando l'hanno trovata, aveva segni di morsi su tutto il corpo. Dei cani randagi, affamati, avevano cercato di mangiarla mentre era ancora viva."
    show toto normal
    show ph mrosa 3 with dissolve
    Totò "Il signore ha chiamato subito l'ASL e chiunque potesse intervenire. Fu allora che il rifugio venne contattato."
    Totò "Con l'aiuto dei vigili del fuoco e dei volontari locali, riuscimmo a caricarla su un carroattrezzi."
    hide ph mrosa 3 with dissolve
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto sad
    show ph mrosa 4 with dissolve
    Totò "Quando Mariarosa arrivò in fattoria, era spaventatissima e debolissima."
    show toto normal
    Totò "La prima notte la passò fuori, vicino a Luna, sotto le stelle. Sembrava che quella pace le servisse."
    hide ph mrosa 4 with dissolve
    show toto sad
    Totò "Il giorno dopo arrivò il veterinario. La sedammo e la portammo in stalla per iniziare a curare la sua gamba."
    Totò "Era chiaro che aveva sofferto tanto."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto normal
    show ph mrosa 5 with dissolve
    Totò "Poiché era stata messa all'ingrasso in allevamento, per aiutarla, dovemmo cambiarle la dieta."
    hide ph mrosa 5 with dissolve
    show toto smile
    show ph mrosa 6 with dissolve
    Totò "Pian piano, la sua forza tornava. Dopo tante cure, Mariarosa riuscì finalmente a stare in piedi da sola."
    show toto sad
    Totò "Era una vittoria, ma purtroppo i danni interni erano più gravi di quanto pensassimo."
    hide ph mrosa 6 with dissolve
    Totò "Le cellule della cancrena erano entrate in circolo e avevano raggiunto i polmoni, causando un edema polmonare."
    Totò "Quando arrivò il freddo, le venne una polmonite."
    Totò "Mariarosa lottò per sei mesi, con tutto il coraggio che aveva. Ma alla fine, non ce l'ha fatta."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto normal
    show ph mrosa 7 with dissolve
    Totò "Ha lasciato questo mondo, ma non ha mai lasciato i nostri cuori."
    Totò "Mariarosa non è stata solo un simbolo per noi maialini. È diventata un esempio di lotta per il diritto di vivere liberi e per il diritto di scegliere come e dove morire."
    hide ph mrosa 7 with dissolve
    show toto rage
    Totò "Lei ha dimostrato che tutti gli animali meritano rispetto, che nessuno dovrebbe essere trattato come un oggetto. È una lezione che non dimenticheremo mai."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto sad
    show ph mrosa 8 with dissolve
    Totò "Mariarosa è diventata un simbolo anche per le lotte delle donne."
    Totò "Pensateci: le maialine, le mucche e le pecore subiscono abusi, vengono private dei loro piccoli, sfruttate e poi uccise."
    Totò "Non è diverso da certe ingiustizie che accadono anche agli esseri umani."
    hide ph mrosa 8 with dissolve
    show toto rage
    Totò "Questa connessione ci insegna che tutte le lotte sono intrecciate. Difendere i diritti di uno significa difendere i diritti di tutti."
    show toto normal
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show ph mrosa 9 with dissolve
    Totò "Oggi, il santuario è ciò che è grazie anche a Mariarosa."
    Totò "Guardate questi maialini: vivono in pace, felici, nello stesso posto dove ha passato i suoi ultimi mesi. È il suo lascito più grande."
    hide ph mrosa 9 with dissolve
    show toto smile
    Totò "Per me, raccontare la sua storia è come renderle omaggio. La sua forza ci guida ogni giorno, ricordandoci perché facciamo tutto questo."
    show toto sad
    Totò "Ma la sua storia ci ricorda anche che ci sono ancora troppi animali che vivono in condizioni terribili."
    Totò "Negli allevamenti, milioni di vite vengono sfruttate e maltrattate ogni giorno, senza alcuna possibilità di riscatto."
    
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto normal
    Totò "Ma ora vi racconterò meglio cosa significa vivere in quei luoghi e perché dobbiamo continuare a lottare per loro."
    show toto rage
    Totò "Quando si parla di allevamenti intensivi, si parla di luoghi dove gli animali vengono trattati come macchine, con l'unico obiettivo di produrre di più nel minor tempo possibile."
    show toto sad
    Totò "Negli allevamenti, la sofferenza degli animali inizia dal primo momento di vita."
    Totò "Immaginate di essere separati dalla vostra mamma subito dopo essere nati, senza mai poter creare un legame affettivo con lei."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    Totò "Questo accade ogni giorno a mucche, maiali, polli e pecore, che vengono privati della possibilità di vivere secondo la loro natura."
    show toto rage
    Totò "Spesso sono rinchiusi in spazi così piccoli da non potersi muovere liberamente, senza mai vedere la luce del sole, toccare un filo d'erba o respirare aria pulita."
    Totò "Anche le condizioni sanitarie di questi luoghi lasciano molto a desiderare."
    show toto sad
    Totò "Nei macelli le condizioni igieniche sono spesso terribili per risparmiare sui costi e aumentare la produttività."
    Totò "Gli animali vivono ammassati, costretti a stare tra le loro feci, con un rischio costante di infezioni."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "Negli ultimi anni abbiamo visto epidemie causate dalla mancanza di controlli adeguati in questi allevamenti, oltre a casi di carne contaminata messa in commercio."
    Totò "E per nascondere la scarsa qualità delle carni, si usano additivi chimici per migliorarne l'aspetto e la conservazione"
    Totò "Purtroppo, non sempre questi trattamenti sono controllati a dovere, aumentando i rischi per chi consuma questi prodotti."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto sad 
    Totò "E poi c'è il trasporto verso il macello, un viaggio che può durare ore, a volte giorni, senza cibo né acqua."
    Totò "Durante questi trasporti, gli animali provano paura e stress enormi. È una situazione che nessuno dovrebbe vivere."
    Totò "E quando arrivano al macello, quello che li attende è altrettanto crudele."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "La pratica dello stordimento dovrebbe ridurre la loro sofferenza prima dell'uccisione, ma spesso non funziona come dovrebbe."
    Totò "In tanti casi, gli animali restano coscienti, sentendo dolore e paura fino all'ultimo istante della loro vita."
    Totò "Inoltre in questi luoghi procedure dolorose come la castrazione o la mutilazione del becco per i polli vengono eseguite senza anestesia, aggiungendo ulteriore sofferenza."
    show toto sad 
    Totò "Gli animali allevati per la loro carne non sono protetti da leggi che impediscano i maltrattamenti."
    Totò "Vivono una vita di sofferenza e miseria negli allevamenti intensivi di tutto il mondo, e questa è una realtà che dobbiamo cambiare."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto rage
    Totò "Per non parlare degli allevamenti estensivi, che dovrebbero offrire condizioni migliori, ma non sono esenti da problemi."
    Totò "In teoria, gli animali qui possono muoversi liberamente e vivere più vicini alla loro natura. Ma anche in questi casi ci sono difficoltà."
    Totò "Ad esempio, l'uso intensivo delle risorse naturali, come acqua e terra, ha un forte impatto ambientale."
    show toto normal
    Totò "Alcuni allevatori stanno cercando di adottare metodi più sostenibili, come l'agricoltura rigenerativa."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "Ma dobbiamo ricordarci che allevare animali, in qualsiasi forma, ha un costo elevato per il pianeta, e noi ne siamo responsabili."
    Totò "Non possiamo continuare a ignorare quanto dolore e distruzione siano causati da questo sistema."
    show toto sad
    Totò "E per questo, voglio farvi riflettere su quanto davvero sia profonda la sofferenza che gli animali vivono ogni giorno in questi luoghi." 
    Totò "Solo così potrete capire davvero cosa significa essere un animale in un allevamento."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto rage
    Totò "Pensate ai bovini, negli allevamenti subiscono mutilazioni dolorosissime, come il taglio delle corna o la castrazione, senza anestesia."
    Totò "Nessuno si preoccupa del loro dolore, perché non viene considerato importante."
    show toto sad
    Totò "Le scrofe, invece, passano la loro esistenza in gabbie così strette che non riescono nemmeno a girarsi, ingravidate di continuo e incapaci di accudire i loro piccoli. È crudele sotto ogni punto di vista."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "E i polli? Sono i più maltrattati al mondo. In pochi sanno che vengono allevati in capannoni sovraffollati e luridi, con migliaia di loro simili, e il loro corpo è una prigione."
    Totò "Sono stati selezionati per crescere così in fretta che i loro organi non riescono a reggere il peso."
    Totò "Molti muoiono per attacchi cardiaci o insufficienze respiratorie prima ancora di essere portati al macello."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto sad
    Totò "Anche gli agnelli subiscono crudeltà indicibili."
    Totò "A pochi giorni dalla nascita, gli mozzano la coda senza anestesia, provocando un dolore enorme e spesso infezioni o problemi cronici."
    Totò "Poi ci sono i conigli, il secondo animale terrestre più allevato in Europa. Vivono stipati in gabbie di metallo piccolissime, dove non possono nemmeno muoversi."
    Totò "È come vivere in una trappola per tutta la vita."
    show toto rage
    Totò "La macellazione dei conigli è altrettanto spaventosa. Spesso sono ancora coscienti mentre vengono appesi per le zampe posteriori."
    Totò "Pensate alla paura e al dolore che provano."
    Totò "In alcune parti del mondo, anche i cani sono considerati animali da allevamento."
    Totò "Vivono in gabbie sovraffollate o minuscole, senza alcuna protezione legale contro maltrattamenti e abusi."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto sad
    Totò "Il punto è che tutti questi animali soffrono allo stesso modo, a prescindere dalla loro specie."
    Totò "Una gallina, un cane, una mucca... tutti provano lo stesso dolore e la stessa paura quando sono privati della loro libertà e costretti a vivere in condizioni disumane."
    Totò "Non dovremmo fare distinzioni tra un animale domestico e uno da allevamento."
    show toto rage
    Totò "Una gallina ha lo stesso diritto di un cane a vivere una vita dignitosa, senza soffrire, senza essere sfruttata."
    Totò "La loro sofferenza è uguale, e merita lo stesso rispetto."
    Totò "Eppure, continuano a morire per produrre carne, uova e latte, solo perché li consideriamo diversi."
    Totò "Ma vale davvero la pena causare tanto dolore solo per un pasto? È questa la domanda che dovremmo tutti chiederci."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto normal
    Totò "Cambiare non è solo un atto di compassione verso gli animali, ma anche verso noi stessi e il pianeta. Perché tutto è collegato."
    show toto sad
    Totò "In Italia, il caso della peste suina africana è un esempio emblematico di come l'allevamento intensivo possa diventare un terreno fertile per malattie."
    Totò "È una malattia virale che ha colpito i suini in Italia, diffondendosi rapidamente a causa delle condizioni igieniche scarse e del sovraffollamento negli allevamenti."
    show toto rage
    Totò "Nonostante non rappresenti un rischio diretto per l'uomo, il suo impatto sugli animali è stato devastante."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto sad
    Totò "Migliaia di suini sono stati abbattuti preventivamente, sollevando interrogativi etici e sanitari riguardo alla gestione di questi focolai."
    Totò "Gli allevamenti intensivi, con il loro abuso di antibiotici e la mancanza di misure di controllo adeguate, sono alla base della diffusione di queste malattie."
    Totò "Le zoonosi, come la peste suina africana, sono un chiaro segnale che il modello di produzione intensiva è insostenibile e pericoloso."
    show toto rage
    Totò "E questo ci porta a un caso che dimostra quanto siano drammatiche le conseguenze di un sistema che non tutela né gli animali né la salute umana: la strage al santuario Cuori Liberi."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto normal
    Totò "Questo rifugio accoglieva maiali salvati da terribili situazioni, dove finalmente avevano trovato un po' di pace."
    show toto sad
    Totò "Ma, purtroppo, la peste suina africana è riuscita ad entrare nel santuario, causando una vera tragedia."
    Totò "La malattia ha colpito e portato alla perdita di tanti maialini che avevano trovato una seconda possibilità."
    show toto normal
    Totò "Eppure, nonostante tutto, alcuni di loro sono sopravvissuti. Piccole storie di speranza in mezzo alla devastazione."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "La cosa più assurda è che, nonostante questi animali non rappresentassero un pericolo per la salute pubblica, le autorità hanno deciso per l'abbattimento preventivo di tutti i maiali rimasti."
    Totò "Una decisione che ha distrutto una comunità di animali che avevano trovato un posto sicuro, lontano dai rischi degli allevamenti intensivi."
    show toto sad
    Totò "Questa decisione ha sollevato una forte opposizione da parte di attivisti e associazioni animaliste, come la Rete dei Santuari di Animali Liberi, che hanno denunciato l'uccisione come una scelta inutile e ingiustificata."
    show toto rage
    Totò "Gli animali del santuario vivevano in un ambiente sicuro, protetti da misure di sicurezza che dovevano garantire l'assenza di rischi di contagio."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    Totò "Eppure, le autorità sanitarie non hanno preso in considerazione le alternative proposte dal rifugio."
    Totò "La rigidità delle autorità ha scatenato il dibattito sulla gestione delle epidemie nei santuari."
    Totò "I rifugi dovrebbero essere trattati diversamente dagli allevamenti produttivi, poiché ospitano animali che non sono destinati al mercato."
    show toto sad
    Totò "Le autorità, agendo sulla base del principio di precauzione e tutelando l'economia degli allevamenti, non hanno tenuto conto del benessere degli animali sani."
    Totò "La storia del rifugio Cuori Liberi non è solo una tragedia per quegli animali, ma anche uno specchio di un conflitto più grande che ci riguarda tutti."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto rage
    Totò "Da una parte c'è la salute pubblica, giustamente da proteggere, ma dall'altra c'è la vita degli animali, che merita rispetto e dignità."
    Totò "Non possiamo più accettare che vengano sacrificati esseri viventi solo perché ci sono dei protocolli che non tengono conto del loro valore."
    show toto sad
    Totò "E alla fine, quello che ci insegnano casi come questo è che la sicurezza e la salute non possono essere la scusa per ignorare il dolore e la sofferenza degli animali."
    Totò "Dai laboratori agli allevamenti, dalla caccia agli animali abbandonati, ogni giorno vediamo quanto sia facile ridurre una vita a un semplice numero, a un oggetto da sfruttare, da usare, da scartare."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto rage
    Totò "È questo che dobbiamo cambiare: un sistema che mercifica tutto, che non rispetta la dignità degli animali, che li sfrutta fino all'ultimo respiro."
    Totò "Non possiamo più guardare da un'altra parte."
    Totò "Ogni animale che soffre, ogni essere abbandonato, ogni vita sacrificata, è un grido silenzioso che ci chiede di fare meglio, di lottare per un mondo in cui tutti, uomini e animali, possano vivere con rispetto."
    Totò "Ma soprattutto, non dobbiamo permettere che questa realtà ci scivoli addosso come se fosse normale."
    play sound "audio/sfx/toto 2.mp3" volume 0.8
    show toto normal
    Totò "Spero che, in ognuno di voi, qualcosa si sia acceso. Una piccola fiamma di cambiamento, di speranza, che ci faccia capire che possiamo fare la differenza."
    Totò "Voglio ringraziarvi tutti per aver ascoltato con cuore aperto fino a questo momento. È un onore per me condividere con voi questa parte della nostra realtà."
    play sound "audio/sfx/toto 1.mp3" volume 2.5
    show toto smile
    Totò "Mi auguro di rivedervi presto qui in fattoria, fino ad allora, vi auguro una giornata piena di riflessioni, di serenità e di azioni positive."
    Totò "Grazie ancora per essere stati con noi oggi e ricordate: ogni passo verso il cambiamento è un passo che vale la pena fare."
    Totò "Ci vediamo presto!"
    stop music fadeout 1.0
    $ totoflag = True
    jump scelta

label test:
    scene bg vigna with fade
    play music "audio/test.mp3" volume 0.7 fadein 1.0 loop
    show vito smile at right with dissolve
    Vito "Sara, vieni qui! I nostri visitatori hanno completato tutti i percorsi!"
    "Arrivo subito!"
    Vito "Io per ora vi saluto, ho altri ospiti da accogliere. A fra poco!"
    hide vito with dissolve
    show sara smile at left with dissolve
    Sara "Che bel lavoro, ragazzi! Congratulazioni per essere arrivati fino alla fine di questo evento."
    Sara "Spero che i percorsi siano stati costruttivi per voi e che abbiate imparato tante cose nuove su quello che davvero succede a tutti quei poveri animaletti sfruttati ingiustamente nel mondo."
    Sara "È importante che queste storie non rimangano solo parole, ma che ci aiutino a cambiare la nostra visione."
    show sara normal 
    Sara "Per questo c'è un test finale che vi aspetta. Non ve lo aspettavate, eh?"
    Sara "Beh, non preoccupatevi, non siamo a scuola e non si vince nulla."
    Sara "Servirà solo a farvi capire se avete davvero compreso ciò che avete ascoltato oggi dalle nostre guide e dalle storie dei nostri rifugiati."
    show sara smile 
    Sara "Quindi mettetevi comodi e preparatevi a rispondere a qualche domanda."
    Sara "Le domande sono divise in tre temi: prima il clima, poi l'alimentazione sostenibile e infine il benessere animale."
    show sara normal
    Sara "Siete pronti? Bene, iniziamo!"

    show sara smile
    Sara "Cosa accade al metano quando viene rilasciato nell'atmosfera dai bovini?"
    show sara normal
    menu:
        "Non accade nulla":
            $ countertest+=0
        "Resta nell'atmosfera e intrappola il calore":
            $ countertest+=1
        "Viene neutralizzato da altre sostanze":
            $ countertest+=0

    show sara smile
    Sara "Quanto contribuisce l'allevamento bovino alla produzione di gas serra a livello globale?"
    show sara normal
    menu:
        "10\%":
            $ countertest+=0
        "57\%":
            $ countertest+=1 
        "70\%":
            $ countertest+=0

    show sara smile
    Sara "Qual è il secondo principale fattore di deforestazione al mondo, subito dopo l'allevamento bovino?"
    show sara normal
    menu:
        "La coltivazione di palma da olio":
            $ countertest+=0
        "La produzione di soia":
            $ countertest+=1
        "L'estrazione di combustibili fossili":
            $ countertest+=0

    show sara smile
    Sara "Quale percentuale della soia prodotta globalmente viene utilizzata come mangime per gli animali?"
    show sara normal
    menu:
        "97\%":
            $ countertest+=1 
        "50\%":
            $ countertest+=0
        "6\%": 
            $ countertest+=0
    
    show sara smile
    Sara "Qual è una delle principali conseguenze della sovrapesca per i pesci?"
    show sara normal
    menu:
        "Gli stock ittici si ripristinano":
            $ countertest+=0
        "Non ci sono conseguenze":
            $ countertest+=0
        "Nessuna riproduzione della specie":
            $ countertest+=1

    show sara smile
    Sara "Qual è il destino dei rifiuti plastici che non vengono smaltiti correttamente?"
    show sara normal
    menu:
        "Finiscono nei mari e danneggiano gli animali marini":
            $ countertest+=1
        "Scompaiono nell'aria":
            $ countertest+=0
        "Vengono reciclati":
            $ countertest+=0

    show sara smile
    Sara "Perfetto, passiamo al prossimo tema!"
    Sara "Quale dei seguenti è un effetto ambientale legato all'industria lattiero-casearia?"
    show sara normal
    menu:
        "Consumo e inquinamento di acqua dolce":
            $ countertest+=1
        "Aumento della biodiversità":
            $ countertest+=0
        "Riduzione delle emissioni di gas serra":
            $ countertest+=0

    show sara smile
    Sara "Qual è uno dei rischi associati al consumo di prodotti animali trattati con antibiotici?"
    show sara normal
    menu:
        "Aumento della qualità del latte":
            $ countertest+=0
        "Resistenza agli antibiotici e rischi per la salute umana":
            $ countertest+=1
        "Riduzione del consumo di acqua":
            $ countertest+=0

    show sara smile
    Sara "Quali sono le principali malattie che l'alimentazione basata su carne può causare?"
    show sara normal
    menu:
        "Diabete, malattie cardiovascolari e cancro":
            $ countertest+=1
        "Obesità e influenza stagionale":
            $ countertest+=0
        "Allergie alimentari":
            $ countertest+=0

    show sara smile
    Sara "Quanta acqua è necessaria per produrre 1 kg di manzo?"
    show sara normal
    menu:
        "1.230 litri":
            $ countertest+=0
        "2.350 litri":
            $ countertest+=1
        "5.150 litri":
            $ countertest+=0

    show sara smile
    Sara "Cosa succede ai pulcini maschi nell'industria delle uova?"
    show sara normal
    menu:
        "Vengono allevati per diventare galli da riproduzione":
            $ countertest+=0
        "Vengono utilizzati per la produzione di carne":
            $ countertest+=0
        "Vengono uccisi perché considerati inutili":
            $ countertest+=1

    show sara smile
    Sara "Qual è una delle possibili conseguenze legate al consumo di uova?"
    show sara normal
    menu:
        "Contaminazione batterica, come la Salmonella":
            $ countertest+=1
        "Diminuzione del colesterelo nel sangue":
            $ countertest+=0
        "Il miglioramento della salute cardiovascolare":
            $ countertest+=0

    show sara smile
    Sara "Va bene, e ora passiamo al prossimo tema!"
    Sara "Cosa caratterizza la selezione genetica dei polli Broiler in Italia?"
    show sara normal
    menu:
        "Vengono selezionati per essere più mansueti":
            $ countertest+=0
        "Sono selezionati per massimizzare la produzione di carne":
            $ countertest+=1
        "Sono selezionati per non avere piume":
            $ countertest+=0

    show sara smile
    Sara "Che tipo di reato è l'abbandono di animali in Italia"
    show sara normal
    menu:
        "Sanzionato solo con una multa":
            $ countertest+=0
        "Un reato penale punibile con l'arresto o una multa":
            $ countertest+=1
        "Non è considerato un reato":
            $ countertest+=0

    show sara smile
    Sara "Che impatto ha il bracconaggio sulla biodiversità?"
    show sara normal
    menu:
        "Aiuta a mantenere l'equilibrio ecologico":
            $ countertest+=0
        "Non ha alcun impatto":
            $ countertest+=0
        "Riduce la biodiversità e altera gli ecosistemi":
            $ countertest+=1

    show sara smile
    Sara "Cosa dimostrano gli studi scientifici riguardo agli animali?"
    show sara normal
    menu:
        "Gli animali manifestano emozioni come gioia, tristezza ed empatia":
            $ countertest+=1
        "Gli animali non sono in grado di provare emozioni complesse":
            $ countertest+=0
        "Gli animali possono provare solo paura e stress":
            $ countertest+=0

    show sara smile
    Sara "Perché il trattamento degli animali nei circhi è criticato dagli attivisti?"
    show sara normal
    menu:
        "Perché gli animali non si esibiscono abbastanza spesso":
            $ countertest+=0
        "Perché gli animali sono costretti a eseguire comportamenti innaturali":
            $ countertest+=1
        "Perché gli animali vengono nutriti troppo frequentemente":
            $ countertest+=0

    show sara smile
    Sara "Qual è una delle principali cause di sofferenza negli allevamenti intensivi?"
    show sara normal
    menu:
        "La mancanza di cibo e acqua":
            $ countertest+=0
        "Il trattamento degli animali come macchine da produzione":
            $ countertest+=1
        "L'impossibilità di accesso a cure veterinarie":
            $ countertest+=0

    show sara smile
    Sara "Quale problema sanitario è spesso riscontrato nei macelli?"
    show sara normal
    menu:
        "Uso di anestesia obbligatoria per gli animali":
            $ countertest+=0
        "Carne contaminata immessa sul mercato":
            $ countertest+=1
        "Eccessiva igiene degli impianti":
            $ countertest+=0

    show sara smile
    Sara "E con questo abbiamo finito!"
    show sara normal
    Sara "siete curiosi di sapere com'è andata?"
    Sara "Il vostro punteggio finale è di..."
    Sara "[countertest]/19!"

    if(countertest==19):
        show sara smile
        play sound "audio/sfx/risultati.mp3" volume 1.5
        Sara "Avete fatto un lavoro fantastico!"
        Sara "Avete risposto correttamente a tutte le domande, segno che avete davvero prestato attenzione e compreso tutto quello che abbiamo condiviso con voi."
    elif(countertest>=10 and countertest<19):
        show sara normal
        Sara "Ottimo lavoro, avete dimostrato di aver compreso molte delle informazioni che vi abbiamo condiviso!"
        Sara "Anche se c'è ancora un po' da imparare, sono sicura che questi concetti vi aiuteranno a riflettere su come possiamo tutti fare la differenza."
    else:
        show sara normal
        Sara "Sembra che alcune cose siano ancora poco chiare, ma non preoccupatevi!"
        Sara "L'importante è che abbiate avuto modo di riflettere su questi temi e spero che questo percorso vi abbia aiutato a vedere il mondo da una prospettiva diversa."
    
    show sara smile
    Sara "Prima di salutarvi, però, ci tengo a farvi 4 ultime domande."
    Sara "Queste sono quelle che servono davvero a capire se avete colto il messaggio che volevamo trasmettere con tutto l'evento di oggi."
    Sara "Quale tipo di dieta potrebbe ridurre le emissioni individuali di gas serra?"
    show sara normal
    menu:
        "Una dieta ricca di carne rossa":
            $ countertest+=0
        "Una dieta a base vegetale":
            $ countertest+=0
        "Una dieta che include solo pesce":
            $ countertest+=0
            
    show sara smile
    Sara "Cosa può fare una persona per ridurre i rischi legati al consumo di carne, uova e latte?"
    show sara normal
    menu:
        "Mangiare più carne e uova provenienti da allevamenti intensivi":
            $ countertest+=0
        "Adottare una dieta plant-based e ridurre il consumo di derivati animali":
            $ countertest+=0
        "Mangiare solo frutta":
            $ countertest+=0

    show sara smile
    Sara "Quale delle seguenti affermazioni riguarda correttamente il benessere animale nella dieta plant-based?"
    show sara normal
    menu:
        "La dieta plant-based contribuisce agli stessi livelli di sofferenza animale delle diete tradizionali":
            $ countertest+=0
        "La dieta plant-based promuove cibi che rispettano gli animali":
            $ countertest+=0
        "La dieta plant-based ignora il benessere degli animali":
            $ countertest+=0

    show sara smile
    Sara "Quindi per concludere, quale alimentazione aiuta di più l'ambiente, rispetta il benessere animale ed è il più sostenibile possibile?"
    show sara normal
    menu:
        "Una dieta plant-based":
            $ countertest+=0
        "Una dieta plant-based":
            $ countertest+=0
        "Una dieta plant-based":
            $ countertest+=0

    show sara smile
    Sara "Sono davvero soddisfatta di vedere che avete colto il significato profondo dietro tutto l'evento di oggi."
    Sara "Si, l'ultima domanda non vi ha lasciato molta scelta, ma so che avreste dato la stessa risposta."
    show sara normal
    Sara "Vedere che oltre 1,7 milioni di italiani hanno scelto un'alimentazione plant-based è un segno di speranza."
    Sara "È un cambiamento enorme che ci dimostra che siamo pronti ad abbracciare stili di vita più sostenibili."
    show sara rage
    Sara "Gli allevamenti intensivi hanno un impatto devastante sul nostro pianeta, non solo sull'ambiente, ma anche sulla povertà alimentare."
    show sara normal
    Sara "La nostra scelta alimentare può fare la differenza."
    Sara "La scienza ci dice che una dieta plant-based può fermare il cambiamento climatico. Ridurre il consumo di carne e latticini è una delle soluzioni più potenti che abbiamo a disposizione."
    Sara "Eliminare gli alimenti di origine animale potrebbe ridurre le emissioni di CO2 di 8 miliardi di tonnellate ogni anno."
    show sara smile
    Sara "Questo è un obiettivo ambizioso, ma alla portata di tutti noi."
    Sara "Ognuno di noi ha la responsabilità di riflettere sull'impatto delle proprie scelte alimentari."
    Sara "Siamo tutti parte di un cambiamento che può fare bene a noi e al nostro pianeta."
    show sara normal
    Sara "Ci stiamo preparando a vivere su un pianeta con 10 miliardi di persone."
    Sara "È essenziale che cambiamenti profondi avvengano ora, e una dieta plant-based è parte di questo cambiamento."
    show sara smile
    Sara "Ma il messaggio più importante di oggi è che possiamo vivere una vita che non causi sofferenza inutile a nessun altro essere vivente."
    Sara "E questo, ragazzi, è il messaggio più importante che dovete portare con voi a casa oggi. Non dimenticatelo mai."
    show sara normal
    Sara "Ora però, è arrivato il momento di salutarvi. La giornata sta per concludersi, ma prima meglio andare da Vito!"
    stop music fadeout 1.0
    jump salutifinali

label salutifinali:
    scene bg inizio viale with fade
    play music "audio/salutifinali.mp3" volume 0.7 fadein 1.0 loop
    show sara normal at left with dissolve
    show vito normal at right with dissolve
    Vito "Ciao Sara! Allora, com'è andato il test? Hanno risposto bene?"
    Sara "Sì, sono stati bravi! Sicuramente hanno imparato tante cose nuove e sono sicura che porteranno con sé l'esperienza di oggi."
    show vito smile
    Vito "Congratulazioni a tutti voi per essere arrivati fino alla fine di questo evento! Spero di rivedervi al più presto, magari anche di persona qui al santuario."
    Vito "Ci farebbe piacere accogliervi davvero!"
    show sara smile
    Sara "Esatto, Vito! Qui siamo sempre felici di avere nuovi ospiti, soprattutto quando, come voi, amano gli animali e vogliono davvero fare la differenza."
    show vito normal
    show sara normal
    Sara "Prima di lasciarvi, c'è una piccola cosa che vorremmo chiedervi."
    Sara "Come sapete, questo rifugio è un luogo che dipende molto dall'aiuto di persone come voi."
    show vito smile
    Vito "Esatto, ogni donazione che riceviamo viene interamente destinata alla cura dei nostri amici a quattro zampe."
    Vito "Ogni piccolo contributo fa davvero la differenza nella vita degli animali che abbiamo salvato."
    show sara smile
    Sara "Potete fare una donazione anche online, comodamente da casa."
    Sara "Ogni donazione aiuta a garantire loro cibo, cure veterinarie e tutto ciò di cui hanno bisogno per vivere felici."
    Vito "Siamo enormemente grati per qualsiasi supporto, grande o piccolo."
    Vito "Ogni gesto conta, e con il vostro aiuto possiamo continuare a dare una seconda possibilità a tanti altri animali che hanno bisogno di noi."
    show sara normal
    Sara "E, se non potete donare, ricordate che potete sempre aiutarci anche condividendo la nostra missione sui social."
    Sara "Ogni piccola azione è un passo in più verso un mondo migliore per gli animali."
    show vito normal
    Vito "Sì, grazie di cuore! E ricordate, ogni volta che scegliamo di fare del bene, lo facciamo non solo per noi, ma anche per il nostro pianeta e tutti gli esseri viventi che lo abitano."
    show sara smile
    Sara "La vera forza del cambiamento è nelle nostre mani. Un passo alla volta, possiamo davvero cambiare il mondo."
    Sara "Grazie ancora per aver partecipato e spero che vi sentiate ispirati ad agire, ogni giorno!"
    show vito smile
    Vito "E non dimenticate mai che anche voi, con le vostre scelte, potete fare la differenza."
    Vito "Grazie per aver trascorso questa giornata con noi. Speriamo di rivedervi presto, e magari, un giorno, a fare parte di questa grande famiglia!"
    Duo "Un abbraccio a tutti! E ricordate: più siamo, più forte è la nostra voce per difendere gli animali e il nostro pianeta. Arrivederci!"
    scene bg the end with fade
    stop music fadeout 3.0
    pause 5
    jump end
    
label end:
    scene bg neutral with fade
    show text "Grazie per aver finito questa avventura!" with dissolve
    pause 3
    hide text with dissolve
    show text "Se hai voglia di fare una donazione per sostenere la fattoria potrai trovare tutti i metodi per farlo nella sezione 'Chi siamo' e poi 'Donazioni e Social'." with dissolve
    pause 5
    hide text with dissolve
    show text "Grazie in anticipo per il tuo supporto!" with dissolve
    pause 3
    hide text with dissolve
    show text "Se vuoi leggere le ricerche su cui sono stati basati tutti i dialoghi nel gioco clicca sulla sezione 'Extra' nel menù." with dissolve
    pause 4
    hide text with dissolve
    show text "Se invece vuoi vedere altre foto degli animaletti del rifugio potrai farlo sempre dalla sezione 'Chi Siamo' poi 'Galleria'." with dissolve
    pause 4
    hide text with dissolve
    show text "Ti aspettiamo in Fattoria! Alla prossima!" with dissolve
    pause 3
    hide text with dissolve
    pause 1
    return