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
        self.logic.compute_matches_second_stage()
        #self.parser.parse_results(constants.GROUPS[0])



if __name__ == '__main__':
    main = Main()
    main.run_project()