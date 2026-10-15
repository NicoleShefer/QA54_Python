import csv
import json
from pathlib import Path


# ---------- Task 1 ----------
def save_test_ids(test_ids):
    with open("tests.txt", "w", encoding="utf-8") as f:
        for test_id in test_ids:
            f.write(f"{test_id}\n")


def add_test_id(test_id):
    with open("tests.txt", "a", encoding="utf-8") as f:
        f.write(f"{test_id}\n")


def load_test_ids(filename="tests.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


# ---------- Task 2 ----------
def get_test_statistics(filename):
    stats = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "total_duration_ms": 0,
        "failed_ids": [],
    }
    with open(filename, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            stats["total"] += 1
            if row["status"] == "PASSED":
                stats["passed"] += 1
            elif row["status"] == "FAILED":
                stats["failed"] += 1
                stats["failed_ids"].append(row["test_id"])
            stats["total_duration_ms"] += int(row["duration_ms"])
    return stats


# ---------- Task 3 ----------
def save_test_config(environment, base_url, timeout):
    config = {
        "environment": environment,
        "base_url": base_url,
        "timeout": timeout,
    }
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)


def load_test_config(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------- Task 4 ----------
def build_run_report(project_name, csv_filename):
    stats = get_test_statistics(csv_filename)

    report_dir = Path("reports") / project_name
    report_dir.mkdir(parents=True, exist_ok=True)

    summary = {
        "project": project_name,
        "total": stats["total"],
        "passed": stats["passed"],
        "failed": stats["failed"],
        "total_duration_ms": stats["total_duration_ms"],
    }
    with open(report_dir / "summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)

    with open(report_dir / "failed_tests.txt", "w", encoding="utf-8") as f:
        for test_id in stats["failed_ids"]:
            f.write(f"{test_id}\n")

    return summary


# ---------- Check ----------
if __name__ == "__main__":
    # Task 1
    save_test_ids(["QA-1", "QA-2"])
    add_test_id("QA-3")
    assert load_test_ids() == ["QA-1", "QA-2", "QA-3"]

    # Task 2
    with open("results.csv", "w", encoding="utf-8", newline="") as f:
        f.write("test_id,status,duration_ms\n")
        f.write("QA-1001,PASSED,120\n")
        f.write("QA-1002,FAILED,230\n")
        f.write("QA-1003,PASSED,150\n")

    assert get_test_statistics("results.csv") == {
        "total": 3,
        "passed": 2,
        "failed": 1,
        "total_duration_ms": 500,
        "failed_ids": ["QA-1002"],
    }

    # файл только с заголовками
    with open("empty.csv", "w", encoding="utf-8", newline="") as f:
        f.write("test_id,status,duration_ms\n")

    assert get_test_statistics("empty.csv") == {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "total_duration_ms": 0,
        "failed_ids": [],
    }

    # Task 3
    save_test_config("staging", "https://example.com", 30)
    config = load_test_config("config.json")
    assert config == {
        "environment": "staging",
        "base_url": "https://example.com",
        "timeout": 30,
    }
    assert type(config["timeout"]) is int

    save_test_config("prod", "https://prod.example.com", 60)
    config = load_test_config("config.json")
    assert config["environment"] == "prod"
    assert config["timeout"] == 60

    # Task 4
    result = build_run_report("Shop", "results.csv")
    assert result["total"] == 3 and result["failed"] == 1

    with open("reports/Shop/failed_tests.txt", encoding="utf-8") as f:
        assert f.read().strip() == "QA-1002"

    build_run_report("Shop", "results.csv")
    with open("reports/Shop/failed_tests.txt", encoding="utf-8") as f:
        assert f.read().splitlines() == ["QA-1002"]

    build_run_report("Empty", "empty.csv")
    with open("reports/Empty/failed_tests.txt", encoding="utf-8") as f:
        assert f.read() == ""

    print("All done")