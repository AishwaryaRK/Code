# Given an array of positive numbers and a positive number ‘k’,
# find the maximum sum of any subarray of size ‘k’.


def max_sub_array_of_size_k(k, arr):
  s = 0
  max_sum = 0
  for i in range(0, len(arr)-k+1):
    if i == 0:
      s = sum(arr[:k])
    else:
      s = s - arr[i-1] + arr[i+k-1]
    if s > max_sum:
      max_sum = s
  return max_sum


def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
