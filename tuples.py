"""
Skill: Tuple indexing, slicing, comparison, string concatenation
"""

def get_coordinate(record):
    """Return the coordinate from a (treasure, coordinate) record."""
    return record[1]

def convert_coordinate(coordinate):
    """Convert '2A' format to ('2', 'A') tuple."""
    return (coordinate[0], coordinate[1])

def compare_records(azara_record, rui_record):
    """Return True if coordinates match between records."""
    return convert_coordinate(azara_record[1]) == rui_record[1]

def create_record(azara_record, rui_record):
    """Combine records if coordinates match, else return 'not a match'."""
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"

def clean_up(combined_record_group):
    """Return cleaned records with duplicate coordinates removed."""
    report = ""
    for record in combined_record_group:
        cleaned = record[:1] + record[2:]
        report += str(cleaned) + "\n"
    return report
