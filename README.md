# IPL Win Probability App

Streamlit app file: app.py
Model file: model.pkl

## Run locally

```powershell
pip install -r requirements.txt
streamlit run app.py
```

## Free deployment (Streamlit Community Cloud)

1. Create a new GitHub repository and push this project.
2. Open https://share.streamlit.io and sign in with GitHub.
3. Click New app.
4. Select your repository and branch.
5. Set Main file path to `app.py`.
6. Click Deploy.

## Notes

- Keep `model.pkl` in repository root next to `app.py`.
- If app fails due to package mismatch, pin exact versions in requirements.txt.
