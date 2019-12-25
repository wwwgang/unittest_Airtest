import os, glob

chromedrive_path = os.path.dirname(__file__) + '/tools/chromedriver'

log_path = os.path.dirname(__file__) + '/log'

case_path = os.path.dirname(__file__) + '/test_case'

report_path = os.path.dirname(__file__) + '/report.html'

rm_log = os.path.dirname(__file__) + '/log'

rm_logs = glob.glob(os.path.dirname(__file__) + r'/*log')

rm_reports_txt = os.path.dirname(__file__) + '/report.html'
