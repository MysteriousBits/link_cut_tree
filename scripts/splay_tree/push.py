# lazy_splay.py
from manim import *
from splay_base import SplayBaseScene, BLUE, RED, MUTED, YELLOW, GREEN

class LazyPushScene(SplayBaseScene):
    def construct(self):
        title = self._section_title("Lazy Propagation  —  push(x)", color=BLUE)
        self.play(Write(title, run_time=0.4))

        # Coordinates for a parent x with left child L and right child R
        X = [0.0, 1.0, 0]
        L = [-1.8, -0.8, 0]
        R = [1.8, -0.8, 0]

        n_x = self._node("x", X, color=RED)
        n_L = self._node("L", L, color=BLUE)
        n_R = self._node("R", R, color=MUTED)

        e0 = VGroup(self._edge(X, L), self._edge(X, R))
        nodes = VGroup(n_x, n_L, n_R)

        # Draw a visual indicator flag for the lazy bit
        lazy_tag = Text("[Flip: True]", font_size=14, color=YELLOW).next_to(n_x, UP, buff=0.15)

        self.play(FadeIn(e0), FadeIn(nodes), FadeIn(lazy_tag), run_time=0.8)
        
        hint = self._hint("push(x): Evaluation of lazy tag requires flipping child pointers", YELLOW, title)
        self.play(FadeIn(hint, run_time=0.4))
        self.wait(0.8)

        # Post-swap layout configuration
        s1 = {"x": [0.0, 1.0, 0], "L": [1.8, -0.8, 0], "R": [-1.8, -0.8, 0]}
        e1 = VGroup(self._edge(s1["x"], s1["L"]), self._edge(s1["x"], s1["R"]))

        # Dynamic update label
        lbl_exec = self._hint("Swapping Left and Right subtrees & passing flags down", YELLOW, title)
        self.play(ReplacementTransform(hint, lbl_exec))

        # Push lazy flags down to children subtrees
        tag_L = Text("[Flip: True]", font_size=12, color=YELLOW).next_to(n_L, DOWN, buff=0.1)
        tag_R = Text("[Flip: True]", font_size=12, color=YELLOW).next_to(n_R, DOWN, buff=0.1)

        self.play(
            FadeOut(e0),
            FadeOut(lazy_tag),
            n_L.animate.move_to(s1["L"]).set_color(MUTED),
            n_R.animate.move_to(s1["R"]).set_color(BLUE),
            run_time=1.2, rate_func=smooth
        )
        self.play(FadeIn(e1), FadeIn(tag_L), FadeIn(tag_R), run_time=0.3)

        ok = self._hint("✓ push(x) complete: Node cleared. Flags deferred to children.", GREEN, title)
        self.play(ReplacementTransform(lbl_exec, ok))
        self.wait(2.0)