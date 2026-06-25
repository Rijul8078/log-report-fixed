import json


def load_report():
    with open("/app/report.json") as f:
        return json.load(f)


def test_total_requests():
    """Success criterion 2."""
    data = load_report()
    assert data["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3."""
    data = load_report()
    assert data["unique_ips"] == 3


def test_top_path():
    """Success criterion 4."""
    data = load_report()
    assert data["top_path"] == "/index.html"