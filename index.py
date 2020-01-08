import re


def change_date_format(date):
    """
    Convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
    Example: 2022-10-3 -> 3-10-2022
    """
    pass

def extract_text_in_quotes(text):
    """
    Match all the characteres between quotes
    """
    return re.findall(r'', text) # fill the regular expression to make the test pass

def match_url_parts(url):
    """
    Match some parts of the url, not some others. Only match if it is a valid URL
    Match: domain name, section name ,file name with extension.
    Do not match: protocol, blog post
    Example: https://truelogic.com/blog-post/334/section/finances/salary_list.json
    Match: ['truelogic.com', 'finances', 'salary_list.json']
    section name is 'finances' and it has this form in the URL 'section/<section_name>'
    the file name always comes last and has the extension, in the example is 'salary_list.json'
    """
    pass

def match_terms_and_conditions_excercise(data):
    """
    See the file "terms_and_conditions.txt" and match the waiver and severity pharagraphs,
    also match the email and phone and return a dictionary with the given info.
    See the test for the expected result.
    :return {'waiver': ..., 'severity': ..., 'email': ..., 'phone': ...}
    """
    pass