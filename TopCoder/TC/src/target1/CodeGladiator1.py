import sys
import os


def GetJumpCount(input1, input2, input3):
    cnt = 0
    for n in input3:
        if input1 >= n:
            cnt += 1
        else:
            h = input1
            cnt += 1
            while h < n:
                h += input1 - input2
                cnt += 1
    return cnt


# ip1 = int(input());
# ip2 = int(input());
# ip3_cnt = 0
# ip3_cnt = int(input())
# ip3_i = 0
# ip3 = []
# while ip3_i < ip3_cnt:
#     ip3_item = int(input());
#     ip3.append(ip3_item)
#     ip3_i += 1
#
# output = GetJumpCount(ip1, ip2, ip3)

print(GetJumpCount(10, 1, [10]))
