import time

class Pupil:
    def _init_(self, Surname, Name, Mark):
        self.Surname = Surname
        self.Name = Name
        self.Mark = Mark

pupils = []

def print_class(pupils):
    for pupil in pupils:
        print(f"{pupil.Surname} {pupil.Name} - {pupil.Mark}")
    print("\n")

def print_five(pupils):
    print("Top students with a mark of 5:")
    top_students = [pupil.Surname for pupil in pupils if pupil.Mark == 5]
    if top_students:
        print("\n".join(top_students))
    else:
        print("No students with a mark of 5.")
    print("\n")

def find_average(pupils):
    if pupils:
        average = sum(pupil.Mark for pupil in pupils) / len(pupils)
        print(f"Average grade for the class: {average:.2f}")
    else:
        print("No data available to calculate an average grade.")

start_time = time.time()

with open("pupil_large.txt", "r") as file:
    for line in file:
        data = line.strip().split(" ")
        if len(data) == 3:  # Ensure there are exactly 3 elements in the line
            pupil = Pupil(data[0], data[1], int(data[2]))
            pupils.append(pupil)

# Uncomment to print all pupil data
# print_class(pupils)
print_five(pupils)
find_average(pupils)
print("Runtime:", round(time.time() - start_time, 2), "seconds")