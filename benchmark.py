import sys
import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# get the path to the right folder
def get_data_folder_path():
    current_dir = os.path.dirname(__file__)
    print(f"current_dir: {current_dir}")
    
    data_folder = os.path.join(current_dir, "/data")
    print(f"data_dir: {data_folder}")
    return data_folder
    
def main():
    data_folder_path = get_data_folder_path()
    print(f"data_path: {data_folder_path}")
    # Algorithme to do 
    # open folder with pandas
    # Open mission file in csv 
    # Plot the graph for each mission


if __name__ == '__main__':
    main();