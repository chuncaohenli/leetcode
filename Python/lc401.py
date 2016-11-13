class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]
        hdic = {0: ['0']}
        mdic = {0: ['00']}
        for i in range(1, 12):
            tmp = i
            key = 0
            for j in range(4):
                if tmp & 1 == 1:
                    key += 1
                tmp = tmp >> 1
            value = str(i)
            if key not in hdic:
                hdic[key] = [value]
            else:
                hdic[key].append(value)

        for i in range(1, 60):
            tmp = i
            key = 0
            for j in range(6):
                if tmp & 1 == 1:
                    key += 1
                tmp = tmp >> 1
            if i < 10:
                value = '0' + str(i)
            else:
                value = str(i)
            if key not in mdic:
                mdic[key] = [value]
            else:
                mdic[key].append(value)
        result = []

        i=0
        while i<4 and i<=num:
            j = num-i
            if j>5:
                i+=1
                continue
            for h in hdic[i]:
                for m in mdic[j]:
                    result.append(h + ':' + m)
            i+=1
        return result
