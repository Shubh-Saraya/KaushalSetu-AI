from typing import List


def build_candidate_matches(profile_text: str):
    text = (profile_text or "").lower()
    keywords = {
        "electrician": ["electrician", "wiring", "switchboard", "circuit", "multimeter", "electrical", "fault", "safe wiring"],
        "construction": ["construction", "maintenance", "repair", "installation", "site work"],
        "safety": ["safety", "insulation", "testing", "grounding", "ppe", "fault detection"],
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

    matches = []
    for code, pack in pack_map.items():
        matched = []
        missing = []
        score = 0

        for label, terms in keywords.items():
            if any(term in text for term in terms):
                matched.append(label)
                score += 25

        for criterion in pack["criteria"]:
            if any(k in text for k in criterion.lower().split()[:3]):
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
            "explanation": f"This skill profile suggests a relevant match to {pack['title']}. The system flags this as a relevance indicator only, not as proof of competence.",
            "matched_criteria": list(dict.fromkeys(matched))[:5],
            "missing_information": missing[:3],
            "verification_status": pack["verification_status"],
        })

    matches.sort(key=lambda item: item["score"], reverse=True)
    return matches
