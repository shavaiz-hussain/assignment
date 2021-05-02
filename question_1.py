
def activity_selection(start, finish, n):
    i = 0
    activites = 1
    for j in range(n):
        if start[j] >= finish[i]:
            activites += 1
            i = j
    return activites


def inputs():
    print('\033[93m' + "Please add space while entering number for start[] and finish[]" + '\033[0m')
    _start = list(map(int, input("\nEnter the start[] : ").strip().split()))
    _finish = list(map(int, input("\nEnter the finish[] : ").strip().split()))
    _n = int(input("Enter numbers of N : "))
    return activity_selection(_start, _finish, _n)


print(inputs())
