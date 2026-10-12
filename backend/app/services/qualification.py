from typing import Any, Dict, List


def build_candidate_matches(profile_text: str) -> List[Dict[str, Any]]:
    text = (profile_text or "").lower()
    if not text:
        return []

    keyword_groups = {
        "electrical_work": ["electrician", "wiring", "switchboard", "circuit", "multimeter", "electrical", "fault"],
        "construction_work": ["construction", "maintenance", "repair", "installation", "site work"],
        "safety_and_testing": ["safety", "insulation", "testing", "grounding", "ppe", "fault detection"],
    }

    pack_map = {
        "QP-ELC-01": {
            "title": "Electrician General (Demonstration)",
            "nsqf_level": "Level 4",
            "criteria": ["Tool identification", "Electrical safety", "Wiring installation", "Fault diagnosis", "Testing equipment use"],
            "verification_status": "Demonstration record; requires official verification.",
        },
        "QP-WIRE-02": {
            "title": "Domestic Wiring Technician",
            "nsqf_level": "Level 3",
            "criteria": ["Basic wiring layout", "Switchboard installation", "Safety compliance", "Testing and troubleshooting"],
            "verification_status": "Demonstration record; requires official verification.",
        },
    }

    matches: List[Dict[str, Any]] = []
    for code, pack in pack_map.items():
        matched: List[str] = []
        missing: List[str] = []
        score = 0

        for group_name, terms in keyword_groups.items():
            if any(term in text for term in terms):
                matched.append(group_name.replace("_", " "))
                score += 25

        for criterion in pack["criteria"]:
            criterion_tokens = criterion.lower().split()[:3]
            if any(token in text for token in criterion_tokens):
                matched.append(criterion)
                score += 10
            else:
                missing.append(criterion)

        if not matched:
            score = 10
            missing = pack["criteria"]

        matches.append({
            "code": code,
            "title": pack["title"],
            "nsqf_level": pack["nsqf_level"],
            "score": round(min(score, 96), 1),
            "explanation": "This output is an AI relevance indicator only. It suggests likely qualification fit based on declared skills and work history, but it is not a certificate or proof of competence.",
            "matched_criteria": matched[:5],
            "missing_information": missing[:3],
            "verification_status": pack["verification_status"],
        })

    matches.sort(key=lambda item: item["score"], reverse=True)
    return matches


def build_ai_assessment_summary(profile_text: str) -> Dict[str, Any]:
    text = (profile_text or "").lower()
    issues = []
    if "multimeter" not in text:
        issues.append("No explicit multimeter evidence has been recorded.")
    if "safety" not in text:
        issues.append("Safety compliance evidence requires confirmation.")
    if "fault" not in text and "troubleshooting" not in text:
        issues.append("Fault diagnosis evidence is incomplete.")

    return {
        "summary": "Worker experience indicates relevant electrical and installation work. Human verification is required to confirm practical competence and safety compliance.",
        "issues": issues,
        "confidence": "Low to medium relevance indicator",
    }
