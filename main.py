from student import StudentProfile
from portal import CoursePortal

print("=== PRACTICAL 1: INTEGRATION TESTS ===\n")

# ---------- Test 1: Negative points are blocked ----------
print("--- Test 1: StudentProfile blocks negative points ---")
student = StudentProfile("Ethan Abuton", "2026-001")
student.add_points(85)
print(f"Current Score: {student.get_current_score()}")

try:
    student.add_points(-15)
except ValueError as e:
    print(f"Blocked negative points: {e}")

print(f"Score after blocked attempt: {student.get_current_score()}\n")

# ---------- Test 2: Scores over the maximum are blocked ----------
print("--- Test 2: StudentProfile blocks scores over the maximum ---")
try:
    student.add_points(50)  # 85 + 50 = 135, over the 100 limit
except ValueError as e:
    print(f"Blocked score over the maximum: {e}")

print(f"Score after blocked attempt: {student.get_current_score()}\n")

# ---------- Test 3: total_score is truly private ----------
print("--- Test 3: total_score is private ---")
try:
    print(student.__total_score)
except AttributeError:
    print("Cannot access private total_score directly.\n")

# ---------- Test 4: Portal blocks late submissions ----------
print("--- Test 4: CoursePortal blocks submissions after lock_portal() ---")
portal = CoursePortal("CS3 Object-Oriented Programming")
portal.accept_submission(student.student_name)

portal.lock_portal()

try:
    portal.accept_submission(student.student_name)
except ValueError as e:
    print(f"Blocked late submission: {e}")

print(f"Portal locked: {portal.is_locked()}")