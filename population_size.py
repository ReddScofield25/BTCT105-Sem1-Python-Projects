# This program predicts the approximate size of a population of organisms

# get daily organism records
population = float(input("Starting number of organisms: "))
avg_increase = float(input("Average daily increase (%): "))
avg_increase = avg_increase / 100
num_days = int(input("Number of days: "))

# tabularize the results in compounding avg daily increase
days = 1
print("Day\t\tPopulation")
print(f"{days}\t\t{population: .4f}")
for i in range(1, num_days):
    days += 1
    population = (population * avg_increase) + population
    print(f"{days}\t\t{population: .4f}")
