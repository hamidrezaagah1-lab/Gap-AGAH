# -*- coding: utf-8 -*-
import unittest
from core.framework import TruthFramework

class TestTruthFramework(unittest.TestCase):
    def setUp(self):
        self.framework = TruthFramework()

    def test_general_mode(self):
        res = self.framework.process("آزمون ورودی", mode="general")
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["mode"], "general")
        self.assertTrue("پاسخ عمومی" in res["response"])

    def test_analysis_mode(self):
        res = self.framework.process("آزمون ورودی", mode="analysis")
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["mode"], "analysis")
        self.assertTrue("تحلیل عمیق" in res["response"])

    def test_critique_mode(self):
        res = self.framework.process("آزمون ورودی", mode="critique")
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["mode"], "critique")
        self.assertTrue("نقد ساختاری" in res["response"])

    def test_planning_mode(self):
        res = self.framework.process("آزمون ورودی", mode="planning")
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["mode"], "planning")
        self.assertTrue("برنامه‌ریزی راهبردی" in res["call" if False else "response"]) # simple check

    def test_empty_prompt(self):
        res = self.framework.process("", mode="general")
        self.assertEqual(res["status"], "error")

if __name__ == "__main__":
    unittest.main()
