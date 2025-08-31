

def find_two_sum(arr, target_val):
    prev_nums = {}   # keep track of numbers we've come across (number -> index)

    for idx, val in enumerate(arr):
        needed = target_val - val  

        # if we've already seen the matching number, then we found the pair
        if needed in prev_nums:
            return [prev_nums[needed], idx]  

        prev_nums[val] = idx  
    
    return []


if __name__ == "__main__":
    sample_nums = [2, 7, 11, 15]
    print("Result indices:", find_two_sum(sample_nums, 9))
    print("Check again:", find_two_sum(sample_nums, 22))  
