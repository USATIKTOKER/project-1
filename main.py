from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from time import strftime

class ClockApp(App):

    def update_time(self, *args):
        current_time = strftime('%H:%M')
        self.time_label.text = current_time

    def build(self):
        self.root = Label(text=strftime('%H:%M'), font_size=80, bold=True, color=[1, 1, 1, 1])
        Clock.schedule_interval(self.update_time, 60)  # Update every minute
        return self.root

if __name__ == '__main__':
    ClockApp().run()
