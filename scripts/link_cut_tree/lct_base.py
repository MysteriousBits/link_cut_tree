import os
import sys
from manim import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from splay_tree.splay_base import SplayBaseScene

SOLID_COLOR = "#4cc9f0"  
DASHED_COLOR = "#7B7B9A" 
BOUND_COLOR = "#6B7280"

class LCTBaseScene(SplayBaseScene):
    """Extends SplayBaseScene with fully reactive dynamic structural links."""
    
    def _dynamic_solid(self, node_a, node_b):
        """Creates a solid edge that perfectly tracks node positions in real-time."""
        return always_redraw(
            lambda: Line(
                node_a.get_center(), 
                node_b.get_center(), 
                stroke_width=4.0, 
                color=SOLID_COLOR, 
                buff=0.38
            )
        )

    def _dynamic_dashed(self, node_a, node_b):
        """Creates a dashed path-parent pointer that tracks node positions in real-time."""
        return always_redraw(
            lambda: DashedLine(
                node_a.get_center(), 
                node_b.get_center(), 
                stroke_width=2.5, 
                dash_length=0.15, 
                color=DASHED_COLOR, 
                buff=0.38
            )
        )

    def _lazy_badge(self, node, text="[Flipped]"):
        return Text(text, font_size=11, color="#ffd166").next_to(node, UR, buff=0.05)

    def _enclose(self, *mobjects, buff=0.45):
        """Wraps an auxiliary tree path component in its own isolated dotted capsule."""
        group = VGroup(*mobjects)
        rect = SurroundingRectangle(
            group, 
            color=BOUND_COLOR, 
            stroke_width=2.0, 
            buff=buff, 
            corner_radius=0.4
        )
        return DashedVMobject(rect, num_dashes=45, dashed_ratio=0.6)
    
