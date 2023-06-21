#!/usr/bin/env python3

#-----------------------------------------------------------------------------------------------------------
# Name: reports.py
# Details: Python's Program that has the libraries to crear a PDF report
# Author: xxxJonasxxx
# Date: 06/07/2023
#-----------------------------------------------------------------------------------------------------------

import reportlab

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(attachment)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])

  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])
