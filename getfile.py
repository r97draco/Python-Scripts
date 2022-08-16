import requests, sys, pyperclip

sys.argv

if (len(sys.argv)>1):
    add = sys.argv[1]

else :
    add = pyperclip.paste()

res = requests.get(add)
print(type(res))
print(len(res.text))
print(res.status_code)
print("--------------------------------")
print(res.text)

