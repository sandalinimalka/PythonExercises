def cutdown_list(numbers):
    list_new = []
    for number in numbers:
        if number % 2 == 0:
            list_new.append(number)
    return (list_new)

list = [2,5,6,10,13,25,56]

print(f"Original list is here: {list}")
print(f"Cut down list is here: {cutdown_list(list)}")