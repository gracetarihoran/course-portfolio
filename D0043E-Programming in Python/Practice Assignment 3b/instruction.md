**Mini-Project: Simple Banking System**
---------------------------------------

***

### **Learning Goals**

*   Understand how to use conditionals (`if`, `elif`, and `else`) in Python.
*   Practice using user input with the `input()` function.
*   Develop a menu-based program to perform different tasks.
*   Learn how to validate user input and perform error handling.
*   Reinforce the use of variables and arithmetic operations to manage data.

***

### **Task**

In a file named `bank.py`, complete the following tasks:

***

### **Starting Balance**

*   Declare a variable `balance` and assign the initial value of `1000`.

***

### **Menu Interface**

*   Display the following menu to the user in the exact format:
    
        Welcome to Simple Bank!1. Check Balance2. Deposit Money3. Withdraw Money4. Exit
    
*   Prompt the user to **choose an option** from the menu by entering `1`, `2`, `3`, or `4`.
    

***

### **Functionalities**

Use an `if-elif-else` statement to handle the users choice. For each possible input, your code will do the following:

1.  **Option 1: Check Balance**
    
    *   Print the current balance in the following format:
        
            Your current balance is: $[balance]
        
2.  **Option 2: Deposit Money**
    
    *   Prompt the user to input the amount to deposit.
        
    *   Update the `balance` by adding the deposit amount.
        
    *   Print the updated balance in the following format:
        
            Enter the amount to deposit: [amount]You have successfully deposited $[amount]. Your new balance is: $[balance]
        
3.  **Option 3: Withdraw Money**
    
    *   Prompt the user to input the amount to withdraw.
        
    *   If the withdrawal amount is **less than or equal to the current balance**:
        
        *   Deduct the amount from the `balance`.
            
        *   Print the updated balance in the following format:
            
                Enter the amount to withdraw: [amount]You have successfully withdrawn $[amount]. Your new balance is: $[balance]
            
    *   If the withdrawal amount is **greater than the current balance**:
        
        *   Print an error message in this format:
            
                Enter the amount to withdraw: [amount]Insufficient balance! You only have $[balance] in your account.
            
4.  **Option 4: Exit**
    
    *   Print a goodbye message:
        
            Thank you for using Simple Bank! Goodbye!
        

***

### **Error Handling**

*   If the user inputs an option that is not `1`, `2`, `3`, or `4`, display the following message:
    
        Invalid choice! Please select an option between 1 and 4.
    

***

### **Example Run**

    Welcome to Simple Bank!1. Check Balance2. Deposit Money3. Withdraw Money4. ExitEnter your choice: 1Your current balance is: $1000