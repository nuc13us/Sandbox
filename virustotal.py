import requests

params = {'apikey': '8f40f27a3e64ec43e9f19e8f8b709b1691436329afb3d554fe52e5a9a8b52f38','resource': '6c2a33512b8b0ec906982783e82b9678' }
headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  My Python requests library example client or username"
  }
response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)
json_response = response.json()

print json_response['scans']

vendors_list = ['ALYac','AVG','AVware','Ad-Aware','AegisLab','Antiy-AVL','Arcabit','Avast','BitDefender','CAT-QuickHeal','CrowdStrike Falcon (ML)','Cyren','Emsisoft','F-Prot','F-Secure','Fortinet','GData','Ikarus','Invincea','Kaspersky','McAfee','McAfee-GW-Edition','eScan','NANO-Antivirus','Qihoo-360','Rising','Sophos','Symantec','Tencent','TheHacker','TrendMicro','VBA32','VIPRE','AhnLab-V3','Alibaba','Baidu','CMC','ClamAV','Comodo','DrWeb','ESET-NOD32','Jiangmin','K7AntiVirus','K7GW','Kingsoft','Malwarebytes','Microsoft','Panda','SUPERAntiSpyware','TotalDefense','Trustlook','ViRobot','WhiteArmor','Yandex']

"""
for i in vendors_list:
  print i + "-->"
  print json_response['scans'][i]

"""
