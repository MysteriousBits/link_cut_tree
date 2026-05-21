from manim import *
import numpy as np

# ─── Colour palette ───────────────────────────────────────────────────────────
BG       = "#0d0d1a"   
BLUE     = "#4cc9f0"   
GREEN    = "#06d6a0"   
YELLOW   = "#ffd166"   
RED      = "#f72585"   
MUTED    = "#7B7B9A"   
EDGE_COL = "#3a3a5c"   

class SplayBaseScene(Scene):
    """Base scene containing all visual helper methods."""
    
    def setup(self):
        self.camera.background_color = BG

    @staticmethod
    def _v3(pos):
        a = np.array(pos, dtype=float)
        return a if a.shape == (3,) else np.append(a, 0.0)

    def _node(self, label: str, pos, color=BLUE, r: float = 0.38):
        pos = self._v3(pos)
        circle = (
            Circle(r, color=color, fill_color=color,
                   fill_opacity=0.18, stroke_width=2.5)
            .move_to(pos)
        )
        text = Text(label, font_size=21, color=WHITE, weight=BOLD).move_to(pos)
        return VGroup(circle, text)

    def _edge(self, a, b):
        a, b = self._v3(a), self._v3(b)
        d = normalize(b - a)
        r = 0.38
        return Line(a + d * r, b - d * r, stroke_width=1.8, color=EDGE_COL)

    def _section_title(self, text: str, color=WHITE):
        t = Text(text, font_size=28, weight=BOLD, color=color)
        t.to_edge(UP, buff=0.32)
        return t

    def _hint(self, text: str, color, anchor):
        return Text(text, font_size=18, color=color).next_to(anchor, DOWN, buff=0.2)

    def _pulse(self, node):
        return Succession(
            node[0].animate(run_time=0.18).set_stroke(width=6),
            node[0].animate(run_time=0.18).set_stroke(width=2.5),
        )