# Fedfina risk-analysis internship report

## Deliverables

- `Risk Analysis at Fedbank Financial Services Ltd - Dattaguru Patil.pdf` — 100-page PDF report.
- `Risk Analysis at Fedbank Financial Services Ltd - Dattaguru Patil.docx` — editable Word report.

## Scope and evidence

The report is titled **Risk Analysis at Fedbank Financial Services Ltd** and uses Dattaguru Patil's supplied particulars (SYMMS, Roll No. M16144; Risk Analyst; 4 April–3 July 2026). It preserves the reference's six-page preliminary structure and fixes the report at 100 pages.

The primary company-data period is FY2025–26. The FY22–FY26 trend series, product disclosures, asset quality, capital, funding, maturity, ECL and interest-rate sensitivities are drawn from Fedfina's supplied FY26 annual report; FY24/FY25 reports are used for historical checks. RBI June 2026 NBFC statistics and stress scenarios are explicitly sector/sample-level and hypothetical, not Fedfina outcomes. RBI's 2025 gold/silver collateral rules are described with consumption-loan LTV limits distinguished from other eligible lending.

Q1 FY27 results for the quarter ended 30 June 2026 were published on 15 July, after the stated internship ended. They are separately labelled post-internship context; filed results are unaudited with a limited-review report, while operational explanations are attributed to management. No confidential monthly MIS, borrower-level data, internal risk-policy thresholds, bounce results or RMC working papers were supplied, so templates remain blank and no internal outcome is fabricated.

The student-supplied phrase **“Graphs & ever Graphs” remains unresolved**. EWS is presented only as one possible interpretation, with an explicit supervisor-confirmation note; references to EWS monitoring methods are conditional or general risk-analysis examples, not confirmed internship duties.

The internship-particulars page is student-prepared and is **not** an employer-issued experience certificate. Verify programme/institution wording, guide details and signatures with the institute, confirm the ambiguous task term with the supervisor, and attach only authentic employer documentation if required.

## Build and validation

The builder reads the supplied reference and annual-report PDFs in this repository. With Python 3.11+ and the system DejaVu font files installed:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-report.txt
.venv/bin/python report_builder.py
```

`report_pages.py` contains the page-by-page content; `report_builder.py` generates Word and PDF. The final PDF was verified at 100 pages and checked by page-text extraction and visual spot checks. The Word file includes the same six preliminary pages and fixed body-page breaks; final pagination can vary slightly across Word-compatible renderers, so recheck it in the institution's preferred version before submission.
