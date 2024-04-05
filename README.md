# Target Sum Checker

The provided Python script contains a function called `hasTargetSum`, which receives two arguments:

1. An array of integers.
2. A target integer.

The function is designed to return `True` if any pair of numbers in the array adds up to the target number; otherwise, it returns `False`.

## Function Description

The `hasTargetSum` function iterates through all possible pairs of numbers in the input array and checks if their sum equals the target integer. If a pair with the target sum is found, the function returns `True`. If no such pair is found after checking all pairs, it returns `False`.

## Usage

To use the `hasTargetSum` function, you can call it with an array of integers and the target integer. For example:

```python
def main():
     int_arr = [12, 3, 7, 89, 35]
     target = 42
     result = hasTargetSum(int_arr, target)
     print(result) # Output: True

if __name__ == "__main__":
     main()
```

In this example, the script checks if there exists a pair of numbers in the array `[12, 3, 7, 89, 35]` that sums up to the target integer `42`. The function will return `True` because `12 + 30 = 42`.
