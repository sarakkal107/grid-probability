# Grid Probability

## Step 1: Test File Generation
In order to generate the test maps and corresponding data, run the generate.py script. To change the size of the grid, modify the row and col variables definied at the top of the file. 

*** NOTE: When generating the files, we do utilize index 0, so all generated paths also utilize 0. To match up with the visualization, we added 1 to each coordinate. ***

## Step 2: Visualization
In order to visualize the test maps and corresponding data, run the visualize.py script using "python visualize.py". Change the folder, mapFile variable, and dataFile variable in order to change which visualization is seen. There is a scrollbar on the right of the window if the window is too large to see the entire grid and legend at the bottom.

# Rejection Sampling and Likelihood Weighting
The scripts used for rejection sampling and likelihood weighting are located in the problem_3 folder. 
## Rejection Sampling
The script for rejection sampling is rejection_sampling.py. Run this script with the command "python3 rejection_sampling.py". Running this script would calculate the probabilities for the three queries for Part b of Question 3 and create the plot for Part d. There is a commented section for the plot of part c in the script.
## Likelihood Weighting
The script for likelihood weighting is likelihood_weighting.py. Run this script with the command "python3 rejection_sampling.py". This script pulls the weighted_sample and likelihood_weighting functions from the likelihood_functions.py script. Running this script would calculate the probabilities for the three queries for Part b of Question 3 and create the plot for Part d. There is a commented section for the plot of part c in the script.
