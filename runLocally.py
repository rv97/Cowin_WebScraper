from cowin_parser import CowinParser
from utils import Cowinutils

#Currently not working
def runLoacally():
        cowin_utils = Cowinutils()
        cowinParser = CowinParser(cowin_utils)
        cowin_utils.setQueryDetails({})
        cowin_utils.getListOfStatesAndDistrict()
        cowin_utils.getStatesFromUser()
        cowin_utils.getDistrictFromUser()
        cowinParser.setStateAndDistrictInWeb()

runLoacally()