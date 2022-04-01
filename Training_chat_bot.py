from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
my_bot = ChatBot(name='bud',
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
trainer = ListTrainer(my_bot)
#use the below dictionary to populate the questions and answers, message and reply in our case.
trainer.train([
'Hi',
'Hello',
'Question',
'Answer',
'Hi bot',
'Hello there',
'Bye bot',
'kudos'
])