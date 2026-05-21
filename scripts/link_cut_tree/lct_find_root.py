import os
import sys
from manim import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from link_cut_tree.lct_base import LCTBaseScene
from splay_tree.splay_base import GREEN, RED, YELLOW, MUTED

class LCTFindRootScene(LCTBaseScene):
    def construct(self):
        title = self._section_title("LCT FindRoot(v)  —  Traversal & Zig-Zig Amortization", color=GREEN)
        self.play(Write(title, run_time=0.4))

        # Deep, unbalanced continuous chain representation inside an Aux Tree
        V_pos = [ 2.0,  2.2, 0]
        P_pos = [ 0.5,  1.0, 0]
        W_pos = [-1.0, -0.2, 0]
        A_pos = [-2.5, -1.4, 0] # This will be our target structural root

        n_v = self._node("v", V_pos)
        n_p = self._node("p", P_pos)
        n_w = self._node("w", W_pos)
        n_a = self._node("a", A_pos, color=RED)
        all_nodes = VGroup(n_v, n_p, n_w, n_a)

        e_vp = self._dynamic_solid(n_v, n_p)
        e_pw = self._dynamic_solid(n_p, n_w)
        e_wa = self._dynamic_solid(n_w, n_a)
        all_edges = VGroup(e_vp, e_pw, e_wa)

        b_chain = self._enclose(n_v, n_p, n_w, n_a)

        self.play(FadeIn(b_chain), FadeIn(all_edges), FadeIn(all_nodes))

        hint = self._hint("Step 1: Walk up leftmost spine of the capsule to extract structural root 'a'", YELLOW, title)
        self.play(FadeIn(hint))

        # Real-time search trajectory guide
        pt = Arrow(start=RIGHT*0.5, end=LEFT*0.5, color=RED).scale(0.5).next_to(n_v, RIGHT)
        self.play(FadeIn(pt))
        self.play(pt.animate.next_to(n_p, RIGHT), run_time=0.5)
        self.play(pt.animate.next_to(n_w, RIGHT), run_time=0.5)
        self.play(pt.animate.next_to(n_a, RIGHT), run_time=0.5)
        self.wait(0.4)
        self.play(FadeOut(pt))

        # ─── STEP 2: ZIG-ZIG DOUBLE ROTATION ───
        lbl2 = self._hint("Step 2: Splay(a) via Zig-Zig execution. Rebalances the deep spine completely.", YELLOW, title)
        self.play(ReplacementTransform(hint, lbl2), FadeOut(b_chain))

        # Symmetric balanced coordinate targets
        new_a = [ 0.0,  2.2, 0]
        new_w = [-1.5,  0.8, 0]
        new_p = [ 1.5,  0.8, 0]
        new_v = [ 2.5, -0.6, 0]

        # Everything transforms uniformly, keeping edges attached dynamically
        self.play(
            n_a.animate.move_to(new_a),
            n_w.animate.move_to(new_w),
            n_p.animate.move_to(new_p),
            n_v.animate.move_to(new_v),
            run_time=1.8,
            rate_func=smooth
        )

        b_rebalanced = self._enclose(n_a, n_w, n_p, n_v)
        self.play(FadeIn(b_rebalanced), run_time=0.4)

        lbl3 = self._hint("✓ Balanced! Spine depth halved, saving time on future operations.", GREEN, title)
        self.play(ReplacementTransform(lbl2, lbl3))
        self.play(self._pulse(n_a))
        self.wait(1.5)