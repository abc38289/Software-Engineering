from scipy.stats import norm

weight_mean = 180
weight_std = 34

weight_lower_limit = 120
weight_upper_limit = 155

probability = norm.cdf(weight_upper_limit, weight_mean, weight_std) - norm.cdf(weight_lower_limit, weight_mean, weight_std)


print(f"The probability of a man weighing between {weight_lower_limit} and {weight_upper_limit} pounds is: {probability:.4f}")
