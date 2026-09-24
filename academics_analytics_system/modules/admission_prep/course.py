"""
Handles admission preparation course and syllabus definitions.

This module keeps admission topics separate from UDVASH course units.
It does not handle schedules, preparation progress, assessments, or
planner logic.
"""

from pathlib import Path

from modules.config_loader import load_config
from modules.storage import load_json


BASE_DIR = Path(__file__).resolve().parent.parent.parent
TOPICS_FILE_PATH = BASE_DIR / "data" / "admission_prep" / "topics.json"
COURSES_FILE_PATH = BASE_DIR / "data" / "admission_prep" / "courses.json"


def get_all_topics():
    topics_data = load_json(TOPICS_FILE_PATH)
    return topics_data.get("topics", [])


def get_topic_by_id(topic_id):
    topics = get_all_topics()

    for topic in topics:
        if topic.get("id") == topic_id:
            return topic

    return None


def get_topics_by_subject(subject):
    topics = get_all_topics()
    normalized_subject = subject.strip().lower()

    return [
        topic
        for topic in topics
        if topic.get("subject", "").strip().lower() == normalized_subject
    ]


def get_all_course_units():
    courses_data = load_json(COURSES_FILE_PATH)
    return courses_data.get("courses", [])


def get_course_unit(unit_id):
    course_units = get_all_course_units()

    for unit in course_units:
        if unit.get("id") == unit_id:
            return unit

    return None


def get_course_units_by_subject(subject):
    course_units = get_all_course_units()
    normalized_subject = subject.strip().lower()

    return [
        unit
        for unit in course_units
        if unit.get("subject", "").strip().lower() == normalized_subject
    ]


def get_course_units_by_topic(topic_id):
    course_units = get_all_course_units()

    return [
        unit
        for unit in course_units
        if topic_id in unit.get("topic_ids", [])
    ]


def validate_topic(topic):
    if not isinstance(topic, dict):
        return {
            "status": "error",
            "message": "Topic must be a dictionary."
        }

    required_fields = ["id", "subject", "paper", "name"]

    for field in required_fields:
        if not topic.get(field):
            return {
                "status": "error",
                "message": f"Topic is missing required field: {field}."
            }

    config = load_config()
    admission_config = config.get("admission_prep", {})

    if topic["subject"] not in admission_config.get("subjects", []):
        return {
            "status": "error",
            "message": f"Invalid admission subject: {topic['subject']}."
        }

    if topic["paper"] not in admission_config.get("papers", []):
        return {
            "status": "error",
            "message": f"Invalid paper: {topic['paper']}."
        }

    return {"status": "success"}


def validate_course_unit(course_unit):
    if not isinstance(course_unit, dict):
        return {
            "status": "error",
            "message": "Course unit must be a dictionary."
        }

    required_fields = ["id", "code", "subject", "paper", "topic_ids"]

    for field in required_fields:
        if field not in course_unit:
            return {
                "status": "error",
                "message": f"Course unit is missing required field: {field}."
            }

    if not course_unit["id"] or not course_unit["code"]:
        return {
            "status": "error",
            "message": "Course unit id and code cannot be empty."
        }

    if not isinstance(course_unit["topic_ids"], list):
        return {
            "status": "error",
            "message": "Course unit topic_ids must be a list."
        }

    config = load_config()
    admission_config = config.get("admission_prep", {})

    if course_unit["subject"] not in admission_config.get("subjects", []):
        return {
            "status": "error",
            "message": f"Invalid admission subject: {course_unit['subject']}."
        }

    if course_unit["paper"] not in admission_config.get("papers", []):
        return {
            "status": "error",
            "message": f"Invalid paper: {course_unit['paper']}."
        }

    topics = {topic.get("id") for topic in get_all_topics()}
    missing_topic_ids = [
        topic_id
        for topic_id in course_unit["topic_ids"]
        if topic_id not in topics
    ]

    if missing_topic_ids:
        return {
            "status": "error",
            "message": f"Unknown topic IDs: {', '.join(missing_topic_ids)}."
        }

    return {"status": "success"}
