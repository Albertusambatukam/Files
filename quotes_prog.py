# Reading and printing the quotes from 'quotes.txt'
with open('quotes.txt', "r", encoding="UTF-8") as file:
    for line in file:
        print(line)

# Prompting the user for the author name and appending it to the file
author = input("Who wrote these lines? ")
with open('quotes.txt', "a", encoding="UTF-8") as file:
    file.write(f"({author})\n")

# Loop to add additional quotes
while True:
    answer = input("Want to add another quote? (yes/no) ").lower()
    if answer == "yes":
        quote = input("Enter a quote: ")
        author = input("Enter an author: ")
        with open("quotes.txt", "a", encoding="UTF-8") as file:
            file.write(f"{quote}\n({author})\n")
    else:
        break