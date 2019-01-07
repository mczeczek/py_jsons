#!/usr/bin/python

import re, sys, os, json, webbrowser, datetime
from datetime import datetime, date, time
from const import *

def py_jsons(file_url, group_by="", attach_original_file=True):
    event = ""
    file_exists = os.path.isfile(file_url)
    if (file_exists):
        bashCommand = "cd " + os.path.dirname(file_url)
        os.system(bashCommand)
        # Open file as file object, read to string and close
        ifile = open(file_url,"r")
        log_file = ifile.read()
        ifile.close()
        
        # For all jsons a regex "\{(\s|.)*?\n\}\n" can be used
        regex = "\{(\s|.)*?\n\}\n"
        pattern = re.compile(regex, re.DOTALL | re.MULTILINE)

        # Open output file HTML and start writing some stuff
        timestamp = str(datetime.now()).replace(":", "-")
        report_file_url = os.path.dirname(file_url) + "/" + os.path.basename(file_url)[:-4]+ "_event_report_" + timestamp + ".html"
        html_report = open(report_file_url,"w")
        html_report.write(HTML_START)
        if (attach_original_file):
            html_report.write(HTML_COL1 + "Original log file: " + file_url + HTML_COL2)
            html_report.write(HTML_COL3 + log_file + HTML_COL4)
                    
        html_report.write(HTML_COL5 + "Found JSONs in file " + file_url + HTML_COL6)
        # Main loop to go through the whole log file and find matching expression
        for match in pattern.finditer(log_file):
            found_json = "%s" % (match.group(0))
            d = json.loads(found_json)
            value = d[group_by]
            html_report.write(HTML_COL1 + value + HTML_COL2)
            html_report.write(HTML_COL3 + found_json + HTML_COL4)
        html_report.write(HTML_STOP)
        html_report.close()
        #Open report in web browser
        webbrowser.open_new_tab("file://" + report_file_url)
    else:
        print(file_url + " file not found.")
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        furl = str(sys.argv[1])
        group = str(sys.argv[2])
        print(furl + " file will be used")
        add_orig_file = True
        py_jsons(furl, group, add_orig_file)
    else:
        print("Input file is missing. Please run as follows:\n python py_jsons.py FILE GROUP")
