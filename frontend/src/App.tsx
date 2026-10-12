from datetime import datetime


def build_candidate_matches(profile_text: str):
    text = (profile_text or "").lower()
    if not text:
        return []

    matches = []
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

    for code, pack in pack_map.items():
        matched = []
        missing = []
        score = 0

        if any(word in text for word in ["electrician", "wiring", "switchboard", "multimeter", "fault", "circuit", "electrical"]):
            matched.append("Electrical work")
            score += 25

        if any(word in text for word in ["safety", "insulation", "grounding", "ppe", "testing"]):
            matched.append("Safety and testing")
            score += 25

        for criterion in pack["criteria"]:
            if any(part in text for part in criterion.lower().split()[:3]):
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
            "explanation": "AI suggestion only: this profile indicates relevant experience for the selected trade. Human assessor verification remains mandatory.",
            "matched_criteria": matched[:5],
            "missing_information": missing[:3],
            "verification_status": pack["verification_status"],
        })

    matches.sort(key=lambda item: item["score"], reverse=True)
    return matches
