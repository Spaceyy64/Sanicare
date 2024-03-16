from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen ,FadeTransition
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton,MDFlatButton, MDRectangleFlatIconButton, MDIconButton
from kivymd.uix.navigationrail import MDNavigationRail, MDNavigationRailItem,MDNavigationRailMenuButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.uix.video import Video
from kivymd.uix.textfield import  MDTextField
from kivy_garden.mapview import MapView, MapMarker
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dropdownitem import  MDDropDownItem
from kivy.metrics import dp
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.textinput import TextInput
from kivymd.uix.label.label import MDIcon
from kivymd.uix.gridlayout import MDGridLayout
import random
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
import webbrowser

############################################################################################################################################################################
######################################  VIDEO SCREEN  #####################################################################################################################
class winvid(Screen):
    def __init__(self, **kwa):
        super(winvid, self).__init__(**kwa)

        box = MDBoxLayout(md_bg_color ="#10e1e9")
        vid = Video(source ="vid.avi")
        vid.bind(eos=self.done)
        vid.state ='play'
        box.add_widget(vid)
        self.add_widget(box)


    def done(self,dt,instance):
        self.manager.current = "win1"



##########################################################################################################################################################################################
############################## STARTING WINDOW ##########################################################################################################################################

class IconListItem(TwoLineListItem):
    icon = StringProperty()


class win1(Screen):
    vidstate = 0
    tmst = 0
    bmst =0



    def __init__(self, **kwa):
        super().__init__(**kwa)


        self.bmcl = MDLabel(text = "", pos_hint = {'x':2,'y':2})
        self.add_widget(self.bmcl)
        self.tmcl = MDLabel(text = "", pos_hint = {'x':2,'y':2})
        self.add_widget(self.tmcl)

        box1 = MDBoxLayout(md_bg_color = "#10e1e9")


        self.add_widget(box1)
        logimg= Image(source="SCIENCE Logo.png", size_hint_x = 0.39, size_hint_y = 0.4, pos_hint={'x':0.3, 'y':0.6})
        self.add_widget(logimg)
        exitbtn=MDRaisedButton(text="Exit", on_release=self.bonm, pos_hint={'x': 0, 'y': .9}, size_hint = (0.1,0.1))
        self.add_widget(exitbtn)




        button = MDRaisedButton( text="Select Region", on_release=self.op, pos_hint={'x': 0.4, "y": 0.35}, size_hint = (0.2,0.1))

        menu_items = [
            {
                "text" :'Thane Municipal Corporation',
                "on_release": self.tmc,
                "viewclass": "IconListItem"
            },

            {
                "text": 'Brihanmumbai Municipal Corporation',
                "on_release":  self.bmc,
                "viewclass":"IconListItem"
            }
        ]


        self.menu = MDDropdownMenu(
            caller = button,
            items=menu_items,
            position="bottom",
            width_mult=5,
        )

        btn = MDRaisedButton(text="Confirm", on_release=self.gg, pos_hint={'x':0.4, 'y': .1}, size_hint = (0.2,0.1))
        self.add_widget(btn)
        self.add_widget(button)

        box = MDBoxLayout(pos_hint={'x': 0.35, 'y': 0.5}, size_hint=(0.3, 0.05), md_bg_color="#FFFFFF")
        self.add_widget(box)

    def op(self,instance):
        self.menu.open()

    def gg(self, instance):
        if win1.tmst==1 :
            self.manager.current = "win3"

        if win1.bmst == 1:
            self.manager.current = "win4"



    def tmc(self):
        self.menu.dismiss()
        self.remove_widget(self.bmcl)
        box = MDBoxLayout(pos_hint={'x': 0.35, 'y': 0.5}, size_hint=(0.3, 0.05), md_bg_color="#FFFFFF")
        box.add_widget(MDIcon(icon="google-maps",text = 'Thane Municipal Corporation', pos_hint = {'x':0.35,'y':0.51}, size_hint = (0.8,0.01),background ="#000000"))
        self.tmcl = MDLabel( text='Thane Municipal Corporation', pos_hint={'x': 0.38, 'y': 0.5},size_hint=(0.8, 0.01), background="#000000")
        box.add_widget(self.tmcl)
        self.add_widget(box)
        win1.tmst = 1

    def bmc(self):
        self.menu.dismiss()
        self.remove_widget(self.tmcl)
        box = MDBoxLayout(pos_hint={'x': 0.35, 'y': 0.5}, size_hint=(0.3, 0.05), md_bg_color="#FFFFFF")
        box.add_widget(MDIcon(icon="google-maps",text = 'Brihanmumbai Municipal Corporation', pos_hint = {'x':0.35,'y':0.51}, size_hint = (0.8,0.01),background ="#000000"))
        self.bmcl = MDLabel( text='Brihanmumbai Municipal Corporation', pos_hint={'x': 0.38, 'y': 0.5},size_hint=(0.8, 0.01), background="#000000")
        box.add_widget(self.bmcl)
        self.add_widget(box)
        win1.bmst = 1


    def pop(self, *args):
        self.manager.current = 'win3'
        win1.vidstate =1

  
    def bonm(self, dt):
        self.dialog = MDDialog(
            text="Are you sure you want to leave?",
           
            buttons=[MDFlatButton(text="CANCEL", text_color="black", on_release=self.no),
                     MDFlatButton(text="YES", text_color="black", on_release=self.yes), ], )
        self.dialog.open()

    def yes(self, instance):
        SaniCare().get_running_app().stop()

    def no(self, instance):
        self.dialog.dismiss()

############################################################################################################################################################################
############################### MAIN WINDOW ####################################################################################################################


class win3(Screen):


    def __init__(self, **kwa):
        super(win3, self).__init__(**kwa)
        self.mapviw = MapView(zoom=12, lat=19.2183, lon=72.9781, double_tap_zoom=True, pos_hint = {'x':3,"y":5})

        box = MDFloatLayout(pos_hint = {'x':0,"y":0},size_hint = (0.1,0.9))
        box.add_widget(MDNavigationRail(
            MDNavigationRailItem(
                text="Map",
                icon="map", on_release=self.map),
            MDNavigationRailItem(
                text="Model",
                icon="air-filter", on_release=self.modal),
            MDNavigationRailItem(
                text="FAQ",
                icon="head-question", on_release=self.Faq),

            MDNavigationRailItem(
                text="Back",
                icon = "arrow-left-bottom-bold",
                on_release=self.back
            ),

            MDNavigationRailItem(
                text="Exit",
                icon="exit-to-app", on_release=self.exit, ),

            md_bg_color="#e7e4c0",
            selected_color_background="#fffcf4",
            ripple_color_item="#e7e4c0",
            anchor="top",

        ))
        

        box1 = MDFloatLayout(pos_hint={'x': 0, 'y': 0.9}, md_bg_color="#EFE4B0")
        but = MDLabel(text="SaniCare", size_hint=(0.45, 0.1), font_style="H4",pos_hint = {'x':0.4,"y":0})

        self.box2 = MDBoxLayout(md_bg_color="#fbfce8",pos_hint={"x": 0.1, "y": 0}, size_hint=(0.9, 0.9))
        self.add_widget(self.box2)
        self.box2.add_widget(self.mapviw)

        self.b1=MDFloatLayout(pos_hint={'x': 20, 'y': 13}, md_bg_color="#FFFFFF", size_hint=(.9, .1))
        self.box2.add_widget(self.b1)

        box1.add_widget(but)

        self.add_widget(box1)

        self.add_widget(box)
        self.sv = MDScrollView()

    def map(self, instance):
        self.box2.remove_widget(self.sv)
        self.box2.remove_widget(self.mapviw)
        self.box2.remove_widget(self.b1)
        self.remove_widget(self.box2)


        self.b1=MDFloatLayout(pos_hint={'x': 2, 'y': 3}, md_bg_color="#FFFFFF", size_hint=(.9, .1))
        label1=MDLabel(text="", pos_hint={'x': 0.3, 'y': 0.3} , font_size="30sp", color = (0,0,0,1))
        self.b1.add_widget(label1)
        self.remove_widget(self.b1)
        self.add_widget(self.b1)

        self.mapviw = MapView(zoom=12, lat=19.283, lon=72.9781, double_tap_zoom=True)
        m1 = MapMarker(lat=19.239, lon=72.997, on_press=self.l1)
        m2 = MapMarker(lat=19.208, lon=73.016, on_release=self.l1)
        m3 = MapMarker(lat=19.217, lon=72.97, on_release=self.l1)
        m4 = MapMarker(lat=19.203, lon=73.005, on_release=self.l1)
        m5 = MapMarker(lat=19.209, lon=72.95, on_release=self.l1)
        m6 = MapMarker(lat=19.273, lon=72.97, on_release=self.l1)
        m7 = MapMarker(lat=19.216, lon=72.985, on_release=self.l1)
        m8 = MapMarker(lat=19.275, lon=73.001, on_release=self.l1)
        m9 = MapMarker(lat=19.258, lon=73.004, on_release=self.l1)
        m10 = MapMarker(lat=19.242494, lon=72.94, on_release=self.l1)
        m11 = MapMarker(lat=19.208914, lon=73.006980, on_release=self.l1)
        m12 = MapMarker(lat=19.299458, lon=72.979290, on_release=self.l1)
        m13 = MapMarker(lat=19.266251, lon=72.973466, on_release=self.l1)
        self.mapviw.add_marker(m1)
        self.mapviw.add_marker(m2)
        self.mapviw.add_marker(m3)
        self.mapviw.add_marker(m4)
        self.mapviw.add_marker(m5)
        self.mapviw.add_marker(m6)
        self.mapviw.add_marker(m7)
        self.mapviw.add_marker(m8)
        self.mapviw.add_marker(m9)
        self.mapviw.add_marker(m10)
        self.mapviw.add_marker(m11)
        self.mapviw.add_marker(m12)
        self.mapviw.add_marker(m13)
        self.box2.add_widget(self.mapviw)

        self.add_widget(self.box2)

    def l1(self, instance):
        wop = random.randrange(5, 10)
        nop = wop*1000000/22
        vop = nop*2.4
        cow = 1200*wop
        vopw = 600*wop

        self.box2.remove_widget(self.b1)
        self.b1=MDFloatLayout(pos_hint={'x': 0.1, 'y': 0}, md_bg_color="#FFFFFF", size_hint=(.9, .1))
        label11=MDLabel(text="Data of Pads Processed in this Plant:", font_style="H4", bold=True, font_size="25sp", pos_hint={'x':0.1, 'y':8})
        label1=MDLabel(text=f"{wop} tonnes of pads recieved\n\n{round(nop)} pads in {wop} tonnes\n\n{cow} Litres of water required\n\n{vopw} pads washed\n\n{round(vop)} grams of polymers recycled", pos_hint={'x': 0.05, 'y': 4} , font_style="H6", font_size="10sp", color = (0,0,0,1))
        
        self.b1.add_widget(label1)
        self.b1.add_widget(label11)
        self.box2.add_widget(self.b1)

    def Faq(self, instance):
        self.box2.remove_widget(self.mapviw)
        self.box2.remove_widget(self.sv)
        self.box2.remove_widget(self.b1)
        self.remove_widget(self.box2)


        self.grid = MDGridLayout(md_bg_color="#fbfce8", pos_hint={"x": 0.1, "y": 0}, size_hint=(1, 0.9),cols = 1,adaptive_height = True,size_hint_y=None)
        self.sv = MDScrollView()

        list = ThreeLineListItem(text = "90% of a pad contains plastics such as polyethelene , polypropelene and polyester ", secondary_text ="Polyster can be used in clothing industry and in home furnishing", tertiary_text = "Polyethylene and Polypropelene are primarily used in the production of Paking films, cable insulation,grocery bags and square bottles", tertiary_text_color = '#000000', secondary_text_color ="#000000")
        list2 = OneLineListItem(text="Approximately 5-7 KL of water will be required for the washing purpose.")
        list3 = OneLineListItem(text ="The Leftovers obtained are all bio-degradable , and are not harmful.")
        list4 = OneLineListItem(text = "Around 2.4 gram of recycled polymer can be obtained from one sanitary napkin")

        list5 = TwoLineListItem(text = "The number of centers required depends on the amount of waste generated in each ward.", secondary_text= "For Example, thane requires 13 wards for its waste, whereas Mumbai requires 8", secondary_text_color = "#00000")
        self.grid.add_widget(
            MDExpansionPanel(
                icon = "cloud-question",
                content = list,

                panel_cls=MDExpansionPanelOneLine(
                    text="What are the uses of the recycled pad?",

            ),
        ))

        self.grid.add_widget(
            MDExpansionPanel(
                icon="cloud-question",
                content=list2,

                panel_cls=MDExpansionPanelOneLine(
                    text="How much amount of water will be required for washing purpose?",
                ))
        )

        self.grid.add_widget(
            MDExpansionPanel(
                icon="cloud-question",
                content=list3,

                panel_cls=MDExpansionPanelOneLine(
                    text="Can the leftovers obtained after the processing pose concern for the environment?",
                ))
        )


        self.grid.add_widget(
            MDExpansionPanel(
                icon="cloud-question",
                content=list4,

                panel_cls=MDExpansionPanelOneLine(
                    text="How much recycled polymer can be obtained from one pad?",
                ))
        )

        self.grid.add_widget(
            MDExpansionPanel(
                icon="cloud-question",
                content=list5,

                panel_cls=MDExpansionPanelOneLine(
                    text="How many centers will be required in one ward?",
                ))
        )



        self.grid.add_widget(MDLabel(text="For further support, contact us through e-mail at:-"))
        self.grid.add_widget(MDFlatButton(text="[color=#0000FF]sanicare.official@gmail.com[/color]", on_release=self.link))



        self.sv.add_widget(self.grid)
        self.box2.add_widget(self.sv)
        self.add_widget(self.box2)

    def link(self,instance):
        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJlLWcxplpPDtgddvBQrsDFPrZdpnjJBrQDbvXWHlBVhLccgZdMzlFkmjwgRCscWFsXFHxq")

    def modal(self, instance):
        self.box2.remove_widget(self.mapviw)
        self.box2.remove_widget(self.sv)
        self.remove_widget(self.box2)
        self.box2.remove_widget(self.b1)
        self.grid =MDFloatLayout(md_bg_color="#fbfce8",pos_hint={"x": 0.1, "y": 0}, size_hint=(0.9, 0.9), size_hint_y = None, adaptive_height=True)
        self.sv = MDScrollView()

        self.sv.add_widget(self.grid)
        self.grid.add_widget(MDLabel(text = "Model Information", pos_hint = {'x':0.3,'y':0.35} , font_style = "H4"))


        self.grid.add_widget(MDLabel(text ="Materials Used:", pos_hint = {'x':0.05,'y':0},  font_style = "H5", bold=True ))

        self.grid.add_widget(MDLabel(text="Motor", pos_hint={'x':0.1, 'y': -0.3}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Water pump", pos_hint={'x':.1, 'y': -.5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Circuit components", pos_hint={'x':.1, 'y': -.7}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Plastic chamber", pos_hint={'x':.1 ,'y': -.9}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Gear", pos_hint={'x':0.1, 'y': -1.1}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Pad", pos_hint={'x':0.1, 'y': -1.3}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Silicon pipes", pos_hint={'x':0.1, 'y': -1.5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Silica gel", pos_hint={'x':0.1, 'y': -1.7}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Model of collection vehicle", pos_hint={'x':0.1, 'y': -1.9}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Model of collection centre", pos_hint={'x':0.1, 'y': -2.1}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Procedure/Description:", pos_hint={'x':0.05, 'y': -2.5}, font_style="H5", bold=True))
        self.grid.add_widget(MDLabel(text="The basic ideology behind this project is to create an atmosphere wherein used pads are treated and reused properly for various purposes. The model which is made is a miniature version of the real one. The following are the processes involved :-", pos_hint={'x':0.1, 'y': -3.5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="1.Collection of pads and transporting them to the models installed in certain areas depending on the location and availability of safe labor in that area.", pos_hint={'x':0.1, 'y': -4.4}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="2.Adding all pads in the unit.", pos_hint={'x':0.1, 'y': -5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="3.Washing the pads with salt solution for around 15mins this process would remove the blood absorbed by the super absorbent polymer(sap) in the napkins.", pos_hint={'x':0.1, 'y': -5.6}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="4.Draining out the blood dissolved water into the drainage .This blood would be treated at the water treatment plants.", pos_hint={'x':0.1, 'y': -6.3}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="5.The leftovers of the pads in the unit undergo spinning in order to dry them up.", pos_hint={'x':0.1, 'y': -6.9}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="6.Through a collection chamber these dried up pads which now only contain plastics[PE, PP ,PET] are further put to another process.", pos_hint={'x':0.1, 'y': -7.5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="7.This includes disinfecting the pads . The E beam sterilization would do the purpose.", pos_hint={'x':0.1, 'y': -8}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="8.Later these sterilized plastic are to be sent to recycling units.", pos_hint={'x':0.1, 'y': -8.5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="9.These recycling units would then convert the plastics to other usable forms.", pos_hint={'x': 0.1, 'y': -9}, font_style="H6", bold=True))



        self.box2.add_widget(self.sv)
        self.add_widget(self.box2)





    def exit(self, dt):
        self.dialog = MDDialog(
            text="Are you sure you want to leave?",
            buttons=[MDFlatButton(text="CANCEL", text_color="black", on_release=self.no),
                     MDFlatButton(text="YES", text_color="black", on_release=self.yes), ], )
        self.dialog.open()

    def back(self, instance):
        self.manager.current="win1"

    def yes(self, instance):
        SaniCare().get_running_app().stop()

    def no(self, instance):
        self.dialog.dismiss()

#############################################################################################################################################################
############################## BMC WINDOW #######################################################################################################################

class win4(Screen):


    def __init__(self, **kwa):
        super(win4, self).__init__(**kwa)
        self.mapviw = MapView(zoom=12, lat=19.2183, lon=72.9781, double_tap_zoom=True, pos_hint = {'x':3,"y":5})

        box = MDFloatLayout(pos_hint = {'x':0,"y":0},size_hint = (0.1,0.9))
        box.add_widget(MDNavigationRail(
            MDNavigationRailItem(
                text="Map",
                icon="map", on_release=self.map),
            MDNavigationRailItem(
                text="Model",
                icon="air-filter", on_release=self.modal),
            MDNavigationRailItem(
                text="FAQ",
                icon="head-question", on_release=self.Faq),

            MDNavigationRailItem(
                text="Back",
                icon = "arrow-left-bottom-bold",
                on_release=self.back
            ),

            MDNavigationRailItem(
                text="Exit",
                icon="exit-to-app", on_release=self.exit, ),

            md_bg_color="#e7e4c0",
            selected_color_background="#fffcf4",
            ripple_color_item="#e7e4c0",
            anchor="top",

        ))
        

        box1 = MDFloatLayout(pos_hint={'x': 0, 'y': 0.9}, md_bg_color="#EFE4B0")
        but = MDLabel(text="SaniCare", size_hint=(0.45, 0.1), font_style="H4",pos_hint = {'x':0.4,"y":0})



        self.box2 = MDBoxLayout(md_bg_color="#fbfce8",pos_hint={"x": 0.1, "y": 0}, size_hint=(0.9, 0.9))
        self.add_widget(self.box2)
        self.box2.add_widget(self.mapviw)

        self.b1=MDFloatLayout(pos_hint={'x': 20, 'y': 13}, md_bg_color="#FFFFFF", size_hint=(.9, .1))
        self.box2.add_widget(self.b1)

        box1.add_widget(but)

        self.add_widget(box1)

        self.add_widget(box)
        self.sv = MDScrollView()

    def map(self, instance):
        self.box2.remove_widget(self.sv)
        self.box2.remove_widget(self.mapviw)
        self.box2.remove_widget(self.b1)
        self.remove_widget(self.box2)


        self.b1=MDFloatLayout(pos_hint={'x': 2, 'y': 3}, md_bg_color="#FFFFFF", size_hint=(.9, .1))
        label1=MDLabel(text="Hello", pos_hint={'x': 0.3, 'y': 0.3} , font_size="30sp", color = (0,0,0,1))
        self.b1.add_widget(label1)
        self.remove_widget(self.b1)
        self.add_widget(self.b1)

        self.mapviw = MapView(zoom=11, lat=19.138786,lon=72.9314192, double_tap_zoom=True)
        m1 = MapMarker(lat=18.929597, lon=72.822267, on_press=self.l1)
        m2 = MapMarker(lat=18.967955, lon=72.807222, on_release=self.l1)
        m3 = MapMarker(lat=19.024857, lon=72.887025, on_release=self.l1)
        m4 = MapMarker(lat=19.122535, lon=72.887025, on_release=self.l1)
        m5 = MapMarker(lat=19.190282, lon=72.868997, on_release=self.l1)
        m6 = MapMarker(lat=19.082620, lon=73.004230, on_release=self.l1)
        m7 = MapMarker(lat=19.193901, lon=72.818021, on_release=self.l1)
        m8 = MapMarker(lat=19.075954, lon=72.897019, on_release=self.l1)
        self.mapviw.add_marker(m1)
        self.mapviw.add_marker(m2)
        self.mapviw.add_marker(m3)
        self.mapviw.add_marker(m4)
        self.mapviw.add_marker(m5)
        self.mapviw.add_marker(m6)
        self.mapviw.add_marker(m7)
        self.mapviw.add_marker(m8)
        self.box2.add_widget(self.mapviw)

        self.add_widget(self.box2)

    def l1(self, instance):
        wop = random.randrange(5, 10)
        nop = wop*1000000/22
        vop = nop*2.4
        cow = 1200*wop
        vopw = 600*wop

        self.box2.remove_widget(self.b1)
        self.b1=MDFloatLayout(pos_hint={'x': 0.1, 'y': 0}, md_bg_color="#FFFFFF", size_hint=(.9, .1))
        label11=MDLabel(text="Data of Pads Processed in this Plant:", font_style="H4", bold=True, font_size="25sp", pos_hint={'x':0.1, 'y':8})
        label1=MDLabel(text=f"{wop} tonnes of pads recieved\n\n{round(nop)} pads in {wop} tonnes\n\n{cow} Litres of water required\n\n{vopw} pads washed\n\n{round(vop)} grams of polymers recycled", pos_hint={'x': 0.05, 'y': 4} , font_style="H6", font_size="10sp", color = (0,0,0,1))
        
        self.b1.add_widget(label1)
        self.b1.add_widget(label11)
        self.box2.add_widget(self.b1)

    def Faq(self, instance):
        self.box2.remove_widget(self.mapviw)
        self.box2.remove_widget(self.sv)
        self.box2.remove_widget(self.b1)
        self.remove_widget(self.box2)


        self.grid = MDGridLayout(md_bg_color="#fbfce8", pos_hint={"x": 0.1, "y": 0}, size_hint=(1, 0.9),cols = 1,adaptive_height = True,size_hint_y=None)
        self.sv = MDScrollView()

        list = ThreeLineListItem(text = "90% of a pad contains plastics such as polyethelene , polypropelene and polyester ", secondary_text ="Polyster can be used in clothing industry and in home furnishing", tertiary_text = "Polyethylene and Polypropelene are primarily used in the production of Paking films, cable insulation,grocery bags and square bottles", tertiary_text_color = '#000000', secondary_text_color ="#000000")
        list2 = OneLineListItem(text="Approximately 5-7 KL of water will be required for the washing purpose.")
        list3 = OneLineListItem(text ="The Leftovers obtained are all bio-degradable , and are not harmful.")
        list4 = OneLineListItem(text = "Around 2.4 gram of recycled polymer can be obtained from one sanitary napkin")

        list5 = TwoLineListItem(text = "The number of centers required depends on the amount of waste generated in each ward.", secondary_text= "For Example, thane requires 13 wards for its waste, whereas Mumbai requires 8", secondary_text_color = "#00000")
        self.grid.add_widget(
            MDExpansionPanel(
                icon = "cloud-question",
                content = list,

                panel_cls=MDExpansionPanelOneLine(
                    text="What are the uses of the recycled pad?",

            ),
        ))

        self.grid.add_widget(
            MDExpansionPanel(
                icon="cloud-question",
                content=list2,

                panel_cls=MDExpansionPanelOneLine(
                    text="How much amount of water will be required for washing purpose?",
                ))
        )

        self.grid.add_widget(
            MDExpansionPanel(
                icon="cloud-question",
                content=list3,

                panel_cls=MDExpansionPanelOneLine(
                    text="Can the leftovers obtained after the processing pose concern for the environment?",
                ))
        )


        self.grid.add_widget(
            MDExpansionPanel(
                icon="cloud-question",
                content=list4,

                panel_cls=MDExpansionPanelOneLine(
                    text="How much recycled polymer can be obtained from one pad?",
                ))
        )

        self.grid.add_widget(
            MDExpansionPanel(
                icon="cloud-question",
                content=list5,

                panel_cls=MDExpansionPanelOneLine(
                    text="How many centers will be required in one ward?",
                ))
        )


        self.grid.add_widget(MDLabel(text="For further support, contact us through e-mail at:-"))
        self.grid.add_widget(MDFlatButton(text="[color=#0000FF]sanicare.official@gmail.com[/color]", on_release=self.link))



        self.sv.add_widget(self.grid)
        self.box2.add_widget(self.sv)
        self.add_widget(self.box2)

    def link(self,instance):
        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJlLWcxplpPDtgddvBQrsDFPrZdpnjJBrQDbvXWHlBVhLccgZdMzlFkmjwgRCscWFsXFHxq")


    def modal(self, instance):
        self.box2.remove_widget(self.mapviw)
        self.box2.remove_widget(self.sv)
        self.remove_widget(self.box2)
        self.box2.remove_widget(self.b1)
        self.grid =MDFloatLayout(md_bg_color="#fbfce8",pos_hint={"x": 0.1, "y": 0}, size_hint=(0.9, 0.9), size_hint_y = None, adaptive_height=True)
        self.sv = MDScrollView()

        self.sv.add_widget(self.grid)
        self.grid.add_widget(MDLabel(text = "Model Information", pos_hint = {'x':0.3,'y':0.35} , font_style = "H4"))


        self.grid.add_widget(MDLabel(text ="Materials Used:", pos_hint = {'x':0.05,'y':0},  font_style = "H5", bold=True ))

        self.grid.add_widget(MDLabel(text="Motor", pos_hint={'x':0.1, 'y': -0.3}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Water pump", pos_hint={'x':.1, 'y': -.5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Circuit components", pos_hint={'x':.1, 'y': -.7}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Plastic chamber", pos_hint={'x':.1 ,'y': -.9}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Gear", pos_hint={'x':0.1, 'y': -1.1}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Pad", pos_hint={'x':0.1, 'y': -1.3}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Silicon pipes", pos_hint={'x':0.1, 'y': -1.5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Silica gel", pos_hint={'x':0.1, 'y': -1.7}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Model of collection vehicle", pos_hint={'x':0.1, 'y': -1.9}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Model of collection centre", pos_hint={'x':0.1, 'y': -2.1}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="Procedure/Description:", pos_hint={'x':0.05, 'y': -2.5}, font_style="H5", bold=True))
        self.grid.add_widget(MDLabel(text="The basic ideology behind this project is to create an atmosphere wherein used pads are treated and reused properly for various purposes. The model which is made is a miniature version of the real one. The following are the processes involved :-", pos_hint={'x':0.1, 'y': -3.5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="1.Collection of pads and transporting them to the models installed in certain areas depending on the location and availability of safe labor in that area.", pos_hint={'x':0.1, 'y': -4.4}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="2.Adding all pads in the unit.", pos_hint={'x':0.1, 'y': -5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="3.Washing the pads with salt solution for around 15mins this process would remove the blood absorbed by the super absorbent polymer(sap) in the napkins.", pos_hint={'x':0.1, 'y': -5.6}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="4.Draining out the blood dissolved water into the drainage .This blood would be treated at the water treatment plants.", pos_hint={'x':0.1, 'y': -6.3}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="5.The leftovers of the pads in the unit undergo spinning in order to dry them up.", pos_hint={'x':0.1, 'y': -6.9}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="6.Through a collection chamber these dried up pads which now only contain plastics[PE, PP ,PET] are further put to another process.", pos_hint={'x':0.1, 'y': -7.5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="7.This includes disinfecting the pads . The E beam sterilization would do the purpose.", pos_hint={'x':0.1, 'y': -8}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="8.Later these sterilized plastic are to be sent to recycling units.", pos_hint={'x':0.1, 'y': -8.5}, font_style="H6", bold=True))
        self.grid.add_widget(MDLabel(text="9.These recycling units would then convert the plastics to other usable forms.", pos_hint={'x': 0.1, 'y': -9}, font_style="H6", bold=True))


        self.box2.add_widget(self.sv)
        self.add_widget(self.box2)





    def exit(self, dt):
        self.dialog = MDDialog(
            text="Are you sure you want to leave?",
            buttons=[MDFlatButton(text="CANCEL", text_color="black", on_release=self.no),
                     MDFlatButton(text="YES", text_color="black", on_release=self.yes), ], )
        self.dialog.open()

    def back(self, instance):
        self.manager.current="win1"

    def yes(self, instance):
        SaniCare().get_running_app().stop()

    def no(self, instance):
        self.dialog.dismiss()



#################################################################################################################################################################
############################### MAIN APP #########################################################################################################################
class SaniCare(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.icon = 'logo.png'
        self._app_name = "SaniCare"
        sm = ScreenManager(transition = FadeTransition())
        sm.add_widget(winvid(name="winvid"))
        sm.add_widget(win1(name='win1'))
        sm.add_widget(win3(name= "win3"))
        sm.add_widget(win4(name="win4"))
        sm.add_widget(winvid(name ="winvid"))
        return sm

if __name__ == "__main__":
    SaniCare().run()



################################################################################################################################################################################
#############################################################################################################################################################################
################################## BYE BYE ##############################################################################################################################################
######################################################################################################### BYE BYE ###########################################################################
######################################################################################################################################################################################

