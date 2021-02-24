from unittest import TestCase
import pypandoc

from docxApp.common.utils import zip_files


class CommonTest(TestCase):

    def test_return_empty(self):
        pypandoc.convert_file("template.docx", 'html', outputfile="tempalate.html")
