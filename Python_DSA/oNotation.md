# BIG O NOTATION

## ALGORITHMS

### Algorithm
- Step-by-step instructions for a computer to follow to do a function.
- Takes an input and produces an output. 

### LeetCode Algorithm Tips
- Algorithms in LeetCode are deterministic. Same input should always produce the same output.
- Algorithms should cater to multiple test cases.

## BIG O

- Big O Notation describes the computational complexity of an algorithm.
- It basically tells the programmer the number of operations an algorithm must do especially if
the input increases.
- It is determined by two factors namely the "Time Complexity" and the
"Space Complexity"

### Big O: Time Complexity
- Refers to the amount of time, steps, or operations an algorithm does
given an input array or string.
- "As the input grows, how fast or how many operations does the 
algorithm takes to finish?"

### Big O: Space Complexity
- Refers to the amount of memory utilized by the algorithm given an input.
- "As the input grows, how much more memory does the algorithm uses?"

## COMPLEXITY

### How does complxity work?
- Complexity is described as a mathematical function wherein one of 
the more essential values is "n".
- n usually refers to the length of the input array or string.

### Different Complexities
1. O(n) - Linear Time
2. O(n^2) - Quadratic Time
4. O(log n) - Logarithmic Time
5. O(nm) - Two Variables
6. O(1) - Constant Time
7. O(2^n) -  Exponential Time
8. O(n^3) - Cubic Time 

- The following are some of the most common complexity functions 
that represent complexities itself which 
can be used to describe the time complexity or space complexity of your
algorithm (how fast or how much memory your algorithm is respectively).
- "The time complexity of my algorithm is O(n)"
- "The space complexity of my algorithm is O(log n)."

### Calculating Complexity

#### Example:
Create an algorithm that would find the max value given an input array
of numbers.

The logic of the algorithm would be as follows:

```
1. Create a variable maxNum = 0
2. Iterate over each element of the array.
3. If num > maxNum, maxNum == num. (Update)
4. print(maxNum)
```

- The following algorithm has a time complexity of O(n).
- If n is the number of inputs, then given that the aforementioned algorithm which
will iterate at each input n, the function expresses that exact number of operations
hence O(n). If there are 100 inputs, n = 100. If there are 400000 inputs, then 
n = 400000, and so on...

#### How was O(n) calculated?
- When ascertaining the complexity of an algorithm, the following steps
should be taken into account:

```
Step 1: Identify the input (how many the algorithm takes) and its potential length.
Step 2: Check how many loops the algorithm does to the input.
Step 3: Based on the number of loops the algorithm has with respect to the input,
a corresponding time complexity would be assigned to it which would help you 
determine the time complexity of the algorithm.
```

#### Complexity Rules

1. **Remove the constants**
- Time & Space complexity only cares about how the algorithm scales in terms of 
both of these factors as the input scales. 
- This means that regardless if the algorithm is O(2n) or O(n + 500), these 
constants would not matter regardless because they will always be O(n) at the 
end of the day. This is due to the fact that in this instance, as n scales up, the 
constant would always scale it based on its value. Complexity only cares about how the
algorithm would scale. Not the specifics on how EXACTLY it scales.

2. **Retain the Highest Term**
- Always consider the complexity of the algorithm as n tends to approach infinity.
- This means that given a complexity O(n^2 + 500n + 2n), the final complexity is O(n^2).
- In analyzing/calculating the complexity of an algorithm, one must assume the worst case
scenario. The worst case scenario is always the input size approaching infinity (or at least a
large size). When applied at the aforementioned function, 500n and 2n is inconsequential because
n^2 is so large, the remaining two terms are like ants compared to the highest scaling term.

#### Time Complexity Cheat Sheet
1. **Constant Complexity O(1)**
- Algorithm has no loops.
- Refers to a complexity wherein the algorithm does not care for the number of inputs.
It will always execute at one pass given any input. 

**Example 1:**
```python
def get_first_item(nums):
    return nums[0]
```

**Example 2**
```python
def addSum(nums):
    return nums + 1
```

2. **Linear Time O(n)**
- Algorithm has one loop.
- Refers to a complexity where in the algorithm iterates over the whole length
of the input one time.

**Example 1:**
```python
def iterate(nums)
    for i in nums:
        return i
```

**Example 2:**
```python
def addAll(nums):
    for i in nums:
        return nums + 1
```

3. **Quadratic Time O(n^2)**
- Algorithim has 1 nested loop.
- Refers to a complexity where in the algorithm has a main loop that iterates
over the whole length of the input one time and a **nested** loop that runs 
within it. 

**Example 1:**
```python
def iterate(nums):
    for i in nums:
        for j in nums:
            print(j)
```

**Example 2:**
```python
def addAll(nums):
    for i in nums:
        for j in nums:
            return i + j
```

4. **Logarithmic Time O(log n)**