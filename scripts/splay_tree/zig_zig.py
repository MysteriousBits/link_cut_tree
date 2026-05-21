from manim import *
from splay_base import SplayBaseScene, GREEN, RED, MUTED, YELLOW

class ZigZigScene(SplayBaseScene):
    def construct(self):
        title = self._section_title("Zig-Zig  —  Same-Direction Rotations", color=GREEN)
        self.play(Write(title, run_time=0.4))

        G = [0.0, 1.9, 0]; P = [-1.6, 0.6, 0]; D = [1.6,  0.6, 0]
        X = [-2.8,-0.7, 0]; C = [-0.4,-0.7, 0]
        A = [-3.5,-1.9, 0]; B = [-2.1,-1.9, 0]

        n_g = self._node("g", G)
        n_p = self._node("p", P)
        n_D = self._node("D", D, color=MUTED)
        n_x = self._node("x", X, color=RED)
        n_C = self._node("C", C, color=MUTED)
        n_A = self._node("A", A, color=MUTED)
        n_B = self._node("B", B, color=MUTED)

        e0 = VGroup(
            self._edge(G, P), self._edge(G, D), self._edge(P, X), 
            self._edge(P, C), self._edge(X, A), self._edge(X, B),
        )
        nodes = VGroup(n_g, n_p, n_D, n_x, n_C, n_A, n_B)

        self.play(FadeIn(e0, lag_ratio=0.05), FadeIn(nodes, lag_ratio=0.05), run_time=0.75)

        hint = self._hint("x and p are both left children", RED, title)
        self.play(FadeIn(hint, run_time=0.3))
        self.play(self._pulse(n_x))

        # Step 1: rotate at g
        s1 = {
            "p": [ 0.0, 1.9, 0], "x": [-1.6, 0.6, 0], "g": [1.6,  0.6, 0],
            "A": [-2.3,-0.7, 0], "B": [-0.9,-0.7, 0],
            "C": [ 0.9,-0.7, 0], "D": [ 2.3,-0.7, 0],
        }
        e1 = VGroup(
            self._edge(s1["p"], s1["x"]), self._edge(s1["p"], s1["g"]),
            self._edge(s1["x"], s1["A"]), self._edge(s1["x"], s1["B"]),
            self._edge(s1["g"], s1["C"]), self._edge(s1["g"], s1["D"]),
        )

        lbl1 = self._hint("Step 1: right-rotate at g", YELLOW, title)
        self.play(ReplacementTransform(hint, lbl1))
        self.play(
            FadeOut(e0),
            n_p.animate.move_to(s1["p"]), n_g.animate.move_to(s1["g"]),
            n_x.animate.move_to(s1["x"]), n_A.animate.move_to(s1["A"]),
            n_B.animate.move_to(s1["B"]), n_C.animate.move_to(s1["C"]),
            n_D.animate.move_to(s1["D"]),
            run_time=0.85, rate_func=smooth,
        )
        self.play(FadeIn(e1, run_time=0.25))

        # Step 2: rotate at p
        s2 = {
            "x": [ 0.0, 1.9, 0], "A": [-1.6, 0.6, 0], "p": [1.6,  0.6, 0],
            "B": [ 0.9,-0.7, 0], "g": [2.3, -0.7, 0],
            "C": [ 1.6,-1.9, 0], "D": [3.0, -1.9, 0],
        }
        e2 = VGroup(
            self._edge(s2["x"], s2["A"]), self._edge(s2["x"], s2["p"]),
            self._edge(s2["p"], s2["B"]), self._edge(s2["p"], s2["g"]),
            self._edge(s2["g"], s2["C"]), self._edge(s2["g"], s2["D"]),
        )

        lbl2 = self._hint("Step 2: right-rotate at p", YELLOW, title)
        self.play(ReplacementTransform(lbl1, lbl2))
        self.play(
            FadeOut(e1),
            n_x.animate.move_to(s2["x"]), n_A.animate.move_to(s2["A"]),
            n_p.animate.move_to(s2["p"]), n_B.animate.move_to(s2["B"]),
            n_g.animate.move_to(s2["g"]), n_C.animate.move_to(s2["C"]),
            n_D.animate.move_to(s2["D"]),
            run_time=0.85, rate_func=smooth,
        )
        self.play(FadeIn(e2, run_time=0.25))

        ok = self._hint("✓  x is now root", GREEN, title)
        self.play(ReplacementTransform(lbl2, ok, run_time=0.35))
        self.wait(2)