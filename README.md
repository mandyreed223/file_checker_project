# Required File Presence Checker

This project simulates an internal platform engineering policy for **LevelUp Bank**.

It uses:
- **Python** to check for required repo files
- **GitHub Actions** to run checks on pull requests and merges
- **AWS CloudWatch Logs** to store audit logs

---

## Required Files

On every run, the CI pipeline checks that these files exist in the **root** of the repo:

- `README.md`
- `.gitignore`

If any are missing, the workflow:
- Prints the missing files
- Exits with a non-zero status code
- Causes the GitHub Action to **fail**

---

## GitHub Secrets

This project uses GitHub **repository secrets** to store AWS credentials and log group names.

Define the following secrets:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION` (for example: `us-east-1`)
- `LOG_GROUP_NAME_BETA` = `/github-actions/required-files-checker/beta`
- `LOG_GROUP_NAME_PROD` = `/github-actions/required-files-checker/prod`

You can add these under:  
**Repo → Settings → Secrets and variables → Actions → New repository secret**

No AWS values are hardcoded in the code or workflow files.

---

## Running the File Presence Check Manually

From the repo root:

```bash
python check_required_files.py
