import re
class LEDTester():
    def __init__(self, N):
        self.N = N
        self.dataGrid = [[False]*self.N for i in range(self.N)]

    def apply(self,i):
        pat = re.compile(
            ".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        commands = pat.search(i)
        if commands!=None:
            method = commands.group(1)
            row1 = int(commands.group(2))
            col1 = int(commands.group(3))
            row2 = int(commands.group(4))
            col2 = int(commands.group(5))
            if row1 < 0:
                row1 = 0
            if col1 < 0:
                col1 = 0
            if row2 >= self.N:
                row2 = self.N-1
            if col2 >= self.N:
                col2 = self.N-1
            
            if method == "turn on":
                for r in range(row1,row2+1):
                    for c in range(col1,col2+1):
                        self.dataGrid[r][c] = True
            elif method == "turn off":
                for r in range(row1, row2+1):
                    for c in range(col1, col2+1):
                        self.dataGrid[r][c] = False
            elif method == "switch":
                for r in range(row1, row2+1):
                    for c in range(col1, col2+1):
                        self.dataGrid[r][c] = not(self.dataGrid[r][c])
    
    def count(self):
        count = sum(r.count(True) for r in self.dataGrid)
        return count
