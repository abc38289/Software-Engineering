from scipy.stats import binom

# Define probability of being allergic (success)
p = 0.15

# Define number of trials (people selected)
n = 60

# Calculate probability of having 7 allergic people
k = 7  # Number of successes (people allergic to cats)

probability = binom.pmf(k, n, p)

# Print the probability
print(f"The probability of having {k} people allergic to cats in a trial of {n} people is: {probability:.4f}")
