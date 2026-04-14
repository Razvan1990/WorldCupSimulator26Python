from initialization import constants
from initialization.helper_functions import HelperFunctions
from logic.logic import LogicCreator


class Main(object):

    def __init__(self):
        self.helper = HelperFunctions()
        self.logic = LogicCreator()

    def run_project(self):
        self.logic.create_group_scores()
        self.logic.create_result_table(constants.TEAMS[0][0], constants.TEAMS[0][1], constants.TEAMS[0][2], constants.TEAMS[0][3])



if __name__ == '__main__':
    main = Main()
    main.run_project()