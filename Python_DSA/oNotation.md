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
5. O(nm)
6. O(1) - Constant Time

- The following complexity functions represent complexities itself that
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
- 