
def min_max_sum_len(*args, list_of_nums):
    if len(args) == 0:
        print("Error: at list of enter one number")
        return

    res_min, res_max, res_sum, res_length = args[0], args[0], 0, 0
    for num in args:
        if num > res_max:
            res_max = num
        if num < res_min:
            res_min = num

        res_length += 1
        res_sum += num

        list_of_nums.append(num)

    return res_min, res_max, res_sum, res_length
print(min_max_sum_len(1, 2, 3, 4, 5, 6, list_of_nums= []))