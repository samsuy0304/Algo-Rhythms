from manim import *

class SortScene(Scene):
    def construct(self):
        # Title Name
        Main  = Text("Sorting Algorithms")
        self.play(Create(Main), run_time = 2)
        self.wait(3)
        initial_text = Text("Bubble Sort").to_edge(LEFT)
        self.play(ReplacementTransform(Main,initial_text))
        
        #Create the bars
        array = [7.5, 7, 5, 4, 2, 3]
        array2 = [0,0,0,0,0,0]
        bars = self.create_bars(array)
        #emptybars = self.create_bars(array2)
        self.play(Create(bars), run_time = 2)
        self.wait(1)

        ######## Bubble Sort #########################
        self.animate_bubble_sort(bars)
        self.wait(3)
        bars3 = self.create_bars(array)
        
        # Transform the initial text into a new text
        new_text = Text("Selection Sort").to_edge(LEFT)
        self.play(ReplacementTransform(bars, bars3),ReplacementTransform(initial_text, new_text),run_time=2)
        self.wait(1)
        

        ############ Selection Sort ###################
        self.animate_selection_sort(bars3)
        self.wait(3)

        bars4 = self.create_bars(array)

        # Transform the initial text into a new text
        new_text2 = Text("Insertion Sort").to_edge(LEFT)
        self.play(ReplacementTransform(bars3, bars4),ReplacementTransform(new_text, new_text2), run_time=2)
        self.wait(1)

        self.animate_insertion_sort(bars4)
        self.wait(3)

        ending = Text("Thank you for watching.")
        self.play(Uncreate(bars4),run_time = 2.5)
        self.play(ReplacementTransform(new_text2,ending))
        self.wait(4)


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
                run_time = 0.5,
            )

            self.play(
                bars[i].animate.shift((shis) * RIGHT),
                bars[min_index].animate.shift(-(shis) * RIGHT),
                run_time = 1.2,
            )

            bars[i], bars[min_index] = bars[min_index], bars[i]

            self.play(
                bars[i].animate.set_fill(PINK, opacity = 0.5),  # Reset color
                bars[min_index].animate.set_fill(PINK, opacity = 0.5),
                run_time = 0.5,
            )

        return bars

    def animate_bubble_sort(self, bars):
        n = len(bars)
        bar_width = 0.5  # Adjust as needed
        spacing = 0.2  # Adjust as needed

        for i in range(n):
            for j in range(0, n - i - 1):
                self.play(
                    bars[j].animate.set_fill(RED, opacity = 0.5),  # Highlight the current minimum
                    bars[j+1].animate.set_fill(RED, opacity = 0.5),
                    run_time = 0.5,
                )
                if bars[j].height > bars[j + 1].height:
                    self.play(
                        bars[j].animate.shift((bar_width + spacing) * RIGHT),
                        bars[j + 1].animate.shift(-(bar_width + spacing) * RIGHT),
                        run_time = 1.2,
                    )

                    bars[j], bars[j + 1] = bars[j + 1], bars[j]
                
                self.play(
                    bars[j].animate.set_fill(PINK, opacity = 0.5),  # Highlight the current minimum
                    bars[j+1].animate.set_fill(PINK, opacity = 0.5),
                    run_time = 0.5,
                )
        return bars

    def animate_insertion_sort(self,bars):
        bar_width = 0.5  # Adjust as needed
        spacing = 0.2  # Adjust as needed
        for i in range(1, len(bars)):
            # The chosen one has risen...
            key_item = bars[i].height
            j = i - 1

            # Others find their way home
            while j >= 0 and bars[j].height > key_item:
                self.play(
                    bars[j].animate.set_fill(RED, opacity = 0.5),  # Highlight the chosen one
                    bars[j+1].animate.set_fill(RED, opacity = 0.5),  # Highlight the follower
                    run_time = 0.5
                )
                self.play(
                    bars[j].animate.shift((bar_width + spacing) * RIGHT),
                    bars[j+1].animate.shift(-(bar_width + spacing) * RIGHT),
                    run_time = 1.2,
                )
                
                self.play(
                    bars[j].animate.set_fill(PINK, opacity = 0.5),  # Highlight the chosen one
                    bars[j+1].animate.set_fill(PINK, opacity = 0.5),  # Highlight the follower
                    run_time = 0.5,
                )
                bars[j], bars[j+1] = bars[j+1], bars[j]
                j -= 1

            # When you finish shifting the elements, you can position
            # `key_item` in its correct location
            #bars[j + 1].height = key_item

        return bars
