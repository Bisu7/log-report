import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_total_requests():
    """Criterion 1: report.json exists at /app/report.json with total_requests = 6."""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6, (
        f"expected total_requests=6, got {data.get('total_requests')}"
    )


def test_unique_ips():
    """Criterion 2: unique_ips equals 3 (192.168.0.1, 192.168.0.2, 10.0.0.5)."""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3, (
        f"expected unique_ips=3, got {data.get('unique_ips')}"
    )


def test_top_path():
    """Criterion 3: top_path is /index.html (requested 3 times, more than any other path)."""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html", (
        f"expected top_path='/index.html', got {data.get('top_path')}"
    )
