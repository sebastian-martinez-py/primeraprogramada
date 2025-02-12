class PlayComparator:
    @staticmethod
    def compare(A, B):
        
        if A.date < B.date:
            return -1
        elif A.date > B.date:
            return 1

        
        if A.qtr < B.qtr:
            return -1
        elif A.qtr > B.qtr:
            return 1

        
        if A.yards < B.yards:
            return -1
        elif A.yards > B.yards:
            return 1

        
        if A.time < B.time:
            return -1
        elif A.time > B.time:
            return 1

        return 0  
