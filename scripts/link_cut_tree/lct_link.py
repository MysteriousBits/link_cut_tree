import os
import sys
from manim import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from link_cut_tree.lct_base import LCTBaseScene
from splay_tree.splay_base import GREEN, RED, YELLOW, BLUE

class LCTLinkScene(LCTBaseScene):
    def construct(self):
        title = self._section_title("LCT Link(u, v)  —  Component Forest Merge", color=GREEN)
        self.play(Write(title, run_time=0.4))

        # TREE COMPONENT 1 (Left Forest Network)
        U = [-3.0,  1.0, 0]; A = [-4.2, -0.5, 0]; B = [-1.8, -0.5, 0]
        n_u = self._node("u", U, color=RED); n_a = self._node("a", A); n_b = self._node("b", B)
        e_ua = self._dynamic_solid(n_u, n_a); e_ub = self._dynamic_dashed(n_u, n_b)
        b_u = self._enclose(n_u, n_a); b_b = self._enclose(n_b)

        # TREE COMPONENT 2 (Right Forest Network)
        V = [ 3.0,  1.0, 0]; C = [ 1.8, -0.5, 0]; D = [ 4.2, -0.5, 0]
        n_v = self._node("v", V, color=BLUE); n_c = self._node("c", C); n_d = self._node("d", D)
        e_vc = self._dynamic_solid(n_v, n_c); e_vd = self._dynamic_dashed(n_v, n_d)
        b_v = self._enclose(n_v, n_c); b_d = self._enclose(n_d)

        self.play(
            FadeIn(VGroup(b_u, b_b, b_v, b_d)),
            FadeIn(VGroup(e_ua, e_ub, e_vc, e_vd)),
            FadeIn(VGroup(n_u, n_a, n_b, n_v, n_c, n_d))
        )
        
        hint = self._hint("Goal: Form a cross-component bridge by making u a child of v", BLUE, title)
        self.play(FadeIn(hint))
        self.wait(0.8)

        # ─── PHYSICAL MERGE MOVEMENT ───
        lbl1 = self._hint("Step 1: Bring subtrees closer to establish space for the new bridge", YELLOW, title)
        self.play(ReplacementTransform(hint, lbl1), FadeOut(VGroup(b_u, b_b, b_v, b_d)))

        # Shift whole networks towards each other dynamically
        self.play(
            n_u.animate.shift(RIGHT * 1.2), n_a.animate.shift(RIGHT * 1.2), n_b.animate.shift(RIGHT * 1.2),
            n_v.animate.shift(LEFT * 1.2),  n_c.animate.shift(LEFT * 1.2),  n_d.animate.shift(LEFT * 1.2),
            run_time=1.2
        )

        # Attach dynamic bridging line natively
        e_bridge = self._dynamic_dashed(n_u, n_v)
        self.play(Create(e_bridge), run_time=0.6)

        # Redraw isolated structural boundaries
        b_u_new = self._enclose(n_u, n_a)
        b_b_new = self._enclose(n_b)
        b_v_new = self._enclose(n_v, n_c)
        b_d_new = self._enclose(n_d)
        
        lbl2 = self._hint("✓ Linked! Dashed bridge connects separate components seamlessly.", GREEN, title)
        self.play(ReplacementTransform(lbl1, lbl2), FadeIn(VGroup(b_u_new, b_b_new, b_v_new, b_d_new)))
        self.play(self._pulse(n_u), self._pulse(n_v))
        self.wait(1.5)