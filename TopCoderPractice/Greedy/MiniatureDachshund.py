class MiniatureDachshund:
    def maxMikan(self, mikan, weight):
        count = 0
        mikan = sorted(mikan)
        i = 0
        while weight < 5000 and i < len(mikan):
            if weight + mikan[i] <= 5000:
                count += 1
                weight += mikan[i]
                i += 1
            else:
                break
        return count


print(MiniatureDachshund().maxMikan([100, 100, 100, 100, 50],
                                    4750))
