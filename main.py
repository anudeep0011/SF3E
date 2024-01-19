from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel, MDIcon
from kivy.metrics import dp
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from twilio.rest import Client

import keys

Window.size = (360, 640)


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'first'
        label = MDLabel(text='SF3E', pos_hint={'center_x': 0.89, 'center_y': 0.5})
        label.font_name = 'Poppins-Mediumitalic.ttf'
        label.color = (1, 0, 0, 1)
        label.font_size = '30sp'
        self.add_widget(label)

    def on_enter(self, *args):
        Clock.schedule_once(self.change_screen, 3)

    def change_screen(self, *args):
        self.manager.current = 'main'


class scrollViewEample():
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'main'
        self.layout = GridLayout(cols=2, spacing=dp(20), padding=(dp(23), dp(71)))
        md_card1 = MDCard(elevation=3, radius=[10, ], on_press=self.instruction)
        md_card1.md_bg_color = get_color_from_hex('#808080')
        label1 = MDLabel(text='       Instruction', pos_hint={'center_x': 0.5, 'center_y': 0.2})
        md_card1.add_widget(label1)
        md_card1.height = dp(140)
        self.layout.add_widget(md_card1)

        # Create the second MDCard
        md_card2 = MDCard(elevation=3, radius=[10, ], on_press=self.register)
        md_card2.md_bg_color = get_color_from_hex('#808080')
        label2 = MDLabel(text='    Register number', pos_hint={'center_x': 0.5, 'center_y': 0.2})
        md_card2.add_widget(label2)
        md_card2.height = dp(140)
        self.layout.add_widget(md_card2)

        # Create the third MDCard
        md_card3 = MDCard(elevation=3, radius=[10, ],on_press=self.view)
        md_card3.md_bg_color = get_color_from_hex('#808080')
        label3 = MDLabel(text='     View Register\n         number', pos_hint={'center_x': 0.5, 'center_y': 0.2})
        md_card3.add_widget(label3)
        md_card3.height = dp(140)
        self.layout.add_widget(md_card3)

        # Create the fourth MDCard
        md_card4 = MDCard(elevation=3, radius=[10, ],on_press=self.clear)
        md_card4.md_bg_color = get_color_from_hex('#808080')
        label4 = MDLabel(text='    Delete  number', pos_hint={'center_x': 0.5, 'center_y': 0.2})
        md_card4.add_widget(label4)
        md_card4.height = dp(140)
        self.layout.add_widget(md_card4)

        # Create the fifth MDCard
        md_card5 = MDCard(elevation=3, radius=[10, ], on_press=self.Edit)
        md_card5.md_bg_color = get_color_from_hex('#808080')
        label5 = MDLabel(text='  Edit SF3E msg', pos_hint={'center_x': 0.5, 'center_y': 0.2})
        md_card5.add_widget(label5)
        md_card5.height = dp(140)
        self.layout.add_widget(md_card5)

        # Create the sixth MDCard
        md_card6 = MDCard(elevation=3, radius=[10, ],on_press=self.viewm)
        md_card6.md_bg_color = get_color_from_hex('#808080')
        label6 = MDLabel(text='      view SF3E msg', pos_hint={'center_x': 0.5, 'center_y': 0.2})
        md_card6.add_widget(label6)
        md_card6.height = dp(140)
        self.layout.add_widget(md_card6)

        next_button = MDRaisedButton(text="Next", pos_hint={'center_x': 0.89, 'center_y': 0.065})
        next_button.bind(on_press=self.Next)

        self.add_widget(next_button)



        self.add_widget(self.layout)

    def instruction(self, *args):
        self.manager.current = 'inst'

    def register(self, *args):
        self.manager.current = 'regi'

    def view(self,*args):
        self.manager.current = 'view'

    def clear(self,*args):
        self.manager.current = 'clear'

    def Edit(self,*args):
        self.manager.current = 'Edit'

    def viewm(self, *args):
        self.manager.current = 'viewm'

    def Next(self, *args):
        self.manager.current = 'Next'

        


class NextScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Next'
        self.layout = BoxLayout(orientation='horizontal', spacing=dp(100), padding=(dp(100), dp(100)))

        md_card1 = MDCard(elevation=5, radius=[15, ], size_hint=(0.3, 0.3),pos_hint={'center_x': 0.5, 'center_y': 0.5},on_press=self.send_message)

        md_card1.md_bg_color = get_color_from_hex('#FF0000')
        label1 = MDLabel(text='              SF3E', pos_hint={'center_x': 0.6, 'center_y': 0.5})


        md_card1.add_widget(label1)
        md_card1.height = dp(100)

        self.layout.add_widget(md_card1)
        self.add_widget(self.layout)
        back_button = MDRaisedButton(
            text="Back",
            on_release=self.go_back,
            pos_hint={'center_x': 0.1, 'center_y': 0.97}
        )

        self.add_widget(back_button)
    def go_back(self,*args):
        self.manager.current = 'main'

    def send_message(self, instance):
        keys = {
            'account_sid1': 'AC20ff294bf1e3d6a3fa6209d87ea9b8d5',
            'auth_token1': '86cf5c5160c3be1ba0eb0073af9f9ce9',
            'twilio_number1': '+14027266274',
            'target_number1': self.manager.get_screen('view').label4.text,
            'account_sid2': 'AC6aa5b5577b98723a8d99b20e2e85728a',
            'auth_token2': '16358038e78a6545e8f307c723fac809',
            'twilio_number2': '+14065211364',
            'target_number2': self.manager.get_screen('view').label1.text,
            'account_sid3': 'AC91f1fe24201881d45584a7aa1060d448',
            'auth_token3': '50903c0fd87bfe5363ca5394185bb24d',
            'twilio_number3': '+14068023171',
            'target_number3': '+919133012672',
            'account_sid4': 'ACba142ba1d56aee77787067df9511673a',
            'auth_token4': '3dd6b97e96b65f60f4604ca164277759',
            'twilio_number4': '+114068023162',
            'target_number4': '+917416257302',

        }

        client1 = Client(keys['account_sid1'], keys['auth_token1'])
        client2 = Client(keys['account_sid2'], keys['auth_token2'])
        client3 = Client(keys['account_sid3'], keys['auth_token3'])
        client4 = Client(keys['account_sid4'], keys['auth_token4'])



        message1 = client1.messages.create(
            body=self.manager.get_screen('viewm').label1.text+'https://goo.gl/maps/XGhNJ2S5y5T7YpyCA',
            from_=keys['twilio_number1'],
            to=keys['target_number1']
        )
        message2 = client2.messages.create(
            body=self.manager.get_screen('viewm').label1.text+'https://goo.gl/maps/XGhNJ2S5y5T7YpyCA',
            from_=keys['twilio_number2'],
            to=keys['target_number2']
        )
        message3 = client3.messages.create(
            body=self.manager.get_screen('viewm').label1.text+'https://goo.gl/maps/XGhNJ2S5y5T7YpyCA',
            from_=keys['twilio_number3'],
            to=keys['target_number3']
        )
        message4 = client4.messages.create(
            body=self.manager.get_screen('viewm').label1.text+'https://goo.gl/maps/XGhNJ2S5y5T7YpyCA',
            from_=keys['twilio_number4'],
            to=keys['target_number4']
        )

        print(message1.body)
        print(message2.body)
        print(message3.body)
        print(message4.body)


class InstructionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'inst'

        label = MDLabel(text="                    ******INSTRUCTIONS*****\n"
                        "                           ---------SF3E---------\n\n\n"


                             " Installation: Download and install the SF3E Emergency App from your devices app store.\n"
                             " Registration: Launch the SF3E Emergency App and complete the registration process. Provide your personal details, such as name, contact information, and any medical information you want to share.\n"
                             "SOS Activation: In case of an emergency, locate and tap the SF3E button within the app's interface. This action will initiate the emergency alert process.\n"
                             "Alert Recipients: The SF3E Emergency App will automatically notify your pre-registered emergency contacts about the emergency situation. These contacts may include family members, friends, or local authorities.\n"
                             "Location Sharing: The app will also transmit your current location to the designated emergency contacts. This information will assist them in quickly locating and providing help.\n"
                             "Emergency Services: In critical situations, the SF3E Emergency App can directly contact emergency services, such as police, fire department.\n"
                             "Confirmation and Communication: The app will provide a confirmation message once the SF3E alert has been sent. Additionally, it may enable a communication channel between you and the emergency contacts to exchange vital information.\n"
                             "Safe Zones: SF3E Emergency App allows you to set up safe zones, such as your home or workplace, where emergency alerts are not triggered. This feature prevents false alarms within familiar and secure environments.\n"
                             "Edit SOS Message: You can customize the SF3E message within the app settings. This message should provide essential information about the emergency, such as your name, nature of the emergency, and any specific instructions for the recipients.\n"
                             "App Ratings: Share your feedback and rate the SF3E Emergency App on the app store. Your ratings and reviews help us improve the app and provide better assistance during emergencies.,\n",
                        size_hint=(1, None), height=dp(1000))
        sv = ScrollView(size_hint_y=.98)
        sv.add_widget(label)
        self.add_widget(sv)

        back_button = MDRaisedButton(
            text="Back",
            on_release=self.go_back,
            pos_hint={'center_x': 0.1, 'center_y': 0.97}
        )

        self.add_widget(back_button)

    def go_back(self, *args):
        self.manager.current = 'main'


class RegisterScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'regi'
        self.label = MDLabel(text='Register Number',pos_hint={'center_x':0.65,'center_y':0.85})
        self.label.font_name = 'Poppins-Bold.ttf'
        self.label.font_size = '30sp'
        self.add_widget(self.label)
        self.start_point_box = BoxLayout(
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            padding=(2, 2, 2, 2),  # Set the padding for the border
            spacing=2  # Set the spacing for the border
        )
        self.input_lang = MDTextField(
            hint_text="Enter your second Number",
            mode="rectangle",
            icon_right="contacts",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height=dp(48)

        )
        self.start_point_box.add_widget(self.input_lang)

        self.end_point_box = BoxLayout(
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            padding=(2, 2, 2, 2),  # Set the padding for the border
            spacing=2  # Set the spacing for the border
        )
        self.output_lang = MDTextField(
            hint_text="Enter your third Number",
            mode="rectangle",
            icon_right="contacts",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height=dp(48)
        )
        self.end_point_box.add_widget(self.output_lang)

        self.start_point_box1 = BoxLayout(
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            padding=(2, 2, 2, 2),  # Set the padding for the border
            spacing=2  # Set the spacing for the border
        )
        self.input_lang1 = MDTextField(
            hint_text="Enter your fourth Number",
            mode="rectangle",
            icon_right="contacts",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height=dp(48)

        )
        self.start_point_box1.add_widget(self.input_lang1)

        self.end_point_box1 = BoxLayout(
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},
            padding=(2, 2, 2, 2),  # Set the padding for the border
            spacing=2  # Set the spacing for the border
        )
        self.output_lang1 = MDTextField(
            hint_text="Enter your first Number",
            mode="rectangle",
            icon_right="contacts",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height=dp(48)
        )
        back_button = MDRaisedButton(
            text="Back",
            on_release=self.go_back,
            pos_hint={'center_x': 0.1, 'center_y': 0.97}
        )

        self.add_widget(back_button)

        save_button = MDRaisedButton(text="Save", pos_hint={'center_x': 0.5, 'center_y': 0.1})
        save_button.bind(on_press=self.view)
        self.end_point_box1.add_widget(self.output_lang1)
        self.add_widget(self.start_point_box)
        self.add_widget(self.end_point_box)
        self.add_widget(self.start_point_box1)
        self.add_widget(self.end_point_box1)
        self.add_widget(save_button)


    def view(self,*args):

        text1 = self.input_lang.text
        text2 = self.input_lang1.text
        text3=self.output_lang.text
        text4 = self.output_lang1.text
        self.manager.get_screen('view').update_label(text1,text2,text3,text4)
        self.manager.get_screen('clear').update_labels(text1, text2, text3, text4)
        self.manager.current = 'main'



    def go_back(self,*args):
        self.manager.current = 'main'

class ViewScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.name = 'view'
        self.label = MDLabel(text='View Registered Numbers', pos_hint={'center_x': 0.65, 'center_y': 0.85})
        self.label.font_name = 'Poppins-Bold.ttf'
        self.label.font_size = '20sp'
        self.add_widget(self.label)
        self.label1 = MDLabel(text='', pos_hint={'center_x': 0.8, 'center_y': 0.7})
        self.label2 = MDLabel(text='', pos_hint={'center_x': 0.8, 'center_y': 0.6})
        self.label3 = MDLabel(text='', pos_hint={'center_x': 0.8, 'center_y': 0.5})
        self.label4 = MDLabel(text='', pos_hint={'center_x': 0.8, 'center_y': 0.4})
        self.add_widget(self.label1)
        self.add_widget(self.label2)
        self.add_widget(self.label3)
        self.add_widget(self.label4)

        back_button = MDRaisedButton(
            text="Back",
            on_release=self.go_back,
            pos_hint={'center_x': 0.1, 'center_y': 0.97}
        )

        self.add_widget(back_button)

    def update_label(self, text1, text2, text3, text4):
        self.label1.text = text1
        self.label2.text = text2
        self.label3.text = text3
        self.label4.text = text4

    def go_back(self,*args):
        self.manager.current = 'main'

class ClearScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.name = 'clear'
        self.label1 = MDLabel(text='', pos_hint={'center_x': 0.8, 'center_y': 0.7})
        self.label2 = MDLabel(text='', pos_hint={'center_x': 0.8, 'center_y': 0.6})
        self.label3 = MDLabel(text='', pos_hint={'center_x': 0.8, 'center_y': 0.5})
        self.label4 = MDLabel(text='', pos_hint={'center_x': 0.8, 'center_y': 0.4})
        self.add_widget(self.label1)
        self.add_widget(self.label2)
        self.add_widget(self.label3)
        self.add_widget(self.label4)

        self.clear_button = MDRaisedButton(
            text='clear',
            pos_hint={'center_x': 0.5, 'center_y': 0.3}
        )
        back_button = MDRaisedButton(
            text="Back",
            on_release=self.clear,
            pos_hint={'center_x': 0.1, 'center_y': 0.97}
        )

        self.add_widget(back_button)
        self.clear_button.bind(on_release=self.clear_labels)
        self.add_widget(self.clear_button)

    def update_labels(self, text1, text2, text3, text4):
        self.label1.text = text1
        self.label2.text = text2
        self.label3.text = text3
        self.label4.text = text4

    def clear_labels(self, *args):
        self.label1.text = ''
        self.label2.text = ''
        self.label3.text = ''
        self.label4.text = ''

    def clear(self,*args):
        self.manager.current = 'main'
class EditScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'Edit'
        self.label = MDLabel(
            text='Edit SF3E Message',
            pos_hint={'center_x': 0.8, 'center_y': 0.75},
            font_name='Poppins-Bold.ttf',
            font_size='70sp'
        )
        self.add_widget(self.label)

        self.start_point_box = BoxLayout(
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            padding=(2, 2, 2, 2),  # Set the padding for the border
            spacing=2  # Set the spacing for the border
        )

        self.output_lang1 = MDTextField(
            hint_text="Enter your Alert Message!",
            mode="rectangle",
            icon_right="message",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height=dp(48)
        )
        self.start_point_box.add_widget(self.output_lang1)

        back_button = MDRaisedButton(
            text="Back",
            on_release=self.go_back,
            pos_hint={'center_x': 0.1, 'center_y': 0.97}
        )
        self.add_widget(back_button)

        save_button = MDRaisedButton(
            text="Save",
            pos_hint={'center_x': 0.5, 'center_y': 0.1}
        )

        save_button.bind(on_press=self.viewm)

        self.add_widget(self.start_point_box)
        self.add_widget(save_button)


    def viewm(self, *args):
        text1 = self.output_lang1.text
        self.manager.get_screen('viewm').update_label(text1)
        self.manager.current = 'main'


    def go_back(self, instance):
        # Add the logic to go back to the previous screen
        self.manager.current = 'main'



class ViewMsgScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'viewm'
        self.label1 = MDLabel(text='', pos_hint={'center_x': 0.8, 'center_y': 0.7})
        self.label = MDLabel(text='View SF3E message', pos_hint={'center_x': 0.65, 'center_y': 0.85})
        self.add_widget(self.label1)

        back_button = MDRaisedButton(
            text="Back",
            on_release=self.go_back,
            pos_hint={'center_x': 0.1, 'center_y': 0.97}
        )

        self.add_widget(back_button)


    def update_label(self, text1):
        self.label1.text = text1

    def go_back(self, *args):
        self.manager.current = 'main'

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'

        # Create a screen manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(FirstScreen(name='first'))
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(InstructionScreen(name='inst'))
        screen_manager.add_widget(RegisterScreen(name='regi'))
        screen_manager.add_widget(ViewScreen(name='view'))
        screen_manager.add_widget(ClearScreen(name='clear'))
        screen_manager.add_widget(EditScreen(name='Edit'))
        screen_manager.add_widget(ViewMsgScreen(name='viewm'))
        screen_manager.add_widget(NextScreen(name='Next'))
        return screen_manager


# Run the app
if __name__ == '__main__':
    MyApp().run()
