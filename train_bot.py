import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def setup():
    bot=ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')


    for files in os.listdir('chatterbot-corpus-master/chatterbot_corpus/data/english/'):
        data=open('chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
        bot.set_trainer(ListTrainer)
        bot.train(data)


setup()