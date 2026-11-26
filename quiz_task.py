from base_task import AcademicTask

class Quiz(AcademicTask):
    def __init__(self, title, max_points, total_questions):
        super().__init__(title, max_points)
        self.__total_questions = total_questions
        self.correct_answers = 0

    def submit_work(self, correct_answers):
        if 0 <= correct_answers <= self.__total_questions:
            self.correct_answers = correct_answers
            print(f"Quiz submitted: {self.title}")
        else:
            raise ValueError("Invalid number of correct answers.")

    def grade_work(self):
        self.is_graded = True
        return (self.correct_answers / self.__total_questions) * self.max_points

    def get_details(self):
        print(f"[QUIZ] {self.title} - Max Points: {self.max_points} - Questions: {self.__total_questions}")