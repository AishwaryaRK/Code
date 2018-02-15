import math


class BearPaints:
    # def maxArea(self, W, H, M):
    #     if W * H <= M:
    #         return W * H
    #     else:
    #         if W >= H:
    #             W -= 1
    #         else:
    #             H -= 1
    #         return self.maxArea(W,H,M)

    def maxArea(self, W, H, M):
        if W * H <= M:
            print("1-" + str(W * H))
            return W * H
        x = int(math.sqrt(M))
        print(x)
        if W >= x and H >= x:
            print("2-" + str(x * x))
            return x * x
        else:
            if W >= x:
                W -= 1
            if H >= x:
                H -= 1
            return self.maxArea(W, H, M)


print(BearPaints().maxArea(1000000, 1000000, 720000000007))
