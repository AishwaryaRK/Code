def optimal_sol(comp_usb, comp_ps2, comp_usb_ps2, mouses):
    total = comp_usb + comp_ps2 + comp_usb_ps2
    cost = 0
    mouses = sorted(mouses, key=lambda mouse: mouse[0])
    for mouse in mouses:
        if mouse[1] == 'USB':
            if comp_usb > 0:
                comp_usb -= 1
                cost += mouse[0]
            elif comp_usb_ps2 > 0:
                comp_usb_ps2 -= 1
                cost += mouse[0]
        else:
            if comp_ps2 > 0:
                comp_ps2 -= 1
                cost += mouse[0]
            elif comp_usb_ps2 > 0:
                comp_usb_ps2 -= 1
                cost += mouse[0]
    mouses_purchased = total - (comp_usb + comp_ps2 + comp_usb_ps2)
    return mouses_purchased, cost


str = raw_input()
comp_usb = int(str.split(" ")[0])
comp_ps2 = int(str.split(" ")[1])
comp_usb_ps2 = int(str.split(" ")[2])
m = int(raw_input())
mouses = []
for i in range(0, m):
    s = raw_input().split(" ")
    mouses.append((int(s[0]), s[1]))
a, b = optimal_sol(comp_usb, comp_ps2, comp_usb_ps2, mouses)
print a,b
