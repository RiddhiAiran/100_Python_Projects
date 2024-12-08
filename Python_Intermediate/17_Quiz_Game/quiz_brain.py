class QuizBrain:
    def __init__(self,question_list):
        self.q_num = 0
        self.q_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.q_num < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        user_ans = input(f"Q.{self.q_num}: {current_question.text} (True/False) : ")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_answer):
        if correct_answer.lower() == user_ans.lower():
            print("You got it Right!")
            self.score += 1
        else:
            print("That's Wrong")
        print(f"The Correct Answer is : {correct_answer}")
        print(f"Your Current Score is : {self.score}/{self.q_num}")
        print('\n')




