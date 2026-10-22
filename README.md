# 🚀 Merged

### "If Committed made 3M commits, how many Merges can we hit?"

Welcome to **Merged**, an experimental open-source social experiment aiming to become the repository with the **highest number of Pull Requests and Git Merges in history**. 

Inspired by the legendary *Committed* repository, this project tests the boundaries of GitHub's branching architecture using automated integration loops.

---

## 📊 Live Status
* **Current Goal:** 1,000,000 Automated Merges.
* **Status:** Running 24/7 via GitHub Actions.

---

## 🛠️ How It Works under the hood
Every few minutes, a secure background worker running via GitHub Actions triggers a Python routine that:
1. Spawns an isolated temporary `feature/` branch.
2. Appends unique cryptographic logs to the historical ledger.
3. Automatically triggers a `--no-ff` (No-Fast-Forward) master merge.
4. Cleans up references and pushes the updated tree back to GitHub.

---

## 🌟 Want to support the chaos?
If you like dumb or funny git experiments or just want to see how far GitHub servers can go before screaming:
1. Leave a **Star** ⭐ on this repository (it helps us climb the GitHub Trending ladder!).
2. **Fork** this project to run your own merge farm.
3. Open a manual Pull Request with any text! **Auto-merge is enabled**, so your profile will instantly join the contributor wall.

---
