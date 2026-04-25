import os
import random

from initialization import constants
from initialization.helper_functions import HelperFunctions


class LogicCreator(object):

    def __init__(self):
        self.helper = HelperFunctions()
        self.dictionary_teams_general = self.helper.create_initial_team_dict()
        self.list_qualified_teams = []
        self.text_location = os.path.join(os.getcwd(), "results", "text_files")
        self.third_place_teams_dict = {}
        self.third_place_teams = []
        self.counter_letters = "ABCDEFGHIJKLMNOPRSTU"
        self.counter_files_generation = 0

    def create_group_scores(self):
        '''
        We will traverse through each group and make the scores
        We will need to keep track of the score and then somehow transfer it to excel
        :return:updated dict_general
        '''
        for i in range(0, len(constants.TEAMS)):
            string_text_file = ""
            '''
            ROUND 1
            '''
            outcome, score_team1, score_team2 = self.helper.computize_scores()
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
            # time.sleep(0.5)
            outcome, score_team1, score_team2 = self.helper.computize_scores()
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
            # time.sleep(0.5)
            '''
            ROUND 2
            '''
            outcome, score_team1, score_team2 = self.helper.computize_scores()
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
            # time.sleep(0.5)
            outcome, score_team1, score_team2 = self.helper.computize_scores()
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
            # time.sleep(0.5)
            '''
            ROUND 3
            '''
            outcome, score_team1, score_team2 = self.helper.computize_scores()
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
            # time.sleep(0.5)
            outcome, score_team1, score_team2 = self.helper.computize_scores()
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
            # time.sleep(0.5)
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
            table_result, teams_ranking = self.create_result_table(constants.TEAMS[i][0], constants.TEAMS[i][1],
                                                                   constants.TEAMS[i][2], constants.TEAMS[i][3])

            # add in the special dictionary all place 3 teams
            dict_place_3 = self.dictionary_teams_general[teams_ranking[2]]
            self.third_place_teams_dict.update({teams_ranking[2]: dict_place_3})

            file_name = self.counter_letters[self.counter_files_generation] + constants.GROUPS[i]
            '''START COMPUTING INTO FILE'''
            with open(file=os.path.join(self.text_location,file_name), mode="w",
                      encoding="utf-8") as result_group:
                result_group.write(string_text_file)
                result_group.write(table_result)
            self.list_qualified_teams.append(teams_ranking[0])
            self.list_qualified_teams.append(teams_ranking[1])
            self.counter_files_generation += 1
        # we will just need the qualified teams
        self.third_place_teams = self.arrange_dict_third_place_teams()
        third_place_teams_group = self.arrange_dict_third_place_teams()
        return third_place_teams_group

    def delete_points(self):
        # remove from dict the points part
        for i in range(0, len(constants.TEAMS)):
            for j in range(0, len(constants.TEAMS[i])):
                del self.dictionary_teams_general[constants.TEAMS[i][j]][constants.ATTRIBUTES[0]]

    def compute_matches_second_stage(self):
        '''
        will compute the qualified teams from the groups and choose based on what group and rank it has if a rank 1 team plays with a rank 3 team or rank 2 team - for world cup source
        :return:LIST OF QUALIFIED TEAMS TO THE LAST 32 AND UPDATE DICT GENERAL
        '''
        computed_last_32_string_results = ""
        winners = []
        dict_team_rank = self.helper.create_team_rank_place(self.list_qualified_teams)
        # make a copy because we update the list qualified teams
        dict_team_rank_opy = dict_team_rank.copy()
        match_string1, winner1 = self.compute_second_stage_match_first_vs_third("1E", dict_team_rank_opy, 0)
        computed_last_32_string_results += match_string1
        winners.append(winner1)
        match_string2, winner2 = self.compute_second_stage_match_first_vs_third("1I", dict_team_rank_opy, 1)
        computed_last_32_string_results += match_string2
        winners.append(winner2)
        match_string9, winner9 = self.compute_second_stage_match_first_vs_second("2A", "2B", dict_team_rank_opy, 2)
        computed_last_32_string_results += match_string9
        winners.append(winner9)
        match_string10, winner10 = self.compute_second_stage_match_first_vs_second("1F", "2C", dict_team_rank_opy, 3)
        computed_last_32_string_results += match_string10
        winners.append(winner10)
        match_string11, winner11 = self.compute_second_stage_match_first_vs_second("2K", "2L", dict_team_rank_opy, 4)
        computed_last_32_string_results += match_string11
        winners.append(winner11)
        match_string12, winner12 = self.compute_second_stage_match_first_vs_second("1H", "2J", dict_team_rank_opy, 5)
        computed_last_32_string_results += match_string12
        winners.append(winner12)
        match_string3, winner3 = self.compute_second_stage_match_first_vs_third("1D", dict_team_rank_opy, 6)
        computed_last_32_string_results += match_string3
        winners.append(winner3)
        match_string4, winner4 = self.compute_second_stage_match_first_vs_third("1G", dict_team_rank_opy, 7)
        computed_last_32_string_results += match_string4
        winners.append(winner4)
        match_string13, winner13 = self.compute_second_stage_match_first_vs_second("1C", "2F", dict_team_rank_opy, 8)
        computed_last_32_string_results += match_string13
        winners.append(winner13)
        match_string14, winner14 = self.compute_second_stage_match_first_vs_second("2E", "2I", dict_team_rank_opy, 9)
        computed_last_32_string_results += match_string14
        winners.append(winner14)
        match_string5, winner5 = self.compute_second_stage_match_first_vs_third("1A", dict_team_rank_opy, 10)
        computed_last_32_string_results += match_string5
        winners.append(winner5)
        match_string6, winner6 = self.compute_second_stage_match_first_vs_third("1L", dict_team_rank_opy, 11)
        computed_last_32_string_results += match_string6
        winners.append(winner6)
        match_string15, winner15 = self.compute_second_stage_match_first_vs_second("1J", "2H", dict_team_rank_opy, 12)
        computed_last_32_string_results += match_string15
        winners.append(winner15)
        match_string16, winner16 = self.compute_second_stage_match_first_vs_second("2D", "2G", dict_team_rank_opy, 13)
        computed_last_32_string_results += match_string16
        winners.append(winner16)
        match_string7, winner7 = self.compute_second_stage_match_first_vs_third("1B", dict_team_rank_opy, 14)
        computed_last_32_string_results += match_string7
        winners.append(winner7)
        match_string8, winner8 = self.compute_second_stage_match_first_vs_third("1K", dict_team_rank_opy, 15)
        computed_last_32_string_results += match_string8
        winners.append(winner8)

        # add the delimiter to delimit for excel
        computed_last_32_string_results += constants.SPECIAL_CHARS_DELIMITERS

        # make initial check to see if self.list_qualified contains all values of winner
        check = self.helper.check_lists(self.list_qualified_teams, winners)
        if not check:
            raise Exception("Elements are not the same!!!")
        else:
            # clear list and make the self.qualified list = winners to keep correct tracking
            self.list_qualified_teams.clear()
            self.list_qualified_teams = winners
        string_winners = self.helper.compute_string_winners(self.list_qualified_teams)
        '''
        ADD TO FILE
        '''
        file_name = self.counter_letters[self.counter_files_generation] + constants.KNOCKOUTS[0]
        self.counter_files_generation +=1
        with open(file=os.path.join(self.text_location,file_name), mode="w", encoding="utf-8") as f:
            f.write(computed_last_32_string_results)
            f.write(string_winners)

    def compute_final_stage_matches(self):
        '''
        LAST16
        '''
        last_16_matches, _ = self.compute_knockout_matches(constants.KNOCKOUTS[1], self.list_qualified_teams)
        last_16_matches += constants.SPECIAL_CHARS_DELIMITERS
        string_winners = self.helper.compute_string_winners(self.list_qualified_teams)
        # ADD TO FILE
        file_name =  self.counter_letters[self.counter_files_generation] + constants.KNOCKOUTS[1]
        self.counter_files_generation += 1
        with open(file=os.path.join(self.text_location,file_name), mode="w", encoding="utf-8") as f:
            f.write(last_16_matches)
            f.write(string_winners)
        '''
        QUARTERFINALS
        '''
        quarterfinal_matches, _ = self.compute_knockout_matches(constants.KNOCKOUTS[2], self.list_qualified_teams)
        quarterfinal_matches += constants.SPECIAL_CHARS_DELIMITERS
        string_winners = self.helper.compute_string_winners(self.list_qualified_teams)
        # ADD TO FILE
        file_name =  self.counter_letters[self.counter_files_generation] + constants.KNOCKOUTS[2]
        self.counter_files_generation += 1
        with open(file=os.path.join(self.text_location,file_name), mode="w", encoding="utf-8") as f:
            f.write(quarterfinal_matches)
            f.write(string_winners)
        '''
        SEMIFINALS
        '''
        semifinal_matches, list_unq = self.compute_knockout_matches(constants.KNOCKOUTS[3], self.list_qualified_teams)
        semifinal_matches += constants.SPECIAL_CHARS_DELIMITERS
        string_winners = self.helper.compute_string_winners(self.list_qualified_teams)
        string_losers = self.helper.compute_string_winners(list_unq)
        # ADD TO FILE
        file_name =  self.counter_letters[self.counter_files_generation] + constants.KNOCKOUTS[3]
        self.counter_files_generation += 1
        with open(file=os.path.join(self.text_location, file_name), mode="w", encoding="utf-8") as f:
            f.write(semifinal_matches)
            f.write(string_winners)
            f.write("\n" + constants.SPECIAL_CHARS_DELIMITERS)
            f.write(string_losers)

        '''
        SMALL FINAL
        '''
        small_final_match, _ = self.compute_knockout_matches(constants.KNOCKOUTS[4], list_unq)
        small_final_match += constants.SPECIAL_CHARS_DELIMITERS
        string_winner = self.helper.compute_string_winners(list_unq)
        # ADD TO FILE
        file_name =  self.counter_letters[self.counter_files_generation] + constants.KNOCKOUTS[4]
        self.counter_files_generation += 1
        with open(file=os.path.join(self.text_location, file_name), mode="w", encoding="utf-8") as f:
            f.write(small_final_match)
            f.write(string_winner)

        '''
        BIG FINAL
        '''
        big_final_match, _ = self.compute_knockout_matches(constants.KNOCKOUTS[5], self.list_qualified_teams)
        big_final_match += constants.SPECIAL_CHARS_DELIMITERS
        string_winner = self.helper.compute_string_winners(self.list_qualified_teams)
        #world cup winner
        print("WORLD CUP 2026 WINNER IS ..." +string_winner)
        # ADD TO FILE
        file_name =  self.counter_letters[self.counter_files_generation] + constants.KNOCKOUTS[5]
        self.counter_files_generation += 1
        with open(file=os.path.join(self.text_location, file_name), mode="w", encoding="utf-8") as f:
            f.write(big_final_match)
            f.write(string_winner)


    def compute_second_stage_match_first_vs_third(self, dictionary_index_value, dict_team_rank, index_addition):
        match_string = ""
        winner = ""
        outcome, score_team1, score_team2 = self.helper.computize_scores()
        random_generated_team_third = self.third_place_teams[
            self.helper.choose_random_third_place_team(self.third_place_teams)]
        if outcome == 1:
            self.third_place_teams.remove(random_generated_team_third)
            match_string = dict_team_rank[dictionary_index_value] + "-" + random_generated_team_third + "*" + str(
                score_team1) + "-" + str(score_team2) + "*" + "\n"
            winner = dict_team_rank[dictionary_index_value]
        elif outcome == 2:
            self.list_qualified_teams.remove(dict_team_rank[dictionary_index_value])
            self.third_place_teams.remove(random_generated_team_third)
            # add the new team
            self.list_qualified_teams.insert(index_addition, random_generated_team_third)
            match_string = dict_team_rank[dictionary_index_value] + "-" + random_generated_team_third + "*" + str(
                score_team1) + "-" + str(score_team2) + "*" + "\n"
            winner = random_generated_team_third
        else:
            # special case where we have penalties
            penalty1 = 0
            penalty2 = 0
            while penalty1 == penalty2:
                penalty1 = random.randint(0, 7)
                penalty2 = random.randint(0, 7)

            if penalty1 > 3 and penalty2 == 0:
                penalty1 = 3
            elif penalty2 > 3 and penalty1 == 0:
                penalty2 = 3
            elif penalty1 == 1 and penalty2 > 4:
                penalty2 = 4
            elif penalty1 > 4 and penalty2 == 1:
                penalty1 = 4
            elif penalty1 > 5 and penalty2 == 2:
                penalty1 = 5
            elif penalty2 > 5 and penalty2 == 2:
                penalty2 = 5

            final_score_team1 = score_team1 + penalty1
            final_score_team2 = score_team2 + penalty2
            # check winner
            if final_score_team1 > final_score_team2:
                match_string = dict_team_rank[dictionary_index_value] + "-" + random_generated_team_third + "*" + str(
                    score_team1) + "-" + str(score_team2) + "*" + dict_team_rank[
                                   dictionary_index_value] + " won on penalties " + str(
                    final_score_team1) + "-" + str(final_score_team2) + "\n"
                self.third_place_teams.remove(random_generated_team_third)
                winner = dict_team_rank[dictionary_index_value]
            elif final_score_team1 < final_score_team2:
                match_string = dict_team_rank[dictionary_index_value] + "-" + random_generated_team_third + "*" + str(
                    score_team1) + "-" + str(
                    score_team2) + "*" + random_generated_team_third + " won on penalties " + str(
                    final_score_team1) + "-" + str(final_score_team2) + "\n"
                self.list_qualified_teams.remove(dict_team_rank[dictionary_index_value])
                self.third_place_teams.remove(random_generated_team_third)
                self.list_qualified_teams.insert(index_addition, random_generated_team_third)
                winner = random_generated_team_third
        self.dictionary_teams_general[dict_team_rank[dictionary_index_value]][constants.ATTRIBUTES[1]] += score_team1
        self.dictionary_teams_general[dict_team_rank[dictionary_index_value]][constants.ATTRIBUTES[2]] += score_team2
        self.dictionary_teams_general[dict_team_rank[dictionary_index_value]][
            constants.ATTRIBUTES[3]] = self.dictionary_teams_general[dict_team_rank[dictionary_index_value]][
                                           constants.ATTRIBUTES[1]] - \
                                       self.dictionary_teams_general[dict_team_rank[dictionary_index_value]][
                                           constants.ATTRIBUTES[2]]

        self.dictionary_teams_general[random_generated_team_third][constants.ATTRIBUTES[1]] += score_team2
        self.dictionary_teams_general[random_generated_team_third][constants.ATTRIBUTES[2]] += score_team1
        self.dictionary_teams_general[random_generated_team_third][constants.ATTRIBUTES[3]] = \
            self.dictionary_teams_general[random_generated_team_third][constants.ATTRIBUTES[1]] - \
            self.dictionary_teams_general[random_generated_team_third][constants.ATTRIBUTES[2]]

        return match_string, winner

    def compute_second_stage_match_first_vs_second(self, dictionary_index_value1, dictionary_index_value2,
                                                   dict_team_rank, index_addition):
        '''
        Basically we know the index values that we need to play
        Here it will automatically delete from the self.qualified_teams
        Need to appeal the helper function to exchange index values to keep track of correct matches
        :param dictionary_index_value1:
        :param dictionary_index_value2:
        :param dict_team_rank:
        :param index_addition: the index where to put the element
        :return: string with result of match to put in text_files
        '''
        match_string = ""
        winner = ""
        outcome, score_team1, score_team2 = self.helper.computize_scores()
        if outcome == 1:
            match_string = dict_team_rank[dictionary_index_value1] + "-" + dict_team_rank[
                dictionary_index_value2] + "*" + str(
                score_team1) + "-" + str(score_team2) + "*" + "\n"
            self.list_qualified_teams.remove(dict_team_rank[dictionary_index_value2])
            self.helper.move_list_elements(self.list_qualified_teams, index_addition,
                                           self.list_qualified_teams.index(dict_team_rank[dictionary_index_value1]))
            winner = dict_team_rank[dictionary_index_value1]
        elif outcome == 2:
            match_string = dict_team_rank[dictionary_index_value1] + "-" + dict_team_rank[
                dictionary_index_value2] + "*" + str(
                score_team1) + "-" + str(score_team2) + "*" + "\n"
            self.list_qualified_teams.remove(dict_team_rank[dictionary_index_value1])
            self.helper.move_list_elements(self.list_qualified_teams, index_addition,
                                           self.list_qualified_teams.index(dict_team_rank[dictionary_index_value2]))
            winner = dict_team_rank[dictionary_index_value2]
        else:
            # special case where we have penalties
            penalty1 = 0
            penalty2 = 0
            while penalty1 == penalty2:
                penalty1 = random.randint(0, 7)
                penalty2 = random.randint(0, 7)

            if penalty1 > 3 and penalty2 == 0:
                penalty1 = 3
            elif penalty2 > 3 and penalty1 == 0:
                penalty2 = 3
            elif penalty1 == 1 and penalty2 > 4:
                penalty2 = 4
            elif penalty1 > 4 and penalty2 == 1:
                penalty1 = 4
            elif penalty1 > 5 and penalty2 == 2:
                penalty1 = 5
            elif penalty2 > 5 and penalty2 == 2:
                penalty2 = 5

            final_score_team1 = score_team1 + penalty1
            final_score_team2 = score_team2 + penalty2
            # check winner
            if final_score_team1 > final_score_team2:
                match_string = dict_team_rank[dictionary_index_value1] + "-" + dict_team_rank[
                    dictionary_index_value2] + "*" + str(
                    score_team1) + "-" + str(score_team2) + "*" + dict_team_rank[
                                   dictionary_index_value1] + " won on penalties " + str(
                    final_score_team1) + "-" + str(final_score_team2) + "\n"
                self.list_qualified_teams.remove(dict_team_rank[dictionary_index_value2])
                self.helper.move_list_elements(self.list_qualified_teams, index_addition,
                                               self.list_qualified_teams.index(dict_team_rank[dictionary_index_value1]))
                winner = dict_team_rank[dictionary_index_value1]
            elif final_score_team1 < final_score_team2:
                match_string = dict_team_rank[dictionary_index_value1] + "-" + dict_team_rank[
                    dictionary_index_value2] + "*" + str(
                    score_team1) + "-" + str(
                    score_team2) + "*" + dict_team_rank[dictionary_index_value2] + " won on penalties " + str(
                    final_score_team1) + "-" + str(final_score_team2) + "\n"
                self.list_qualified_teams.remove(dict_team_rank[dictionary_index_value1])
                self.helper.move_list_elements(self.list_qualified_teams, index_addition,
                                               self.list_qualified_teams.index(dict_team_rank[dictionary_index_value2]))
                winner = dict_team_rank[dictionary_index_value2]
        # update dictionary
        self.dictionary_teams_general[dict_team_rank[dictionary_index_value1]][constants.ATTRIBUTES[1]] += score_team1
        self.dictionary_teams_general[dict_team_rank[dictionary_index_value1]][constants.ATTRIBUTES[2]] += score_team2
        self.dictionary_teams_general[dict_team_rank[dictionary_index_value1]][
            constants.ATTRIBUTES[3]] = self.dictionary_teams_general[dict_team_rank[dictionary_index_value1]][
                                           constants.ATTRIBUTES[1]] - \
                                       self.dictionary_teams_general[dict_team_rank[dictionary_index_value1]][
                                           constants.ATTRIBUTES[2]]
        self.dictionary_teams_general[dict_team_rank[dictionary_index_value2]][constants.ATTRIBUTES[1]] += score_team2
        self.dictionary_teams_general[dict_team_rank[dictionary_index_value2]][constants.ATTRIBUTES[2]] += score_team1
        self.dictionary_teams_general[dict_team_rank[dictionary_index_value2]][
            constants.ATTRIBUTES[3]] = self.dictionary_teams_general[dict_team_rank[dictionary_index_value2]][
                                           constants.ATTRIBUTES[1]] - \
                                       self.dictionary_teams_general[dict_team_rank[dictionary_index_value2]][
                                           constants.ATTRIBUTES[2]]
        return match_string, winner

    def compute_knockout_matches(self, stage_name, list_teams):
        '''
        :param stage_name: it will be the knockout stage
        :param list_teams: either the qualified teams and in the small final wil be the unqualified teams
        :return: the file for knockout stage
        '''
        string_matches = ""
        list_unqualified_teams = []
        for i in range(0, len(list_teams), 2):
            match_string = ""
            outcome, score_team1, score_team2 = self.helper.computize_scores()
            if outcome == 1:
                match_string += list_teams[i] + "-" + list_teams[i + 1] + "*" + str(
                    score_team1) + "-" + str(score_team2) + "*" + "\n"
                list_unqualified_teams.append(list_teams[i + 1])
            elif outcome == 2:
                match_string += list_teams[i] + "-" + list_teams[i + 1] + "*" + str(
                    score_team1) + "-" + str(score_team2) + "*" + "\n"
                list_unqualified_teams.append(list_teams[i])
            else:
                # special case where we have penalties
                penalty1 = 0
                penalty2 = 0
                while penalty1 == penalty2:
                    penalty1 = random.randint(0, 7)
                    penalty2 = random.randint(0, 7)

                if penalty1 > 3 and penalty2 == 0:
                    penalty1 = 3
                elif penalty2 > 3 and penalty1 == 0:
                    penalty2 = 3
                elif penalty1 == 1 and penalty2 > 4:
                    penalty2 = 4
                elif penalty1 > 4 and penalty2 == 1:
                    penalty1 = 4
                elif penalty1 > 5 and penalty2 == 2:
                    penalty1 = 5
                elif penalty2 > 5 and penalty2 == 2:
                    penalty2 = 5

                final_score_team1 = score_team1 + penalty1
                final_score_team2 = score_team2 + penalty2

                # check winner
                if final_score_team1 > final_score_team2:
                    match_string += list_teams[i] + "-" + list_teams[i + 1] + "*" + str(
                        score_team1) + "-" + str(score_team2) + "*" + list_teams[i] + " won on penalties " + str(
                        final_score_team1) + "-" + str(final_score_team2) + "\n"
                    list_unqualified_teams.append(list_teams[i + 1])
                elif final_score_team1 < final_score_team2:
                    match_string += list_teams[i] + "-" + list_teams[i + 1] + "*" + str(
                        score_team1) + "-" + str(score_team2) + "*" + list_teams[
                                        i + 1] + " won on penalties " + str(
                        final_score_team1) + "-" + str(final_score_team2) + "\n"
                    list_unqualified_teams.append(list_teams[i])
            self.dictionary_teams_general[list_teams[i]][
                constants.ATTRIBUTES[1]] += score_team1
            self.dictionary_teams_general[list_teams[i]][
                constants.ATTRIBUTES[2]] += score_team2
            self.dictionary_teams_general[list_teams[i]][
                constants.ATTRIBUTES[3]] = self.dictionary_teams_general[list_teams[i]][
                                               constants.ATTRIBUTES[1]] - self.dictionary_teams_general[list_teams[i]][
                                               constants.ATTRIBUTES[2]]

            self.dictionary_teams_general[list_teams[i + 1]][
                constants.ATTRIBUTES[1]] += score_team2
            self.dictionary_teams_general[list_teams[i + 1]][
                constants.ATTRIBUTES[2]] += score_team1
            self.dictionary_teams_general[list_teams[i + 1]][
                constants.ATTRIBUTES[3]] = self.dictionary_teams_general[list_teams[i + 1]][
                                               constants.ATTRIBUTES[1]] - \
                                           self.dictionary_teams_general[list_teams[i + 1]][
                                               constants.ATTRIBUTES[2]]

            string_matches += match_string
        # update the qualified list
        self.helper.remove_unqualified_elements(list_teams, list_unqualified_teams)
        if stage_name == constants.KNOCKOUTS[3]:  # SEMIFINALS
            return string_matches, list_unqualified_teams
        return string_matches, None

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
            if idx == len(list_items):  # 4+1
                string_line = str(counter) + "." + str(list_items[idx][0]) + "." + str(list_items[idx][1]) + "." + str(
                    list_items[idx][2]) + "." + \
                              str(list_items[idx][3]) + "." + str(list_items[idx][4])
                string_sorted += string_line
            else:
                string_line = str(counter) + "." + str(list_items[idx][0]) + "." + str(list_items[idx][1]) + "." + str(
                    list_items[idx][2]) + "." + \
                              str(list_items[idx][3]) + "." + str(list_items[idx][4]) + "\n"
                string_sorted += string_line
            counter += 1
        return string_sorted, sorted_dict

    def arrange_dict_third_place_teams(self):
        teams = list(self.third_place_teams_dict.keys())
        sorted_dict = sorted(teams, key=lambda team: (self.dictionary_teams_general[team][constants.ATTRIBUTES[0]],
                                                      self.dictionary_teams_general[team][constants.ATTRIBUTES[3]],
                                                      self.dictionary_teams_general[team][constants.ATTRIBUTES[1]]),
                             reverse=True)
        return sorted_dict[:8]

    def populate_player_goals(self):
        goals_players = []
        for i in range (0, len(constants.TEAMS)):
            for j in range (0, len(constants.TEAMS[i])):
                list_temp = []
                player = constants.PLAYERS[i][j]
                team = constants.TEAMS[i][j]
                goals_scored_team = self.dictionary_teams_general[team][constants.ATTRIBUTES[1]]
                goals_scored_player = self.helper.generate_player_goals(goals_scored_team, 2)
                list_temp.append(player)
                list_temp.append(team)
                list_temp.append(goals_scored_player)
                goals_players.append(list_temp)
        #sort the list based on goal numbers
        goals_players.sort(key=lambda x: x[2], reverse=True)
        '''
        ADD TO FILE
        '''
        string_goals = ""
        for j in range (0, len(goals_players)):
            string_temp =""
            for i in range (0, len(goals_players[0])):
                if i == len(goals_players[0]) - 1:
                    string_temp += str(goals_players[j][i])
                else:
                    string_temp += str(goals_players[j][i]) +"*"
            string_goals += string_temp +"\n"
        filename = self.counter_letters[self.counter_files_generation] + constants.RANKING_FILES[1]
        with open(file = os.path.join(self.text_location, filename), mode="w", encoding="utf-8") as text_file:
            text_file.write(string_goals)


    def create_file_final_rankings(self):
        #sort in alphabetical order
        sorted_dict =  {k: v for k, v in
                             sorted(self.dictionary_teams_general.items(), key=lambda item: item[0])}
        string_sorted_final_rankings = ""
        for team in sorted_dict:
            string_team_info = team+"*"+str(sorted_dict[team][constants.ATTRIBUTES[1]])+"*"+str(sorted_dict[team][constants.ATTRIBUTES[2]])+"*"+str(sorted_dict[team][constants.ATTRIBUTES[3]])+"\n"
            string_sorted_final_rankings += string_team_info
        '''
        WRITE TO FILE
        '''
        filename = self.counter_letters[self.counter_files_generation]+constants.RANKING_FILES[0]
        self.counter_files_generation +=1
        with open (file = os.path.join(self.text_location, filename), mode='w', encoding="utf-8") as file:
            file.write(string_sorted_final_rankings)










