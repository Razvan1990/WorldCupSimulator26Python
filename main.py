from initialization import constants
from initialization.helper_functions import HelperFunctions
from logic.logic import LogicCreator
from excel.report_parser import TxtParser


class Main(object):

    def __init__(self):
        self.helper = HelperFunctions()
        self.logic = LogicCreator()
        self.parser = TxtParser()

    def run_project(self):
        self.logic.create_group_scores()
        self.logic.delete_points()
        self.logic.compute_matches_second_stage()
        #self.parser.parse_results_stages(constants.GROUPS[0])
        #self.parser.parse_results_knockouts(constants.KNOCKOUTS[0])
        self.logic.compute_final_stage_matches()



if __name__ == '__main__':
    main = Main()
    main.run_project()