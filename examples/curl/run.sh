#!/usr/bin/env bash
# Run the "Job Salary Data Scraper: Pay Transparency Jobs Feed" Apify Actor synchronously and print the dataset items.
# Usage: export APIFY_TOKEN=your_apify_token && ./run.sh
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN first (Apify Console > Settings > API & Integrations)}"

curl -sS -X POST "https://api.apify.com/v2/acts/leadsbrary~pay-transparency-salary-jobs-feed/run-sync-get-dataset-items" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "companies": [
    "greenhouse:coinbase",
    "lever:outreach"
  ],
  "useBuiltInSeedList": false,
  "atsSources": [
    "greenhouse",
    "lever"
  ],
  "countries": [],
  "titleKeywords": [],
  "remoteOnly": false,
  "currencies": [],
  "maxResults": 3,
  "maxCompanies": 50,
  "includeDescription": false,
  "proxyConfiguration": {
    "useApifyProxy": true
  }
}
JSON
