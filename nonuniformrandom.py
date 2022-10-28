from scipy.stats import uniform
import numpy as np

# create a array based on the Figure 15 plot (manually measure the values from the plot)
# cdf_bins_to_power[CDF] = Power
# The plot in Figure 15 needs to be discretize by creating bins, i.e., instread of continuous values of CDF and Power, use discrete values
# More bins you have, the more accurate will be the sampling. Creating 100 bins should be good.
# from example, creating 10 bins below by entering rough power values corresponding to CDF value between 0 to 1 (with a bin size of 0.1) from Figure 15
cdf_bins_to_power = [-45, -37.5, -36, -34, -33, -32, -31, -29, -27.5, -26, -20]

# Sample one-by-one in the code below. But you can also generate multiple random numbers at one go which can speed up the code.
def sample_power_using_inverse_transform():
    U=uniform.rvs(size=1)[0] # get a uniform number between 0 and 1
    cdf_bin = round(U * 10) # which cdf bin does it fall between 0 and 10 ? Multiply by 10 and round off to thee nearest integer
    power = cdf_bins_to_power[cdf_bin] # look up the power from the array above
    return(power)
