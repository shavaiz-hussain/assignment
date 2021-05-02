
def equilibriumPoint(arr, n):
    for i in range(n):
        leftsum = 0
        rightsum = 0
        for j in range(i):
            leftsum += arr[j]
        for j in range(i + 1, n):
            rightsum += arr[j]
        if leftsum == rightsum:
            return i + 1
    return -1


def validate_equilibrium_inputs(array, n):
    if n < 0 or n > len(array):
        raise Exception('Please add a validate N value')
    for a in array:
        if isinstance(a, int):
            if a < 0:
                raise Exception('value cannot be negative')
        else:
            raise Exception('value can only be integers')


def inputs():
    print('\033[93m' + "Please add space while entering numbers of array" + '\033[0m')
    print('\033[93m' + "Only add positive number" + '\033[0m')
    array = list(map(int, input("\nEnter the array : ").strip().split()))
    _n = int(input("Enter numbers of N : "))
    validate_equilibrium_inputs(array, _n)
    return equilibriumPoint(array, _n)


print(inputs())