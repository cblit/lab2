print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
     print("“Enter some numbers separated by commas (e.g. 5, 67, 32)”  ")

def calc_average(tem):
    length = len(tem)
    ave = 0
    index = 0
    ave = sum(tem)/ len(tem)
    return ave

def get_user_input():
    x = input()
    y = x.split(",")
    y = [int(num.strip()) for num in y]
    return y

def find_min_max(tem):
    largest = max(tem)
    smallest = min(tem)
    return largest, smallest

def sort_temperature(tem):
    tem.sort()
    return tem

def calc_median_temperature(temsorted):
    length = len(temsorted)
    if length%2 == 0:
        middle1 = temsorted[length // 2]
        middle2 = temsorted[length // 2 - 1]
        median = (middle1 + middle2) / 2
    elif length % 2 == 1:
        median = temsorted[(length+1)//2 -1]
    return median

def main():
    display_main_menu()
    z = get_user_input()
    average = calc_average(z)
    print("average is " + str(average))
    max , min = find_min_max(z)
    print("min is " + str(min) )
    print("max is " + str(max) )
    temsorted = sort_temperature(z)
    median = calc_median_temperature(temsorted)
    print("median number is " + str(median))

main()

