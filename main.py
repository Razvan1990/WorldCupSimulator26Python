import time

from logic.logic import LogicCreator
from excel.excel_reader import ExcelReader


class Main(object):

    def __init__(self):
        self.logic = LogicCreator()
        self.excel_reader = ExcelReader()

    def run_project(self):
        print("Group stage matches simulating.......")
        time.sleep(5)
        third_place_team_groups = self.logic.create_group_scores()
        self.logic.delete_points()
        print("Last 32 matches simulating......")
        time.sleep(3)
        self.logic.compute_matches_second_stage()
        print("Simulating final stage matches...")
        print("Last 16...")
        time.sleep(1.5)
        print("Quarterfinals....")
        time.sleep(1.5)
        print("Semifinals....")
        time.sleep(1)
        print("Small final....")
        time.sleep(1)
        print("Big final....")
        time.sleep(2)
        self.logic.compute_final_stage_matches()
        print("Computing final stats....")
        time.sleep(2)
        self.logic.create_file_final_rankings()
        self.logic.populate_player_goals()
        # #add to excel
        self.excel_reader.create_excel_stage_sheets(third_place_team_groups)
        self.excel_reader.create_excel_knockout_stages()
        self.excel_reader.create_sheet_final_rankings_sheet()
        self.excel_reader.create_sheet_strikers_list()
        self.excel_reader.delete_empty_sheet()
        print("FOR DETAILS PLEASE CHECK THE SIMULATION RESULTS FROM {}".format(self.excel_reader.excel_file))



if __name__ == '__main__':
    main = Main()
    main.run_project()