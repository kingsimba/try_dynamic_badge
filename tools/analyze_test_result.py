#!/usr/bin/env python3

import xml.dom.minidom
import argparse


def writeFile(filename: str, content: str):
    f = open(filename, "w")
    f.write(content)
    f.close()


def parseFile(filename: str):
    doc = xml.dom.minidom.parse(filename)
    suites = doc.getElementsByTagName("testsuites")[0]
    testCount = suites.getAttribute("tests")
    failureCount = suites.getAttribute("failures")

    testColor = ""
    msg = ""
    if int(failureCount) == 0:
        testColor = "green"
        msg = f"{testCount} passed"
    else:
        testColor = "red"
        msg = f"{failureCount} of {testCount} failed"

    print(f"Test Result: {msg} - {testColor}")
    writeFile("TEST_RESULT", f"TEST_RESULT={msg}\n")
    writeFile("TEST_COLOR", f"TEST_COLOR={testColor}\n")


parser = argparse.ArgumentParser()
parser.add_argument("file", help="File to parse", metavar="FILE")
args = parser.parse_args()
parseFile(args.file)
