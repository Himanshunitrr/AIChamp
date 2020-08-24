import csv
import re

import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from string import Template


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text


if __name__ == '__main__':
    x = 1
    while x <= 3:
        # field names
        fields = ["Profile %s" %(x)]

        # data rows of csv file
        rows = []
        str = "D:/Documents/AIChamp/Profiles/Profile (%s).pdf" % (x)
        x += 1
        info = extract_text_from_pdf(str)
        filteredInfo = re.findall("[a-zA-Z]+", info)
        rows.append(filteredInfo)
        # name of csv file
        filename = "testing.csv"

        # writing to csv file
        with open(filename, 'a') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(fields)

            # writing the data rows
            csvwriter.writerows(rows)
            # "Hello, %s. You are %s." % (name, age)
