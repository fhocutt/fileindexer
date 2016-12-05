#!usr/bin/env python3
"""Tests for counter.py"""

import pytest

from fileindexer.counter import split_words, count_frequency, find_top_words


def test_split_words_empty_string():
    assert split_words('') == []


def test_split_words_one_word():
    assert split_words('ABCabc123') == ['ABCabc123']


def test_split_words_all_symbols():
    assert split_words('!@#$%^&*') == []


def test_split_words_with_accent():
    assert split_words('Est-ce que ça te plaît?')\
        == ['Est', 'ce', 'que', 'a', 'te', 'pla', 't']


def test_split_words_long_file():
    # code to test
    with open('files/anne_of_green_gables.txt') as book:
        text = book.read()
    word_list = split_words(text)

    # reference/correct list
    with open('files/anne_of_green_gables_word_list.txt') as reference:
        correct_list_str = reference.read()
    correct_list = eval(correct_list_str)

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


def test_count_frequency_non_latin_input():
    assert count_frequency(['漢字', '漢字']) == {'漢字': 2}


def test_count_frequency_book_length_input():
    # code to test
    with open('files/anne_of_green_gables_word_list.txt') as word_list_file:
        word_list_str = word_list_file.read()
    word_list = eval(word_list_str)
    freq_dict = count_frequency(word_list)

    # reference/correct list
    with open('files/anne_of_green_gables_freq_dict.txt') as reference:
        correct_freq_dict_str = reference.read()
    correct_freq_dict = eval(correct_freq_dict_str)

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
    with open('files/anne_of_green_gables_freq_dict.txt') as freq_dict_file:
        freq_dict_str = freq_dict_file.read()
    freq_dict = eval(freq_dict_str)
    top_words = find_top_words(freq_dict)

    # reference/correct list
    with open('files/anne_of_green_gables_top_words.txt') as reference:
        correct_top_words_str = reference.read()
    correct_top_words = eval(correct_top_words_str)

    assert top_words == correct_top_words
