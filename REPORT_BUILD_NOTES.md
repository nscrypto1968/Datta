# Fedfina risk-analysis internship report

## Deliverables

- `Risk Analysis at Fedbank Financial Services Ltd - Dattaguru Patil.pdf` — 100-page report.
- `Summer Intership Project final By DP.docx` — editable Word version of the report, replacing the prior draft.
- `Fedfina Risk Analyst Internship Workbook.xlsx` — public FY22–FY26 trend data plus blank monthly, trigger, bounce, risk-paper and RMC templates.

## Scope and evidence

The report is focused on FY2025–26 (year ended 31 March 2026). The supplied FY2023–24 and FY2024–25 annual reports provide historical context and cross-checks. Where older annual reports and the latest FY26 trend charts show different historical yield, spread or borrowing-cost figures, the report uses the latest FY26 series consistently and explicitly records the discrepancy.

No confidential monthly MIS, borrower-level data, internal risk-policy thresholds, bounce results or RMC working papers were supplied. These are not fabricated: associated report and workbook templates are left blank. The internship-particulars page is student-prepared and is **not** an employer-issued experience certificate. The phrase “ever graphs” is provisionally interpreted as EWS graphs and should be confirmed with the internship supervisor before submission.

Before submitting, verify the programme/institution wording, guide details and signatures with the institute, confirm the ambiguous task term, and attach only authentic employer documentation if required.

## Rebuild

The builder reads the supplied reference and annual-report PDFs in this repository. With Python 3.11+ and the system DejaVu font files installed:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-report.txt
.venv/bin/python report_builder.py
```

The source content is in `report_pages.py`; layout and workbook generation are in `report_builder.py`.
