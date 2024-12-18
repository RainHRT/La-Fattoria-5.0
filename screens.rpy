﻿## Inizializzazione

init offset = -1

## Stili

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

## Schermate interne al gioco

## Schermata dei dialoghi
screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Se c'è una side image, mostrala sopra al testo.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Rendi la casella dei nomi disponibile per lo styling attraverso l'oggetto Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize 300

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 90
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos 25
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos 90

    adjust_spacing False

## Schermata di inserimento 

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

## Schermata di scelta 

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 850
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")

## Schermata del Menu Rapido

screen quick_menu():

    ## Assicura che compaia in cima ad altri screen.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Indietro") action Rollback()
            textbutton _("Cronologia") action ShowMenu('history')
            textbutton _("Salta") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Salva") action ShowMenu('save')
            #textbutton _("Salva R.") action QuickSave()
            #textbutton _("Carica R.") action QuickLoad()
            textbutton _("Opzioni") action ShowMenu('preferences')

## Questo codice assicura che il quick menu sia mostrato nel gioco, a meno che
## il giocatore non nasconda esplicitamente l'interfaccia.

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")

## Main Menu e Game Menu
## Schermata di navigazione

screen navigation():

    vbox:
        style_prefix "navigation"

        if renpy.get_screen("main_menu"):
            xalign 0.5
            yalign 0.93
        else:
            xpos 150
            yalign 0.5


        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Inizia") action Start()

        else:

            textbutton _("Cronologia") action ShowMenu("history")

            textbutton _("Salva") action ShowMenu("save")

        textbutton _("Carica") action ShowMenu("load")

        textbutton _("Opzioni") action ShowMenu("preferences")

        textbutton _("Extra") action ShowMenu("extra")

        textbutton _("Chi Siamo") action ShowMenu("help")

        textbutton _("Crediti") action ShowMenu("about")

        if _in_replay:

            textbutton _("Fine Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Esci") action MainMenu()

        if renpy.variant("pc"):

            ## Il pulsante esci è vietato su iOS e inutile su Android e sul Web.
            textbutton _("Chiudi") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    xalign 0.5

## Schermata del menu principale

screen main_menu():

    ## Questo assicura che ogni altro menu sia rimpiazzato.
    tag menu

    add gui.main_menu_background

    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

    #        text "[config.name!t]":
    #            style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## Schermata del Menu di Gioco

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Riserva spazio per la sezione di navigazione.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Indietro"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos 150
    yalign 1.0
    yoffset -45

## Schermata delle informazioni

screen about():

    tag menu
    
    use game_menu(_("Crediti"), scroll="viewport"):

        style_prefix "about"

        vbox:

            ## gui.credits viene di solito impostato in options.rpy.
            if gui.credits:
                text "[gui.credits!t]"

        text _("Creato con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") 

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Schermate di Caricamento e Salvataggio

screen save():

    tag menu

    use file_slots(_("Salva"))


screen load():

    tag menu

    use file_slots(_("Carica"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Pagina {}"), auto=_("Salvataggi automatici"), quick=_("Salvataggi rapidi"))

    use game_menu(title):

        fixed:

            ## Questo garantisce che l'input riceva un'eventuale pressione di Invio prima che accada ad altri pulsanti.
            order_reverse True

            ## Il nome della pagina, che può essere cambiato cliccando su un pulsante.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La griglia di slot.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Spazio Vuoto")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Pulsanti per accedere ad altre pagine.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    #textbutton _("<") action FilePagePrevious()
                    #key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    #if config.has_quicksave:
                    #    textbutton _("{#quick_page}R") action FilePage("quick")

                    ## range(1, 10) fornisce i numeri da 1 a 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    #textbutton _(">") action FilePageNext()
                    #key "save_page_next" action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")

## Schermata delle opzioni
screen preferences():

    tag menu

    use game_menu(_("Opzioni"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Schermo")
                        textbutton _("Finestra") action Preference("display", "window")
                        textbutton _("Schermo intero") action Preference("display", "fullscreen")

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "check"
                        label _("Salta")
                        textbutton _("Testo non letto") action Preference("skip", "toggle")
                        textbutton _("Dopo le Scelte") action Preference("after choices", "toggle")
                        textbutton _("Transizioni") action InvertSelected(Preference("transitions", "toggle"))

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    
                    label _("Velocità del Testo")

                    bar value Preference("text speed")

                    label _("Ritmo di Avanzamento Automatico")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Volume della Musica")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volume dei Suoni")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Prova") action Play("sound", config.sample_sound)

                    # if config.has_voice:
                    #     label _("Volume della Voce")

                    #     hbox:
                    #         bar value Preference("voice volume")

                    #         if config.sample_voice:
                    #             textbutton _("Prova") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Silenzia Tutto"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675

## Schermata della cronologia

screen history():

    tag menu

    ## Evita di predirre questo screen, perché può essere molto grande.
    predict False

    use game_menu(_("Cronologia"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Questo dispone le cose appropriatamente, se history_height è None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Prende il colore dal nome del personaggio, se impostato.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Nessun dialogo da mostrare.")


## Determina quali tag possono essere visualizzati nella schermata della cronologia.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

## Schermata extra

screen extra():

    tag menu

    default device = "clima"

    use game_menu(_("Ricerche"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23
            xalign 0.5

            hbox:
                xalign 0.5
                
                textbutton _("Clima") action SetScreenVariable("device", "clima")
                text _("  |  ")
                textbutton _("Alimentazione") action SetScreenVariable("device", "alimentazione")
                text _("  |  ")
                textbutton _("Benessere") action SetScreenVariable("device", "benessere")

            if device == "clima":
        
                default sub_device_a = "metano"

                vbox:
                    spacing 23
                    xalign 0.5

                    hbox:
                        xalign 0.5
                
                        textbutton _("Mucche & Metano") action SetScreenVariable("sub_device_a", "metano")
                        text _("  |  ")
                        textbutton _("Mangimi & Deforestazione") action SetScreenVariable("sub_device_a", "mangimi")
                        text _("  |  ")
                        textbutton _("Pesca") action SetScreenVariable("sub_device_a", "pesca")

                if sub_device_a == "metano":
                    use metano_ricerche
                elif sub_device_a == "mangimi":
                    use mangimi_ricerche
                elif sub_device_a == "pesca":
                    use pesca_ricerche
        
            elif device == "alimentazione":

                default sub_device_b = "tradizioni"

                vbox:
                    spacing 23
                    xalign 0.5

                    hbox:
                        xalign 0.5
                
                        textbutton _("Tradizioni") action SetScreenVariable("sub_device_b", "tradizioni")
                        text _("  |  ")
                        textbutton _("Latte") action SetScreenVariable("sub_device_b", "latte")
                        text _("  |  ")
                        textbutton _("Carne") action SetScreenVariable("sub_device_b", "carne")
                        text _("  |  ")
                        textbutton _("Uova") action SetScreenVariable("sub_device_b", "uova")
                        text _("  |  ")
                        textbutton _("Plant-Based") action SetScreenVariable("sub_device_b", "plantbased")

                if sub_device_b == "tradizioni":
                    use tradizioni_ricerche
                elif sub_device_b == "latte":
                    use latte_ricerche
                elif sub_device_b == "carne":
                    use carne_ricerche
                elif sub_device_b == "uova":
                    use uova_ricerche
                elif sub_device_b == "plantbased":
                    use plantbased_ricerche

            elif device == "benessere":

                default sub_device_c = "speriment"

                vbox:
                    spacing 23
                    xalign 0.5

                    hbox:
                        xalign 0.5
                
                        textbutton _("Esperimenti") action SetScreenVariable("sub_device_c", "speriment")
                        text _("  |  ")
                        textbutton _("Abbandono\n     &\n  Caccia") action SetScreenVariable("sub_device_c", "caccia")
                        text _("  |  ")
                        textbutton _("Mercificazione") action SetScreenVariable("sub_device_c", "merci")
                        text _("  |  ")
                        textbutton _("Allevamenti") action SetScreenVariable("sub_device_c", "allevamenti")

                if sub_device_c == "speriment":
                    use speriment_ricerche
                elif sub_device_c == "caccia":
                    use caccia_ricerche
                elif sub_device_c == "merci":
                    use merci_ricerche
                elif sub_device_c == "allevamenti":
                    use allevamenti_ricerche

## le gui."" vengono impostate in ricerche.rpy

screen metano_ricerche():
    vbox:
        text "[gui.metano!t]\n"

screen mangimi_ricerche():
    vbox:
        text "[gui.mangimi!t]\n"

screen pesca_ricerche():
    vbox:
        text "[gui.pesca!t]\n"

screen tradizioni_ricerche():
    vbox:
        text "[gui.tradizioni!t]\n"

screen latte_ricerche():
    vbox:
        text "[gui.latte!t]\n"

screen carne_ricerche():
    vbox:
        text "[gui.carne!t]\n"

screen uova_ricerche():
    vbox:
        text "[gui.uova!t]\n"

screen plantbased_ricerche():
    vbox:
        text "[gui.plantbased!t]\n"

screen speriment_ricerche():
    vbox:
        text "[gui.speriment!t]\n"

screen caccia_ricerche():
    vbox:
        text "[gui.caccia!t]\n"

screen merci_ricerche():
    vbox:
        text "[gui.merci!t]\n"

screen allevamenti_ricerche():
    vbox:
        text "[gui.allevamenti!t]\n"

## Schermata di aiuto

screen help():

    tag menu

    default device = "info"

    use game_menu(_("Chi Siamo"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                xalign 0.4
                
                textbutton _("Informazioni") action SetScreenVariable("device", "info")
                text _("  |  ")
                textbutton _("Donazioni & Social") action SetScreenVariable("device", "dona")
                text _("  |  ")
                textbutton _("Galleria") action SetScreenVariable("device", "album")

            if device == "info":
                use info_help
            elif device == "dona":
                use dona_help
            elif device == "album":
                use album

screen info_help():
        vbox:
            ## gui.about viene impostato in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

screen dona_help():

        vbox:
            ## gui.dona viene impostato in options.rpy.
            if gui.dona:
                text "[gui.dona!t]\n"

        vbox:
            spacing 23
            xalign 0.4

            hbox:
                
                imagebutton:
                    idle "icone/ig.png"
                    hover "icone/ighover.png"
                    action OpenURL("https://www.instagram.com/la_fattoria_di_nonno_peppino/")

                text _("    ")
                
                imagebutton:
                    idle "icone/fb.png"
                    hover "icone/fbhover.png"
                    action OpenURL("https://www.facebook.com/lafattoriadinonnopeppino")

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

## Schermate addizionali

## Schermata di conferma

screen confirm(message, yes_action, no_action):

    ## Garantisce che gli altri screen non ricevano input fino a che questo screen è attivo.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Sì") action yes_action
                textbutton _("No") action no_action

    ## Click destro ed ESC rispondono "no".
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")

## Schermata dell'indicatore di salto

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Salto")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

## Questa transform è usata per far lampeggiare le freccie una dopo l'altra.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    font "DejaVuSans.ttf"

## Schermata di notifica

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

## Schermata NVL

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Mostra il dialogo in una vpgrid o in una vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Mostra il menu, se fornito. Il menu può apparire distorto se
        ## config.narrator_menu è impostato a True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## Questo controlla il numero massimo di elementi NVL che possono venire mostrati all'unisono.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")

## Schermata a bolle

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}

# Varianti Mobili

style pref_vbox:
    variant "medium"
    xsize 675

## Dato che un mouse non è presente, rimpiazziamo il quick menu con una versione che usa meno pulsanti e più grandi, più facili da toccare.

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

            hbox:
                style_prefix "quick"
                yoffset -25
                xalign 0.5
                yalign 1.0

                textbutton _("Indietro") action Rollback()
                textbutton _("Salta") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Salva") action ShowMenu('save')
                textbutton _("Menu") action ShowMenu()

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900