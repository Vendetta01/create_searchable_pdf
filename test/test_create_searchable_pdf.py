#!/usr/bin/env python3

import unittest
import tempfile
import subprocess
from shutil import copyfile
import pathlib
import filecmp


class TestCreateSearchablePDF(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        copyfile("input/testocr_eng.pdf", self.tmpdir.name + "/testocr_eng.pdf")
        copyfile("input/testocr_deu.pdf", self.tmpdir.name + "/testocr_deu.pdf")

    #@classmethod
    #def tearDownClass(self):
    #    pathlib.Path(self.tmpdir.name).unlink()

    def test_non_overwrite(self):
        in_file = "{}/testocr_eng.pdf".format(self.tmpdir.name)
        out_file = "{}.ocred.pdf".format(in_file)
        cmp_file = pathlib.Path("output/testocr_eng.pdf.ocred.pdf").absolute().as_posix()
        cmd = "../create_searchable_pdf.py {}".format(in_file)
        with subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
            out_stdout = p.stdout.read()
            out_stderr = p.stderr.read()
            #print("__DEBUG: out: {}".format(out_stdout))
            #print("__DEBUG: err: {}".format(out_stderr))
            input("test")
        self.assertTrue(filecmp.cmp(out_file, cmp_file, shallow=False))

    def test_overwrite(self):
        in_file = "{}/testocr_deu.pdf".format(self.tmpdir.name)
        out_file = in_file
        cmp_file = "output/testocr_deu.pdf"
        cmd = "../create_searchable_pdf.py -i {}".format(in_file)
        #with subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
        #        stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
        #    out_stdout = p.stdout.read()
        #    out_stderr = p.stderr.read()
        #self.assertTrue(filecmp.cmp(out_file, cmp_file, shallow=False))


if __name__ == '__main__':
    unittest.main()

