import unittest

from buzz import generator

def test_sample_single_word():
    g = ('foo', 'bar', 'foobar')
    word = generator.sample(g)
    assert word in g

def test_sample_multiple_words():
    g = ('foo', 'bar', 'foobar')
    words = generator.sample(g, 2)
    assert len(words) == 2
    assert words[0] in g
    assert words[1] in g
    assert words[0] is not words[1]

def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5