"""
Link: https://www.codingninjas.com/studio/problems/ninja%E2%80%99s-training_3621003
Problem:
- Each day you can perform 3 activities which can give u points
- Once u do activity 1, next day you cant do the same activity again
- Consider you do 1 activity each day, following condition whats the max you can earn

Solution
- Reverse the situation from Day 0 <- Day n
- dp[day][activity_index] = max points you can get by doing activity_index on day 
- First day -> dp[0] = arr[0] (THIS IS UR FIRST DAY)
- Next day onwards, if you do activity_index then prev_day you cant pick the same activity index
    - cur_activity != cur_activity
    - dp[day][cur_activity] = max(dp[day][cur_activity], arr[day][cur_activity] + dp[day-1][cur_activity])
"""
  
def ninjaTraining(k: int, arr: List[List[int]]) -> int:
    days = len(arr)

    dp = [[0 for _ in range(3)] for _ in range(days)]
    dp[0] = arr[0]

    for day in range(1,days):
        for cur_activity in range(3):
            for prev_activity in range(3):
                if prev_activity == cur_activity:
                    continue
                # print(day, cur_activity, prev_activity)
                dp[day][cur_activity] = max(dp[day][cur_activity], arr[day][cur_activity] + dp[day-1][prev_activity])
    

    # print(dp)
    return max(dp[-1])


# REVERSE APPROACH -> Ending at last
def ninjaTraining(self, arr):
    arr = arr
    n = len(arr)

    # dp[i][j] => Max profit you can make starting at day "i" and "picking up jth cost" on day "i"
    dp = [[float("-inf") for _ in range(3)] for _ in range(n)]
    dp[-1] = arr[-1].copy() # last day cant move ahead

    for day in range(n-2,-1,-1):
        for cur_act in range(3):
            for next_act in range(3):
                if next_act != cur_act:
                    dp[day][cur_act] = max(dp[day][cur_act], arr[day][cur_act]+dp[day+1][next_act])
    return max(dp[0])
