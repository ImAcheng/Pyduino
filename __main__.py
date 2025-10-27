# This is where you code

from Arduino import *

class Main:
    def __init__(self):
        self.Arduino = ArduinoMain(self.Setup, self.Loop)
        self.Arduino.Run()

    # Please put all your setup code here.
    def Setup(self):
        pass

    # Please put all your code here to update every frame.
    def Loop(self):
        Serial.print("Test for print ")
        Serial.println("Test for ln")
        self.Arduino.delay(1000)

main = Main()