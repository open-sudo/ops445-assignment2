import unittest
from unittest.mock import patch
import os
import solution
import argparse
from io import StringIO

class TestParseCommandLineArguments(unittest.TestCase):

    def test_parse_command_line_arguments(self):
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(directory_path='test_dir', search_criteria=['*.txt', '-type', 'f'])):
            args = solution.parse_command_line_arguments()
            self.assertEqual(args.directory_path, 'test_dir')
            self.assertEqual(args.search_criteria, ['*.txt', '-type', 'f'])

    @patch('sys.argv', ['solution.py', '-h'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_argparse_help_message(self, mock_stdout):
        with self.assertRaises(SystemExit):
            solution.parse_command_line_arguments()

        output = mock_stdout.getvalue()
        self.assertIn('usage:', output)
        self.assertIn('--directory', output)
        self.assertIn('--criteria', output)


class TestExecuteFindCommand(unittest.TestCase):

    def setUp(self):
        os.mkdir('test_dir')
        # Create test files
        for i in range(1, 3):
            with open(f'test_dir/file{i}.txt', 'w') as f:
                f.write('')

    def tearDown(self):
        # Clean up the test directory and files
        for i in range(1, 3):
            os.remove(f'test_dir/file{i}.txt')
        os.rmdir('test_dir')

    @patch('subprocess.Popen')
    def test_execute_find_command(self, mock_popen):
        mock_process = mock_popen.return_value
        mock_process.communicate.return_value = ('test_dir/file1.txt\ntest_dir/file2.txt\n'.encode('utf-8'), None)
        result = solution.execute_find_command('test_dir')
        self.assertEqual(result, 'test_dir/file1.txt\ntest_dir/file2.txt\n')

class TestFormatDateTimestamp(unittest.TestCase):

    def test_format_date_timestamp(self):
        timestamp = 1636542891
        result = solution.format_date_timestamp(timestamp)
        self.assertEqual(result, '10/11/2021 16:14:51')


class TestFormatFilesize(unittest.TestCase):

    def test_format_filesize(self):
        file_size = 1048576  # 1 MB
        result = solution.format_filesize(file_size)
        self.assertEqual(result, 1.0)

    def test_format_filesize_zero(self):
        file_size = 0  # 0 MB
        result = solution.format_filesize(file_size)
        self.assertEqual(result, 0.0)

class TestParseFindOutput(unittest.TestCase):

    def setUp(self):
        os.mkdir('test_dir')
        # Create test files
        for i in range(1, 3):
            with open(f'test_dir/file{i}.txt', 'w') as f:
                f.write('')

    def tearDown(self):
        # Clean up the test directory and files
        for i in range(1, 3):
            os.remove(f'test_dir/file{i}.txt')
        os.rmdir('test_dir')

    def test_parse_find_output(self):
        find_output = 'test_dir/file1.txt\ntest_dir/file2.txt\n'
        try: result = solution.parse_find_output(find_output)
        except Exception  as e:
            print(e)
        expected_result = [
            {'path': 'test_dir/file1.txt', 'size': 0, 'permissions': '0o644', 'modification_time': 0},
            {'path': 'test_dir/file2.txt', 'size': 0, 'permissions': '0o644', 'modification_time': 0}
        ]
        # Assert only given keys are present and equal to expected values
        for i in range(0, len(expected_result)):
            self.assertEqual(result[i]['path'], expected_result[i]['path'])
            self.assertEqual(result[i]['size'], expected_result[i]['size'])
            self.assertEqual(result[i]['permissions'], expected_result[i]['permissions'])

    def test_parse_find_output_empty(self):
        find_output = ''
        result = solution.parse_find_output(find_output)
        self.assertEqual(result, [])

class TestParseFileDetails(unittest.TestCase):

    def setUp(self):
        os.mkdir('test_dir')
        # Create test files
        for i in range(1, 3):
            with open(f'test_dir/file{i}.txt', 'w') as f:
                f.write('')

    def tearDown(self):
        # Clean up the test directory and files
        for i in range(1, 3):
            os.remove(f'test_dir/file{i}.txt')
        os.rmdir('test_dir')

    @patch('os.stat')
    @patch('os.path.getmtime')
    def test_parse_file_details(self, mock_getmtime, mock_stat):
        mock_stat.return_value.st_size = 0
        line = 'test_dir/file1.txt'
        result = solution.parse_file_details(line)
        expected_result = {'path': 'test_dir/file1.txt', 'size': 0, 'permissions': '0o644'}
        # Assert only given keys are present and equal to expected values
        self.assertEqual(result['path'], expected_result['path'])
        self.assertEqual(result['size'], expected_result['size'])
        # self.assertEqual(result['permissions'], expected_result['permissions'])


    def test_parse_file_details_nonexistent(self):
        line = '/nonexistent/file'
        with self.assertRaises(FileNotFoundError):
            solution.parse_file_details(line)

if __name__ == '__main__':
    unittest.main()
