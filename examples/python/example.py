"""
Run the "Job Salary Data Scraper: Pay Transparency Jobs Feed" Apify Actor and print its results.

Setup:
    pip install -r requirements.txt
    export APIFY_TOKEN=your_apify_token   # Apify Console > Settings > API & Integrations

This repository only documents the Actor; its source code runs on Apify's infrastructure.
"""
import os
import sys

from apify_client import ApifyClient

ACTOR_ID = "leadsbrary/pay-transparency-salary-jobs-feed"

RUN_INPUT = {
    "companies": [
        "greenhouse:coinbase",
        "lever:outreach"
    ],
    "useBuiltInSeedList": False,
    "atsSources": [
        "greenhouse",
        "lever"
    ],
    "countries": [],
    "titleKeywords": [],
    "remoteOnly": False,
    "currencies": [],
    "maxResults": 3,
    "maxCompanies": 50,
    "includeDescription": False,
    "proxyConfiguration": {
        "useApifyProxy": True
    }
}


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set the APIFY_TOKEN environment variable first (Apify Console > Settings > API & Integrations).")
    client = ApifyClient(token)
    print(f"Starting {ACTOR_ID} ...")
    run = client.actor(ACTOR_ID).call(run_input=RUN_INPUT)
    print(f"Run finished with status: {run['status']}")
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)


if __name__ == "__main__":
    main()
