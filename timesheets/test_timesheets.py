import unittest 
from unittest import TestCase
from unittest.mock import patch, call

import timesheets

class TestTimeSheet(TestCase):

    """ Mock the print function, check it was called with expected text"""
    
    @patch('builtins.print')
    def test_display_total(self, mock_print):
        timesheets.display_total(123)
        mock_print.assert_called_once_with('Total hours worked: 123')


    """ Mock input() to force it to return '2' """

    @patch('builtins.input', side_effect=['2'])
    def test_get_hours_for_day(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)


    """ Verify the get_hours_for_day function ignores non-numerical input """

    @patch('builtins.input', side_effect=['cat', '123pizza', '2.4'])
    def test_get_hours_for_day_validation(self, mock_input):
        hours = timesheets.get_hours_for_day('whatever')
        self.assertEqual(2.4, hours)


    """ Mock the get_hours_for_day function 
    and return predetermined numbers"""

    # @patch('timesheets.get_hours_for_day')
    # def test_get_hours(self, mock_get_hours):
    #     mock_hours = [5, 7, 9]
    #     mock_get_hours.side_effect = mock_hours
    #     days = ['m', 't', 'w']
    #     expected_hours = dict(zip(days, mock_hours))        
    #     hours = timesheets.get_hours(days)
    #     self.assertDictEqual(expected_hours, hours)


    @patch('timesheets.get_hours_for_day', side_effect=[5, 7, 9])
    def test_get_hours(self, mock_get_hours):
        days = ['m', 't', 'w']
        expected_hours = dict(zip(days,[5, 7,9]))        
        hours = timesheets.get_hours(days)

        self.assertDictEqual(expected_hours, hours)


    """ Mock the print function, check the correct calls are made in the expected order"""

    @patch('builtins.print')
    def test_display_hours(self, mock_print):
        example = {'M':3, 'T': 12, 'W': 8.5}

        expected_table_calls = [
            call('Day            Hours Worked   '),
            call('M              3              '),
            call('T              12             '),
            call('W              8.5            ')
        ]
        
        timesheets.display_hours(example)
        mock_print.assert_has_calls(expected_table_calls)


    """ This is an easy function to test - no mocking needed """
    
    def test_total_hours(self):
        example = {'M':3, 'T': 12, 'W': 8}  # total = 23
        total = timesheets.total_hours(example)
        self.assertEqual(23, total)


    """ Mock the alert function so no actual beeping needed """
    
    @patch('timesheets.alert')
    def test_alert_meet_min_hours_doesnt_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(12, 30)
        mock_alert.assert_called_once()


    @patch('timesheets.alert')
    def test_alert_meet_min_hours_exceed(self, mock_alert):
        timesheets.alert_not_meet_min_hours(45, 30)
        mock_alert.assert_not_called()




if __name__ == '__main__':
    unittest.main()