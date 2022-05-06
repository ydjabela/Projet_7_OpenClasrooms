from controller.bruteforce import BruteForce
from controller.optimized import Optimized

# ---------------------------------------------------------------------------------------------------------------------#


def start_programme():
    if __name__ == "__main__":

        # brute force excution
        BruteForce().excution_bruteforce()

        # optimized file
        Optimized().excution_optimized()

        # optimized sienna file
        Optimized().excution_optimized_sienna_data()

# ---------------------------------------------------------------------------------------------------------------------#


start_programme()

# ---------------------------------------------------------------------------------------------------------------------#
