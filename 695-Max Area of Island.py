def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = []
        c = 0
        for i in grid:
            if c == 0:
                c = len(i)
            row.extend(i)
        n = 0

        area = 0
        for i in range(len(row)):
            if row[i] == 1:
                if i%c!=0 and (i-1)>=0 and row[i-1] == 1:
                    total -= 1
                if i%c!=(c-1) and (i+1)<len(row) and row[i+1] == 1:
                    total -= 1
                if (i-c)>=0 and row[i-c] == 1:
                    total -= 1
                if (i+c)<(len(row)) and row[i+c] == 1:
                    total -= 1
        return total

if __name__ == '__main__':
    List = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    List2 =[[1],[1]]
    List3 = [[1,0],[1,0]]

    results = islandPerimeter(List)
    print results
