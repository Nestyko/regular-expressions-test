from unittest import TestCase
from index import change_date_format, extract_text_in_quotes, match_url_parts, match_terms_and_conditions_excercise

class TestRegularExpressions(TestCase):

    def test_change_date_format(self):
        date = "2026-01-02"
        expected_date = "02-01-2026"
        self.assertEqual(expected_date, change_date_format(date))

    def test_extract_text_in_quotes(self):
        text = '"Python" is really great, "Java" is statically typed and "PHP"... well, it\'s there.'
        self.assertEqual(['Python',  'Java', 'PHP', ],
                         extract_text_in_quotes(text))

    def test_match_url_parts(self):
        url = 'https://stacksuperflow.com/blog-post/222/section/tweets/usernames.xml'
        not_url = '/this/is/a/file/addresss/not/a/web/url'
        self.assertEqual(['stacksuperflow.com', 'tweets', 'usernames.xml'], match_url_parts(url))
        self.assertEqual([], match_url_parts(not_url))

    def test_match_terms_and_services_exercise(self):
        expected_result = {
            'waiver': """Except as provided herein, the failure to exercise a right or to require
performance of an obligation under this Terms shall not effect a party's
ability to exercise such right or require such performance at any time
thereafter nor shall be the waiver of a breach constitute a waiver of any
subsequent breach.""",
            'severability': """If any provision of these Terms is held to be unenforceable or invalid, such
provision will be changed and interpreted to accomplish the objectives of such
provision to the greatest extent possible under applicable law and the
remaining provisions will continue in full force and effect.""",
            'email': 'someexample@mycompany.com',
            'phone': '+144557788441',
        }
        with open('./terms_and_conditions.txt', 'r', encoding='utf-8') as file:
            self.assertEqual(expected_result, match_terms_and_conditions_excercise(file.read()))