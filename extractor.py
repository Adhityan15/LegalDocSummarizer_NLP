import re

def extract_clauses(text):
    patterns = [
        r"(confidentiality.*?)(\n|$)",
        r"(termination.*?)(\n|$)",
        r"(liability.*?)(\n|$)",
        r"(governing law.*?)(\n|$)"
    ]
    clauses = {}
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            clause_title = match.group(1).split('\n')[0].strip().capitalize()
            clauses[clause_title] = match.group(0).strip()
    return clauses
