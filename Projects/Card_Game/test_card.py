'''
Test for Card class in card.py
'''
import pytest
from card import Card


def test_inputs():
    '''
    Test different formats of suit and rank of same card
    to see if they are still equal
    '''
    spade_ace_a = Card("Spade", "A")
    spade_ace_b = Card("SPADE", "a")
    assert spade_ace_a == spade_ace_b

    club_three_a = Card("Club", 3)
    club_three_b = Card("club", "3")
    club_three_c = Card("Club", "three")
    assert club_three_a == club_three_b == club_three_c


def test_print():
    '''
    Test different formats of suit and rank of same card
    to check if print() will still output the same result
    '''
    output = "Ten of Spades"
    spade_ten_1 = Card("Spade", "ten")
    spade_ten_2 = Card("spAde", "10")
    spade_ten_3 = Card("SPADE", 10)
    assert str(spade_ten_1) == output
    assert str(spade_ten_2) == output
    assert str(spade_ten_3) == output


def test_attr():
    '''
    Test rank and suit attributes
    rank will return the value of the card (Ace being 14)
    suit will return a number based on hierarchy
    Club - 1, Diamond - 2, Heart - 3, Spade - 4
    '''
    heart_queen = Card("Heart", "Q")
    assert heart_queen.rank == 12
    assert heart_queen.suit == 3

    diam_six = Card("Diamond", 6)
    assert diam_six.rank == 6
    assert diam_six.suit == 2


def test_comparison():
    '''
    Test comparison of two card objects based on suit and rank
    '''
    spade_king = Card("Spade", "K")
    club_king = Card("Club", "K")
    assert (spade_king == club_king) is False
    assert (spade_king != club_king) is True
    assert (spade_king > club_king) is True
    assert (spade_king >= club_king) is True
    assert (spade_king < club_king) is False
    assert (spade_king <= club_king) is False


def test_sort():
    '''
    Test if the card objects are sortable based on suit and rank
    '''
    club_five = Card("Club", 5)
    spade_seven = Card("Spade", 7)
    heart_jack = Card("Heart", "J")
    club_queen = Card("Club", "Q")
    diamond_ace = Card("Diamond", "A")
    spade_ace = Card("Spade", "A")

    deck = sorted([heart_jack, spade_ace, club_five, diamond_ace, club_queen, spade_seven])
    assert deck[0] == club_five
    assert deck[1] == spade_seven
    assert deck[2] == heart_jack
    assert deck[3] == club_queen
    assert deck[4] == diamond_ace
    assert deck[5] == spade_ace
