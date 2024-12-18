"""MDList:
    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                              תוינוציח תוילאוזיו תוקידב [/font]"

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                               יוטיח תילטמ תועצמאב תכרעמ הקנו הנגה תופפכ הטע [/font]"
        secondary_text: "[font=Arial.ttf]                                                           תכרעמה זראמיקלח ללכ תא הקנ[/font]"
        on_press:
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)
        TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                              םיקדוהמו םירבוחמ םימלוב אדוו[/font]"
        secondary_text: "[font=Arial.ttf]                                                             סחדמ יגרב 8 רותיאל סנפב רזעה[/font]"
        on_press:
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                        דעיה תרוצתל םאתהב תכרעמ עקת אדוו   [/font]"
        secondary_text: "[font=Arial.ttf]                                                                     ב''הרא /הפוריא /לארשי[/font]"
        on_press:
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                           הקדל םירטיל 5 לש הקיפס לע לעפהו חתמ רוקמל תכרעמ רבח [/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                              זראמה ייגרב ללכתואצמיה אדוו[/font]"
        secondary_text: "[font=Arial.ttf]                                                                 תכרעמה בגב םיגרב 9 אדוו[/font]"
        on_press:
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                          הפוסכ רוציי תקבדמ תואצמיה אדוו[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                        POWER SUPPLY םיחתמ תקבדמ אדוו[/font]"
        secondary_text: "[font=Arial.ttf]                                                                  תכרעמה בגב םיגרב 9 אדוו[/font]"
        on_press:
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                    דוקרב תבלושמ ןאבצ ירודיס רפסמ תקבמד אדוו[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                   סחדמ ןנסמו ילאירטקב ןנסמ ,סג ןנסמ רוביח אדוו [/font]"
        secondary_text: "[font=Arial.ttf]                                                                  רישכמה בגב םיננסמה אתב םיננסמה םוקימ[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                    תוריבשו םיפופיכ אלל םיננסמ תרנצ אדוו[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                    יוארכ םקוממו רבוחמ תרכעמ לוקמר אדוו[/font]"
        secondary_text: "[font=Arial.ttf]                                                                  האישנה תידיב םוקימ[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                      יוארכ ספדומ ןאבצ וגול [/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                    NO SMOKE תקבדמ תואצמיה אדוו[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                    ןיקת םיביכר בותיכ אדוו[/font]"
        secondary_text: "[font=Arial.ttf]                                                                  LCD הלעפה גתמ , CB , הקיפס דמ[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                    תיברימ הקיפס תרהזא תקבדמ קבדה[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                    םיננסמ תפלחה תקבדמ קבדה[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]     ןוקית תומיא אלמל שרדנ אל שרדנ אל ןוקית עצוב אלו הדימב :(לוחכ) ינדי ד''בצ םע הקידב - תילועפת תקידב[/font]"

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                    LCDה ךסמב יוארכ תגצומ תכרעמה תגוצת יכ אדוו[/font]"
        secondary_text: "[font=Arial.ttf]                                                                  תכרעמ תועש הנומ תגוצת אדוו[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                             תוקלוד יוויח תורונ אדוו[/font]"
        secondary_text: "[font=Arial.ttf]                             (תוקלוד)POWER, NORMAL OXYGEN / (היובכ) SERVICE REQUIRED[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]          הקדל םירטיל 4.5-5.5 תכרעמ תקיפס אדוו ינדי דמ רבח.םירטיל 5 לש תכרעמ תקיפסל המירז דמ ןווכ[/font]"
        secondary_text: "[font=Arial.ttf]                                         תרחבנה הקיפסה תא גציימ תירודכה זכרמ[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                  94%+-2% (94%-96%) ינדיה דמב ןצמחתאירק אדוו  [/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                    (7.7-9.3 psi) 8.5PSI+-0.8 : אצומ ץחל אדוו ינדי דמ אצומ רוגס[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                    OXYGEN FLOW LOW הכומנ הקיפס תערתה אדוו ינדי דמ אצומ רוגס[/font]"
        secondary_text: "[font=Arial.ttf]                                                                  LCDה ךסמ לע גצומ הערתהה םשו תבהבהמ SERVICE תרונ אדוו[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                    ספאל תלפונ הקיפס תירודכ אדוו ינדי דמ אצומ רוגס[/font]"
        secondary_text: "[font=Arial.ttf]                                                                  תוליזנ תקידב[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                   (5.5-9.5LPM) 7.5 +-2LPM תיברמ הקיפס אדוו םומיסקמל הקיפס דמ ררוב ןווכ[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                    HIGH OXYGEN FLOW הקיפס תערתה אדוו םומיסקמל הקיפס דמ ררוב ןווכ[/font]"
        secondary_text: "[font=Arial.ttf]                                                                  LCDה ךסמ לע גצומ הארתהה םשו תבהבהמ SERVICE תירונ אדוו[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                    OXYGEN LOW ךומנ ןצמח תערתה אדוו םירטיל 4ל תכרעמ תקיפס דרוה 80%ל תחתמ לא ןצמחה תדירי םע[/font]"
        secondary_text: "[font=Arial.ttf]                                                                  LCDה ךסמ לע גצומ הארתהה םשו תבהבהמ SERVICE תירונ אדוו[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    TwoLineIconListItem:
        text: "[font=Arial.ttf]                                                    חתמצתלקת תוערתה אדוו תדבוע הדועב חתמ רוקממ תכרעמ קתנ[/font]"
        secondary_text: "[font=Arial.ttf]                                                                  הנתשמ רדתב ילוק יוויח עמשנו תקלוד SERVICE תירונ אדוו[/font]"
        MDCheckbox:
        pos_hint: {"center_x": 0.1, "center_y": 0.5}
        active: False
        on_active: app.on_checkbox(*args)

    OneLineIconListItem:
        text: "[font=Arial.ttf]                          (תיללכ הקידב תרוצתב) בשחוממ ד''בצ םע תכרעמ תציר - תילנויצקנופ הקידב[/font]"

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                                      LPM ד''בצב תכרעמ תקיפס[/font]"
        MDTextField:
        text: ""
        font_name: 'Arial'
        pos_hint: {"center_x": .2, "center_y": 0.3}
        size_hint_x: None
        width: "300dp"
        Widget:

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                                      %אצומב ןצמח תמר[/font]"
        MDTextField:
        text: ""
        font_name: 'Arial'
        pos_hint: {"center_x": .2, "center_y": 0.3}
        size_hint_x: None
        width: "300dp"
        Widget:

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                                     (4.5-5.5)םירטיל 5ל הקיפס ןווכלעפה , חתמ רוקמ תכרעמ רבח[/font]"
        MDTextField:
        text: ""
        font_name: 'Arial'
        pos_hint: {"center_x": .2, "center_y": 0.3}
        size_hint_x: None
        width: "300dp"
        Widget:

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                                      LPM הקיפס תויתדונת[/font]"
        MDTextField:
        text: ""
        font_name: 'Arial'
        pos_hint: {"center_x": .2, "center_y": 0.3}
        size_hint_x: None
        width: "300dp"
        Widget:

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                                      ףרגב ןצמח זוחא תויתדונת[/font]"
        MDTextField:
        text: ""
        font_name: 'Arial'
        pos_hint: {"center_x": .2, "center_y": 0.3}
        size_hint_x: None
        width: "300dp"
        Widget:

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                                      PSI אצומ ץחל[/font]"
        MDTextField:
        text: ""
        font_name: 'Arial'
        pos_hint: {"center_x": .2, "center_y": 0.3}
        size_hint_x: None
        width: "300dp"
        Widget:

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                                      ספאל תלפונ הקיפס תירודכ אדוו ינדי דמ אצומ רוגס[/font]"
        MDTextField:
        text: ""
        font_name: 'Arial'
        pos_hint: {"center_x": .2, "center_y": 0.3}
        size_hint_x: None
        width: "300dp"
        Widget:

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                                      הרירק ללוחמ אצומ תרוטרפמט אדוו[/font]"
        MDTextField:
        text: ""
        font_name: 'Arial'
        pos_hint: {"center_x": .2, "center_y": 0.3}
        size_hint_x: None
        width: "300dp"
        Widget:

    OneLineIconListItem:
        text: "[font=Arial.ttf]                                                                     הזירא תוקידב[/font]"


    """
