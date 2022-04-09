from manim import *
import numpy as np

class MScene(Scene):
    mConfig = {
        "subfile" : open("Subtitles/SLess.txt", mode="rt", encoding='utf-8' ),
        "FSD" : 30,
        "MAXS" : 35
        }
    def debug(self):
        self.dCoords()

    def default(self):
        line = Line(start=np.array([-8, -2.5, 0]), end=np.array([9, -2.5, 0]))
        self.play(Create(line))

    def dGraph(self, obj):
        for i in obj:
            self.play(Create(i), run_time=1)

    def dCoords(self, sx=-7, ex=8, sy=-4, ey=4):
        for x in range(sx, ex):
            for y in range(sy, ey):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY))
    
    def dSt(self):
        stext = self.mConfig["subfile"].readline()
        stext1 = stext[:self.mConfig["MAXS"]]
        stext2 = stext[self.mConfig["MAXS"]:]
        st1 = Text(stext1, font_size=self.mConfig["FSD"]).shift(np.array([0, -3, 0]))
        st2 = Text(stext2, font_size=self.mConfig["FSD"]).next_to(st1, DOWN)
        stal = VGroup(st1, st2)
        self.play(Write(stal))