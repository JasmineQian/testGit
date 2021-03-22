#!/bin/sh
#export GOOGLE_APPLICATION_CREDENTIALS=credentials/service_account.json
cd /Users/jasqia/testGit/

# Debug commands for local run
# 1 Collect tests list
# pytest --collect-only ./tests/e2e/lsh/test_lsh.py --disable-pytest-warnings --junitxml=reports/junit.xml --cucumberjson=reports/cucumber.json
# 2 Show locals in tracebacks
# pytest -v -l --durations=0 ./tests/e2e/lsh/test_lsh.py --disable-pytest-warnings --junitxml=reports/junit.xml --cucumberjson=reports/cucumber.json

# Run tests
pytest ./tests/test_book.py

# Upload reports
#python ./scripts/upload_reports.py lsh-e2e
