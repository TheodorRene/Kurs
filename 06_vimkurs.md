def fizzbuzz(i):
    answer = ""
    if i % 3 == 0:
        answer += "Fizz"
    if i % 5 == 0:
        answer += "Buzz"
    return answer or str(i)



