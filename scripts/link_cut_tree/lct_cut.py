import os
import sys
from manim import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from link_cut_tree.lct_base import LCTBaseScene
from splay_tree.splay_base import GREEN, RED, YELLOW, BLUE

class LCTCutScene(LCTBaseScene):
    def construct(self):
        title = self._section_title("LCT Cut(u, v)  —  Component Severance", color=GREEN)
        self.play(Write(title, run_time=0.4))

        # Combined initial setup sharing a continuous path capsule
        V_pos = [ 0.0,  2.0, 0]
        U_pos = [-2.0,  0.5, 0]
        A_pos = [-3.5, -1.0, 0]
        B_pos = [ 2.0,  0.5, 0]

        n_v = self._node("v", V_pos, color=RED)
        n_u = self._node("u", U_pos, color=BLUE)
        n_a = self._node("a", A_pos)
        n_b = self._node("b", B_pos)

        e_vu = self._dynamic_solid(n_v, n_u)
        e_ua = self._dynamic_solid(n_u, n_a)
        e_vb = self._dynamic_dashed(n_v, n_b)
        
        b_vua = self._enclose(n_v, n_u, n_a)
        b_b   = self._enclose(n_b)

        self.play(
            FadeIn(VGroup(b_vua, b_b)), 
            FadeIn(VGroup(e_vu, e_ua, e_vb)), 
            FadeIn(VGroup(n_v, n_u, n_a, n_b))
        )

        hint = self._hint("Goal: Isolate and sever the solid link connecting v and u", YELLOW, title)
        self.play(FadeIn(hint))
        self.wait(0.8)

        # ─── BREAK LINK & CHOP ───
        lbl1 = self._hint("Step 1: Destroy structural link. The continuous path capsule splits into two.", YELLOW, title)
        self.play(ReplacementTransform(hint, lbl1), FadeOut(b_vua))

        # Erase tracking connector
        self.play(FadeOut(e_vu), run_time=0.4)

        # New separate boundaries
        b_v_isolated = self._enclose(n_v)
        b_ua_isolated = self._enclose(n_u, n_a)
        self.play(FadeIn(VGroup(b_v_isolated, b_ua_isolated)), run_time=0.4)
        self.wait(0.5)

        # ─── PHYSICAL DRIFT SEPARATION ───
        lbl2 = self._hint("Step 2: Physically move isolated subtrees apart to complete visual separation", GREEN, title)
        self.play(ReplacementTransform(lbl1, lbl2), FadeOut(VGroup(b_v_isolated, b_ua_isolated, b_b)))

        # Drift detached components away safely
        self.play(
            n_u.animate.shift(LEFT * 1.5 + DOWN * 0.5),
            n_a.animate.shift(LEFT * 1.5 + DOWN * 0.5),
            n_v.animate.shift(RIGHT * 0.5),
            n_b.animate.shift(RIGHT * 0.5),
            run_time=1.4,
            rate_func=smooth
        )

        # Wrap final separate components up beautifully
        b_final_v = self._enclose(n_v)
        b_final_ua = self._enclose(n_u, n_a)
        b_final_b = self._enclose(n_b)

        self.play(FadeIn(VGroup(b_final_v, b_final_ua, b_final_b)), run_time=0.5)
        self.play(self._pulse(n_v), self._pulse(n_u))
        self.wait(1.5)