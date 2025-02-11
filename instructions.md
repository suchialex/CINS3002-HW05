# Instructions  

- Use Ctrl + / to toggle commenting

## The objective of this homework assignment is
- to write the contents of the file (employees.csv) to a multi-dimensional list
- we will add new employees to this list
- we will lookup employee from this list
- we will update employee data in this list
- we will delete employee from this list
- we will display employees from this list
- after all these operations are done, we will write this list back to the file

🚩 Note: Changes will not reflect in the file immediately. You will see the changes in the list.

<details>
  <summary>
    ✅ Get everything started
  </summary>

  - Copy main.py, validations.py, functions.py, list_functions.py from HW04
  - We won't be using functions.py or list_functions.py, but it will be nice to have all your modules in one place
  - Download employees.csv from https://github.com/suchialex/CINS3002-HW05/blob/main/employees.csv
  - Download suchi_pretty_print.py if you need it https://github.com/suchialex/CINS3002-HW05/blob/main/suchi_pretty_print.py
  - Create a new file named multilist_functions.py, write an import statement to import the validations module
  - In **main.py** edit the import statement to import from multilist_functions module
</details>

## In multilist_functions.py

<details>
  <summary>
    ✅ Define employee_operations()
  </summary>

  - It is a void function that takes no parameters
  - Write print statement to print `Employee Management`
</details>


<details>
  <summary>
    ✅ Define function file_to_list
  </summary>
  
  - **Objective**: This function will read the contents of the employees.csv file line by line and split each line into a list using the delimiter ; and  store this list in a list. This multi-dimensional list is returned to the calling function.
  - This function does not accept any parameters and returns a list
  - In the function body,
    - First, create an empty list (this list will contain all the employees data)
    - Using the context manager, open the file employees.csv in read mode and store it in a file pointer
      - 🚩 Use exception handling since file is being opened in read mode (in the except clause, print `file not found` and return an empty list)
    - Using this file pointer, start a for loop with a loop variable of your choice (this variable will read each line of the file)
      - Remove the newline character from the loop variable
      - Convert the string stored in the loop variable to a list using the delimiter ⏩ 7-20b
        - 🚩 Name this list differently than the empty list above
      - Now append this list to the empty list you created above
    - Outside the for loop return the list
    - Using list comprehension rewrite the above statements as concisely as possible ⏩ 7-25
</details>


<details>
  <summary>
    ✅ Call the function file_to_list()
  </summary>

   - Inside employee_operations(), after the print statement, call the file_to_list()
   - Store the returned list in a variable
   - Print the returned list (you may use suchi_print(), after importing it)
   - 📜 Test your code
     - See if the multi-dimensional list is being printed correctly
     - Clear the contents of the file and ensure an empty list is printed (🚩 replace the contents after testing)
     - Misspell the file name and ensure an empty list is printed
</details>


<details>
  <summary>
    ✅ Define display_employees()
  </summary>
  
  - The objective of this function is to display all employees in a tabular format
  - This function takes one parameter - the employee multi-dimensional list
  - This function returns nothing, so it is a void function
  - In the function body
    - Start a for loop to go over the multi-dimensional list, choose a name for the loop variable
    - Using the appropriate indices of the loop variable, print ID, Name, Department and Salary in a formatted tabular fashion
</details>


<details>
  <summary>
    ✅ Call display_employees()
  </summary>
  
  - Inside employee_operations(), after the call to file_to_list() function, call the display_employees() by passing the employees list (obtained from the file_to_list function) as an argument
  - 📜 Test your code - all employee data should be displayed in a tabular format
  - If code executes correctly, you may comment out this function call
</details>

## In validations.py

<details>
  <summary>
    ✅ Define generate_employee_id_multilist()
  </summary>
  
  - The objective of this function is to generate the next employee ID
  - This function takes one parameter - the employee multi-dimensional list
  - This function returns a numeric string
  - In the function body
    - Check if there are any employees in the list, if not, return a default numeric string, maybe `1234` ⏩ Tutorial: 7-12
    - Get the last employee from the multidimesional list and store it in a variable (this will be a list) ⏩ Tutorial: 7-6b
    - Get the first element of from the list above, that is the last employee ID and store in a variable ⏩ Tutorial: 7-6a
    - 💡 You may consolidate the above two steps into one by using two sets of square brackets
    - Convert it to an integer and add 1 to it
    - Return this after converting it to a string
</details>


## In multilist_functions.py

<details>
  <summary>
    ✅ Define add_employee()
  </summary>
  
  - The objective of this function is to add a new employee to the multilist
  - This function takes one parameter - the employee multi-dimensional list
  - This function returns the modified multi-dimensional list
  - In the function body
    - Get the employee ID by calling the generate_employee_id_multilist and store it in a variable
    - 🚩 You may have to import the validations module
    - Get the first name, last name, department, salary of the employee using the appropriate validation functions
    - Concatenate first name and last name with a space in between
    - Create a list (choose a name for this list) of id, name, department and salary in that order ⏩ Tutorial: 7-3
    - Append the above list to the employees multidimensional list passed as parameter
    - Return the multidimensional list
</details>

<details>
  <summary>
    ✅ Call add_employee
  </summary>

  - Inside employee_operations(), after the commented display_employees() function call, call add_employee by passing the employees list returned by file_to_list as an argument
  - Store the returned list in the same employees list variable (for simplicity)
  - 📜 Test your code - Add a new employee and see if the employees list is modified correctly
  - If code works correctly, you may comment out this function call
</details>


<details>
  <summary>
    ✅ Define lookup_employee()
  </summary>

  This function takes two parameters 
  - the employees list 
  - the employee_id we are trying to lookup
  - It returns two values
    - boolean - True if the employee is found, False if not
    - index (the integer position in the employees list where this employee was found, we don't find the employee, we will return 0)
  - In the function body
    - Start a for loop to go over the multi-dimensional employee list, choose a name for the loop variable, (each employee list will be stored in this variable, one at a time)
    - Using an if statement and the in operator, check if the employee_id (passed as parameter) is present in the list stored in the loop variable
    - If yes,
      - Get the index of the employee stored in the loop variable in the multi-dimensional list
      - Using the loop variable's appropriate indices, print the Name, Department and Salary
      - return True and the index obtained above
    - Outside the if block, 
    - print `Employee Not Found`
    - return False and 0

</details>



<details>
  <summary>
    ✅ Call the lookup_employee()
  </summary>

  - Inside employee_operations(), after the commented add_employee() function call, ask the user to provide the employee ID that needs to be looked up using input statement
  - Call the lookup_employee() passing TWO arguments, the multi-dimensional list obtained earlier and the employee id from the above step
  - Store the returned values in two variables
  - Check if the first variable is False, if yes, print employee not found
  - 📜 Test your code
    - Enter employee ID 1235 and see if the correct values are being printed
    - Enter employee ID 54, it should print `Employee Not Found`
  - If code works correctly, you may comment out this function call
</details>


<details>
  <summary>
    ✅ Define update_employee_name()
  </summary>
  
  - The objective is to get an employee ID and call the lookup_function to see if that employee exists in the employees list
  - If yes, we use the index returned by the lookup function and update the name which will be at [index][1] position
  - This function takes the employee multi-dimensional list as parameter and returns the modified employee list
  - In the function body
    - Ask the user to provide the employee ID whose name needs to be updated and store in a variable
    - call the lookup function using the employee list passed as the parameter and the above variable
    - store the returned values in two variables
    - check if the first variable is True, if yes
      - Ask the user for first name and last name by calling the appropriate validations functions
      - Concatenate the first and last names with a space in between 
      - Modify the [index][1] position in the employees multi-dimensional list with the new full name ⏩ Tutorial: 7-13a
    - Outside the if block, return the employees list
</details>



<details>
  <summary>
    ✅ Call update_employee_name
  </summary>
  
  - In employee_operations(), call the update_employee_name by passing the employees list returned by file_to_list as an argument.
  - Store the returned list in the same employees list variable (for simplicity)
  - 📜 Test your code - update name and print the employees multidimenstional list to check if it is modified accordingly
  - If code works correctly, you may comment out the function call
</details>


<details>
  <summary>
    ✅ Define update_employee_dept()
  </summary>
  
  - The objective is to get an employee ID and call the lookup_function to see if that employee exists in the employees list
  - If yes, we use the index returned by the lookup function and update the department which will be at [index][2] position
  - This function takes the employee multi-dimensional list as parameter and returns the modified employee list
  - In the function body
    - Ask the user to provide the employee ID whose department needs to be updated and store in a variable
    - call the lookup function using the employee list passed as the parameter and the above variable
    - store the returned values in two variables
    - check if the first variable is True, if yes
      - Ask the user for department by calling the appropriate validation function
      - Modify the [index][2] position in the employees multi-dimensional list with the new department ⏩ Tutorial: 7-13a
    - Outside the if block, return the employees list
</details>



<details>
  <summary>
    ✅ Call update_employee_dept
  </summary>
  
  - In employee_operations(), call the update_employee_dept by passing the employees list returned by file_to_list as an argument
  - Store the returned list in the same employees list variable (for simplicity)
  - 📜 Test your code - update department and print the employees multidimenstional list to check if it is modified accordingly
  - If code works correctly, you may comment out the function call
</details>


<details>
  <summary>
    ✅ Define update_employee_salary()
  </summary>
  
  - Use the same code logic as update_employee_dept and write code to update the salary
  - 🚩 Modify at the appropriate index position
  - Return the employees list
</details>



<details>
  <summary>
    ✅ Call update_employee_salary
  </summary>
  
  - In employee_operations(), call the update_employee_salary by passing the employees list returned by file_to_list as an argument
  - Store the returned list in the same employees list variable (for simplicity)
  - 📜 Test your code - update salary and print the employees multidimenstional list to check if it is modified accordingly
  - If code works correctly, you may comment out the function call
</details>




<details>
  <summary>
    ✅ Define delete_employee()
  </summary>
  
  - The objective is to ask the employee to enter the employee ID to be deleted and delete the corresponding elements from the employees list
  - This function accepts one parameter - the employee list
  - It returns one parameter - the modified employee list
  - In the function body
    - Ask the user for the employee ID to be deleted and store in a variable
    - Call the lookup function using the employees list passed as the parameter and the employee ID above
    - Store the returned values in two variables
    - If the first returned variable is True,
      - Write a statement to delete the element at the index position of the multi-dimensional employees list ⏩ Tutorial: 7-10b
    - Outside the if block, return the employees multi-dimensional list
</details>



<details>
  <summary>
    ✅ Call the delete_employee() function
  </summary>
  
  - In employee_operations(), call the delete_employee by passing the employees list returned by file_to_list as an argument
  - Store the returned list in the same employees list variable (for simplicity)
  - 📜 Test your code - delete employee 1234 and print the employees multidimenstional list to check if it is modified accordingly
  - If code works correctly, you may comment out the function call

</details>



<details>
  <summary>
    ✅ Define list_to_file()
  </summary>
  
  - The objective is to write all the list elements back to the file
  - This function accepts one parameter, the employee multi-dimensional list
  - This function returns nothing, so it is a void function
  - In the function body
    - Using a context manager, open the file employees.txt in **write mode** and get the file object/pointer
    - Use a for loop to go over the multi-dimensional list passed as the parameter, choose a loop variable name (it stores each employee data in a list)
      - Convert this list to a string with a delimiter ⏩ Tutorial: 7-20c, choose name for this string
      - Concatenate a newline character to this string and write to the file
      - 💡 You may consolidate the above two steps into one
</details>


<details>
  <summary>
    ✅ Call the list_to_file() function
  </summary>
  
  - Call the function list_to_file() passing the employee multi-dimensional list as argument
</details>


<details>
  <summary>
    ✅ Modify employee_operations() function
  </summary>

  - Place your function calls in the appropiate if-elif blocks
  - file_to_list() will be the first function call
  - inside a while loop that exits when the user presses x or X
    - print the menu of options
    - ask the user what option he/she chooses using input statement
    - place the function calls in the correct if-elif-else blocks as per your menu
    - 🚩 Remember to place add_employee in its own while loop to keep adding new employees until user presses **n** or **N**
  - Place list_to_file() outside the while loop

</details>
