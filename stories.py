"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb_1", "verb_2", "adjective_1", "adjective_2", "adjective_3", "plural_noun_1", "plural_noun_2"],
    """Once upon a time, on a {adjective_1} island there was a {adjective_2} {place}. There lived a 
    {adjective_3} {noun}. It loved to {verb_1} {plural_noun_1} and {verb_2} {plural_noun_2}."""
)