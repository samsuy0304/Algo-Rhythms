import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Mt:
    """A crappy sorting class"""

    # initialization method for Random class
    def __init__(self, seed=5555):
        self.m_random = Random(seed)

    # sorts array using bubble sort
    def BubbleSort(self, array):
        n = len(array)
        fig, ax = plt.subplots()

        # Define the bar plot for the initial state of the array
        bar_plot = ax.bar(range(n), array)

        # Define the function to update the bar plot for each iteration of the algorithm
        def update_plot(iteration):
            # Create a flag that will allow the function to
            # terminate early if there's nothing left to sort
            already_sorted = True

            # Start looking at each item of the list one by one,
            # comparing it with its adjacent value. With each
            # iteration, the portion of the array that you look at
            # shrinks because the remaining items have already been
            # sorted.
            for j in range(n - iteration - 1):
                if array[j] > array[j + 1]:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    array[j], array[j + 1] = array[j + 1], array[j]

                    # Since you had to swap two elements,
                    # set the `already_sorted` flag to `False` so the
                    # algorithm doesn't finish prematurely
                    already_sorted = False

                # Update the bar plot to reflect the current state of the array
                for i, bar in enumerate(bar_plot):
                    bar.set_height(array[i])

            # If there were no swaps during the last iteration,
            # the array is already sorted, and you can terminate
            if already_sorted:
                anim.event_source.stop()

        # Create the animation object
        anim = animation.FuncAnimation(fig, update_plot, frames=n,
                                       interval=1000, repeat=False)

        plt.show()

        return array


# generate some random data to be sorted
N = 20
data = np.random.randint(1, 50, N)

# create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(0, N)
ax.set_ylim(0, 50)

# create a bar chart of the initial data
bar_rects = ax.bar(range(N), data, align="center")

# initialize the sorting algorithm
mysort = Mt()

# define the update function for the animation
def update(frame):
    global data
    global bar_rects

    # sort the data using bubble sort
    data = mysort.BubbleSort(data)

    # update the heights of the bar chart to show the current state of the sorted data
    for i, rect in enumerate(bar_rects):
        rect.set_height(data[i])

    return bar_rects

# create the animation object
anim = animation.FuncAnimation(fig, update, frames=N, blit=True)

# display the animation
plt.show()




