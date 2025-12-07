# Tell the operating system to use Python 3 to run this script
#!/usr/bin/env python3

# Import the os module to work with file paths and check if files exist
import os

# Import the sys module to allow exiting with status codes
import sys

# Define the list of required files that must exist in the project root
REQUIRED_FILES = ["README.md", ".gitignore"]

# Define the main function that will run the file checks
def main():

    # Create a list of any required files that are missing
    missing = [f for f in REQUIRED_FILES if not os.path.exists(f)]

    # Check if any files are missing
    if missing:
        # Print a failure message
        print("❌ Required files are missing:")

        # Loop through and print each missing file
        for f in missing:
            print(f" - {f}")

        # Exit with a non-zero code so CI fails
        sys.exit(1)

    else:
        # Exit with zero so CI passes silently
        sys.exit(0)

# Check if this script is being run directly
if __name__ == "__main__":

    # Call the main function
    main()
