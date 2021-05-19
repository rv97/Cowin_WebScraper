import requests

class Cowinutils:

    def setQueryDetails(self, queryDetails):
        self.queryDetails = queryDetails
    
    def getQueryDettails(self):
        return self.queryDetails

    def getListOfStatesAndDistrict(self):
        REQUEST_URL = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        self.headers={
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        result = requests.get(REQUEST_URL, headers=self.headers)
        self.STATES_JSON = result.json()
        REQUEST_URL = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+str(self.queryDetails['state_id'])
        result = requests.get(REQUEST_URL, headers=self.headers)
        self.DISTRICTS = result.json()

    def getStatesFromUser(self):
        print("Select the State Number: ")
        for state in self.STATES_JSON['states']:
            print(str(state['state_id'])+" "+state['state_name'])
        state_id = input()
        self.queryDetails['state_id'] = int(state_id)

    def getDistrictFromUser(self):
        for district in self.DISTRICTS['districts']:
            print(str(district['district_id'])+" "+district['district_name'])
        district_id = input()
        self.queryDetails['district_id'] = int(district_id)
    
    def getStateAndDistrictName(self):
        state_id = self.queryDetails['state_id']
        district_id = self.queryDetails['district_id']
        stateName = self.STATES_JSON['states'][state_id]['state_name']
        for district in self.DISTRICTS['districts']:
            if district['district_id'] == district_id:
                districtName = district['district_name']
        return stateName, districtName
    
    def getStates(self):
        REQUEST_URL = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
        self.headers={
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
        result = requests.get(REQUEST_URL, headers=self.headers)
        self.STATES_JSON = result.json()

    def getDistrict(self, state_id):
        REQUEST_URL = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/"+str(state_id)
        result = requests.get(REQUEST_URL, headers=self.headers)
        self.DISTRICTS = result.json()