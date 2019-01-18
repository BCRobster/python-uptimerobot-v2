# python3 modul for uptimerobot API v2
import requests
import json
import sys
import os

# tasks to do:
    # - add typing to all variabels
    # - add more usefull variabels in the newMonitor Function
    # - in getMonitorIdByFriendlyName deriving responce ok?
    # - in getMonitorIdByFriendlyName deriving responce ok?


class UptimeRobot:

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.baseUrl = "https://api.uptimerobot.com/v2/"


    def requestApi(self, url, payload, headers):
        response = requests.request("POST", url, data=payload , headers=headers)
        jResponce = json.loads(response.content)
        if jResponce.get('stat'):
            stat = jResponce.get('stat')
            if stat == 'ok':
                return True, jResponce
        return False, jResponce


    def getMonitors(self):
        
        url = self.baseUrl
        url += 'getMonitors'
        
        payload  = 'api_key=' 
        payload += self.apiKey
        payload += '&format=json&logs=1'

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
            }
        return self.requestApi(url, payload, headers)
    

    def getMonitorIdByFriendlyName(self, monitorFriendlyName: str):
        responce = UptimeRobot.getMonitors(self) #make that better self.getMonitors(self)
        if responce[0] == True:
            monitors = responce[1].get('monitors')
            for monitor in monitors:
                if monitorFriendlyName == monitor['friendly_name']:
                    return monitor['id']
        return None


    def getMonitorById(self, monitorId: int):
        responce = UptimeRobot.getMonitors(self) #make that better self.getMonitors(self)
        if responce[0] == True:
            monitors = responce[1].get('monitors')
            for monitor in monitors:
                if monitorId == monitor['id']:
                    return monitor
        return None


    def deleteMonitorById(self, monitorId):
        url = self.baseUrl
        url += 'deleteMonitor'
        
        payload  = 'api_key=' 
        payload += self.apiKey
        payload += '&format=json&id='
        payload += monitorId

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
            }
        return self.requestApi(url, payload, headers)         

    
    #def deleteMonitorByFriendlyName(self, FriendlyName):
    #   get monitorId by friendly name
    #   delet monitor by id



    def newMonitor(self, monitorType: int, monitorUrl: str, monitorFriendlyName):
        #add more usefull parameters: {
            # interval
            # http_username
            # http_password
            # alert_contacts
            # mwindows
            # handling correctness of values / python3 typing 
                # -friendly name
                # -monitor url
                # -type
        # }
        url = self.baseUrl
        url += 'newMonitor'
        
        payload  = 'api_key=' 
        payload += self.apiKey
        payload += '&format=json&type='
        payload += monitorType # monitorType values defines the UptimeRobot API v2 
            # 1 - HTTP(s)
            # 2 - Keyword 
            # 3 - Ping
            # 4 - Port
        payload += '&url=http%3A%2F%2F'
        payload += monitorUrl # url: my-url.domain
        payload += '&friendly_name='
        payload += monitorFriendlyName

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
            }
        return self.requestApi(url, payload, headers)

