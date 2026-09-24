import unittest
from unittest.mock import patch

from modules.admission_prep import course


class TestAdmissionCourse(unittest.TestCase):

    def setUp(self):
        self.topic = {
            "id": "physics-01",
            "subject": "Physics",
            "paper": "1st",
            "name": "Kinematics"
        }

        self.course_unit = {
            "id": "P-01-P01",
            "code": "P-01",
            "part": 1,
            "title": "Sample Unit",
            "subject": "Physics",
            "paper": "1st",
            "topic_ids": ["physics-01"]
        }

    def test_get_topic_by_id(self):
        with patch.object(course, "load_json", return_value={
            "topics": [self.topic]
        }):
            result = course.get_topic_by_id("physics-01")

        self.assertEqual(result, self.topic)

    def test_get_course_unit_by_id(self):
        with patch.object(course, "load_json", return_value={
            "courses": [self.course_unit]
        }):
            result = course.get_course_unit("P-01-P01")

        self.assertEqual(result, self.course_unit)

    def test_get_course_units_by_topic(self):
        with patch.object(course, "load_json", return_value={
            "courses": [self.course_unit]
        }):
            result = course.get_course_units_by_topic("physics-01")

        self.assertEqual(result, [self.course_unit])

    def test_validate_topic(self):
        self.assertEqual(
            course.validate_topic(self.topic)["status"],
            "success"
        )

    def test_validate_course_unit_rejects_unknown_topic(self):
        with patch.object(course, "load_json", side_effect=[
            {"admission_prep": {
                "subjects": ["Physics", "Chemistry", "Higher Mathematics"],
                "papers": ["1st", "2nd"]
            }},
            {"topics": []}
        ]):
            result = course.validate_course_unit(self.course_unit)

        self.assertEqual(result["status"], "error")


if __name__ == "__main__":
    unittest.main()
