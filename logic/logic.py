import os
import time

from initialization import constants
from initialization.helper_functions import HelperFunctions


class LogicCreator(object):

    def __init__(self):
        self.helper = HelperFunctions()
        self.dictionary_teams_general = self.helper.create_initial_team_dict()
        self.list_qualified_teams = []
        self.list_unqualified_teams = []
        self.text_location = os.path.join(os.getcwd(), "results", "text_files")
        self.third_place_teams_dict = {}
        self.third_place_teams =[]

    def create_group_scores(self):
        '''
        We will traverse through each group and make the scores
        We will need to keep track of the score and then somehow transfer it to excel
        :return:updated dict_general
        '''
        for i in range(0, len(constants.TEAMS)):
            string_text_file = ""
            string_text_file += constants.GROUPS[i] + "\n"
            '''
            ROUND 1
            '''
            outcome, score_team1, score_team2 = self.helper.computize_group_scores()
            # * will be used as a split
            match_string = constants.TEAMS[i][0] + "-" + constants.TEAMS[i][
                1] + "*" + str(score_team1) + "-" + str(score_team2) + "\n"
            if outcome == 1:
                # start computing in dict
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[2]] += score_team1
            elif outcome == 2:
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[2]] += score_team1

                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[2]] += score_team2
            else:
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[2]] += score_team1
            string_text_file += match_string
            #time.sleep(0.5)
            outcome, score_team1, score_team2 = self.helper.computize_group_scores()
            # * will be used as a split
            match_string = constants.TEAMS[i][2] + "-" + constants.TEAMS[i][
                3] + "*" + str(score_team1) + "-" + str(score_team2) + "\n"
            if outcome == 1:
                # start computing in dict
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[2]] += score_team1
            elif outcome == 2:
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[2]] += score_team1

                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[2]] += score_team2
            else:
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[2]] += score_team1
            string_text_file += match_string
            #time.sleep(0.5)
            '''
            ROUND 2
            '''
            outcome, score_team1, score_team2 = self.helper.computize_group_scores()
            # * will be used as a split
            match_string = constants.TEAMS[i][1] + "-" + constants.TEAMS[i][
                3] + "*" + str(score_team1) + "-" + str(score_team2) + "\n"
            if outcome == 1:
                # start computing in dict
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[2]] += score_team1
            elif outcome == 2:
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[2]] += score_team1

                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[2]] += score_team2
            else:
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[2]] += score_team1
            string_text_file += match_string
            #time.sleep(0.5)
            outcome, score_team1, score_team2 = self.helper.computize_group_scores()
            # * will be used as a split
            match_string = constants.TEAMS[i][0] + "-" + constants.TEAMS[i][
                2] + "*" + str(score_team1) + "-" + str(score_team2) + "\n"
            if outcome == 1:
                # start computing in dict
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[2]] += score_team1
            elif outcome == 2:
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[2]] += score_team1

                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[2]] += score_team2
            else:
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[2]] += score_team1
            string_text_file += match_string
            #time.sleep(0.5)
            '''
            ROUND 3
            '''
            outcome, score_team1, score_team2 = self.helper.computize_group_scores()
            # * will be used as a split
            match_string = constants.TEAMS[i][1] + "-" + constants.TEAMS[i][
                2] + "*" + str(score_team1) + "-" + str(score_team2) + "\n"
            if outcome == 1:
                # start computing in dict
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[2]] += score_team1
            elif outcome == 2:
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[2]] += score_team1

                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[2]] += score_team2
            else:
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][1]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][2]][constants.ATTRIBUTES[2]] += score_team1
            string_text_file += match_string
            #time.sleep(0.5)
            outcome, score_team1, score_team2 = self.helper.computize_group_scores()
            # * will be used as a split
            match_string = constants.TEAMS[i][0] + "-" + constants.TEAMS[i][
                3] + "*" + str(score_team1) + "-" + str(score_team2) + "\n"
            if outcome == 1:
                # start computing in dict
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[2]] += score_team1
            elif outcome == 2:
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[0]] += 3
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[2]] += score_team1

                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[2]] += score_team2
            else:
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[1]] += score_team1
                self.dictionary_teams_general[constants.TEAMS[i][0]][constants.ATTRIBUTES[2]] += score_team2

                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[0]] += 1
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[1]] += score_team2
                self.dictionary_teams_general[constants.TEAMS[i][3]][constants.ATTRIBUTES[2]] += score_team1
            string_text_file += match_string
            #time.sleep(0.5)
            '''
            ADD an extra line with some special characters to delimit when we write into excel between results and table data
            '''
            string_text_file += constants.SPECIAL_CHARS_DELIMITERS
            '''
            ADD IN THE DICTIONARY OF TEAMS THE DIFFERENCE
            '''
            for j in range(0, 4):
                self.dictionary_teams_general[constants.TEAMS[i][j]][constants.ATTRIBUTES[3]] = \
                    self.dictionary_teams_general[constants.TEAMS[i][j]][constants.ATTRIBUTES[1]] - \
                    self.dictionary_teams_general[constants.TEAMS[i][j]][constants.ATTRIBUTES[2]]
            # appeal result_table
            table_result, teams_ranking = self.create_result_table(constants.TEAMS[i][0], constants.TEAMS[i][1], constants.TEAMS[i][2], constants.TEAMS[i][3])

            #add in the special dictionary all place 3 teams
            dict_place_3 = self.dictionary_teams_general[teams_ranking[2]]
            self.third_place_teams_dict.update({teams_ranking[2]:dict_place_3})

            '''START COMPUTING INTO FILE'''
            with open(file=os.path.join(self.text_location, constants.GROUPS[i]), mode="w",
                      encoding="utf-8") as result_group:
                result_group.write(string_text_file)
                result_group.write(table_result)
            self.list_qualified_teams.append(teams_ranking[0])
            self.list_qualified_teams.append(teams_ranking[1])
        for key, dict_val in self.dictionary_teams_general.items():
            print(key, dict_val)
        #we will just need the qualified teams

        #print(self.list_qualified_teams)
        print(self.third_place_teams_dict)

    def compute_matches_second_stage(self):
        '''
        will compute the qualified teams from the groups and choose based on what group and rank it has if a rank 1 team plays with a rank 3 team or rank 2 team - for world cup source
        :return:LIST OF QUALIFIED TEAMS TO THE LAST 32 AND UPDATE DICT GENERAL
        '''
        dict_team_rank = self.helper.create_team_rank_place(self.list_qualified_teams)
        self.third_place_teams = self.arrange_dict_third_place_teams()
        print(self.third_place_teams)
        print(dict_team_rank)

    def create_result_table(self, team1, team2, team3, team4):
        '''
        :return:The function returns the results for every group. It returns a string that it will be computed at every group in the final part
        will just use a sorting method and create some dicts which are then actually ordered
        '''
        list_teams = [team1, team2, team3, team4]
        # we have 4 things already here
        sorted_dict = sorted(list_teams, key=lambda team: (self.dictionary_teams_general[team][constants.ATTRIBUTES[0]],
                                                           self.dictionary_teams_general[team][constants.ATTRIBUTES[3]],
                                                           self.dictionary_teams_general[team][
                                                               constants.ATTRIBUTES[1]]), reverse=True)
        # we now have the order, so we can create custom dicts to put in our text files
        string_sorted = ""
        list_items = []
        for sorted_item in sorted_dict:
            list_item = [sorted_item, self.dictionary_teams_general[sorted_item][constants.ATTRIBUTES[0]],
                         self.dictionary_teams_general[sorted_item][constants.ATTRIBUTES[1]],
                         self.dictionary_teams_general[sorted_item][constants.ATTRIBUTES[2]],
                         self.dictionary_teams_general[sorted_item][constants.ATTRIBUTES[3]]]
            list_items.append(list_item)
        counter = 1
        for idx in range(0, len(list_items)):
            # separation here will be .
            if idx == len(list_items): # 4+1
                string_line = str(counter) + "." + str(list_items[idx][0]) + "." + str(list_items[idx][1]) + "." + str(list_items[idx][2]) + "." + \
                              str(list_items[idx][3]) + "." + str(list_items[idx][4])
                string_sorted += string_line
            else:
                string_line = str(counter) + "." + str(list_items[idx][0]) + "." + str(list_items[idx][1]) + "." + str(
                    list_items[idx][2]) + "." + \
                              str(list_items[idx][3]) + "." + str(list_items[idx][4]) +"\n"
                string_sorted += string_line
            counter += 1
        return string_sorted, sorted_dict

    def arrange_dict_third_place_teams(self):
        teams = list(self.third_place_teams_dict.keys())
        sorted_dict = sorted(teams, key= lambda team : (self.dictionary_teams_general[team][constants.ATTRIBUTES[0]],
                                                                             self.dictionary_teams_general[team][constants.ATTRIBUTES[3]],
                                                                             self.dictionary_teams_general[team][constants.ATTRIBUTES[1]]), reverse=True)
        return sorted_dict[:8]



