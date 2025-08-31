# Trying out Kadane's Algorithm to find the largest sum of a contiguous subarray.
# Time: O(n), Space: O(1) 

def max_subarray(nums):
    # Just starting with the first value as the "best" we know so far
    current_best = nums[0]
    running_total = nums[0]

    # Looping through rest of the list
    for i in range(1, len(nums)):
        num = nums[i]

        # At each step: do we start fresh from this number, or continue the running sum?
        running_total = max(num, running_total + num)

        # Update max if needed
        if running_total > current_best:
            current_best = running_total
        # else: just keep the old best (not writing an else branch here, but I could)

        # Debugging print (commented out, might be handy later)
        # print(f"i={i}, num={num}, running_total={running_total}, best={current_best}")

    return current_best

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  
    result = max_subarray(arr)
    print("Max Subarray Sum is:", result)
