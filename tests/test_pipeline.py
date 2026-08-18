from pathlib import Path

from src.pipeline import process_customers


def test_process_customers(tmp_path):

    input_file = tmp_path / "customers.csv"
    output_file = tmp_path / "output.csv"

    input_file.write_text(
        "customer_id,name,city,amount\n"
        "C001,Rahul,Delhi,1200\n"
        "C002,Amit,Mumbai,2500\n",
        encoding="utf-8"
    )

    rows = process_customers(input_file, output_file)

    assert len(rows) == 2
    assert rows[0]["customer_id"] == "C001"
    assert rows[0]["amount"] == 1200.0
    assert output_file.exists()