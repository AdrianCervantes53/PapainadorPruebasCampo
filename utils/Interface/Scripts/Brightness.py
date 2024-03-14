import screen_brightness_control as sbc

class Brisho():
    def __init__(self):
        self.val = sbc.get_brightness()

    def updateSlider(self, slider):
        slider.setValue(self.val[0])
    
    def updateValue(self, slider):
        value = slider.value()
        sbc.set_brightness(value)