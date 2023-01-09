CHATGPTTOKEN = ""
BOTTOKEN = ""

#ChatGPT settings
model="text-davinci-003" # See README.md
temperature=0 # Controls randomness (0-1)
max_tokens=3000 # The maximum numbers of tokens to generate (1-4000)
top_p=1.0 #Controls diversity via nucleus sampling (0-1)
frequency_penalty=0.5 # How much to penalize new tokens based on their existing frequency in the text so far (0-1)
presence_penalty=0.0  # How much to penalize new tokens based on whether they appear in the text so far (0-1)