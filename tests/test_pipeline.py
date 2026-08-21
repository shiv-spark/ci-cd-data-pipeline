# from pathlib import Path

# from src.pipeline import process_customers


# def test_process_customers(tmp_path):

#     input_file = tmp_path / "customers.csv"
#     output_file = tmp_path / "output.csv"

#     input_file.write_text(
#         "customer_id,name,city,amount\n"
#         "C001,Rahul,Delhi,1200\n"
#         "C002,Amit,Mumbai,2500\n",
#         encoding="utf-8"
#     )

#     rows = process_customers(input_file, output_file)

#     assert len(rows) == 2
#     assert rows[0]["customer_id"] == "C001"
#     assert rows[0]["amount"] == 1200.0
#     assert output_file.exists()

from pathlib import Path

import pytest

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
    assert rows[1]["amount"] == 2500.0
    assert output_file.exists()


def test_empty_csv(tmp_path):
    input_file = tmp_path / "customers.csv"
    output_file = tmp_path / "output.csv"

    input_file.write_text(
        "customer_id,name,city,amount\n",
        encoding="utf-8"
    )

    rows = process_customers(input_file, output_file)

    assert rows == []
    assert output_file.exists()


def test_invalid_amount(tmp_path):
    input_file = tmp_path / "customers.csv"
    output_file = tmp_path / "output.csv"

    input_file.write_text(
        "customer_id,name,city,amount\n"
        "C001,Rahul,Delhi,invalid\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError):
        process_customers(input_file, output_file)


def test_missing_input_file(tmp_path):
    input_file = tmp_path / "missing.csv"
    output_file = tmp_path / "output.csv"

    with pytest.raises(FileNotFoundError):
        process_customers(input_file, output_file)


def test_output_content(tmp_path):
    input_file = tmp_path / "customers.csv"
    output_file = tmp_path / "output.csv"

    input_file.write_text(
        "customer_id,name,city,amount\n"
        "C001,Rahul,Delhi,1200\n",
        encoding="utf-8"
    )

    process_customers(input_file, output_file)

    content = output_file.read_text(encoding="utf-8")

    assert "customer_id,name,city,amount" in content
    assert "C001,Rahul,Delhi,1200.0" in content