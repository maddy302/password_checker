import sys
import hashlib
import requests
import getpass
'''
Source - https://haveibeenpwned.com/
@Madhukar
'''

class Pwned:
    api_key = ''
    req_url = 'https://api.pwnedpasswords.com/range/'
    pwd = ''
    def __init__(self, args):
        pwd = args[0]
    
    def hashpwdSha1(self, pwd):
        sha1 = hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()
        print('Entire hash of your password is {}'.format(sha1))
        return sha1

    def queryAPI(self,partialHash):
        res = requests.get(self.req_url+partialHash)
        #print(res.text)
        return res



def main(args):
    obj =  Pwned(args)
    pHash = obj.hashpwdSha1(args)
    head = pHash[:5]
    print('passing {} to the API'.format(head))
    res = obj.queryAPI(head)
    found = False
    for entry in res.text.splitlines():
        temp = entry.split(':')
        if(pHash[5:] == temp[0]):
            print('Your password was found as {} in {} occurances'.format(pHash, temp[1]))
            found = True
    if not (found):
        print('good it wasn\'t found')

if __name__ == '__main__':
    #inp = sys.argv[1:]
    try:
        print('Enter your password')
        pwd = getpass.getpass()
    except Exception as error:
        print('ERROR', error)
    else:
        main(pwd)

    