from HtmlTestRunner import HTMLTestRunner
from unittest import TestLoader, TestSuite
from eshop.tests.sample_test import SampleTest
from eshop.utils.config_parser import ConfigParser


def main():
    runner = HTMLTestRunner(**ConfigParser().get_report_params())
    runner.run(TestSuite(TestLoader().loadTestsFromTestCase(SampleTest)))


if __name__ == "__main__":
    main()
