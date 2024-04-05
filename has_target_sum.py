'''
Write a function called hasTargetSum that receives two arguments:
an array of integers
a target integer
The function should return true if any pair of numbers in the array adds up to the target number.
'''

def hasTargetSum(int_arr, target):
     for i in range(len(int_arr)):
          for j in range(i +1, len(int_arr)):
               if (int_arr[i] + int_arr[j]) == target:
                    return True
     return False
               
def main():
     int_arr = [12, 3, 7, 89, 35]
     target = 42
     result = hasTargetSum(int_arr, target)
     print(result) #true

if __name__ == "__main__":
     main()