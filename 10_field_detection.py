# Example: Deduce State from Address
if 'Address' in mapped_entities and 'State' not in mapped_entities:
    address = mapped_entities['Address']
    # Simple extraction assuming state is last two letters
    state = address.strip().split()[-1]
    mapped_entities['State'] = state