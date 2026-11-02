from song_quiz import encode_password, hint, verify_password


def test_hint_keeps_punctuation_and_hides_letters():
    """The first letter shows, letters are hidden, and a hyphen stays visible."""
    assert hint("Half-life") == "H _ _ _ - _ _ _ _"

def test_hint_with_a_single_letter():
    """If the title is a single letter, it should be shown."""
    assert hint("A") == "A"

def test_verify_password_accepts_the_right_password():
    """A password checks out against its own hash."""
    stored = encode_password("secret123")

    assert verify_password("secret123", stored) is True

def test_verify_password_rejects_wrong_password():
    """A password should not check out against a different hash."""
    stored = encode_password("secret123")

    assert verify_password("wrongpassword", stored) is False

def test_verify_password_rejects_an_empty_stored_password():
    """An empty stored password should not check out against any password."""
    stored = ""

    assert verify_password("secret123", stored) is False