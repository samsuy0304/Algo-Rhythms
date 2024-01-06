from manim import *
class CollectiveSortScene(Scene):
    def construct(self):
        initial_text = Text("Bulble Sort").to_edge(LEFT)

        self.play(Create(initial_text), run_time = 0.5)
        array = [4, 2, 7, 1, 9, 3]

        bars = self.create_bars(array)
        self.play(Create(bars), run_time = 0.5)
        self.wait(1)

        self.animate_bubble_sort(bars)
        self.wait(3)
        bars3 = self.create_bars(array)
        self.play(ReplacementTransform(bars, bars3))

        # Transform the initial text into a new text
        new_text = Text("Selection Sort").to_edge(LEFT)
        self.play(Transform(initial_text, new_text))
        #self.play(Create(bars2))
        self.wait(1)

        self.animate_selection_sort(bars3)
        self.wait(3)

    def create_bars(self, array):
        bars = VGroup()

        for value in array:
            bar = Rectangle(height=value, width=0.5, fill_color=PINK, fill_opacity=0.5)
            bars.add(bar)

        bar_width = 0.5
        spacing = 0.2
        bars.arrange(RIGHT, buff=spacing)
        bars.move_to(ORIGIN)
        return bars

    def animate_selection_sort(self, bars):
        n = len(bars)
        bar_width = 0.5
        spacing = 0.2

        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if bars[j].height < bars[min_index].height:
                    min_index = j
            tis = min_index-i
            shis = (bar_width + spacing)*tis
            self.play(
                bars[i].animate.set_fill(RED, opacity = 0.5),  # Highlight the current minimum
                bars[min_index].animate.set_fill(RED, opacity = 0.5),
                run_time = 0.2,
            )

            self.play(
                bars[i].animate.shift((shis) * RIGHT),
                bars[min_index].animate.shift(-(shis) * RIGHT),
                run_time = 0.7,
            )

            bars[i], bars[min_index] = bars[min_index], bars[i]

            self.play(
                bars[i].animate.set_fill(PINK, opacity = 0.5),  # Reset color
                bars[min_index].animate.set_fill(PINK, opacity = 0.5),
                run_time = 0.2,
            )

        return bars

    def animate_bubble_sort(self, bars):
        n = len(bars)
        bar_width = 0.5  # Adjust as needed
        spacing = 0.5  # Adjust as needed

        for i in range(n):
            for j in range(0, n - i - 1):
                if bars[j].height > bars[j + 1].height:
                    self.play(
                        bars[i].animate.set_fill(RED, opacity = 0.5),  # Highlight the current minimum
                        bars[j+1].animate.set_fill(RED, opacity = 0.5),
                        run_time = 0.2,
                    )
                    self.play(
                        bars[j].animate.shift((bar_width + spacing) * RIGHT),
                        bars[j + 1].animate.shift(-(bar_width + spacing) * RIGHT),
                        run_time = 0.7,
                    )


                    self.play(
                        bars[i].animate.set_fill(PINK, opacity = 0.5),  # Highlight the current minimum
                        bars[j+1].animate.set_fill(PINK, opacity = 0.5),
                        run_time = 0.2,
                    )
                    bars[j], bars[j + 1] = bars[j + 1], bars[j]
        return bars
