import random

from initialization import constants


class HelperFunctions(object):

    def create_team_goal_dict(self):
        '''
        Function to create the team goal dictionary
        :return: a dictionary which defines for every team the best player
        '''
        team_player_dict = dict()
        for i in range (0, len(constants.TEAMS)):
            for j in range (0, len(constants.TEAMS[i])):
                team_player_dict.update({constants.TEAMS[i][j]: constants.PLAYERS[i][j]})
        return team_player_dict


    def create_initial_team_dict(self):
        '''
        Function which creates an initial dictionary of all teams and the points, goals scored, conceived, difference
        :return:  dictionary with attributes for each team
        '''
        dict_initialization = dict()
        for i in range (0, len(constants.TEAMS)):
            for j in range (0, len(constants.TEAMS[i])):
                key = constants.TEAMS[i][j]
                team_dict = dict()
                for attribute in constants.ATTRIBUTES:
                    team_dict.update({attribute: 0})
                #now we add in the dict_initialization for every team with the initial attributes
                dict_initialization.update({key: team_dict})
        return dict_initialization

    @staticmethod
    def create_random_score():
        return random.randint(0, 6)


    def computize_group_scores(self):
        '''
        Function to check the result of the match and also store the scores
        :return: number which defines the result
        '''
        score_match1 = self.create_random_score()
        score_match2 = self.create_random_score()
        if score_match1 > score_match2:
            return 1, score_match1, score_match2
        elif score_match1 < score_match2:
            return 2, score_match1, score_match2
        else:
            return 3, score_match1, score_match2

    def order_desc_scores(self, points1, points2, points3, points4):
        pass
