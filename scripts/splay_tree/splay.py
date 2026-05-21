from manim import *
from splay_base import SplayBaseScene, GREEN, RED, MUTED, YELLOW

class SplayPureAnimation(SplayBaseScene):
    def construct(self):
        # 1. Setup Title/Heading at the top
        title = self._section_title("Splay Function  —  Loop Execution", color=GREEN)
        self.play(Write(title, run_time=0.5))

        # 2. Define Initial 4-Level Coordinates (w -> g -> p -> x)
        W = [ 0.0,  2.0, 0]   # Great-grandparent / Working Root
        G = [-1.6,  0.7, 0]   # Grandparent
        P = [-2.8, -0.6, 0]   # Parent
        X = [-1.6, -1.9, 0]   # Target Node (Zig-Zag orientation relative to g)

        n_w = self._node("w", W, color=MUTED)
        n_g = self._node("g", G)
        n_p = self._node("p", P)
        n_x = self._node("x", X, color=RED) # Target Node highlighted in Red

        e0 = VGroup(
            self._edge(W, G), 
            self._edge(G, P), 
            self._edge(P, X)
        )
        nodes = VGroup(n_w, n_g, n_p, n_x)

        # Slower initial reveal
        self.play(FadeIn(e0, lag_ratio=0.1), FadeIn(nodes, lag_ratio=0.1), run_time=1.2)

        # Initial Status Hint right below the title
        hint = self._hint("Target node x requires multiple loop steps to reach root", RED, title)
        self.play(FadeIn(hint, run_time=0.4))
        self.play(self._pulse(n_x))
        self.wait(0.5)

        # ─── STEP 1: ZIG-ZAG OPERATION ───
        s1 = {
            "w": [ 0.0,  2.0, 0],
            "x": [-1.6,  0.7, 0],   # x climbs up to g's original position
            "p": [-2.8, -0.6, 0],   # p becomes left child of x
            "g": [-0.4, -0.6, 0],   # g becomes right child of x
        }
        e1 = VGroup(
            self._edge(s1["w"], s1["x"]), 
            self._edge(s1["x"], s1["p"]), 
            self._edge(s1["x"], s1["g"])
        )

        lbl1 = self._hint("Step 1: Double rotation (Zig-Zag) at g", YELLOW, title)
        self.play(ReplacementTransform(hint, lbl1, run_time=0.4))
        
        # Significantly slowed down transition speed
        self.play(
            FadeOut(e0),
            n_w.animate.move_to(s1["w"]),
            n_x.animate.move_to(s1["x"]),
            n_p.animate.move_to(s1["p"]),
            n_g.animate.move_to(s1["g"]),
            run_time=1.5, rate_func=smooth,
        )
        self.play(FadeIn(e1, run_time=0.4))
        self.wait(1.0)

        # ─── STEP 2: ZIG OPERATION ───
        s2 = {
            "x": [ 0.0,  2.0, 0],   # x reaches the absolute Root level
            "p": [-1.6,  0.7, 0],   # p shifts to the left child of x
            "w": [ 1.6,  0.7, 0],   # w drops to become the right child of x
            "g": [ 0.4, -0.6, 0],   # g reattaches as the left child of w
        }
        e2 = VGroup(
            self._edge(s2["x"], s2["p"]), 
            self._edge(s2["x"], s2["w"]), 
            self._edge(s2["w"], s2["g"])
        )

        lbl2 = self._hint("Step 2: Single rotation (Zig) at root node w", YELLOW, title)
        self.play(ReplacementTransform(lbl1, lbl2, run_time=0.4))
        
        # Significantly slowed down transition speed
        self.play(
            FadeOut(e1),
            n_x.animate.move_to(s2["x"]),
            n_p.animate.move_to(s2["p"]),
            n_w.animate.move_to(s2["w"]).set_stroke(color=BLUE, width=2.5),
            n_g.animate.move_to(s2["g"]),
            run_time=1.5, rate_func=smooth,
        )
        self.play(FadeIn(e2, run_time=0.4))
        self.wait(0.5)

        # ─── COMPLETION ───
        ok = self._hint("✓  Splay Complete: x is now the absolute root", GREEN, title)
        self.play(ReplacementTransform(lbl2, ok, run_time=0.4))
        self.play(self._pulse(n_x))
        self.wait(2.5)