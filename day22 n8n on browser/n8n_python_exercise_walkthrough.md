# n8n + Python — Complete Walkthrough
Follow every step in order. Don't skip Part 0 — nothing else works without it.

---

## Part 0: Install and Open n8n

1. Go to **n8n.io/download** and download the installer for your OS (Windows `.exe` or Mac `.dmg`).
   - No install permissions? Skip to the **alternative** box at the bottom of this section instead.
2. Run the installer and click through the prompts (like any normal app install).
3. Open the **n8n Desktop** app from your Start Menu / Applications folder.
4. On first launch, create an owner account: enter any email + password. This stays on your machine — nothing is sent anywhere.
5. You'll land on a blank canvas. This is the **Editor** — where you'll build both exercises.

> **No install permissions / on Linux?**
> Open a terminal and run:
> ```
> npx n8n
> ```
> (requires Node.js 18+ — check with `node -v`). Wait for it to say `Editor is now accessible via: http://localhost:5678`, then open that URL in your browser.

---

## Part 1: Exercise 1 — Your First Workflow

**Goal:** pull data from a public API and reshape it. No Python yet.

1. On the n8n home screen, click **+ Add workflow** (or **New workflow**) — you get a blank canvas.
2. Click the **+** button in the middle of the canvas. In the search box, type `manual` and select **"Trigger manually"**. This node now sits on your canvas.
3. Click the small **+** on the right edge of that node. Search `HTTP Request` and select it.
4. With the HTTP Request node selected, the parameters panel opens on the right:
   - **Method:** leave as `GET`
   - **URL:** paste `https://jsonplaceholder.typicode.com/users/1`
5. Click **Execute step** (small play icon on the node, or the panel's "Test step" button). A green checkmark appears and you'll see JSON data returned in the output panel below.
6. Click the **+** on the HTTP Request node's right edge. Search `Edit Fields` and select **"Edit Fields (Set)"**.
7. In its parameters panel:
   - Mode should already be **"Manual Mapping"**
   - Click **+ Add Field**. Set **Name** = `studentName`, **Type** = `String`, **Value** = `{{ $json.name }}`
     - Tip: click inside the Value box, then click the small **fx / expression** icon if it doesn't already accept `{{ }}` — this tells n8n the value is dynamic, not literal text.
   - Click **+ Add Field** again. Set **Name** = `studentEmail`, **Type** = `String`, **Value** = `{{ $json.email }}`
8. Click **Execute Workflow** (top right, or bottom of canvas). All three nodes should turn green.
9. Click the **Edit Fields (Set)** node and open its **Output** tab. You should see:
   ```json
   [
     {
       "studentName": "Leanne Graham",
       "studentEmail": "Sincere@april.biz"
     }
   ]
   ```
10. Save the workflow: `Ctrl+S` (or the **Save** button top right). Name it `Exercise 1`.

**If the output doesn't match:**
- Nodes not connected? Drag from the small dot on one node's right edge to the next node's left edge.
- Values showing as literal text like `{{ $json.name }}` instead of the real name? The field isn't in expression mode — click the `fx` icon next to that field.

---

## Part 2: Exercise 2 — ML Prediction Pipeline

**Goal:** n8n calls a real Python service and gets a prediction back.

### 2a. Start the Python prediction service

1. Open a terminal (separate from n8n — leave n8n running).
2. Create a new folder and move into it:
   ```
   mkdir n8n-python-exercise
   cd n8n-python-exercise
   ```
3. Create a file named `tiny_model.py` and paste this exactly:
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
4. Install Flask and run the server:
   ```
   pip install flask
   python tiny_model.py
   ```
5. Confirm the terminal shows something like `Running on http://127.0.0.1:5000`. **Leave this terminal open and running** for the rest of the exercise.

### 2b. Build the n8n workflow

1. Back in n8n, create another **New workflow**.
2. Add a **Manual Trigger** node the same way as step 2 in Exercise 1 (`+` → search `manual` → "Trigger manually").
3. Click **+** on the trigger, search `Edit Fields`, select **"Edit Fields (Set)"**. In its panel:
   - **+ Add Field**: Name = `study_hours`, Type = `Number`, Value = `6`
   - **+ Add Field**: Name = `attendance`, Type = `Number`, Value = `85`
4. Click **+** on that Set node, search `HTTP Request`, select it. In its parameters panel:
   - **Method:** change the dropdown from `GET` to `POST`
   - **URL:** `http://localhost:5000/predict`
   - Scroll down and turn ON **Send Body**
   - **Body Content Type:** select `JSON`
   - A **JSON** text box appears — paste:
     ```
     {
       "study_hours": {{ $json.study_hours }},
       "attendance": {{ $json.attendance }}
     }
     ```
     - If the field shows this as plain text instead of evaluating it, click the `fx` icon on that field to switch it to expression mode.
5. Click **Execute Workflow**. All nodes should turn green.
6. Click the **HTTP Request** node and open its **Output** tab. You should see:
   ```json
   {
     "prediction": "Pass",
     "confidence": 0.82
   }
   ```
7. **Try it again with different numbers:** go back to the Set node, change `study_hours` to `1` and `attendance` to `20`, then click **Execute Workflow** again. The prediction should now flip to `"Fail"`.
8. Save the workflow: `Ctrl+S`, name it `Exercise 2`.

**Common issues:**
| Symptom | Fix |
|---|---|
| "ECONNREFUSED" / connection error | `tiny_model.py` isn't running — go back to your terminal and re-run `python tiny_model.py` |
| Prediction always blank or error | Body Content Type isn't set to `JSON`, or Send Body is off |
| Wrong / unexpected prediction | Check the Set node fields are Type = `Number`, not `String` |
| "Address already in use" when starting Flask | An old `tiny_model.py` process is still running — close that terminal first, or use a different port in both the script and the n8n URL |

---

## Part 3 (Optional): Import the Ready-Made Solutions

If your class provided `exercise1_first_workflow.json` and `exercise2_prediction_pipeline.json`, you can load a fully working version instantly:

1. In n8n, open the menu (⋯ top right, or press `Ctrl+O`).
2. Select **Import from File**.
3. Choose the `.json` file.
4. The complete workflow appears on your canvas, already connected.

Use this to check your work, or as a fallback if you get stuck — not as a shortcut to skip building it yourself.
