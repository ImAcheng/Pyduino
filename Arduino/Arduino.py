from time import sleep

import pygame
import enum
import threading

__py_window__: pygame.Surface = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pyduino Indev 1.0.0")

class ArduinoEnums(enum.Enum):
    LOW = 0
    HIGH = 1
    OUTPUT = 2
    INPUT = 3

class ArduinoMain:
    def __init__(self, SetupMethod, LoopMethod):
        # Arduino Component
        self.AdnComp = ArduinoComponent()
        self.unoBoard = self.AdnComp.UnoBoard()

        self.setupMethod = SetupMethod
        self.loopMethod = LoopMethod

        self.InputPins: set = set()
        self.OutPutPins: set = set()

        # python stuff
        self.window: pygame.Surface = __py_window__
        self.running: bool = True
        self.ArduinoThread = threading.Thread(target=self.ArduinoProcess)
        self.StopEvent = threading.Event()
        # ------------

    def Run(self):
        self.setupMethod()
        self.ArduinoThread.start()

        while self.running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
                    self.StopEvent.set()
                    self.ArduinoThread.join()

            pygame.display.flip()
            self.window.fill((100, 100, 100))
            self.unoBoard.draw()

    def ArduinoProcess(self):
        while self.running:
            self.loopMethod()

    def SetMode(self, PinNumber: int, Mode: ArduinoEnums):
        if Mode == ArduinoEnums.INPUT and PinNumber not in self.InputPins:
            self.InputPins.add(PinNumber)

            if PinNumber in self.OutPutPins: self.OutPutPins.remove(PinNumber)

        elif Mode == ArduinoEnums.OUTPUT and PinNumber not in self.InputPins:
            self.OutPutPins.add(PinNumber)

            if PinNumber in self.InputPins: self.InputPins.remove(PinNumber)

        else:
            raise f"[Error] Unknown Mode \"{Mode}\". Must be \"INPUT\" or \"OUTPUT\""

    def delay(self, milSeconds: int):
        sleep(milSeconds*0.001)


"""
dataType:
    digital = 0
    analog = 1
"""
class ArduinoComponent:
    class UnoBoard:
        def __init__(self):
            self.Board = pygame.Surface((600, 480))
            self.Board.fill((0, 100, 0))
            self.rect = self.Board.get_rect()
            self.rect.center = (1280/2, 720/2)

        def draw(self):
            __py_window__.blit(self.Board, self.rect)

    class SingleLED:
        def __init__(self, PinNumer: int, Color: tuple = (255, 0, 0)):
            self.dataType = 0
            self.input_data: bool = 0

        def draw(self):
            ...


class SerialCode:
    def __init__(self):
        ...

    def print(self, string: str):
        print(string, end='')

    def println(self, string: str):
        print(string)