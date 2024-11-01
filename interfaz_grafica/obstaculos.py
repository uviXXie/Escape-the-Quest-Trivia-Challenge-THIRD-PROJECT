import time
import threading
from personajes import Gallina

class obstaculos(Gallina):
    
    def __init__(self, x, y, animations) -> None:
        super().__init__(x, y, animations)
        

