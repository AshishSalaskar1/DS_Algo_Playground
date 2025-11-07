"""
This is exactly same as BOOK ALLOCATION PROBLEM and PAINTERS PARTITION PROBLEM
"""
class Solution:
    def check_nstudents_needed(self, arr, max_pages_held):
        # check how many students you need  such that max_pages_held_by_each is max_pages_held
        n_students = 1
        cpages = 0
        for x in arr:
            if cpages+x <= max_pages_held:
                cpages += x
            else:
                cpages = x
                n_students += 1
        return n_students

    def splitArray(self, arr: List[int], ns: int) -> int:
        n = len(arr)
        if ns==1: # only 1 student -> then he will read all books
            return sum(arr)
        
        if ns > n: #  book allocation impossible - each students needs atleast one book
            return -1

        lo = max(arr) # min result -> each person gets one book, so max in this case is max(arr)
        hi = sum(arr) # max result -> you give all the books to single person

        res = -1
        while lo <= hi:
            mid = lo + ((hi-lo)//2)
            
            students_needed = self.check_nstudents_needed(arr, mid)

            # lets say ur mid needs 10 studs which is more then given students.
            # then you need to increase ur mid (if nstudents are lower, then they will get more pages per student to read)

            if students_needed > ns:
                lo = mid+1
            else:
                res = mid
                hi = mid-1

        # you can return LO also here -> BINARY SEARCH OPPOSITE POLARITY CONCEPT
        return res
            