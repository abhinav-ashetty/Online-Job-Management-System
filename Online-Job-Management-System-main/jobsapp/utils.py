def calculate_skill_match(submitted_skills, required_skills):
    submitted_set = set(skill.strip().lower() for skill in submitted_skills.split(',') if skill)
    required_set = set(skill.strip().lower() for skill in required_skills.split(',') if skill)

    if not required_set:
        return 0

    matched = submitted_set & required_set
    return (len(matched) / len(required_set)) * 100