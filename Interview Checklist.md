# How Exception Handling Works
``` python
import logging

# Configure logging to write to a file
logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_file():
    try:
        # Ask user for file name and divisor
        filename = input("Enter filename (e.g., data.txt): ")
        divisor = int(input("Enter a number to divide by: "))

        # Try to open the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Process each line in the file
        results = []
        for line in lines:
            number = int(line.strip())      # May raise ValueError
            result = number / divisor       # May raise ZeroDivisionError
            results.append(result)

    except FileNotFoundError as e:
        print("File not found!")
        logging.error("FileNotFoundError: %s", e)

    except ValueError as e:
        print("Invalid data. Ensure the file contains only numbers.")
        logging.error("ValueError: %s", e)

    except ZeroDivisionError as e:
        print("Cannot divide by zero.")
        logging.error("ZeroDivisionError: %s", e)

    except Exception as e:
        # Catch any other unexpected errors
        print("An unexpected error occurred:", str(e))
        logging.error("Unknown error: %s", e)

    else:
        # Runs only if no exception occurred
        print("✅ Results of division:")
        for r in results:
            print(r)

    finally:
        # Always runs
        print("🔁 Finished processing.")

# Run the function
process_file()
'''