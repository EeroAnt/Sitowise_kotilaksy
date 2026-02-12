def get_unique_keys(fields: list[str]) -> list[tuple[str, str]]:
    """Returns list of (original_field, unique_key) tuples."""
    counts = {}
    result = []
    
    for field in fields:
        count = counts.get(field, 0)
        counts[field] = count + 1
        
        if count == 0:
            unique_key = field
        else:
            unique_key = f"{field}_{count}"
        
        result.append((field, unique_key))
    
    return result