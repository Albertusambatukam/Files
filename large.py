import time

class Pupil:
    def _init_(self, Surname, Name, Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark

# Initialize counters and lists
pupils_count = 0
best_pupils = []
total_marks = 0

start_time = time.time()
with open("pupil_large.txt", "r") as file:
    for line in file:
        data = line.strip().split(" ")
        
        # Ensure data contains the expected fields
        if len(data) == 3:
            pupil = Pupil(data[0], data[1], int(data[2]))

            # Add to the best pupils list if the mark is 5
            if pupil.Mark == 5:
                best_pupils.append(pupil.Surname)
            
            # Update counts and sum of marks
            pupils_count += 1
            total_marks += pupil.Mark

# Calculate and print average mark if there are pupils
if pupils_count > 0:
    print(f"Average grade: {total_marks / pupils_count:.2f}")
else:
    print("No pupil data available to calculate an average grade.")

# Print top students
print("\nTop students:")
for pupil in best_pupils:
    print(pupil)

# Print runtime
print("Runtime:", round(time.time() - start_time, 2), "seconds")