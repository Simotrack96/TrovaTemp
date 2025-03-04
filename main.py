from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest

class TrovaTemperatura(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols= 1 
        self.window.size_hint = (0.8, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        Window.size = (360, 640)

        self.window.add_widget(Image(source = "logo.png"))
        
        self.input_testo= TextInput(
            size_hint= (1, 0.2),
            font_size= "20sp",
            padding_y= "12sp",
            halign="center"
        )
        self.window.add_widget(self.input_testo)
        
        self.bottone= Button(
            text= "VIA!",
            size_hint= (1, 0.2),
            bold= True,
            background_color="#0099ff"
            )
        self.window.add_widget(self.bottone)
        self.bottone.bind(on_press=self.trova_temp)
        
        self.etichetta= Label(
            text= "Cerca una città :-)",
            font_size= "20sp",
            color="#007dd1"
            )
        self.window.add_widget(self.etichetta)
        
        return self.window
    
    def trova_temp(self, instance):
        def edit_label(request, result):
            temp= result["main"]["temp"]
            self.etichetta.text= f"Oggi a {self.input_testo.text} ci sono {temp} °C"
        link= f"https://api.openweathermap.org/data/2.5/weather?q={self.input_testo.text}&appid=c573256deb55c517fea35d848bb1a9c9&units=metric"
        UrlRequest(link, edit_label)

TrovaTemperatura().run() #per avviare app