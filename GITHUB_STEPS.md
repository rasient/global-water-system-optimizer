# GitHub upload steps

## 1. Open the project folder

```bash
cd global_water_system_optimizer
```

## 2. Initialize Git

```bash
git init
git add .
git commit -m "Initial Global Water System Optimizer prototype"
```

## 3. Create a new GitHub repo

Recommended repo name:

```text
global-water-system-optimizer
```

Description:

```text
A Streamlit systems-thinking prototype for water resilience, precision irrigation, reuse, retention, and climate adaptation.
```

## 4. Connect local repo to GitHub

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/global-water-system-optimizer.git
git push -u origin main
```

## 5. Suggested GitHub topics

```text
water sustainability climate-agriculture systems-thinking streamlit python ai iot irrigation infrastructure
```

## 6. Optional: deploy on Streamlit Community Cloud

1. Go to Streamlit Community Cloud
2. Connect GitHub
3. Select this repository
4. Main file path:

```text
app/main.py
```

5. Add `OPENAI_API_KEY` only in Streamlit secrets if you want AI memo generation.
