# Job Salary Data Scraper: Pay Transparency Jobs Feed — Apify Actor usage guide

[![Run on Apify](https://img.shields.io/badge/Apify-Run%20this%20Actor-24C1E0)](https://apify.com/leadsbrary/pay-transparency-salary-jobs-feed?fpr=aupara)
[![Try Apify free](https://img.shields.io/badge/Apify-Try%20it%20free-24C1E0)](https://console.apify.com/sign-up?fpr=aupara)

Job salary data scraper for Greenhouse, Lever and Ashby boards: returns only postings with a disclosed pay range (min, max, currency, period, annual pay, country, remote). Export JSON, CSV, Excel.

> **This repository does not contain the Actor's source code.** The Actor is closed-source and
> runs on Apify's infrastructure. This repo is documentation plus ready-to-run client examples
> (curl, Python, JavaScript) that call the hosted Actor with **your own** Apify API token.

**Run it on Apify →** [https://apify.com/leadsbrary/pay-transparency-salary-jobs-feed?fpr=aupara](https://apify.com/leadsbrary/pay-transparency-salary-jobs-feed?fpr=aupara)

## What it does

You give it company job boards (for example `greenhouse:coinbase`, `lever:outreach`, `ashby:ramp`, or a public board URL), or switch on the built-in list of 35 boards. The Actor reads the public board APIs and keeps **only the postings with a disclosed salary range**. Postings without pay data are dropped, so you are never billed for them.

Each row contains the raw range (`salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod`), annualised values (`annualSalaryMin`, `annualSalaryMax`, `annualSalaryMid`), the range width in percent, a title family, a seniority guess, the country, a remote flag and the job URL.

## Use cases

- Salary benchmark by job title family, seniority and country
- Pay-transparency compliance monitoring (which employers publish ranges, and how wide they are)
- Salary-first job alerts (scheduled runs, only postings above a minimum annual pay)
- Training and evaluation data for salary-prediction models


## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `companies` | array | no | Boards to scan: 'greenhouse:stripe', 'lever:outreach', 'ashby:ramp' or a public board URL (boards.greenhouse.io/x, jobs.lever.co/x, jobs.ashbyhq.com/x). Invalid entries are logged and skipped. |
| `useBuiltInSeedList` | boolean | no | Adds a curated list of 35 public boards known to publish pay ranges (limited by 'Max companies'). |
| `atsSources` | array | no | Only scan boards of these vendors. |
| `countries` | array | no | Keep only postings in these ISO 3166-1 alpha-2 countries (e.g. US, GB, DE). Empty = all. |
| `titleKeywords` | array | no | Keep only postings whose title contains any of these words (case-insensitive). Empty = all. |
| `remoteOnly` | boolean | no | Keep only postings detected as remote. |
| `minAnnualSalary` | integer | no | Keep rows whose annualised maximum is at least this value, in the posting's own currency (no FX conversion). |
| `currencies` | array | no | Keep only these ISO 4217 currencies (e.g. USD, EUR). Empty = all. |
| `maxResults` | integer | no | Stop after this many salary rows (each one is billed). |
| `maxCompanies` | integer | no | Safety cap on the number of boards scanned per run. |
| `includeDescription` | boolean | no | Add the plain-text job description (max 5,000 chars). Makes datasets larger. |
| `proxyConfiguration` | object | no | Datacenter proxy used for the public board APIs. |

The full input form (with defaults and validation) is on the [Actor page](https://apify.com/leadsbrary/pay-transparency-salary-jobs-feed?fpr=aupara).


## Output (sample item)

Sample trimmed for readability (long texts and lists are shortened) — a real run returns the complete data.

```json
{
  "jobId": "greenhouse:coinbase:8175363",
  "ats": "greenhouse",
  "companySlug": "coinbase",
  "companyName": "Coinbase",
  "title": "Accelerations Programs Intern",
  "titleFamily": "other",
  "seniority": "intern",
  "department": "People Success",
  "employmentType": null,
  "location": "Hybrid - New York, NY",
  "country": "US",
  "isRemote": false,
  "salaryMin": 40,
  "salaryMax": 40,
  "salaryCurrency": "USD",
  "salaryPeriod": "HOUR",
  "annualSalaryMin": 83200,
  "annualSalaryMax": 83200,
  "annualSalaryMid": 83200,
  "rangeWidthPct": 0,
  "salaryLabel": "Hourly Rate",
  "salaryRangesCount": 1,
  "salaryRanges": [
    {
      "min": 40,
      "max": 40,
      "currency": "USD",
      "period": "HOUR",
      "label": "Hourly Rate"
    }
  ],
  "salarySource": "greenhouse.pay_input_ranges",
  "salaryPeriodSource": "label",
  "jobUrl": "https://www.coinbase.com/careers/positions/8175363?gh_jid=8175363",
  "applyUrl": null,
  "publishedAt": "2026-09-08T22:53:27.000Z",
  "updatedAt": "2026-09-22T17:02:37.000Z",
  "description": null,
  "scrapedAt": "2026-10-05T16:32:14.263Z"
}
```

## Pricing

Pay only for results: about **$0.54 per 1,000 results** on the Apify Free plan, down to **$0.36 per 1,000** on paid Apify plans.

Apify platform usage (compute) is billed by Apify on top of the per-result price — about **$0.01 per 1,000 results** in our measured test runs (estimate, varies with input). Tip: keep only the output formats and options you need to reduce it.

Prices can change — the [Actor page](https://apify.com/leadsbrary/pay-transparency-salary-jobs-feed?fpr=aupara) always shows the current pricing.

## Quick start

You need an Apify account and an API token (Apify Console → **Settings → API & Integrations**).
Never commit your token: export it as the `APIFY_TOKEN` environment variable.

### cURL

```bash
curl -X POST "https://api.apify.com/v2/acts/leadsbrary~pay-transparency-salary-jobs-feed/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
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
```

### Python (`apify-client`)

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
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

run = client.actor("leadsbrary/pay-transparency-salary-jobs-feed").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### JavaScript (`apify-client`)

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const runInput = {
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
};

const run = await client.actor('leadsbrary/pay-transparency-salary-jobs-feed').call(runInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

Runnable versions live in [`examples/`](./examples).

## Troubleshooting

- **401 / "User was not found or authentication token is not valid"** — check that `APIFY_TOKEN` is set and copied completely.
- **The run finished but the dataset is empty** — widen your search input or check the run log on the Apify Console.
- **Run stops early** — you may have reached the maximum cost per run you set in Apify; raise it in the run options.
- **Need something else?** Open an issue in this repository or use the Issues tab on the Actor page.

## Don't have an Apify account yet?

[Sign up here](https://console.apify.com/sign-up?fpr=aupara) — new accounts get $5 of free platform usage every month, enough to try most Actors without paying upfront.
Browse the full [Apify Store](https://apify.com/store?fpr=aupara) or [all Actors from this developer](https://apify.com/leadsbrary?fpr=aupara).

## Links

- Actor page: [https://apify.com/leadsbrary/pay-transparency-salary-jobs-feed?fpr=aupara](https://apify.com/leadsbrary/pay-transparency-salary-jobs-feed?fpr=aupara)
- All Actors from this developer: [https://apify.com/leadsbrary?fpr=aupara](https://apify.com/leadsbrary?fpr=aupara)
- Apify API reference: [https://docs.apify.com/api/v2](https://docs.apify.com/api/v2)

## Keywords

job salary data scraper, salary range jobs api, pay transparency jobs dataset, jobs with salary, salary benchmark data, greenhouse salary ranges, lever salary range, ashby compensation jobs, ats jobs salary, compensation data api, pay range scraper, salary dataset, job postings with salary

#salarydata #paytransparency #jobs #jobsdata #compensation #salarybenchmark #greenhouse #lever #ashby #hrtech #apify

## License

The example code in this repository is released under the MIT License — see [LICENSE](./LICENSE).
It does not cover the Actor itself, which remains closed-source and is operated by its developer on Apify.
