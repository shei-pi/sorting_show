import random

from bubble_sort import bubble_sort_gen
from profiling import LogTimer
from sorting_plot import SortingAlgoPlotter
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s" " - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.DEBUG,
)
if __name__ == "__main__":

    l = list(range(200))
    random.shuffle(l)

    algo_plotter = SortingAlgoPlotter(["bubble_sort"])

    for a in bubble_sort_gen(l):
        with LogTimer("Update Charts and plot"):
            algo_plotter.plot_results({"bubble_sort": a})

    input("Press any key...")
