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
        
        url = self._baseUrl
        url += 'getMonitors'
        
        payload  = 'api_key=' 
        payload += self.apiKey
        payload += '&format=json&logs=1'

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
        url = self._baseUrl
        url += 'deleteMonitor'
        
        payload  = 'api_key=' 
        payload += self.apiKey
        payload += '&format=json&id='
        payload += monitorId

        headers = self.__newHeaders()

        return self.__requestApi(url, payload, headers)         

    
    #def deleteMonitorByFriendlyName(self, FriendlyName):
    #   get monitorId by friendly name
    #   delet monitor by id



    def newMonitor(self, monitorType: int, monitorUrl: str, monitorFriendlyName):
        url = self._baseUrl
        url += 'newMonitor'
        
        payload  = 'api_key=' 
        payload += self.apiKey
        payload += '&format=json&type='
        payload += monitorType # monitorType values defines the UptimeRobot API v2 
            # 1 - HTTP(s)
            # 2 - Keyword 
            # 3 - Ping
            # 4 - Port
        payload += '&url=http://'
        payload += monitorUrl # url: my-url.domain
        payload += '&friendly_name='
        payload += monitorFriendlyName

        headers = self.__newHeaders()

        return self.__requestApi(url, payload, headers)


    # privat methods

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

