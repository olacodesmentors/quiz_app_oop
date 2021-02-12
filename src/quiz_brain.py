class QuizBrain:
  ''' QuizBrain will define all the necessary attributes and methods for quiz app'''

  def __init__(self, question_bank):
    '''This method is used to keep track of all the necessary variables'''

    # question_bank is a list of question objects and should be passed in as argument to QuizBrain class
    self.question_bank = question_bank
    # current_question keeps track the index of question that is being ask
    self.current_question = 0
    # Score keeps track of user score and it is initialized with 0
    self.score = 0

  def next_question(self):
    ''' This method should ask user a question and increment the self.current_question instance variable
        and call the check answer method
    '''
    self.check_answer(user_answer, correct_answer)


  def still_has_question(self):
    '''This method should return a boolean value. True if still has question, return false otherwise'''
    pass

  def check_answer(self, user_answer, correct_answer):
    '''
    This method should check if the user answer is correct.
      If correct increase the self.score variable and print the message
      else print a message for wrong answer
    print the current score to the user
     '''
    pass