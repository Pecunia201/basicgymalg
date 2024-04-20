from itertools import combinations

# Setting the numbers
target = float(input("Enter target (kg): "))
weights = [2.5, 2, 1.5, 1.25]

# Function
def smallest_sum_over_target(weights, target):
    # Initialise variables
    smallest_sum = float('inf')
    smallest_combination = None

    # Try all possible combinations
    for r in range(1, len(weights) + 1):
        for combination in combinations(weights, r):
            sum_combination = sum(combination)
            if sum_combination == target/2:
                return sum_combination, combination  # Return if sum is equal to target
            elif target/2 < sum_combination < smallest_sum:
                smallest_sum = sum_combination
                smallest_combination = combination

    return smallest_sum, smallest_combination

smallest_sum, smallest_combination = smallest_sum_over_target(weights, target)

# Print output
print(smallest_sum, smallest_combination)