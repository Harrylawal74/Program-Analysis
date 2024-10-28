def analyser(nums):
  count = 0
  x = nums[0]
  for i in range(0, len(nums)-2):
    if nums[i+2] == (nums[i] * nums[i+1]) and (nums[i] * nums[i+1] * nums[i+2]) != 0:
      count += 1

    elif nums[i+2] != (nums[i] * nums[i+1]) and (nums[i] * nums[i+1] * nums[i+2]) != 0:
      continue

    else:
      return count
      break

  return count


numbers = [1, 2, 2, 0, 2, 4, 8, 32]
analyser(numbers)
