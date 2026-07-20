Student Grade Management System
===============================

### **Concepts Covered:**

*   Lists
*   Dictionaries
*   Loops
*   Adding, removing, and updating elements
*   Input validation and error handling

***

### **Goal:**

Write a Python program that manages student names and their grades using a **dictionary**.  
The program should allow the user to add, update, remove, and display students through a simple text-based menu.

***

### **Program Requirements**

1.  Use a global dictionary called `students`:
    
        students = {}
    
    *   **Keys:** student names (strings)
    *   **Values:** lists of grades (integers)
2.  Implement the following **functions**:
    
    #### 1. `add_student()`
    
    *   Prompts the user for a **student’s name** and a **grade**.
    *   Adds the student and their grade as a list (e.g., `{"Alice": [90]}`).
    *   If the student already exists, print an error message and do not overwrite the entry.
    *   Validate all user input:
        *   Student name must not be empty.
        *   Grade must be a valid integer (use `isdigit()` **or** `try/except` when converting input to `int`).
    
    > 💡 _Tip:_ You can later extend this function to add **multiple grades** to a student. For example:
    > 
    >     students["Alice"].append(95)   # Adds another gradestudents["Alice"].extend([88, 92])  # Adds multiple grades at once
    
    #### 2. `update_grade()`
    
    *   Prompts for a **student’s name**.
    *   If the student is not found, display an error message.
    *   Otherwise:
        *   Display the list of current grades.
        *   Ask for the **index** (starting from 0) of the grade to update.
        *   Validate that the entered index is an integer **and** exists in the list.
        *   You should use a `try/except` block to handle **`IndexError`** in case the user enters an invalid index.
        *   Then prompt for a new valid grade and replace the old value.
    
    #### 3. `remove_student()`
    
    *   Prompts for a **student’s name** to remove.
    *   If found, remove the entry and confirm.
    *   If not found, display an error message.
    
    #### 4. `display_students()`
    
    *   Displays all students and their grades in a clear format.
    *   If there are no students, print “No students in the system.”
    
    #### 5. `main()`
    
    *   Runs a menu in a loop with these options:
        
            1. Add a new student2. Update a grade3. Remove a student4. Display all students5. Quit
        
    *   Based on user input, call the appropriate function.
    *   Validate menu choices (only accept numbers 1–5).
    *   The program ends when the user chooses **5\. Quit**.

***

### **Input Validation and Error Handling Notes**

*   Always validate user input:
    *   Student names should not be empty strings.
    *   Grades should be integers (use `.isdigit()` or `try/except`).
    *   Menu choices must be between 1 and 5.
*   When printing Error messages such as "Student already exists." you should use the format "Error: Student already exists."
*   When updating grades, use a `try/except` block to catch invalid index access:
    
        try:    students[name][index] = new_gradeexcept IndexError:    print("Error: Invalid index! Please try again.")
    

***

### **Sample Runs**

#### **1\. Add a new student**

    1. Add a new student2. Update a grade3. Remove a student4. Display all students5. QuitChoose an option: 1Enter the student's name: AliceEnter Alice's grade: 90Alice added successfully!

#### **2\. Update a grade**

    Choose an option: 2Enter the student's name: AliceCurrent grades for Alice: [90]Enter the index of the grade to update (starting from 0): 1Invalid index! Please try again.Enter the index of the grade to update (starting from 0): 0Enter the new grade: 95Alice's grade updated successfully!

#### **3\. Remove a student**

    Choose an option: 3Enter the student's name to remove: AliceAlice removed successfully!

#### **4\. Display all students**

    Choose an option: 4Student Grades:Bob: 85, 88Charlie: 92

#### **5\. Quit**

    Choose an option: 5Goodbye!

***

### **Example Full Run**

    1. Add a new student2. Update a grade3. Remove a student4. Display all students5. QuitChoose an option: 1Enter the student's name: AliceEnter Alice's grade: 90Alice added successfully!Choose an option: 1Enter the student's name: BobEnter Bob's grade: 85Bob added successfully!Choose an option: 4Student Grades:Alice: 90Bob: 85Choose an option: 2Enter the student's name: BobCurrent grades for Bob: [85]Enter the index of the grade to update (starting from 0): 0Enter the new grade: 88Bob's grade updated successfully!Choose an option: 4Student Grades:Alice: 90Bob: 88Choose an option: 5Goodbye!