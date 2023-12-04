from chatbox.bot import generate_response


def test_can_generate_response():
    # Given
    test_input = "Hello!"
    actual_output = generate_response(test_input)
    assert actual_output != ""
