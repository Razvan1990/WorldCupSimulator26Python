from initialization import constants
from initialization.helper_functions import HelperFunctions
from logic.logic import LogicCreator
from excel.report_parser import TxtParser
from excel.excel_reader import ExcelReader


class Main(object):

    def __init__(self):
        self.helper = HelperFunctions()
        self.logic = LogicCreator()
        self.parser = TxtParser()
        self.excel_reader = ExcelReader()

    def run_project(self):
        third_place_team_groups = self.logic.create_group_scores()
        self.logic.delete_points()
        self.logic.compute_matches_second_stage()
        #self.parser.parse_results_stages(constants.GROUPS[0])
        #self.parser.parse_results_knockouts(constants.KNOCKOUTS[0])
        self.logic.compute_final_stage_matches()
        self.logic.create_file_final_rankings()
        self.logic.populate_player_goals()
        #self.excel_reader.create_excel_stage_sheets(third_place_team_groups)
        #self.excel_reader.create_excel_knockout_stages()
        self.excel_reader.create_sheet_final_rankings_sheet()
        self.excel_reader.create_sheet_strikers_list()



if __name__ == '__main__':
    main = Main()
    main.run_project()