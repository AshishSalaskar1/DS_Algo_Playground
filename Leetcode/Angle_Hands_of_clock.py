class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        
        m = minutes * 6
        h = (hour*30) + (minutes * 30)/60
        
        # print(m)
        # print((minutes * 30)/60)
        
        res = abs(m-h)
        return min([res,abs(360-res)])
        
