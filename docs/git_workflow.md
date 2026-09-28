# Git workflow

## Rules
- main always works. Nobody pushes to main directly (enable branch protection:
  require a pull request and 1 approval).
- One branch per task: feature/<name>, fix/<name>, docs/<name>
  e.g. feature/triage-agent, feature/rag-ingestion
- Commit small and often, using: type: short description
  types: feat, fix, docs, test, refactor, chore
  e.g. "feat: add triage agent structured output"

## Daily flow
1. git checkout main && git pull
2. git checkout -b feature/your-task
3. Work, commit often
4. git push -u origin feature/your-task
5. Open a pull request, teammate reviews, squash-merge, delete the branch

## Tracking
- One GitHub Issue per task, labeled by week (week-1 ... week-13), with an owner.
- Link work with "Closes #<issue number>" in the PR description.
- Use a GitHub Projects board: To do / In progress / In review / Done.
- One Milestone per phase (setup, ML baseline, RAG, agents, governance, UI, evaluation).

## Never commit
- .env or any API key. If a key is ever committed, revoke it immediately;
  deleting the commit is not enough because it stays in history.
- Datasets or the Chroma vector store (already in .gitignore).

## Schema changes
A pull request touching agents/schemas.py needs approval from all three members.
