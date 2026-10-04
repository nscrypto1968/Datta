from report_builder import Page
from report_data import *

AR26 = "Fedfina Annual Report 2025-26"
AR25 = "Fedfina Annual Report 2024-25"
AR24 = "Fedfina Annual Report 2023-24"


def cagr(a, b, years):
    return ((b / a) ** (1 / years) - 1) * 100


def pages(C):
    P = []

    # ------------------------------------------------------------------ 1 Certificate
    pg = Page("Certificate")
    pg.space(0.3)
    pg.p("COLLEGE STAMP HERE", align="center", bold_lead=None, size=10)
    pg.space(0.3)
    pg.p("This is to certify that the summer internship report titled “Fundamental Analysis of Fedbank Financial Services Limited” submitted in partial fulfilment for the MMS Degree Examination (Finance specialisation) of the University of Mumbai by Mr. Dattaguru Kallapa Patil (Roll No. M-16144) is a record of research work carried out by the student during the academic year 2026–27 under my guidance, and has been found satisfactory.")
    pg.p("The project work is original, is based on published information of the company and the sector, and has not been submitted earlier for the award of any degree, diploma or associateship of any other University or Institute.")
    pg.space(0.5)
    pg.table(["", "Project Guide", "Director", "External Examiner"],
             [["Name", "Dr. Rahul N. Wadekar / Dr. Prasad Supekar", "Dr. Rasika Mallya", ""],
              ["Signature", "", "", ""],
              ["Date", "", "", ""]], widths=[1.0, 2.4, 1.8, 1.8])
    pg.space(0.3)
    pg.p("DES’s Navinchandra Mehta Institute of Technology and Development, Dadar (W), Mumbai – 400028", align="center", italic=True)
    P.append(pg)

    # ------------------------------------------------------------------ 2 Declaration
    pg = Page("Declaration")
    pg.p("I hereby declare that this project report, submitted to DES’s Navinchandra Mehta Institute of Technology and Development in partial fulfilment of the requirements for the award of the degree of Master of Management Studies (Finance) of the University of Mumbai, is my bona fide work. It has not been submitted to any other University or Institute for the award of any degree, diploma or certificate, nor has it been published anywhere before.")
    pg.p("The analysis has been prepared purely for academic purposes from publicly available information, principally the Annual Reports of Fedbank Financial Services Limited for the financial years 2023–24, 2024–25 and 2025–26, together with regulatory material of the Reserve Bank of India and publicly reported results of peer companies. Every figure used in the report is traceable to one of these sources; where a figure has been computed by me from reported numbers it is marked as “derived”. No figure has been estimated, assumed or fabricated.")
    pg.p("The report does not constitute investment advice, a credit opinion or a valuation, and the views expressed are my own and do not represent the views of the company, its parent or the Institute.")
    pg.space(0.6)
    pg.table(["Particulars", "Details"],
             [["Name of the student", "Dattaguru Kallapa Patil"], ["Roll number", "M-16144"],
              ["Programme", "Master of Management Studies (Finance), 2026–27"],
              ["Title of the project", "Fundamental Analysis of Fedbank Financial Services Limited"],
              ["Place", "Mumbai"], ["Date", "____________________"], ["Signature", "____________________"]],
             widths=[2.2, 4.8])
    P.append(pg)

    # ------------------------------------------------------------------ 3 Acknowledgement
    pg = Page("Acknowledgement")
    pg.p("I express my sincere gratitude to my project guides, Dr. Rahul N. Wadekar and Dr. Prasad Supekar, for their continuous guidance, critical feedback and encouragement throughout the preparation of this report. Their insistence that every claim be supported by a disclosed number has shaped the discipline with which this report has been written.")
    pg.p("I thank Dr. Rasika Mallya, Director, DES’s Navinchandra Mehta Institute of Technology and Development, and all faculty members of the Finance specialisation for providing the academic environment, library resources and database access required for this work. I am also grateful to the Institute’s library staff for help with locating regulatory circulars and rating-agency publications.")
    pg.p("The project would not have been possible without the detailed public disclosures of Fedbank Financial Services Limited. The Corporate Overview, Management Discussion and Analysis, Directors’ Report, Corporate Governance Report, Business Responsibility and Sustainability Report and the audited financial statements for FY 2023–24, FY 2024–25 and FY 2025–26 have been the backbone of this analysis. I acknowledge the company, its Board and its statutory auditors as the source of the data used.")
    pg.p("I thank the Reserve Bank of India, the Securities and Exchange Board of India, the Ministry of Statistics and Programme Implementation and the credit-rating agencies whose publications are cited in the sector chapters. Finally, I thank my family and classmates for their patience and support during the summer internship period.")
    pg.space(0.4)
    pg.p("Dattaguru Kallapa Patil", align="center", bold_lead=None)
    pg.p("Roll No. M-16144  |  MMS (Finance) 2026–27", align="center", italic=True)
    P.append(pg)

    # ------------------------------------------------------------------ 4 Executive Summary
    pg = Page("Executive Summary")
    pg.p("This report presents a fundamental analysis of Fedbank Financial Services Limited (“Fedfina”), a Mumbai-headquartered, NSE/BSE-listed non-banking financial company (NBFC) and a 60.79%-owned subsidiary of The Federal Bank Limited. The study follows the Economy–Industry–Company (E-I-C) approach: it first describes the Indian NBFC sector, the gold-loan and mortgage markets and the regulatory framework; then the organisation, its products and distribution; and finally its five-year financial performance, risk profile and strategic position. The analysis draws on the company’s annual reports for FY 2023–24, FY 2024–25 and FY 2025–26, which together provide a continuous eight-year series for key indicators.")
    pg.kpis([("₹20,153 cr", "AUM, 31 Mar 2026 (+27.5% YoY)"), ("₹343.6 cr", "PAT FY26 (+52.6% YoY)"),
             ("98.9%", "Secured share of AUM"), ("2.4% / 12.6%", "RoA / RoE FY26"),
             ("1.9% / 1.3%", "GNPA / NNPA"), ("0.8%", "Credit cost (FY25: 1.8%)"),
             ("22.4%", "Capital adequacy (Tier I 17.5%)"), ("757", "Branches in 17 states/UTs")], cols=4)
    pg.p(f"Key findings. Fedfina’s AUM has grown from ₹2,019 crore in FY19 to ₹20,153 crore in FY26 and PAT from ₹36 crore to ₹344 crore. Over the five years FY22–FY26 AUM compounded at {cagr(AUM_MN['FY22'], AUM_MN['FY26'], 4):.1f}% and PAT at {cagr(PAT_MN['FY22'], PAT_MN['FY26'], 4):.1f}% (derived). FY25 was a year of reset – profit fell 8% as small-ticket LAP delinquencies forced higher provisioning and the unsecured business-loan book was run down – and FY26 was the year of recovery: net interest income rose 15% to ₹1,230 crore, credit cost fell by 93 basis points, and PAT rose 53%. Gold loans were the growth engine (AUM +76% to ₹10,352 crore, now 51.4% of AUM), the unsecured book was fully assigned, and 148 branches were added.")
    pg.p("Risks. The report identifies leverage (debt-equity 4.6x, up from 4.0x), the maturing of 148 young branches, gold-price sensitivity, the still-stabilising small-ticket LAP book, the April 2026 RBI gold-lending directions, competition from banks (82% of the organised gold-loan market) and cyber/operational risk as the principal watch-points. The company’s AA+/Stable ratings from four agencies, diversified 41-lender funding base, fully hedged USD 250 million ECB programme and conservative 60.9% gold LTV are the main mitigants.")
    pg.p("Conclusion. Fedfina has a credible, now fully secured growth platform with improving earnings quality (direct-assignment income is down to 1.6% of PBT from 21.7%). The sustainability of the recovery depends on keeping credit cost below 1%, converting new-branch capacity into productivity, and preserving capital as leverage rises. The report offers recommendations on growth, risk governance and sustainability and answers four research questions on growth-profitability, risk profile, capitalisation and external risks.")
    P.append(pg)

    # ------------------------------------------------------------------ 5 Table of Contents
    pg = Page("Table of Contents")
    toc = [
        ("Front matter", "Certificate, Declaration, Acknowledgement, Executive Summary, Contents, Lists", "2 – 7"),
        ("Chapter 1", "Introduction and study design: need, objectives, scope, research questions, methodology, data sources, limitations", "8 – 15"),
        ("Chapter 2", "Sector analysis: Indian NBFC sector, macro-economy, gold-loan and mortgage markets, MSME credit gap, regulation, competition, Porter and PESTLE", "16 – 27"),
        ("Chapter 3", "Company analysis: history, parentage and shareholding, vision, business model, Fedfina 2.0, distribution, customers, people, technology, governance, listing and ratings", "28 – 38"),
        ("Chapter 4", "Product analysis: gold loans, medium-ticket LAP, small-ticket LAP and housing loans, exit from unsecured lending, co-lending and direct assignment, product economics", "39 – 46"),
        ("Chapter 5", "Financial analysis: framework, FY25–FY26 snapshot, five-year trends, income statement, costs, balance sheet, funding, capital, asset quality, returns, per-share and valuation", "47 – 60"),
        ("Chapter 6", "Risk analysis: architecture, credit, liquidity/ALM, market, operational and cyber, regulatory and reputational, collections, risk matrix, ESG", "61 – 69"),
        ("Chapter 7", "SWOT, investment case, scenarios, balanced scorecard and recommendations", "70 – 77"),
        ("Chapter 8", "Key findings, hypothesis testing, conclusion, limitations and bibliography", "78 – 82"),
        ("Appendices", "A Balance sheet; B Profit and loss; C Branch network by state; D Debt instruments; E Shareholding; F Glossary and formulae; G Viva preparation; H Checklist and data notes", "83 – 90"),
    ]
    pg.table(["Section", "Contents", "Pages"], [list(t) for t in toc], widths=[1.1, 5.1, 0.85])
    pg.p("Page numbers refer to the printed sequence of this document (cover page = 1). Each section of the report begins on a new page, so the page count of the original submission template (90 pages) has been retained while the content of every page has been expanded with reported data.", italic=True, size=9)
    P.append(pg)

    # ------------------------------------------------------------------ 6 Lists
    pg = Page("List of Tables, Figures and Abbreviations")
    pg.h2("Principal tables")
    pg.table(["No.", "Table", "No.", "Table"],
             [["T1", "Sector datapoints FY26", "T9", "Income statement FY25 vs FY26"],
              ["T2", "RBI gold-lending directions 2025", "T10", "Expense structure and cost ratios"],
              ["T3", "Peer snapshot FY26", "T11", "Balance sheet composition"],
              ["T4", "Corporate journey 1995–2026", "T12", "Borrowing composition and ALM buckets"],
              ["T5", "Fedfina 2.0 commitments vs delivery", "T13", "Capital adequacy FY25–FY26"],
              ["T6", "Product key numbers FY26", "T14", "Stage-wise loans and impaired-loan movement"],
              ["T7", "Directors’ Report highlights FY23–FY26", "T15", "Risk matrix; SWOT; scorecard"],
              ["T8", "Eight-year KPI series FY19–FY26", "T16", "Appendices A–E (statements, branches, NCDs, shareholding)"]],
             widths=[0.5, 3.0, 0.5, 3.0])
    pg.h2("Principal figures")
    pg.p("F1 AUM FY19–FY26; F2 PAT FY19–FY26; F3 product mix FY24–FY26; F4 RoA and RoE; F5 yield, cost of borrowings and spread; F6 GNPA, NNPA and PCR; F7 CRAR and book value; F8 borrowings by instrument; F9 branch network by format; F10 disbursements by product; F11 stage classification; F12 shareholding pattern; F13 top-five-state concentration; F14 expense structure; F15 structural liquidity; F16 revenue, PAT and margin.", size=9)
    pg.h2("Abbreviations")
    pg.table(["Term", "Meaning", "Term", "Meaning"],
             [["AUM", "Assets under management (on-book + co-lent/assigned)", "LTV", "Loan-to-value ratio"],
              ["AUF", "Assets under finance (on-book)", "MT LAP / ST LAP", "Medium- / small-ticket loan against property"],
              ["BRE", "Business rule engine", "NCD / CP", "Non-convertible debenture / commercial paper"],
              ["CRAR", "Capital to risk-weighted assets ratio", "NII / NIM", "Net interest income / net interest margin"],
              ["DA", "Direct assignment (portfolio sell-down)", "NNPA / GNPA", "Net / gross non-performing assets"],
              ["DSGL", "Doorstep gold loan", "PCR", "Provision coverage ratio"],
              ["ECB", "External commercial borrowing", "PPOP", "Pre-provision operating profit"],
              ["ECL", "Expected credit loss (Ind AS 109)", "RoA / RoE", "Return on (average) assets / equity"],
              ["EWS", "Early-warning signal", "SBR", "RBI scale-based regulation for NBFCs"],
              ["HL", "Housing loan", "TAT", "Turnaround time"]],
             widths=[0.9, 2.6, 1.1, 2.4], font=8)
    P.append(pg)

    # ------------------------------------------------------------------ 7 Chapter 1 Introduction
    pg = Page("Chapter 1 — Introduction")
    pg.p("Financial intermediaries channel household savings into productive credit. In India this function is shared between scheduled commercial banks, non-banking financial companies (NBFCs), housing finance companies, small finance banks, co-operative institutions and, increasingly, fintech platforms. NBFCs occupy a distinctive niche: they specialise in customer segments and products that banks have historically served less well – self-employed borrowers with informal incomes, small enterprises without audited accounts, households needing short-tenor liquidity against gold, and property-backed working-capital loans in Tier 2–4 towns.")
    pg.p(f"The sector has become systemically significant. According to the Management Discussion and Analysis in the {AR26}, total NBFC assets stood at approximately ₹{SECTOR['nbfc_assets_tn']} trillion in FY 2025–26, loan books were expanding at 15–17%, and CRISIL expects sector AUM to cross ₹{SECTOR['nbfc_fy27_tn']} trillion in FY 2026–27. Within this, secured retail lending – gold loans and loans against property – has emerged as the preferred growth avenue after the stress seen in unsecured small-ticket personal loans and microfinance during 2024–25.")
    pg.p("Fedbank Financial Services Limited is a useful subject for fundamental analysis for four reasons. First, it is a bank-promoted NBFC (Federal Bank holds 60.79%), so the interaction between institutional parentage and NBFC agility can be studied. Second, it operates a “twin-engine” model – short-tenor gold loans and long-tenor mortgage loans – that allows the analyst to compare two very different secured products inside one balance sheet. Third, it has gone through a complete cycle within the study period: rapid growth and an IPO in FY24, an asset-quality reset in FY25, and a recovery with a strategic pivot to a fully secured book in FY26. Fourth, its disclosures are unusually granular: the annual reports provide eight years of KPIs, product-level disbursements, stage-wise loan data, ALM buckets and borrowing terms.")
    pg.h2("Structure of the report")
    pg.p("Chapter 1 sets out the study design. Chapter 2 analyses the sector (macro-economy, NBFC industry, gold-loan and mortgage markets, regulation, competition, Porter and PESTLE). Chapters 3 and 4 profile the company and its products. Chapter 5 contains the five-year financial analysis (FY22–FY26) with an eight-year view of AUM and PAT. Chapter 6 analyses risk; Chapter 7 presents SWOT, scenarios and recommendations; Chapter 8 summarises findings, tests the hypothesis and lists limitations and references. Appendices reproduce the summarised statements and supporting tables.")
    pg.table(["Company fact (31 March 2026)", "Value", "Company fact (31 March 2026)", "Value"],
             [["Incorporated / RBI registration", "1995 / NBFC-ND, CoR N-16.00187 (Aug 2010)", "Promoter holding", "Federal Bank 60.79%"],
              ["Listing", "NSE & BSE, November 2023 (IPO ₹1,092 crore)", "Market capitalisation", "₹4,642 crore"],
              ["AUM / secured share", "₹20,153 crore / 98.9%", "Employees / branches", "5,303 / 757 in 17 states & UTs"],
              ["PAT / RoA / RoE", "₹343.6 crore / 2.4% / 12.6%", "Credit ratings", "AA+/Stable – CARE, CRISIL, ICRA, India Ratings"]],
             widths=[1.7, 2.0, 1.55, 1.8], font=8, source=f"{AR26}, Key Highlights p.2–3, Directors’ Report, Corporate Governance Report.")
    pg.p("Throughout, amounts are in Indian rupees. The annual reports use lakh (₹1,00,000) in statutory sections and crore (₹1,00,00,000) or million (₹10,00,000) in the corporate overview; this report converts to crore wherever possible and states the unit in every table. Figures computed by the author from reported numbers are labelled “derived”.")
    P.append(pg)

    # ------------------------------------------------------------------ 8 Need of the study
    pg = Page("Need of the Study")
    pg.p("Management education in finance equips students with tools – ratio analysis, trend analysis, DuPont decomposition, industry frameworks – but these tools are normally practised on manufacturing or trading companies. A lender is different. Its “raw material” is borrowed money, its “inventory” is a loan book whose value depends on borrower behaviour, and its profit can be flattered for years by under-provisioning before losses surface. Conventional measures such as operating margin, inventory turnover or current ratio are either meaningless or misleading (the company’s own Key Ratios table marks debtors turnover, inventory turnover, interest coverage and operating margin as “NA”). The study is needed, first, to apply fundamental analysis in the way it must be applied to a financial intermediary.")
    pg.p("Second, the retail-NBFC segment is at an inflection point. The RBI’s scale-based regulation (SBR) framework, the November 2023 increase in risk weights on bank lending to NBFCs, the 2024 restrictions on cash disbursal of gold loans, the June 2025 Directions on lending against gold collateral (effective 1 April 2026) and the Digital Personal Data Protection framework have all changed the operating rules within the three years covered by this study. Understanding how a single company adapted – in pricing, LTV, funding mix and collections – is directly relevant to anyone who will work in or lend to the sector.")
    pg.p("Third, Fedfina’s FY25 experience is a live case study in what goes wrong when collections infrastructure lags growth. The FY25 annual report candidly states that small-mortgage delinquencies rose because “our collection infrastructure had not kept pace with business growth”, and credit cost jumped from 0.7% to 1.8% of average assets. The FY26 report then documents the fix: new leadership, a business rule engine, verticalised collections (in-house team scaled to 1.8x), sale of stressed pools to ARCs and complete exit from unsecured business loans. Few listed companies describe a problem and its remediation so explicitly across consecutive annual reports.")
    pg.table(["Indicator", "FY24", "FY25 (reset)", "FY26 (recovery)"],
             [["PAT (₹ crore)", "244.7", "225.2 (−8%)", "343.6 (+53%)"], ["Credit cost (% of average assets)", "0.7", "1.8", "0.8"],
              ["GNPA / NNPA (%)", "1.7 / 1.3", "2.0 / 1.2", "1.9 / 1.3"], ["RoA / RoE (%)", "2.4 / 13.5", "1.8 / 9.4", "2.4 / 12.6"],
              ["Unsecured business-loan AUM (₹ crore)", "≈ 2,000 (16% of AUM)", "1,656", "nil on book (assigned ₹886 crore)"]],
             widths=[2.6, 1.3, 1.5, 1.65], source=f"{AR24} p.20–23; {AR25} p.3, 18–21; {AR26} p.2–3, 18–21. FY24 business-loan AUM derived from 16.4% residual of product mix.")
    pg.p("Fourth, investors, lenders and rating agencies need a framework to separate the structural from the cyclical. Gold-loan growth of 76% in FY26 occurred while international gold prices rose about 65% during calendar 2025. How much of the growth is tonnage (gold under custody grew 12% to 12.6 tonnes) and how much is price? How dependent is profit on direct-assignment income (which fell from 21.7% of PBT to 1.6%)? Is a 22.4% capital adequacy ratio sufficient when debt-equity has risen to 4.6x? These are the kinds of questions a fundamental analyst must ask, and the study is designed to answer them with reported data.")
    pg.p("Finally, the study is needed for the student’s own development: it bridges the classroom and the market, builds the habit of reading a 180-page annual report critically, and produces a reference document that can be defended in a viva voce examination with page-level evidence.")
    P.append(pg)

    # ------------------------------------------------------------------ 9 Objectives
    pg = Page("Objectives of the Study")
    pg.p("The overall aim of the project is to evaluate the fundamental strength and sustainability of Fedbank Financial Services Limited as a secured retail lender, using a structured Economy–Industry–Company approach. The specific objectives are:")
    pg.bullets([
        "Sector understanding:: To describe the structure, size, growth drivers, asset-quality trends and regulatory framework of the Indian NBFC sector, with particular reference to the organised gold-loan market (which crossed ₹15 lakh crore in FY26) and the loan-against-property and affordable-housing segments.",
        "Company understanding:: To document Fedfina’s history since 1995, its ownership and relationship with Federal Bank, its vision and values, the “twin-engine” business model, the Fedfina 2.0 transformation programme, distribution footprint (757 branches), human capital (5,303 employees), technology stack and governance structure.",
        "Product analysis:: To analyse each product – gold loans, medium-ticket LAP, small-ticket LAP and housing loans, and the discontinued unsecured business loans – in terms of AUM, disbursements, ticket size, yield, collateral cover, customer profile and risk controls, and to assess the role of co-lending and direct assignment.",
        "Five-year financial analysis:: To examine trends in AUM, disbursements, revenue, net interest income, operating costs, credit cost, PAT, RoA, RoE, EPS, book value, yield, cost of borrowings, spread, cost-to-income, GNPA, NNPA, provision coverage, CRAR and leverage for FY22–FY26, supported by the longer eight-year series for AUM and PAT.",
        "Statement interpretation:: To interpret the FY 2025–26 statement of profit and loss and balance sheet through common-size analysis, ratio analysis, DuPont decomposition and comparison with FY 2024–25.",
        "Risk assessment:: To identify and evaluate credit, liquidity, market (gold price, interest rate, currency), operational, fraud, cyber, regulatory, compliance and reputational risks, and the mitigants disclosed by the company.",
        "Strategic evaluation:: To prepare SWOT, Porter’s Five Forces, PESTLE and balanced-scorecard assessments, a peer comparison, scenario analysis and an evidence-based investment case.",
        "Recommendations:: To draw practical conclusions and recommendations for management, investors, lenders and students, and to answer the research questions and test the working hypothesis stated in this chapter.",
    ])
    pg.table(["Objective", "Chapter", "Principal metrics / tools"],
             [["1 Sector", "2", "Sector size and growth, gold-loan and LAP market data, RBI directions, Porter, PESTLE"],
              ["2 Company; 3 Products", "3, 4", "Milestones, shareholding, branch and employee data, product AUM/disbursement/ticket/yield, LTV, CIBIL mix"],
              ["4 Trends; 5 Statements", "5", "Eight-year KPI series, growth and CAGR, common-size P&L and balance sheet, DuPont, funding and ALM tables"],
              ["6 Risk", "6", "Credit, liquidity, market, operational, regulatory risk; risk matrix; ESG indicators"],
              ["7 Strategy; 8 Recommendations", "7, 8", "SWOT, scenarios, balanced scorecard, peer snapshot, hypothesis test, recommendations"]],
             widths=[1.9, 0.8, 4.35])
    P.append(pg)

    # ------------------------------------------------------------------ 10 Scope
    pg = Page("Scope of the Study")
    pg.p("Entity. The study covers Fedbank Financial Services Limited on a standalone basis. The company has no subsidiaries (Corporate Governance Report, FY26), so standalone and consolidated figures are identical. Federal Bank is discussed only as parent, lender and promoter; the bank’s own financials are outside scope.")
    pg.p("Period. The reference year is the financial year ended 31 March 2026. Five-year trend analysis covers FY 2021–22 to FY 2025–26, and the eight-year series for AUM, PAT, RoA, RoE, GNPA, NNPA, CRAR, book value and provision coverage (FY 2018–19 to FY 2025–26) is reproduced from the FY24, FY25 and FY26 annual reports. Statement-level analysis (income statement, balance sheet, notes) compares FY26 with FY25, with Directors’ Report highlights extending back to FY23. Events after the date of the FY26 annual report (dated 25 August 2026 for the Directors’ Report; AGM 29 September 2026) are not covered.")
    pg.p("Content. The scope includes: sector and macro context; business profile and strategy; product-level performance; distribution, technology and people; income statement, balance sheet, funding, capital, asset quality and returns; risk management; ESG and governance; SWOT, Porter, PESTLE and scorecard; peer snapshot; valuation perspective; and recommendations.")
    pg.table(["In scope", "Out of scope"],
             [["Published annual reports FY24, FY25, FY26 (all sections)", "Management interviews, branch visits, borrower surveys"],
              ["RBI directions and press releases cited in the reports", "Proprietary databases (e.g., bureau data, Bloomberg terminals)"],
              ["Publicly reported FY26 results of two listed gold-loan peers", "Detailed peer financial-statement analysis"],
              ["Market capitalisation as disclosed in the annual report (31 Mar 2026)", "Share-price history, technical analysis, target price"],
              ["Ratio and trend analysis; derived metrics computed from disclosed numbers", "Independent audit, re-performance or verification of reported figures"],
              ["Qualitative risk assessment based on disclosures", "Credit rating opinion or regulatory compliance opinion"]],
             widths=[3.5, 3.5])
    pg.p("Units and conventions. Statutory tables in the annual reports are in ₹ lakh; the corporate overview uses ₹ crore and ₹ million. This report standardises on ₹ crore (1 crore = 100 lakh = 10 million) except where a table reproduces a statutory schedule in lakh, in which case the unit is stated in the table header. Percentages are as reported by the company; derived ratios show the formula used. Rounding differences of ±0.1 may occur.")
    pg.p("Depth of coverage. The reference year is analysed at the level of individual notes to accounts (interest-income split, finance-cost split, impairment split, borrowing schedules, stage-wise loans, ALM buckets, capital computation). Earlier years are analysed at the level of the Directors’ Report highlights and the KPI series in the corporate overview, which is the depth the public record supports consistently across all five years.")
    pg.p("Disclaimer. The report is an academic exercise. It is not investment advice, an audit, a credit rating or a fairness opinion, and nothing in it should be relied upon for any financial decision.")
    P.append(pg)

    # ------------------------------------------------------------------ 11 RQs
    pg = Page("Research Questions and Hypotheses")
    pg.p("The analysis is organised around four research questions (RQs) and one working hypothesis. Each question is answered in Chapter 8 (“Hypothesis Testing and Answers to Research Questions”) with reference to the evidence assembled in Chapters 2–7.")
    pg.table(["RQ", "Question", "Principal evidence used", "Chapter"],
             [["RQ1", "Has Fedfina’s growth been accompanied by improved profitability, or has growth been bought at the expense of returns?",
               "AUM, PAT, NII, PPOP, RoA, RoE, EPS, cost-to-income, credit cost, DA income share, FY19–FY26", "5"],
              ["RQ2", "Has the change in product mix and portfolio security strengthened the risk profile of the loan book?",
               "Secured share of AUM, GNPA/NNPA, stage-wise loans, PCR, LTV, CIBIL distribution, write-offs, ARC sales", "4, 5, 6"],
              ["RQ3", "Is the company adequately capitalised and funded for the growth “targeted at 20 to 25% on a sustainable basis” (Chairman’s message, FY26)?",
               "CRAR (Tier I/II), debt-equity, borrowing mix, lender count, ECB/CP programmes, ALM buckets, ratings", "5, 6"],
              ["RQ4", "What operational, regulatory and external risks could challenge the growth plan, and how well are they mitigated?",
               "Risk matrix, RBI gold-loan directions 2025, competition, cyber disclosures, branch vintage, gold price", "2, 6, 7"]],
             widths=[0.5, 2.7, 3.1, 0.7], font=8.5)
    pg.h2("Working hypothesis")
    pg.p("H1: A higher secured share of AUM combined with stronger operating discipline (system-driven underwriting and in-house collections) supports sustainable profitability, subject to asset-quality and funding-cost control.", bold_lead=None)
    pg.p("H0 (null): The FY26 improvement in profitability is primarily cyclical – driven by rising gold prices and falling interest rates – rather than structural, and would reverse if these tailwinds faded.")
    pg.h2("How the hypothesis will be tested")
    pg.bullets([
        "Decompose FY26 profit growth into volume (AUM, NII), margin (yield, cost of borrowings, spread), efficiency (cost-to-income) and credit-cost effects using the reported income statement.",
        "Separate price and tonnage effects in gold-loan growth using gold-under-custody data (12.6 tonnes, +12%) against gold AUM (+76%).",
        "Compare the quality of earnings in FY26 with FY25 and FY24 using the share of direct-assignment income in PBT and the share of interest on loans in interest income.",
        "Assess whether asset-quality indicators improved on both a reported (GNPA/NNPA) and a stage-wise (Ind AS 109) basis, and whether improvement came from write-offs/ARC sales or from lower fresh slippage.",
        "Evaluate the funding structure’s resilience to a 100 bps rise in borrowing costs using the fixed-rate share (40%) and ALM data.",
    ])
    pg.p("The hypothesis is accepted if the evidence shows that (a) core NII growth exceeded total revenue growth, (b) credit cost fell on a like-for-like basis, (c) the stage 2 + stage 3 share of loans declined, and (d) returns improved without a disproportionate rise in leverage; otherwise it is rejected or accepted with qualifications.")
    P.append(pg)

    # ------------------------------------------------------------------ 12 Methodology
    pg = Page("Research Methodology")
    pg.p("Research design. The study is descriptive and analytical. It is descriptive in documenting the sector, the company and its products from published sources, and analytical in applying ratio analysis, trend analysis, common-size analysis, DuPont decomposition and qualitative strategic frameworks to interpret those facts. It is a single-company longitudinal case study supplemented by a peer snapshot.")
    pg.p("Type of data. Only secondary data has been used. The primary documents are the three annual reports of Fedbank Financial Services Limited (FY 2023–24, 256 pages; FY 2024–25, 155 pages; FY 2025–26, 182 pages), each comprising the Corporate Overview, Management Discussion and Analysis, Directors’ Report with annexures, Report on Corporate Governance, Business Responsibility and Sustainability Report, auditor’s report and audited Ind AS financial statements with notes. Sector data are taken from the sources the company itself cites (MoSPI, PIB, RBI, World Gold Council, ICRA, CRISIL, Economic Survey) and from RBI directions. Peer figures are taken from the FY26 results of Muthoot Finance and Manappuram Finance as reported in May 2026.")
    pg.h2("Analytical procedure")
    pg.table(["Step", "Activity", "Output"],
             [["1", "Define objectives and research questions; agree the page structure with the guide", "Chapter 1"],
              ["2", "Read all three annual reports; extract every quantitative disclosure into a data sheet with page references", "Data layer (Appendix H)"],
              ["3", "Reconcile the multi-year KPI charts across the three reports (the FY26 report presents yield, spread and cost of borrowings on a revised basis)", "Eight-year series, Table T8"],
              ["4", "Standardise units (lakh → crore) and compute derived metrics: growth rates, CAGR, common-size percentages, DuPont components, ALM gaps, borrowing shares", "Chapter 5 tables"],
              ["5", "Compare FY26 with FY25 line-by-line (income statement, balance sheet, notes 8, 16–18, 26–34, 48)", "Chapters 5 and 6"],
              ["6", "Interpret trends in the context of sector data and regulation; apply Porter, PESTLE, SWOT, balanced scorecard and scenario frameworks", "Chapters 2, 6, 7"],
              ["7", "Answer research questions, test hypothesis, formulate recommendations, document limitations", "Chapter 8"]],
             widths=[0.5, 4.8, 1.75])
    pg.h2("Tools and techniques")
    pg.p("Ratio analysis (profitability, efficiency, leverage, liquidity, asset quality, capital); horizontal (trend) analysis with year-on-year growth and compound annual growth rates; vertical (common-size) analysis of the income statement relative to total revenue and average assets; DuPont decomposition of RoE into margin, asset turnover and leverage; structural-liquidity gap analysis using RBI ALM buckets; and the qualitative frameworks named above. Charts were prepared from the extracted data; every chart and table carries a source line.")
    pg.p("Verification. Reported totals were cross-checked for internal consistency (e.g., balance-sheet totals, borrowing sub-totals against notes, cost-to-income recomputed from the income statement, debt-equity recomputed from borrowings and net worth). Where the company’s own sections differ (for instance GNPA of 1.9% in the Key Highlights versus 2.2% in the FY26 five-year chart), both figures are shown and the difference is flagged rather than resolved by assumption.")
    P.append(pg)

    # ------------------------------------------------------------------ 13 Data sources
    pg = Page("Data Sources and Reliability")
    pg.table(["Source", "Sections used", "Reliability and treatment"],
             [[AR26 + " (182 pp.)", "Key highlights; offerings; investment case; Chairman and MD&CEO messages; financial highlights; operating environment; technology, marketing and ESG; MD&A; Directors’ Report; Corporate Governance Report; BRSR; audited financial statements with notes 8, 16–18, 26–34 and 48",
               "Audited (KKC & Associates LLP, unmodified opinion). Primary source for all FY26 and FY25 figures."],
              [AR25 + " (155 pp.)", "Measuring our progress p.3; branch expansion p.7; Chairman and MD&CEO letters p.8–15; momentum in metrics p.18–21; Directors’ Report p.64–",
               "Audited. Source for FY25 narrative (ST LAP stress, business-loan slowdown), FY25 product mix and FY21–FY25 KPI charts."],
              [AR24 + " (256 pp.)", "Company overview p.4–9; Chairman p.10–13; MD&CEO p.14–17; KPIs p.20–23; MD&A p.46–; Directors’ Report p.64–",
               "Audited. Source for FY19–FY24 KPI series, IPO details, FY24 product data and corporate milestones."],
              ["RBI – Directions on Lending Against Gold Collateral (June 2025), SBR Directions 2025, Digital Lending Guidelines, Co-lending guidelines", "Regulatory provisions summarised in Chapter 2",
               "Official regulations; summarised from the directions and an EY impact note (Feb 2026)."],
              ["Sector statistics cited in the FY26 MD&A: MoSPI, PIB, World Economic Outlook (Apr 2026), World Gold Council, ICRA, CRISIL, Ministry of MSME, Economic Survey 2025–26", "Macro and industry numbers in Chapter 2",
               "Reproduced as quoted by the company with its citations; not independently re-sourced."],
              ["Peer FY26 results (Muthoot Finance, Manappuram Finance) as reported in results coverage dated May 2026", "Peer snapshot, Chapter 2",
               "Secondary press/analyst coverage of exchange filings; used for order-of-magnitude comparison only."]],
             widths=[1.7, 3.2, 2.15], font=8)
    pg.h2("Reliability considerations")
    pg.p("The annual reports are statutory documents approved by the Board and audited; the financial statements carry an unmodified audit opinion and the Directors’ Report confirms no qualifications by statutory or secretarial auditors for FY26. Corporate-overview sections are unaudited management presentations and occasionally round or re-base figures; where they differ from audited numbers, the audited number is preferred and the difference is noted. Sector data quoted in the MD&A are the company’s selection of third-party statistics; they are used as context rather than as findings of this study.")
    pg.p("A particular reliability issue was the five-year KPI charts in the FY26 report, whose values were reconciled year-by-year against the FY24 and FY25 reports and the Directors’ Report tables; the reconciled series is used throughout. Any item that could not be reconciled is reported as “not available” rather than estimated.")
    P.append(pg)

    # ------------------------------------------------------------------ 14 Limitations of methodology
    pg = Page("Limitations of Methodology")
    pg.p("Every research design has boundaries. The following limitations of method should be kept in mind when reading the findings; the limitations of the study as a whole are discussed separately in Chapter 8.")
    pg.bullets([
        "Dependence on company presentation:: The analysis relies on the definitions, classifications and rounding adopted by the company. For example, “AUM” includes co-lent and assigned portfolios (12.1% of AUM was off-book at 31 March 2026), while the balance-sheet “Loans” line shows only on-book assets; the two cannot be fully bridged from public data.",
        "Changing bases across reports:: The FY26 report re-states yield, spread and cost of borrowings for earlier years on a basis different from the FY24 and FY25 reports (e.g., FY24 yield 16.7% in the FY26 report versus 16.2% in the FY24 report). This report uses the FY26 basis for five-year trends and discloses the earlier figures in Table T8 for transparency.",
        "Ratios not meaningful for a lender:: Inventory turnover, debtors turnover, operating margin and interest coverage are marked “NA” by the company and are not computed here. Conversely, lender-specific ratios (NIM, credit cost, PCR) follow the company’s methodology, which may differ from peers.",
        "Average-balance effects:: Reported RoA (2.44%) uses the company’s average-asset methodology; a simple average of opening and closing total assets gives a slightly lower figure (about 2.3%). Where this report derives a ratio, it uses opening/closing averages and says so.",
        "Single-company, secondary-data design:: There are no interviews, site visits or borrower data. Judgements about execution quality (e.g., branch productivity ramp-up) rest on disclosed indicators such as gold AUM per branch rather than on primary observation.",
        "Peer comparison is a snapshot:: Peer figures are drawn from results coverage for FY26 and differ in basis (standalone vs consolidated, gold-only vs diversified). They indicate relative scale, not relative quality.",
        "No market-price analysis:: The report uses only the market capitalisation disclosed in the annual report (₹4,642 crore at 31 March 2026). Price multiples derived from it are illustrative and dated.",
        "Forward-looking statements:: Management targets (e.g., 20–25% sustainable growth, sub-1% credit cost, gold tonnage CAGR of 10–12%) are reproduced as stated and are not independently assessed for achievability.",
        "Time boundary:: The FY26 financial statements were approved on 28 April 2026 and the Directors’ Report is dated 25 August 2026 (AGM 29 September 2026). Regulatory, market or company developments after those dates are not reflected.",
    ])
    pg.p("How the limitations were managed. Restated prior-year ratios are shown alongside the earlier-basis figures (Table T8) with the basis named in every source line; where a report contains two values for the same metric both are given with their location and the likely reason; missing data points are marked ‘n.a.’ rather than interpolated; every author-computed figure is labelled ‘derived’ with its formula in Appendix F; peer data are used for scale context only; and valuation multiples are presented as at 31 March 2026 only.")
    pg.p("Despite these constraints, the methodology is adequate for the objectives: the questions concern multi-year trends, structural shifts in product mix and funding, and the consistency of management’s stated strategy with reported outcomes – all of which can be assessed rigorously from audited public disclosures.")
    P.append(pg)

    # ================================================================== CHAPTER 2 SECTOR
    # ------------------------------------------------------------------ 15
    pg = Page("Chapter 2 — The Indian NBFC Sector: Structure and Role")
    pg.p("Non-banking financial companies are companies registered under the Companies Act and regulated by the Reserve Bank of India that carry on the business of lending, investment, leasing or hire-purchase without holding a banking licence. Unlike banks they cannot offer demand deposits or participate in the payment system, and most – including Fedfina, which is registered as a non-deposit-taking NBFC (RBI Certificate of Registration N-16.00187, August 2010) – cannot accept public deposits at all. They fund themselves from bank loans, bonds, commercial paper, securitisation/direct assignment, external commercial borrowings and equity.")
    pg.p("The sector complements banks in three ways. It reaches customer segments that are costly for banks to serve through branch networks in Tier 2–4 towns and doorstep models; it specialises in products requiring non-standard underwriting (cash-flow assessment of informal incomes, gold appraisal, used-vehicle valuation); and it provides last-mile distribution for banks through co-lending and portfolio assignment. The FY26 MD&A notes that MSME and retail assets account for nearly 60–65% of NBFC loan books (ICRA).")
    pg.h2("Scale-based regulation")
    pg.p("Since October 2022 the RBI has classified NBFCs into four layers – Base, Middle, Upper and Top – with progressively tighter capital, governance, liquidity and disclosure requirements. Fedfina is categorised in the Middle Layer under the Reserve Bank of India (NBFC – Registration, Exemptions and Framework for Scale Based Regulation) Directions, 2025 (Directors’ Report, FY26). Middle-layer NBFCs must maintain a minimum CRAR of 15%, follow Ind AS with RBI prudential floors on provisioning, maintain a liquidity coverage ratio, operate board-level risk, audit and IT strategy committees, and – from FY27 for NBFCs with assets above ₹15,000 crore – appoint joint statutory auditors (Fedfina has proposed V. Sankar Aiyar & Co. as joint auditor from the 31st AGM).")
    pg.table(["Sector datapoint (as cited in the FY26 MD&A)", "Value", "Source quoted by the company"],
             [["Total NBFC sector assets, FY 2025–26", f"≈ ₹{SECTOR['nbfc_assets_tn']} trillion", "Industry rankings / press"],
              ["NBFC loan-book growth through FY 2025–26", SECTOR["nbfc_growth"], "Press reports"],
              ["Projected NBFC AUM by FY 2026–27", f"> ₹{SECTOR['nbfc_fy27_tn']} trillion (mid-teens growth)", "CRISIL"],
              ["Share of MSME + retail in NBFC loan books", "≈ 60–65%", "ICRA"],
              ["Retail credit growth, FY 2025–26", f"{SECTOR['retail_credit_growth']}%", "RBI / PIB"],
              ["India retail credit market size", f"≈ ₹{SECTOR['retail_credit_tn']} trillion, ~15% CAGR", "MD&CEO statement"],
              ["Household credit to GDP: India vs China / US / UK", f"{SECTOR['household_credit_gdp']}% vs {SECTOR['china']}% / {SECTOR['us']}% / {SECTOR['uk']}%", "Chairman’s message"],
              ["Bank credit to GDP, India", f"≈ {SECTOR['bank_credit_gdp']}%", "MD&CEO statement"]],
             widths=[3.3, 2.0, 1.75], source=f"{AR26}, MD&A p.58–59, Chairman’s message p.16, MD&CEO statement p.18.")
    pg.p("Two features of the recent cycle are important for this study. First, asset-quality stress emerged in FY25 in unsecured small-ticket personal loans, fintech-sourced credit and microfinance, pushing lenders towards secured products – precisely Fedfina’s positioning. Second, the November 2023 increase in risk weights on bank lending to NBFCs raised the sector’s funding cost (Fedfina’s own cost of borrowings rose about 40 bps in FY25 for this reason, per the FY25 MD&CEO letter) and encouraged diversification into bonds, CP and ECBs – a shift visible in Fedfina’s FY26 borrowing mix.")
    P.append(pg)

    # ------------------------------------------------------------------ 16 Macro
    pg = Page("Macro-Economic Environment FY2025-26")
    pg.p("The macro backdrop in the reference year was unusually favourable for retail and MSME lenders. The FY26 MD&A, citing MoSPI’s first advance estimates, records real GDP growth of 7.7% in FY 2025–26 (FY25: 7.1%; FY24: 7.2%), with gross fixed capital formation up 7.8% on public infrastructure spending and a gradual revival in private capex. Household consumption held up on easing inflation, improving income visibility and stable employment. The outlook for FY 2026–27 is 6.6%–7.2%, consistent with India’s potential growth rate.")
    pg.table(["Indicator", "FY 2023–24", "FY 2024–25", "FY 2025–26", "Comment"],
             [["Real GDP growth (%)", "7.2", "7.1", "7.7 (E)", "MoSPI provisional/advance estimates"],
              ["Headline CPI inflation", "5.4% (avg)", "–", "≈1.7% Apr–Dec 2025; ≈2.1% FY avg", "Multi-year low, below RBI 4% target"],
              ["Repo rate", "6.50%", "6.25% (Feb-25 cut)", "5.25% after cumulative 125 bps cuts", "RBI neutral stance in April 2026"],
              ["Gold price (USD/oz, calendar year)", "–", "2,607 (end-2024)", "4,315 (end-2025), +65%", "Economic Survey 2025–26"],
              ["Global GDP growth (CY)", "–", "3.4 (CY25)", "3.1 (CY26 proj.)", "IMF WEO April 2026"],
              ["India gold imports (USD bn)", "–", "57.9", "72.4 (+24%)", "Ministry of Commerce / DGCI&S"]],
             widths=[1.7, 1.0, 1.3, 1.75, 1.3], font=8,
             source=f"{AR26}, MD&A p.54–57; {AR24} Chairman’s message (FY24 GDP and CPI).")
    pg.h2("Interest rates and liquidity")
    pg.p("The RBI cut the repo rate by a cumulative 125 basis points over roughly 14 months to 5.25% and injected durable liquidity, before pausing with a neutral “wait and watch” stance in April 2026 amid geopolitical risk and volatile crude prices. For an NBFC with 60% floating-rate borrowings, falling policy rates reduce the cost of funds with a lag; Fedfina’s daily-average cost of borrowing fell from 8.72% in Q4 FY25 to 7.83% in Q4 FY26. At the same time, lower rates improve borrower affordability and eligibility for mortgage products. The company responded by raising the fixed-rate share of borrowings from about 10% to 40% as a hedge against a future reversal.")
    pg.h2("Rural and semi-urban demand")
    pg.p("A stable monsoon, improved agricultural activity and sustained infrastructure spending strengthened rural and semi-urban incomes, lifting demand for formal credit among first-time borrowers, self-employed individuals and small businesses in underserved geographies. This is the customer base of both gold loans (household liquidity) and small-ticket LAP (working capital), and it is where Fedfina added most of its 148 new branches.")
    pg.h2("Gold prices and the collateral effect")
    pg.p("Gold prices rose approximately 65% during calendar 2025 (USD 2,607 to USD 4,315 per ounce) on a weaker dollar, expectations of negative real rates and geopolitical hedging; investment demand exceeded 40% of Indian gold consumption even as jewellery volumes fell 11% to about 711 tonnes (World Gold Council). Higher prices raise the loan amount available against the same jewellery and reduce LTV on existing loans, improving collateral cover – but they also increase the sensitivity of the book to a price correction. Chapter 6 analyses this risk; Chapter 4 separates tonnage from price in Fedfina’s gold-loan growth.")
    P.append(pg)

    # ------------------------------------------------------------------ 17 NBFC size/growth/asset quality
    pg = Page("NBFC Sector Size, Growth and Asset-Quality Trends")
    pg.p("The NBFC sector has roughly doubled in size over the last five years. The FY24 MD&A (citing KPMG) projected NBFC credit AUM to grow 12–14% a year to reach ₹42 trillion by FY 2024–25, with NBFCs holding a rising share of total credit; the FY26 MD&A puts total sector assets at about ₹45 trillion with loan books growing 15–17% in FY26 and CRISIL projecting AUM above ₹50 trillion in FY27. NBFCs have consistently outpaced bank credit growth by relying on niche lending strategies, digital distribution and deeper penetration of underserved markets.")
    pg.h2("Growth drivers identified by the industry")
    pg.bullets([
        "Retail credit expansion:: RBI data cited in the FY26 MD&A show retail credit growing 19.8% in FY26, driven by housing loans, surging gold-backed loans, digitisation of lending and rising consumption among the urban middle class.",
        "Digital public infrastructure:: Aadhaar e-KYC, UPI, the Account Aggregator framework, GST data and bureau coverage lower acquisition and underwriting costs and allow cash-flow-based assessment of thin-file borrowers.",
        "MSME formalisation:: 7.9 crore registrations on the Udyam portal and Udyam Assist Platform (July 2020 – March 2026) create documented, bankable small businesses.",
        "Shift to secured lending:: Stress in unsecured personal loans and credit cards has pushed lenders towards gold loans and LAP, which offer physical collateral, shorter tenors (gold) and lower loss-given-default.",
    ])
    pg.h2("Asset-quality and funding trends")
    pg.p("Sector asset quality improved steadily from the pandemic peak until FY24, then deteriorated in specific pockets – small-ticket personal loans, fintech partnerships and microfinance – during FY25 and FY26. The FY26 MD&A observes that rapid expansion in these segments “heightened vulnerability to delinquencies”. Secured lenders were comparatively insulated: Fedfina’s own GNPA ranged between 1.7% and 2.2% across FY22–FY26 and its credit cost peaked at 1.8% in FY25 before falling to 0.8%. Funding costs rose across the sector in FY24–FY25 after the RBI increased risk weights on bank exposures to NBFCs, prompting diversification into NCDs, CP and ECBs; the subsequent repo-rate cuts in FY26 have eased costs. The FY25 MD&CEO letter expected industry growth to moderate towards 13–15% over FY 2026–27 to FY 2027–28 as the cycle matures, “necessitating sharper risk selection, disciplined origination and calibrated expansion”.")
    pg.h2("Regulatory direction of travel")
    pg.p("The RBI’s SBR framework has progressively strengthened prudential norms, risk management and supervisory oversight, and recent clarifications extend regulatory purview to smaller non-deposit-taking NBFCs. Governance Directions 2025, KYC Directions 2025, the Internal Ombudsman Directions 2026, the Fraud Risk Management Master Direction 2024 and the IT Governance Master Direction – all listed in Fedfina’s FY26 secretarial audit report – show how comprehensive the compliance perimeter has become. The practical implication for analysis is that compliance capability is now a core competitive asset, not a back-office function.")
    pg.p("Implication for Fedfina. The company is positioned in the two fastest-growing secured segments, is rated AA+ (which protects funding access when the sector is under pressure), and has a bank parent that is itself a lender (₹1,064 crore term loan outstanding) – advantages that should let it grow with the sector while avoiding the unsecured-credit stress that hurt many peers.")
    P.append(pg)

    # ------------------------------------------------------------------ 18 Gold loan industry
    pg = Page("Gold Loan Industry Landscape")
    pg.p("India’s households hold an estimated 25,000 tonnes of gold – the largest private stock in the world (FY26 MD&CEO statement; the FY24 MD&A cited 24,000 tonnes with only about 5,300 tonnes pledged). Lending against this stock has been migrating from the informal sector (money-lenders and pawnbrokers) to banks and specialised NBFCs; the FY24 MD&A put the value of gold-loan advances in India at ₹7,150 billion as of December 2023. The FY26 MD&A, citing ICRA, states that the organised gold-loan market crossed ₹15 lakh crore in FY 2025–26 – a year ahead of earlier projections – and is expected to reach nearly ₹18 lakh crore by FY 2026–27.")
    pg.table(["Gold-loan market indicator", "Value", "Source (as cited in FY26 MD&A)"],
             [["Organised gold-loan market, FY26", "> ₹15 lakh crore", "ICRA"],
              ["Projected market, FY27", "≈ ₹18 lakh crore", "ICRA"],
              ["Banks’ share of organised gold loans", "≈ 82%", "ICRA"],
              ["NBFC share of gold-loan market, March 2021", "22% (moderated since)", "ICRA"],
              ["Top-4 NBFCs’ share of NBFC gold-loan AUM", "81% (Mar 2025) vs 90% (Mar 2022)", "ICRA"],
              ["India gold demand, CY2025", "≈ 711 tonnes (−11% by volume; value up)", "World Gold Council"],
              ["Gold price, CY2025", "USD 2,607 → 4,315/oz (+65%)", "Economic Survey 2025–26"],
              ["Household gold holdings", "≈ 25,000 tonnes", "MD&CEO statement"]],
             widths=[3.0, 2.3, 1.75], source=f"{AR26}, MD&A p.56–57 and p.60; MD&CEO statement p.18.")
    pg.h2("Structure and competition")
    pg.p("Banks dominate by value (about 82%) because agricultural gold loans qualify as priority-sector lending and banks have the lowest cost of funds. Specialised NBFCs – led by Muthoot Finance and Manappuram Finance, with IIFL Finance and several smaller players – compete on speed (loans in under 30 minutes), branch density in semi-urban markets, doorstep service and flexible repayment. Concentration within the NBFC segment is easing: the top four held 81% of NBFC gold AUM in March 2025 versus 90% in March 2022, indicating that mid-sized entrants such as Fedfina (gold AUM ₹10,352 crore, 12.6 tonnes under custody) are gaining share.")
    pg.h2("Growth drivers and economics")
    pg.p("The FY26 report lists six drivers: higher gold prices (larger eligible loans), borrower migration from unsecured to secured credit, improved funding conditions and supportive RBI measures, strong rural demand, gold’s liquidity and ease of valuation (which makes the product operationally scalable), and co-lending partnerships that extend NBFC reach. Economically, gold loans are short-tenor (typically 6–12 months), high-yield, low-credit-loss products: Fedfina’s average ticket is ₹2.7 lakh, its portfolio LTV is 60.9% and its gold-loan branches generate ₹16.5 crore of AUM each. The main risks are a sharp price fall, custody/purity fraud and conduct issues around auctions – all addressed by the 2025 RBI directions discussed on page 21.")
    pg.p("Regulatory stability is itself a growth driver: clear norms on LTV, auctions and provisioning have reduced uncertainty and encouraged lenders to expand gold portfolios confidently, while the shift to secured lending after unsecured stress has made gold loans attractive to banks and NBFCs alike.")
    P.append(pg)

    # ------------------------------------------------------------------ 19 Mortgage/LAP
    pg = Page("Mortgage, Housing Finance and LAP Landscape")
    pg.p("India’s mortgage market – individual housing loans plus loans against property – has deepened steadily over the past decade. The Economic Survey 2025–26, cited in the FY26 MD&A, shows housing loans rising to about 11% of GDP in FY 2024–25 from 8% in FY 2014–15, and outstanding individual housing loans more than tripling to approximately ₹37 lakh crore by March 2025 from about ₹10 lakh crore a decade earlier. Even so, penetration remains low by international standards, and demand is shifting towards affordable, mid-income and Tier 2–3 markets.")
    pg.h2("Loan against property as an MSME product")
    pg.p("LAP has become a key pillar of secured MSME finance. The secured MSME-LAP portfolio is projected to grow 16–18% a year over FY 2024–25 to FY 2027–28 (FY26 MD&A), supported by rising MSME financing needs, appreciation in property values and borrower preference for secured loans that carry lower rates than unsecured business loans. Two sub-segments exist. Medium-ticket LAP (Fedfina average ticket ₹72.4 lakh) serves established traders, wholesalers, distributors and small manufacturers with documented cash flows, and is contested by banks and large NBFCs on price. Small-ticket LAP (average ticket ₹16.1 lakh) serves self-employed borrowers with median annual incomes of around ₹5 lakh and limited documentation, assessed on household cash flows; it is a higher-yield (Fedfina origination yield 15.1%), operationally intensive product dominated by affordable-housing finance companies and specialised NBFCs.")
    pg.table(["Segment", "Typical customer", "Ticket / yield (Fedfina FY26)", "Main competitors", "Key risk"],
             [["Medium-ticket LAP", "Established MSMEs with formal income records", "₹72.4 lakh; 12.0% origination yield", "Private banks, large NBFCs/HFCs", "Yield pressure; balance-transfer attrition"],
              ["Small-ticket LAP", "Self-employed, informal income, Tier 2–4 towns", "₹16.1 lakh; 15.1% origination yield", "Affordable HFCs, Five-Star-type NBFCs", "Collections intensity; early delinquency"],
              ["Affordable housing loan", "First-time buyers in non-metro markets", "Bundled with ST LAP (₹3,792 cr AUM)", "HFCs, SFBs, PSU banks", "Construction/title risk; long duration"]],
             widths=[1.2, 1.7, 1.6, 1.45, 1.1], font=8, source=f"{AR26} MD&A p.60–61 and p.64–65; {AR24} MD&A p.58.")
    pg.h2("Growth drivers")
    pg.p("The FY26 report identifies six: an easing interest-rate cycle improving affordability and refinancing; mortgage payments becoming competitive with rents in several markets; digital mortgage transformation (automated underwriting, AI-based scoring, digital documentation) cutting approval times; expansion of non-traditional segments (self-employed and gig-economy borrowers); policy support (tax benefits, affordable-housing schemes); and demographics – a growing population in the 25–40 prime home-buying age group.")
    pg.h2("Implications")
    pg.p("For Fedfina the mortgage business (₹9,362 crore AUM, 46.5% of total) provides duration and stable yields that complement the short-tenor gold book. Its FY25 experience showed that small-ticket LAP cannot be scaled faster than the collections machinery that supports it; its FY26 rebuild – business rule engine, higher CIBIL thresholds, 82.2% of mortgage AUM backed by self-occupied property, in-house collections at 1.8x prior strength – is the company’s answer to the segment’s defining risk.")
    P.append(pg)

    # ------------------------------------------------------------------ 20 MSME credit gap
    pg = Page("MSME Credit Gap and Financial Inclusion")
    pg.p("Micro, small and medium enterprises are the demand side of Fedfina’s business. The FY26 MD&A, citing the Union Budget 2026–27 and the Ministry of MSME, records that India has over 7.47 crore MSMEs employing nearly 32.8 crore people – the second-largest employer after agriculture – contributing about 35.4% of manufacturing output, 48.58% of exports and 31.1% of GDP. Yet the sector remains chronically under-financed: the FY24 MD&A noted that of over 64 million MSMEs only 14% had access to formal credit, and the FY26 operating-environment section depicts a formal-sector addressable market of ₹25 trillion against a credit gap of ₹92 trillion.")
    pg.kpis([("7.47 crore", "MSME units"), ("32.8 crore", "People employed"), ("31.1%", "Share of GDP"),
             ("48.6%", "Share of exports"), ("7.9 crore", "Udyam + UAP registrations"), ("₹92 tn", "Estimated MSME credit gap")], cols=6)
    pg.h2("Why the gap persists")
    pg.p("Traditional lenders struggle with MSMEs because incomes are informal, accounts are unaudited, collateral is often residential property rather than business assets, and the cost of physical delivery is high relative to ticket size. Many MSMEs therefore borrow from informal sources at high rates. Gold loans and LAP are the two most natural bridges: both are secured by assets the borrower already owns, both can be underwritten on collateral plus observed cash flow rather than audited financials, and both can be delivered through small branches in the borrower’s own town.")
    pg.h2("Policy and infrastructure support")
    pg.bullets([
        "Udyam registration and the Udyam Assist Platform (4.7 crore and 3.2 crore registrations respectively by March 2026) formalise micro-enterprises and create a verifiable identity for lenders.",
        "The Ministry of MSME’s budgetary outlay has risen steadily over FY20–FY27 (FY26 MD&A chart), funding credit-guarantee schemes, cluster development and production-linked incentives.",
        "GST returns, bank-statement analysis via Account Aggregator, UPI transaction histories and utility-payment data enable cash-flow-based underwriting of thin-file borrowers while maintaining risk discipline.",
        "The RBI’s co-lending model lets banks fund priority-sector MSME assets originated by NBFCs, lowering the blended cost of credit for the borrower.",
    ])
    pg.h2("Fedfina’s inclusion footprint")
    pg.p("The company describes itself as “often the first point of access to formal finance” for its customers. At 31 March 2026 it served 3.44 lakh active customers through 757 branches in 17 states and union territories, with 455 customers per branch; gold-loan customers are predominantly traders, owners of service and manufacturing units and their employees seeking short-term working capital, while small-ticket LAP customers are self-employed households on the outskirts of Tier 1 cities and in Tier 2–3 towns. The BRSR frames responsible lending and consumer financial protection as a material issue, and the company runs financial-literacy programmes through educational institutions and self-help groups. The social relevance of the business model is therefore direct: each secured loan to an MSME household substitutes formal, regulated credit for informal borrowing.")
    pg.p("Analytically, the size of the gap means that growth is not constrained by demand; it is constrained by the lender’s ability to underwrite, collect and fund profitably – which is why the operating and risk chapters of this report focus on those capabilities.")
    P.append(pg)

    # ------------------------------------------------------------------ 21 Regulation
    pg = Page("Regulatory Environment")
    pg.p("As a Middle-Layer NBFC listed on both exchanges with listed debt, Fedfina operates under three regulators – the RBI (prudential and conduct), SEBI (listing, disclosure, insider trading, debt securities) and the Ministry of Corporate Affairs (Companies Act) – in addition to FEMA (for its ECBs), the Prevention of Money Laundering Act and the Digital Personal Data Protection framework. The FY26 secretarial audit report lists ten RBI directions specifically applicable to the company. The most consequential recent change for its largest product is summarised below.")
    pg.table(["RBI Directions on Lending Against Gold Collateral (June 2025; effective 1 April 2026)", "Provision", "Implication for Fedfina"],
             [["Loan-to-value ceiling", "Tiered: up to 85% for loans ≤ ₹2.5 lakh; 80% for ₹2.5–5 lakh; 75% above ₹5 lakh (earlier flat 75%)", "Average ticket ₹2.7 lakh sits at the boundary; headroom exists but portfolio LTV is held at 60.9%"],
              ["LTV maintenance", "Ceiling must be maintained throughout the tenor, not only at sanction; for bullet loans LTV computed on total amount due at maturity", "Requires daily price tracking and systems for top-up/renewal triggers – already in place (gold prices tracked daily)"],
              ["Credit assessment", "Assessment of repayment capacity required for loans above ₹2.5 lakh", "Adds underwriting steps for higher tickets; supports the ‘credit infrastructure’ investment noted by the MD&CEO"],
              ["Renewal / top-up norms", "Revised norms for renewal and top-up; interest to be serviced before renewal", "Changes rollover behaviour; the FY25 letter already flagged pressure on volumes from revised rollover rules"],
              ["Conduct", "Transparent valuation, return of gold within 7 working days of closure, standardised auction norms and borrower communication", "Fedfina auctioned 4,633 accounts in FY26 realising ₹44.0 crore against ₹20.4 crore principal"]],
             widths=[1.7, 2.9, 2.45], font=7.5,
             source="RBI Directions as summarised in EY, ‘RBI gold loan guidelines 2025: impact assessment’ (Feb 2026); " + AR26 + " MD&CEO statement p.18 and Directors’ Report p.76.")
    pg.h2("Other regulations shaping the business")
    pg.bullets([
        "Scale-based regulation (SBR) Directions 2025:: capital (CRAR ≥ 15%), leverage, concentration, liquidity coverage, provisioning floors and the ICAAP policy adopted by Fedfina’s Board.",
        "Risk weights on bank lending to NBFCs (November 2023):: raised sector funding costs and drove diversification; Fedfina responded with a USD 250 million ECB programme (17% of debt) and a CP programme (9%).",
        "Cash disbursal limit on gold loans (₹20,000 per year, 2024):: pushed disbursements to digital channels; over 86% of Fedfina’s e-NACH registrations are digital.",
        "Digital Lending Guidelines and DPDP framework:: consent-based data use, transparency to borrowers, and secure storage – relevant to the BRE, Account Aggregator usage and AI tools.",
        "SEBI LODR, SBEB (ESOPs), NCS (listed NCDs/CPs) and PIT regulations:: three minor BSE fines (₹10,000; ₹1,53,400; ₹10,000) between 2023 and 2026 for filing delays are disclosed; one was later waived.",
        "Companies Act / RBI Statutory Audit Directions 2026:: joint statutory auditors mandatory for NBFCs with assets ≥ ₹15,000 crore – triggered by Fedfina’s ₹16,875 crore balance sheet.",
    ])
    P.append(pg)

    # ------------------------------------------------------------------ 22 Competition & peers
    pg = Page("Competitive Landscape and Peer Snapshot")
    pg.p("Fedfina competes with four groups: (1) banks – including its own parent – which hold about 82% of the organised gold-loan market and price medium-ticket LAP aggressively; (2) large gold-loan NBFCs with national branch networks and strong brands; (3) housing finance companies and affordable-housing lenders in small-ticket LAP and home loans; and (4) digital lenders and fintech–NBFC partnerships that compete on convenience in small-ticket credit. The FY26 MD&A notes that well-capitalised banks are expanding retail and MSME lending using lower funding costs, while fintechs scale through data-driven underwriting and embedded finance.")
    pg.table(["Company (FY26, as reported)", "AUM (₹ cr)", "Gold-loan AUM (₹ cr)", "PAT (₹ cr)", "CRAR (%)", "Branches", "GNPA / NNPA (%)"],
             [list(r) for r in PEERS],
             widths=[2.1, 0.85, 1.15, 0.75, 0.65, 0.7, 0.85], font=8,
             source="Fedfina: " + AR26 + ". Muthoot Finance and Manappuram Finance: FY26 results as reported in results coverage (Investywise, 14 May 2026; IndiaInfoline Directors’ Report extract; Yahoo Finance Q4 FY26 call transcript, 4 May 2026; Multibagg, 10 May 2026). Bases differ (standalone/consolidated); see bibliography.")
    pg.p("The snapshot shows the scale gap: Muthoot’s standalone AUM is about eight times Fedfina’s total book and Manappuram’s consolidated AUM about three times. All three grew gold AUM rapidly in FY26 on the back of record gold prices (Muthoot and Manappuram reported AUM growth of roughly 50% and 48% respectively, Fedfina’s gold AUM grew 76% from a smaller base). Capital adequacy is similar across the three (20.8%–22.4%). Fedfina’s distinguishing features are its bank parentage, its mortgage “second engine” (46.5% of AUM) and a credit-cost profile that, after the FY25 reset, is now within the sub-1% range management targets.")
    pg.h2("Basis of competition")
    pg.table(["Dimension", "Fedfina position (FY26 disclosures)"],
             [["Price / cost of funds", "AA+/Stable from four agencies; Q4 cost of borrowing 7.83%; bank parent among 41 lenders – competitive for an NBFC but above banks"],
              ["Speed and convenience", "10-day approval and 15-day disbursement TAT for mortgages; doorstep gold loans (₹1,730 cr AUM, +108%); 35% of service requests auto-served by bots"],
              ["Distribution", "757 branches, 17 states; field outreach within ~30 km of branches; 200+ connectors and trader partners; ~75% in-house sourcing"],
              ["Brand and trust", "Google reviews up from ~1,500 to 7,500+ at 4.58/5; 85% positive customer-satisfaction score; Federal Bank association"],
              ["Underwriting and risk", "~76% of mortgage AUM from CIBIL >700 customers; 82.2% self-occupied collateral; portfolio gold LTV 60.9% vs regulatory 75–85%"],
              ["Capital efficiency", "Co-lending and DA (12.1% of AUM off-book); ECB and CP diversify funding; Tier II raised via ₹450 cr subordinated debt"]],
             widths=[1.6, 5.45], font=8)
    pg.p("The competitive conclusion is that Fedfina is a mid-sized specialist in a market led by much larger players, and must therefore compete on execution quality, local presence and the complementarity of its two products rather than on scale or price alone.")
    P.append(pg)

    # ------------------------------------------------------------------ 23 Opportunities
    pg = Page("Industry Opportunities")
    pg.p("The sector chapters above point to a set of opportunities that are structural rather than cyclical. They are listed below with the evidence that supports each and the way Fedfina is positioned to capture it.")
    pg.table(["Opportunity", "Evidence (source)", "Fedfina positioning"],
             [["Under-penetrated formal credit", "Household credit/GDP 42% vs 60–76% in China, US, UK; bank credit/GDP ≈56% (AR26 Chairman and MD&CEO)", "Secured products designed for self-employed and MSME borrowers; 757 branches in Tier 2–4 markets"],
              ["Gold-loan market growth", "Organised market > ₹15 lakh crore FY26 → ≈ ₹18 lakh crore FY27 (ICRA); NBFC concentration easing", "Gold AUM +76% to ₹10,352 cr; 12.6 t under custody; doorstep channel; 148 new branches"],
              ["Shift from unsecured to secured", "Stress in personal loans/microfinance (AR26 MD&A); borrower migration to gold loans", "98.9% secured AUM; business-loan book fully assigned (₹886 cr) in H1 FY26"],
              ["MSME LAP demand", "Secured MSME-LAP projected +16–18% p.a. to FY28; 7.47 cr MSMEs; ₹92 tn credit gap", "MT LAP ₹5,570 cr (+ steady disbursements); ST LAP rebuilt on BRE; 70 co-located MSME hubs"],
              ["Falling rate cycle", "Repo cut 125 bps to 5.25%; cost of borrowing 8.72% → 7.83% (Q4 to Q4)", "60% floating borrowings reprice down; mortgage affordability improves"],
              ["Digital public infrastructure", "Aadhaar, UPI, Account Aggregator, GST data lower acquisition and underwriting costs", "LOS–LMS–CRM integration; Credit GPT; 86% digital e-NACH; Fedfina Lite field app"],
              ["Co-lending / capital-light growth", "RBI co-lending framework; banks seek PSL assets", "₹2,433 cr co-lent gold AUM; ₹2,579 cr sell-downs; 12.1% off-book"],
              ["Cross-sell within branch network", "20–25% overlap between gold and LAP customers (MD&CEO)", "70 co-located branches; hyperlocal marketing; 3.44 lakh customers"],
              ["Green and inclusive finance", "Rising demand for green financing (AR26 MD&A)", "Exploring loans for solar installations and energy-efficient appliances"]],
             widths=[1.5, 2.9, 2.65], font=8)
    pg.h2("Sizing the opportunity for a mid-sized lender")
    pg.p("Even a one-percentage-point share of the projected FY27 organised gold-loan market (₹18 lakh crore) would be ₹18,000 crore – larger than Fedfina’s entire FY26 gold book. The company does not need to win share from the leaders to deliver the 20–25% sustainable growth targeted by the Board; it needs to keep displacing informal lenders in its own catchments (the FY26 report states that the gold franchise gained share “from informal lenders”), raise productivity in young branches (gold AUM per branch rose ₹4.4 crore to ₹16.5 crore in a year), and let the mortgage engine compound at the segment’s 16–18% growth rate. The branch-vintage effect is central: the MD&CEO notes that “branch economics improve meaningfully with vintage, and as these branches mature, they will contribute significantly to AUM without proportionate cost addition”.")
    pg.p("The opportunities are therefore real and quantifiable, but each carries an execution condition – collections for ST LAP, custody controls for gold, liability management for the rate cycle – which is why Chapter 6 treats risk as the mirror image of this page.")
    P.append(pg)

    # ------------------------------------------------------------------ 24 Challenges
    pg = Page("Industry Challenges")
    pg.p("The same sector data that reveal opportunity also reveal the challenges facing retail NBFCs. The FY26 MD&A groups them under increased competition, cybersecurity and technology risk, and data-privacy and regulatory compliance; the earlier reports add funding-cost volatility and asset-quality stress. Each is examined below with its specific relevance to Fedfina.")
    pg.bullets([
        "Funding-cost volatility and concentration:: Sector borrowing costs rose after the November 2023 risk-weight increase (Fedfina +40 bps in FY25; cost of borrowings 9.0% in FY25 on the FY26-report basis). Although rates fell in FY26, 60% of Fedfina’s borrowings remain floating and 39% of borrowings mature within one year, so a reversal in the rate cycle would compress spreads within quarters.",
        "Asset-quality stress among informal borrowers:: Small-ticket LAP delinquencies in FY25 lifted credit cost to 1.8% and forced write-offs of ₹88 crore (net) in FY26 and sale of 814 NPA accounts (₹105 crore principal) to ARCs. Sector-wide, microfinance and small personal loans remain stressed, which can spill over into household cash flows that service LAP and gold loans.",
        "Competition and yield pressure:: Banks with 82% of the gold market and lower funding costs, large NBFCs with national brands, and HFCs in affordable housing all compete for the same borrowers. MT LAP origination yield is already 12.0% and the FY26 report mentions “broader industry yield pressures” in that segment.",
        "Gold-price risk:: A 65% price rise in a single year increases eligible loan amounts but also the probability of a correction. Portfolio LTV of 60.9% gives roughly a 35% buffer before principal is uncovered, but auction volumes and customer behaviour change long before that point.",
        "Regulatory change:: The April 2026 gold-lending directions tighten LTV maintenance, renewals and credit assessment; the FY25 letter already attributed volume and credit-cost pressure to earlier RBI gold-loan changes. Compliance costs rise with every new direction (joint auditors, internal ombudsman, IT governance).",
        "Cybersecurity and fraud:: BFSI is among the most targeted sectors globally; the FY26 MD&A cites a sharp rise in attacks on digital banking portals. Fedfina reported frauds of ₹110 lakh to the RBI in FY26 and is prototyping a tracked, dual-authentication “security box” for doorstep gold loans – evidence that physical custody risk is live.",
        "Data privacy:: The DPDP framework raises the bar for consent-based data governance just as lenders increase reliance on alternative data; breaches carry financial and reputational penalties.",
        "Branch-led cost structure:: A 757-branch network with 5,303 employees carries fixed costs; cost-to-income has stayed in a narrow 57–59% band for five years, and 148 young branches must mature before operating leverage appears.",
        "Talent and attrition:: The BRSR reports average voluntary employee turnover of 35.85% – typical of field-intensive NBFCs but costly for underwriting and collections continuity.",
    ])
    pg.p("Taken together these challenges explain why the FY26 recovery, though strong, should be judged over several years: the sector rewards lenders that sustain sub-1% credit costs and stable spreads through a full rate and gold-price cycle, not those that post a single good year.")
    P.append(pg)

    # ------------------------------------------------------------------ 25 Porter
    pg = Page("Porter’s Five Forces")
    pg.p("Porter’s framework assesses the structural attractiveness of an industry by examining five competitive forces. Applied to secured retail lending by NBFCs in India – Fedfina’s arena – the analysis is as follows.")
    pg.table(["Force", "Assessment", "Evidence from the reports", "Intensity"],
             [["Rivalry among existing competitors", "Banks (82% of gold loans), two very large gold NBFCs, HFCs and regional lenders compete for the same semi-urban borrower; competition is on branch proximity, TAT, LTV and price",
               "Top-4 NBFC share of NBFC gold AUM fell from 90% to 81%; MT LAP yield pressure; 148 branch additions by Fedfina alone", "High"],
              ["Threat of new entrants", "Licensing, capital (CRAR 15%), ratings and branch economics are barriers, but fintechs and banks can enter via co-lending or digital channels", "Large corporates investing in digital lending platforms (AR26 MD&A); SBR raises compliance cost for new NBFCs", "Moderate"],
              ["Bargaining power of buyers (borrowers)", "Low for first-time formal borrowers with few alternatives; high for prime MT LAP customers who can refinance with banks", "ST LAP median income ≈ ₹5 lakh, limited documents; MT LAP customers with CIBIL >700 (81%)", "Moderate"],
              ["Bargaining power of suppliers (funders)", "Lenders, bond investors and rating agencies set the cost of the NBFC’s raw material; risk-weight changes showed this power in FY24–25", "41 lenders; AA+ rating; ECB 17% and CP 9% of debt; Federal Bank ₹1,370 cr exposure; fixed-rate share 40%", "Moderate to high"],
              ["Threat of substitutes", "Unsecured personal loans, credit cards, informal money-lenders, gold ETF/sale, bank overdrafts", "Borrower shift from unsecured to gold loans in FY26; informal lenders still hold a large share of gold lending", "Moderate"]],
             widths=[1.35, 2.45, 2.45, 0.8], font=8)
    pg.h2("Interpretation")
    pg.p("Rivalry is the dominant force. The industry is attractive in aggregate – growing in the mid-teens with low loss rates for secured products – but returns accrue to lenders with distribution density, funding advantage and operational control, not to all participants. Fedfina’s responses map onto each force: against rivalry it deepens local presence (hyperlocal marketing, doorstep service) and leverages customer overlap between products; against supplier power it has diversified funding across 41 lenders, four rating agencies and three instrument classes while raising fixed-rate exposure; against buyer power in MT LAP it emphasises service and relationship rather than price; and against substitutes it positions gold loans and LAP as cheaper, faster and more dignified than informal credit.")
    pg.p("The force most likely to change over the study horizon is the threat of new entrants via co-lending and digital channels: as banks seek priority-sector gold and MSME assets, NBFCs with origination capability become partners as much as competitors, which both reduces rivalry and increases dependence on bank partners. This dual role is visible in Fedfina’s ₹2,433 crore of co-lent gold AUM.")
    P.append(pg)

    # ------------------------------------------------------------------ 26 PESTLE
    pg = Page("PESTLE Analysis")
    pg.p("The PESTLE framework organises external influences into political, economic, social, technological, legal and environmental factors. The table below records each factor, the evidence available in the annual reports and the implication for Fedfina.")
    pg.table(["Factor", "Key developments (FY24–FY26)", "Implication for Fedfina"],
             [["Political / policy", "Government priority on MSMEs (budget outlay rising FY20–FY27), affordable housing, financial inclusion, Udyam formalisation (7.9 crore registrations); fiscal consolidation with sustained capex",
               "Supportive demand environment for LAP and inclusion-oriented lending; policy stability lowers country risk for ECB investors"],
              ["Economic", "GDP growth 7.2% → 7.1% → 7.7%; CPI down to ≈2% average; repo cut 125 bps to 5.25%; gold price +65% in CY2025; rural consumption recovery; global growth ≈3.1–3.4%",
               "Lower cost of funds (Q4 CoB 7.83%), higher gold collateral values, better borrower cash flows; but gold-price and rate reversals are the main macro risks"],
              ["Social", "25,000 tonnes of household gold; cultural acceptance of gold loans rising; growing self-employed and gig workforce; aspiration for home ownership among 25–40 age group; 16.4% women in Fedfina’s workforce",
               "Large, culturally embedded demand base; need for respectful collections and transparent auctions to preserve trust; D&I targets (≥22% women in senior management by FY28)"],
              ["Technological", "Aadhaar e-KYC, UPI, Account Aggregator, GST data; AI/GenAI tools (Credit GPT, Fedfina GPT); Salesforce BRE; cloud (AWS); rising cyber threats to BFSI",
               "Faster, more consistent underwriting and collections (70% digital collections); but larger attack surface – Zero Trust, MFA, EDR/XDR, VAPT, red-teaming deployed"],
              ["Legal / regulatory", "SBR Directions 2025; gold-lending directions (effective Apr 2026); Governance, KYC, Internal Ombudsman and Fraud Risk Directions; DPDP; SEBI LODR; joint-auditor requirement; three minor BSE fines",
               "Compliance is a core capability; LTV and renewal rules reshape gold product design; disclosure quality is a differentiator for a listed NBFC"],
              ["Environmental", "Climate-risk assessment conducted; Scope 1+2 emission intensity cut ≈25% (3.93 → 2.96 tCO2e per ₹ crore turnover); Scope 3 monitoring from FY27; LED branches; 1.9 t e-waste recycled; 89,432 kl water",
               "Direct footprint is small (service business) but climate events can affect branches and borrowers; green-loan products (solar, efficient appliances) are an emerging opportunity"]],
             widths=[1.1, 3.1, 2.85], font=8, source=f"{AR26} Corporate Overview p.26–27, 32–43; MD&A p.54–63; Directors’ Report; BRSR.")
    pg.p("Overall assessment. Five of the six factors are currently supportive or neutral; the legal/regulatory factor is the one most likely to constrain near-term volumes (gold-loan renewals and LTV maintenance) while improving long-term industry conduct. The economic factor is favourable today but is also the source of the two largest cyclical risks – gold price and interest rates – examined in Chapter 6.")
    pg.h2("Linking PESTLE to the rest of the study")
    pg.p("The six factors are not independent. The political and economic factors (financial-inclusion priority, falling repo rate, strong gold prices) created the demand and funding conditions that produced FY26’s 27.5% AUM growth and 8.6% spread; the social and technological factors (self-employed households, digital public infrastructure) determine the cost at which that demand can be served and underpin the BRE-based underwriting and 70% digital collections discussed in Chapters 3 and 4; and the legal and environmental factors set the boundaries within which growth is permitted – the gold-lending Directions effective 1 April 2026 being the most immediate. Chapter 6 converts the adverse elements of each factor into the risk register, and Chapter 7 uses the favourable elements as the ‘opportunities’ column of the SWOT. Readers should therefore treat this page as the bridge between the industry analysis of Chapter 2 and the company analysis that follows.")
    P.append(pg)

    return P
