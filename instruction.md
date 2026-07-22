You have an Apache-style access log at /app/access.log. Parse it and write a JSON report to /app/report.json.

The report must be a single JSON object with exactly these three keys:

- "total_requests": integer — total number of log lines (excluding blank lines)
- "unique_ips": integer — count of distinct client IP addresses
- "top_path": string — the URL path that appears most frequently in GET/POST requests

Success criteria:

1. /app/report.json exists and is valid JSON.
2. "total_requests" is the correct integer count of all requests in the log.
3. "unique_ips" is the correct count of distinct client IPs seen in the log.
4. "top_path" is the single path with the highest request count (exact string, e.g. "/index.html").
