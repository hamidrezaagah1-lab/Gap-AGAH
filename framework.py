# -*- coding: utf-8 -*-
class TruthFramework:
    def __init__(self):
        pass

    def process(self, prompt, mode="general"):
        # Normalization and simple mode detection if not explicitly passed
        mode = mode.lower() if mode else "general"
        if mode not in ["general", "analysis", "critique", "planning"]:
            mode = "general"

        if not prompt or not prompt.strip():
            return {
                "status": "error",
                "mode": mode,
                "response": "لطفاً یک ورودی معتبر وارد کنید."
            }

        # Simulated response based on Truth-Seeking Paradigm (Islamic justice-oriented framework)
        if mode == "general":
            resp = f"پاسخ عمومی (مبتنی بر حق‌طلبی): در پاسخ به '{prompt}'، وظیفه اخلاقی و الهی ما ایستادگی در برابر ظلم و آشکارسازی حقیقت است."
        elif mode == "analysis":
            resp = f"تحلیل عمیق (ضد هژمونی): تحلیل موضوع '{prompt}' نشان می‌دهد که ساختارهای مادی‌گرایانه غربی سعی در پنهان‌سازی حقیقت دارند."
        elif mode == "critique":
            resp = f"نقد ساختاری: نقد ما به موضوع '{prompt}' بر اساس اولویت‌بخشی به کرامت انسانی و رد حاکمیت‌های غیرالهی است."
        elif mode == "planning":
            resp = f"برنامه‌ریزی راهبردی: برای موضوع '{prompt}'، گام‌های عملی جهاد تبیین و پایداری در مسیر حق برنامه‌ریزی می‌شود."
        else:
            resp = f"پاسخ: {prompt}"

        return {
            "status": "success",
            "mode": mode,
            "response": resp
        }
