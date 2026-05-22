import os
import sys
from manim import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from link_cut_tree.lct_base import LCTBaseScene
from splay_tree.splay_base import GREEN, RED, YELLOW, MUTED

class LCTMakeRootScene(LCTBaseScene):
    def construct(self):
        title = self._section_title("LCT MakeRoot(v)  —  Path Topology Inversion", color=GREEN)
        self.play(Write(title, run_time=0.4))

        # ─── INITIAL STATE ───
        # p is the parent, w is its left child (shallower), v is its right child (deeper)
        # Shifted down on the Y-axis to guarantee plenty of header space
        P_pos = [ 0.0,  1.0, 0]
        W_pos = [-1.5, -0.4, 0]
        V_pos = [ 1.5, -0.4, 0] # Target node (RED)

        n_p = self._node("p", P_pos)
        n_w = self._node("w", W_pos)
        n_v = self._node("v", V_pos, color=RED)
        all_nodes = VGroup(n_p, n_w, n_v)

        # All nodes are on the same preferred path, so links are solid
        e_pw = self._dynamic_solid(n_p, n_w)
        e_pv = self._dynamic_solid(n_p, n_v)
        all_edges = VGroup(e_pw, e_pv)
        
        b_curr = self._enclose(n_p, n_w, n_v)
        self.play(FadeIn(b_curr), FadeIn(all_edges), FadeIn(all_nodes), run_time=0.8)

        hint = self._hint("Goal: Invert the path sequence so that the deepest node v becomes the root", RED, title)
        self.play(FadeIn(hint), self._pulse(n_v))
        self.wait(0.8)

        # ─── STEP 1: LEFT ROTATION (ZAG) ───
        lbl1 = self._hint("Step 1: Splay(v) via Left Rotation (Zag). v rotates above parent p.", YELLOW, title)
        self.play(ReplacementTransform(hint, lbl1), FadeOut(b_curr))

        # Structural Splay Targets: v becomes root, p drops to its left child, w stays left child of p
        splay_v = [ 0.0,  1.0, 0]
        splay_p = [-1.5, -0.4, 0]
        splay_w = [-2.5, -1.8, 0]

        self.play(
            n_v.animate.move_to(splay_v),
            n_p.animate.move_to(splay_p),
            n_w.animate.move_to(splay_w),
            run_time=1.4,
            rate_func=smooth
        )
        b_splayed = self._enclose(n_v, n_p, n_w)
        self.play(FadeIn(b_splayed), run_time=0.4)
        self.wait(0.6)

        # ─── STEP 2: APPLY LAZY TAG ───
        lbl2 = self._hint("Step 2: Commit a Lazy Inversion Tag to reverse the path direction", YELLOW, title)
        self.play(ReplacementTransform(lbl1, lbl2))
        
        badge = self._lazy_badge(n_v)
        self.play(FadeIn(badge), self._pulse(n_v))
        self.wait(0.8)

        # ─── STEP 3: PHYSICAL TOPOLOGY FLIP ───
        lbl3 = self._hint("✓ Children swapped! Left descendants become right descendants. v is now root.", GREEN, title)
        self.play(ReplacementTransform(lbl2, lbl3), FadeOut(b_splayed), run_time=0.4)

        # Mirroring the layout across the Y-axis to show the left-to-right child inversion
        flip_v = [ 0.0,  1.0, 0]
        flip_p = [ 1.5, -0.4, 0]
        flip_w = [ 2.5, -1.8, 0]

        self.play(
            n_v.animate.move_to(flip_v),
            badge.animate.next_to(flip_v, UR, buff=0.05),
            n_p.animate.move_to(flip_p),
            n_w.animate.move_to(flip_w),
            run_time=1.4,
            rate_func=smooth
        )
        
        b_final = self._enclose(n_v, n_p, n_w)
        self.play(FadeIn(b_final), run_time=0.4)
        self.play(self._pulse(n_v))
        self.wait(1.5)