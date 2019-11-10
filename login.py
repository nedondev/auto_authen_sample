import requests
import re
import sys
import hashlib
import config

def octalString2Int(string):
    power = 0
    salt_val = 0
    for i in range(len(string) -1,-1, -1):
        salt_val += int(string[i])*(8**power)
        power+=1
    return salt_val
if __name__ == "__main__":
    total = len(sys.argv)
    username = ''
    password = ''
    check = 0
    for option, argument in zip(sys.argv[1::2],sys.argv[2::2]):
        if option == '-p':
            password = argument
            check += 1
        elif option == '-u':
            username = argument
            check += 1
    if check < 2:
        if config.USERNAME != None and config.PASSWORD != None:
            username = config.USERNAME
            password = config.PASSWORD
        else:
            print("Require: username and pasword")
            exit()
    response = requests.get("http://10.5.50.1/login")
    # print(type(response.content))
    # print(response.content)
    pass_encrypt_template  = re.search("hexMD5[\w\(\)\\\\ \'\"\+\.]*", str(response.content))
    # print(pass_encrypt_template.group().split('\\'))
    if pass_encrypt_template != None:
        prefix_salt = []
        suffix_salt = []
        mode = 0
        for element in pass_encrypt_template.group().split('\\'):
            if len(element) > 2:
                if re.search("MD5", element) != None:
                    pass
                elif re.search("password", element) != None:
                    mode = 1
                elif mode == 0:
                    salt = octalString2Int(element)
                    prefix_salt.append(salt)
                    # print(salt)
                    # print("prefix: ", element)
                elif mode == 1:
                    salt = octalString2Int(element)
                    suffix_salt.append(salt)
                    #print(salt)
                    #print("prefix: ", element)
        hash_password = hashlib.md5(bytes(prefix_salt)+bytes(password, 'ascii')+bytes(suffix_salt))
        data = {'username':'2207',
                'password':hash_password.hexdigest(),
                'dst': '',
                'popup':'true'
                }
        response = requests.post(url = "http://10.5.50.1/login", data = data)
        print(response)
    else :
        print("Already login")
