from nlplogic import corenlp


def test_get_phrases():
    assert "microsoft" in corenlp.get_noun_phrases("Microsoft")