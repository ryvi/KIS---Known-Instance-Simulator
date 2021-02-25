import Framework.General
from Framework.General.Position import Position


class Character:
    model_img_dir = ""
    position = Position(0,0)

    def __init__(self):
        self.model_dir = "Images/Characters/Tank_Icon.png"
