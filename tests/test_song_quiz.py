from song_quiz import hint


def test_hint_keeps_punctuation_and_hides_letters():
    """The first letter shows, letters are hidden, and a hyphen stays visible."""
    assert hint("Half-life") == "H _ _ _ - _ _ _ _"

def test_hint_with_a_single_letter():
    """If the title is a single letter, it should be shown."""
    assert hint("A") == "A"