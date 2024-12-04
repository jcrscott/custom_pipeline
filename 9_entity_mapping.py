# Define mapping
entity_mapping = {
    'PERSON': 'Full Name',
    'GPE': 'Address',
    'CARDINAL': 'License Number',
    # Add other mappings as necessary
}

mapped_entities = {}
for text, label in entities:
    if label in entity_mapping:
        field = entity_mapping[label]
        mapped_entities[field] = text

print(mapped_entities)