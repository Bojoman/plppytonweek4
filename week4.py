# File read and write

def modify_file_content(input_filename, output_filename):
    """Reads a file, modifies its content, and writes it to a new file."""
    try:
        with open(input_filename, "r") as infile:
            content = infile.read()
            modified_content = content.upper()  
        
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        print(f"Content successfully modified and written to {output_filename}.")
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: Unable to read or write files.")

# File handling example
input_file = "plpweek4.txt" 
output_file = "modified_plpweek4.txt"
modify_file_content(input_file, output_file)
