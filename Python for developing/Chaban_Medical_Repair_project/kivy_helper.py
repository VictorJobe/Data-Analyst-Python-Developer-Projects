kivy_helper = """

ScreenManager:
    HomeScreen:
        id: screen
        name: 'HomeScreen'
        Image:
            id: avatar
            size_hint: (.7,.7)
            source: "image.png"
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}  
        BoxLayout:
            orientation: "vertical"
            MDToolbar:
                id: toolbar
                name: 'toolbar'
                title:'OXYTEC 5S'
                elevation: 10
            Widget:    
            Ar_text:
                id: worker
                name: "worker"
                text: 'קדוב םש'
                font_name: "Arial"
                size_hint: 1 , None
                height: "60 dp"
                base_direction:"rtl"
                size_hint_x: 0.4
                pos_hint: {'center_x': 0.5}
                

            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:

                        OneLineAvatarListItem:
                            text: "[size=30] [font=Arial.ttf]                                                                                             ןוקית[/font] [/size]"
                            on_press: root.current = 'ClalitScreen'
                            font_size: "18 dp"
                            ImageLeftWidget:
                                source: "clalitlogo.jpg" 
                                
                        OneLineIconListItem:
                            text: "[size=30] [font=Arial.ttf]                                                                                              רוצי[/font] [/size]"
                            font_name:'Arial'
                            on_press:root.current = 'ItzurScreen'


                        OneLineIconListItem:
                            text: "[size=30] [font=Arial.ttf]                                                                                       טקרמ ידמ[/font] [/size]"
                            font_name:'Arial'
                            on_press:root.current = 'MedimarketScreen'


                        OneLineIconListItem:
                            text: "[size=30] [font=Arial.ttf]                                                                                       דיקלמ שד[/font] [/size]"
                            font_name:'Arial'
                            on_press:root.current = 'DashmedikScreen'
                    
                        
            

                        

    ClalitScreen:
        id: ClalitScreen
        name: "ClalitScreen"
        BoxLayout:
            orientation: "vertical"
            MDToolbar:
                id: toolbar
                name: 'toolbar'
                title:'OXYTEC 5S REPAIR'
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.get_back()]] 
            MDTabs:
                Tab:
                    id: tab
                    text:"[font=Arial.ttf] תויפוס תוקידב ח''וד[/font]"
                    BoxLayout:
                        orientation:"vertical"
                        ScrollView:
                            BoxLayout:
                                orientation:"vertical"
                                size_hint: 1 , None
                                height: 4000
                                
                                GridLayout:
                                    cols: 3
                                    Button:
                                        text: 'מק"ט מערכת'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                    Button:
                                        text: 'הבכרהה םש'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                    Button:
                                        text: 'טקיורפה םש'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint:{"top": 1}
                                        color: 0, 0, 0, 1
                                                 
                                    Button:
                                        text: 'PK444A05M'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        color: 0, 0, 0, 1
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                            
                                    Button:
                                        text: 'Oxygen Concentrator 5L'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        color: 0, 0, 0, 1
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                
                                    Button:
                                        text: 'OXYTEC 5S'
                                        size_hint: 1 , None
                                        height: "40 dp"                                   
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    Button:
                                        text: "סחדמ ירודיס 'סמ "
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                        
                                    Button:
                                        text: 'ןאבצ דוקרב'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                        
                                    Button:
                                        text: "רישכמל ירודיס 'סמ"
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                        
                                    BoxLayout:
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "140 dp"
                                        BoxLayout:
                                            orientation: "vertical"
                                            height: "140 dp"
                                            size_hint: 1 , None
                                            pos_hint: {"top": 1}
                                            font_name:'Arial'
                                        
                                            Ar_text:
                                                name: "menuTable.cell(3, 0)"
                                                text: 'SN:'
                                                size_hint: 1 , None
                                                height: "60 dp"
                                                max_text_length: 8
                                                size_hint_x: 0.8
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21 )
                                                  
                                            Button:
                                                text: 'סיטרכ ירודיס רפסמ'
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                font_name:'Arial'
                                                color: 0, 0, 0, 1
                                                
                                            Ar_text:
                                                name: "menuTable.cell(6, 0)"
                                                text: 'SN:'
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                font_name:'Arial'
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21 )
                                                
                                    Ar_text:
                                        id: menuTable.cell(4, 1)
                                        name: "menuTable.cell(4, 1)"
                                        text: '                                Barcode'
                                        size_hint: 1 , None
                                        height: "140 dp"                     
                                        font_name:'Arial'
                                        pos_hint: {"center_x": 0.5, "center_y" : 0.5}
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        Widget:
                                    
                                    BoxLayout:
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        height: "140 dp"
                                        pos_hint: {"top": 1}
                                        BoxLayout:
                                            orientation:"vertical"
                                            Ar_text:
                                                name: "menuTable.cell(3, 2)"
                                                text: 'SN:'
                                                size_hint: 1 , None
                                                height: "60dp"                                             
                                                font_name:'Arial'
                                                pos_hint: {"top": 1}    
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21 )
                                                
                                            Button:
                                                text: "ןוניס ילכמ ירודיס 'סמ"
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                font_name:'Arial'
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                
                                            Ar_text:
                                                name: "menuTable.cell(6, 2)"
                                                text: "SN:"
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                font_name:'Arial'
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21 )
                                                
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40dp"
                                        background_color: (1.0, 0.0, 0.0, 1.0)
                                        font_name:'Arial'
                                        background_color: (237, 242, 239, 1.0)
                                                                              
                                    Button:
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (1.0, 0.0, 0.0, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (237, 242, 239, 1.0)
                                        
                                    Button:
                                        text: "תוינוציח תוילאוזיו תוקידב"
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תורעה"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout:
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        BoxLayout:
                                            Button:
                                                text:"ןוקית תומיא"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"הקידב"  
                                                font_name:"Arial" 
                                                size_hint: 1 , None
                                                height: "40 dp"     
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                        BoxLayout:
                                            orientation:"horizontal"                                          
                                            size_hint: 1 , None
                                            pos_hint: {"top": 1}
                                            height: "30 dp"
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                color: 0, 0, 0, 1
                                                pos_hint: {"top": 1}
                                                  
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                    BoxLayout: 
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            text:"הקידב"  
                                            font_name:"Arial" 
                                            size_hint: 1 , None
                                            height: "70 dp"     
                                            pos_hint: {"top": 1}
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                                
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תכרעמה זראמ יקלח ללכ תא הקנ"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            icon:''
                                            id: Table2.cell(2, 2)
                                            pos_hint: {"top": .98}
                                            text: "Table2.cell(2, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                         
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "תועצמאב תכרעמ הקנו הנגה תופפכ הטע \\n יוטיח תילטמ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "1"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "סחדמ יגרב 8 רותיאל סנפב רזעה"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            icon:''
                                            id: table_one_1
                                            pos_hint: {"top": .98}
                                            text: "Table2.cell(3, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                         
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "םיקדוהמו םירבוחמ םימלוב אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "2"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "ב''הרא / הפוריא / לארשי"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )                                        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            icon:''
                                            
                                            pos_hint: {"top": .98}
                                            text: "Table2.cell(4, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                         
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "דעיה תרוצתל םאתהב תכרעמ עקת אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "3"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            icon:''
                                            pos_hint: {"top": .98}
                                            text: "Table2.cell(5, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                         
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                            
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "הקיפס לע לעפהו חתמ רוקמל תכרעמ רבח\\n הקדל םירטיל 5 לש"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "4"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תכרעמה בגב םיגרב 9 אדוו"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            icon: ""
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(6, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "זראמה ייגרב ללכ תואצמיה אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "5"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            icon: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            text: "Table2.cell(7, 2)"
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "הפוסכ רוציי תקבדמ תואצמיה אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "6"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "110V/230V תרוצתל םאתהב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            icon:""
                                            text: "Table2.cell(8, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )     
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "POWER SUPPLY םיחתמ תקבדמ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "7"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(9, 2)"
                                            icon:""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "ןאבצ ירודיס רפסמ תקבדמ אדוו\\n דוקרב תבלושמ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "8"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )     
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "רישכמה בגב םיננסמה אתב םיננסמה םוקימ"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(10, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "ןנסמו ילאירטקב ןנסמ ,סג ןנסמ רוביח אדוו\\n סחדמ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "9"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(11, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "תוריבשו םיפופכ אלל םיננסמ תרנצ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "10"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "האישנה תידיב םוקימ"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(12, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                            
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "יוארכ םקוממו רבוחמ תכרעמ לוקמר אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "11"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                            
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(13, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "יוארכ ספדומ ןאבצ וגול"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "12"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                            
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                            
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(14, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "NO SMOKE תקבדמ תואצמיה אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "13"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                            
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(15, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""                                           
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "ןיקת םיביכר בותיכ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "14"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(16, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "תיברימ הקיפס תרהזא תקבדמ קבדה"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "15"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(17, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "םיננסמ תפלחה תקבדמ קבדה"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "16"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40dp"
                                        background_color: (1.0, 0.0, 0.0, 1.0)
                                        font_name:'Arial'
                                        background_color: (237, 242, 239, 1.0)
                                                                              
                                    Button:
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (237, 242, 239, 1.0)
                                        
                                    Button:
                                        text: "ןוקית תומיא אלמל שרדנ אל ןוקית עצוב אלו הדימב :(לוחכ) ינדי ד''בצ םע הקידב - תילועפת תקידב                                                                  "
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תורעה"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout:
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        BoxLayout:
                                            Button:
                                                text:"ןוקית תומיא"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"הקידב"  
                                                font_name:"Arial" 
                                                size_hint: 1 , None
                                                height: "40 dp"     
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                        BoxLayout:
                                            orientation:"horizontal"                                          
                                            size_hint: 1 , None
                                            pos_hint: {"top": 1}
                                            height: "30 dp"
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                color: 0, 0, 0, 1
                                                pos_hint: {"top": 1}
                                                  
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                    BoxLayout: 
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            text:"הקידב"  
                                            font_name:"Arial" 
                                            size_hint: 1 , None
                                            height: "70 dp"     
                                            pos_hint: {"top": 1}
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תכרעמ תועש הנומ תגוצת אדוו"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(2, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "ךסמב יוארכ תגצומ תכרעמה תגוצת יכ אדוו\\n LCDה"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "1"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "(תוקלוד) POWER, NORMAL OXYGEN\\n(היובכ) SERVICE REQUIRED"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(3, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "תוקלוד יווח תורונ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "2"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תרחבנה הקיפסה תא גציימ תירודכה זכרמ"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(4, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: ".םירטיל 5 לש תכרעמ תקיפסל המירז מד ןווכ\\n תכרעמ תקיפס אדוו ינדי דמ רבח\\n הקדל םירטיל 4.5-5.5"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "3"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(5, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "(92%-96%) ינדיה דמב ןצמח תאירק אדו\\n 94% +- 2%"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "4"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(6, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: ":אצומ ץחל אדוו ינדי דמאצומ רוגס  \\n (7.7-9.3) 8.5PSI +- 0.8 "
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "5"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "SERVICE  תבהבהמ תרונ אדוו\\n LCD ךסמ לע גצומ הערתהה םשו  "
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(7, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "הקיפס תערתה אדוו ינדי דמ אצומ רוגס \\n OXYGEN FLOW LOW הכומנ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "6"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תוליזנ תקידב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(8, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "הקיפס תירפס תירודכ אדוו ינדי אצומ רוגס \\n ספאל תלפונ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "7"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(9, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "הקיפס אדוו םומיסקמל הקיפס דמ ררוב ןווכ \\n (5.5-9.5LPM) 7.5+-2LPM :תיברמ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "8"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תבהבהמ SERVICEתירונ אדוו\\n LCDה ךסמ לע גצומ הארתהה םשו"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(10, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "תערתה אדוו םומיסקמל הקיפס דמ ררוב ןווכ\\n HIGH OXYGEN FLOW הקיפס"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "9"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תבהבהמ SERVICEתירונ אדוו\\n LCDה ךסמ לע גצומ הארתהה םשו"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(11, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: " דרוה 80%ל תחתמ לא ןצמחה תדירי םע\\n תערתה אדוו םירטיל 4ל תכרעמ תקיפס\\n OXYGEN LOW ךומנ ןצמח"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "10"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תקלוד SERVICE תירונ אדוו   \\n הנתשמ רדתב ילוק יוויח עמשנו  "
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(12, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "אדוו תדבוע הדועב חתמ רוקממ תכרעמ קתנ\\n חתמ תלקת תערתה"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "11"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40dp"
                                        background_color: (1.0, 0.0, 0.0, 1.0)
                                        font_name:'Arial'
                                        background_color: (237, 242, 239, 1.0)
                                                                              
                                    Button:
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (237, 242, 239, 1.0)
                                        
                                    Button:
                                        text: "(תיללכ הקידב תרוצתב) : בשחוממ ד''בצ םע תכרעמ תציר - תילנויצקנופ הקידב 3                                            "
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תורעה"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout:
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        BoxLayout:
                                            Button:
                                                text:"ןוקית תומיא"
                                                font_name:"Arial"
                                                size_hint: .7 , None
                                                height: "40 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            
                                            Button:
                                                text:"ךרע"  
                                                font_name:"Arial" 
                                                size_hint: .3 , None
                                                height: "40 dp"     
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"הקידב"
                                                font_name:"Arial"
                                                size_hint: .7 , None
                                                height: "40 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            
                                            Button:
                                                text:"ךרע"  
                                                font_name:"Arial" 
                                                size_hint: .3 , None
                                                height: "40 dp"     
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                        BoxLayout:
                                            orientation:"horizontal"                                          
                                            size_hint: 1 , None
                                            pos_hint: {"top": 1}
                                            height: "30 dp"
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: .35 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: .35 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:" "
                                                font_name:"Arial"
                                                size_hint: .3 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: .35 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: .35 , None
                                                height: "32 dp"
                                                color: 0, 0, 0, 1
                                                pos_hint: {"top": 1}
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:" "
                                                font_name:"Arial"
                                                size_hint: .3 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            
                                    BoxLayout: 
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            text:"הקידב"  
                                            font_name:"Arial" 
                                            size_hint: 1 , None
                                            height: "70 dp"     
                                            pos_hint: {"top": 1}
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(2, 2)"
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                                                     
                                        Ar_text:
                                            name:"Table4.cell(2, 3)"
                                            font_name: 'Arial'
                                            hint_text: ""
                                            pos_hint: {"top": .98}
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                 
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "LPM ד''בצב תכרעמ תקיפס"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "1"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(3, 2)"
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                           
                                        Ar_text:
                                            name:"Table4.cell(3, 3)"
                                            font_name: 'Arial'
                                            hint_text: ""
                                            pos_hint: {"top": .98}
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "%אצומב ןצמח תמר"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "2"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(4, 2)"
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                            
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: "N/A"
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                 
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: "N/A"
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "ןווכ לעפה ,חתמ רוקמל תכרעמ רבח \\n  (4.5-5.5) םירטיל 5ל הקיפס"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "3"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(5, 2)"
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                           
                                        Ar_text:
                                            name:"Table4.cell(5, 3)"
                                            font_name: 'Arial'
                                            hint_text: ""
                                            pos_hint: {"top": .98}
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                 
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "LPM הקיפס תויתדונת"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "4"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(6, 2)"
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                           
                                        Ar_text:
                                            name:"Table4.cell(6, 3)"
                                            font_name: 'Arial'
                                            hint_text: ""
                                            pos_hint: {"top": .98}
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "ףרגב ןצמח זוחא תויתדונת"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "5"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(7, 2)"
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                           
                                        Ar_text:
                                            name:"Table4.cell(7, 3)"
                                            font_name: 'Arial'
                                            hint_text: ""
                                            pos_hint: {"top": .98}
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                             
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "PSI אצומ ץחל"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "6"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תןליזנ תקידב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(8, 2)"
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                           
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: "N/A"
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                 
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: "N/A"
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "תירודכ אדוו ינדי דמ אצומ רוגס \\n ספאל תלפונ הקיפס"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "7"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "םח וניא ריוואה יכ אדוול שרדנ"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(9, 2)"
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                           
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: "N/A"
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                 
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: .35 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: "N/A"
                                            size_hint: .3 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "הרירק ללוחמ אצומ תרוטרפמט אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "8"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40dp"
                                        background_color: (1.0, 0.0, 0.0, 1.0)
                                        font_name:'Arial'
                                        background_color: (237, 242, 239, 1.0)
                                                                              
                                    Button:
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (237, 242, 239, 1.0)
                                        
                                    Button:
                                        text: "                                              : הזירא תוקידב 4"
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תורעה"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout:
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        BoxLayout:
                                            Button:
                                                text:"ןוקית תומיא"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"הקידב"  
                                                font_name:"Arial" 
                                                size_hint: 1 , None
                                                height: "40 dp"     
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                        BoxLayout:
                                            orientation:"horizontal"                                          
                                            size_hint: 1 , None
                                            pos_hint: {"top": 1}
                                            height: "30 dp"
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                color: 0, 0, 0, 1
                                                pos_hint: {"top": 1}
                                                  
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                    BoxLayout: 
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            text:"הקידב"  
                                            font_name:"Arial" 
                                            size_hint: 1 , None
                                            height: "70 dp"     
                                            pos_hint: {"top": 1}
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תוקנל שי תכלכולמ םאב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            icon: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            text: "Table5.cell(2, 2)"                                                          
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "ךולכלו תוטירש ,תועיגפ אלל תכרעמ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "1"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                         
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "הרוצתל םאתהב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(3, 2)"
                                            icon:""                                          
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                              
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                           
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "הנמזהל םאות הזירא גוס"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "2"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "הרוצתל םאתהב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(4, 2)"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                              
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "הזיראה יבג לע SHIPMENT תקבדמ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "3"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "הרוצתל םאתהב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(5, 2)"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                              
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "תופרוצמ תומאות שומיש תוארוה אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "4"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(6, 2)"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                              
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "תופרוצמ ףא תוירוניצ יתש אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "5"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(7, 2)"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                             
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "ףרוצמ (HUMIDIFIER) יודיא לכימ בוליש אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "6"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "רישכמה לש ירודיסה ורפסמל םיאתמ יכ אדוו"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(8, 2)"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                              
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "הזיראה ג''ע ןאבצ S/N תקבדמ קבדה"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "7"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "רישכמה לש ירודיסה רפסמל ההז תויהל בייח"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(9, 2)"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                              
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "דוקרבה הדשב הזיראה ירודיס רפסמ סנכה \\n תרתוכב "
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "8"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "              תוכרעמ זרוא י''ע עוציב  \\n ספוטה יולימ תוניקתו הזירא תוניקת תומיאל"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(10, 2)"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                           
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "ינש קדוב י''ע ירודיס תוקבדמ תמאתה תקידב"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "9"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "___________________:המיתח"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        on_release: 
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    Button:    
                                        pos_hint: {"top": 1}
                                        id: worker1
                                        text: "___________________:קדוב םש"
                                        size_hint: .13 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        on_release: app.worker_name()
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                
                                    Button:    
                                        pos_hint: {"top": 1}
                                        
                                        id:date
                                        text: "___________________:הקידב ךיראת"
                                        size_hint: .13 , None
                                        on_release: app.document_date_one()
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "___________________:המיתח"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:    
                                        pos_hint: {"top": .98}
                                        text: "___________________:ינש קדוב םש"
                                        size_hint: .13 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        id: date_two    
                                        pos_hint: {"top": 1}
                                        text: "___________________:הקידב ךיראת"
                                        size_hint: .13 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        on_release: app.document_date_two()
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    
                                    
                                    
                                                        
                                
                Tab:
                    id: tab
                    text:"[font=Arial.ttf] ופלחיש םיקלח[/font]"
                    BoxLayout:
                        orientation:"vertical"
                        ScrollView:
                            MDList:
                                OneLineIconListItem:
                                    text: "[font=Arial.ttf]                                                                                                                                                            לוחכ לבק[/font]"
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, '11000316C', "קבל כחול", "OM-73")   
                                    
                                OneLineIconListItem:
                                    text: "[font=Arial.ttf]                                                                                                                                              PCB הרקב סיטרכ[/font]"
                                    font_name:'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19004469C", ' 230V כרטיס בקרה PCB' , "OM-73")
                                        
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                      230V רוואמ[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19001298C", "230V מאוור", "OM-64") 
                    
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                              FLOW[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19001296C", "FLOW", "OM-65")
                    
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                              דיונילוס[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19003296C", "סולינויד", "OM-59")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                        סחדמ םלוב[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19004333C", "בולם מדחס", "OM-59")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                         BUZZER[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19004386C", "BUZZER", "OM-68")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                              BUZZER PLASTIC CUP[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19004387C", "BUZZER PLASTIC CUP", "OM-68")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                                   תסוו[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19003299C", "תסוו", "OM-69") 
                                
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                         תסוו קובקב[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19003298C", " בקבוק תסוו", "OM-69") 
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                    ג'צ/ ךסמ סיטרכ[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19003302C", " כרטיס מסך/צ'ג", "OM-83")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                        230V סחדמ[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19003293C", " 230V מדחס", "OM-82/ OM-57/ OM-62")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                    לבכ ספות 'צוקס[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19004393C", " סקוצ' תופס כבל", "OM-75")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                 קיטספל לבכ ספות[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "40001504C", " תןפס כבל פלסטיק", "OM-84")
                                
                                
                
                Tab:
                    id: tab
                    text:"[font=Arial.ttf] הירוטסיה[/font]"
                    BoxLayout:
                        orientation:"vertical"
                        ScrollView:
                            BoxLayout:
                                orientation:"vertical"
                                size_hint: 1 , None
                                height: 4000        
                    
            
        Widget:
            
            
    ItzurScreen:
        id: ItzurScreen
        name: "ItzurScreen"
        
        BoxLayout:
            orientation: "vertical"
            MDToolbar:
                id: toolbar
                name: 'toolbar'
                title:'OXYTEC 5S PRODUCTION'
                elevation: 10
                left_action_items: [["arrow-left", lambda x: app.get_back()]] 
            MDTabs:
                Tab:
                    id: tab
                    text:"[font=Arial.ttf] תויפוס תוקידב ח''וד[/font]"
                    BoxLayout:
                        orientation:"vertical"
                        ScrollView:
                            BoxLayout:
                                orientation:"vertical"
                                size_hint: 1 , None
                                height: 4000
                                
                                GridLayout:
                                    cols: 3
                                    Button:
                                        text: 'מק"ט מערכת'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                    Button:
                                        text: 'הבכרהה םש'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                    Button:
                                        text: 'טקיורפה םש'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint:{"top": 1}
                                        color: 0, 0, 0, 1
                                                 
                                    Button:
                                        text: 'PK444A05M'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        color: 0, 0, 0, 1
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                            
                                    Button:
                                        text: 'Oxygen Concentrator 5L'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        color: 0, 0, 0, 1
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                
                                    Button:
                                        text: 'OXYTEC 5S'
                                        size_hint: 1 , None
                                        height: "40 dp"                                   
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    Button:
                                        text: "סחדמ ירודיס 'סמ "
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                        
                                    Button:
                                        text: 'ןאבצ דוקרב'
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                        
                                    Button:
                                        text: "רישכמל ירודיס 'סמ"
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                        
                                    BoxLayout:
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "140 dp"
                                        BoxLayout:
                                            orientation: "vertical"
                                            height: "140 dp"
                                            size_hint: 1 , None
                                            pos_hint: {"top": 1}
                                            font_name:'Arial'
                                        
                                            Ar_text:
                                                name: "menuTable.cell(3, 0)"
                                                text: 'SN:'
                                                size_hint: 1 , None
                                                height: "60 dp"
                                                max_text_length: 8
                                                size_hint_x: 0.8
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21 )
                                                  
                                            Button:
                                                text: 'סיטרכ ירודיס רפסמ'
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                font_name:'Arial'
                                                color: 0, 0, 0, 1
                                                
                                            Ar_text:
                                                name: "menuTable.cell(6, 0)"
                                                text: 'SN:'
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                font_name:'Arial'
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21 )
                                                
                                    Ar_text:
                                        name: "menuTable.cell(4, 1)"
                                        text: '                                Barcode'
                                        size_hint: 1 , None
                                        height: "140 dp"                     
                                        font_name:'Arial'
                                        pos_hint: {"center_x": 0.5, "center_y" : 0.5}
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        Widget:
                                    
                                    BoxLayout:
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        height: "140 dp"
                                        pos_hint: {"top": 1}
                                        BoxLayout:
                                            orientation:"vertical"
                                            Ar_text:
                                                name: "menuTable.cell(3, 2)"
                                                text: 'SN:'
                                                size_hint: 1 , None
                                                height: "60dp"                                             
                                                font_name:'Arial'
                                                pos_hint: {"top": 1}    
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21 )
                                                
                                            Button:
                                                text: "ןוניס ילכמ ירודיס 'סמ"
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                font_name:'Arial'
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                
                                            Ar_text:
                                                name: "menuTable.cell(6, 2)"
                                                text: "SN:"
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                font_name:'Arial'
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21 )
                                                
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40dp"
                                        background_color: (1.0, 0.0, 0.0, 1.0)
                                        font_name:'Arial'
                                        background_color: (237, 242, 239, 1.0)
                                                                              
                                    Button:
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (1.0, 0.0, 0.0, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (237, 242, 239, 1.0)
                                        
                                    Button:
                                        text: "תוינוציח תוילאוזיו תוקידב"
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תורעה"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout:
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        BoxLayout:
                                            Button:
                                                text:"ןוקית תומיא"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"הקידב"  
                                                font_name:"Arial" 
                                                size_hint: 1 , None
                                                height: "40 dp"     
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                        BoxLayout:
                                            orientation:"horizontal"                                          
                                            size_hint: 1 , None
                                            pos_hint: {"top": 1}
                                            height: "30 dp"
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                color: 0, 0, 0, 1
                                                pos_hint: {"top": 1}
                                                  
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                    BoxLayout: 
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            text:"הקידב"  
                                            font_name:"Arial" 
                                            size_hint: 1 , None
                                            height: "70 dp"     
                                            pos_hint: {"top": 1}
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                                
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תכרעמה זראמ יקלח ללכ תא הקנ"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            icon:''
                                            id: Table2.cell(2, 4)itzur
                                            pos_hint: {"top": .98}
                                            text: "Table2.cell(2, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                         
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "תועצמאב תכרעמ הקנו הנגה תופפכ הטע \\n יוטיח תילטמ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "1"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "סחדמ יגרב 8 רותיאל סנפב רזעה"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )       
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            icon:''
                                            id: table_one_1
                                            pos_hint: {"top": .98}
                                            text: "Table2.cell(3, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                         
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )     
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "םיקדוהמו םירבוחמ םימלוב אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "2"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "ב''הרא / הפוריא / לארשי"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )                                        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            icon:''
                                            pos_hint: {"top": .98}
                                            text: "Table2.cell(4, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                         
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "דעיה תרוצתל םאתהב תכרעמ עקת אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "3"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            icon:''
                                            pos_hint: {"top": .98}
                                            text: "Table2.cell(5, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                         
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                            
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "הקיפס לע לעפהו חתמ רוקמל תכרעמ רבח\\n הקדל םירטיל 5 לש"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "4"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תכרעמה בגב םיגרב 9 אדוו"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            icon: ""
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(6, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "זראמה ייגרב ללכ תואצמיה אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "5"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            icon: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            text: "Table2.cell(7, 4)itzur"
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "הפוסכ רוציי תקבדמ תואצמיה אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "6"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "110V/230V תרוצתל םאתהב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            icon:""
                                            text: "Table2.cell(8, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "POWER SUPPLY םיחתמ תקבדמ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "7"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(9, 4)itzur"
                                            icon:""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "ןאבצ ירודיס רפסמ תקבדמ אדוו\\n דוקרב תבלושמ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "8"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )     
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "רישכמה בגב םיננסמה אתב םיננסמה םוקימ"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(10, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "ןנסמו ילאירטקב ןנסמ ,סג ןנסמ רוביח אדוו\\n סחדמ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "9"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(11, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "תוריבשו םיפופכ אלל םיננסמ תרנצ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "10"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "האישנה תידיב םוקימ"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(12, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                            
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "יוארכ םקוממו רבוחמ תכרעמ לוקמר אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "11"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                            
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(13, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "יוארכ ספדומ ןאבצ וגול"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "12"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                            
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                            
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(14, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "NO SMOKE תקבדמ תואצמיה אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "13"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                            
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(15, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""                                           
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "ןיקת םיביכר בותיכ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "14"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(16, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "תיברימ הקיפס תרהזא תקבדמ קבדה"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "15"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )        
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table2.cell(17, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "םיננסמ תפלחה תקבדמ קבדה"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "16"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40dp"
                                        background_color: (1.0, 0.0, 0.0, 1.0)
                                        font_name:'Arial'
                                        background_color: (237, 242, 239, 1.0)
                                                                              
                                    Button:
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (237, 242, 239, 1.0)
                                        
                                    Button:
                                        text: "ןוקית תומיא אלמל שרדנ אל ןוקית עצוב אלו הדימב :(לוחכ) ינדי ד''בצ םע הקידב - תילועפת תקידב                                                                  "
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תורעה"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout:
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        BoxLayout:
                                            Button:
                                                text:"ןוקית תומיא"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"הקידב"  
                                                font_name:"Arial" 
                                                size_hint: 1 , None
                                                height: "40 dp"     
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                        BoxLayout:
                                            orientation:"horizontal"                                          
                                            size_hint: 1 , None
                                            pos_hint: {"top": 1}
                                            height: "30 dp"
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                color: 0, 0, 0, 1
                                                pos_hint: {"top": 1}
                                                  
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                    BoxLayout: 
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            text:"הקידב"  
                                            font_name:"Arial" 
                                            size_hint: 1 , None
                                            height: "70 dp"     
                                            pos_hint: {"top": 1}
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תכרעמ תועש הנומ תגוצת אדוו"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(2, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "ךסמב יוארכ תגצומ תכרעמה תגוצת יכ אדוו\\n LCDה"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "1"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "(תוקלוד) POWER, NORMAL OXYGEN\\n(היובכ) SERVICE REQUIRED"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )       
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(3, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "תוקלוד יווח תורונ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "2"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תרחבנה הקיפסה תא גציימ תירודכה זכרמ"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(4, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: ".םירטיל 5 לש תכרעמ תקיפסל המירז מד ןווכ\\n תכרעמ תקיפס אדוו ינדי דמ רבח\\n הקדל םירטיל 4.5-5.5"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "3"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(5, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "(92%-96%) ינדיה דמב ןצמח תאירק אדו\\n 94% +- 2%"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "4"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(6, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: ":אצומ ץחל אדוו ינדי דמאצומ רוגס  \\n (7.7-9.3) 8.5PSI +- 0.8 "
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "5"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "SERVICE  תבהבהמ תרונ אדוו\\n LCD ךסמ לע גצומ הערתהה םשו  "
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(7, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "הקיפס תערתה אדוו ינדי דמ אצומ רוגס \\n OXYGEN FLOW LOW הכומנ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "6"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תוליזנ תקידב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )      
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(8, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "הקיפס תירפס תירודכ אדוו ינדי אצומ רוגס \\n ספאל תלפונ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "7"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                        
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )         
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(9, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "הקיפס אדוו םומיסקמל הקיפס דמ ררוב ןווכ \\n (5.5-9.5LPM) 7.5+-2LPM :תיברמ"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "8"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תבהבהמ SERVICEתירונ אדוו\\n LCDה ךסמ לע גצומ הארתהה םשו"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(10, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "תערתה אדוו םומיסקמל הקיפס דמ ררוב ןווכ\\n HIGH OXYGEN FLOW הקיפס"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "9"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תבהבהמ SERVICEתירונ אדוו\\n LCDה ךסמ לע גצומ הארתהה םשו"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )        
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(11, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: " דרוה 80%ל תחתמ לא ןצמחה תדירי םע\\n תערתה אדוו םירטיל 4ל תכרעמ תקיפס\\n OXYGEN LOW ךומנ ןצמח"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "10"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תקלוד SERVICE תירונ אדוו   \\n הנתשמ רדתב ילוק יוויח עמשנו  "
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )      
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            text: "Table3.cell(12, 4)itzur"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "אדוו תדבוע הדועב חתמ רוקממ תכרעמ קתנ\\n חתמ תלקת תערתה"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 0.98}
                                            text: "11"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40dp"
                                        background_color: (1.0, 0.0, 0.0, 1.0)
                                        font_name:'Arial'
                                        background_color: (237, 242, 239, 1.0)
                                                                              
                                    Button:
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (237, 242, 239, 1.0)
                                        
                                    Button:
                                        text: "(תיללכ הקידב תרוצתב) : בשחוממ ד''בצ םע תכרעמ תציר - תילנויצקנופ הקידב 3                                            "
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תורעה"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout:
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        BoxLayout:
                                            Button:
                                                text:"ןוקית תומיא"
                                                font_name:"Arial"
                                                size_hint: .7 , None
                                                height: "40 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            
                                            
                                            Button:
                                                text:"הקידב"
                                                font_name:"Arial"
                                                size_hint: .7 , None
                                                height: "40 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            
                                            
                                        BoxLayout:
                                            orientation:"horizontal"                                          
                                            size_hint: 1 , None
                                            pos_hint: {"top": 1}
                                            height: "30 dp"
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: .35 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: .35 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: .35 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: .35 , None
                                                height: "32 dp"
                                                color: 0, 0, 0, 1
                                                pos_hint: {"top": 1}
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            
                                            
                                    BoxLayout: 
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            text:"הקידב"  
                                            font_name:"Arial" 
                                            size_hint: 1 , None
                                            height: "70 dp"     
                                            pos_hint: {"top": 1}
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                          
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(2, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )      
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "LPM ד''בצב תכרעמ תקיפס"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "1"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                          
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(3, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                   
                                        
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "%אצומב ןצמח תמר"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "2"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                             
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                 
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(4, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )       
                                                                          
                                        
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "ןווכ לעפה ,חתמ רוקמל תכרעמ רבח \\n  (4.5-5.5) םירטיל 5ל הקיפס"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "3"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                           
                                                                       
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(5, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                     
                                       
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "LPM הקיפס תויתדונת"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "4"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                            
                                                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(6, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                   
                                        
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "ףרגב ןצמח זוחא תויתדונת"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "5"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                          
                                                                    
                                        Button:
                                            pos_hint: {"top": 0.98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )   
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(7, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                   
                                        
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "PSI אצומ ץחל"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "6"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תןליזנ תקידב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                        
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                 
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(8, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                                                  
                                                                               
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "תירודכ אדוו ינדי דמ אצומ רוגס \\n ספאל תלפונ הקיפס"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "7"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "םח וניא ריוואה יכ אדוול שרדנ"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                             
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                 
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            text: "Table4.cell(9, 2)"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            icon:""
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )      
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "הרירק ללוחמ אצומ תרוטרפמט אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "8"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40dp"
                                        background_color: (1.0, 0.0, 0.0, 1.0)
                                        font_name:'Arial'
                                        background_color: (237, 242, 239, 1.0)
                                                                              
                                    Button:
                                        text: ""
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        background_color: (237, 242, 239, 1.0)
                                        
                                    Button:
                                        text: "                                              : הזירא תוקידב 4"
                                        size_hint: 1 , None
                                        height: "40 dp"
                                        background_color: (237, 242, 239, 1.0)
                                        font_name:'Arial'
                                        pos_hint: {"top": 1}
                                        color: 0, 0, 0, 1
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תורעה"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout:
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        BoxLayout:
                                            Button:
                                                text:"ןוקית תומיא"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "40 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"הקידב"  
                                                font_name:"Arial" 
                                                size_hint: 1 , None
                                                height: "40 dp"     
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                        BoxLayout:
                                            orientation:"horizontal"                                          
                                            size_hint: 1 , None
                                            pos_hint: {"top": 1}
                                            height: "30 dp"
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת אל"
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                pos_hint: {"top": 1}
                                                color: 0, 0, 0, 1
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                            Button:
                                                text:"ןיקת "
                                                font_name:"Arial"
                                                size_hint: 1 , None
                                                height: "32 dp"
                                                color: 0, 0, 0, 1
                                                pos_hint: {"top": 1}
                                                  
                                                background_color: (0.219, 0.219, 0.219, 0.21)
                                    BoxLayout: 
                                        orientation:"vertical"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"         
                                        Button:
                                            text:"הקידב"  
                                            font_name:"Arial" 
                                            size_hint: 1 , None
                                            height: "70 dp"     
                                            pos_hint: {"top": 1}
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "תוקנל שי תכלכולמ םאב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                           
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        MyButton:
                                            pos_hint: {"top": 0.98}
                                            icon: ""
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            text: "Table5.cell(2, 4)itzur" 
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "ךולכלו תוטירש ,תועיגפ אלל תכרעמ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "1"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                         
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "הרוצתל םאתהב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                 
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                           
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                 
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(3, 4)itzur"
                                            icon:""                                          
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "הנמזהל םאות הזירא גוס"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "2"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "הרוצתל םאתהב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""  
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                    
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                               
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                    
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(4, 4)itzur"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "הזיראה יבג לע SHIPMENT תקבדמ אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "3"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "הרוצתל םאתהב"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                    
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                              
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                 
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(5, 4)itzur"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )  
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "תופרוצמ תומאות שומיש תוארוה אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "4"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                        
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                         
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(6, 4)itzur"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                            
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "תופרוצמ ףא תוירוניצ יתש אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "5"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: ""
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                        
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                          
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                 
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                          
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(7, 4)itzur"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "ףרוצמ (HUMIDIFIER) יודיא לכימ בוליש אדוו"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "6"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "רישכמה לש ירודיסה ורפסמל םיאתמ יכ אדוו"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                        
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                        
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                            
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                        
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(8, 4)itzur"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                            
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "הזיראה ג''ע ןאבצ S/N תקבדמ קבדה"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "7"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "רישכמה לש ירודיסה רפסמל ההז תויהל בייח"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                        
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                     
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                              
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                     
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(9, 4)itzur"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "דוקרבה הדשב הזיראה ירודיס רפסמ סנכה \\n תרתוכב "
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "8"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "              תוכרעמ זרוא י''ע עוציב  \\n ספוטה יולימ תוניקתו הזירא תוניקת תומיאל"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"                                    
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                       
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                       
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                         
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                                                             
                                        Button:
                                            pos_hint: {"top": .98}
                                            text: ""                                         
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )                                    
                                        MyButton:
                                            pos_hint: {"top": .98}
                                            size_hint: 1, None
                                            text: "Table5.cell(10, 4)itzur"
                                            icon:""
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 ) 
                                        
                                    BoxLayout: 
                                        orientation:"horizontal"
                                        size_hint: 1 , None
                                        pos_hint: {"top": 1}
                                        height: "70 dp"
                                        
                                        Button:
                                            pos_hint: {"top": 1}
                                            text: "ינש קדוב י''ע ירודיס תוקבדמ תמאתה תקידב"
                                            size_hint: 1 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                        Button:    
                                            pos_hint: {"top": 1}
                                            text: "9"
                                            size_hint: .13 , None
                                            height: "70 dp"                                     
                                            font_name:'Arial'
                                            color: 0, 0, 0, 1
                                            background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "___________________:המיתח"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        on_release: 
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    Button:    
                                        pos_hint: {"top": 1}
                                        id: worker1
                                        text: "___________________:קדוב םש"
                                        size_hint: .13 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        on_release: app.worker_name()
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                
                                    Button:    
                                        pos_hint: {"top": 1}
                                        
                                        id:date
                                        text: "___________________:הקידב ךיראת"
                                        size_hint: .13 , None
                                        on_release: app.document_date_one()
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        pos_hint: {"top": 1}
                                        text: "___________________:המיתח"
                                        size_hint: 1 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:    
                                        pos_hint: {"top": .98}
                                        text: "___________________:ינש קדוב םש"
                                        size_hint: .13 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    Button:
                                        id: date_two    
                                        pos_hint: {"top": 1}
                                        text: "___________________:הקידב ךיראת"
                                        size_hint: .13 , None
                                        height: "70 dp"                                     
                                        font_name:'Arial'
                                        on_release: app.document_date_two()
                                        color: 0, 0, 0, 1
                                        background_color: (0.219, 0.219, 0.219, 0.21 )
                                    
                                    
                                    
                                    
                                                        
                                
                Tab:
                    id: tab
                    text:"[font=Arial.ttf] ופלחיש םיקלח[/font]"
                    BoxLayout:
                        orientation:"vertical"
                        ScrollView:
                            MDList:
                                OneLineIconListItem:
                                    text: "[font=Arial.ttf]                                                                                                                                                            לוחכ לבק[/font]"
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, '11000316C', "קבל כחול", "OM-73")   
                                    
                                OneLineIconListItem:
                                    text: "[font=Arial.ttf]                                                                                                                                              PCB הרקב סיטרכ[/font]"
                                    font_name:'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1 , "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19004469C", ' 230V כרטיס בקרה PCB' , "OM-73")
                                        
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                      230V רוואמ[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19001298C", "230V מאוור", "OM-64") 
                    
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                              FLOW[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19001296C", "FLOW", "OM-65")
                    
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                              דיונילוס[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19003296C", "סולינויד", "OM-59")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                        סחדמ םלוב[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19004333C", "בולם מדחס", "OM-59")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                         BUZZER[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19004386C", "BUZZER", "OM-68")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                              BUZZER PLASTIC CUP[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19004387C", "BUZZER PLASTIC CUP", "OM-68")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                                   תסוו[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19003299C", "תסוו", "OM-69") 
                                
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                         תסוו קובקב[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19003298C", " בקבוק תסוו", "OM-69") 
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                    ג'צ/ ךסמ סיטרכ[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19003302C", " כרטיס מסך/צ'ג", "OM-83")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                        230V סחדמ[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19003293C", " 230V מדחס", "OM-82/ OM-57/ OM-62")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                    לבכ ספות 'צוקס[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "19004393C", " סקוצ' תופס כבל", "OM-75")
                                
                                OneLineListItem:
                                    text:"[font=Arial.ttf]                                                                                                                                                                 קיטספל לבכ ספות[/font]"
                                    font_name: 'Arial'
                                    MDCheckbox:
                                        pos_hint:{"center_x": 0.1, "center_y": 0.5}
                                        active: False
                                        on_active: app.on_checkbox_active(*args, "40001504C", " תןפס כבל פלסטיק", "OM-84")
                                
                                
                
                Tab:
                    id: tab
                    text:'[font=Arial.ttf] םייוקיל ח"וד[/font]'
                    BoxLayout:
                        orientation:"vertical"
                        
                        
                        BoxLayout:
                            orientation:"horizontal"
                            bg_color: 1, 1, 1
                            pos_hint: {"top": 1}
                            size_hint: 1, None
                            size:"100dp", "70dp"
                            Button:
                                text: "םייוקיל ח''וד"
                                size_hint: 1 , None
                                height: "70 dp"
                                font_name:'Arial'
                                font_size: "40sp"
                                pos_hint: {"top": 1}
                                color: 0, 0, 0, 1   
                                background_color: 255,233, 0, 1                 
                            Button:
                                pos_hint: {"top": 1}
                                size_hint: 1, None
                                text:"ןאבצ תצובק"
                                height: "70 dp"                                     
                                font_name:'Arial'
                                font_size: "40sp"
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1      
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp"
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center_x": 0.75}
                                size_hint: 1, None
                                text:":טקיורפ"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1 , "center": 0.25}
                                size_hint: 1, None
                                text:':טקיורפל ןאבצ ט"קמ'
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                size_hint: None, None
                                size:"700dp", "25dp"
                                text:"ןצמח ללוחמ"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1 , "center": 0.25}
                                size_hint: None, None
                                text:':טירפה רואת'
                                size: "300dp" , "40dp"                                    
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                id: likuim_date
                                name: "likuim_date"
                                size_hint: 1, None
                                text:" : ךיראת"
                                height: "40 dp"
                                on_release: app.date()                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                id: likuim_sn
                                name: "likuim_sn"
                                pos_hint: {"top": 1 , "center": 0.25}
                                size_hint: 1, None
                                text:':תכרעמ ירודיס רפסמ'
                                height: "40 dp"                                     
                                font_name:'Arial'
                                on_release: app.likuim_serial_number()
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1     
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: 1, None
                                text:"                                                                                                                               םייוקיל"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                        
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:"ךיראת"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:"המיתח"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:"ןקתמה םש"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .5, None
                                text:"יוקילה/הלקתה רואת"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1 
                                
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .45, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .05, None
                                text:"1"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1    
                            
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .45, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .05, None
                                text:"2"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1    
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .45, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .05, None
                                text:"3"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1    
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .45, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .05, None
                                text:"4"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1    
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .45, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .05, None
                                text:"5"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1    
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .45, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .05, None
                                text:"6"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1    
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .45, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .05, None
                                text:"7"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1    
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .45, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .05, None
                                text:"8"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1    
                        BoxLayout:
                            orientation: "horizontal"
                            size_hint: 1, None
                            size:"100dp", "40dp" 
                            pos_hint: {"top": 1}
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .16, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .45, None
                                text:""
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1
                            Button: 
                                pos_hint: {"top": 1, "center": 0.75}
                                name: "likuim_date"
                                size_hint: .05, None
                                text:"9"
                                height: "40 dp"                                     
                                font_name:'Arial'
                                color: 0, 0, 0, 1
                                background_color: 255,233, 0, 1    
                                                               
                        Widget:           
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        Widget:

   
                

    MedimarketScreen:
        id: MedimarketScreen
        name: "MedimarketScreen"
        
        
        BoxLayout:
            orientation: "vertical"
            MDToolbar:
                id: toolbar
                name: 'toolbar'
                title:'Chaban Medical Repair'
                elevation: 10        
            Widget:

            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:

                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     [/font]"
                            on_press:
                            
                            
                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                    [/font]"
                            
                            font_name:'Arial'
                            on_press:


    DashmedikScreen:
        id: DashmedikScreen
        name: "DashmedikScreen"
        
        
        BoxLayout:
            orientation: "vertical"
            MDToolbar:
                id: toolbar
                name: 'toolbar'
                title:'Chaban Medical Repair'
                elevation: 10        
            Widget:

            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:

                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     [/font]"
                            on_press: 
                            

                        OneLineIconListItem:
                            text: "[font=Arial.ttf]                                                     [/font]"
                            
                            font_name:'Arial'
                            on_press:



"""