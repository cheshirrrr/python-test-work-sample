from main import PhoneNumberCheck

def test_text_block_parsing(block_data):
    title = block_data["title"]
    data = block_data["data"]
    solution = block_data["solution"]
    result = PhoneNumberCheck.parse_block(data)
    assert result == solution, f"Incorrect result in {title}"

def test_number_verbalization(verb_data):
    title = verb_data["title"]
    data = verb_data["data"]
    solution = verb_data["solution"]
    result = PhoneNumberCheck.verbalize_number(data)
    assert result == solution, f"Incorrect result in {title}"