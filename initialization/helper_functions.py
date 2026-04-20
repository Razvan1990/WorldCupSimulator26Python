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


    def computize_scores(self):
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

    def create_team_rank_place(self, list_qualified_teams: list[str]) -> dict[str, str]:
        string_groups = "ABCDEFGHIJKL"
        dict_team_rank = dict()
        group_count= 0
        for i in range (0, len(list_qualified_teams), 2):
            count = 1
            key1 = str(count)+string_groups[group_count]
            key2 = str(count+1)+string_groups[group_count]
            dict_team_rank.update({key1: list_qualified_teams[i]})
            dict_team_rank.update({key2: list_qualified_teams[i+1]})
            group_count += 1
        return dict_team_rank

    @staticmethod
    def choose_random_third_place_team(list_third_place_teams: list[str]) -> int:
        return random.randint(0, len(list_third_place_teams)-1)

    @staticmethod
    def move_list_elements(list_elements: list[str], index_element1:int, index_element2:int) -> None:
        list_elements.insert(index_element1, list_elements.pop(index_element2))

    @staticmethod
    def check_lists(list1: list[str], list2:list[str]) ->bool:
        for element in list1:
            if element not in list2:
                return False
        return True

    @staticmethod
    def compute_string_winners(list_winners: list[str]) -> str:
        string_winners = ""
        for i in range (0, len(list_winners)):
            if i == len(list_winners)-1:
                string_winners += list_winners[i]
            else:
                string_winners += list_winners[i]+"\n"
        return string_winners

    @staticmethod
    def remove_unqualified_elements(list_qualified_teams: list[str], list_unqualified_teams: list[str]) -> None:
        for element in list_unqualified_teams:
            list_qualified_teams.remove(element)

    def check_third_place_team_is_qualified(self,team:str, list_third_place_teams: list[str]) -> bool:
        return team in list_third_place_teams

    def generate_player_goals(self, goals_scored_team:int, threshold) -> int:
        '''

        :param goals_scored_team:
        :param threshold: it is a random threshold that can be modify based on your preferences
        :return: number goals scored by a player
        '''
        if goals_scored_team - threshold < 2:
            threshold = 0
        player_goals = random.randint(0, goals_scored_team - threshold)
        if player_goals < threshold:
            return random.randint(0, threshold)
        return player_goals


