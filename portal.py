class CoursePortal:
    def __init__(self, course_name):
        self.course_name = course_name
        self.__is_locked = False

    def lock_portal(self):
        self.__is_locked = True
        print(f"The portal for {self.course_name} is now locked.")
        print(f"Deadline passed. Portal for {self.course_name} is now locked.")

    def accept_submission(self, student_name):
        if self.__is locked:
            raise ValueError("Error: Deadline has passed. Submission rejected,")
        else:
            print(f"Submission accepted for {student_name}.")

