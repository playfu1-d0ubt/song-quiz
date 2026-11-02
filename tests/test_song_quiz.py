"""Tests for song_quiz.py."""

from song_quiz import (
    encode_password,
    get_choice,
    hint,
    read_lines,
    verify_password,
)


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


def test_verify_password_accepts_an_old_plain_text_password():
    """A stored value with no colon is treated as a plain-text password."""
    assert verify_password("hello", "hello") is True


def test_verify_password_rejects_the_wrong_old_plain_text_password():
    """A stored value with no colon is treated as a plain-text password."""
    assert verify_password("hello", "goodbye") is False


def test_verify_password_rejects_a_damaged_hash():
    """A stored value with a colon but no salt is treated as a damaged hash."""
    assert verify_password("hello", "zzzz:abcd") is False


def test_read_lines_returns_empty_list_when_file_is_missing(tmp_path):
    """A file that doesn't exist yet gives an empty list, not an error."""
    missing_file = tmp_path / "does_not_exist.txt"

    assert read_lines(missing_file) == []


def test_read_lines_skips_blank_lines_and_strips_spaces(tmp_path):
    """Blank lines and leading/trailing spaces are ignored."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("  a  \n\n  b  \n  c  ")

    assert read_lines(test_file) == ["a", "b", "c"]


def test_get_choice_returns_a_valid_answer(monkeypatch):
    """A valid answer is returned straight away."""
    monkeypatch.setattr("builtins.input", lambda prompt: "1")

    assert get_choice(":", ["1", "2", "-1"]) == "1"


def test_get_choice_asks_again_after_an_invalid_answer(monkeypatch):
    """An invalid answer is ignored and the user is asked again."""
    answers = iter(["A", "-1"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    assert get_choice(":", ["1", "2", "-1"]) == "-1"
