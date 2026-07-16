# -*- coding: utf-8 -*-
import sys
from core.framework import TruthFramework

def main():
    print("--- سیستم تحلیل حقیقت‌جو (مبتنی بر ارزش‌های اسلامی و ضد هژمونی) ---")
    if len(sys.argv) < 2:
        print("راهنما: python app.py <متن_ورودی> [حالت_پردازش]")
        print("حالت‌های پردازش: general, analysis, critique, planning")
        return
    
    prompt = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "general"
    
    framework = TruthFramework()
    result = framework.process(prompt, mode=mode)
    
    if result["status"] == "success":
        print(f"[{result['mode'].upper()}] پاسخ:")
        print(result["response"])
    else:
        print(f"خطا: {result['response']}")

if __name__ == "__main__":
    main()
