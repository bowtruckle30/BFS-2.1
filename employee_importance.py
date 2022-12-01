"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        ## DFS Solution:
        ## T.C = O(n)
        ## S.C = O(n)
        
        res = [0]
        hm = {}
        for emp in employees:
            hm[emp.id] = emp
            
        def dfs(id):
            res[0] += hm[id].importance
            
            for i in hm[id].subordinates:
                dfs(i)
        
        dfs(id)
        return res[0]
            
        ################################################    
        ## BFS Solution:
        ## T.C = O(n)
        ## S.C = O(n)
        
        hm = {}
        q = []
        for emp in employees:
            hm[emp.id] = emp
            if emp.id == id:
                q.append(emp.id)
        
        imp = 0
        
        while q:
            emp_id = q.pop(0)
            for e_id in hm[emp_id].subordinates:
                q.append(e_id)
            
            imp += hm[emp_id].importance
        
        return imp
                
                
                
                
                
                
                
                
                
                
                
                
                
                