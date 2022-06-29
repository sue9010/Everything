import requests


# text = "http://admin:cg600ip100m@192.168.0.34/cgi-bin/httpapi/thermal.cgi?svc=tempAdvInfo&action=gets"
# response = requests.get(text)
# txt = response.text
# target = "max_temp_value="
# ntarget = "avr_temp_value"
# sn=txt.rfind(target)
# ln=txt.rfind(ntarget)
# print("MAX:" + txt[sn+15:ln])


text = "http://admin:cg600ip100m@192.168.0.34/cgi-bin/httpapi/thermal.cgi?svc=tempAdvInfo&action=gets&max_temp_value=-20.0-650.0"
response = requests.get(text)
txt = response.text
print(txt)