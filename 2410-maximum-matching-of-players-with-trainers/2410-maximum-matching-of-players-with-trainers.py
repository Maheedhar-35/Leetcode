class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        
        players_i = 0
        trainers_j = 0
        
        while players_i < len(players) and trainers_j < len(trainers):
            if trainers[trainers_j] >= players[players_i]:
                players_i += 1
            trainers_j += 1
            
        return players_i