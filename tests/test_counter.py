#!usr/bin/env python3
"""Tests for counter.py

Tests for the split_words, count_frequency, and find_top_words methods
of fileindexer.counter. Although Unicode code points and bytestrings are
not expected input, tests account for them so that any changes to
behavior are visible.

To test with a larger dataset, the following files are expected and
provided, courtesy of Project Gutenberg (https://www.gutenberg.org):
    files/anne_of_green_gables.txt
    files/anne_of_green_gables_word_list.json
    files/anne_of_green_gables_freq_dict.json
    files/anne_of_green_gables_top_words.json
"""

import json

import pytest

from fileindexer.counter import split_words, count_frequency, find_top_words


def test_split_words_empty_string():
    assert split_words('') == []


def test_split_words_one_word():
    assert split_words('ABCabc123') == ['ABCabc123']


def test_split_words_all_symbols():
    assert split_words('!@#$%^&*') == []


def test_split_words_Unicode_input():
    assert split_words('Est-ce que ça te plaît? 漢字') \
        == ['Est', 'ce', 'que', 'a', 'te', 'pla', 't']


def test_split_words_long_file():
    # code to test
    with open('files/anne_of_green_gables.txt') as book:
        text = book.read()
    word_list = split_words(text)

    # reference/correct list
    with open('files/anne_of_green_gables_word_list.json') as reference:
        correct_list = json.loads(reference.read())

    assert word_list == correct_list


def test_split_words_bytestring_input():
    with pytest.raises(TypeError):
        split_words(b'ABC abc 123')


def test_count_frequency_empty_list():
    assert count_frequency([]) == {}


def test_count_frequency_different_cases_same_word():
    words = ['chicken', 'CHICKEN', 'ChIcKeN']
    assert count_frequency(words) == {'chicken': 3}


def test_count_frequency_multiple_words():
    words = ['chicken', 'velociraptor', 'velociraptor', 'bat', 'bat']
    assert count_frequency(words) == {'chicken': 1, 'velociraptor': 2,
                                      'bat': 2}


def test_count_frequency_bytestring_input():
    assert count_frequency([b'chicken', 'chicken']) == {b'chicken': 1,
                                                        'chicken': 1}


def test_count_frequency_Unicode_input():
    assert count_frequency(['漢字', '漢字']) == {'漢字': 2}


def test_count_frequency_book_length_input():
    # code to test
    with open('files/anne_of_green_gables_word_list.json') as word_list_file:
        word_list = json.loads(word_list_file.read())
    freq_dict = count_frequency(word_list)

    # reference/correct list
    with open('files/anne_of_green_gables_freq_dict.json') as reference:
        correct_freq_dict = json.loads(reference.read())

    assert freq_dict == correct_freq_dict


# Dict has fewer items than the number requested
def test_find_top_words_small_dict():
    word_count = {'cat': 2, 'chicken': 5}
    assert find_top_words(word_count, 5) == [('chicken', 5), ('cat', 2)]


def test_find_top_words_empty_dict():
    assert find_top_words({}) == []


# Dict has more items than the number requested
def test_find_top_words_fewer_items():
    word_count = {'cat': 5, 'chicken': 3, 'velociraptor': 99}
    assert find_top_words(word_count, 2) == [('velociraptor', 99), ('cat', 5)]


def test_find_top_words_book_length_input():
    # code to test
    with open('files/anne_of_green_gables_freq_dict.json') as freq_dict_file:
        freq_dict = json.loads(freq_dict_file.read())
    top_words = find_top_words(freq_dict)
    # json reference file is a list of lists not a list of tuples, compare
    # as json
    top_words_json = json.dumps(top_words, indent=4)

    # reference/correct list
    with open('files/anne_of_green_gables_top_words.json') as reference:
        correct_top_words_json = reference.read()

    assert top_words_json == correct_top_words_json
