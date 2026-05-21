from manim import *
from splay_base import SplayBaseScene, BLUE, RED, MUTED, GREEN

class ZigScene(SplayBaseScene):
    def construct(self):
        title = self._section_title("Zig  —  Single Rotation", color=BLUE)
        self.play(Write(title, run_time=0.4))

        # Before positions
        P = [ 0.0,  1.2, 0]; X = [-1.55,  0.0, 0]; C = [1.55,  0.0, 0]
        A = [-2.3, -1.3, 0]; B = [-0.8,  -1.3, 0]

        n_p = self._node("p", P)
        n_x = self._node("x", X, color=RED)
        n_C = self._node("C", C, color=MUTED)
        n_A = self._node("A", A, color=MUTED)
        n_B = self._node("B", B, color=MUTED)

        e0 = VGroup(
            self._edge(P, X), self._edge(P, C),
            self._edge(X, A), self._edge(X, B),
        )
        nodes = VGroup(n_p, n_x, n_C, n_A, n_B)

        self.play(FadeIn(e0, lag_ratio=0.07), FadeIn(nodes, lag_ratio=0.07), run_time=0.75)

        hint = self._hint("Splay x → root", RED, title)
        self.play(FadeIn(hint, run_time=0.3))
        self.play(self._pulse(n_x))

        # After positions
        X2 = [ 0.0,  1.2, 0]; A2 = [-1.55, 0.0, 0]; P2 = [1.55,  0.0, 0]
        B2 = [ 0.8, -1.3, 0]; C2 = [2.3,  -1.3, 0]

        e1 = VGroup(
            self._edge(X2, A2), self._edge(X2, P2),
            self._edge(P2, B2), self._edge(P2, C2),
        )

        self.play(
            FadeOut(e0),
            n_x.animate.move_to(X2), n_p.animate.move_to(P2),
            n_A.animate.move_to(A2), n_B.animate.move_to(B2),
            n_C.animate.move_to(C2),
            run_time=1.0, rate_func=smooth,
        )
        self.play(FadeIn(e1, run_time=0.3))

        ok = self._hint("✓  x is now root", GREEN, title)
        self.play(ReplacementTransform(hint, ok, run_time=0.35))
        self.wait(2)