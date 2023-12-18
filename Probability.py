from scipy.stats import rv_discrete

x = [1, 2, 3, 4, 5, 6]
p = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

# Create a discrete random variable
custom_discrete = rv_discrete(values=(x, p))

# Calculate the expected value
expected_value = custom_discrete.expect()
print(expected_value)

