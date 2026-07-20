### **Concepts Covered:**

`try`, `except`, `else`, `finally`, input validation, arithmetic operations, division by zero handling

***

### **Description**

Create a **calculator program** that performs basic arithmetic operations with built-in **error handling**.

*   Define a `calculator()` function which will contain the whole logic of your program.
*   The program should ask the user to:
    *   Enter **two numbers**.
    *   Choose an **operation**: `+`, `/`, `-`, `*`.
*   The program should handle the following errors:
    *   **`ValueError`** if the user enters something that isn’t a valid number.
    *   **`ZeroDivisionError`** if the user attempts to divide by zero.
    *   Any **unexpected errors** should be caught using a generic `except` block with an appropriate message.
*   Use a `finally` block to display `"Calculation complete."` regardless of success or failure.
*   The program should allow the user to **continue calculating** until they type `"exit"`.

***

### **Example Interaction: (follow the exact interaction, no deviation, else Codegrade tests will fail)**

    Enter the first number: 10 Enter the second number: 2 Choose an operation (+, -, *, /): / Result: 5.0 Calculation complete.Enter the first number: 5 Enter the second number: 0 Choose an operation (+, -, *, /): / Cannot divide by zero! Calculation complete.Enter the first number: 12 ]Enter the second number: abc Invalid input! Please enter a valid number. Calculation complete.Enter "exit" at any time to quit.