from report_builder import Page
from report_data import *

AR26 = "Fedfina Annual Report 2025-26"
AR25 = "Fedfina Annual Report 2024-25"
AR24 = "Fedfina Annual Report 2023-24"


def cr(x, d=1):
    return f"{x/100:,.{d}f}"


def pages(C):
    P = []
    F26, F25 = FIN["FY26"], FIN["FY25"]
    P26, P25 = PL["FY26"], PL["FY25"]
    B26, B25 = BS["FY26"], BS["FY25"]
    L26, L25 = LOANS["FY26"], LOANS["FY25"]

    # ================================================================== CHAPTER 6 RISK
    pg = Page("Chapter 6 — Risk Management Architecture")
    pg.p("For a lender, risk management is the business, not a department. Fedfina’s FY26 MD&A describes an enterprise risk-management framework built on three lines of defence – business units own risk; the risk, compliance and finance functions provide oversight; internal audit provides independent assurance – under a Board-level Risk Management Committee supported by the Audit Committee, the Asset Liability Committee (ALCO), the IT Strategy Committee, a Wilful Default Review Committee and a Special Committee for monitoring frauds. The Board has adopted an ICAAP policy, a Fraud Risk Management and Fraud Investigation Policy, a whistle-blower policy, a compensation policy aligned to the RBI circular of 29 April 2022 and a related-party transaction policy.")
    pg.table(["Risk category (FY26 MD&A)", "Description given by the company", "Mitigation disclosed"],
             [["Credit risk", "Borrower default on gold, mortgage and legacy business loans", "Secured lending (98.9% of AUM), LTV discipline, BRE-based underwriting, bureau thresholds, early-warning signals, in-house collections, ECL provisioning"],
              ["Liquidity risk", "Inability to meet obligations as they fall due or to refinance", "ALCO; structural-liquidity buckets; 41 lenders; cash ₹1,340 crore; undrawn lines; CP/NCD/ECB diversification"],
              ["Market risk", "Interest-rate, gold-price and foreign-exchange movements", "40% fixed-rate borrowings; daily gold-price tracking and LTV triggers; ECBs fully hedged with cross-currency swaps"],
              ["Operational risk", "Process failures, people errors, custody losses, system outages", "Standard operating procedures, maker-checker, insurance, audits, security-box prototype, business continuity"],
              ["Fraud risk", "Internal or external fraud (gold purity, identity, documentation)", "Multi-layered prevention: due diligence, authentication checks, AI analytics; ₹110 lakh reported in FY26"],
              ["Technology and cyber risk", "Data breaches, ransomware, system compromise", "Zero Trust, MFA, EDR/XDR, VAPT, red-teaming, vendor risk management; IT Strategy Committee"],
              ["Regulatory and compliance risk", "Breach of RBI/SEBI/Companies Act requirements; regulatory change", "Compliance function, secretarial audit, internal ombudsman, policy framework; gold-loan directions readiness"],
              ["Reputational risk", "Loss of stakeholder trust from conduct or service failures", "Fair-practices code, grievance redressal, transparent auctions, CSAT monitoring"],
              ["Strategic / concentration risk", "Product or geographic concentration; execution of Fedfina 2.0", "Twin-engine model; 17-state footprint; top-5 states 75.1% of AUM; Board oversight"],
              ["ESG / climate risk", "Physical and transition climate risks; social licence", "Climate-risk assessment conducted; emission-intensity reduction; green-loan exploration"]],
             widths=[1.55, 2.3, 3.2], font=7.5, source=f"{AR26}, MD&A – Risk Management section and ‘Risks and concerns’ table; Directors’ Report; Report on Corporate Governance.")
    pg.h2("Assurance and oversight indicators FY26")
    pg.kpis([("11", "Board meetings"), ("4", "IT Strategy Committee meetings"), ("16 (3)", "Whistle-blower complaints (vigil)"), ("Nil", "Audit / secretarial qualifications"),
             ("₹110 lakh", "Frauds reported to RBI"), ("0.47%", "Top-20 borrowers / advances")], cols=6)
    pg.p("Assessment. The architecture is standard for a Middle-Layer NBFC and is now tested: the FY25 stress revealed a gap (collections lagging growth) that the framework detected late but then remediated within a year through structural changes rather than cosmetic ones. The pages that follow examine each risk with the quantitative disclosures available.")
    P.append(pg)

    # ------------------------------------------------------------------ 63 Credit risk
    pg = Page("Credit Risk")
    pg.p("Credit risk is the risk that borrowers fail to repay. For Fedfina it has three distinct faces: gold loans, where the collateral almost always covers the exposure and the residual risk is price and fraud; mortgage loans, where default is low but resolution is slow and costly; and the legacy unsecured book, which has now been exited. The FY26 data show the result of moving the mix towards the first two.")
    pg.table(["Indicator", "FY24", "FY25", "FY26", "Direction"],
             [["GNPA / NNPA (%)", "1.7 / 1.3", "2.0 / 1.2", "1.9 / 1.3", "Stable"],
              ["Provision coverage ratio (%)", "20.4", "40.0", "32.3", "Lower after write-offs/ARC sales"],
              ["Credit cost (% average assets)", "0.7", "1.8", "0.8", "Normalised"],
              ["Impairment on financial instruments (₹ crore)", "n.a.", "216.4", "115.3", "−47%"],
              ["Stage 2 + Stage 3 share of amortised book", "n.a.", "7.4%", "3.5%", "Halved"],
              ["Secured share of AUM", "≈ 84%", "≈ 89%", "98.9%", "Fully secured"],
              ["Unsecured loans on book (₹ crore)", "n.a.", "1,232", "48", "−96%"],
              ["Write-offs (₹ crore, note 48)", "n.a.", "6.8", "88.2", "Clean-up"],
              ["NPA accounts sold to ARCs (principal, ₹ crore)", "n.a.", "16.9 (1 account)", "104.9 (814 accounts)", "Clean-up"],
              ["Monthly Stage 3 recoveries (₹ crore)", "n.a.", "6.5", "14.5", "More than doubled"],
              ["Gold portfolio LTV", "70.5%", "n.a.", "60.9%", "Conservative"]],
             widths=[2.7, 0.9, 1.1, 1.3, 1.05], font=8, source=f"{AR24}, {AR25}, {AR26} – Key Highlights, MD&CEO statements, notes 8, 32 and 48. FY24/FY25 secured shares derived from product mix.")
    pg.h2("Underwriting and monitoring controls")
    pg.bullets([
        "Origination:: ≈75% in-house sourcing (DSA 25%); API-led BRE for ST LAP removes discretion; bureau-score thresholds (81% of MT LAP and 68% of ST LAP AUM above CIBIL 700); cash-flow assessment for informal incomes; property valuation and legal checks; 82.2% of mortgage AUM backed by self-occupied property.",
        "Portfolio monitoring:: early-warning signals, vintage tracking of the FY26 book versus the old book, concentration limits (top-20 borrowers 0.47% of advances; four largest impaired accounts ₹9.4 crore), ECL staging under Ind AS 109 with RBI prudential floors.",
        "Collections:: verticalised, in-house team scaled to 1.8x FY25 strength with agency reliance cut to 0.4x; digital collections above 70% of monthly receipts; 90% of accounts on e-NACH; early-bucket cure rates up ~2 pp and Stage 1–2 cure rates up 5–6 pp; collection efficiency 99.7%.",
        "Resolution:: SARFAESI for mortgages; gold auctions under RBI norms (4,633 accounts, 92% of dues realised); sale of delinquent pools to ARCs.",
    ])
    pg.h2("Residual concerns")
    pg.p("Three concerns remain. First, additions to credit-impaired loans rose 16% to ₹227 crore in FY26 – the old vintages are still slipping, and the improvement in stock ratios owes much to write-offs and sales. Second, the FY26 ST LAP cohort is unseasoned; small-ticket mortgage delinquency typically peaks 18–36 months after origination. Third, the household balance sheets that service ST LAP and gold loans are exposed to the same unsecured-credit stress that hurt the sector in FY25, even though Fedfina no longer lends unsecured itself. The sub-1% credit-cost commitment should therefore be judged over FY27–FY28, not FY26 alone.")
    P.append(pg)

    # ------------------------------------------------------------------ 64 Liquidity / ALM
    pg = Page("Liquidity Risk and Asset-Liability Management")
    pg.p("Because NBFCs cannot raise deposits, liquidity risk is existential: the 2018 IL&FS episode showed how quickly wholesale funding can close. Fedfina’s structural liquidity statement at 31 March 2026 (note 48) shows the maturity profile of advances and borrowings in RBI buckets; the cumulative view is charted below.")
    pg.fig(f"{C}/alm.png", "Figure 15 – Cumulative maturity of advances versus borrowings, 31 March 2026 (₹ crore). Source: " + AR26 + ", note 48 – maturity pattern of assets and liabilities.", 2.0, width=4.6)
    adv_t = sum(ALM_ADV_26); bor_t = sum(ALM_BOR_26)
    cum_a = cum_b = 0; rows = []
    for i, bkt in enumerate(ALM_BUCKETS):
        cum_a += ALM_ADV_26[i]; cum_b += ALM_BOR_26[i]
        rows.append([bkt, f"{ALM_ADV_26[i]/100:,.0f}", f"{ALM_BOR_26[i]/100:,.0f}", f"{(ALM_ADV_26[i]-ALM_BOR_26[i])/100:+,.0f}", f"{cum_a/adv_t*100:.1f}%", f"{cum_b/bor_t*100:.1f}%"])
    rows.append(["Total", f"{adv_t/100:,.0f}", f"{bor_t/100:,.0f}", f"{(adv_t-bor_t)/100:+,.0f}", "100%", "100%"])
    pg.table(["Bucket", "Advances (₹ cr)", "Borrowings (₹ cr)", "Gap (₹ cr)", "Cum. advances %", "Cum. borrowings %"], rows,
             widths=[0.9, 1.2, 1.2, 1.1, 1.3, 1.35], font=8, source=f"{AR26}, note 48 (₹ lakh converted to ₹ crore; cumulative shares derived). Borrowings here are market and bank borrowings per the ALM table (₹13,484 crore).")
    pg.p(f"Interpretation. The profile is strongly positive: {sum(ALM_ADV_26[:7])/adv_t*100:.0f}% of advances mature within one year (the gold book) against {sum(ALM_BOR_26[:7])/bor_t*100:.0f}% of borrowings, so inflows exceed outflows in every cumulative bucket up to one year by a wide margin (₹3,749 crore cumulative surplus at 12 months, derived). The mismatch reverses in the 1–3 year bucket, where ₹6,409 crore of borrowings mature against ₹1,984 crore of advances – this is where the long-tenor mortgage book is funded by medium-term bank loans and ECBs, and it is the bucket to watch for refinancing. Compared with 31 March 2025, the share of advances maturing within a year rose (as gold loans doubled) while borrowings lengthened (ECB and 2033 sub-debt), improving the structure.")
    pg.p("Buffers and governance. Cash and cash equivalents of ₹1,340 crore plus bank balances of ₹51 crore equal 7.9% of total assets (derived), with investments of ₹402 crore largely liquid; 41 lenders and a shareholder-approved borrowing limit of ₹18,000 crore (about 75% utilised) provide headroom; CP outstanding of ₹1,164 crore is the main short-term rollover exposure. ALCO oversees the position under the SBR liquidity framework; the specific liquidity coverage ratio is not disclosed in the extracted text and is not estimated here.")
    P.append(pg)

    # ------------------------------------------------------------------ 65 Market risk
    pg = Page("Market Risk: Interest Rates, Gold Price and Currency")
    pg.h2("Interest-rate risk")
    pg.p("Fedfina’s assets are largely fixed-rate for their (short) tenor in gold and floating or periodically reset in mortgages; its liabilities were about 60% floating at 31 March 2026 after the fixed-rate share was deliberately raised from roughly 10% to 40% during FY26. In a falling-rate year this mix produced a 90 bp drop in cost of borrowings and an 8.6% spread; in a rising-rate year it would compress the spread until gold loans repriced (within a year) and mortgage rates were reset. The company does not publish an earnings-at-risk sensitivity in the extracted text, so this report illustrates the exposure: a 100 bp rise in cost on the floating 60% of ₹13,484 crore of borrowings would add about ₹81 crore to annual finance costs before any asset repricing – roughly 18% of FY26 PBT (derived, illustrative). The 2033 subordinated issues at 8.85–8.90% and the 7.29% January 2026 NCD show the company locking in term funding near cycle lows.")
    pg.h2("Gold-price risk")
    pg.table(["Gold-price sensitivity (derived, illustrative)", "Value"],
             [["Gold AUM / gold loans on book (31 Mar 2026)", "₹10,352 crore / ₹7,919 crore"], ["Portfolio LTV / onboarding LTV", "60.9% / ≈70%"],
              ["Price fall at which average loan reaches 100% LTV", "≈ 39% (1 − 0.609)"], ["Price fall at which a fresh 70%-LTV loan is uncovered", "≈ 30%"],
              ["Price move in CY2025", "+65% (USD 2,607 → 4,315/oz)"], ["Auction realisation vs dues in FY26", "₹44.0 crore vs ₹48.0 crore (≈92%)"],
              ["Regulatory LTV from 1 April 2026", "85% (≤ ₹2.5 lakh), 80% (₹2.5–5 lakh), 75% (> ₹5 lakh), maintained through tenor"]],
             widths=[4.2, 2.85], font=8.5, source=f"{AR26}; RBI Directions 2025 (EY summary). Sensitivities are arithmetic on disclosed LTVs, not company estimates.")
    pg.p("A correction in gold prices affects the business through three channels: collateral cover (buffer shown above), demand (smaller eligible loans, lower disbursements) and conduct (more auctions, customer attrition). The short tenor is the main defence – the book turns over within a year, so LTVs reset quickly – together with daily price tracking and margin-call/top-up triggers. The decision to target tonnage growth of 10–12% rather than price-led growth is the strategic hedge. The last comparable episode, the 2013 gold-price fall of about 25%, caused losses at some gold NBFCs operating at 85%+ LTV; at 61% portfolio LTV Fedfina’s exposure is materially lower.")
    pg.h2("Currency risk")
    pg.p("ECB borrowings of ₹2,382 crore (USD 250 million programme) and FCNR borrowings of ₹62.5 crore are the only foreign-currency liabilities. The company states that ECBs are fully hedged for the entire maturity by cross-currency swaps; derivative assets of ₹215 crore (notional ₹2,446 crore) at 31 March 2026 are the mark-to-market of these hedges and are offset through cash-flow-hedge accounting in OCI. The residual foreign-currency translation loss in finance costs was ₹1.7 crore. Currency risk is therefore economically neutralised, with counterparty and basis risk on the swaps the remaining exposure.")
    P.append(pg)

    # ------------------------------------------------------------------ 66 Operational / fraud / cyber
    pg = Page("Operational, Fraud and Cyber-Security Risk")
    pg.p("Operational risk in a 757-branch, 5,303-employee lender handling 12.6 tonnes of gold and 3.4 lakh customer relationships is pervasive. The FY26 disclosures allow a reasonably granular view.")
    pg.table(["Risk", "Exposure indicators (FY26)", "Controls and outcomes disclosed"],
             [["Gold custody and purity", "12.6 t of pledged gold across 558 branches; doorstep channel AUM ₹1,730 crore (+108%)", "Strong-rooms, insurance (premium ₹11 crore, +160%), dual control, surprise audits; prototype portable ‘security box’ with dual authentication, live tracking and remote unlocking; AI-based fraud analytics"],
              ["Fraud", "Frauds reported to RBI ₹110 lakh in FY26 (0.005% of AUM, derived); Special Committee of the Board for monitoring frauds", "Board-approved Fraud Risk Management and Investigation Policy; Master Direction on Fraud Risk Management (2024) compliance; whistle-blower channel (16 complaints)"],
              ["People and process", "735 employees added; 148 new branches; voluntary attrition 35.85%; 25% DSA sourcing", "Gurukul and Branch Gurukul Days; DREAM programme; 7.44 training hours per employee; standard operating procedures; maker-checker in LOS"],
              ["Technology and cyber", "Rising attacks on BFSI digital portals (MD&A); cloud (AWS), mobile apps, API integrations with 20+ partners", "Zero Trust network access, MFA, EDR/XDR, VAPT, red-team exercises, vendor risk management; IT Strategy Committee met 4 times; ISO-aligned information-security practices; business-continuity planning"],
              ["Data privacy", "Customer KYC, bureau and Account Aggregator data; DPDP framework", "Consent-based data governance; data-classification tools (Klassify, Forcepoint, Netskope); privacy policy"],
              ["Outsourcing and third parties", "DSAs, collection agencies (commission ₹24 crore), technology vendors, ARCs", "Vendor risk management; agency reliance cut to 0.4x; RBI outsourcing directions"],
              ["Legal and conduct", "SARFAESI actions, auction notices, complaints; Internal Ombudsman Directions 2026", "100% complaint resolution within TAT; fair-practices code; CSAT 85%"],
              ["Business continuity", "Branch network exposed to floods, strikes, local disruptions", "BCP/DR framework; cloud infrastructure; climate-risk assessment conducted"]],
             widths=[1.3, 2.5, 3.25], font=7.5, source=f"{AR26}, MD&A, Corporate Overview (technology, cyber-security, people), Directors’ Report (frauds, whistle-blower), notes 34 and 48; BRSR.")
    pg.h2("Assessment")
    pg.p("The most consequential operational exposure is gold custody in a rapidly growing doorstep channel: the company’s own investment in a tracked, dual-authenticated portable locker signals that it regards this as a live risk. Reported fraud of ₹1.1 crore is low in absolute and relative terms, but the number of frauds and their type are not disclosed in the extracted text, so trend analysis is not possible. Cyber-security disclosures are more detailed than those of many peers and name specific controls; the absence of any disclosed material incident is a positive but not a guarantee. The 35.85% attrition rate is the metric most likely to translate into operational error, and the training and career programmes described are the right response. Overall, operational risk appears actively managed, with the growth in young branches and doorstep volumes the main sources of incremental exposure in FY27.")
    pg.p("Cost of control. The 160% rise in insurance premium to ₹11 crore is one visible price of the gold-custody build-out (12.6 tonnes, 558 branches, a doubling of doorstep AUM); together with agency commissions of ₹24 crore, security, audit and technology costs, these items form part of the operating-expense base that keeps the cost-to-income ratio near 57%. They are, however, the costs that make a 0.8% credit cost possible on a book that turns over within a year, and should be read as risk expenditure rather than inefficiency.")
    P.append(pg)

    # ------------------------------------------------------------------ 67 Regulatory & reputational
    pg = Page("Regulatory, Compliance and Reputational Risk")
    pg.p("Fedfina’s compliance perimeter spans the RBI (NBFC-ML under SBR), SEBI (equity and debt listing), the Companies Act, FEMA (ECBs), PMLA and the DPDP framework. The secretarial audit report for FY26 lists ten RBI directions specifically applicable to the company and records no qualification. The table summarises the regulatory record and the forward-looking regulatory risks.")
    pg.table(["Item", "Disclosure", "Assessment"],
             [["RBI penalties / strictures in FY24–FY26", "None disclosed", "Clean prudential record"],
              ["SEBI / exchange actions", "BSE fines ₹10,000 and ₹1,53,400 (relating to 2023) and ₹10,000 (2024, later waived) for filing delays; paid March 2026", "Minor procedural lapses; immaterial"],
              ["Statutory / secretarial audit", "Unmodified opinion; no qualifications; auditors KKC & Associates LLP and DKJ & Associates", "Satisfactory"],
              ["Joint statutory audit", "V. Sankar Aiyar & Co. proposed as joint auditor from 31st AGM (RBI Statutory Audit Directions 2026; assets ≥ ₹15,000 crore)", "Adds assurance; modest cost"],
              ["Gold-lending Directions 2025 (effective 1 Apr 2026)", "Tiered LTV, LTV maintenance, 12-month bullet cap, credit assessment above ₹2.5 lakh, standard auction and gold-return norms", "Main forward-looking regulatory risk for 51% of AUM; readiness indicated by conservative LTV and system capability"],
              ["Cash disbursal limit (₹20,000) and digital lending guidelines", "Implemented; >86% digital e-NACH registration", "Operational, not financial, impact"],
              ["Internal Ombudsman Directions 2026", "Applicable; grievance framework in place", "Compliance cost; conduct benefit"],
              ["DPDP framework", "Consent-based governance and data-classification tools", "Rising obligation; breach risk"],
              ["Risk-weight changes on bank lending to NBFCs (Nov 2023)", "Raised cost of borrowings ≈40 bps in FY25", "Shows sensitivity to regulatory funding changes"],
              ["Related-party oversight", "Federal Bank funding ₹1,370 crore, interest ₹84.8 crore, distribution income ₹33 crore – arm’s length, Audit Committee approved", "Transparent; dependence moderate (10% of debt)"]],
             widths=[2.0, 3.0, 2.05], font=7.5, source=f"{AR26}, Directors’ Report, Report on Corporate Governance, secretarial audit report, BRSR; RBI Directions 2025.")
    pg.h2("Reputational risk")
    pg.p("Gold lending and small-ticket mortgage recovery are conduct-sensitive activities: auctioning a family’s jewellery or enforcing against a self-occupied home attracts scrutiny from regulators, courts, media and local communities. Fedfina’s disclosed mitigants are a fair-practices code, transparent auction procedures with surplus refunds, a grievance mechanism with 100% resolution within TAT, an 85% positive CSAT score, rising public ratings (4.58/5 on Google across 7,500+ reviews) and financial-literacy outreach. Its brand is also tied to Federal Bank’s, which raises both the standard expected and the cost of any lapse. No material customer-conduct action is disclosed for FY26.")
    pg.p("Assessment. Regulatory risk at Fedfina is predominantly about change rather than non-compliance: the record is clean, but the rules governing its largest product changed materially on 1 April 2026 and the compliance load for a Middle-Layer listed NBFC keeps rising. The analytical implication is that compliance capacity – systems, people and Board attention – is a prerequisite for the growth plan, and the FY26 disclosures suggest it is being built.")
    P.append(pg)

    # ------------------------------------------------------------------ 68 Collections (concentration + collections)
    pg = Page("Collections Capability and Concentration Risk")
    pg.h2("Collections: the lesson of FY25")
    pg.p("The FY25 annual report is unusually candid: small-mortgage delinquencies rose and realisation from deeper-bucket NPA pools fell because “our collection infrastructure had not kept pace with business growth”. The FY26 report describes the rebuild and its measured effects. The sequence is a textbook case of how lender profitability depends on an operational capability that does not appear on the balance sheet.")
    pg.table(["Collections lever", "FY25 position", "FY26 action", "FY26 measured effect"],
             [["Structure", "Mixed in-house and agency; collections within business lines", "Verticalised collections; in-house team scaled to 1.8x FY25", "Agency reliance 0.4x; agency commission −7% (₹23.9 crore)"],
              ["Early buckets", "Rising 30+ day delinquency in ST LAP", "Early-warning signals; digital reminders; e-NACH push", "Early-bucket cure rates +≈2 pp; 90% accounts on e-NACH; 70%+ digital collections"],
              ["Stage 1–2 management", "Stage 2 at 5.1% of amortised book", "Cure-focused teams; restructured incentives", "Stage 1–2 cure rates +5–6 pp; Stage 2 down to 1.9%"],
              ["Stage 3 resolution", "Monthly Stage 3 recoveries ₹6.5 crore; one NPA account sold", "SARFAESI, settlements, ARC sales, write-offs", "Monthly Stage 3 recoveries ₹14.5 crore; 814 accounts (₹105 crore) sold; write-offs ₹88 crore"],
              ["Outcome", "Credit cost 1.8%; PCR built to 40%", "Credit cost commitment < 1%", "Credit cost 0.8%; collection efficiency 99.7%"]],
             widths=[1.3, 1.8, 2.0, 1.95], font=8, source=f"{AR25}, MD&CEO letter; {AR26}, MD&CEO statement, notes 34 and 48.")
    pg.h2("Concentration risk")
    pg.fig(f"{C}/top5.png", "Figure 13 – Share of AUM in top five states, FY21–FY26. Source: annual reports FY24–FY26 (geographic concentration disclosures).", 2.0, width=5.2)
    pg.table(["Concentration dimension", "FY26 disclosure", "Comment"],
             [["Product", "Gold 51.4%, mortgage 46.5%", "Two products – concentration by design, diversified by behaviour"],
              ["Geography", "Top-5 states 75.1% of AUM (FY21: 85.1%); 4 states host 61% of branches", "Improving; still western/southern India heavy"],
              ["Borrower", "Top-20 borrowers 0.47% of advances (FY25: 0.70%)", "Negligible single-name risk"],
              ["Collateral type", "Gold 47% of total assets; residential property ₹5,413 crore; commercial ₹852 crore", "Gold-price and property-market sensitivity"],
              ["Funding", "Bank term loans 50%; largest single lender Federal Bank ≈10% of debt", "Moderate; diversified across 41 lenders"]],
             widths=[1.6, 3.0, 2.45], font=8, source=f"{AR26}, Key Highlights, MD&A, note 48 (concentration, real-estate exposure, top borrowers).")
    P.append(pg)

    # ------------------------------------------------------------------ 69 Risk matrix
    pg = Page("Consolidated Risk Matrix")
    pg.p("The matrix below consolidates the analysis of this chapter. Likelihood and impact are the author’s qualitative judgements based on the disclosed evidence; they are not company assessments. ‘Trend’ compares FY26 with FY25.")
    pg.table(["#", "Risk", "Likelihood", "Impact", "Trend", "Key evidence", "Principal mitigants"],
             [["1", "Gold-price correction", "Medium", "High", "↑ (price +65%)", "Gold 51% of AUM; LTV 60.9%; tonnage +12%", "Short tenor; daily tracking; conservative LTV; tonnage-led targets"],
              ["2", "ST LAP asset quality (new vintage)", "Medium", "Medium", "↓", "Stage 2 1.9%; cure rates up; book unseasoned", "BRE underwriting; in-house collections; co-location"],
              ["3", "Rising leverage / capital", "Medium", "Medium", "↑", "D/E 4.6x; Tier I 17.5% (−1.4 pp)", "CRAR 22.4%; RoE 12.6% retained; Tier II headroom"],
              ["4", "Interest-rate reversal", "Low–Medium", "Medium", "↓", "60% floating; 39% of debt < 1 year", "Fixed share 40%; short asset tenor; spread 8.6%"],
              ["5", "Regulatory change (gold directions)", "High (certain)", "Medium", "New", "Effective 1 Apr 2026; renewal/LTV rules", "Low LTV; systems; experience with 2024 changes"],
              ["6", "Competition / yield pressure", "High", "Medium", "→", "Banks 82% of gold market; MT LAP yield 12.0%", "Local presence; service; cross-sell; brand"],
              ["7", "Branch-expansion execution", "Medium", "Medium", "↑", "148 young branches; C/I 57.2%", "Vintage economics; hub-and-spoke; productivity tracking"],
              ["8", "Operational / custody / fraud", "Medium", "Medium", "↑ (DSGL +108%)", "Frauds ₹110 lakh; doorstep growth", "Security box; insurance; audits; AI analytics"],
              ["9", "Cyber / data privacy", "Medium", "High", "↑ (sector)", "Rising BFSI attacks; DPDP", "Zero Trust, MFA, EDR/XDR, VAPT, red-teaming"],
              ["10", "Liquidity / refinancing", "Low", "High", "↓", "1–3 yr bucket gap ₹4,425 crore; CP ₹1,164 crore", "Positive <1-yr gap; cash ₹1,340 crore; 41 lenders; AA+"],
              ["11", "Attrition / people", "High", "Low–Medium", "→", "Voluntary attrition 35.85%", "Training, ESOPs, career programmes"],
              ["12", "Reputational / conduct", "Low", "High", "→", "Auctions 4,633; SARFAESI; CSAT 85%", "Fair practices; ombudsman; transparency"],
              ["13", "Parent / shareholder changes", "Low", "Medium", "New (True North exit)", "AIF holding 14.4% → 13.0%; promoter 60.8%", "Stable promoter; broadened public float"],
              ["14", "Macro slowdown / rural stress", "Low–Medium", "Medium", "↓", "GDP 7.7%; CPI ≈2%; rural recovery", "Secured book; granular tickets; geographic spread"]],
             widths=[0.3, 1.45, 0.8, 0.7, 0.85, 1.6, 1.35], font=7.5)
    pg.p("Reading the matrix. The highest-impact risks (gold price, cyber, liquidity, reputation) are those with the strongest mitigants and, except for gold price, low-to-medium likelihood. The risks most likely to materialise (regulatory change, competition, attrition) have medium or lower impact. The risks whose trend is rising – gold price, leverage, branch execution, custody – are all consequences of FY26’s success, which is the natural pattern after a strong growth year and the reason this report treats FY27 asset quality and capital as the key monitoring variables.")
    P.append(pg)

    # ------------------------------------------------------------------ 70 ESG
    pg = Page("Environmental, Social and Governance (ESG) Profile")
    pg.p("Fedfina publishes a Business Responsibility and Sustainability Report (BRSR) within its annual report, and the FY26 Corporate Overview devotes several pages to ESG. The disclosures that can be quantified are collected here.")
    pg.table(["Pillar", "Indicator", "FY25", "FY26", "Target / comment"],
             [["Environment", "Scope 1 + 2 emission intensity (tCO2e per ₹ crore turnover)", f"{KPI26['emission_int_from']}", f"{KPI26['emission_int_to']}", "≈25% reduction; Scope 3 monitoring from FY27"],
              ["Environment", "Water withdrawal (third-party, kilolitres)", "77,509", f"{KPI26['water_kl']:,}", "All operational; intensity tracked"],
              ["Environment", "E-waste recycled through certified handlers", "–", f"{KPI26['ewaste_t']} t", "Paper reduced through digitisation"],
              ["Environment", "Energy efficiency", "–", "LED lighting (20–40% lower power); certified green main office", "Climate-risk assessment conducted"],
              ["Environment", "Green products", "–", "Solar and energy-efficient appliance loans under exploration", "Business-led sustainability"],
              ["Social", "Women in workforce", f"{KPI26['women_prev']}%", f"{KPI26['women']}%", "≥22% women in senior management by FY28"],
              ["Social", "Training hours per employee / participation", "–", f"{KPI26['training_hrs']} / 70.3%", "57 online modules; ₹0.27 crore invested"],
              ["Social", "Voluntary attrition", "–", f"{KPI26['attrition']}%", "Field-heavy workforce"],
              ["Social", "CSR expenditure (₹ crore)", "4.73", "5.84", "2% of average profits; Cuddles Foundation (496 children), Samarthanam Trust (700 women)"],
              ["Social", "Customer satisfaction / complaint resolution", "–", "85% positive / 100% within TAT", "Internal Ombudsman in place"],
              ["Social", "Financial inclusion", "–", "3.44 lakh customers; 757 branches in Tier 2–4 markets", "First formal-credit access for many borrowers"],
              ["Governance", "Board independence / women directors", "–", "5 of 9 independent; 2 women", "Chairman unrelated to CEO"],
              ["Governance", "Board meetings / IT Strategy Committee", "–", "11 / 4", "No gap > 120 days"],
              ["Governance", "Whistle-blower / POSH cases", "–", "16 (3 vigil) / 3 resolved", "Policies in place"],
              ["Governance", "Audit qualifications / RBI penalties", "Nil", "Nil", "Three minor BSE fines"]],
             widths=[0.9, 2.5, 0.7, 1.4, 1.55], font=7.5, source=f"{AR26}, ESG section of Corporate Overview, BRSR, Directors’ Report (CSR, POSH, whistle-blower), Report on Corporate Governance; {AR25} for prior-year comparatives where disclosed.")
    pg.h2("Assessment")
    pg.p("As a service business Fedfina’s direct environmental footprint is small, and the 25% cut in emission intensity is mostly an artefact of revenue growth outpacing branch energy use; the more meaningful commitments are Scope 3 monitoring from FY27 and the green-loan products under exploration. The social pillar is where the business model and ESG coincide: secured, regulated credit to underserved households is the company’s purpose, and conduct metrics (CSAT, complaint resolution, transparent auctions) are the right measures. Governance is institutional-grade for a company of this size – bank-promoted, majority-independent board, four rating agencies, joint auditors from FY27 – with the True North exit reducing the private-equity influence that had shaped the company since 2018. ESG risks that could affect value are concentrated in the ‘S’ (collections conduct) and ‘G’ (compliance with rapidly changing regulation) rather than the ‘E’.")
    P.append(pg)

    # ================================================================== CHAPTER 7
    pg = Page("Chapter 7 — SWOT Analysis")
    pg.p("The SWOT below synthesises Chapters 2–6. Each entry is tied to a disclosed figure so that it can be defended with evidence.")
    pg.table(["Strengths (internal)", "Weaknesses (internal)"],
             [["• 60.79% Federal Bank parentage: governance, funding access (₹1,370 crore), brand\n• AA+/Stable from four agencies; 41 lenders; USD 250 mn ECB; CP programme\n• Fully secured book (98.9%); gold LTV 60.9%; top-20 borrowers 0.47%\n• Twin-engine model: gold velocity + mortgage duration; 20–25% customer overlap\n• 757 branches in 17 states; gold AUM/branch ₹16.5 crore and rising\n• Eight-year record: AUM 10x, PAT 9.5x, GNPA always ≤ 2.3%\n• FY26 execution: 8 of 9 Fedfina 2.0 commitments delivered\n• Technology as control: BRE, digital collections 70%, e-NACH 90%, Zero-Trust security",
               "• Cost-to-income stuck at 57–59% for five years; branch-heavy fixed costs\n• RoE 12.6% below mid-teens peers; valuation ≈1.6x book\n• Leverage up to 4.6x; Tier I down to 17.5%; no equity raised since IPO\n• Scale gap: AUM one-eighth of Muthoot, one-third of Manappuram\n• Voluntary attrition 35.85%; 148 unseasoned branches\n• FY25 showed collections lagged growth; ST LAP vintage unproven\n• Geographic concentration: top-5 states 75% of AUM\n• Disclosure inconsistencies (GNPA 1.9% vs 2.2%; DA income definitions; headcount growth)"]],
             widths=[3.525, 3.525], font=8, align_num=False)
    pg.table(["Opportunities (external)", "Threats (external)"],
             [["• Organised gold-loan market > ₹15 lakh crore → ≈ ₹18 lakh crore FY27 (ICRA); NBFC concentration easing\n• Secured MSME-LAP growth 16–18% p.a. to FY28; ₹92 trillion MSME credit gap\n• Household credit/GDP 42% vs 60–76% in peers – structural under-penetration\n• Falling rate cycle (repo 5.25%); CoB 7.83% in Q4 FY26\n• Co-lending demand from banks for PSL gold/MSME assets\n• Higher permitted LTV (85%) on loans ≤ ₹2.5 lakh from April 2026\n• Digital public infrastructure lowering acquisition and underwriting cost\n• Green finance (solar, efficient appliances) and cross-sell to 3.44 lakh customers",
               "• Gold-price correction after +65% in CY2025\n• Banks (82% of gold market) and large NBFCs competing on price; MT LAP yield pressure\n• Gold-lending Directions 2025: LTV maintenance, renewal and credit-assessment rules\n• Interest-rate reversal with 60% floating liabilities\n• Unsecured-credit stress in households spilling into secured products\n• Cyber-attacks on BFSI; DPDP penalties\n• Further regulatory funding shocks (e.g., risk-weight changes) raising CoB\n• Macro or rural slowdown; property-market softness in key states"]],
             widths=[3.525, 3.525], font=8, align_num=False)
    pg.p("Using the SWOT. The matrix supports four strategy pairings. Strength–Opportunity: deploy the AA+ funding franchise and 757-branch base into the growing organised gold and secured-MSME markets, including through co-lending. Strength–Threat: use the 60.9% LTV, short tenor and in-house collections to absorb a gold-price correction better than higher-LTV competitors. Weakness–Opportunity: let falling funding costs and maturing branches lift RoE from 12.6% towards the Q4 FY26 run-rate of 14% without further leverage. Weakness–Threat: the combination of rising leverage and a possible rate or gold reversal is the scenario the Board’s capital planning must address first.")
    pg.p("Strategic reading. The strengths and opportunities align closely (secured products in growing, under-penetrated markets with a strong funding franchise), while the weaknesses and threats cluster around the same two variables – operating leverage and gold-price/credit cyclicality. The strategic task is therefore to convert branch capacity into productivity (addressing the cost ratio and RoE) while keeping credit cost and leverage within the limits that preserve the AA+ rating; the recommendations in this chapter follow from that reading.")
    P.append(pg)

    # ------------------------------------------------------------------ 72 Positives
    pg = Page("Investment Case: Key Positives")
    pg.p("Drawing the analysis together, the following are the strongest evidence-based arguments in favour of Fedfina’s fundamental quality. Each is stated with the number that supports it and the page where it is analysed.")
    pg.table(["#", "Positive", "Evidence", "Why it matters"],
             [["1", "Consistent long-term compounding", "AUM ₹2,019 cr → ₹20,153 cr and PAT ₹36 cr → ₹344 cr over FY19–FY26; BVPS 21.6% CAGR; no dividend, all profit reinvested", "Demonstrates a repeatable growth engine across rate, pandemic and credit cycles"],
              ["2", "Fully secured, granular book", "98.9% secured; gold LTV 60.9%; average tickets ₹2.7 lakh (gold) and ₹16.1 lakh (ST LAP); top-20 borrowers 0.47%", "Low loss-given-default; no single-name risk; resilient to unsecured-credit stress"],
              ["3", "Credible turnaround executed within one year", "Credit cost 1.8% → 0.8%; Stage 2+3 7.4% → 3.5%; PAT +53%; 8 of 9 FY25 commitments delivered", "Management does what it says; problems are disclosed and fixed"],
              ["4", "Improving earnings quality", "Interest on loans 93% of interest income; DA income share of PBT down sharply; off-book AUM 25% → 12%", "Profits are recurring, not front-loaded"],
              ["5", "Widening spread in a competitive market", "Spread 8.6% (best in five years); NIM 8.8%; Q4 CoB 7.83%", "Pricing power in gold plus funding-cost advantage from parentage and ratings"],
              ["6", "Strong funding franchise", "AA+/Stable × 4; 41 lenders; ECB 17%; CP 9%; fixed-rate 40%; positive ALM gap in every bucket to one year", "Liquidity is the existential risk for NBFCs; Fedfina’s profile is conservative"],
              ["7", "Adequate capital with headroom", "CRAR 22.4% vs 15% floor; Tier I 17.5%; ICAAP; ₹18,000 crore borrowing limit 75% used", "Supports 20–25% growth for several years without dilution if RoE holds"],
              ["8", "Operating leverage ahead", "148 young branches; gold AUM/branch +₹4.4 crore in a year; C/I 57.2% with growth costs expensed", "Cost ratio should fall as cohorts mature, lifting RoA and RoE"],
              ["9", "Institutional governance", "Bank promoter 60.8%; 5 independent directors; four rating agencies; joint auditors from FY27; clean regulatory record", "Reduces governance discount typical of mid-sized NBFCs"],
              ["10", "Valuation does not assume success", "≈1.6x book, ≈13.5x FY26 EPS at 31 March 2026; below IPO price", "Improvement in RoE towards 14% (Q4 run-rate) is not priced in"]],
             widths=[0.3, 1.6, 3.0, 2.15], font=8)
    pg.kpis([("≈34%", "AUM CAGR FY22–FY26"), ("98.9%", "Secured share of AUM"), ("8.6%", "Spread FY26 (5-yr high)"), ("22.4%", "CRAR vs 15% floor"), ("+53%", "PAT growth FY26"), ("≈1.6x", "Price / book, 31 Mar 2026")], cols=6)
    pg.p("Context against the gold-loan leaders. Fedfina’s capital position (CRAR 22.4%) compares with 20.75% at Muthoot Finance and 21.3% at Manappuram Finance at 31 March 2026, and its FY26 PAT growth of 53% sits between Muthoot’s 98% consolidated increase and Manappuram’s 17.5% decline, which was caused by provisions on non-gold books – an illustration of the value of Fedfina’s decision to exit unsecured lending. The scale gap is large (Muthoot’s standalone AUM is about eight times Fedfina’s), but the quality indicators that matter for sustainability – secured mix, LTV, credit cost and funding diversity – are at or above the standards set by the larger peers.")
    pg.p("Together these positives support the working hypothesis that a higher secured share combined with stronger operating discipline supports sustainable profitability. The next page presents the counter-case – the factors that must be watched – with equal rigour.")
    P.append(pg)

    # ------------------------------------------------------------------ 73 Watch factors
    pg = Page("Investment Case: Factors to Watch")
    pg.p("A balanced fundamental analysis must give equal weight to the evidence against the thesis. The following factors could undermine the positives on the previous page; each is paired with the indicator that would reveal it first.")
    pg.table(["#", "Watch factor", "Evidence of concern", "Leading indicator to monitor"],
             [["1", "Gold-price dependence", "Gold AUM +76% with tonnage +12%: roughly five-sixths of growth was price/LTV-driven; gold now 51% of AUM and 47% of assets", "Gold price; portfolio LTV; auction counts; tonnage growth vs 10–12% target"],
              ["2", "Unseasoned ST LAP and branch cohorts", "₹904 crore of FY26 ST LAP disbursements and 148 branches less than a year old; small-mortgage delinquency peaks 18–36 months out", "30+/90+ dpd on FY26 vintage; Stage 2 ratio; branch break-even timelines"],
              ["3", "Leverage creep", "D/E 3.6x → 4.0x → 4.6x; Tier I 18.9% → 17.5%; no equity since 2023", "D/E above 5x; Tier I below 15%; rating-agency commentary"],
              ["4", "Credit cost normalisation incomplete", "Additions to impaired loans +16% (₹227 crore); improvement partly via ₹88 crore write-offs and ₹105 crore ARC sales; PCR down to 32%", "Gross slippage ratio; recoveries from ARC pools; PCR trend"],
              ["5", "Cost ratio inertia", "C/I 58.6% → 57.2% over four years despite 2.5x AUM; employee cost +13.7%", "C/I below 55%; opex/average assets below 3.5%"],
              ["6", "Regulatory change in gold lending", "Directions effective 1 Apr 2026 change LTV maintenance, renewals and credit assessment; FY25 already saw volume effects from earlier changes", "Gold disbursement run-rate in H1 FY27; renewal rates; compliance cost"],
              ["7", "Non-interest income erosion", "Fee and other income −24%; distribution income from Federal Bank −31%; FVOCI gains −30%", "Fee income trend; co-lending servicing income"],
              ["8", "Yield compression in MT LAP", "Origination yield 12.0%; ‘broader industry yield pressures’ acknowledged; disbursements −5%", "Blended yield; balance-transfer attrition; MT LAP growth vs AUM"],
              ["9", "Disclosure consistency", "GNPA 1.9% vs 2.2%; DA income ₹7.4 crore vs ₹102 crore; headcount +6.3% vs +16%; AUM–loan bridge not published", "Reconciliations in FY27 report; investor-presentation detail"],
              ["10", "Shareholder and leadership transition", "True North exit; new CS; MD&CEO in second full year; small free float", "Board stability; promoter intent; institutional holding trend"]],
             widths=[0.3, 1.5, 3.1, 2.15], font=8)
    pg.kpis([("51.4%", "Gold share of AUM"), ("4.6x", "Debt / equity"), ("32.3%", "Provision coverage"), ("35.85%", "Voluntary attrition"), ("₹227 cr", "Additions to impaired loans (+16%)"), ("57.2%", "Cost-to-income")], cols=6)
    pg.p("Signals that would change the assessment. The view taken in this report would weaken if any of the following appeared in FY27 disclosures: credit cost back above 1.5% (the FY25 level was 1.8%); Stage 2 loans above 4% of the amortised-cost book (5.1% at the FY25 peak); gold tonnage growth below the 10–12% target with AUM still growing on price; D/E above 5x without a capital plan; or a cost-to-income ratio that rises rather than falls as the 148 FY26 branches complete their first full year. Conversely, a reported fall in C/I below 55% with credit cost under 1% would confirm that operating leverage has arrived and that the FY26 RoE of 12.6% understates normalised earning power.")
    pg.p("Weighing the two pages. None of the watch factors is, on the FY26 evidence, a thesis-breaker; the first four are consequences of the strategy’s success and will be resolved by time and data rather than by further management action. The appropriate stance is conditional confidence: the fundamentals are sound and improving, and FY27 will show whether the improvement is durable.")
    P.append(pg)

    # ------------------------------------------------------------------ 74 Scenarios
    pg = Page("Scenario Analysis")
    pg.p("Scenario analysis asks how the key profit drivers would behave under different external conditions. The scenarios below are illustrative and author-constructed; they use FY26 reported figures as the base and apply the sensitivities derived in Chapters 5 and 6. They are not forecasts and do not represent company guidance.")
    pg.table(["Driver (FY26 base)", "Base case: steady state", "Upside: tailwinds persist", "Downside: gold correction + credit stress"],
             [["Macro and rates", "GDP ≈ 6.6–7.2%; repo stable near 5.25%", "Further 25–50 bp easing; strong rural demand", "Rates rise 100 bp; rural stress returns"],
              ["Gold price", "Flat to modestly higher", "Continues to rise; tonnage +12%", "Falls 20–25% within a year"],
              ["AUM growth (27.5%)", "20–25% (Board target)", "25–30%", "10–15%; gold disbursements slow; mortgage steady"],
              ["Spread / NIM (8.6% / 8.8%)", "Stable 8.3–8.6%", "Widens 20–30 bp as CoB falls", "Compresses 50–80 bp on floating liabilities"],
              ["Cost-to-income (57.2%)", "Drifts to 54–55% as branches mature", "Below 53% with operating leverage", "Rises above 60% on lower income"],
              ["Credit cost (0.8%)", "0.8–1.0%", "0.6–0.8%", "1.5–2.0% (FY25-type ST LAP stress plus gold auction losses)"],
              ["RoA (2.4%)", "2.3–2.5%", "2.6–2.8% (Q4 FY26 run-rate 2.6%)", "1.3–1.6%"],
              ["RoE (12.6%)", "13–14%", "15–16%", "7–9%"],
              ["Capital (CRAR 22.4%)", "Stable; Tier I slowly declines with growth", "Comfortable; possible equity raise for growth", "Falls but stays > 18%; growth slows to preserve capital"],
              ["Earnings signal", "PAT grows roughly in line with AUM", "PAT grows faster than AUM", "PAT falls 30–45% from FY26 (derived from RoA range on a flat balance sheet)"]],
             widths=[1.6, 1.75, 1.75, 1.95], font=8)
    pg.h2("Discussion")
    pg.p("The base case corresponds to the Board’s 20–25% sustainable-growth target with the FY26 margin and credit-cost structure maintained, and yields an RoE in the 13–14% range – roughly the Q4 FY26 exit rate. The upside case requires the FY26 tailwinds (falling rates, rising gold, strong rural demand) to continue and operating leverage to show through; it would lift RoE into the mid-teens seen in FY23 and justify a re-rating of the shares. The downside case combines the two risks the matrix rates highest – a gold-price correction and renewed small-ticket mortgage stress – with a rate reversal. Even in that scenario the derived RoA stays positive and CRAR remains above the regulatory floor by a wide margin, because of the secured book, the short gold tenor and the 22.4% starting capital; the damage is to earnings and valuation rather than solvency.")
    pg.p("The asymmetry matters for the hypothesis: the structural changes of FY25–FY26 (secured mix, in-house collections, BRE underwriting, funding diversification) lower the probability and severity of the downside without capping the upside. That is the essence of the argument that profitability has become more sustainable, and it is what distinguishes the FY26 recovery from a purely cyclical rebound.")
    P.append(pg)

    # ------------------------------------------------------------------ 75 Balanced scorecard
    pg = Page("Balanced Scorecard Assessment")
    pg.p("The balanced scorecard evaluates performance across four perspectives rather than financial results alone. Each perspective is scored on the disclosed FY26 evidence relative to the company’s own commitments and sector norms (author’s qualitative scores: Strong / Adequate / Needs improvement).")
    pg.table(["Perspective", "Objective", "FY26 measure", "Result", "Score"],
             [["Financial", "Grow profitably", "AUM +27.5%; PAT +53%; RoA 2.44%; RoE 12.62%", "Above FY25 and FY24 in absolute terms; RoE below FY23 peak", "Strong"],
              ["Financial", "Control credit cost", "0.8% vs sub-1% commitment", "Delivered; sustainability to be proven on new vintage", "Strong"],
              ["Financial", "Improve efficiency", "C/I 57.2% (−0.35 pp); opex/assets 5.1%", "Marginal improvement; growth investment continues", "Needs improvement"],
              ["Financial", "Maintain capital and funding", "CRAR 22.4%; D/E 4.6x; 41 lenders; AA+ × 4", "Strong funding; leverage rising", "Adequate"],
              ["Customer", "Serve emerging Bharat", "3.44 lakh customers; 757 branches; 455 customers/branch", "Reach expanding; inclusion mandate met", "Strong"],
              ["Customer", "Service quality", "CSAT 85%; 100% TAT resolution; Google 4.58/5; TAT 10/15 days", "Good and improving", "Strong"],
              ["Customer", "Fair conduct", "Auctions 4,633 with 92% dues realised; ombudsman; fair-practices code", "No adverse action disclosed", "Adequate"],
              ["Internal process", "Underwriting discipline", "BRE live; 76% mortgage AUM CIBIL >700; 75% in-house sourcing", "Structural upgrade", "Strong"],
              ["Internal process", "Collections", "In-house 1.8x; agency 0.4x; Stage 3 recoveries 2.2x; 70% digital", "Rebuilt after FY25 failure", "Strong"],
              ["Internal process", "Risk and compliance", "Nil audit qualifications; frauds ₹110 lakh; 3 minor BSE fines", "Clean, with procedural lapses", "Adequate"],
              ["Learning and growth", "People capability", "735 hires; 7.44 training hrs; Gurukul/DREAM; attrition 35.85%", "Investment visible; attrition high", "Needs improvement"],
              ["Learning and growth", "Technology and innovation", "LOS–LMS–CRM integration; Credit GPT; Fedfina Lite; 89 start-ups screened", "Ahead of mid-sized peers", "Strong"],
              ["Learning and growth", "Diversity and ESG", "Women 16.4% (+0.7 pp); emission intensity −25%; CSR ₹5.84 crore", "Progressing against targets", "Adequate"]],
             widths=[1.1, 1.3, 2.3, 1.6, 0.75], font=7.5)
    pg.p("Change versus FY25. On the same criteria the FY25 report would have scored ‘Needs improvement’ on credit cost (1.8%), collections (the stated root cause of the stress), efficiency (C/I 57.6%) and people (attrition and a leadership change), with growth (AUM +31%) and funding (AA+, 41 lenders) the main strengths. The movement of two internal-process objectives and one financial objective from ‘Needs improvement’ to ‘Strong’ within one year is the scorecard expression of the turnaround discussed in Chapters 3 and 5.")
    pg.p("Overall. Nine of thirteen objectives score Strong or Adequate on the evidence; the two ‘Needs improvement’ items – cost efficiency and attrition – are related (a field-heavy, high-turnover workforce is expensive) and are the areas where the recommendations on the following pages concentrate. The scorecard supports the conclusion that FY26 performance was broad-based rather than driven by a single favourable line item.")
    P.append(pg)

    # ------------------------------------------------------------------ 76 Recos growth
    pg = Page("Recommendations: Growth and Operating Efficiency")
    pg.p("The recommendations in this and the following two pages are addressed primarily to management and the Board, with implications for investors and lenders noted. They follow directly from the evidence in Chapters 2–7 and are framed so that progress can be measured from future annual reports.")
    pg.table(["#", "Recommendation", "Rationale (evidence)", "Measurable indicator"],
             [["G1", "Prioritise productivity of the FY25–FY26 branch cohorts over further network additions in FY27", "148 branches opened in FY26 and 73 in FY25; gold AUM/branch ₹16.5 crore vs mature-branch potential; C/I stuck at 57%", "Gold AUM per branch > ₹20 crore; C/I < 55% by FY28"],
              ["G2", "Set an explicit tonnage-growth disclosure alongside gold AUM", "76% AUM growth vs 12% tonnage; management already targets 10–12% tonnage CAGR", "Tonnage, customers and AUM per gram reported quarterly"],
              ["G3", "Rebuild ST LAP volumes gradually, gated by vintage performance", "Disbursements ₹904 crore vs ₹1,475 crore in FY24; new book better than old but unseasoned", "30+ dpd on each quarterly vintage below the FY24 cohort before scaling"],
              ["G4", "Use the 70 co-located ‘Vyapaar’ branches as the template for mortgage expansion", "20–25% customer overlap; co-location reduces operating costs", "Share of ST LAP sourced from gold-customer base; cost per branch"],
              ["G5", "Expand co-lending in gold and MSME LAP as the preferred capital-light channel", "Co-lending AUM ₹2,433 crore (2.2x); DA income front-loaded; D/E 4.6x", "Off-book AUM share stable at 12–15% with co-lending > DA"],
              ["G6", "Defend MT LAP economics through service rather than price", "Origination yield 12.0%; industry yield pressure; 81% CIBIL >700", "MT LAP blended yield ≥ 12%; attrition from balance transfer tracked"],
              ["G7", "Pilot the green-finance products already under exploration", "Solar and efficient-appliance loans mentioned in ESG section; secured by asset", "Pilot AUM and loss experience disclosed"],
              ["G8", "Deepen cross-sell analytics across the 3.44 lakh customer base", "Twin-engine overlap; integrated LOS–LMS–CRM now in place", "Products per customer; cross-sell share of disbursements"]],
             widths=[0.4, 2.0, 2.65, 2.0], font=8)
    pg.h2("FY26 baselines against which the indicators can be tracked")
    pg.kpis([("₹16.5 cr", "Gold AUM per branch"), ("57.2%", "Cost-to-income"), ("₹904 cr", "ST LAP + HL disbursements"), ("₹2,433 cr", "Co-lending AUM"), ("70", "Co-located ‘Vyapaar’ branches"), ("3.44 lakh", "Customers")], cols=6)
    pg.p("Sequencing. G1–G3 are FY27 priorities because they protect the credit-cost and efficiency gains on which the thesis depends; G4–G6 build on infrastructure already in place (co-located branches, co-lending partnerships, the integrated LOS–LMS–CRM stack) and can run in parallel; G7–G8 are option-value initiatives whose cost is low and whose benefit is strategic. All eight can be tracked from metrics the company already discloses in its annual report, so progress is verifiable by external readers without access to management.")
    pg.p("For investors and lenders the growth recommendations translate into two monitoring questions: is growth coming from tonnage and new customers rather than gold price, and is the cost ratio finally bending as the branch base matures? Both can be answered from the KPIs the company already publishes.")
    P.append(pg)

    # ------------------------------------------------------------------ 77 Recos risk & governance
    pg = Page("Recommendations: Risk, Capital and Governance")
    pg.table(["#", "Recommendation", "Rationale (evidence)", "Measurable indicator"],
             [["R1", "Publish vintage-wise delinquency curves for ST LAP and gold loans", "FY25 stress was detected late; FY26 new book is ‘better than old’ but data are qualitative", "30+/90+ dpd by origination quarter in investor materials"],
              ["R2", "Set a leverage ceiling and a Tier I floor above regulatory minimums, and disclose them", "D/E 3.6x → 4.6x in two years; Tier I 17.5% (−1.4 pp); growth target 20–25%", "Board-approved D/E cap (e.g., ≤ 5.0x) and Tier I floor (e.g., ≥ 15%) disclosed"],
              ["R3", "Plan the next equity raise before leverage forces it", "RoE 12.6% supports ≈12–13% equity growth vs 20–25% asset growth; shares at ≈1.6x book", "Capital plan in ICAAP; timing linked to RoE and valuation"],
              ["R4", "Maintain the 40% fixed-rate share and lengthen tenor in the 1–3 year bucket", "1–3 year borrowings ₹6,409 crore vs advances ₹1,984 crore; 60% floating", "Fixed share ≥ 40%; 1–3 year cumulative gap narrowing"],
              ["R5", "Disclose gold-price stress tests (e.g., 20% and 30% declines) and LTV distribution", "Gold 51% of AUM; price +65% in CY2025; LTV 60.9% average only", "Share of gold book above 75% LTV; auction-loss sensitivity"],
              ["R6", "Complete the doorstep ‘security box’ roll-out with disclosed custody-loss metrics", "DSGL AUM +108% to ₹1,730 crore; prototype under development", "Custody incidents per 1,000 DSGL loans; insurance claims"],
              ["R7", "Reconcile and standardise key metrics across report sections", "GNPA 1.9% vs 2.2%; DA income ₹7.4 crore vs ₹102 crore; headcount growth 6.3% vs 16%; no AUM–loan bridge", "Single definitions page and AUM reconciliation in the annual report"],
              ["R8", "Strengthen Board renewal planning after True North’s exit", "One nominee seat vacated; CS changed; MD&CEO in second year", "Board skills matrix; succession plan disclosed"],
              ["R9", "Prepare an impact assessment of the gold-lending Directions and disclose it", "Rules effective 1 April 2026 affect LTV maintenance, renewals, credit assessment", "Management commentary on volume and process effects in H1 FY27"],
              ["R10", "Keep credit-cost guidance explicit and report it quarterly", "Sub-1% commitment met at 0.8%; FY25 showed how quickly it can move", "Credit cost on average assets each quarter with stage-wise drivers"]],
             widths=[0.4, 2.0, 2.65, 2.0], font=8)
    pg.p("Rationale for emphasis on capital. Of all the recommendations, R2 and R3 are the most consequential for shareholders. Fedfina has grown assets at 25–30% a year while equity has grown at 13–15%; arithmetic guarantees that leverage will keep rising until either growth slows, RoE rises or new equity is raised. A clearly communicated leverage policy would reassure rating agencies (whose AA+ ratings underpin the funding cost advantage) and allow the market to price the eventual equity raise rather than fear it.")
    pg.p("Illustrative capital arithmetic (derived). At an RoE of 12.6% with no dividend, equity grows by about 12.6% a year; if assets grow 22.5% (the mid-point of the Board’s target), the debt-to-equity ratio would rise from 4.6x to roughly 5.6x in two years and 6.6x in three, and Tier I would fall towards the mid-teens – still above the regulatory floor but below the level that supports an AA+ rating comfortably. A rise in RoE to 15% would slow this trajectory but not reverse it. This is why a pre-emptive, moderately sized equity raise is the recommended route.")
    pg.p("Rationale for emphasis on disclosure. The company’s disclosure is already better than that of most mid-sized NBFCs; the inconsistencies noted are small, but at a listed company they invite questions that cost management credibility. A definitions page and a quarterly vintage table would close the gap at negligible cost.")
    P.append(pg)

    # ------------------------------------------------------------------ 78 Recos sustainability
    pg = Page("Recommendations: Sustainability, People and Stakeholders")
    pg.table(["#", "Recommendation", "Rationale (evidence)", "Measurable indicator"],
             [["S1", "Target a reduction in voluntary attrition, especially in collections and credit roles", "35.85% voluntary turnover; collections capability was the root cause of FY25 stress", "Attrition by function; tenure of collections staff"],
              ["S2", "Link variable pay for branch and sales staff to vintage asset quality, not only disbursement", "In-house sourcing 75%; BRE reduces discretion but incentives still shape behaviour", "Share of variable pay tied to 12-month portfolio quality"],
              ["S3", "Accelerate the women-in-senior-management target and extend it to branch leadership", "Women 16.4% of workforce; ≥22% senior-management target by FY28", "Annual progress against target; women branch managers"],
              ["S4", "Publish Scope 3 (financed emissions) methodology when monitoring begins in FY27", "Roadmap announced; lenders increasingly asked for financed-emission data", "Scope 3 baseline disclosed in FY27 BRSR"],
              ["S5", "Scale financial-literacy programmes in catchments of new branches", "148 new branches in Tier 2–4 markets; many first-time formal borrowers", "Participants reached; linked account openings"],
              ["S6", "Maintain CSR focus areas (child nutrition, women’s skills) with outcome reporting", "CSR ₹5.84 crore; 496 children (Cuddles), 700 women (Samarthanam)", "Outcome metrics per programme in Directors’ Report"],
              ["S7", "Formalise a customer-conduct dashboard for gold auctions and SARFAESI actions", "4,633 auctions; 92% realisation; conduct-sensitive activities", "Auctions per 1,000 loans; complaints per 1,000 customers; surplus refund timeliness"],
              ["S8", "Continue the ‘Startup Friday’ model with disclosed outcomes", "89 evaluated, 6 onboarded, 8 in proof-of-concept", "Solutions deployed; measured productivity or risk benefit"]],
             widths=[0.4, 2.0, 2.65, 2.0], font=8)
    pg.p("Why people metrics belong in a fundamental analysis. Employee benefits are the largest operating expense (₹{:,.0f} crore in FY26, {:.0f}% of total operating expenses) and the FY25 episode showed that the quality of field staff in collections determines credit cost directly. Attrition of 35.85% therefore has a measurable financial cost – recruitment, training (7.44 hours per employee), and the productivity lag of new staff in 148 new branches – and reducing it is as much a profitability lever as a social objective.".format(P26["emp"]/100, P26["emp"]/(P26["emp"]+P26["dep"]+P26["other_exp"])*100))
    pg.h2("Recommendations for different readers")
    pg.bullets([
        "Equity investors:: treat FY27 as the confirmation year. The thesis is supported if credit cost stays below 1%, Stage 2 remains near 2%, C/I begins to fall and D/E stays below 5x; it weakens if gold-price support fades and tonnage growth is below 10%.",
        "Lenders and debenture holders:: the structural-liquidity profile, 22.4% CRAR, fully hedged ECBs and bank parentage support the AA+ ratings; monitor the 1–3 year funding gap and Tier I trend.",
        "Management:: the FY26 results earn the right to grow; the recommendations above are about making the growth durable – productivity before footprint, capital policy before necessity, disclosure before doubt.",
        "Students and researchers:: Fedfina is a model case for studying how an NBFC’s profitability is determined by collections infrastructure, funding mix and product selection, and how a company communicates a reset and recovery across consecutive annual reports.",
    ])
    P.append(pg)

    # ================================================================== CHAPTER 8
    pg = Page("Chapter 8 — Summary of Key Findings")
    pg.p("The study set out to evaluate the fundamental strength and sustainability of Fedbank Financial Services Limited through an Economy–Industry–Company analysis of its FY24, FY25 and FY26 annual reports. The principal findings are:")
    pg.table(["Area", "Key finding", "Supporting figures"],
             [["Sector", "The NBFC sector (≈ ₹45 trillion assets, growing 15–17%) is shifting decisively to secured retail lending; the organised gold-loan market crossed ₹15 lakh crore and secured MSME LAP is projected to grow 16–18% a year; regulation (SBR, gold-lending Directions 2025) is tightening but clarifying", "Chapter 2 tables; ICRA, CRISIL, RBI data as cited in AR26"],
              ["Company", "Fedfina is a bank-promoted (60.79%), AA+-rated, 757-branch secured lender that completed a strategic reset (Fedfina 2.0) within one year, delivering eight of nine FY25 commitments", "Commitments vs delivery table; shareholding; ratings"],
              ["Products", "The mix moved from mortgage-led to gold-led (gold 32.6% → 51.4% of AUM) and the unsecured book was fully exited (secured AUM 98.9%); ST LAP was rebuilt on system-driven underwriting", "Product mix FY24–FY26; note 8 secured/unsecured split"],
              ["Growth", "AUM compounded at 39% (FY19–FY26) and 34% (FY22–FY26); FY26 AUM ₹20,153 crore (+27.5%); disbursements ₹31,410 crore (+67%)", "Eight-year series; Directors’ Reports"],
              ["Profitability", "PAT ₹343.6 crore (+53%); RoA 2.44%; RoE 12.62%; spread 8.6% (five-year high); roughly two-thirds of the FY26 profit improvement came from lower credit cost and one-third from NII growth net of costs", "Income statement; DuPont decomposition"],
              ["Efficiency", "Cost-to-income improved only marginally to 57.2% as 148 branches and 735 employees were added; operating leverage is deferred, not absent", "Directors’ Reports; note 34"],
              ["Asset quality", "GNPA 1.9% / NNPA 1.3%; Stage 2+3 share halved to 3.5%; credit cost 0.8% after ₹88 crore write-offs and ₹105 crore ARC sales; additions to impaired loans still rising", "Notes 8, 32, 48"],
              ["Capital and funding", "CRAR 22.4% (Tier I 17.5%); D/E up to 4.6x; 41 lenders; ECB 17%; fixed-rate 40%; positive ALM gap to one year; cash ₹1,340 crore", "Notes 16–18, 48"],
              ["Risk", "Highest-impact risks (gold price, cyber, liquidity) are well mitigated; rising-trend risks (gold dependence, leverage, young branches, custody) are consequences of success", "Risk matrix"],
              ["Governance and ESG", "Institutional-grade governance; clean regulatory record; True North exit; ESG focus on social conduct and emerging Scope 3 reporting", "CG report; BRSR"],
              ["Valuation", "≈1.6x book and ≈13.5x earnings at 31 March 2026 – a discount consistent with 12.6% RoE and the FY25 reset", "Market cap ₹4,642 crore"]],
             widths=[1.2, 4.1, 1.75], font=8)
    pg.p("Relative to the three objectives of the study – to analyse the sector, to evaluate the company’s financial performance and risk profile across five years, and to test whether FY26’s improvement is structural – the evidence is sufficient on the first two and conditional on the third: the structural changes are documented, but one year of post-reset data cannot by itself establish durability.")
    pg.p("The overall conclusion of the findings is that Fedfina’s fundamentals are sound and improving, that the FY26 recovery rests on structural as well as cyclical factors, and that the key uncertainties – gold price, unseasoned vintages and leverage – are identifiable and measurable from the company’s own disclosures.")
    P.append(pg)

    # ------------------------------------------------------------------ 80 Hypothesis testing
    pg = Page("Hypothesis Testing and Answers to Research Questions")
    pg.p("Chapter 1 proposed a working hypothesis (H1) that a higher secured share of AUM combined with stronger operating discipline supports sustainable profitability, against the null (H0) that FY26’s improvement is primarily cyclical. Four tests were specified; the results follow.")
    pg.table(["Test", "Criterion", "Evidence", "Result"],
             [["(a) Core income growth", "NII growth should exceed total revenue growth", "NII +15% vs revenue +7%; interest on loans +13% and 93% of interest income; DA income down", "Met"],
              ["(b) Credit cost", "Credit cost should fall on a like-for-like basis, not only via write-offs", "Credit cost 1.8% → 0.8%; Stage 2 5.1% → 1.9%; cure rates up; but additions to impaired loans +16% and improvement aided by ₹193 crore of write-offs/ARC sales", "Met with qualification"],
              ["(c) Stress share of book", "Stage 2 + Stage 3 share should decline", "7.4% → 3.5% of amortised-cost loans", "Met"],
              ["(d) Returns vs leverage", "RoA and RoE should rise without disproportionate leverage increase", "RoA +0.62 pp; RoE +3.2 pp; average leverage 5.26x → 5.51x (+5%) – RoE gain mostly from RoA", "Met"],
              ["Price vs tonnage (supplementary)", "Growth should not depend solely on gold price", "Tonnage +12% vs gold AUM +76%: majority of gold growth is price/LTV-driven", "Partly cyclical"],
              ["Rate cycle (supplementary)", "Spread gain should not depend solely on falling rates", "CoB −90 bp but yield −40 bp; spread +40 bp; fixed-rate share raised to 40%", "Partly cyclical, partly structural"]],
             widths=[1.5, 1.9, 2.75, 0.9], font=8)
    pg.p("Verdict. H1 is accepted with qualifications. The structural components – a fully secured mix, system-driven underwriting, in-house collections, diversified and partly fixed-rate funding – are real and documented, and three of four primary tests are met cleanly. The qualifications are that gold-price appreciation and falling interest rates contributed materially to FY26 growth and margin, and that part of the asset-quality improvement came from crystallising old losses. H0 is rejected in its strong form (the improvement is not primarily cyclical) but retains partial force: a reversal of the gold price or rate cycle would reduce, though on the evidence not eliminate, the profitability gains.")
    pg.h2("Answers to the research questions")
    pg.bullets([
        "RQ1 – Growth and profitability:: Growth has been accompanied by improved profitability over the cycle (PAT CAGR ≈ AUM CAGR over FY22–FY26) with one reset year; FY26 RoA of 2.44% equals the FY24 peak and earnings quality is higher.",
        "RQ2 – Risk profile:: Yes – the risk profile is stronger: secured share 98.9%, Stage 2+3 halved, gold LTV 60.9%, concentration negligible; the residual risks are market (gold) and vintage seasoning rather than unsecured default.",
        "RQ3 – Capital and funding:: Adequate for the 20–25% target in the medium term (CRAR 22.4%, 41 lenders, positive short-term ALM gap), but leverage of 4.6x and Tier I of 17.5% imply that equity will be needed within the planning horizon if RoE stays near 13%.",
        "RQ4 – External risks:: Gold-price correction, the April 2026 gold-lending Directions, bank competition, rate reversal and cyber risk are the principal external risks; mitigation is credible on each, strongest for liquidity and currency and least tested for gold price.",
    ])
    P.append(pg)

    # ------------------------------------------------------------------ 81 Conclusion
    pg = Page("Conclusion")
    pg.p("Fedbank Financial Services Limited entered the study period as a fast-growing, recently listed, mortgage-led NBFC with a meaningful unsecured book; it ends it as a fully secured, gold-led, bank-promoted lender with a rebuilt mortgage franchise, a diversified liability profile and a profit base 40% higher than at the IPO. Between those two points lies FY25, a year in which the company discovered that its collections infrastructure had not kept pace with growth, absorbed the cost of that discovery through provisions and write-offs, changed its leadership, and redesigned its operating model. The FY26 annual report shows the results: AUM ₹20,153 crore, PAT ₹343.6 crore, RoA 2.44%, RoE 12.62%, GNPA 1.9%, credit cost 0.8%, CRAR 22.4%.")
    pg.p("The fundamental analysis supports three conclusions. First, the business model is sound. Gold loans and loans against property are the two most natural forms of secured credit for India’s self-employed and MSME households; both markets are large, growing and under-penetrated; and the twin-engine combination provides diversification of tenor, yield and risk that single-product lenders lack. Second, management execution in FY26 was credible: commitments made in FY25 were delivered, costs of the transition were disclosed, and the operating changes – in-house sourcing and collections, rule-based underwriting, funding diversification, fixed-rate hedging – are structural rather than cosmetic. Third, the sustainability of the recovery is probable but not yet proven. FY26 benefited from a 65% rise in gold prices, a 125 bp fall in policy rates and the write-off or sale of old problem loans; the FY26 vintages of small-ticket LAP and the 148 new branches have yet to season; and leverage has risen to 4.6x. The hypothesis that secured mix plus operating discipline supports sustainable profitability is therefore accepted with qualifications.")
    pg.p("For the sector, Fedfina’s experience illustrates a general lesson: in retail lending, the binding constraint on growth is not demand but the lender’s capacity to underwrite, collect and fund – and that capacity must be built ahead of volume, not after it. For the company, the task for FY27 is to convert capacity into productivity: to let young branches mature, to prove the new mortgage vintages, to grow gold tonnage rather than rely on price, and to set a capital policy before leverage sets it for them. For the analyst, the company’s disclosures are rich enough to track each of these variables, which is itself a mark of quality.")
    pg.p("On the evidence of three annual reports and the broader sector data, Fedbank Financial Services Limited is a fundamentally sound, well-governed and improving secured lender whose principal risks are the mirror image of its recent success. Its investment merit depends less on whether the FY26 numbers are good – they are – than on whether they can be repeated through a less favourable gold-price and interest-rate environment. The structural changes documented in this report make that outcome more likely than it was two years ago.")
    pg.kpis([("10x", "AUM growth FY19–FY26"), ("98.9%", "Secured AUM"), ("0.8%", "Credit cost"), ("22.4%", "CRAR"), ("AA+", "Rating × 4 agencies"), ("4.6x", "Leverage – the watch metric")], cols=6)
    P.append(pg)

    # ------------------------------------------------------------------ 82 Limitations
    pg = Page("Limitations of the Study")
    pg.p("The findings should be read subject to the following limitations, which extend the methodological limitations noted in Chapter 1.")
    pg.bullets([
        "Secondary data only:: The study relies on published annual reports and publicly cited sector data. No access was available to management, branch operations, borrower files, bureau data or the company’s investor presentations and quarterly results, which would allow vintage and quarterly analysis.",
        "Reporting-basis changes:: The FY26 report restates yield, cost of borrowings and spread for prior years; GNPA appears as both 1.9% and 2.2%; DA income appears as ₹7.4 crore and ₹102.0 crore under different definitions; headcount growth is described as 6.3% while disclosed numbers imply 16%. The report presents both figures where they differ and does not adjudicate beyond noting the likely cause.",
        "AUM reconciliation:: AUM (₹20,153 crore) and on-book gross loans (₹14,505 crore) cannot be fully reconciled from public data because the composition of off-book AUM (co-lending partner share, assigned pools, other managed assets) is not published in full.",
        "Averages and derived ratios:: Ratios derived in this report use simple opening/closing averages and may differ slightly from company methodology (e.g., RoA 2.28% derived vs 2.44% reported). Sensitivities in Chapters 5–7 are arithmetic illustrations, not models.",
        "Peer comparison:: Peer data are drawn from results coverage of FY26 announcements, differ in basis (standalone vs consolidated) and were not analysed at statement level; the comparison indicates scale, not relative quality.",
        "Market data:: Only the single market-capitalisation figure disclosed in the annual report (31 March 2026) is used; price history, trading volumes and multiples over time were outside scope, so valuation observations are dated and illustrative.",
        "Qualitative judgements:: Likelihood/impact ratings in the risk matrix, scorecard scores and scenario parameters are the author’s judgements and would differ between analysts.",
        "Time boundary:: The analysis stops at the FY26 annual report (financial statements approved 28 April 2026; Directors’ Report dated 25 August 2026). Events thereafter – including the first quarters under the gold-lending Directions and any capital-raising – are not reflected.",
        "Sector data provenance:: Industry statistics are reproduced as cited by the company (ICRA, CRISIL, MoSPI, World Gold Council, Economic Survey) and from RBI directions; they were not independently re-sourced from the original publications except where noted.",
        "Scope exclusions:: Federal Bank’s own financial condition, the detailed terms of individual borrowing facilities, tax positions and litigation (beyond disclosed penalties) were not analysed.",
    ])
    pg.p("None of these limitations alters the direction of the findings, but several – especially the absence of vintage data and the AUM reconciliation – limit the precision with which the sustainability of FY26 asset quality can be judged. They also define the agenda for a follow-up study after the FY27 results.")
    pg.h2("Suggested extensions for future research")
    pg.p("A follow-up study could (i) extend the series to FY27 to test whether credit cost stayed below 1% and cost-to-income fell as the FY25–FY26 branch cohorts matured; (ii) use quarterly investor presentations to construct vintage curves for the ST LAP and gold books; (iii) benchmark Fedfina at statement level against Muthoot Finance, Manappuram Finance and bank-promoted mortgage NBFCs on yield, cost of funds, opex ratio and credit cost; (iv) analyse the share-price history and multiples against RoE to test the valuation observations made here; and (v) examine the first year of operation under the RBI gold-lending Directions 2025 for its effect on LTV, renewals and disbursement velocity.")
    P.append(pg)

    # ------------------------------------------------------------------ 83 Bibliography
    pg = Page("Bibliography and References")
    pg.h2("Primary sources – company documents")
    pg.bullets([
        "Fedbank Financial Services Limited, Annual Report 2025-26 (31st year), including Corporate Overview, Management Discussion and Analysis, Directors’ Report and annexures, Report on Corporate Governance, Business Responsibility and Sustainability Report, Independent Auditor’s Report and audited Ind AS financial statements with notes (notes 8, 16, 17, 18, 26–34 and 48 cited). Mumbai, 2026.",
        "Fedbank Financial Services Limited, Annual Report 2024-25 (30th year), including Chairman’s and MD&CEO’s messages, ‘Measuring our progress’, branch-expansion data and Directors’ Report. Mumbai, 2025.",
        "Fedbank Financial Services Limited, Annual Report 2023-24 (29th year), including ‘Reflecting on our journey’, key performance indicators FY19–FY24, product overview, MD&A and Directors’ Report. Mumbai, 2024.",
    ], size=8.5)
    pg.h2("Regulatory and official sources")
    pg.bullets([
        "Reserve Bank of India, Reserve Bank of India (Lending Against Gold and Silver Collateral) Directions, 2025, issued June 2025, effective 1 April 2026.",
        "Reserve Bank of India, Non-Banking Financial Companies – Registration, Exemptions and Framework for Scale Based Regulation Directions, 2025; NBFC Internal Ombudsman Directions, 2026; Master Direction on Fraud Risk Management in NBFCs, 2024; Statutory Audit Directions, 2026 (as listed in the company’s secretarial audit report).",
        "Ministry of Statistics and Programme Implementation; Press Information Bureau; Ministry of MSME; Economic Survey 2025-26; IMF World Economic Outlook, April 2026; World Gold Council – statistics as cited in the FY26 Management Discussion and Analysis.",
        "ICRA Limited and CRISIL Ratings – gold-loan market and NBFC AUM projections as cited in the FY26 Management Discussion and Analysis.",
        "EY India, ‘RBI gold loan guidelines 2025: an impact assessment’, February 2026 (summary of the tiered LTV and conduct provisions of the Directions).",
    ], size=8.5)
    pg.h2("Peer and market sources (secondary coverage of exchange filings)")
    pg.bullets([
        "Muthoot Finance Limited – FY26 audited results and Directors’ Report extracts as reported by Investywise (14 May 2026) and IndiaInfoline (Directors’ Report extract, May 2026): consolidated AUM ₹1,81,916 crore, standalone AUM ₹1,62,826 crore, gold-loan AUM ₹1,65,030 crore, standalone PAT ₹10,134 crore, CRAR 20.75%, 7,568 branches.",
        "Manappuram Finance Limited – Q4 FY26 earnings call transcript (Yahoo Finance, 4 May 2026) and results summary (Multibagg, 10 May 2026): consolidated AUM ₹63,798 crore, gold AUM ₹50,953 crore, consolidated PAT ₹993 crore, CRAR 21.3%, cost of borrowing 8.6%.",
    ], size=8.5)
    pg.h2("Academic and methodological references")
    pg.bullets([
        "Porter, M. E., Competitive Strategy: Techniques for Analyzing Industries and Competitors, Free Press, 1980 (Five Forces framework).",
        "Kaplan, R. S. and Norton, D. P., ‘The Balanced Scorecard – Measures that Drive Performance’, Harvard Business Review, 1992.",
        "Koller, T., Goedhart, M. and Wessels, D., Valuation: Measuring and Managing the Value of Companies, 7th edition, Wiley, 2020 (chapter on valuing banks and financial institutions; DuPont decomposition).",
        "Reserve Bank of India, Report on Trend and Progress of Banking in India (annual) – structure and regulation of NBFCs.",
        "Gupta, Rashmi, ‘Summer Internship Report on Fundamental Analysis of IT Sector Companies’, MMS (Finance) project report, DES’s NMITD, University of Mumbai, 2023–25 (structure and format reference).",
    ], size=8.5)
    pg.p("Citation convention. In-text references such as “Directors’ Report FY26” or “note 48” refer to the corresponding section of the annual report for that financial year. Where a figure is computed by the author it is marked ‘derived’; formulae are given in Appendix F.", italic=True, size=9)
    P.append(pg)

    # ================================================================== APPENDICES
    pg = Page("Appendix A — Summarised Balance Sheet (₹ lakh)")
    def r(name, k):
        return [name, f"{B26[k]:,}", f"{B25[k]:,}", f"{B26[k]/B26['total_assets']*100:.2f}%", f"{B25[k]/B25['total_assets']*100:.2f}%"]
    pg.table(["ASSETS", "31 March 2026", "31 March 2025", "% FY26", "% FY25"],
             [r("Cash and cash equivalents", "cash"), r("Bank balances other than cash and cash equivalents", "bank_bal"), r("Derivative financial instruments", "deriv"),
              r("Trade receivables", "trade_rec"), r("Other receivables", "other_rec"), r("Loans", "loans"), r("Investments", "inv"), r("Other financial assets", "other_fin"),
              r("Total financial assets", "total_fin"), r("Current tax assets (net)", "cur_tax"), r("Deferred tax assets (net)", "dta"), r("Property, plant and equipment", "ppe"),
              r("Right-of-use assets", "rou"), r("Capital work-in-progress", "cwip"), r("Intangible assets under development", "intang_dev"), r("Other intangible assets", "intang"),
              r("Other non-financial assets", "other_nonfin"), r("Total non-financial assets", "total_nonfin"), r("TOTAL ASSETS", "total_assets")],
             widths=[3.3, 1.1, 1.1, 0.75, 0.8], font=8)
    pg.table(["LIABILITIES AND EQUITY", "31 March 2026", "31 March 2025", "% FY26", "% FY25"],
             [r("Derivative financial instruments", "deriv_l"), r("Trade payables", "trade_pay"), r("Other payables", "other_pay"), r("Debt securities", "debt_sec"),
              r("Borrowings (other than debt securities)", "borr"), r("Subordinated liabilities", "subdebt"), r("Lease liabilities", "lease"), r("Other financial liabilities", "other_fin_l"),
              r("Total financial liabilities", "total_fin_l"), r("Current tax liabilities (net)", "cur_tax_l"), r("Provisions", "prov"), r("Other non-financial liabilities", "other_nonfin_l"),
              r("Total non-financial liabilities", "total_nonfin_l"), r("Equity share capital", "share_cap"), r("Other equity", "other_eq"), r("TOTAL EQUITY", "equity"),
              ["TOTAL LIABILITIES AND EQUITY", f"{B26['total_assets']:,}", f"{B25['total_assets']:,}", "100.00%", "100.00%"]],
             widths=[3.3, 1.1, 1.1, 0.75, 0.8], font=8, source=f"{AR26}, Balance Sheet as at 31 March 2026 (audited by KKC & Associates LLP). Common-size percentages derived. Sub-totals may differ by ±1 lakh due to rounding in the source.")
    P.append(pg)

    # ------------------------------------------------------------------ 85 Appendix B P&L
    pg = Page("Appendix B — Summarised Statement of Profit and Loss (₹ lakh)")
    def q(name, k):
        return [name, f"{P26[k]:,}", f"{P25[k]:,}", f"{P26[k]/P26['total_rev']*100:.2f}%", f"{P25[k]/P25['total_rev']*100:.2f}%"]
    pg.table(["Particulars", "FY 2025-26", "FY 2024-25", "% of revenue FY26", "% of revenue FY25"],
             [q("Interest income", "int_income"), q("Fee and commission income", "fee_comm"), q("Net gain on fair value changes", "fv_gain"), q("Total revenue from operations", "rev_ops"),
              q("Other income", "other_inc"), q("Total income", "total_rev"), q("Finance costs", "fin_cost"), q("Fee and commission expense", "fee_exp"),
              q("Impairment on financial instruments", "impairment"), q("Employee benefits expense", "emp"), q("Depreciation, amortisation and impairment", "dep"), q("Other expenses", "other_exp"),
              q("Total expenses", "total_exp"), q("Profit before tax", "pbt"), q("Current tax", "cur_tax"), q("Deferred tax (credit)", "def_tax"), q("Profit for the year", "pat"),
              q("Other comprehensive income (net of tax)", "oci"), q("Total comprehensive income", "tci")],
             widths=[3.1, 1.1, 1.1, 0.9, 0.85], font=7.5, source=f"{AR26}, Statement of Profit and Loss for the year ended 31 March 2026.")
    pg.table(["Selected notes (₹ lakh)", "FY26", "FY25", "Selected notes (₹ lakh)", "FY26", "FY25"],
             [["Note 27 – Income from distribution", f"{FEE_BREAKUP['Income from distribution'][0]:,}", f"{FEE_BREAKUP['Income from distribution'][1]:,}", "Note 30 – Interest on borrowings", f"{FIN_COST_BREAKUP['Interest on borrowings (other than debt securities)'][0]:,}", f"{FIN_COST_BREAKUP['Interest on borrowings (other than debt securities)'][1]:,}"],
              ["Note 27 – Loan servicing fee", f"{FEE_BREAKUP['Loan servicing fee'][0]:,}", f"{FEE_BREAKUP['Loan servicing fee'][1]:,}", "Note 30 – Interest on debt securities", f"{FIN_COST_BREAKUP['Interest on debt securities (NCD/CP)'][0]:,}", f"{FIN_COST_BREAKUP['Interest on debt securities (NCD/CP)'][1]:,}"],
              ["Note 27 – Other fees and charges", f"{FEE_BREAKUP['Other fee and charges'][0]:,}", f"{FEE_BREAKUP['Other fee and charges'][1]:,}", "Note 30 – Interest on subordinated liabilities", f"{FIN_COST_BREAKUP['Interest on subordinated liabilities'][0]:,}", f"{FIN_COST_BREAKUP['Interest on subordinated liabilities'][1]:,}"],
              ["Note 32 – Bad debts net of recovery (amortised)", f"{IMPAIRMENT_BREAKUP['Bad debts (net of recovery) – amortised cost loans'][0]:,}", f"{IMPAIRMENT_BREAKUP['Bad debts (net of recovery) – amortised cost loans'][1]:,}", "Note 30 – Interest on lease liability", f"{FIN_COST_BREAKUP['Interest on lease liability'][0]:,}", f"{FIN_COST_BREAKUP['Interest on lease liability'][1]:,}"],
              ["Note 32 – ECL provision (amortised)", f"{IMPAIRMENT_BREAKUP['ECL provision – amortised cost loans'][0]:,}", f"{IMPAIRMENT_BREAKUP['ECL provision – amortised cost loans'][1]:,}", "Note 33 – Salaries and wages", f"{EMP_BREAKUP['Salaries and wages'][0]:,}", f"{EMP_BREAKUP['Salaries and wages'][1]:,}"],
              ["Note 32 – Bad debts net of recovery (FVOCI)", f"{IMPAIRMENT_BREAKUP['Bad debts (net of recovery) – FVOCI loans'][0]:,}", f"{IMPAIRMENT_BREAKUP['Bad debts (net of recovery) – FVOCI loans'][1]:,}", "Note 33 – Share-based payments", f"{EMP_BREAKUP['Share based payments'][0]:,}", f"{EMP_BREAKUP['Share based payments'][1]:,}"],
              ["Note 32 – ECL provision (FVOCI)", f"{IMPAIRMENT_BREAKUP['ECL provision – FVOCI loans'][0]:,}", f"{IMPAIRMENT_BREAKUP['ECL provision – FVOCI loans'][1]:,}", "Note 34 – CSR expenditure", f"{OTHER_EXP_TOP['CSR expenditure'][0]:,}", f"{OTHER_EXP_TOP['CSR expenditure'][1]:,}"]],
             widths=[2.3, 0.7, 0.7, 2.0, 0.7, 0.65], font=7.5, source=f"{AR26}, notes 27, 30, 32, 33 and 34 to the financial statements.")
    nii26, nii25 = P26["int_income"] - P26["fin_cost"], P25["int_income"] - P25["fin_cost"]
    opx26, opx25 = P26["emp"] + P26["dep"] + P26["other_exp"], P25["emp"] + P25["dep"] + P25["other_exp"]
    ppop26, ppop25 = P26["pbt"] + P26["impairment"], P25["pbt"] + P25["impairment"]
    pg.table(["Derived from the statement above", "FY26", "FY25", "Change", "Formula"],
             [["Net interest income (₹ lakh)", f"{nii26:,}", f"{nii25:,}", f"{(nii26/nii25-1)*100:+.1f}%", "Interest income − finance costs"],
              ["Operating expenses (₹ lakh)", f"{opx26:,}", f"{opx25:,}", f"{(opx26/opx25-1)*100:+.1f}%", "Employee + depreciation + other expenses"],
              ["Pre-provision operating profit (₹ lakh)", f"{ppop26:,}", f"{ppop25:,}", f"{(ppop26/ppop25-1)*100:+.1f}%", "PBT + impairment"],
              ["Effective tax rate", f"{(P26['cur_tax']+P26['def_tax'])/P26['pbt']*100:.1f}%", f"{(P25['cur_tax']+P25['def_tax'])/P25['pbt']*100:.1f}%", "", "(Current + deferred tax) / PBT"]],
             widths=[2.5, 1.0, 1.0, 0.8, 1.75], font=7.5, source="Author’s computations on the figures above.")
    P.append(pg)

    # ------------------------------------------------------------------ 86 Appendix C branches by state
    pg = Page("Appendix C — Branch Network by State and Format (31 March 2026)")
    rows = [[s[0], s[1], s[2], s[3], s[4], f"{s[4]/757*100:.1f}%"] for s in BRANCH_STATE] + [["Total", 129, 558, 70, 757, "100.0%"]]
    pg.table(["State / Union Territory", "MSME hubs", "Gold-loan branches", "Co-located (MSME + Gold)", "Total", "Share"], rows,
             widths=[2.4, 0.9, 1.1, 1.3, 0.7, 0.65], font=8, source=f"{AR26}, Directors’ Report – ‘Branch network’ table. Shares derived.")
    pg.table(["Year-end", "FY19", "FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"],
             [["Total branches"] + [str(BRANCHES[y]) for y in YEARS8],
              ["Gold-loan branches", "–", "–"] + [str(BRANCH_GOLD[y]) for y in ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]],
              ["MSME hubs", "–", "–"] + [str(BRANCH_MSME[y]) for y in ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]],
              ["Co-located branches", "–", "–", "–", "–", "–", "–", "–", "70"],
              ["States / UTs", "8", "–", "–", "–", "–", "18", "18", "17"]],
             widths=[1.6, 0.68, 0.68, 0.68, 0.68, 0.68, 0.68, 0.68, 0.69], font=8, source=f"{AR24} journey and KPI pages; {AR25} p.7; {AR26} Directors’ Report. The FY26 state count of 17 follows the Directors’ Report table (Delhi NCR counted once).")
    pg.p("Observations. Gujarat (136) and Maharashtra (141) together host 37% of the network; the southern states of Karnataka, Tamil Nadu, Andhra Pradesh and Telangana a further 38%. The co-located format is concentrated in Gujarat (15), Telangana (11), Karnataka (9) and Maharashtra (8) – the states with the deepest gold-branch presence and therefore the largest cross-sell base. Northern expansion (Delhi NCR, Haryana, Uttar Pradesh, Rajasthan, Punjab, Uttarakhand, Chandigarh) accounts for 166 branches (22%), almost all gold-loan format.")
    pg.p(f"Network growth. The branch count rose from {BRANCHES['FY19']} at 31 March 2019 to {BRANCHES['FY26']} at 31 March 2026, a compound growth rate of about {((BRANCHES['FY26']/BRANCHES['FY19'])**(1/7)-1)*100:.0f}% a year (derived), with the two largest annual additions in FY25 ({BRANCHES['FY25']-BRANCHES['FY24']} branches) and FY26 ({BRANCHES['FY26']-BRANCHES['FY25']}). Gold-loan branches account for all of the net addition since FY21 together with the new co-located format, while the number of stand-alone MSME hubs has stayed broadly stable – consistent with the strategy of growing mortgages out of existing catchments rather than new ones.")
    P.append(pg)

    # ------------------------------------------------------------------ 87 Appendix D NCDs
    pg = Page("Appendix D — Debt Instruments Outstanding and Issued in FY26")
    pg.table(["Instrument", "Allotment date", "Maturity", "Amount (₹ crore)", "Type"],
             [[n[0], n[1], n[2], f"{n[3]:,.2f}", "Secured" if "ecured" in n[0] and "nsecured" not in n[0] else "Unsecured / subordinated"] for n in NCDS] +
             [["Total NCDs outstanding (face value)", "", "", f"{sum(n[3] for n in NCDS):,.2f}", ""]],
             widths=[2.9, 1.0, 1.0, 1.05, 1.1], font=8, source=f"{AR26}, Directors’ Report – debentures outstanding as at 31 March 2026. Carrying amounts in the balance sheet differ from face value because of unamortised issue costs and accrued interest.")
    pg.table(["Other debt facts FY26", "Detail"],
             [["Fresh NCD issuance authority", "Board approval 25 August 2025 and shareholders’ special resolution (30th AGM) for up to ₹2,500 crore on private placement"],
              ["NCDs issued during FY26", "₹200 crore 7.29% secured reset-rate NCDs (6 Jan 2026, 3-year); ₹250 crore 8.85% and ₹200 crore 8.90% unsecured subordinated Tier II NCDs (24 Mar 2026, maturing Oct/Nov 2033)"],
              ["Commercial paper", "Outstanding ₹1,164 crore (net of discount); maximum outstanding during the year ₹1,375 crore (FY25: ₹575 crore); all maturities under one year; rated A1+"],
              ["External commercial borrowings", "USD 250 million programme; carrying amount ₹2,382 crore (FY25: ₹257 crore); fully hedged for the entire maturity through cross-currency swaps; derivative notional ₹2,446 crore"],
              ["FCNR borrowings", "₹62.5 crore (foreign-currency facility rolled over)"],
              ["Bank term loans", "₹5,682 crore from banks other than Federal Bank; ₹1,064 crore from Federal Bank; ₹866 crore from other financial institutions"],
              ["Demand loans / working capital", "₹783 crore from banks; ₹60 crore from Federal Bank"],
              ["Borrowing limit", "₹18,000 crore approved by shareholders; total borrowings ₹13,484 crore at 31 March 2026 (75% utilised, derived)"],
              ["Debenture trustees / registrar", "Axis Trustee Services, Beacon Trusteeship, IDBI Trusteeship Services; MUFG Intime India (RTA)"],
              ["Credit ratings", "AA+/Stable long-term and A1+ short-term from CARE, CRISIL, ICRA and India Ratings"]],
             widths=[1.9, 5.15], font=8, source=f"{AR26}, Directors’ Report, notes 16–18, note 48; Report on Corporate Governance.")
    pg.p("Composition and cost. By the MD&CEO’s classification the funding mix at 31 March 2026 was term loans 50%, external commercial borrowings 17%, NCDs and commercial paper 13% and direct assignment 14%, with the share of fixed-rate borrowings raised from about 10% to 40% during the year. The average cost of borrowings for FY26 was 8.1% (FY25: 9.0%) and the exit cost in the fourth quarter was 7.83%. Federal Bank’s facilities (₹1,124 crore of term and demand loans above, plus the FCNR line) represent roughly a tenth of total borrowings and are priced on arm’s-length terms disclosed under related-party transactions (interest paid ₹84.8 crore in FY26).")
    P.append(pg)

    # ------------------------------------------------------------------ 88 Appendix E shareholding & related party
    pg = Page("Appendix E — Shareholding, Share Capital and Related-Party Summary")
    pg.table(["Category", "31 Mar 2026 (%)", "31 Mar 2025 (%)"], [[s[0], f"{s[1]:.2f}", f"{s[2]:.2f}"] for s in SHAREHOLDING] + [["Total", "100.00", "100.00"]],
             widths=[4.05, 1.5, 1.5], font=8, source=f"{AR26}, Report on Corporate Governance – categories of shareholders.")
    pg.table(["Share capital and listing facts", "Detail"],
             [["Equity shares outstanding", f"{SHARES_OUT:,} of ₹10 each (31 Mar 2025: {SHARES_OUT_PY:,})"],
              ["Shares allotted in FY26", f"{ESOP_ALLOTTED:,} under ESOS 2018 on exercise of options"],
              ["ESOP schemes", "ESOS 2018 and ESOS 2024 (approved at 29th AGM, 19 Sep 2024); amendments approved at 30th AGM"],
              ["IPO", "November 2023; total size ₹1,092 crore (fresh issue ₹600 crore + offer for sale); listed on NSE and BSE"],
              ["Market capitalisation", f"₹{MCAP_CR:,} crore at 31 March 2026 (AR FY26 inside cover)"],
              ["Dividend", "No dividend recommended for FY26; profits retained; ₹68.72 crore transferred to statutory reserve"],
              ["Promoter", "The Federal Bank Limited – 60.79%; nominee directors Mr. K.V.S. Manian and Mr. Harsh Dugar"],
              ["Private-equity investor", "True North Fund VI LLP – invested ₹168.6 crore in 2018; exited in FY26; nominee director resigned 14 May 2026"],
              ["31st AGM", "29 September 2026 (through VC/OAVM); RTA MUFG Intime India Pvt Ltd"]],
             widths=[2.0, 5.05], font=8)
    pg.table(["Related-party transactions with Federal Bank (₹ crore, FY26 vs FY25)", "FY26", "FY25"],
             [["Interest paid on cash credit / WCDL / term loans", "84.82", "78.12"], ["Processing fees paid", "1.43", "n.a."],
              ["Income from distribution of bank products", "33.07", "3.16"], ["PTC service fees received", "0.30", "0.25"],
              ["Term loan outstanding (31 March)", "1,064.1", "1,029.6"], ["Demand loan outstanding", "60.0", "60.0"], ["Subordinated NCDs held by Federal Bank", "246.1", "245.5"]],
             widths=[4.55, 1.25, 1.25], font=8, source=f"{AR26}, related-party disclosures (note 48) and notes 17–18. Items marked n.a. were not separately disclosed in the extracted text.")
    P.append(pg)

    # ------------------------------------------------------------------ 89 Appendix F glossary & formulae
    pg = Page("Appendix F — Glossary and Ratio Formulae")
    pg.table(["Ratio / term", "Formula used in this report", "FY26 value", "Source basis"],
             [["AUM", "On-book loans + co-lent partner share + assigned portfolio under management", "₹20,153 crore", "Company-defined"],
              ["Yield on advances", "Interest on loans ÷ average advances (company basis)", "16.7%", "Reported"],
              ["Cost of borrowings", "Finance costs ÷ average borrowings (company basis)", "8.1% (Q4: 7.83%)", "Reported"],
              ["Spread", "Yield − cost of borrowings", "8.6%", "Reported"],
              ["Net interest margin", "Net interest income ÷ average total assets", "8.8%", "Reported"],
              ["Cost-to-income", "Operating expenses ÷ (NII + fee and other income)", "57.2%", "Reported; derived reconciles"],
              ["Credit cost", "Impairment on financial instruments ÷ average total assets", "0.8% (derived 0.77%)", "Reported / derived"],
              ["GNPA / NNPA", "Stage 3 loans (gross / net of provisions) ÷ gross / net advances", "1.9% / 1.3%", "Reported"],
              ["Provision coverage ratio", "Stage 3 provisions ÷ gross Stage 3 loans", "32.3%", "Reported"],
              ["Return on average assets", "PAT ÷ average total assets", "2.44% (derived 2.28%)", "Reported / derived"],
              ["Return on equity", "PAT ÷ average net worth", "12.62% (derived 12.55%)", "Reported / derived"],
              ["Debt-to-equity", "Total borrowings ÷ net worth", "4.6x (derived 4.61x)", "Reported / derived"],
              ["CRAR", "(Tier I + Tier II capital) ÷ risk-weighted assets", "22.40% (Tier I 17.52%)", "Reported"],
              ["Book value per share", "Net worth ÷ shares outstanding", "₹78.19", "Reported"],
              ["EPS (basic)", "PAT ÷ weighted average shares", "₹9.20", "Reported"],
              ["Price-to-book / P/E", "Implied price (mcap ÷ shares) ÷ BVPS or EPS", "≈1.59x / ≈13.5x", "Derived"],
              ["CAGR", "(End ÷ Start)^(1/years) − 1", "AUM FY22–26: 34.3%", "Derived"],
              ["PPOP", "NII + fee and other income − operating expenses", "₹576 crore", "Derived"]],
             widths=[1.5, 3.2, 1.4, 0.95], font=7.5)
    pg.table(["Term", "Meaning", "Term", "Meaning"],
             [["Stage 1 / 2 / 3", "Ind AS 109 buckets: performing / significant increase in credit risk / credit-impaired", "FVOCI loans", "Loans held in a business model of collect-and-sell, measured at fair value through OCI (pools earmarked for assignment)"],
              ["ECL", "Expected credit loss – forward-looking provision under Ind AS 109", "ARC", "Asset reconstruction company – buyer of NPA pools"],
              ["Co-lending", "RBI model where bank and NBFC jointly fund loans originated by the NBFC", "Direct assignment", "Sale of a loan pool with servicing retained; excess spread recognised as income"],
              ["NBFC-ML", "Middle-Layer NBFC under RBI scale-based regulation", "ICAAP", "Internal capital adequacy assessment process"],
              ["ALM", "Asset-liability management; structural liquidity by maturity bucket", "SARFAESI", "Act enabling enforcement of security without court intervention"],
              ["LTV", "Loan amount ÷ value of collateral", "DSGL", "Doorstep gold loan – gold loan originated and serviced at the customer’s premises"]],
             widths=[1.0, 2.55, 1.0, 2.5], font=7.5)
    P.append(pg)

    # ------------------------------------------------------------------ 90 Appendix G viva Q&A
    pg = Page("Appendix G — Viva Voce Preparation: Likely Questions and Evidence-Based Answers")
    pg.table(["Likely question", "Evidence-based answer (with source)"],
             [["Why choose Fedfina for fundamental analysis?", "Bank-promoted listed NBFC with a complete cycle (IPO FY24, reset FY25, recovery FY26) inside the study period and unusually granular disclosures – eight-year KPIs, product disbursements, stage data, ALM buckets."],
              ["What explains the 53% PAT growth in FY26?", "NII +15% (₹159 crore) from 27.5% AUM growth and a wider 8.6% spread; impairment −₹101 crore (credit cost 1.8% → 0.8%); operating costs +₹65 crore; fee income −₹38 crore; tax rate stable at 25.5% (Directors’ Report; P&L)."],
              ["Is the growth just gold prices?", "Partly. Gold AUM +76% with tonnage +12% – most gold growth is price/LTV-driven. But mortgage AUM grew 16%, the unsecured book was exited, and management targets 10–12% tonnage CAGR (MD&CEO statement)."],
              ["How safe is the gold book?", "Portfolio LTV 60.9% vs 75% regulatory ceiling; average ticket ₹2.7 lakh; auctions fell to 4,633 accounts with 92% of dues realised; short tenor means LTV resets within a year (notes 48; Directors’ Report)."],
              ["What went wrong in FY25?", "Small-ticket LAP delinquencies rose because “collection infrastructure had not kept pace with business growth”; credit cost rose to 1.8%; unsecured BL stopped Dec 2024 (FY25 MD&CEO letter)."],
              ["What was fixed in FY26?", "BRE-based underwriting with Salesforce; in-house collections 1.8x, agency 0.4x; 75% in-house sourcing; ₹886 crore BL assigned; 814 NPA accounts sold; Stage 2 fell 5.1% → 1.9% (FY26 MD&CEO statement; note 8)."],
              ["Is the company adequately capitalised?", "CRAR 22.4% (Tier I 17.5%, Tier II 4.9%) vs 15% floor; but D/E rose to 4.6x and no equity raised since the IPO – equity will be needed if 20–25% growth continues at 13% RoE (note 48; Directors’ Report)."],
              ["How is the company funded?", "₹13,484 crore borrowings from 41 lenders: bank term loans 50%, ECB 17% (USD 250 mn, fully hedged), NCD/CP 13%, DA 14%; 40% fixed-rate; AA+/Stable from four agencies (notes 16–18)."],
              ["What is the liquidity position?", "Positive cumulative ALM gap in every bucket to one year (₹3,749 crore surplus at 12 months); cash ₹1,340 crore; refinancing concentrated in the 1–3 year bucket (note 48)."],
              ["Which ratios are not meaningful here and why?", "Inventory and debtors turnover, operating margin and interest coverage – a lender’s inventory is its loan book and interest is its cost of goods; the company marks them ‘NA’ in its key-ratio table."],
              ["What is the difference between AUM and loans on the balance sheet?", "AUM ₹20,153 crore includes co-lent and assigned portfolios; on-book gross loans are ₹14,505 crore; 12.1% of AUM is off-book per the Directors’ Report; the remaining gap is not fully bridged publicly (limitation)."],
              ["Did you accept your hypothesis?", "Accepted with qualifications: three of four tests met cleanly; credit-cost improvement partly via write-offs/ARC sales; gold price and rate cuts contributed – structural changes lower the downside without capping the upside."],
              ["What would change your view?", "Credit cost above 1% on the FY26 ST LAP vintage; D/E above 5x without an equity plan; tonnage growth below 10% with a falling gold price; or renewed collections slippage."],
              ["How does Fedfina compare with Muthoot and Manappuram?", "Much smaller (AUM ₹20,153 crore vs ₹1,62,826 crore standalone at Muthoot and ₹55,952 crore at Manappuram) but comparably capitalised (CRAR 22.4% vs 20.75% and 21.3%) and more diversified by product (gold 51% of AUM vs ≈90% at the gold specialists); peer figures from FY26 results coverage."],
              ["What is the impact of the RBI gold-lending Directions 2025?", "From 1 April 2026: tiered LTV caps of 85%/80%/75% by ticket size maintained through the tenor, bullet loans capped at 12 months with LTV computed on the maturity amount, standardised valuation and auction conduct, gold return within seven working days. Fedfina’s ₹2.7 lakh average ticket and 60.9% LTV leave headroom; the compliance effect falls on renewals and processes rather than on pricing."],
              ["Which data did you not fabricate or estimate?", "None of the numbers are estimated: every figure is from the three annual reports, RBI directions, the EY summary or peer results coverage; derived figures show their formula; items unavailable are marked n.a."]],
             widths=[2.1, 4.95], font=7.5)
    P.append(pg)

    # ------------------------------------------------------------------ 91 Appendix H checklist & data notes
    pg = Page("Appendix H — Submission Checklist and Data Notes")
    pg.table(["Checklist item", "Status", "Where"],
             [["Certificate, declaration and acknowledgement signed", "To be signed at submission", "Pages 2–4"],
              ["Executive summary with key figures", "Complete", "Page 5"],
              ["Objectives, scope, research questions, hypothesis, methodology", "Complete", "Chapter 1"],
              ["Sector analysis with Porter and PESTLE", "Complete", "Chapter 2"],
              ["Company, product and five-year financial analysis", "Complete", "Chapters 3–5"],
              ["Risk analysis with risk matrix and ESG", "Complete", "Chapter 6"],
              ["SWOT, scenarios, scorecard and recommendations", "Complete", "Chapter 7"],
              ["Findings, hypothesis test, conclusion, limitations, bibliography", "Complete", "Chapter 8"],
              ["All tables and figures sourced; derived figures labelled", "Complete", "Throughout"],
              ["Appendices: statements, branches, debt, shareholding, glossary, viva", "Complete", "Appendices A–G"],
              ["Plagiarism declaration and originality check", "To be run by the Institute", "–"]],
             widths=[3.9, 1.9, 1.25], font=8)
    pg.h2("Data notes and reconciliations")
    pg.bullets([
        "Units:: Statutory sections use ₹ lakh; corporate overview uses ₹ crore/million. Conversions: ₹1 crore = ₹100 lakh = ₹10 million. Example: PAT ₹34,360 lakh = ₹343.6 crore = ₹3,436 million.",
        "Eight-year KPI series:: Taken from the FY24 report (FY19–FY24) and FY25/FY26 reports (FY25–FY26). The FY26 report’s five-year charts present values in a non-chronological text layer; they were reconciled year-by-year against the earlier reports and the Directors’ Report tables (Table T8 on page 54).",
        "Yield / CoB / spread basis:: FY26-report basis used for FY22–FY26; earlier-basis figures disclosed alongside. Directions of all trends are identical on both bases.",
        "GNPA FY26:: 1.9% (Key Highlights, MD&A, Directors’ Report context) vs 2.2% (FY26 five-year chart). Both shown; 1.9% used in headline tables. Net credit-impaired ratio per note 48 is 1.28%, consistent with NNPA 1.3%.",
        "Direct-assignment income:: ₹7.4 crore (Corporate Overview, −88.8%, 1.6% of PBT) vs ₹102.0 crore (note 26, ‘income on direct assignment’). Definitions differ; both reported.",
        "Headcount:: 4,568 (FY25) → 5,303 (FY26) per Directors’ Reports (+16.1%); Directors’ Report narrative says employee strength ‘grew 6.3%’. Headcount figures used; discrepancy noted.",
        "Borrowings reconciliation:: Notes 16 + 17 + 18 = ₹13,48,413 lakh = Directors’ Report borrowings. Debt securities ₹1,73,031 lakh = secured NCDs ₹56,588 + CP ₹1,16,443 lakh. Subordinated liabilities ₹91,635 lakh = related party ₹24,612 + others ₹67,023 lakh.",
        "Cost-to-income reconciliation:: (₹44,393 + ₹5,447 + ₹27,281 lakh) ÷ (₹1,22,975 + ₹11,754 lakh) = 57.2% = reported 57.23%.",
        "RoA / RoE methodology:: Reported 2.44% / 12.62% use company averages; two-point averages give 2.28% / 12.55%. Reported figures used in headline tables; derived figures in DuPont analysis.",
        "AUM vs on-book loans:: ₹20,153 crore vs ₹14,505 crore gross (₹14,319 crore net); off-book disclosed as 12.1% of AUM; remaining difference not reconcilable from public data.",
        "Peer data:: FY26 figures from results coverage (May 2026); standalone/consolidated bases differ and are labelled; not used for ratio comparison.",
        "Charts:: All figures were drawn from the data above; no chart values are estimated.",
    ])
    P.append(pg)

    return P
