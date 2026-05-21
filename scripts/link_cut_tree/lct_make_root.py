import os
import sys
from manim import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from link_cut_tree.lct_base import LCTBaseScene
from splay_tree.splay_base import GREEN, RED, YELLOW

class LCTMakeRootScene(LCTBaseScene):
    def construct(self):
        title = self._section_title("LCT MakeRoot(v)  —  Path Topology Inversion", color=GREEN)
        self.play(Write(title, run_time=0.4))

        # Initial left-heavy path component
        W_pos = [ 1.5,  2.0, 0]
        P_pos = [ 0.0,  0.5, 0]
        V_pos = [-1.5, -1.0, 0]

        n_w = self._node("w", W_pos)
        n_p = self._node("p", P_pos)
        n_v = self._node("v", V_pos, color=RED)
        
        e_wp = self._dynamic_solid(n_w, n_p)
        e_pv = self._dynamic_solid(n_p, n_v)
        
        b_curr = self._enclose(n_w, n_p, n_v)
        self.play(FadeIn(b_curr), FadeIn(VGroup(e_wp, e_pv)), FadeIn(VGroup(n_w, n_p, n_v)))

        hint = self._hint("Step 1: Splay(v) brings target node to the top of its local path capsule", YELLOW, title)
        self.play(FadeIn(hint))
        self.wait(0.6)

        # ─── PHYSICAL SPLAY TO TOP ───
        self.play(FadeOut(b_curr), run_time=0.2)
        splay_v = [ 0.0,  2.0, 0]
        splay_p = [ 1.2,  0.5, 0]
        splay_w = [ 2.4, -1.0, 0]

        self.play(
            n_v.animate.move_to(splay_v),
            n_p.animate.move_to(splay_p),
            n_w.animate.move_to(splay_w),
            run_time=1.2
        )
        b_splayed = self._enclose(n_v, n_p, n_w)
        self.play(FadeIn(b_splayed))
        self.wait(0.5)

        # ─── LAZY TAG FLIP ───
        lbl2 = self._hint("Step 2: Commit a Lazy Inversion Tag to reverse sequence direction", YELLOW, title)
        self.play(ReplacementTransform(hint, lbl2))
        
        badge = self._lazy_badge(n_v)
        self.play(FadeIn(badge), self._pulse(n_v))
        self.wait(0.6)

        # Physically reverse/mirror layout positions to display sequence inversion
        lbl3 = self._hint("✓ Sequence flipped. Node v is now the true structural root.", GREEN, title)
        self.play(ReplacementTransform(lbl2, lbl3), FadeOut(b_splayed), run_time=0.4)

        flip_v = [ 0.0,  2.0, 0]
        flip_p = [-1.2,  0.5, 0]
        flip_w = [-2.4, -1.0, 0]

        self.play(
            n_v.animate.move_to(flip_v),
            badge.animate.next_to(flip_v, UR, buff=0.05),
            n_p.animate.move_to(flip_p),
            n_w.animate.move_to(flip_w),
            run_time=1.4,
            rate_func=smooth
        )
        
        b_final = self._enclose(n_v, n_p, n_w)
        self.play(FadeIn(b_final))
        self.wait(1.5)