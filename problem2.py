
# Employee Impotance

# (https://leetcode.com/problems/employee-importance/)


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
        
        d = {}
        for emp in employees:
            if emp.id not in d:
                d[emp.id] = emp
        
        total_imp = 0
        
        queue = []
        queue.append(id)
        
        while len(queue) != 0:
            popped_id = queue.pop(0)
            emp = d[popped_id]
            
            total_imp += emp.importance
            
            for sub_id in emp.subordinates:
                queue.append( sub_id )
            
            
        return total_imp