# RECURSION
- Defined as simply a function that calls itself.
- Antonym for a recursive algorithm is an **"iterative algorithm."** In theory,
all iterative algorithms can be made recursive through for and while loops.

## RECURSION EXAMPLE 1
```python
def outPut(i):
    print(i)
    outPut(i + 1)
outPut(1)
```

- The following example shows a recursion in python format. The source code
starts with an argument of 1, prints 1 then calls in the user-defined function 
within and adds it by 1 which then throws in a new argument (2) which then
kicks off another iteration of the user-defined function.
- The problem with this code is that it will run endlessly and hit python's 
**RecursionError** which specifically states that the recursion iteration has 
reached **1000** times which is the default recursion depth of python. One can
identify the recursion depth of their python through compiling this python code:

```python
import sys
print(sys.getrecursionlimit())
```

- A simple conditional statement can fix an endless recursive algorithm:
```python
def outPut(i):
    if i > 10:
        return
    print(i)
    outPut(i + 1)

outPut(1)
```

## RECURSION EXAMPLE 2:
```python
def outPut(i):
    if i > 3:
        return
    print(i)
    outPut(i + 1)
    print(f"End of call where i = {i}")
    return

outPut(1)
```

- The following example shows the **"return"** capability of python and how 
significant its role is given recursive functions with base cases (conditional statements
to prevent infinite loops).
- The following output of the algorithm would be as follows:

```
1
2
3
End of call where i = 3
End of call where i = 2
End of call where i = 1
```

- The following is a classic example that the order of lines of code given a recursive 
algorithm is important. At a glance, it should be expected the the string print statements
should all print from 1 - 3 however, due to the return syntax, python goes back to the previous
**"saved"** function call.

### Explanation of Example 2
- **Step 1:** outPut(1) executes with the argument 1. Since 1 < 3, conditional statement does not hold true
- and proceeds to the next line of code to execute.
- **Step 2:** outPut(1) prints 1 in the terminal.
- **Step 3:** outPut(2) is created (with its own code which is outPut()) due to the addition.
- **Step 4:** outPut(2) executes with the argument 2. Since 2 < 3, conditional statement does not hold true
and proceeds to the next line of code to execute.
- **Step 5:** outPut(2) prints 2 in the terminal.
- **Step 6:** outPut(3) is created (with its own code which is outPut()) due to the addition.
- **Step 7:** outPut(3) executes with the argument 3. Since 3 !> 3, conditional statement does not hold true
and proceeds to the next line of code to execute.
- **Step 8:** outPut(3) prints 3 in the terminal.
- **Step 9:** outPut(4) is created (with its own code which is outPut()) due to the addition.
- **Step 10:** outPut(4) executes with the argument 4. Since 4 > 3, conditional statement does holds true and
 returns to outPut(3)

- **Note**: As the functions are created and iterated on the next one as the algorithms of each functions
proceed, the preceeding functions are saved. In this case, return is understood as a **"go back to the
previous"** function.

- **Step 11:** outPut(3) prints "End of call where i = 3" then returns to outPut(2).
- **Step 12:** outPut(2) prints "End of call where i = 2" then returns to outPut(1).
- **Step 13:** outPut(1) prints "End of call where i = 1". 

## USE-CASE FOR RECURSIONS
- A classic example for a proper an appropriate use for recursion is translating the fibonacci sequence
into a recursive algorithm. This is due to the fact that the expression for fibonacci sequence translates
perfectly into a recursive algorithm.
- Fibonacci Sequence Expression: **F_n = F_n-1 + F_n-2**

**Effective Recursive Algorithm Example**
```python
def get_fibonacci(n):
    if n <= 1:
        return n
        
    one_back = get_fibonacci(n - 1)
    two_back = get_fibonacci(n - 2)
    
    return one_back + two_back
```

### Explanation for Effective Recursive Algorithm Example

#### If get_fibonacci(0) or get_fibonacci(1):
- **Step 1:** get_fibonacci(0) or get_fibonacci(1) would simply output 0 and 1 respectively due to the fact 
that the conditions state as such (and there wouldn't be two addens that would add to such respectively).

#### If get_fibonacci(3)
- **Step 1:** get_fibonacci(3) is not <= 1.
- **Step 2:** get_fibonacci(3) executes one_back which then executes its own code.
- **Step 3:** get_fibonacci(2) is not <= 1.
- **Step 4:** get_fibonacci(2) executes one_back which then executes its own code.
- **Step 5:** get_fibonacci(1) == 1 which returns the value 1 back to the function get_fibonacci(2).
- **Step 6:** get_fibonacci(2) saves the value 1 to one_back and executes two_back or get_fibonacci(0).
- **Step 7:** get_fibonacci(0) <= 1 which returns the value 0 back to the function get_fibonacci(2).
- **Step 8:** get_fibonacci(2) saves the value 0 to two_back.
- **Step 9:** get_fibonacci(2) goes back to get_fibonacci(3) with the value 1.
- **Step 10:** get_fibonacci(3) saves the value 1 to one_back and executes two_back or get_fibonacci(1).
- **Step 11:** get_fibonacci(1) == 1 which returns the value 1 back to the function get_fibonacci(3).
- **Step 12:** get_fibonacci(3) saves the value 1 to two_back.
- **Step 13:** get_fibonacci(3) returns the value 1 + 1 which is 2 as its final step.