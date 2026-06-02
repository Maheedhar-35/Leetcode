class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        landcomplete=[x + y for x, y in zip(landStartTime,landDuration )]
        watercomplete=[x + y for x, y in zip(waterStartTime,waterDuration )]
        n = len(landStartTime)
        m = len(waterStartTime)
        earliest = float('inf')
        
        for i in range(n):
            for j in range(m):

                land_finish = landcomplete[i]
                water_start = max(land_finish, waterStartTime[j])
                seq1_finish = water_start + waterDuration[j]
                
                water_finish = watercomplete[j]
                land_start = max(water_finish, landStartTime[i])
                seq2_finish = land_start + landDuration[i]
                
                earliest = min(earliest, seq1_finish, seq2_finish)
                
        return earliest
        