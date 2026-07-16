# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session
import os
import uuid
from core.framework import TruthFramework
from core.storage import init_db, save_chat, get_history, clear_history

app = Flask(__name__)
app.secret_key = "truth_seeking_secret_key_v66"

# Initialize SQLite database
init_db()

framework = TruthFramework()

@app.route("/", methods=["GET", "POST"])
def index():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    
    session_id = session["session_id"]
    
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        mode = request.form.get("mode", "general")
        
        # Process request using Framework
        result = framework.process(prompt, mode=mode)
        
        # Save to SQLite
        if result["status"] == "success":
            save_chat(session_id, prompt, result["response"], result["mode"])
        
        return redirect(url_for("index"))
        
    history = get_history(session_id)
    return render_template("index.html", history=history)

@app.route("/clear", methods=["POST"])
def clear():
    if "session_id" in session:
        clear_history(session["session_id"])
    return redirect(url_for("index"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
