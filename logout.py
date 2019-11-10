import requests
import re
import sys
import hashlib
def octalString2Int(string):
    power = 0
    salt_val = 0
    for i in range(len(string) -1,-1, -1):
        salt_val += int(string[i])*(8**power)
        power+=1
    return salt_val
if __name__ == "__main__":
    response = requests.get("http://10.5.50.1/logout")
    print(response)
