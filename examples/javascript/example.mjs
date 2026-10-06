// Run the "Job Salary Data Scraper: Pay Transparency Jobs Feed" Apify Actor and print its results.
// Setup: npm install  &&  export APIFY_TOKEN=your_apify_token  &&  node example.mjs
// This repository only documents the Actor; its source code runs on Apify's infrastructure.
import { ApifyClient } from 'apify-client';

const token = process.env.APIFY_TOKEN;
if (!token) {
    console.error('Set the APIFY_TOKEN environment variable first (Apify Console > Settings > API & Integrations).');
    process.exit(1);
}

const client = new ApifyClient({ token });

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
console.log(`Run finished with status: ${run.status}`);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items, null, 2));
