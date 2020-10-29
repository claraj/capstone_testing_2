import unittest 
from unittest import TestCase
from unittest.mock import patch, call

import game 

class TestGame(TestCase):

    @patch('random.choice', side_effect=['PAPER'])
    def test_computer_choice(self, mock_random):
        example_choices = ['ROCK', 'PAPER', 'SCISSORS']
        computer_choice = game.choose_computer_play(example_choices)
        self.assertEqual('PAPER', computer_choice)


    @patch('builtins.input', side_effect=['ROCK'])
    def test_human_choice(self, mock_random):
        example_choices = ['ROCK', 'PAPER', 'SCISSORS']
        human_choice = game.choose_human_play(example_choices)
        self.assertEqual('ROCK', human_choice)


    @patch('builtins.input', side_effect=['', '12345', 'not rock', '!!!!!', 'r', 'ROCK'])
    def test_human_choice_reject_invalid_choices(self, mock_random):
        example_choices = ['ROCK', 'PAPER', 'SCISSORS']
        human_choice = game.choose_human_play(example_choices)
        self.assertEqual('ROCK', human_choice)

    
    def test_determine_winner_human(self):
        valid_choices = ['rock', 'paper', 'scissors']
        self.assertEqual('human', game.determine_winner('rock', 'scissors', valid_choices))
        self.assertEqual('human', game.determine_winner('scissors', 'paper', valid_choices))
        self.assertEqual('human', game.determine_winner('paper', 'rock', valid_choices))


    def test_determine_winner_computer(self):
        valid_choices = ['rock', 'paper', 'scissors']
        self.assertEqual('computer', game.determine_winner('scissors', 'rock', valid_choices))
        self.assertEqual('computer', game.determine_winner('paper', 'scissors', valid_choices))
        self.assertEqual('computer', game.determine_winner('rock', 'paper', valid_choices))


    def test_determine_winner_tie(self):
        valid_choices = ['rock', 'paper', 'scissors']
        self.assertEqual('tie', game.determine_winner('scissors', 'scissors', valid_choices))
        self.assertEqual('tie', game.determine_winner('paper', 'paper', valid_choices))
        self.assertEqual('tie', game.determine_winner('rock', 'rock', valid_choices))


    def test_determine_winner_called_with_invalid_choices(self):
        valid_choices = ['rock', 'paper', 'scissors']

        with self.assertRaises(ValueError):
            # not a valid choice for human
            game.determine_winner('NOPE', 'scissors', valid_choices)


        with self.assertRaises(ValueError):
            # not a valid choice for computer
            game.determine_winner('rock', 'computer', valid_choices)


        with self.assertRaises(ValueError):
            # not a valid choice for both human and computer
            game.determine_winner('', 'hat', valid_choices)


if __name__ == '__main__':
    unittest.main()