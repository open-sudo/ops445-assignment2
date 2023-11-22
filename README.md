# Assignment: Creating findim.py - Enhancing the Find Command in Python

## Overview:

In this assignment, you will develop a Python script, `findim.py`, designed to enhance the functionality of the `find` command. The script will take a directory path and search criteria as command-line arguments, execute the `find` command for that directory, and generate a comprehensive report about the files that match the specified criteria.

### Purpose:
The primary goal of this assignment is to reinforce your understanding of working with command-line arguments, subprocess execution, and data parsing in Python. By building upon the existing `find` command, you will gain hands-on experience in handling file-related information and generating detailed reports.

### Expected Features:
Your script should exhibit the following features:

1. **Accept Command-Line Arguments:**
   - Function Name: `parse_command_line_arguments`
   - Parameters: None (Uses the `argparse` library for parsing)

2. **Invoke the Find Command:**
   - Function Name: `execute_find_command`
   - Parameters: `directory_path` (str)

3. **Parse Find Output:**
   - Function Name: `parse_find_output`
   - Parameters: `find_output` (str)

4. **Generate Detailed Report:**
   - Function Name: `generate_detailed_report`
   - Parameters: `file_info` (list of dictionaries containing file details)

5. **Display Totals:**
   - Function Name: `display_totals`
   - Parameters: `total_files` (int), `total_disk_space` (float)

### How it Works:
- The program will utilize command-line arguments to receive user inputs, employing the `argparse` library for efficient parsing.
- It will then leverage the `os` library to execute the `find` command on the specified directory.
- The output of the `find` command will be captured and processed to extract relevant information about matching files.
- A comprehensive report will be generated, including details like file size, permissions, and modification time, for each file meeting the criteria.
- The script will conclude by displaying the total number of matching files and the combined disk space they occupy.

### Restrictions:
To ensure a focused learning experience, you are limited to using only native Python libraries such as `os`, `sys`, `argparse`, etc.

## Program Functions:

Now, let's break down the tasks into distinct program functions for a more structured approach.

### 1. Accept Command-Line Arguments:
Function to parse command-line arguments using the argparse library. <br><strong>Returns:</strong> Parsed arguments object
```python
parse_command_line_arguments()
```

### 2. Invoke the Find Command:
```
execute_find_command(directory_path)
```
Function to execute the 'find' command for the specified directory.<br>
<strong>Returns:</strong> Output of the 'find' command.

### 3. Format Date:
Function to convert timestamp from epoch timestamp into human-readable format.<br>
<strong>Returns:</strong> Date/Time in DD/MM/YYY HH:MM:SS format
```
format_date_timestamp(timestamp)
```

### 4. Format file size:
Function to convert file sizes from bytes to megabytes<br>
<strong>Returns:</strong> File size in megabytes (float)
```
format_filesize(file_size)
```

### 5. Parse Find Output:
Function to parse the output of the 'find' command.<br>
<strong>Returns:</strong> List of dictionaries containing file details.
```
parse_find_output(find_output)
```


### 6. Generate Detailed Report:
Function to generate a detailed report for each matching file.<br>
<strong>Returns:</strong> None (Prints the detailed report).
```
generate_detailed_report(file_info)
```


### 7. Display Totals:
Function to display the total number of matching files and total disk space.<br>
<strong>Returns:</strong> None (Prints the totals).
```
display_totals(total_files, total_disk_space)
```

## Output
<strong>Command</strong>:
```
$ ./findim.py /path/to/directory --name "*.txt" --size +1M
```
<strong>Output</strong>:
```
Found 3 matching files in /path/to/directory:



1. /path/to/directory/file1.txt
- Size: 1.2M
- Permissions: rw-r--r--
- Modification Time: 2023-01-15 09:30:00

2. /path/to/directory/file2.txt
- Size: 2.5M
- Permissions: rw-rw-r--
- Modification Time: 2023-02-20 14:45:22

3. /path/to/directory/file3.txt
- Size: 1.8M
- Permissions: rw-r--r--
- Modification Time: 2023-03-10 18:12:10



Total: 5.5M
```
## Testing:
Test cases are implemented in Check2.py that allows you to validate your work before submission. You may run a test case with a command such as:
  ```python3 CheckA2.py -f TestParseFileDetails```
  
## How It Works:
 - The parse_command_line_arguments function uses the argparse library to parse command-line arguments and returns the parsed arguments object.
 - `execute_find_command` takes a directory path, executes the find command using the os library, and returns the command output.
 - `parse_find_output` processes the output of the find command and returns a list of dictionaries containing file details.
 - `generate_detailed_report` takes the file information and prints a detailed report for each matching file.
 - `display_totals` prints the total number of matching files and the total disk space they occupy.
 
## Instructions:

### Milestone 1:
1. **Implement Command-Line Argument Parsing:**
   - Create the `parse_command_line_arguments` function using the `argparse` library to handle and parse command-line arguments.
   - Test the function with various inputs to ensure accurate parsing.

2. **Execute the Find Command:**
   - Implement the `execute_find_command` function to execute the `find` command for the specified directory using the `os` library.
   - Verify that the function can successfully capture and print the output of the `find` command.

3. **Test Script:**
   - Create a test script to ensure that the command-line argument parsing and `find` command execution work as expected.

### Milestone 2:
1. **Parse Find Command Output:**
   - Implement the `parse_find_output` function to process the output of the `find` command and extract relevant information about matching files.
   - Test the function with different `find` command outputs to ensure accurate parsing.

2. **Generate Detailed Report:**
   - Implement the `generate_detailed_report` function to create a detailed report for each matching file, including file size, permissions, and modification time.
   - Verify that the function produces a readable and informative report.

3. **Display Totals:**
   - Implement the `display_totals` function to calculate and display the total number of matching files and the total disk space they occupy.
   - Test the function with various inputs to ensure accurate calculation and display.

4. **Final Testing:**
   - Test your script with different directory paths and search criteria to ensure robustness.

### Getting Started:
1. Clone the assignment repository from the provided GitHub link.
2. Create a new branch for your work.
3. Implement the functions outlined in Milestone 1 and 2.
4. Create a test script to verify the correctness of your functions.
5. Test your script with different directory paths and search criteria to ensure robustness.

### Submission:
1. Push your code to GitHub before the assignment deadline.
2. Make sure your code is well-documented, follows best practices, and includes the test script.
3. Additionally, submit your code to Blackboard using the provided link.

### Evaluation Criteria:
Your assignment will be evaluated based on the correct implementation of the specified functions, adherence to best coding practices, clarity and completeness of documentation, and the effectiveness of test cases.

Good luck, and feel free to reach out if you have any questions or encounter challenges during the assignment.
