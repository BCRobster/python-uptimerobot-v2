# python3 modul for uptimerobot API v2

import json
import os
import requests
import sys



class UptimeRobot:
    def __init__(self, apiKey: str):
        self.apiKey = apiKey
        self._baseUrl = "https://api.uptimerobot.com/v2/"


    def getMonitors(self):
        url = '%sgetMonitors' % (self._baseUrl)
        payload  = 'api_key=%s&format=json&logs=1' % (self.apiKey)
        headers = self.__newHeaders()
        return self.__requestApi(url, payload, headers)
    

    def getMonitorIdByFriendlyName(self, monitorFriendlyName: str):
        response = self.getMonitors()
        if response[0] == True:
            monitors = response[1].get('monitors')
            for monitor in monitors:
                if monitorFriendlyName == monitor['friendly_name']:
                    return monitor['id']
        return None


    def getMonitorById(self, monitorId: int):
        response = self.getMonitors()
        if response[0] == True:
            monitors = response[1].get('monitors')
            for monitor in monitors:
                if monitorId == monitor['id']:
                    return monitor
        return None


    def deleteMonitorById(self, monitorId):
        url = '%sdeleteMonitor' % (self._baseUrl)
        payload  = 'api_key=%s&format=json&id=%s' % (self.apiKey, monitorId)
        headers = self.__newHeaders()
        return self.__requestApi(url, payload, headers)         

    
    def deleteMonitorByFriendlyName(self, friendlyName:str):
        monitorId = self.getMonitorIdByFriendlyName(friendlyName)
        self.deleteMonitorById(monitorId)


    def newMonitor(self, monitorType: int, monitorUrl: str, monitorFriendlyName):
        url = '%snewMonitor' % (self._baseUrl)
        payload  = 'api_key=%s&format=json&type=%s&url=%s&friendly_name=%s' % (self.apiKey, monitorType, monitorUrl, monitorFriendlyName) 
        headers = self.__newHeaders()

        return self.__requestApi(url, payload, headers)
       

    # ==================
    # = privat methods =
    # ==================
    
    def __requestApi(self, url, payload, headers):
        response = requests.request("POST", url, data=payload , headers=headers)
        jResponce = json.loads(response.content)
        if jResponce.get('stat'):
            stat = jResponce.get('stat')
            if stat == 'ok':
                return True, jResponce
        return False, jResponce


    def __newHeaders(self):
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'cache-control': 'no-cache'
            }
        return(headers)

