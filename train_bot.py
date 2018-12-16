import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    bot.train(data)
