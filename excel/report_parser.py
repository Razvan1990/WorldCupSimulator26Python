import os
from logic.logic import LogicCreator
from initialization import constants


class TxtParser(object):

    def __init__(self):
        self.logic = LogicCreator()

    def parse_results_stages(self, text_file):
        change_list_flag = False
        with open(file=os.path.join(self.logic.text_location, text_file), mode="r", encoding="utf-8") as f:
            list_needed_1 = []
            list_needed_2 = []
            lines_first_part = []
            lines_second_part = []
            lines = f.readlines()
            '''
            First time we will see where we have the special character to delimit the lists
            '''

            for i in range(0, len(lines)):
                if lines[i] == constants.SPECIAL_CHARS_DELIMITERS:
                    change_list_flag = True
                    continue
                if change_list_flag:
                    lines_second_part.append(lines[i][:-1])
                else:
                    lines_first_part.append(lines[i][:-1])
            '''
            COMPUTE FIRST LIST
            '''
            matches = []
            scores = []
            for line in lines_first_part:
                match = line.split("*")[0]
                score = line.split("*")[1]
                matches.append(match)
                scores.append(score)
            list_needed_1.append(matches)
            list_needed_1.append(scores)

            '''
            COMPUTE SECOND LIST
            '''
            rank = []
            teams = []
            points = []
            goals_scored = []
            goals_received = []
            difference_goals = []
            for line in lines_second_part:
                r = line.split(".")[0]
                t = line.split(".")[1]
                p = line.split(".")[2]
                gs = line.split(".")[3]
                gr = line.split(".")[4]
                dg = line.split(".")[5]
                rank.append(r)
                teams.append(t)
                points.append(p)
                goals_scored.append(gs)
                goals_received.append(gr)
                difference_goals.append(dg)
            list_needed_2.append(rank)
            list_needed_2.append(teams)
            list_needed_2.append(points)
            list_needed_2.append(goals_scored)
            list_needed_2.append(goals_received)
            list_needed_2.append(difference_goals)
            return list_needed_1, list_needed_2

    def parse_results_knockouts(self, text_file):
        with open(file=os.path.join(self.logic.text_location, text_file), mode="r", encoding="utf-8") as f:
            #reset back to false
            change_list_flag = False
            lines = f.readlines()
            #split when we have delimiter characters
            part1_list =[]
            part2_list =[]

            for i in range(0, len(lines)):
                if lines[i] == constants.SPECIAL_CHARS_DELIMITERS:
                    change_list_flag = True
                    continue
                elif change_list_flag and i == len(lines) - 1:
                    part2_list.append(lines[i])
                elif change_list_flag:
                    part2_list.append(lines[i][:-1])
                else:
                    part1_list.append(lines[i][:-1])

            first_list =[]

            list_matches = []
            list_scores = []
            penalties = []
            for result in part1_list:
                match = result.split("*")[0]
                score = result.split("*")[1]
                penalty = result.split("*")[2]
                list_matches.append(match)
                list_scores.append(score)
                penalties.append(penalty)
            first_list.append(list_matches)
            first_list.append(list_scores)
            first_list.append(penalties)
            return first_list, part2_list

    def parse_final_stats_file(self, text_file):
        with open(file=os.path.join(self.logic.text_location, text_file), mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            list_rankings = []

            for line in lines:
                temp_list = []
                team = line.split("*")[0]
                goals_scored = line.split("*")[1]
                goals_received = line.split("*")[2]
                difference_goals = line.split("*")[3][:-1]
                temp_list.append(team)
                temp_list.append(goals_scored)
                temp_list.append(goals_received)
                temp_list.append(difference_goals)
                list_rankings.append(temp_list)
            return list_rankings

    def parse_goals_players_file(self, text_file):
        with open(file=os.path.join(self.logic.text_location, text_file), mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            list_players = []
            for line in lines:
                temp_list = []
                player = line.split("*")[0]
                team = line.split("*")[1]
                goals_scored = line.split("*")[2][:-1]
                temp_list.append(player)
                temp_list.append(team)
                temp_list.append(goals_scored)
                list_players.append(temp_list)
            return list_players







