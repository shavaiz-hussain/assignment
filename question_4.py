class meeting:

    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos


def maxMeeting(l, n):
    ans = []
    l.sort(key=lambda x: x.end)
    ans.append(l[0].pos)
    time_limit = l[0].end
    for i in range(1, n):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end
    print(len(ans))


def inputs():
    print('\033[93m' + "Please add space while entering numbers of array" + '\033[0m')
    s = list(map(int, input("\nEnter the S[] : ").strip().split()))
    f = list(map(int, input("\nEnter the F[] : ").strip().split()))
    n = len(s)
    l = []
    for i in range(n):
        l.append(meeting(s[i], f[i], i))
    return maxMeeting(l, n)


inputs()
