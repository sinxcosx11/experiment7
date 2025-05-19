import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 


log_Fe3_0_A = np.array([-2.376, -2.199, -2.075, -1.978, -1.921])
log_Rate_A = np.array([-7.057, -6.984, -6.997, -6.769, -6.960])

log_Fe3_0_A_reliable = np.array([-2.199, -1.978]) 
log_Rate_A_reliable = np.array([-6.984, -6.769])  

log_I_0_B = np.array([-2.199, -2.075, -1.978])
log_Rate_B = np.array([-6.648, -6.460, -6.136])


slope_A_all, intercept_A_all, r_value_A_all, p_value_A_all, std_err_A_all = stats.linregress(log_Fe3_0_A, log_Rate_A)
line_A_all = slope_A_all * log_Fe3_0_A + intercept_A_all

slope_A_reliable, intercept_A_reliable, r_value_A_reliable, p_value_A_reliable, std_err_A_reliable = stats.linregress(log_Fe3_0_A_reliable, log_Rate_A_reliable)
line_A_reliable = slope_A_reliable * log_Fe3_0_A_reliable + intercept_A_reliable


plt.figure(figsize=(10, 6))
plt.scatter(log_Fe3_0_A, log_Rate_A, color='blue', label='Experimental Data (All Runs 1-5)')
plt.plot(log_Fe3_0_A, line_A_all, color='lightblue', linestyle='--', label=f'Regression (All Runs)\nSlope (a) = {slope_A_all:.2f}\nR² = {r_value_A_all**2:.2f}')

plt.scatter(log_Fe3_0_A_reliable, log_Rate_A_reliable, color='red', marker='x', s=100, label='Experimental Data (Runs 2 & 4)')
x_range_A = np.array([min(log_Fe3_0_A), max(log_Fe3_0_A)])
line_A_reliable_extended = slope_A_reliable * x_range_A + intercept_A_reliable
plt.plot(x_range_A, line_A_reliable_extended, color='darkred', label=f'Regression (Runs 2 & 4)\nSlope (a) = {slope_A_reliable:.2f}\nR² = {r_value_A_reliable**2:.2f}')


plt.title('Determination of Reaction Order with respect to $Fe^{3+}$')
plt.xlabel('$log[Fe^{3+}]_0$')
plt.ylabel('$log(Rate)$')
plt.legend()
plt.grid(True)
plt.show()

# ---order of reaction with respect to I- ---

slope_B, intercept_B, r_value_B, p_value_B, std_err_B = stats.linregress(log_I_0_B, log_Rate_B)
line_B = slope_B * log_I_0_B + intercept_B

plt.figure(figsize=(10, 6))
plt.scatter(log_I_0_B, log_Rate_B, color='green', label='Experimental Data (Runs 6-8)')
plt.plot(log_I_0_B, line_B, color='darkgreen', label=f'Linear Regression\nSlope (b) = {slope_B:.2f}\nR² = {r_value_B**2:.2f}')

plt.title('Determination of Reaction Order with respect to $I^-$')
plt.xlabel('$log[I^-]_0$')
plt.ylabel('$log(Rate)$')
plt.legend()
plt.grid(True)
plt.show()
