import os


def html_outfile():
    os.system(
        'airtest report test_case_web/__init__.py --log_root log --outfile log.html --lang zh --plugin airtest_selenium.report poco.utils.airtest.report --export .')
