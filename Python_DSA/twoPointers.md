# TWO POINTERS

## What are Pointers in DSA?
* Pointers refer to markers or references to elements inside a data structure.
* These are commonly variables that point or store an element in an array. This is for various purposes but commonly is utilized for tracking that specific element in an array. 

## What is Two Pointers in DSA?
* Two pointers is a common methodology in solving DSA problems.
* Simply involves two pointers/variables that references an element that move along an array for specific purposes.
* The examples below will present an example of two pointers in action.

### Example 1

**Given a string, return true if it is a palindrome, false otherwise.**
A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".

#### Solution:
```python
class Palindrome:
    def __init__(self, string):
        self.string = string
        pass

    def is_pal(self):
        left = 0
        right = len(self.string) - 1

        while left < right:
            if self.string[left] != self.string[right]: return False

            left += 1
            right -= 1

            return True

instance1 = Palindrome("racecar")
instance2 = Palindrome("hello")

print(instance1.is_pal())
print(instance2.is_pal())
```

#### Explanation

* Use two pointers: left starts at the first character, and right starts at the last.
* Compare both characters; if they don't match, return false.
* Move left forward and right backward until they meet; if no mismatch is found, return true.

### Example 2
**Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.** For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

#### Solution
```python
class TwoSum:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def two_check(self):
        left = 0
        right = len(self.arr) - 1

        while left < right:
            curr = self.arr[left] + self.arr[right]
            if curr == self.target: return True

            if curr > self.target:
                right -= 1
            else:
                left += 1

        return False

instance1 = TwoSum([3, 6, 21, 23, 25], 27)
print(instance1.two_check())
```

#### Explanation

* If the sum is too large, move the right pointer to the left to try a smaller number.
* If the sum is too small, move the left pointer to the right to try a larger number.
* Repeat until the sum matches the target or no valid pairs remain.