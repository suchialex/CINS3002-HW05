# Instructions  

- Use Ctrl + / to toggle commenting

## The objective of this homework assignment is
- to write the contents of the file (employees.csv) to a multi-dimensional list
- we will lookup employee from this list
- we will update employee name in this list
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
      - 🚩 Use exception handling since file is being opened in read mode (in the else clause return an empty list)
    - Using this file pointer, start a for loop with a loop variable of your choice (this variable will read each line of the file)
    - Strip off the newline character from the loop variable
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
     - Clear the contents of the file and ensure an empty list is printed
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
  
  - After the call to file_to_list() function, call the display_employees() by passing the employees list (obtained from the file_to_list function) as an argument
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
    - Check if there are any employees in the list, if not, return a default numeric string, maybe `1001`
    - Get the last employee from the multidimesional list and store it in a variable (this will be a list)
    - Get the first element of from the list above, that is the last employee ID and store in a variable
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
    - Check 
</details>


<details>
  <summary>
    ✅ Define lookup_employee()
  </summary>

  This function takes two parameters 
  - the employees list 
  - the employee_id we are trying to lookup 

  It returns two values 
  - found (boolean) - True if the employee is found, False if not
  - index (the integer position in the employees list where this employee was found, we don't find the employee, we will return 0)

In the function body

  - Start a for loop to go over the multi-dimensional employee list, choose a name for the loop variable, (each employee list will be stored in this variable, one at a time)
  - Using an if statement and the in operator, check if the employee_id (passed as parameter) is present in the list stored in the loop variable
  - If yes,
    - Get the index of the employee stored in the loop variable in the multi-dimensional list
    - Using the loop variables' appropriate indices, print the Name, Department and Salary
    - return True and the index obtained above
  - If not
    - print employee not found
    - return False and 0

</details>



<details>
  <summary>
    ✅ Call the lookup_employee()
  </summary>

  - After the file_to_list() function call, ask the user to provide the employee ID that needs to be looked up using input statement
  - Call the lookup_employee() passing TWO arguments, the multi-dimensional list obtained earlier and the employee id from the above step
  - Store the returned values in two variables
  - Check if the first variable is False, if yes, print employee not found
  - Execute your code and enter employee ID 1004 and see if the correct values are being printed
  - Execute your code again and enter employee ID 54, it should print employee not found
</details>





<details>
  <summary>
    ✅ Define update_employee_name()
  </summary>
  The objective is to get an employee ID and call the lookup_function to see if that employee exists in the employees list, if yes, we use the index returned by the lookup function and update the name which will be at [index][1] position. This function takes the employee multi-dimensional list as parameter and returns the modified employee list back<br>

  
In the function body

  - Ask the user to provide the employee ID whose name needs to be updated and store in a variable
  - call the lookup function using the employee list passed as the parameter and the above variable
  - store the returned values in two variables
  - check if the first variable is True, if yes
    - Ask the user to provide a new first name by calling the validate_first_name() function
    - Ask the user to provide a new last name by calling the validate_first_name() function
    - 🚩 You may have to import the validations module
    - concatenate the first and last names with a space in between 
    - then modify the [index][1] position in the employees multi-dimensional list with the new full name
  - Outside the if block, return the employees list
</details>

## In main.py

<details>
  <summary>
    ✅ Call update_employee_name
  </summary>
  After the display_employees, call the update_employee_name by passing the employees list returned by file_to_list as an argument. Store the returned list in the same employees list variable (for simplicity)
</details>


<details>
  <summary>
    ✅ Define delete_employee()
  </summary>
  The objective is to ask the employee to enter the employee ID to be deleted and delete the corresponding elements from the employees list

  - This function accepts one parameter - the employee list
  - It returns one parameter - the modified employee list

  In the function body<br>

  - Ask the user for the employee ID to be deleted and store in a variable
  - Call the lookup function using the employees list passed as the parameter and the employee ID above
  - Store the returned values in two variables
  - If the first returned variable is True,
    - Write a statement to delete the element at the index position of the multi-dimensional employees list
  - Outside the if block, return the employees multi-dimensional list
</details>

## In main.py

<details>
  <summary>
    ✅ Call the delete_employee() function
  </summary>
  You may comment out update_employee_name() call<br>
  Call the delete_employee() by passing the employee list as the argument

</details>

## In multilist_functions.py

<details>
  <summary>
    ✅ Define list_to_file()
  </summary>
  The objective is to write all the list elements back to the file<br>

  - This function accepts one parameter, the employee multi-dimensional list
  - This function returns nothing, so it is a void function

    In the function body<br>

  - Using a context manager, open the file employees.txt in write mode (not append mode) and get the file object/pointer
  - Use a for loop to go over the multi-dimensional list passed as the parameter, choose a loop variable name
  - Loop variable stores each employee data in a list, so convert this list to a string with a delimiter ⏩ 7-0c, choose  name for this string
  - To this string add a newline character and write to the file

</details>

## In main.py

<details>
  <summary>
    ✅ Call the list_to_file() function
  </summary>
  You may comment the delete_employee() function<br>
  Call the function list_to_file passing the employee multi-dimensional list as argument
</details>


<details>
  <summary>
    ✅ Place your function calls in the appropiate if-elif blocks
  </summary>

  - file_to_list() will be the first function call
  - print the menu of options
  - ask the user what option he/she chooses using input statement
  - place the function calls in the correct if-elif-else blocks as per your menu
  - you may use pass statement in the blocks for which we haven't written functions for
  - list_to_file will be the last function call in main body
  - If you'd like to write the while loop, until user presses x or X, you are encouraged to do so. 🚩 BUT, make sure file_to_list and list_to_file function calls are OUTSIDE the while loop
  - Write code documentation for all your functions

</details>
