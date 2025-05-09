# Create an empty list to store the grades
grades = []

# Ask the user to input 5 grades
for i in range(5):
    while True:
        try:
            grade = float(input(f"Enter grade #{i+1} (0 to 100): ")) #the f in the beginning of the input string 
            if 0 <= grade <= 100:                                    #is to give you the ability to add variables
                grades.append(grade)            #append is to add the value given into the list
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:          #If the user inputs letters instead of numbers
            print("Please enter a valid number.")

# Calculate average, maximum, and minimum
average = sum(grades) / len(grades)
maximum = max(grades)
minimum = min(grades)

# Display results
print("\nResults:")
print(f"Average grade: {average:.2f}") #{average:.2f} will show the average with two decimal points
print(f"Highest grade: {maximum}")
print(f"Lowest grade: {minimum}")