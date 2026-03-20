# Together For Better Mental Health — GAD-7 Checkpoint

A clean, animated web app that guides users through the **GAD-7 anxiety screening questionnaire**. Built as a single-page HTML/CSS/JS application with no frameworks or dependencies — just open `index.html` in any browser.

---

## File Structure

```
/
├── index.html   — Main HTML structure (all 3 screens)
├── style.css    — All styles, animations, and responsive layout
├── app.js       — Quiz logic, scoring, screen switching
├── images.js    — Base64-encoded character illustrations (auto-generated)
└── README.md    — This file
```

---

## How It Works

| Screen | Description |
|---|---|
| **Home** | Welcome screen with calm floating character, quiz info cards, Start/Contact buttons |
| **Question (×7)** | GAD-7 questions with matching animated character illustration, dot progress indicator, back button |
| **Result** | GAD-7 score display with colour-coded severity band and disclaimer |

### Scoring (GAD-7 Standard)

| Score | Severity |
|---|---|
| 0 – 4  | Minimal Anxiety |
| 5 – 9  | Mild Anxiety |
| 10 – 14 | Moderate Anxiety |
| 15 – 21 | Severe Anxiety |

---

## Running Locally

Simply open `index.html` in any modern browser — no server or build step required:

```bash
# Option 1: double-click index.html in your file manager

# Option 2: serve with Python (avoids any CORS issues with large JS files)
python3 -m http.server 8080
# then visit http://localhost:8080
```

> **Note:** Because `images.js` is ~2.3 MB (base64 images), some browsers may be slow to open the file directly. Using a local server (`python3 -m http.server`) gives the fastest load.

---

## Deploying to GitHub Pages

1. Push all files to a GitHub repository
2. Go to **Settings → Pages**
3. Set source to **Deploy from a branch → main → / (root)**
4. Your site will be live at `https://<username>.github.io/<repo-name>/`

---

## Customisation

### Changing questions
Edit the `questions` array in **`app.js`**:
```js
var questions = [
  { text: "Your question here?", img: IMAGES["q1"], color: "#4285F4" },
  // ...
];
```

### Changing scoring thresholds
Edit the `showResults()` function in **`app.js`**:
```js
if (totalScore <= 4)  { /* minimal */ }
else if (totalScore <= 9)  { /* mild */ }
else if (totalScore <= 14) { /* moderate */ }
else                       { /* severe */ }
```

### Changing colours
Edit the CSS variables at the top of **`style.css`**:
```css
:root {
  --teal: #4A9BB0;   /* primary accent colour */
  --bg:   #EEF4F8;   /* page background */
  /* ... */
}
```

### Replacing character images
Update **`images.js`** — replace any `IMAGES["q1"]` through `IMAGES["q7"]` and `IMAGES["calm"]` values with new base64-encoded PNG strings (transparent background recommended).

---

## Tech Stack

- **HTML5** — semantic structure
- **CSS3** — custom properties, keyframe animations, CSS Grid/Flexbox
- **Vanilla JS (ES5)** — no frameworks, no build tools
- **Google Fonts** — Nunito (loaded from CDN)

---

## Disclaimer

This tool is for **educational and awareness purposes only**. It is a screening tool, not a clinical diagnosis, and does not replace a professional evaluation. Users should consult a qualified mental health professional for an accurate assessment.
