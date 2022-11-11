class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter = [0 for _ in range(26)]
        maxFreq = 0
        numsWithMaxFreq = 0
        
        for task in tasks:
            idx = ord(task)-65
            taskCounter[idx] += 1
            
            if taskCounter[idx] == maxFreq:
                numsWithMaxFreq += 1
            elif taskCounter[idx] > maxFreq:
                maxFreq = taskCounter[idx]
                numsWithMaxFreq = 1
        
        numParts = maxFreq-1
        partLen = n-(numsWithMaxFreq-1)
        
        availableSlots = numParts*partLen
        availableTasks = len(tasks)-(maxFreq*numsWithMaxFreq)
        
        idleSlots = max(0,availableSlots-availableTasks)
        
        return len(tasks)+idleSlots
        
        
        
  
