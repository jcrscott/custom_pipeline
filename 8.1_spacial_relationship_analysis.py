import pandas as pd

# Assuming df contains 'text' and 'bbox' columns
def assign_name_components(df, full_name):
    first, middle, last = '', '', ''
    name_parts = full_name.strip().split()
    
    if len(name_parts) == 3:
        first, middle, last = name_parts
    elif len(name_parts) == 2:
        first, last = name_parts
    else:
        first = name_parts[0]
        if len(name_parts) > 1:
            last = name_parts[-1]
    
    return first, middle, last

# Assigning to mapped_entities
first, middle, last = assign_name_components(df, mapped_entities.get('Full Name', ''))
mapped_entities['First Name'] = first
mapped_entities['Middle Name'] = middle
mapped_entities['Last Name'] = last