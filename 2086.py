class Solution:
    @staticmethod
    def minimumBuckets(hamsters: str) -> int:
        '''
        . - empty
        ! - food
        H - hungry hamster
        '''

        hamsters = [*hamsters]
        food = 0
        for i in range(len(hamsters)):
            if hamsters[i] == 'H':
                if i - 1 >= 0 and hamsters[i - 1] == '!':
                    pass
                elif i + 1 < len(hamsters) and hamsters[i + 1] == '.':
                    food += 1
                    hamsters[i + 1] = '!'
                elif i - 1 >= 0 and hamsters[i - 1] == '.':
                    food += 1
                    hamsters[i - 1] = '!'
                else:
                    return -1
        return food
