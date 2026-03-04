# This program calculates the projected semester tuition increase for 5 years

# tuition variables
tuition = 8000
yearly_increment = .03
years = 5

# initiate the table
print("Year\t\tSemester 1\t\tSemester 2\t\tTotal")
for year in range(1, years + 1):
    tuition_1 = (tuition * yearly_increment) + tuition
    print(f"{year}\t\t{tuition: .2f}\t\t{tuition_1: .2f}\t\t{tuition + tuition_1: .2f}")
    tuition = tuition_1
