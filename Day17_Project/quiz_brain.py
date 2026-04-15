class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.user_score=0
        self.question_list=q_list
    
    def NextQuestion(self):
        current_question = self.question_list[self.question_number]
        question=input(f"Q:{self.question_number}:{current_question.text} (True/False):")
        self.question_number+=1
        self.check_answer(question, current_question.answer)
        
    def still_has_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else :
            return False
    def check_answer(self,question,correct_answer):
        if question.lower()==correct_answer.lower():
            print("you got it!")
            self.user_score+=1
        else:
            print("That's Wrong")
        print(f"The Correct Answer is {correct_answer}")
        print(f"The User Score is{self.user_score}/{self.question_number}")