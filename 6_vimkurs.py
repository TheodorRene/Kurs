def fizzbuzz(num):
    answer = ""
    if num % 3 == 0:
        answer += "Fizz"
    if num % 5 == 0:
        answer += "Buzz"
    return answer or str(num)

print([fizzbuzz(i) for i in range(1, 100)])


print("hello world")

# [[1,2,3],[3,4,5]]
# [1,2,3,3,4,5]
# 3
# Refakturer if setningen og funksjonsbruken
def median_of_multiple_arrays(l):
    flat_list = []
    for sublist in l: #FLATTEN
        for item in sublist:
            flat_list.append(item)
    flat_list.sort() #SORT
    # FINN MEDIAN
    length = len(flat_list)
    median_lower = flat_list[int(length/2)-1]
    median_higher = flat_list[int((length/2))]
    avg_median = (median_lower + median_higher)/2
    if len(flat_list)%2==0: #even
        return avg_median
    else: #odd
        return flat_list[len(flat_list)//2]

l_odd = [[3,6,9],[1,5,4], [7,2,8]]
l_even = [[4,2],[5,1],[6,3]]

def flatten(l):
    new_l = []
    for el in l:
        for item in el:
            new_l.append(item)
    return sorted(new_l)

print(flatten(l_even))
print(median_of_multiple_arrays(l_odd))
