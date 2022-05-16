from matplotlib import pyplot as plt

from profiling import LogTimer


class SortingAlgoPlotter:
    def __init__(self, sorting_algos: list):

        plot_cols = 2
        if len(sorting_algos) > 1:
            self.fig, self.ax = plt.subplots(
                len(sorting_algos) // plot_cols, plot_cols
            )
            self.axes_map = dict(zip(sorting_algos, self.ax.flat))
        else:
            self.fig, self.ax = plt.subplots()

            self.axes_map = dict(zip(sorting_algos, [self.ax]))

        self.bar_map_rects = {}

    def _init_bar(self, algo_key: str, init_data_array):

        ax = self.axes_map[algo_key]
        self.bar_map_rects[algo_key] = ax.bar(
            list(range(len(init_data_array))), init_data_array
        )
        plt.show(block=False)
        return self.bar_map_rects[algo_key]

    def plot_results(self, algo_arrays: dict):

        for k in algo_arrays.keys():

            ax = self.axes_map[k]
            try:
                bar_rects = self.bar_map_rects[k]
            except KeyError:
                bar_rects = self._init_bar(k, algo_arrays[k])
            ax.set_title(k)
            for rect, h in zip(bar_rects, algo_arrays[k]):
                rect.set_height(h)

        with LogTimer("Drawing:"):
            plt.draw()
            plt.pause(0.000001)
