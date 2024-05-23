"""
PROBLEM: https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
- Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)} => RES: 2 60
- Each job is (job_id, job_deadline, profit)
- You need to do the job on or before `job_deadline` to get profit
- Consider each job to be 1 unit/day of effort

SOLUTION:
- Find max_deadline, make boolean array [1->max_deadline] which indicates if your doing some job at that given day
- Sort based on profit
- For deadline, profit in sorted(jobs -> based on profit):
    - Check if you can do the job on day `deadline`, `deadline`- 1, `deadline`- 2 and so on
    - Basically check if 1<-deadline, any day is False (False -> no job decided to be done)
    - In case you find a free day, increment profit, njobs


"""

'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):
        max_deadline = max([x.deadline for x in jobs])
        
        # Are you doing any job on given day (1->max_deadline)
        # True -> scheduled to do, False -> nothing
        job_status = [False for _ in range(max_deadline+1)] 
        
        jobs = sorted(jobs,key = lambda x:x.profit, reverse=True)

        njobs, profit = 0,0
        for job in jobs:
            deadline = job.deadline
            cur_profit = job.profit
            
            # can you do this job within deadline -> check backwards
            for day in reversed(range(1, deadline+1)):
                if job_status[day] is False: # no job is being done at this day
                    njobs += 1
                    profit += cur_profit
                    job_status[day] = True # marking it as scheduled to do
                    break # done
        
        return [njobs, profit]
                