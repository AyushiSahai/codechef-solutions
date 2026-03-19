name: Update README Progress

on:
  push:
    paths:
      - 'Easy/**'
      - 'Medium/**'
      - 'Hard/**'
      - 'Contests/**'

jobs:
  update-readme:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v3

      - name: Count solutions and update README
        run: python3 update_readme.py

      - name: Commit and push changes
        run: |
          git config --global user.name "AyushiSahai"
          git config --global user.email "22A91A1291@aec.edu.in"
          git add README.md
          git diff --cached --quiet || git commit -m "Auto: Updated README progress"
          git push
