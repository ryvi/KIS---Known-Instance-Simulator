from Framework.General.Position import Position
from Framework.Characters.Actor import Actor


class Event:
    source = Actor()
    target = Actor()
    duration = 0  # ms

    def __init__(self, source, target):
        self.source = source
        self.target = target
