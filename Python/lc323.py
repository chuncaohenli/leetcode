# union find 
# 1. some point may never appear in edges
# 2. need to judge both start point and end point
class Solution(object):
    
    def getRoot(self,edge):
        while self.dic[edge] != edge:
            edge = self.dic[edge]
        return edge
    
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.dic = {}
        for e in edges:
            if e[0] in self.dic and e[1] not in self.dic:
                self.dic[e[1]] = self.getRoot(e[0])
            elif e[1] in self.dic and e[0] not in self.dic:
                self.dic[e[0]] = self.getRoot(e[1])
            elif e[0] in self.dic and e[1] in self.dic:
                self.dic[self.getRoot(e[1])] = self.getRoot(e[0])
            else:
                self.dic[e[0]] = e[0]
                self.dic[e[1]] = e[0]
        result = 0
        for k,v in self.dic.iteritems():
            if k==v:
                result += 1
                
        for i in range(n):
            if i not in self.dic:
                result += 1
        print self.dic
        return result
