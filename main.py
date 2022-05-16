import random

from bubble_sort import bubble_sort_gen
from insertion_sort import insertion_sort_gen
from merge_sort import merge_sort
from profiling import LogTimer
from sorting_plot import SortingAlgoPlotter
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s" " - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.DEBUG,
)
if __name__ == "__main__":

    l = list(range(1, 30))
    random.shuffle(l)

    algo_plotter = SortingAlgoPlotter(["bubble_sort", "insertion_sort"])

    for a in bubble_sort_gen(l):
        with LogTimer("Update Charts and plot"):
            algo_plotter.plot_results({"bubble_sort": a})

    random.shuffle(l)
    for a in insertion_sort_gen(l):
        with LogTimer("Update Charts and plot"):
            algo_plotter.plot_results({"insertion_sort": a})

    input("Press any key...")
