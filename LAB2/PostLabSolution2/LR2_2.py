def read_file(filename):
    """Read lines from a file and return them as a list."""
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

def main():
    """Main function to navigate through lines of a file."""
    filename = input("Enter the filename: ")
    lines = read_file(filename)

    while True:
        print(f"\nNumber of lines in the file: {len(lines)}")
        line_number = int(input("Enter a line number (1 to {} or 0 to quit): ".format(len(lines))))

        if line_number == 0:
            print("Exiting the program.")
            break
        elif 1 <= line_number <= len(lines):
            print(f"Line {line_number}: {lines[line_number - 1].strip()}")
        else:
            print("Invalid line number. Please try again.")

if __name__ == "__main__":
    main()
