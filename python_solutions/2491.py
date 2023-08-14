class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Solution Overview
        # if we divide the total sum of skill with n/2 then it should be divisible and we should be able to form such teams
        n = len(skill)
        total_skill_sum = sum(skill)
        team_skill = total_skill_sum//(n//2)
        if team_skill * (n//2) != total_skill_sum:
            return -1
        freq_cnt = {}
        for sk in skill:
            if sk in freq_cnt:
                freq_cnt[sk] += 1
            else:
                freq_cnt[sk] = 1
        chem = 0
        for sk in freq_cnt:
            pl1_sk = sk
            pl2_sk = team_skill-pl1_sk
            if pl2_sk not in freq_cnt:
                return -1
            if pl1_sk == pl2_sk:
                if freq_cnt[pl1_sk]%2 == 1:
                    return -1
                team_cnt = freq_cnt[pl1_sk]//2
            else:
                if freq_cnt[pl2_sk] != freq_cnt[pl1_sk]:
                    return -1
                team_cnt = freq_cnt[pl1_sk]
            freq_cnt[pl1_sk] = 0
            freq_cnt[pl2_sk] = 0
            chem += team_cnt * (pl1_sk * pl2_sk)
        return chem
