# ChatGPT Telegram Bot
## Setup
1) Execute `pip install -r requirements.txt`
2) Choose Version1 or Version2 bot(Read more below)
3) Open settings.py file and Insert _OpeanAI API Key_ or _ChatGPT_ Token in the CHATGPTTOKEN variable
4) Insert Telegram Bot Token in the BOTTOKEN variable
5) Change ChatGPT settings (optional)
6) Start bot_v1.py or bot_v2.py
## Version #1
First version uses official OpenAI API. Without changing default settings, the results may not be the best. Here is a little guide for setting up the first version of the bot
> Model – The model which will generate complection. You can see all models on https://beta.openai.com/playground
> Temperature – Controls randomness (0-1)
> Max tokens – The maximum numbers of tokens to generate (1-4000)
> Top P – Controls diversity via nucleus sampling (0-1)
> Frequency Penalty – How much to penalize new tokens based on their existing frequency in the text so far (0-1)
> Presence Penalty – How much to penalize new tokens based on whether they appear in the text so far (0-1)

You can change all settings in settings.py file
## Version #2
Second version uses 3-rd party API, it uses selenium python module. So it opens ChatGPT site in browser and gets data from it. It uses original ChatGPT model, that's it's advantage. 
1. Go to https://chat.openai.com/chat and open the developer tools by F12
2. Find the `__Secure-next-auth.session-token` cookie in `Application` > `Storage` > `Cookies` > `https://chat.openai.com`.
3. Copy the value in the `Cookie Value` field.
4. Insert it in CHATGPTTOKEN variable

![alt text](https://user-images.githubusercontent.com/19218518/206170122-61fbe94f-4b0c-4782-a344-e26ac0d4e2a7.png)
