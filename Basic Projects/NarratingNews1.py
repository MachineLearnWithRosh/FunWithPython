import requests
import json


def speakBol(msg):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(msg)


#speakBol("Roshan bhai!! Khaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaana khaya?")

url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=275d980cf99e4a6dba844d602955d853')
india = requests.get(url=url).text
india = json.loads(india)
print(india['articles'][0]['description'])
dict_ind=india['articles']
print(len(india['articles']))
for i in dict_ind:
    print(i['title'])
    #print(i, india['articles'][i]['source']['name'])

num=int(input("Enter the input :"))
speakBol(india['articles'][num]['title'])
print("For more ",india['articles'][num]['url'])
print(india['articles'][num]['content'])
speakBol(india['articles'][num]['content'])
print(india['articles'][num]['description'])
speakBol(india['articles'][num]['description'])