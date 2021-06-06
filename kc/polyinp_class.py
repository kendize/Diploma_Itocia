class PolyInp(object):
    def __init__(
        self, 
        X_Y_W_H, 
        text = "GUI", 
        Text_Size = 30, 
        Disabled_Text_Color = [0, 0, 0], 
        Disabled_Body_Color = [255, 255, 255], 
        Disabled_Border_Color = [0, 0, 0], 
        Border_Size = 1, 
        Enabled_Text_Color = [0, 0, 0], 
        Enabled_Body_Color = [255, 255, 255], 
        Enabled_Border_Color = [150, 0, 0], 
        position = False
        ):
        
        self.X_Y_W_H = X_Y_W_H
        self.position = position
        self.Disabled_Body_Color = Disabled_Body_Color
        self.Disabled_Border_Color = Disabled_Border_Color
        self.Disabled_Text_Color = Disabled_Text_Color

        self.Enabled_Body_Color = Enabled_Body_Color
        self.Enabled_Border_Color = Enabled_Border_Color
        self.Enabled_Text_Color = Enabled_Text_Color

        self.Border_Size = Border_Size
        self.text = text
        self.Text_Size = Text_Size
        self.Enabled_Text = Text((1, 1), self.text, self.Text_Size, self.Enabled_Text_Color)
        self.Disabled_Text = Text((1, 1), self.text, self.Text_Size, self.Disabled_Text_Color)