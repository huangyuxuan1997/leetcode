class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for i in range(R):
            for j in range(C):
                res.append([i, j])
        res.sort(key=lambda a: abs(a[0] - r0) + abs(a[1] - c0))
        return res
