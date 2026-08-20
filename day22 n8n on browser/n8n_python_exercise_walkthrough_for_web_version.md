# n8n Cloud + Python (VS Code) — Complete Walkthrough
Follow every step in order. Don't skip Part 0.

**Your setup:** n8n runs on n8n's servers (n8n.io / app.n8n.cloud), accessed in your browser. Python runs locally, in VS Code, on your own machine.

> **Why this matters:** n8n Cloud lives on the internet — it cannot reach `http://localhost:5000` on your laptop, because "localhost" from n8n's servers means *n8n's own server*, not yours. Exercise 1 doesn't care (it calls a public API). Exercise 2 does care, because it calls your local Python service — so we'll open a public tunnel to it with a free tool called **ngrok**. That's the one extra step versus running everything on one machine.

---

## Part 0: Get Into n8n

1. Go to **n8n.io** and click **Sign up** (or **Log in** if you already have an account).
2. Verify your email if asked. You'll land in your n8n Cloud workspace at a URL like `https://youraccount.app.n8n.cloud`.
3. Click **+ Create workflow** (or **New workflow**). You get a blank canvas — this is the **Editor**, same one you'll use for both exercises.

Nothing to install for n8n itself — it's fully in the browser.

---

## Part 1: Exercise 1 — Your First Workflow

**Goal:** pull data from a public API and reshape it. No Python yet, and no tunnel needed — the API is already public.

1. On the blank canvas, click the **+** button. Search `manual` and select **"Trigger manually"**.
2. Click the small **+** on that node's right edge. Search `HTTP Request` and select it.
3. In its parameters panel:
   - **Method:** leave as `GET`
   - **URL:** paste `https://jsonplaceholder.typicode.com/users/1`
4. Click **Execute step** on that node (or the panel's "Test step" button). You should see JSON appear below.
5. Click **+** on the HTTP Request node. Search `Edit Fields` and select **"Edit Fields (Set)"**.
6. In its panel:
   - **+ Add Field**: Name = `studentName`, Type = `String`, Value = `{{ $json.name }}`
     - If it shows the literal text instead of evaluating it, click the `fx` icon next to the field to switch it to expression mode.
   - **+ Add Field**: Name = `studentEmail`, Type = `String`, Value = `{{ $json.email }}`
7. Click **Execute Workflow** (top right). All three nodes should turn green.
8. Click **Edit Fields (Set)** → **Output** tab. You should see:
   ```json
   [
     {
       "studentName": "Leanne Graham",
       "studentEmail": "Sincere@april.biz"
     }
   ]
   ```
9. Save: `Ctrl+S`, name it `Exercise 1`.

---

## Part 2: Exercise 2 — ML Prediction Pipeline

**Goal:** n8n Cloud calls your local Python service (via a tunnel) and gets a prediction back.

### 2a. Write and run the Python service in VS Code

1. Open **VS Code**. Open a new folder (`File → Open Folder`) called `n8n-python-exercise`.
2. Create a new file in that folder named `tiny_model.py` (`File → New File`).
3. Paste this in exactly:
   ```python
   from flask import Flask, request, jsonify

   app = Flask(__name__)

   def predict(hours, attendance):
       score = hours * 4 + attendance * 0.5
       label = "Pass" if score >= 60 else "Fail"
       confidence = round(min(score / 100, 0.99), 2)
       return label, confidence

   @app.route("/predict", methods=["POST"])
   def predict_route():
       data = request.get_json()
       hours = data.get("study_hours", 0)
       attendance = data.get("attendance", 0)
       label, confidence = predict(hours, attendance)
       return jsonify({"prediction": label, "confidence": confidence})

   if __name__ == "__main__":
       app.run(port=5000)
   ```
4. Save the file (`Ctrl+S`).
5. Open VS Code's integrated terminal: **Terminal → New Terminal**.
6. In that terminal, run:
   ```
   pip install flask
   python tiny_model.py
   ```
   (On Mac, if `python` isn't found, use `python3` for both commands.)
7. Confirm it prints something like `Running on http://127.0.0.1:5000`. **Leave this terminal running** — don't close it or press Ctrl+C.

### 2b. Open a public tunnel with ngrok

Your Flask app only listens on your machine right now. ngrok gives it a temporary public URL.

1. Go to **ngrok.com**, sign up free, and follow their "Getting Started" page to download ngrok and run the one-time `ngrok config add-authtoken <your-token>` command (the site shows you your exact token).
2. In VS Code, open a **second** terminal (keep the Flask one running): click the **+** in the terminal panel, or **Terminal → New Terminal**.
3. In this new terminal, run:
   ```
   ngrok http 5000
   ```
4. ngrok shows a screen with a line like:
   ```
   Forwarding    https://a1b2-203-0-113-5.ngrok-free.app -> http://localhost:5000
   ```
   **Copy that `https://...ngrok-free.app` URL.** This is your public address for the rest of the exercise. **Leave this terminal running too** — you now have two terminals open, both must stay open.

   > ngrok's free URL changes every time you restart it. If you stop and re-run `ngrok http 5000` later, copy the new URL and update it in n8n.

### 2c. Build the workflow in n8n

1. Back in your n8n browser tab, create another **New workflow**.
2. Add a **Manual Trigger** node (`+` → search `manual` → "Trigger manually").
3. Click **+** on it, search `Edit Fields`, select **"Edit Fields (Set)"**:
   - **+ Add Field**: Name = `study_hours`, Type = `Number`, Value = `6`
   - **+ Add Field**: Name = `attendance`, Type = `Number`, Value = `85`
4. Click **+** on that node, search `HTTP Request`, select it. In its panel:
   - **Method:** change from `GET` to `POST`
   - **URL:** paste **your ngrok URL** + `/predict`, e.g. `https://a1b2-203-0-113-5.ngrok-free.app/predict`
   - Turn ON **Send Body**
   - **Body Content Type:** `JSON`
   - In the JSON box, paste:
     ```
     {
       "study_hours": {{ $json.study_hours }},
       "attendance": {{ $json.attendance }}
     }
     ```
     - Click the `fx` icon on that field if it's not evaluating the expressions.
5. Click **Execute Workflow**. All nodes should turn green.
6. Click the **HTTP Request** node → **Output** tab. You should see:
   ```json
   {
     "prediction": "Pass",
     "confidence": 0.82
   }
   ```
7. Try different numbers: edit the Set node to `study_hours = 1`, `attendance = 20`, re-run. Prediction should flip to `"Fail"`.
8. Save: `Ctrl+S`, name it `Exercise 2`.

**Common issues:**

| Symptom | Fix |
|---|---|
| n8n error like "could not resolve host" or timeout | ngrok URL is wrong or ngrok was restarted (new URL) — copy the current one from the ngrok terminal |
| "ERR_NGROK_..." page instead of a prediction | You forgot `/predict` at the end of the URL |
| Connection refused | `tiny_model.py` isn't running in VS Code — check the first terminal |
| Prediction blank or errors out | Body Content Type isn't `JSON`, or Send Body is off |
| Wrong prediction | Set node fields must be Type `Number`, not `String` |
| ngrok terminal closed by accident | Re-run `ngrok http 5000`, then paste the new URL into the HTTP Request node |

---

## Part 3 (Optional): Import the Ready-Made Solutions

1. In n8n, click the workflow menu (⋯) → **Import from File** (or **Import from URL**).
2. Choose `exercise1_first_workflow.json` or `exercise2_prediction_pipeline.json`.
3. For Exercise 2's imported workflow, you still need to **edit the HTTP Request node's URL** to match your own current ngrok address — the imported file has a placeholder `localhost` URL that won't work from n8n Cloud.

Use this as a check or a fallback if stuck, not a shortcut past building it yourself.
