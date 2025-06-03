def read_dictionary_from_file(filename):
    """
    Reads a dictionary from a text file where each line contains key: value pairs
    Returns a dictionary object
    """
    dictionary = {}
    try:
        with open(filename, 'r') as file:
            print(f"Successfully opened {filename}")
            for line_number, line in enumerate(file, 1):
                line = line.strip()  # Remove whitespace and newlines
                if line and ':' in line:  # Check if line is not empty and contains ':'
                    try:
                        key, value = line.split(':', 1)  # Split only on first ':'
                        key = key.strip()
                        value = value.strip()
                        dictionary[key] = value
                        print(f"Line {line_number}: Added '{key}' -> '{value}'")
                    except ValueError:
                        print(f"Warning: Skipping malformed line {line_number}: {line}")
                elif line:  # Non-empty line without ':'
                    print(f"Warning: Skipping invalid line {line_number}: {line}")

        print(f"Successfully read {len(dictionary)} items from {filename}")
        return dictionary

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename and try again.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'. Check file permissions.")
        return None
    except Exception as e:
        print(f"Unexpected error reading '{filename}': {e}")
        return None


def invert_dictionary(original_dict):
    """
    Inverts a dictionary by swapping keys and values
    If multiple keys have the same value, they are combined in a list
    """
    if not original_dict:
        print("Warning: Cannot invert empty dictionary")
        return {}

    inverted_dict = {}
    print("\nInverting dictionary...")

    for key, value in original_dict.items():
        print(f"Processing: '{key}' -> '{value}'")

        if value in inverted_dict:
            # If the value already exists as a key, append to the list
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                # Convert single item to list and add new item
                inverted_dict[value] = [inverted_dict[value], key]
            print(f"  Added '{key}' to existing entry for '{value}'")
        else:
            # First occurrence of this value
            inverted_dict[value] = key
            print(f"  Created new entry: '{value}' -> '{key}'")

    print(f"Dictionary inversion complete. {len(inverted_dict)} unique values found.")
    return inverted_dict


def write_dictionary_to_file(dictionary, filename):
    """
    Writes a dictionary to a text file in key: value format
    Handles both single values and lists of values
    """
    if not dictionary:
        print("Warning: Cannot write empty dictionary")
        return False

    try:
        with open(filename, 'w') as file:
            print(f"\nWriting inverted dictionary to {filename}...")
            file.write("{\n")

            for key, value in dictionary.items():
                if isinstance(value, list):
                    # Handle multiple values (convert list to comma-separated string)
                    value_str = ", ".join(value)
                    file.write(f"{key}: {value_str}\n")
                    print(f"Wrote: '{key}' -> '{value_str}'")
                else:
                    # Handle single value
                    file.write(f"{key}: {value}\n")
                    print(f"Wrote: '{key}' -> '{value}'")

            file.write("}")
            print(f"Successfully wrote {len(dictionary)} items to {filename}")
            return True

    except PermissionError:
        print(f"Error: Permission denied to write to '{filename}'. Check file permissions.")
        return False
    except Exception as e:
        print(f"Unexpected error writing to '{filename}': {e}")
        return False


def display_dictionary(dictionary, title):
    """
    Displays a dictionary in a formatted way
    """
    print(f"\n{'=' * 50}")
    print(f"{title}")
    print(f"{'=' * 50}")

    if not dictionary:
        print("Dictionary is empty")
        return

    for key, value in dictionary.items():
        if isinstance(value, list):
            value_str = ", ".join(value)
            print(f"{key}: {value_str}")
        else:
            print(f"{key}: {value}")

    print(f"Total items: {len(dictionary)}")


def main():
    """
    Main function that orchestrates the dictionary inversion process
    """
    print("Dictionary Inversion Program")
    print("=" * 40)

    # File names
    input_filename = "input_dictionary.txt"
    output_filename = "output_dictionary.txt"

    # Step 1: Read original dictionary from file
    print(f"\nStep 1: Reading dictionary from {input_filename}")
    original_dict = read_dictionary_from_file(input_filename)

    if original_dict is None:
        print("Failed to read input file. Program terminated.")
        return

    # Display original dictionary
    display_dictionary(original_dict, "ORIGINAL DICTIONARY")

    # Step 2: Invert the dictionary
    print(f"\nStep 2: Inverting dictionary")
    inverted_dict = invert_dictionary(original_dict)

    # Display inverted dictionary
    display_dictionary(inverted_dict, "INVERTED DICTIONARY")

    # Step 3: Write inverted dictionary to file
    print(f"\nStep 3: Writing inverted dictionary to {output_filename}")
    success = write_dictionary_to_file(inverted_dict, output_filename)

    if success:
        print(f"\n✓ Program completed successfully!")
        print(f"✓ Original dictionary read from: {input_filename}")
        print(f"✓ Inverted dictionary written to: {output_filename}")
    else:
        print(f"\n✗ Program completed with errors.")


# Execute the program
if __name__ == "__main__":
    main()