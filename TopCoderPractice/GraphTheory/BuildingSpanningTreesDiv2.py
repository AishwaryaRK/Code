import itertools

class BuildingSpanningTreesDiv2:
    def getNumberOfSpanningTrees(self, n, x, y):
        connected_components = []
        for v1, v2 in zip(x, y):
            is_inserted = False
            for component in connected_components:
                if v1 and v2 in component:
                    return 0
                if v1 in component:
                    component.add(v2)
                    is_inserted = True
                elif v2 in component:
                    component.add(v1)
                    is_inserted = True
            if not is_inserted:
                connected_components.append({v1, v2})
        nodes = list(itertools.chain.from_iterable(connected_components))
        for i in range(1, n + 1):
            if i not in nodes:
                connected_components.append({i})
        print(connected_components)

        a = len(connected_components[0])
        b = len(connected_components[1])
        c = len(connected_components[2])
        return a*b*b*c + a*c*c*b + b*a*a*c


print(BuildingSpanningTreesDiv2().getNumberOfSpanningTrees(6,[1,1,2],[2,3,3]))
