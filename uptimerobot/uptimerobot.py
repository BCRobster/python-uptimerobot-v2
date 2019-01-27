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
        (success, values) = self.getMonitors()
        if success:
            for monitor in values.get('monitors'):
                if monitorFriendlyName == monitor['friendly_name']:
                    return monitor['id']
        return values, monitorFriendlyName
        

    def getMonitorById(self, monitorId: int):
        (success, values) = self.getMonitors()
        if success:
            for monitor in values.get('monitors'):
                if monitorId == monitor['id']:
                    return monitor
        return values, monitorId


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
        jResponse = json.loads(response.content)
        if jResponse.get('stat') == 'ok':
            return True, jResponse
        return False, jResponse
    

    def __newHeaders(self):
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'cache-control': 'no-cache'
            }
        return(headers)

