#thaknks ethan
class CoursePortal:
    def __init__(self, course_name="Course Portal"):
        self.course_name = course_name
        self.__is_locked = False
        self.submissions = []

    def lock_portal(self):
        """Locks the portal to simulate a passed deadline."""
        self.__is_locked = True
        print(f"[{self.course_name}] The portal is now locked. Submissions are closed.")

    def accept_submission(self, student_name, submission="Assignment"):
        """Accepts a submission if unlocked; raises an error if locked."""
        if self.__is_locked:
            raise PermissionError("Cannot submit: The portal is locked because the deadline has passed.")
        
        self.submissions.append({
            "student_name": student_name,
            "submission": submission
        })
        print(f"Submission accepted from {student_name}: {submission}")

    def get_lock_status(self):
        """Getter method to safely read the private __is_locked state."""
        return self.__is_locked

if __name__ == "__main__":
    portal = CoursePortal("OOP 101")
   
    portal.accept_submission("Juan Dela Cruz", "activity1.py")
    portal.lock_portal()
    
    try:
        portal.accept_submission("Maria Santos", "activity1_late.py")
    except PermissionError as e:
        print(f"Error caught: {e}")