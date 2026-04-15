import os
from logic.logic import LogicCreator
from initialization import constants


class TxtParser(object):

    def __init__(self):
        self.logic = LogicCreator()
        self.change_list_flag = False

    def parse_results(self, text_file):
        with open(file=os.path.join(self.logic.text_location, text_file), mode="r", encoding="utf-8") as f:
            list_needed_1 = []
            list_needed_2 = []
            lines_first_part = []
            lines_second_part = []
            lines = f.readlines()
            '''
            First time we will see where we have the special character to delimit the lists
            '''

            for i in range(1, len(lines)):
                if lines[i] == constants.SPECIAL_CHARS_DELIMITERS:
                    self.change_list_flag = True
                    continue
                if self.change_list_flag:
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
