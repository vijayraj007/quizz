# modifed file 
import random
# create two teams

team_alpha = []
team_beta = []
# create a function to questions and answers 

def ask_questions(questions,answers):
    guess = input(questions + '\n')
    if guess.lower() == answers.lower():
        print('correct')
        return True
    else :
        print('incorrect')
        return False
  # list of questions & answers  
    
questions = [
    {'question' : 'what is python?', 'answer' : 'simple programming language'},
    {'question' : 'what is string?', 'answer' : 'collection of characters'},
    {'question' : 'what is list?',   'answer' : 'collection of homogeneous elements'},
    {'question' : 'what is mutability?', 'answer' : 'where we can change'}
]

#shuffle the questions
random.shuffle(questions)

for i, question in enumerate(questions):
    if i % 2 == 0 :
        team = team_alpha
    else :
        team = team_beta
    print('Team{i % 2 + 1}, it is your turn')
    if ask_questions(question['question'], question['answer']):
        team.append(question['answer'])

# mark scores 
score1 = len(team_alpha)
score2 = len(team_beta)

print('Team_alpha scored {score1} point')
print('Team_beta scored {score2} point')


if score1 > score2 :
    print('Team_alpha')
elif score2 > score1 :
    print('Team_beta wins')
else:
    print('it is a tie')


    # "this is modified by Venkatesh"
        
