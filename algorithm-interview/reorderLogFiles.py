class Solution:
    def reorderLogFiles(self, logs):
        lets, digs = [], []
        for log in logs:
            #dig
            if ord('0') <= ord(log[-1]) and ord(log[-1]) <= ord('9'):
                digs.append(log)
            # let
            else:
                lets.append((
                    ' '.join(
                        log.split()[1:]
                        )
                    , log.split()[0]
                    ))
        # lets 
        lets.sort()
        for i in range(len(lets)):
            lets[i] = lets[i][1] + ' ' + lets[i][0]
            
        return lets + digs

s = Solution()
print(s.reorderLogFiles(["a1 9 2 3 1"]))