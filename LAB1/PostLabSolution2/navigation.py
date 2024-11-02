def main():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found. Please try again.")
        return

    while True:
        print(f"\nNumber of lines in the file: {len(lines)}")
        line_number = int(input("Enter a line number (1 to {0}, or 0 to quit): ".format(len(lines))))

        if line_number == 0:
            print("Exiting the program.")
            break
        elif 1 <= line_number <= len(lines):
            print(f"Line {line_number}: {lines[line_number - 1].strip()}")
        else:
            print("Invalid line number. Please try again.")

if __name__ == "__main__":
    main()
