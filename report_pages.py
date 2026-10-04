"""Page-by-page academic content for the 100-page Fedfina risk-analysis report.

Company disclosures are cited to the supplied annual-report PDF page numbers.
No confidential monthly internship data or internal policy limits are inferred.
"""


def pg(section, title, paragraphs=(), bullets=(), table=None, chart=None,
       note=None, sources=()):
    return {
        "section": section, "title": title, "paragraphs": list(paragraphs),
        "bullets": list(bullets), "table": table, "chart": chart,
        "note": note, "sources": list(sources),
    }


PAGES = [
# 7 — Contents
pg("PRELIMINARY", "Contents", paragraphs=[
    "The report follows the academic sequence of the reference project: study design, organisation, risk framework, evidence-based analysis, internship workstreams, findings and supporting appendices. Page references below refer to this report; source-page references appear in the relevant sections.",
], table={"headers":["Section", "Coverage", "Pages"], "rows":[
    ["Preliminary matter", "Project at a glance", "1–9"],
    ["Chapter 1", "Introduction and study design", "10–16"],
    ["Chapter 2", "Organisation and lending model", "17–25"],
    ["Chapter 3", "Enterprise-risk landscape", "26–35"],
    ["Chapter 4", "Research methodology and monitoring methods", "36–44"],
    ["Chapter 5", "FY2025–26 financial and risk analysis", "45–61"],
    ["Chapter 6", "Internship role and recurring deliverables", "62–69"],
    ["Chapter 7", "Findings, controls and recommendations", "70–82"],
    ["Chapter 8", "Conclusion, learning and limitations", "83–87"],
    ["References", "Annual reports and source reconciliation", "88–89"],
    ["Appendices", "Data dictionary, monitoring templates and viva aid", "90–100"],
]}, note="The annual reports are used as retrospective public evidence. Internal company working papers are not reproduced.", sources=()),

# 8 — Lists
pg("PRELIMINARY", "List of Figures, Tables and Abbreviations", paragraphs=[
    "Figures: five-year AUM trend (p.46); PAT and returns (p.47); yield, spread and cost of borrowings (p.48); GNPA, NNPA and provision coverage (p.49); CRAR and ROE (p.50); secured-AUM progression (p.51); maturity gap (p.55); interest-rate sensitivity (p.56); qualitative risk map (p.71).",
    "Selected abbreviations are expanded here for readability. Definitions are analytical aids; where a term is defined differently in an approved company policy or annual-report note, that source definition takes precedence.",
], table={"headers":["Term", "Meaning", "Term", "Meaning"], "rows":[
    ["ALCO", "Asset Liability Committee", "AUM", "Assets Under Management"],
    ["BRE", "Business Rule Engine", "CRAR", "Capital to Risk-Weighted Assets Ratio"],
    ["DPD", "Days Past Due", "EAD", "Exposure at Default"],
    ["ECL", "Expected Credit Loss", "EWS", "Early Warning Signals"],
    ["GNPA / NNPA", "Gross / Net Non-Performing Assets", "LAP", "Loan Against Property"],
    ["LGD", "Loss Given Default", "LTV", "Loan-to-Value"],
    ["NCD", "Non-Convertible Debenture", "NBFC", "Non-Banking Financial Company"],
    ["NII", "Net Interest Income", "PAT", "Profit After Tax"],
    ["PD", "Probability of Default", "PCR", "Provision Coverage Ratio"],
    ["RMC", "Risk Management Committee", "ROA / ROE", "Return on Assets / Equity"],
    ["SMA", "Special Mention Account", "ST / MT", "Small Ticket / Medium Ticket"],
]}, note="Other terms are defined at first use and in Appendix A (p.90).", sources=()),

# 9
pg("PROJECT AT A GLANCE", "Project at a Glance", paragraphs=[
    "This study examines how a listed, secured-lending NBFC identifies and monitors risk, and how public annual-report evidence can be translated into a disciplined monthly and quarterly reporting workflow. The central unit of analysis is Fedbank Financial Services Limited (Fedfina) for the year ended 31 March 2026.",
    "The internship role supplied by the student is Risk Analyst Intern at Fedbank Financial Services Ltd from 4 April to 3 July 2026. The listed workstreams are monthly performance/EWS graphs, quarterly RMC preparation, a monthly risk paper, policy-trigger-versus-actual monitoring and bounce analysis. No borrower-level, monthly MIS, internal trigger or RMC minutes were supplied; therefore this report explains the work method and does not invent internal results.",
], table={"headers":["Item", "Report basis"], "rows":[
    ["Primary analytical period", "FY2025–26; year ended 31 March 2026"],
    ["Historical context", "FY2023–24 and FY2024–25 annual reports; latest five-year chart series used where noted"],
    ["Research method", "Documentary analysis, trend/ratio interpretation and risk-control design"],
    ["Practical output", "Monthly dashboard, EWS, risk-paper, RMC and bounce-analysis templates"],
]}, note="The project is an academic risk-analysis report, not an audit, credit rating or investment recommendation.", sources=["Fedfina Annual Reports FY2023–24, FY2024–25 and FY2025–26 (supplied PDFs)."]),

# Chapter 1, pp.10–16
pg("CHAPTER 1 · INTRODUCTION", "Introduction and Study Context", paragraphs=[
    "A lender's financial position is inseparable from the quality, timing and recoverability of its loan assets. Growth in assets under management can expand revenue, but it also increases exposure to borrower cash-flow shocks, collateral-value changes, collection delays, funding costs, liquidity mismatches, process failures and regulatory obligations. Risk analysis therefore asks not only how quickly a lender grows, but whether that growth is controlled and adequately funded.",
    "Fedfina's FY2025–26 disclosures describe a strategy centred on secured Gold Loans and Mortgage Loans, alongside an operating rebuild in small-ticket LAP, collections, sourcing and technology. This report studies those public disclosures through a risk-management lens and connects them to the student's stated internship responsibilities.",
], bullets=["The focal reporting date is 31 March 2026.", "FY24 and FY25 are used only as historical context and cross-checks.", "Any internal monthly result must be inserted from authorised records, not inferred from annual data."], note="Risk-adjusted growth, rather than volume growth alone, is the organising idea of this report.", sources=["FY26 Annual Report, supplied PDF pp.4, 13–15."]),
pg("CHAPTER 1 · INTRODUCTION", "Need and Relevance of the Study", paragraphs=[
    "A management student working in risk analysis must be able to translate financial disclosures into early questions for management: which portfolio is growing, what is changing in delinquency, whether collections are curing accounts, how much loss buffer is available, whether asset and liability cash flows align, and whether exceptions remain inside approved policy. A single profitability ratio cannot answer these questions.",
    "The study is relevant because Fedfina's reported FY26 results combine faster AUM growth and a substantial profit recovery with a changing portfolio mix, an expanding branch base, ongoing mortgage exposures and active funding diversification. Reading these facts together makes the project a practical application of credit, market, liquidity and operational-risk concepts.",
], bullets=["It builds a transparent baseline from the three annual reports supplied.", "It separates reported facts from author calculations and from unavailable internal data.", "It develops repeatable monthly and quarterly templates matching the stated job tasks."], note="A public-data study can explain the monitoring logic; it cannot replace account-level validation.", sources=["FY24 Annual Report, supplied PDF pp.13–14, 24; FY25 Annual Report, p.33; FY26 Annual Report, pp.4, 13–15."]),
pg("CHAPTER 1 · INTRODUCTION", "Objectives of the Study", paragraphs=[
    "The project has one overall objective: to analyse the principal risks associated with Fedfina's FY2025–26 business and financial disclosures, and to translate that analysis into an academically sound description of the Risk Analyst internship workstreams. The analysis is descriptive and interpretive; it does not claim access to the Company's internal risk appetite or confidential portfolio data.",
], bullets=["Understand Fedfina's ownership, products, operating model and FY26 strategic direction.", "Compare selected FY22–FY26 company-reported indicators using the latest annual-report series.", "Assess credit, collateral, asset-quality, funding, liquidity, interest-rate, operational and conduct risks.", "Explain monthly graphs/EWS, risk-paper, trigger-versus-actual, bounce analysis and quarterly RMC-pack workflows.", "Identify evidence-based control improvements and limitations for further study."], table={"headers":["Objective class", "Expected academic output"], "rows":[
    ["Descriptive", "Company and product profile"], ["Analytical", "Trend, ratio and risk interpretation"], ["Applied", "Reusable monitoring templates"], ["Evaluative", "Prioritised findings and recommendations"],
]}, sources=[]),
pg("CHAPTER 1 · INTRODUCTION", "Scope, Period and Delimitations", paragraphs=[
    "Company-specific performance is anchored to FY2025–26, the financial year ended 31 March 2026. The supplied FY2023–24 and FY2024–25 reports are used to contextualise the transition and to cross-check historical series. The internship period is separately stated as 4 April–3 July 2026. The FY26 annual report was filed on 4 September 2026, so its figures are retrospective study evidence, not evidence that the intern had that report during the placement.",
    "The scope covers the listed entity, its retail-lending products, public risk disclosures, reported financial trends, selected risk metrics and monitoring-process design. It excludes unpublished borrower records, live month-end risk MIS, policy thresholds, internal committee packs, branch visits, management interviews, independent audit work and market valuation.",
], table={"headers":["Period / boundary", "Use in this report"], "rows":[
    ["FY2023–24", "Baseline and earlier risk-management disclosures"],
    ["FY2024–25", "Transition-year comparison and risk framework narrative"],
    ["FY2025–26", "Primary company-data year; year-end 31 March 2026"],
    ["4 Apr–3 Jul 2026", "Student-stated internship dates; no daily activity log supplied"],
]}, note="Fiscal-year figures and calendar internship months are not interchangeable periods.", sources=["FY26 Annual Report, supplied PDF pp.1, 14–15."]),
pg("CHAPTER 1 · INTRODUCTION", "Research Questions and Working Propositions", paragraphs=[
    "The questions are designed to test whether scale, mix, profitability and control indicators move consistently, not to claim causality from annual aggregates. Reported changes are interpreted as signals for further monitoring. A secured loan can still default, collateral can be misvalued or difficult to realise, and growth can conceal weaker cohorts; these propositions frame the analysis.",
], bullets=["RQ1: How did AUM, PAT and returns evolve through FY22–FY26?", "RQ2: What does the disclosed movement in secured AUM and asset-quality ratios imply—and not imply—about credit risk?", "RQ3: What funding, maturity and market-risk signals are visible in FY26 disclosures?", "RQ4: How can monthly monitoring and quarterly RMC preparation be made evidence-led?", "RQ5: Which risks remain unquantified without internal account-level and policy data?"], note="Working proposition: secured mix and operating discipline can support resilience only when underwriting, collections, liquidity and controls keep pace.", sources=["FY24 Annual Report, supplied PDF p.24; FY25 Annual Report, p.33; FY26 Annual Report, pp.13–15, 114–118."]),
pg("CHAPTER 1 · INTRODUCTION", "Research Design and Analytical Process", paragraphs=[
    "The study uses descriptive research based on secondary data. Annual-report disclosures are extracted, the reporting period and units are recorded, and metrics are compared only after checking whether their definition and source presentation are compatible. The workflow then links changes in reported figures to company-described portfolio actions and to risk-management concepts.",
    "The steps are: define the period and questions; inventory sources; extract and cross-check figures; convert units; compute transparent ratios; identify direction and exceptions; distinguish fact from interpretation; design monitoring templates; and state limits. Where two annual reports present different historical values, the latest report's five-year series is used for the plotted trend and the difference is explicitly disclosed.",
], table={"headers":["Stage", "Control question"], "rows":[
    ["Extract", "What is the exact source page, date and unit?"],
    ["Validate", "Does the number reconcile to the relevant chart/note?"],
    ["Interpret", "Is the change fact, calculation or hypothesis?"],
    ["Report", "Can another analyst reproduce the calculation?"],
]}, sources=["All three supplied Fedfina annual reports; detailed source map on p.89."]),
pg("CHAPTER 1 · INTRODUCTION", "Reliability, Ethics and Study Limitations", paragraphs=[
    "Annual reports are management-prepared public disclosures, with audited financial statements and separately presented operational or forward-looking information. The report identifies which category a number belongs to. Rounded operational ratios are not treated as more precise than disclosed. AUM, GNPA, credit cost, CRAR and audited PAT can have different definitions, consolidation bases or denominator choices; they are not interchangeable.",
    "No personal customer information, confidential policy limits, unpublished RMC material or fabricated internship outcome is included. The report uses a respectful, non-judgmental approach to borrowers: a payment bounce or arrear is a monitoring signal, not proof of bad intent. The analysis is not a substitute for Fedfina's approved policies, RBI requirements, auditor conclusions or management judgement.",
], bullets=["Three annual reports are the primary evidence set.", "No quantitative monthly bounce rate or policy-breach count is available in the repository.", "Terminology and year-to-year chart differences are noted rather than silently reconciled."], sources=[]),

# Chapter 2, pp.17–25
pg("CHAPTER 2 · ORGANISATION", "Company Profile", paragraphs=[
    "Fedbank Financial Services Limited, commonly referred to as Fedfina, is a public retail-lending NBFC and a subsidiary of The Federal Bank Limited. The Company was incorporated on 17 April 1995 and is headquartered in Mumbai. Its shares trade on NSE as FEDFINA and on BSE under scrip code 544027; the FY26 annual report lists CIN L65910MH1995PLC364635.",
    "The company profile matters to risk analysis because lender type, promoter support, listing status and product design determine the governance, disclosure and funding context. Parentage may support institutional credibility, but it does not remove the NBFC's own obligations to assess borrowers, manage liquidity, protect collateral and control operations.",
], table={"headers":["Company identifier", "Disclosed detail"], "rows":[
    ["Legal name", "Fedbank Financial Services Limited"], ["Common name", "Fedfina"],
    ["Incorporation", "17 April 1995"], ["NSE / BSE", "FEDFINA / 544027"],
    ["CIN", "L65910MH1995PLC364635"], ["Primary period", "FY2025–26"],
]}, sources=["FY26 Annual Report, supplied PDF pp.3, 6."]),
pg("CHAPTER 2 · ORGANISATION", "Parentage, Listing and Governance Context", paragraphs=[
    "The annual reports describe Fedfina as a subsidiary of Federal Bank. The FY26 investment-case section states that Federal Bank held approximately 60.8% of the Company. That relationship is strategically relevant to reputation, governance and access to institutional funding, but the risk analyst should still assess the NBFC on its own balance sheet, maturity profile, capital, asset quality and contractual obligations.",
    "As a listed company, Fedfina reports through statutory, governance and sustainability sections in addition to its financial statements. The Risk Management Committee (RMC) and Asset Liability Committee (ALCO) have different roles: the former oversees the broader risk framework and portfolio; ALCO focuses on asset-liability and market/liquidity positions. Reporting lines and committee responsibilities should be mapped to the current approved terms of reference.",
], bullets=["Promoter support is a mitigant, not a substitute for standalone liquidity analysis.", "Listed disclosures provide public evidence but not the full internal risk dashboard.", "Committee oversight should be paired with named executive ownership and closure tracking."], sources=["FY26 Annual Report, supplied PDF p.10 and p.53."]),
pg("CHAPTER 2 · ORGANISATION", "Business Model and Sources of Risk", paragraphs=[
    "Fedfina originates loans through a combination of branch-led, field and digital-enabled processes, funds those loans through borrowings and other disclosed funding arrangements, and earns interest and fee income while bearing credit, operating, funding and servicing costs. A lender's financial engine therefore depends on both sides of the balance sheet: performing assets generate receipts, while liabilities create scheduled outflows and refinancing needs.",
    "A useful risk lens follows the loan lifecycle from acquisition through closure. Each stage has a distinct control objective: eligible sourcing, identity verification, underwriting, collateral validation, approval authority, documentation, disbursement, mandate setup, servicing, early warning, collection, recovery and release of security. A lapse in an early stage can reappear later as a bounce, delinquency, fraud loss or customer complaint.",
], table={"headers":["Value chain", "Key risk question"], "rows":[
    ["Source / acquire", "Is the channel, borrower and application traceable?"],
    ["Underwrite / secure", "Are repayment capacity and collateral independently assessed?"],
    ["Disburse / service", "Are approvals, documents and payment mandates complete?"],
    ["Monitor / collect", "Are exceptions, arrears and complaints escalated on time?"],
    ["Recover / close", "Are recoveries fair, reconciled and security released correctly?"],
]}, sources=["FY25 Annual Report, supplied PDF p.33; FY26 Annual Report, pp.13, 116."]),
pg("CHAPTER 2 · ORGANISATION", "Product Portfolio and Risk Differentiation", paragraphs=[
    "The supplied annual reports describe Gold Loans and Mortgage Loans as core secured products. Mortgage lending includes small-ticket LAP (ST LAP), medium-ticket LAP (MT LAP) and home loans. FY26 describes an exit from the ₹886 crore business-loan portfolio during the first half of the year and a sharper concentration on secured lending. The precise composition should always be read from the product disclosures for the reporting date.",
    "Products differ in collateral, tenor, ticket size, verification effort, repayment pattern and recovery method. A common dashboard can compare outcomes, but risk limits and early-warning thresholds should be product-specific. A low-ticket gold loan secured by jewellery is not operationally equivalent to a longer-tenor LAP backed by property and business cash flow.",
], table={"headers":["Product", "Primary repayment / security lens", "Monitoring emphasis"], "rows":[
    ["Gold Loan", "Jewellery collateral; short-tenor liquidity", "LTV/margin, custody, valuation, overdue/release"],
    ["ST LAP", "Small-business cash flows and property", "Vintage quality, bureau, field collection, fraud"],
    ["MT LAP", "Larger borrower cash flows and property", "Title, valuation, leverage, concentration, ALM"],
    ["Home Loan", "Household repayment and housing collateral", "Income, property/legal checks, tenor and rate"],
]}, sources=["FY26 Annual Report, supplied PDF pp.8, 13."]),
pg("CHAPTER 2 · ORGANISATION", "Gold Loans: Risk and Control Logic", paragraphs=[
    "Gold lending combines relatively short tenor and readily realisable collateral with intense custody, valuation and transaction-control requirements. The FY26 report states that Gold AUM reached ₹10,352 crore, up 76% year on year, while gold under custody rose 12% to 12.6 tonnes. These disclosures distinguish physical portfolio growth from growth attributable only to higher gold prices, but they do not remove the need for granular purity, weight, LTV and custody controls.",
    "The annual report describes the margin retained on gold jewellery and the exclusion of stone value from collateral valuation. A risk analyst should monitor approved LTV at origination and through the loan tenor, reconciliation of packets and system records, maker-checker approvals, vault access, insurance, renewal/overdue behaviour and fair customer notice before recovery actions.",
], bullets=["Track both price-driven collateral value and underlying gold quantity.", "Stress a sustained price fall, not only a one-day movement.", "Treat custody/process failures as operational and conduct risks as well as credit risks."], note="Collateral reduces expected loss only when it is correctly valued, secured and enforceable.", sources=["FY26 Annual Report, supplied PDF pp.13, 116, 118; FY24 Annual Report, p.24."]),
pg("CHAPTER 2 · ORGANISATION", "Mortgage Loans: Risk and Control Logic", paragraphs=[
    "LAP and home loans are secured by immovable property, but recovery depends on enforceable title, accurate valuation, borrower cash flows, legal documentation and the time and cost of realisation. FY26 reports that 82.2% of Mortgage AUM was backed by self-occupied residential or commercial property. Occupancy is a portfolio descriptor; it is not itself proof of clear title, market liquidity or repayment capacity.",
    "The FY26 report gives average ticket sizes and origination yields separately for ST LAP and MT LAP and describes the rebuilding of ST LAP underwriting and collections. The analyst should use vintage-based cohort views, delinquency roll-rates, bureau and bank-statement quality, property valuation ageing, legal exceptions, sector/geography concentration, and end-use monitoring to detect risk before NPA recognition.",
], table={"headers":["Control step", "Evidence to retain"], "rows":[
    ["Borrower capacity", "Verified income/cash flows, obligations, bureau and repayment analysis"],
    ["Security", "Title search, independent valuation, charge creation and insurance where applicable"],
    ["Decision", "Delegated authority, policy checks, exceptions and maker-checker audit trail"],
    ["Post-disbursement", "End-use/early-warning follow-up, overdue, collateral and complaint monitoring"],
]}, sources=["FY26 Annual Report, supplied PDF p.13."]),
pg("CHAPTER 2 · ORGANISATION", "Customer and Loan Lifecycle", paragraphs=[
    "Risk controls should be designed as a continuous chain rather than a one-time credit approval. Before disbursement, identity, consent, bureau, cash flow, collateral, documentation and repayment mandate need to be checked. After disbursement, servicing and early-warning signals can reveal deteriorating capacity, mandate failure, fraud patterns, collateral exceptions or unfair customer outcomes.",
    "The reported FY26 customer and digital-servicing indicators show why operating metrics belong in risk reporting. The annual report discloses active customers, average customers per branch, automated service and resolution-within-turnaround-time measures. These are service indicators, not direct proof of credit quality. Each operational KPI should have a definition, source system, owner, reporting cut-off and exception path.",
], bullets=["Pre-origination: eligibility, identity, affordability and collateral.", "Origination: authority, terms, documentation and disbursement controls.", "Servicing: mandate status, payments, complaints and account changes.", "Collections: contact, promise-to-pay, cure, recovery and escalation.", "Closure: no-dues, collateral release, reconciliation and record retention."], sources=["FY26 Annual Report, supplied PDF p.4 and pp.31–32."]),
pg("CHAPTER 2 · ORGANISATION", "Branch Network, Sourcing and Portfolio Reach", paragraphs=[
    "Fedfina's FY26 report states 757 branches across 17 states and union territories, with 148 branches added during the year. FY25 reports 694 branches across 18 states/UTs. The year-end network rose by 63 between those disclosed snapshots, not by 148; the reports do not provide a complete opening/closure/reclassification reconciliation in the cited summary. The two figures should therefore be reported as disclosed, not arithmetically conflated.",
    "The FY26 strategy describes greater in-house origination and branch co-location for Gold and LAP. Branch-level reporting should combine production with quality: vintage AUM, approval exceptions, early-bucket delinquency, bounce, cash reconciliation, customer complaints, audit findings and staff capacity. Growth without a control-capacity view can conceal emerging execution risk.",
], table={"headers":["Disclosure", "FY24", "FY25", "FY26"], "rows":[
    ["Year-end branches", "621", "694", "757"],
    ["States / UTs", "18", "18", "17"],
    ["FY26 additions", "—", "—", "148 reported additions"],
]}, note="FY26's 148 branch additions do not equal the 63 difference between FY25 and FY26 year-end counts; the source does not reconcile gross additions to net movement.", sources=["FY24 Annual Report, supplied PDF pp.6, 14; FY25 Annual Report, p.13; FY26 Annual Report, pp.4, 7."]),
pg("CHAPTER 2 · ORGANISATION", "FY26 Strategy and Portfolio Rebuild", paragraphs=[
    "FY2025–26 is described by management as a year of rebuilding, re-securing and strengthening collections. The annual report highlights the business-loan portfolio exit, Gold AUM growth, ST LAP redesign, increased direct origination, an expanded internal collections team, branch co-location and a Business Rule Engine. Those actions are relevant to risk because they change mix, origination control, recoveries, fixed-cost leverage and data availability.",
    "Management reported FY26 PAT growth of 52.6% to ₹343.6 crore and credit cost of 0.8%, while targeting quality-led growth for FY27. This report does not extend management's forward-looking statements into a forecast. The analyst's job is to convert strategic claims into observable tests: cohort performance, policy exceptions, cash collections, productivity, capital use, funding mix and customer outcomes.",
], bullets=["Risk change: from legacy business-loan exposure toward a more secured portfolio.", "Control change: system-driven ST LAP decisioning and verticalised collections.", "Funding change: more lenders, expanded ECB programme and a higher fixed-rate share.", "Execution test: new branch vintages and rehabilitated ST LAP cohorts must season safely."], sources=["FY26 Annual Report, supplied PDF pp.4, 13–14."]),

# Chapter 3, pp.26–35
pg("CHAPTER 3 · RISK LANDSCAPE", "Retail-NBFC Risk Context", paragraphs=[
    "A retail NBFC transforms funding into loans to borrowers who may be underserved by conventional channels. The model creates value when pricing covers the cost of funds, operating expense, expected credit losses, capital and liquidity. It can also amplify stress: a slowdown can reduce borrower cash flows, delay collections, increase delinquencies and constrain refinancing at the same time.",
    "Fedfina's reports position the Company in emerging retail credit, with Gold and Mortgage lending as its principal engines. Public market-growth narratives describe opportunity, but risk analysis must focus on the Company's realised portfolio quality, underwriting discipline, concentration, funding and control capacity rather than treating macro demand as a guarantee of repayment.",
], table={"headers":["Risk driver", "Potential channel into performance"], "rows":[
    ["Household / MSME cash flow", "Missed instalments, roll-forward delinquency and loss"],
    ["Interest-rate / funding cycle", "Higher borrowing costs or repricing mismatch"],
    ["Collateral market / legal process", "Lower recovery value or delayed enforcement"],
    ["Branch / digital scale", "Process, fraud, cyber and conduct exposure"],
    ["Regulatory change", "Policy redesign, systems cost and compliance risk"],
]}, sources=["FY24 Annual Report, supplied PDF pp.15, 24; FY26 Annual Report, pp.11–13."]),
pg("CHAPTER 3 · RISK LANDSCAPE", "Risk Governance: Board, RMC and ALCO", paragraphs=[
    "The FY26 annual report sets out the RMC's broad remit: risk identification and mitigation, internal controls, business continuity, monitoring systems, policy review, product-level delinquency and NPA oversight, and liquidity risk. It also requires information flow to the Board. ALCO is separately described as overseeing earnings-at-risk and asset-liability management. The monthly analyst pack should be designed to serve both decisions without blurring their mandates.",
    "The FY26 report records five RMC meetings during the year. Meeting frequency in an annual report should not be misread as proof of a quarterly meeting in every calendar quarter; the student's stated task is quarterly preparation of the pack. A good committee paper shows what changed, what breached, who owns remediation and which decisions are requested.",
], table={"headers":["Forum / line", "Primary oversight question"], "rows":[
    ["Board / RMC", "Are principal risks, policy and remediation adequately overseen?"],
    ["ALCO", "Are structural liquidity, funding, repricing and interest exposures controlled?"],
    ["Business (first line)", "Are controls performed and exceptions corrected at source?"],
    ["Risk / Compliance (second line)", "Are risks independently monitored and escalated?"],
    ["Internal Audit (third line)", "Are controls tested and findings closed independently?"],
]}, sources=["FY26 Annual Report, supplied PDF p.53 and pp.114–118; FY25 Annual Report, p.33."]),
pg("CHAPTER 3 · RISK LANDSCAPE", "Credit Risk and Portfolio Concentration", paragraphs=[
    "Credit risk is the possibility that a borrower or counterparty will not meet contractual obligations. It is driven by borrower capacity and willingness, underwriting quality, product design, geography, sector, sourcing channel, fraud, documentation and the effectiveness of collections. A collateralised portfolio can lower loss severity while leaving probability of default and operational execution risk intact.",
    "Concentration analysis should examine product, ticket size, vintage, state/district, branch, channel, borrower type, occupation, collateral type and funding counterparty. The FY26 annual report reports that the top five states represented 75.1% of AUM. A declining concentration ratio over the five-year chart is positive diversification evidence, but it still leaves a material share in the largest geographies and does not disclose district-level clustering.",
], bullets=["Measure both exposure share and quality by segment.", "Separate new-book vintages from legacy portfolios.", "Monitor correlated concentrations: same state, employer/industry, collateral market or collection route."], sources=["FY26 Annual Report, supplied PDF pp.7, 116–117."]),
pg("CHAPTER 3 · RISK LANDSCAPE", "Collateral, Valuation and Recovery Risk", paragraphs=[
    "Collateral affects loss given default; it does not automatically make an exposure low risk. Gold requires accurate purity/weight testing, packet custody and price monitoring. Property requires title, valuation, lien perfection, insurance where applicable, legal enforceability and a realistic time-to-sale estimate. Both require clear customer consent and release controls after repayment.",
    "A robust collateral dashboard records the latest valuation date, source and independence, margin/LTV, document exceptions, charge status, insurance, custody, location, revaluation triggers and recovery status. Haircuts should be policy-approved and stress-tested. The annual report's stated margin or collateral practices should not be treated as the confidential live trigger for an account.",
], table={"headers":["Collateral failure mode", "Potential control"], "rows":[
    ["Incorrect gold purity / weight", "Independent test, dual verification and exception audit"],
    ["Gold packet mismatch / loss", "Maker-checker, sealed custody, access log and surprise counts"],
    ["Title / charge defect", "Legal search, charge perfection and post-registration evidence"],
    ["Stale or optimistic valuation", "Independent valuer, ageing control and stress haircut"],
    ["Delayed recovery", "Track legal status, costs, notices and expected recovery time"],
]}, sources=["FY24 Annual Report, supplied PDF p.24; FY26 Annual Report, pp.116, 118."]),
pg("CHAPTER 3 · RISK LANDSCAPE", "Liquidity Risk and Asset-Liability Management", paragraphs=[
    "Liquidity risk is the risk that cash obligations cannot be met when due without unacceptable cost or loss. A lender can be solvent on a balance-sheet basis and still face a funding gap if contractual or behavioural cash outflows arrive before collections, liquid assets or committed facilities. The ALM view therefore needs maturity buckets, stress assumptions, available liquidity and contingent funding—not just total assets less total liabilities.",
    "FY26 disclosures include a maturity analysis at 31 March 2026. The reported net position is positive within one year and negative beyond one year. This is a disclosed contractual-maturity snapshot; it is not by itself the RBI structural liquidity statement, an intraday view, a stress survival period or proof that funds are freely available. Encumbrance, behavioural prepayment, rollover and collection stress should be assessed separately.",
], bullets=["Monitor cumulative cash-flow gaps by approved time bucket.", "Separate unencumbered liquid assets from pledged or restricted balances.", "Test delayed collections, reduced renewal, refinancing closure and higher drawdowns.", "Escalate breaches against approved ALM limits; do not invent public thresholds."], sources=["FY26 Annual Report, supplied PDF pp.114–115, 118."]),
pg("CHAPTER 3 · RISK LANDSCAPE", "Interest-Rate and Foreign-Currency Risk", paragraphs=[
    "Interest-rate risk arises when asset yields and liability costs reprice at different speeds, frequencies or amounts. Rising funding cost can compress spread and NII if loan repricing lags; falling rates can also affect income where assets reprice faster than liabilities or where fixed-rate assets are funded with variable-rate borrowing. Tenor, reset dates, fixed/floating mix and customer prepayment all matter.",
    "The FY26 report discloses an earnings-at-risk framework and a 25-basis-point sensitivity table for loans and borrowings. It also states that foreign-currency borrowing exposures are hedged through derivatives to fix functional-currency outflows. A risk analyst should report gross sensitivities and hedge effectiveness separately, then reconcile the net impact under the approved ALCO model.",
], table={"headers":["Exposure", "Monitoring view"], "rows":[
    ["Asset repricing", "Product yield, reset date, fixed/floating share"],
    ["Liability repricing", "Borrowing reset, maturity and lender concentration"],
    ["Basis / timing", "Gap between asset and liability repricing cycles"],
    ["FX borrowing", "Notional, hedge ratio, maturity and counterparty"],
]}, sources=["FY26 Annual Report, supplied PDF pp.15, 118."]),
pg("CHAPTER 3 · RISK LANDSCAPE", "Operational, Fraud and Process Risk", paragraphs=[
    "Operational risk can arise from people, processes, systems and external events. In lending, examples include wrong data entry, unauthorised approval, incomplete documentation, duplicate applications, misdirected disbursement, collateral handling failure, cash/reconciliation breaks and delayed complaint resolution. Fraud risk overlaps with credit and operational risk but should have its own incident taxonomy and investigation controls.",
    "The FY25 report describes a three-lines-of-defence framework, segregation of duties, access and authorisation controls, reconciliations, employee training, a fraud-control unit and incident root-cause analysis. These are management disclosures; a public report cannot prove operating effectiveness. Monitoring should connect incidents, near misses, loss events, audit findings, overdue actions and repeat causes.",
], bullets=["Record gross and net loss, recovery, root cause and control owner.", "Do not close an incident only because a system ticket was raised.", "Review access rights and privileged-user activity after role changes.", "Test branch controls through samples, surprise checks and independent reconciliation."], sources=["FY25 Annual Report, supplied PDF p.33; FY24 Annual Report, p.24."]),
pg("CHAPTER 3 · RISK LANDSCAPE", "Cyber, Data and Third-Party Risk", paragraphs=[
    "Digital workflows can improve speed and consistency but create dependency on core platforms, APIs, identity services, payment rails, cloud or technology vendors, telecom connectivity and data quality. A cyber incident can interrupt sourcing or servicing, expose personal data, enable fraud and damage customer trust. Resilience requires preventive, detective and recovery controls across the full third-party chain.",
    "The FY25 report describes continuous security monitoring, vulnerability assessment and penetration testing, incident response, vendor risk and business-continuity oversight. The FY26 report describes a system-driven ST LAP model and digital collection adoption. These disclosures suggest an expanding technology surface; the risk analyst should ask whether incidents, vulnerabilities, outages and recovery tests are measured consistently and escalated to accountable owners.",
], table={"headers":["KRI example", "Evidence / escalation"], "rows":[
    ["Critical-system availability", "Service logs, outage minutes, root cause and recovery test"],
    ["Open high-severity vulnerabilities", "Ageing, owner, compensating control and closure evidence"],
    ["Third-party incidents", "Materiality, data/system impact and contractual notice"],
    ["Data-quality exceptions", "Reconciliation breaks, duplicate records and correction ageing"],
]}, sources=["FY25 Annual Report, supplied PDF p.33; FY26 Annual Report, pp.13, 32."]),
pg("CHAPTER 3 · RISK LANDSCAPE", "Regulatory, Conduct, Reputational and ESG Risk", paragraphs=[
    "Regulatory risk includes failure to identify, interpret, implement or evidence applicable requirements. Conduct risk includes unsuitable sales, unclear terms, unfair collection behaviour, weak consent, incorrect charges or unresolved grievances. Such issues can create penalties, remediation cost, customer harm and reputational damage even before a financial loss is recognised.",
    "The FY26 RMC terms of reference expressly include financial, operational, sectoral, sustainability, information and cyber risks and business continuity. The annual report also describes customer-service indicators and ESG disclosures. A balanced risk pack should combine prudential measures with complaints, turnaround-time failures, responsible collection, privacy, inclusion and relevant environmental-risk signals, using definitions approved by the Company.",
], bullets=["Track complaints by product, root cause, ageing and repeat occurrence.", "Monitor collection conduct and customer-impact indicators alongside recovery.", "Assess regulatory changes for policy, system, training and evidence requirements.", "Link ESG risk to portfolio, operations and governance—not only expenditure."], sources=["FY26 Annual Report, supplied PDF pp.4, 21, 53; FY25 Annual Report, p.33."]),
pg("CHAPTER 3 · RISK LANDSCAPE", "How Risks Interact", paragraphs=[
    "Risks rarely appear in isolation. A local economic shock can weaken small-business cash flow; a failed payment mandate raises bounce volumes; delayed collection moves accounts into higher DPD buckets; falling property liquidity or gold prices can lower collateral coverage; provisions and recovery costs affect profit; and funding markets may become less receptive if asset quality weakens. Rapid expansion can intensify every link when controls and staffing lag.",
    "Risk reporting should therefore show leading and lagging measures together. Leading indicators include application quality, policy exceptions, mandate success, borrower contactability, collateral margin, branch productivity and complaint trends. Lagging indicators include GNPA, write-offs, provisions, loss and legal recovery. A single traffic light is insufficient unless it shows the underlying driver, time horizon, owner and remediation.",
], table={"headers":["Shock", "Transmission chain", "Monitoring link"], "rows":[
    ["Borrower cash-flow stress", "Bounce → arrears → Stage migration → loss", "Bounce, roll-rate, cure, ECL"],
    ["Gold-price fall", "Lower collateral cushion → margin pressure", "LTV distribution, price stress, overdue"],
    ["Funding spread widening", "Higher CoF → lower NII / liquidity strain", "Maturity, repricing, undrawn lines"],
    ["Technology outage", "Servicing delay → missed receipts / complaints", "Availability, back-up, reconciliation"],
]}, note="The matrix is an analytical pathway, not a claim that any one event occurred at Fedfina.", sources=[]),

# Chapter 4, pp.36–44
pg("CHAPTER 4 · METHODOLOGY", "Research Methodology", paragraphs=[
    "A descriptive, secondary-data design is used. The three supplied annual reports form the evidence base; the FY26 report is the primary period, while FY24 and FY25 provide context and cross-checks. The analysis includes trend comparisons, year-on-year calculations, ratio interpretation, maturity and sensitivity disclosures, and qualitative risk-control mapping.",
    "No statistical causal model is estimated because the repository does not contain monthly borrower- or product-level observations. No internal policy limit, trigger or committee finding is inferred. This distinction protects the analysis from converting an illustrative academic framework into a false company disclosure.",
], table={"headers":["Method", "Application"], "rows":[
    ["Trend analysis", "FY22–FY26 series reported in FY26 report"],
    ["Comparative review", "FY24/FY25/FY26 as-reported checks"],
    ["Ratio / sensitivity", "Transparent calculations with units and assumptions"],
    ["Process design", "Monthly and quarterly templates for the stated internship tasks"],
]}, sources=["All three supplied annual reports; source map on p.89."]),
pg("CHAPTER 4 · METHODOLOGY", "Source Hierarchy and Evidence Labels", paragraphs=[
    "Every company-specific statement is tagged mentally—and, for material facts, visibly—as an audited financial-statement figure, company-reported operational KPI, management narrative, author calculation or proposed monitoring method. These categories have different assurance and precision. The report does not present a management narrative or future aspiration as a realised financial result.",
    "When annual reports disagree on a historical metric, the latest FY26 five-year chart is used for the trend and the earlier as-reported figure is retained in the reconciliation note. This is a transparent selection rule, not proof that the later series is the only valid measure. The reader should use the FY26 report's definition and audited notes for formal decisions.",
], table={"headers":["Label", "Meaning", "Example"], "rows":[
    ["Reported", "Stated in source", "FY26 AUM ₹20,153 crore"],
    ["Calculated", "Formula applied to reported values", "FY26 AUM growth ≈27.5%"],
    ["Interpretation", "Analyst's explanation / implication", "Growth raises monitoring demands"],
    ["Illustrative", "Proposed template or scenario only", "Blank policy-trigger test sheet"],
]}, sources=["FY26 Annual Report, supplied PDF pp.4, 14–15; FY25 Annual Report, pp.12–13."]),
pg("CHAPTER 4 · METHODOLOGY", "Data Extraction, Validation and Unit Control", paragraphs=[
    "The annual reports state some balance-sheet values in ₹ lakh, selected trends in ₹ million and the company overview in ₹ crore. This report converts ₹ million to ₹ crore by dividing by 10 and ₹ lakh to ₹ crore by dividing by 100. Percentages and ratios are not converted. Rounded values are shown with limited decimal precision, and small differences may arise from rounding.",
    "For every extracted figure, record the report year, PDF page, printed annual-report page where visible, label, period, unit, basis and whether it is audited or operational. Cross-check labels visually against the charts because PDF text extraction may reorder chart values. Do not copy values from search snippets without inspecting the page.",
], bullets=["1 crore = 10 million = 100 lakh.", "Keep source precision in working notes; round only for display.", "Check sign, basis, reporting date and denominator before comparing.", "Reconcile derived totals; if a source does not reconcile, disclose the gap."], sources=["FY26 Annual Report, supplied PDF pp.14–15, 114–118."]),
pg("CHAPTER 4 · METHODOLOGY", "Ratio and Trend Analysis", paragraphs=[
    "AUM growth is calculated as (closing AUM this year ÷ closing AUM last year) − 1. A year-on-year change in a percentage ratio is reported in percentage points; a relative percentage change is a different calculation. ROA and ROE are taken from the company's chart series, not recomputed from closing assets or equity because the denominator conventions may differ.",
    "GNPA and NNPA are asset-quality indicators with different provisioning treatments. PCR is interpreted with its disclosed basis and should not be treated as a stand-alone estimate of recovery. CRAR is a capital-adequacy measure, while leverage and funding maturities provide separate context. Ratio interpretation is therefore paired with product, vintage, funding and operational views.",
], table={"headers":["Indicator", "Basic interpretation"], "rows":[
    ["AUM growth", "Scale change; pair with quality and funding"],
    ["PAT / ROA / ROE", "Profit and return; assess denominator and leverage"],
    ["GNPA / NNPA / PCR", "Delinquency and reserve context; definitions matter"],
    ["CRAR", "Capital buffer relative to risk-weighted assets"],
    ["Spread / CoF", "Pricing less funding-cost context; not full NIM analysis"],
]}, sources=["FY26 Annual Report, supplied PDF pp.14–15."]),
pg("CHAPTER 4 · METHODOLOGY", "EWS and Portfolio-Monitoring Method", paragraphs=[
    "An early-warning signal is a measurable indicator that may precede delinquency, loss, conduct failure or liquidity pressure. An EWS is not a prediction of default by itself. Each signal needs a definition, population, frequency, source, threshold authority, false-positive review, owner and action deadline. Segmentation by product, vintage, channel and geography makes the signal more useful than a single company-wide average.",
    "Potential credit EWS include mandate failure, repeated bounce, excess utilisation, missed promise-to-pay, bureau deterioration where lawfully available, adverse cash-flow movement, collateral-margin erosion and abnormal early closure or top-up patterns. These examples are proposed analytical categories; only approved internal indicators and definitions should be used for actual company reporting.",
], table={"headers":["Signal family", "Example measure", "Follow-up"], "rows":[
    ["Payments", "First-presentment success / repeated returns", "Separate technical and customer causes"],
    ["Delinquency", "DPD roll-forward and cure rate by vintage", "Validate account population and cut-off"],
    ["Collateral", "LTV / valuation-age / exception count", "Apply approved revaluation and escalation rules"],
    ["Operations", "Reconciliation breaks / unresolved complaints", "Assign owner and ageing-based escalation"],
]}, sources=["FY25 Annual Report, supplied PDF p.33; FY26 Annual Report, p.116."]),
pg("CHAPTER 4 · METHODOLOGY", "Policy Trigger Versus Actual: Analytical Rule", paragraphs=[
    "A trigger comparison is valid only when the approved policy threshold, direction of breach, population, reporting date and actual value refer to the same definition. A high-is-bad limit and a low-is-bad floor need different logic. The comparison should preserve the official threshold and should not substitute an analyst's preferred benchmark.",
    "The report recommends a register with the policy clause, indicator, approved limit, actual, headroom, status, duration, root cause, compensating controls, accountable owner, due date, escalation forum and evidence of closure. No Fedfina-specific threshold is available in the supplied files, so Appendix F deliberately leaves policy-limit fields blank.",
], bullets=["Confirm current approved policy version and effective date.", "Validate denominator, scope, cut-off and data lineage.", "Record breach even if subsequently cured; retain the event trail.", "Escalate repeated near-breaches as well as formal breaches."], note="No numeric policy trigger in this report should be used as an internal Fedfina limit.", sources=["FY25 Annual Report, supplied PDF p.33; FY26 Annual Report, pp.53, 116."]),
pg("CHAPTER 4 · METHODOLOGY", "Bounce-Analysis Method", paragraphs=[
    "A payment bounce is a presentment or mandate outcome, not automatically a credit default. Count bounce rate is bounced presentments divided by total valid presentments; amount bounce rate is bounced value divided by presented value. A portfolio should define whether retries, reversals, duplicates and technical returns are included, and should avoid double-counting the same instalment.",
    "Useful cuts include product, due-date cycle, vintage, branch, channel, mandate type, return code, first-time versus repeat, amount band and cure window. Separate technical failures from insufficient funds or other customer-related returns. Pair the bounce trend with subsequent DPD, collection efficiency, cure and complaint metrics to see whether an operational event became a credit event.",
], table={"headers":["Measure", "Formula"], "rows":[
    ["Count bounce rate", "Valid bounced presentments ÷ valid total presentments"],
    ["Amount bounce rate", "Returned amount ÷ presented amount"],
    ["Cure rate", "Bounced accounts cured within defined window ÷ bounced accounts"],
    ["Repeat bounce rate", "Accounts with ≥2 returns ÷ accounts presented"],
]}, note="No actual monthly bounce dataset was supplied; this page specifies a method, not a Fedfina result.", sources=[]),
pg("CHAPTER 4 · METHODOLOGY", "Monthly Risk Paper and Quarterly RMC Pack", paragraphs=[
    "The monthly risk paper is a concise management document that records period performance, movement against risk appetite, emerging exceptions, portfolio drivers and actions. It should state what changed since the last month, why it changed, whether the movement is persistent, what decision is needed and who owns the response. Definitions and cut-off dates belong beside the chart, not in an analyst's memory.",
    "The quarterly RMC pack escalates material and cross-functional matters. It should synthesise monthly trends, concentration, asset quality, liquidity/ALM, capital, market, operational, cyber, compliance and customer risks, and track prior committee actions. The FY26 annual report's RMC terms of reference support this broad view; committee material itself remains internal and is not reproduced here.",
], bullets=["Monthly: management dashboard, exceptions, root cause and action log.", "Quarterly: risk appetite, systemic themes, stress, material incidents and decisions.", "Both: source, definition, owner, due date, evidence and escalation status."], sources=["FY26 Annual Report, supplied PDF p.53; FY25 Annual Report, p.33."]),
pg("CHAPTER 4 · METHODOLOGY", "Confidentiality, Integrity and Limitations", paragraphs=[
    "A workplace risk analyst may see non-public customer, portfolio, policy and committee data. Such data should only be used in the authorised work environment and only in accordance with company policy and academic permission. It should not be copied into a public repository, personal report or Git history. This project intentionally contains no customer-level information or confidential Fedfina policy limits.",
    "A student should keep source files, formulas and review evidence traceable, disclose estimates, avoid retrofitting a narrative after seeing outcomes, and seek supervisor approval for external circulation. The templates in this report are blank academic formats. Before submission, the student should confirm permission for internship details, guide names, the institution's certificate wording and the interpretation of the task-list term 'ever graphs'.",
], bullets=["Do not publish internal data, borrower identifiers or committee deliberations.", "Do not imply an employer-issued certificate without the original signed document.", "Do not present a blank template as completed internship evidence.", "Use the latest authorised policy and data dictionary for any live comparison."], sources=[]),

# Chapter 5, pp.45–61
pg("CHAPTER 5 · FY26 ANALYSIS", "FY26 Risk and Financial Dashboard", paragraphs=[
    "The FY26 annual report snapshot shows scale, growth and improvement in several return measures, alongside asset-quality and execution indicators that require continued monitoring. The dashboard below deliberately places profitability and risk side by side. A year-end ratio is a point-in-time or annual summary; it does not show volatility within the year or quality by cohort.",
    "The snapshot reports AUM of ₹20,153 crore, secured AUM of 98.9%, GNPA 1.9%, NNPA 1.3%, credit cost 0.8%, ROA 2.4%, ROE 12.6%, disbursements ₹31,410 crore and PAT ₹343.6 crore. These are company-disclosed headline indicators; their calculation bases should be checked in the underlying disclosures before peer comparison.",
], table={"headers":["FY26 indicator", "Reported value", "Risk reading"], "rows":[
    ["AUM / disbursement", "₹20,153 Cr / ₹31,410 Cr", "Scale and origination pace; quality by vintage needed"],
    ["Secured AUM", "98.9%", "Lower unsecured share; collateral execution remains material"],
    ["GNPA / NNPA", "1.9% / 1.3%", "Gross improved; net rose from 1.2% in FY25 chart"],
    ["Credit cost", "0.8%", "Below 1%; sustainability depends on cohorts and collections"],
    ["PAT / ROA / ROE", "₹343.6 Cr / 2.4% / 12.6%", "Strong recovery; assess funding, leverage and repeatability"],
]}, sources=["FY26 Annual Report, supplied PDF p.4 and pp.14–15."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "AUM Growth and Scale", paragraphs=[
    "The latest five-year series shows AUM rising from ₹6,187.2 crore in FY22 to ₹20,153 crore in FY26. On the reported closing figures, FY26 AUM grew approximately 27.5% year on year; the FY22–FY26 compound annual growth rate is approximately 34.3%. These are author calculations from company-reported values, not an independently audited reconstruction of monthly balances.",
    "AUM growth is a scale measure, not a standalone success measure. It should be decomposed into product, vintage, geographic and channel contributions, and viewed with credit cost, cost of funds, branch maturity, capital consumption and collection performance. A rapid secured-AUM expansion can still create concentration, collateral and execution risks.",
], chart="aum", note="₹ million values in the FY26 chart are divided by 10 to display ₹ crore. CAGR is calculated over four annual intervals.", sources=["FY26 Annual Report, supplied PDF p.14; FY24 Annual Report, p.13; FY25 Annual Report, p.12."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Profitability, ROA and ROE", paragraphs=[
    "Reported PAT increased from ₹225.2 crore in FY25 to ₹343.6 crore in FY26, a calculated year-on-year increase of about 52.6%. The FY26 five-year chart also shows a FY25 dip after FY24 growth. ROA moved from 1.8% to 2.4% and ROE from 9.4% to 12.6% in that latest chart series. Profit recovery is positive, but should be tested against core income, provisioning, cost of funds and one-off or portfolio-mix effects.",
    "ROE can increase because of higher earnings, lower equity, leverage or combinations of these. ROA is less directly affected by capital leverage but still depends on the averaging convention and portfolio composition. The analyst should not infer that profitability is sustainable from a single annual comparison; quarterly and vintage views are required.",
], chart="profitability", note="PAT is shown in ₹ crore; return ratios are the company's disclosed trend series. Values are rounded.", sources=["FY26 Annual Report, supplied PDF pp.4, 14–15; FY25 Annual Report, pp.12–13."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Yield, Spread and Funding-Cost Trend", paragraphs=[
    "The FY26 report's five-year chart shows FY26 yield of 16.7%, spread of 8.6%, cost of borrowings of 8.1% and cost-to-income of 57.2%. Relative to FY25 in that same chart, yield is lower by 0.4 percentage point while spread is higher by 0.4 point and borrowing cost is lower by 0.9 point. Such movements can reflect pricing, product mix, funding mix or methodology; the report does not attribute every change to one cause.",
    "Prior annual reports present different historical yield/spread/cost-of-borrowing values for some years. For this plot, the latest FY26 five-year series is used consistently. Before calculating a live NIM or price-versus-cost gap, use the exact approved metric definitions and distinguish nominal yield, spread, net interest margin and cost of funds.",
], chart="pricing", note="Historical series in FY26 report differs from selected FY25 report disclosures; see reconciliation on p.89. Do not splice series silently.", sources=["FY26 Annual Report, supplied PDF pp.14–15; FY25 Annual Report, p.12."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Asset Quality and Provision Coverage", paragraphs=[
    "The FY26 latest five-year chart shows GNPA at 1.9% versus 2.0% in FY25, while NNPA rises from 1.2% to 1.3%. Provision coverage is 32.3% versus 40.0% in FY25 in the same series. The measures do not move in lockstep: gross delinquency can improve while net NPA or coverage changes because exposures, provisions, write-offs and stage mix also change.",
    "The FY25 report described 1.7% credit cost for the rebuild year, while the FY26 report states 0.8% credit cost and a 93-basis-point decline. GNPA and credit cost answer different questions: GNPA is a stock ratio at a date; credit cost is a period flow/ratio. Monitor both with Stage 2, roll rates, write-offs, recoveries and vintage loss.",
], chart="asset_quality", note="No account-level delinquency, Stage 2 or bounce series was provided; conclusions are limited to published aggregate indicators.", sources=["FY26 Annual Report, supplied PDF pp.4, 15; FY25 Annual Report, p.13."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Capital Adequacy and Return Profile", paragraphs=[
    "The FY26 five-year chart reports CRAR of 22.4% in FY26, compared with 21.9% in FY25. The ratio is a regulatory capital measure and should be interpreted against minimum requirements, buffers, risk-weighted asset growth, capital planning and the Company's own approved appetite. A headroom calculation requires the applicable requirement and the precise standalone/consolidated basis.",
    "The same chart reports ROE of 12.6% in FY26. Rising AUM may consume capital even when the portfolio is secured. The analyst should link projected disbursements and product risk weights to capital usage, retained earnings, dividend policy and direct-assignment/co-lending choices. Public CRAR is a year-end indicator, not a guarantee of future capacity.",
], chart="capital", note="No internal capital target or trigger is available in the supplied repository; none is inferred here.", sources=["FY26 Annual Report, supplied PDF p.15; FY25 Annual Report, p.13."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Secured-AUM Progression and Mix", paragraphs=[
    "Company disclosures describe a rising secured share: 85.0% in FY24, 89.5% in FY25 and 98.9% in FY26. The FY26 change accompanies the reported ₹886 crore business-loan portfolio exit and a stronger Gold/LAP focus. This is a material change in portfolio structure and likely alters the composition of credit and operational risks; it does not eliminate borrower default, collateral valuation, recovery timing or fraud risk.",
    "The three annual reports are not a uniform account-level panel, and the secured percentage is a rounded company-level disclosure. The figures are presented as reported, with no attempt to infer product balances from the residual. A robust follow-up would examine each product's cohort loss, LTV, cash-flow coverage, maturity, regional mix and collection cost.",
], chart="secured_mix", note="Reported company disclosures: FY24 85%; FY25 89.5%; FY26 98.9%. Comparability should be confirmed against the applicable AUM definition.", sources=["FY24 Annual Report, supplied PDF p.31; FY25 Annual Report, p.33; FY26 Annual Report, pp.4, 8."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Gold Portfolio: Growth and Collateral Sensitivity", paragraphs=[
    "FY26 Gold AUM reached ₹10,352 crore, up 76% year on year, and gold under custody reached 12.6 tonnes, up 12%. The report also states Gold AUM per branch of ₹16.5 crore. The difference between value growth and tonnage growth indicates that price and balance movements should be separated when assessing collateral coverage and business expansion.",
    "Gold-price stress can affect collateral margin, customer behaviour, renewal economics and portfolio growth. The FY26 financial-statement note states that the RMC periodically reviews price movement and stress impact; the FY25 report describes historical-volatility and hypothetical 10–20% declines. These are described stress examples, not company policy triggers supplied for this report. Any LTV analysis must use the approved valuation, margin and customer-notice rules.",
], table={"headers":["FY26 disclosure", "Value", "Monitoring implication"], "rows":[
    ["Gold AUM", "₹10,352 Cr; +76% YoY", "Separate price, disbursement, renewal and repayment effects"],
    ["Gold under custody", "12.6 tonnes; +12% YoY", "Physical quantity / custody reconciliation"],
    ["Gold AUM per branch", "₹16.5 Cr", "Pair productivity with quality and control exceptions"],
    ["Annual report stress example", "10–20% price decline (FY25 narrative)", "Scenario only; not a stated FY26 policy limit"],
]}, sources=["FY26 Annual Report, supplied PDF pp.13, 116; FY25 Annual Report, p.33."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Mortgage Portfolio and ST/MT LAP Signals", paragraphs=[
    "FY26 management disclosures report ST LAP disbursals of ₹904 crore for the year, including ₹289 crore in Q4, up 39% sequentially. MT LAP disbursals were ₹2,180 crore, with ₹632 crore in Q4, up 16% sequentially. Average ticket sizes and origination yields differ materially between ST and MT; therefore a combined mortgage metric can mask cohort and risk differences.",
    "The Company reports that 82.2% of Mortgage AUM was backed by self-occupied residential or commercial property. Monitoring should examine origination quality, early-bucket delinquency, property title/valuation exceptions, borrower leverage, sector and geography, collections capacity and the performance of post-rebuild vintages. A single quarter's disbursement momentum is not evidence of mature-book quality.",
], table={"headers":["FY26 item", "ST LAP", "MT LAP"], "rows":[
    ["Annual disbursals", "₹904 Cr", "₹2,180 Cr"],
    ["Q4 disbursals", "₹289 Cr (+39% sequential)", "₹632 Cr (+16% sequential)"],
    ["Average ticket size", "₹16.1 lakh", "₹72.4 lakh"],
    ["Origination yield", "15.1%", "12.0%"],
]}, note="These are annual-report operating disclosures; they are not monthly intern portfolio results.", sources=["FY26 Annual Report, supplied PDF p.13."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Expected Credit Loss and Staging", paragraphs=[
    "The FY26 risk note describes an expected-credit-loss framework using Exposure at Default (EAD), Probability of Default (PD) and Loss Given Default (LGD), adjusted for historical and forward-looking information. The model is an accounting estimate, not a direct count of future defaults. Model governance includes data quality, calibration, scenario weights, overlays, validation, approval and back-testing.",
    "The disclosed staging framework treats Stage 1 as current/early delinquency, Stage 2 as 30–89 DPD and specified restructuring cases, and Stage 3 as 90+ DPD or other qualifying conditions. The Company states that 30+ DPD is a quantitative significant-increase-in-credit-risk indicator and also considers qualitative factors, including restructuring or gold-loan LTV/margin. Account-level staging follows the detailed policy and accounting notes.",
], table={"headers":["Concept", "Analytical meaning"], "rows":[
    ["EAD", "Exposure expected to be outstanding at default"],
    ["PD", "Likelihood of default over the relevant horizon"],
    ["LGD", "Share of exposure not expected to be recovered after default"],
    ["ECL", "Probability-weighted expected cash shortfall / impairment estimate"],
]}, note="Stage descriptions are summarised from the FY26 annual-report note; consult the full policy/accounting note for edge cases.", sources=["FY26 Annual Report, supplied PDF p.116; FY24 Annual Report, pp.198–199."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Liquidity: Disclosed Maturity Analysis", paragraphs=[
    "The FY26 maturity table reports a net asset position of ₹4,976.24 crore within one year and a net liability position of ₹2,050.13 crore after one year, leaving a total net position of approximately ₹2,926.08 crore. The author converts the note's ₹ lakh values to ₹ crore. The positive total does not cancel the negative longer-tenor bucket or prove liquidity under stress.",
    "A practical ALM review should reconcile contractual maturities with behavioural cash flows, eligible liquid assets, pledged balances, undrawn facilities, rollover assumptions, collection stress and concentration of funding maturities. The report's maturity note is a static reporting-date analysis; it should not be represented as the complete structural-liquidity statement or a stress survival horizon.",
], chart="liquidity", table={"headers":["Maturity bucket", "Net position disclosed", "₹ crore"], "rows":[
    ["Within 1 year", "₹4,97,624 lakh", "+4,976.24"],
    ["After 1 year", "₹(2,05,013) lakh", "−2,050.13"],
    ["Total", "₹2,92,608 lakh", "+2,926.08"],
]}, note="Converted from the FY26 financial-statement maturity analysis; rounding explains small addition differences.", sources=["FY26 Annual Report, supplied PDF pp.114–115."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Interest-Rate Sensitivity: Disclosed 25 bp Shock", paragraphs=[
    "The FY26 financial-statement note presents separate profit-after-tax sensitivities for loans and borrowings at a 25-basis-point increase/decrease, holding other variables constant. For a 25 bp upward shock, the table shows a ₹652 lakh positive loan sensitivity and a ₹1,479 lakh negative borrowing sensitivity; the reverse shock reverses each sign. These are separate gross sensitivities as disclosed.",
    "A naïve netting of the two values would ignore repricing timing, instrument mix, floors/caps, hedge positions and model assumptions. The proper analysis is a reconciled ALCO earnings-at-risk view, with parallel and non-parallel shocks, behavioural assumptions and documented limits. The sensitivity is a useful illustration of why both sides of the balance sheet matter.",
], chart="rate_sensitivity", note="₹652 lakh = ₹6.52 crore; ₹1,479 lakh = ₹14.79 crore. Do not treat the separate values as a verified combined forecast.", sources=["FY26 Annual Report, supplied PDF p.118."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Funding Mix, Cost and Refinance Risk", paragraphs=[
    "The FY26 management discussion describes a broader lender base, rising from 39 to 41, an expanded USD 250 million external-commercial-borrowing programme, and a fixed-rate borrowing component of about 40% versus about 10% in FY25. It also reports that daily average borrowing cost eased from 8.72% in Q4 FY25 to 7.83% in Q4 FY26. These measures suggest diversification and repricing changes, but require maturity- and currency-specific review.",
    "Funding concentration should be measured by lender, instrument, currency, secured/unsecured status, reset date, maturity, covenant and collateral encumbrance. A diversified lender count can still conceal dependence on a few large counterparties or market channels. A risk paper should distinguish contracted funding, sanctioned but undrawn lines and assumed refinancing.",
], bullets=["Track top-lender share and maturity concentration.", "Map ECB principal, hedges, rollover and counterparty limits.", "Monitor fixed/floating mix and asset-liability repricing gaps.", "Link cost-of-funds changes to product yields, spreads and customer pricing."], sources=["FY26 Annual Report, supplied PDF p.13 and p.10."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Operational, Collection and Digital Indicators", paragraphs=[
    "FY26 describes a rebalanced origination and collection architecture: around 75% of business originated by in-house teams, DSA dependence at 25%, internal collections team scaled to 1.8 times FY25 levels and external agency reliance reduced to 0.4 times. Management reports improved cure rates and monthly Stage 3 recoveries rising from ₹6.5 crore to ₹14.5 crore. These are management-reported changes; the report does not independently test attribution or denominator definitions.",
    "Digital mandate and collection adoption can improve evidence and reduce manual delay, but reconciliation, access, exceptions, vendor continuity and customer consent remain essential. A monthly dashboard should show channel-level cash conversion and failed collections, not only digital adoption. Recovery improvement should be paired with conduct, complaint and cost-to-collect indicators.",
], table={"headers":["FY26 management disclosure", "Reported movement"], "rows":[
    ["Direct / in-house sourcing", "~75% in-house; DSA ~25%"],
    ["Internal collections team", "1.8× FY25 level"],
    ["External agency reliance", "0.4× FY25 level"],
    ["Monthly Stage 3 recoveries", "₹6.5 Cr to ₹14.5 Cr"],
    ["Digital collections", ">70% of monthly collections via digital channels"],
]}, sources=["FY26 Annual Report, supplied PDF pp.13–14."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Geographic, Branch and Operating Concentration", paragraphs=[
    "Fedfina reports 757 branches across 17 states/UTs at FY26 year-end. The annual-report series shows top-five-state AUM concentration at 75.1% for FY26, down from 76.0% in FY25. This is gradual geographic diversification, yet a material majority of AUM remains in five states. A state-level average can also conceal district, branch or borrower-industry concentration.",
    "Branch performance should be segmented by vintage and product, including new and co-located branches. Productivity is not just AUM per branch: compare disbursals, active accounts, collection efficiency, staff capacity, audit exceptions, cash/collateral controls, complaint rates and local market conditions. The disclosed 148 additions need opening/closure reconciliation before productivity comparisons.",
], table={"headers":["Measure", "FY25", "FY26", "Interpretation"], "rows":[
    ["Year-end branches", "694", "757", "Network expanded; vintage and net movement matter"],
    ["States / UTs", "18", "17", "Footprint count alone does not show exposure share"],
    ["Top 5 states' AUM", "76.0%", "75.1%", "Slow diversification; concentration remains material"],
]}, sources=["FY25 Annual Report, supplied PDF p.13; FY26 Annual Report, pp.7, 13."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Stress Testing and Scenario Design", paragraphs=[
    "Stress testing asks how earnings, capital, liquidity and collections respond to severe but plausible changes. It should be forward-looking, multi-factor and linked to actions. A single 10% gold-price decline or uniform delinquency uplift may not capture correlated shocks: stressed borrowers may cure less, collateral may be harder to sell, funding cost may rise and new-business volumes may slow together.",
    "A practical design uses a base, adverse and severe-but-plausible scenario, with separate product and vintage assumptions. For secured lending, include gold price/LTV, property recovery haircut and time-to-recovery, payment-bounce and roll-forward, cost of funds, branch productivity, direct-assignment capacity and liquidity outflow. Scenario values in Appendix I are blank assumptions to be approved, not Fedfina forecasts.",
], bullets=["Specify shock size, horizon, affected population and source.", "Translate the shock into loss, ECL, PAT, capital and cash-flow effects.", "Document management actions, feasibility and time lag.", "Back-test assumptions against historical outcomes and model limitations."], note="FY25's 10–20% gold-price drop is cited as a stress-test example in management narrative—not an approved FY26 risk limit.", sources=["FY25 Annual Report, supplied PDF p.33; FY26 Annual Report, pp.116, 118."]),
pg("CHAPTER 5 · FY26 ANALYSIS", "Integrated Risk Assessment and Watchlist", paragraphs=[
    "Public disclosures indicate strong FY26 growth, higher profitability, a very high secured share, improved GNPA and sub-1% credit cost. Counter-signals deserve attention: NNPA rose 0.1 percentage point in the latest chart, provision coverage eased from 40.0% to 32.3%, yield fell while spread improved, a large branch expansion is still seasoning, and mortgage rehabilitation requires cohort evidence. None alone proves deterioration; together they justify targeted monitoring.",
    "The watchlist should focus on early-book quality in ST LAP, branch vintage performance, gold collateral margin and custody, the sustainability of collections gains, longer-tenor maturity mismatch, cost and repricing of borrowings, capital use, top-state concentration and cyber/operational incidents. Internal policies determine formal triggers; this list is an external analyst's prioritisation, not an official company risk rating.",
], table={"headers":["Watch item", "Why it matters", "Evidence needed"], "rows":[
    ["ST LAP vintage", "Rebuild and faster Q4 disbursal", "30/60/90 DPD, cure, loss by cohort"],
    ["Gold collateral", "AUM grew faster than custody tonnage", "LTV distribution, price stress, custody audit"],
    ["Collections", "Reported cure/recovery improvement", "Definitions, sample, cost and conduct outcomes"],
    ["Longer-tenor ALM", "Negative after-one-year net gap disclosed", "Stress buckets, liquidity buffer and plan"],
    ["Reserves / quality", "NNPA up; PCR lower year on year", "Stage mix, overlays, write-offs, provisioning basis"],
]}, sources=["FY26 Annual Report, supplied PDF pp.4, 13–15, 114–118."]),

# Chapter 6, pp.62–69
pg("CHAPTER 6 · INTERNSHIP", "Internship Profile and Role", paragraphs=[
    "The student-provided internship particulars are: Dattaguru Patil, S.Y. MMS (SYMMS), Roll No. M16144; Risk Analyst Intern at Fedbank Financial Services Ltd; 4 April 2026 to 3 July 2026. The task list provided describes recurring reporting and analysis work. The report documents those responsibilities as a workflow and does not assert a particular unpublished monthly outcome or committee decision.",
    "A risk analyst supports decisions by making the data accurate, comparable, timely and actionable. The analyst does not change a policy limit, make a lending decision outside delegated authority, or treat a chart as a conclusion without checking the underlying population, denominator and exception context.",
], table={"headers":["Internship detail", "Student-supplied information"], "rows":[
    ["Student", "Dattaguru Patil; S.Y. MMS (SYMMS)"],
    ["Roll number", "M16144"], ["Organisation", "Fedbank Financial Services Ltd"],
    ["Role", "Risk Analyst Intern"], ["Period", "4 Apr 2026 – 3 Jul 2026"],
]}, note="Confirm institute naming and certificate/signature details with the college before final submission.", sources=[]),
pg("CHAPTER 6 · INTERNSHIP", "Monthly Portfolio Graphs: Preparation Workflow", paragraphs=[
    "A monthly graph should answer one defined question and allow a reviewer to reproduce the number. Begin with an approved data extract, record its cut-off and version, reconcile totals to the source system, freeze definitions, and segment the portfolio consistently. Show current month, prior month, same month last year where relevant, plan/trigger only when authorised, and a rolling trend.",
    "Good graph labels include unit, numerator, denominator, period, population, product and source. Use stable scales, mark restatements, distinguish stock from flow, and avoid dual axes unless they are essential and clearly explained. A chart should not hide a denominator change, a reclassification, a change in account count or the impact of business exits.",
], bullets=["AUM/disbursement: stock and flow shown separately.", "Asset quality: GNPA/NNPA, Stage 2, roll rates and cure by vintage.", "Collections: due, collected, digital share, bounce and recovery.", "Operations: turnaround, exceptions, complaints, reconciliation and action ageing."], note="Appendix B (p.91) provides a monthly graph catalogue; actual data fields must follow company-approved definitions.", sources=["FY25 Annual Report, supplied PDF p.33; FY26 Annual Report, p.13."]),
pg("CHAPTER 6 · INTERNSHIP", "Early-Warning Graphs and the 'Ever Graphs' Term", paragraphs=[
    "The task list supplied by the student says 'Preparation of Graphs & ever Graphs on monthly basis'. In this report, 'ever graphs' is provisionally interpreted as EWS (Early Warning Signals) graphs because the risk context and FY25 annual report describe monthly portfolio reviews including EWS triggers. The exact internal label should be confirmed with the internship supervisor before the report is submitted.",
    "An EWS graph should present movement, threshold status, affected exposure, segment, ageing, root cause and action—not merely the number of alerts. Plot counts and exposure separately; distinguish new signals from persistent alerts; measure false positives, confirmed deterioration and cure; and ensure that the alert list is access-controlled. The threshold must come from approved policy or model governance.",
], table={"headers":["EWS view", "Example display"], "rows":[
    ["New / open / closed alerts", "Monthly count and exposure, by product/vintage"],
    ["Ageing", "Days since trigger; owner and overdue action"],
    ["Conversion", "Alert later entering arrears / remaining current"],
    ["Cure / false positive", "Validated outcome using an approved observation window"],
]}, note="Terminology clarification is pending. Replace 'EWS' if the team used another term.", sources=["FY25 Annual Report, supplied PDF p.33."]),
pg("CHAPTER 6 · INTERNSHIP", "Monthly Risk Paper: Suggested Structure", paragraphs=[
    "The monthly risk paper should be decision-oriented and short enough to review. Start with a one-page executive summary, then show portfolio trends, product/vintage quality, policy trigger status, collections/bounce, funding/ALM where in remit, operational incidents, customer outcomes and open actions. Each chart should carry a source and definition; each red/amber status should have an owner and due date.",
    "A strong narrative separates fact, interpretation and action. For example: state the movement and denominator; identify the segment driving it; compare with an approved limit; explain plausible causes; state what remains unverified; and ask for a specific decision. Do not state that a strategy caused a change unless the data and review support the link.",
], bullets=["1. Executive summary and key decisions.", "2. Portfolio, disbursement and vintage quality.", "3. EWS, bounce, cures, collections and write-offs.", "4. Funding, liquidity, capital and market-risk exceptions.", "5. Operational/cyber/compliance incidents and action tracker."], sources=["FY25 Annual Report, supplied PDF p.33; FY26 Annual Report, p.53."]),
pg("CHAPTER 6 · INTERNSHIP", "Quarterly RMC Pack: Preparation Checklist", paragraphs=[
    "RMC preparation converts ongoing monitoring into governance-level oversight. Before the meeting, reconcile monthly data to the approved source, compare the current quarter with prior periods, confirm definitions and policy versions, refresh the risk register, collect accountable-owner commentary, validate action closure and identify decisions requested. Disagreement or uncertainty should be visible rather than suppressed.",
    "The committee pack should cover the RMC's disclosed remit: risk policy and appetite, portfolio and delinquency, product-level NPA management, liquidity, operational and cyber risk, business continuity, material incidents and implementation of prior recommendations. Board-level material should be aggregated and anonymised; customer-level detail belongs only in authorised controlled annexures.",
], table={"headers":["Pack section", "Minimum evidence"], "rows":[
    ["Executive dashboard", "RAG status, movement, top decisions"],
    ["Credit / product", "AUM, vintage, delinquency, ECL, concentration"],
    ["Liquidity / market", "ALM gaps, stress, funding, rate/FX sensitivity"],
    ["Non-financial", "Fraud, cyber, BCP, compliance, conduct and complaints"],
    ["Actions", "Owner, due date, status, evidence and escalation"],
]}, sources=["FY26 Annual Report, supplied PDF p.53; FY25 Annual Report, p.33."]),
pg("CHAPTER 6 · INTERNSHIP", "Risk Policy Triggers Versus Actual Performance", paragraphs=[
    "A trigger-versus-actual report translates the approved appetite into an exception-control process. For each indicator, capture the exact policy clause, threshold and direction; actual value and population; measurement date; headroom; previous status; duration; business explanation; independent risk view; and corrective action. A breach should be recorded even if it is later cured, so recurring patterns remain visible.",
    "The annual reports disclose that the Company has risk appetite and portfolio-quality triggers, but the supplied material does not contain the internal numeric thresholds. This report therefore provides a blank register and does not infer limits from public outcomes such as GNPA, credit cost or CRAR. Those outcomes are not substitutes for a policy limit.",
], table={"headers":["Indicator", "Approved limit", "Actual", "Status / action"], "rows":[
    ["[Insert approved metric]", "[Policy value]", "[Month-end actual]", "[Within / near / breach; owner]"],
    ["[Insert approved metric]", "[Policy value]", "[Month-end actual]", "[Root cause and due date]"],
    ["[Insert approved metric]", "[Policy value]", "[Month-end actual]", "[Escalation / closure evidence]"],
]}, note="Populate only from authorised policy and MIS. No Fedfina internal threshold is included in this academic report.", sources=["FY25 Annual Report, supplied PDF p.33; FY26 Annual Report, pp.53, 116."]),
pg("CHAPTER 6 · INTERNSHIP", "Bounce Analysis: Interpretation and Controls", paragraphs=[
    "Bounce analysis starts with a controlled population of payment presentments and a consistent mapping of return reasons. Report both count and amount rates because a few high-value returns can move the amount measure while many small returns can move the count measure. Separate first presentation, retry and final status to avoid double-counting. Reconcile the source to mandate, payment and loan-servicing systems.",
    "Break the analysis by product, branch, channel, mandate type, due date, vintage and reason code. Track resolution in defined windows, subsequent DPD migration, repeat bounces, customer contact, complaints and costs. A technically failed debit should not be treated the same as insufficient funds; an automated or manual customer intervention must comply with approved contact and conduct controls.",
], bullets=["Confirm presentment denominator and retry rules.", "Classify technical, mandate, account and funds-related returns.", "Measure same-cycle cure and subsequent 1/30/60/90 DPD migration.", "Validate unusual spikes with operations before escalation."], note="No actual bounce counts or amounts are present in the supplied annual reports; Appendix G is a blank working template.", sources=[]),
pg("CHAPTER 6 · INTERNSHIP", "Monthly and Quarterly Work Cadence", paragraphs=[
    "A repeatable cadence reduces last-minute reporting error. During a month-end cycle, data should be frozen only after the source owner signs off; reconciliation and exceptions should be logged; the analyst should draft graphs and narrative; a reviewer should challenge definitions and anomalies; and the final pack should be version-controlled. Post-meeting actions should be carried forward until independently evidenced as complete.",
    "The internship dates span April to early July 2026. This report does not claim which particular live committee meetings or deliverables the intern attended because no activity log, meeting minutes or supervisor confirmation was supplied. The cadence below is a recommended description of the task workflow and should be aligned to the actual internship diary before submission.",
], table={"headers":["Cycle", "Analyst activity", "Control"], "rows":[
    ["Month-end", "Extract, reconcile, graph, explain exceptions", "Source-owner sign-off and version log"],
    ["Monthly review", "Risk paper, EWS, bounce and action updates", "Peer/manager review; definitions locked"],
    ["Quarterly RMC", "Synthesis, decision requests and prior actions", "Committee secretary / risk-owner validation"],
    ["Closeout", "Handover, learning reflection and records", "Remove confidential data from academic copy"],
]}, sources=[]),

# Chapter 7, pp.70–82
pg("CHAPTER 7 · FINDINGS", "Principal Findings", paragraphs=[
    "The disclosures show a lender scaling into a more secured portfolio while rebuilding selected underwriting and collection capabilities. FY26 AUM rose about 27.5% and PAT about 52.6%; secured AUM reached 98.9%, and the Company reported 0.8% credit cost. These are constructive headline signals, but quality is demonstrated only through consistent cohort performance, validated recoveries, capital and liquidity resilience, and sustainable customer outcomes.",
    "Three watch items are especially important: mortgage/ST LAP seasoning after the rebuild; collateral and operational control as Gold grows; and the balance-sheet interaction between longer-tenor assets, borrowings, interest sensitivity and liquidity. The slight NNPA increase and lower reported provision coverage should be read alongside GNPA improvement and not simplified into a single 'better' or 'worse' conclusion.",
], bullets=["Growth: strong and secured-mix led.", "Profitability: recovered; historical chart definitions need reconciliation.", "Asset quality: GNPA improved slightly; NNPA/PCR require follow-up.", "Execution: branch, ST LAP, sourcing and collections changes need cohort evidence.", "Funding: diversification and repricing improve resilience but require ALM stress."], sources=["FY26 Annual Report, supplied PDF pp.4, 13–15, 114–118."]),
pg("CHAPTER 7 · FINDINGS", "Qualitative Risk Register and Heat Map", paragraphs=[
    "The following prioritisation is the author's external analytical view based only on public disclosures. It is not Fedfina's internal risk rating, probability estimate, residual-risk score or approved appetite. The point is to make the evidence gaps visible and direct follow-up work toward topics where scale or change may increase exposure.",
    "Credit/vintage and collateral operations are rated as priority follow-ups because the Company highlights a ST LAP rebuild and rapid Gold growth. Funding/liquidity and technology also merit sustained monitoring given the reported maturity schedule, ECB/funding changes and system-led operating model. Any final RMC prioritisation belongs to authorised management and the Board committee.",
], chart="risk_heatmap", table={"headers":["Analyst watch area", "Public-evidence reason", "Priority"], "rows":[
    ["ST LAP vintage / collections", "Rebuild and Q4 disbursal recovery", "High follow-up"],
    ["Gold custody / collateral", "AUM +76%; custody +12%", "High follow-up"],
    ["ALM / funding", "Negative after-one-year net maturity bucket", "High follow-up"],
    ["Cyber / data / process", "Increasing system-led workflows", "Ongoing"],
]}, note="Qualitative prioritisation only; not a company risk score.", sources=["FY26 Annual Report, supplied PDF pp.13, 114–118."]),
pg("CHAPTER 7 · FINDINGS", "Recommendations: Credit Origination and Underwriting", paragraphs=[
    "Maintain a consistent origination control chain as the channel mix changes. The Business Rule Engine should apply version-controlled policy rules, retain reason codes and record authorised overrides. Independent sampling should test data capture, bureau results, repayment capacity, collateral, documentation and approval authority, with different check depth for new products, new branches and higher-risk cohorts.",
    "For rebuilt portfolios, use graduated limits and vintage gates. Review first-payment default, early-bucket delinquency, bounce, roll-rate and fraud alerts before increasing branch or channel exposure. Use independent model validation, exception analytics and feedback from collections to recalibrate underwriting only through approved governance. Scale should follow evidence of stable cohorts, not target achievement alone.",
], bullets=["Track approval rate and policy exception rate by product/channel/vintage.", "Separate manual overrides from automated pass/fail decisions.", "Use early-vintage gates and independent post-disbursement sampling.", "Feed verified collection/root-cause evidence back to product policy."], sources=["FY26 Annual Report, supplied PDF pp.13, 35; FY25 Annual Report, p.33."]),
pg("CHAPTER 7 · FINDINGS", "Recommendations: Gold Collateral and Custody", paragraphs=[
    "As Gold AUM expands, retain a control design that is independent of branch sales pressure. Standardise purity/weight testing, calibrated equipment, dual verification, photographic or system evidence where policy permits, sealed custody, access control, packet-to-ledger reconciliation, insurance and surprise physical verification. Exceptions should be resolved before disbursement or escalated to an authorised approver.",
    "Stress LTV and recovery under multiple gold-price paths, delayed customer payments and auction-cost assumptions. Monitor tail exposures near approved margin limits, not just portfolio average. Review customer notice, fair auction process, collateral release and complaint patterns. A gold price rising during FY26 does not demonstrate resilience to a sustained decline; the scenario should include a lower price and possible borrower non-cooperation.",
], bullets=["Reconcile physical gold to system balances and loan accounts.", "Monitor LTV distribution, revaluation age and policy exceptions.", "Separate value growth due to price from weight, disbursal and redemption.", "Independently test recovery and auction documentation."], sources=["FY26 Annual Report, supplied PDF pp.13, 116, 118."]),
pg("CHAPTER 7 · FINDINGS", "Recommendations: Mortgage Underwriting and Collateral", paragraphs=[
    "Strengthen the end-to-end property control trail: identity and ownership, legal title, encumbrance search, independent valuation, charge registration, end-use, insurance if required, and post-disbursement follow-up. Property valuation should be stress-haircut and aged; self-occupied status is useful context but does not replace legal or repayment checks.",
    "For ST and MT LAP, report separate cohorts by origination quarter, source channel, branch, ticket size, occupation, state and collateral type. Compare early delinquency, bounce, Stage migration, cure, write-off and recovery. Give additional independent attention to new policy versions and co-located branches until performance matures. Record restructuring, top-up and repeat borrowing distinctly.",
], table={"headers":["Control theme", "Suggested evidence"], "rows":[
    ["Cash-flow capacity", "Verified inflows/outflows, leverage and debt-service basis"],
    ["Property quality", "Title/search, valuation, charge and exceptions"],
    ["Vintage monitoring", "30/60/90 DPD, Stage 2, cure and loss by quarter"],
    ["Rebuild governance", "Policy version, override, branch and channel comparison"],
]}, sources=["FY26 Annual Report, supplied PDF p.13."]),
pg("CHAPTER 7 · FINDINGS", "Recommendations: Collections and Bounce Controls", paragraphs=[
    "Institutionalise a single bounce and collection taxonomy across payment systems and servicing platforms. Reconcile valid presentments and return codes; distinguish first attempt, retry, technical return and final resolution; and measure both count and amount rates. Pair the report with account-level DPD migration and recoveries in the authorised environment. Report trends early enough to adjust service and collection capacity.",
    "Collections effectiveness should be balanced with customer fairness. Define permitted contact channels and time windows, record promises-to-pay accurately, prohibit inappropriate pressure, monitor complaints and independently review third-party agencies. Measure sustainable cure rather than only same-day cash. The FY26-reported Stage 3 recovery increase is encouraging management evidence, but ongoing validation should include cost, repeat default and conduct outcomes.",
], bullets=["Create cause-coded return reporting and a stable denominator.", "Use segment-specific cure and roll-rate views.", "Reconcile agency and digital collections to bank/ledger receipts.", "Escalate repeat bounces and vulnerable-customer issues under approved rules."], sources=["FY26 Annual Report, supplied PDF p.13; FY25 Annual Report, p.33."]),
pg("CHAPTER 7 · FINDINGS", "Recommendations: Liquidity, ALM and Contingency Funding", paragraphs=[
    "Use a forward-looking ALM view that reconciles contractual and behavioural cash flows, maturity concentrations, asset prepayment, collection delays and off-balance-sheet commitments. Keep a daily/weekly operating view for cash and near-term maturities, a monthly structural gap review, and a quarterly stress narrative for RMC. Each limit needs a named owner, escalation point and contingency action.",
    "The FY26 maturity disclosure shows a positive within-one-year net but a negative beyond-one-year net. Management should assess the tenor and availability of funding against the longer asset profile, preserve unencumbered liquidity, test closure of wholesale channels and keep contingency funding options operationally ready. Do not treat total balance-sheet surplus as a substitute for a bucketed liquidity plan.",
], bullets=["Stress delayed collections and lower renewal/assignment capacity.", "Monitor top maturity buckets, committed lines and collateral encumbrance.", "Pre-agree escalation actions and communication responsibilities.", "Back-test behavioural assumptions and disclose model limitations."], sources=["FY26 Annual Report, supplied PDF pp.114–115, 118."]),
pg("CHAPTER 7 · FINDINGS", "Recommendations: Interest-Rate, FX and Funding Risk", paragraphs=[
    "ALCO reporting should combine repricing ladders, fixed/floating shares, basis risk, earnings-at-risk, fair-value sensitivity and customer repricing constraints. The disclosed FY26 sensitivity table shows distinct directions for loan and borrowing exposures. Management should reconcile these gross effects to the approved model and hedges, then test parallel, steepener/flattener and delayed-pass-through scenarios.",
    "For ECBs, report principal currency, hedge instrument, counterparties, maturity, collateral, rollover and hedge effectiveness. Diversification should be assessed by actual exposure shares and liquidity under stress, not the number of lenders alone. A change in fixed-rate funding can reduce exposure to immediate rate moves but may create future refinancing or pricing risk.",
], table={"headers":["Monthly / quarterly view", "Decision use"], "rows":[
    ["Repricing gap and EVE/EaR", "Identify timing and earnings sensitivity"],
    ["ECB and hedge dashboard", "Check currency cash flows and residual exposure"],
    ["Funding concentration / maturity", "Assess refinancing dependence and action window"],
    ["Cost-of-funds bridge", "Separate repricing, mix, fees and tenor effects"],
]}, sources=["FY26 Annual Report, supplied PDF pp.13, 15, 118."]),
pg("CHAPTER 7 · FINDINGS", "Recommendations: Branch, Fraud and Operational Controls", paragraphs=[
    "Rapid distribution expansion needs matching control capacity. A branch-opening dashboard should include staff training, system access, cash/collateral readiness, maker-checker coverage, audit plan, local complaint routes and first-month reconciliation. Track gross openings, closures, relocation and co-location separately so network growth reconciles to the year-end footprint.",
    "Fraud controls should span identity, application duplication, collateral substitution, employee access, disbursement account changes, suspicious repayment patterns and vendor activity. Maintain a single incident register that links event, loss, recovery, root cause, customer impact, regulatory reporting, control owner and closure evidence. Repeated near misses should be escalated even where no financial loss has yet crystallised.",
], bullets=["Apply role-based access and periodic recertification.", "Use independent surprise collateral/cash verification.", "Review repeat audit observations, not only new findings.", "Measure action closure quality and repeat-event rate."], sources=["FY25 Annual Report, supplied PDF p.33; FY26 Annual Report, pp.4, 13."]),
pg("CHAPTER 7 · FINDINGS", "Recommendations: Cyber, Data and Third Parties", paragraphs=[
    "Map critical services and data flows from customer acquisition to collections, including vendors and payment partners. Set recovery-time and recovery-point objectives through approved business-impact analysis; test failover and restore from backups; and track vulnerability remediation by severity and age. Third-party due diligence should cover access, subcontractors, incident notification, data use, resilience and exit arrangements.",
    "For management reporting, define data owners and lineage for every key risk indicator. Reconcile changes in logic, system migration, missing data and restatements. A zero-incident count is not proof of zero exposure if detection coverage or reporting is incomplete. The analyst should state coverage and known blind spots next to operational, cyber and customer metrics.",
], bullets=["Track critical-system availability and recovery exercises.", "Age open vulnerabilities and audit observations by severity.", "Maintain vendor inventory, materiality and exit plans.", "Reconcile key risk data to source systems with change logs."], sources=["FY25 Annual Report, supplied PDF p.33; FY26 Annual Report, pp.13, 32."]),
pg("CHAPTER 7 · FINDINGS", "Recommendations: Conduct, Complaints and Responsible Lending", paragraphs=[
    "The Company's disclosed customer-centric indicators should be supplemented by outcome measures: time to resolve complaints, repeat complaint rate, fee/charge disputes, collection-conduct allegations, mandate consent and collateral-release turnaround. Use a common case taxonomy and root-cause ownership across branches, call centres, digital and external agencies. Report both average and aged tail cases.",
    "Responsible lending requires suitable terms, clear communication, privacy, consent and affordable repayment. Growth targets should be balanced with quality and customer outcomes. Where a borrower is under stress, collections and restructuring actions must follow current law and policy. A public report cannot validate case-level conduct; independent sample review is therefore important.",
], table={"headers":["Outcome indicator", "Why it belongs in risk reporting"], "rows":[
    ["Complaint ageing / repeat rate", "Detect unresolved process or product harm"],
    ["Collection conduct cases", "Control legal, conduct and reputation exposure"],
    ["Collateral release timing", "Protect customer property and trust"],
    ["Turnaround-time misses", "Identify servicing bottlenecks and missed payments"],
]}, sources=["FY26 Annual Report, supplied PDF pp.4, 21; FY25 Annual Report, p.33."]),
pg("CHAPTER 7 · FINDINGS", "Recommendations: Limits, EWS and Stress Governance", paragraphs=[
    "Every risk limit should have an owner, rationale, calibration method, data source, breach workflow and periodic review. EWS should be tested for timeliness, predictive value, false positives, segment stability and outcome. A policy trigger can be appropriate even if no breach occurred; an EWS can be useful without being a hard limit. Keep the two concepts distinct in reporting.",
    "Quarterly stress testing should include gold-price, delinquency, recovery-time, funding-cost, refinancing, branch productivity and technology disruption scenarios. Combine risks where plausible, identify management actions and quantify implementation lags. RMC should receive a clear statement of what changed since the previous cycle, the uncertainty range and the decisions requested.",
], bullets=["Validate triggers and models through independent challenge.", "Record limit overrides, near-breaches and recurring exceptions.", "Link stress outcomes to liquidity, capital, pricing and recovery plans.", "Reassess assumptions after portfolio or policy changes."], sources=["FY26 Annual Report, supplied PDF p.53; FY25 Annual Report, p.33."]),
pg("CHAPTER 7 · FINDINGS", "Implementation Roadmap and Ownership", paragraphs=[
    "The roadmap below is a recommended control-improvement sequence, not a statement of Fedfina's approved plan. Start with definitions and source reconciliation, because dashboards built on inconsistent populations create false confidence. Then strengthen product/vintage monitoring and connect exceptions to accountable actions. Governance should review the design after the first complete reporting cycle.",
    "The Risk function can coordinate measurement and challenge; business owners remain responsible for source controls and remediation; Finance/ALCO own relevant capital and liquidity inputs; Compliance, Operations, Technology and Internal Audit provide specialist oversight. Each recommendation needs a sponsor, due date, deliverable, success measure and evidence of independent validation.",
], table={"headers":["Horizon", "Priority output", "Illustrative success evidence"], "rows":[
    ["0–30 days", "Lock KPI definitions, source lineage and policy versions", "Signed data dictionary and reconciliation log"],
    ["31–60 days", "Pilot product/vintage, bounce and action dashboards", "Reviewed sample; exceptions assigned and tracked"],
    ["61–90 days", "Integrate monthly risk paper and RMC action tracker", "Stable pack, decisions and independently evidenced closure"],
    ["Ongoing", "Back-test EWS, stress and controls", "Periodic validation and documented changes"],
]}, note="This roadmap is a student recommendation; approval and ownership belong to Fedfina.", sources=[]),

# Chapter 8, pp.83–87
pg("CHAPTER 8 · CONCLUSION", "Answers to the Research Questions", paragraphs=[
    "RQ1: Yes, reported AUM and PAT increased over FY22–FY26, with a FY25 PAT dip and a strong FY26 recovery. The latest chart shows improving FY26 ROA/ROE. These movements demonstrate reported growth and profitability, not a proven causal relationship between scale and sustainable earnings.",
    "RQ2: Secured AUM rose from 85.0% in FY24 to 98.9% in FY26 in company disclosures, while FY26 GNPA improved slightly. This supports the view that the mix became more collateral-backed, but the NNPA increase, lower provision coverage and absence of monthly cohorts require caution. RQ3: CRAR was 22.4% in the latest chart; capacity still depends on risk-weighted growth and capital planning. RQ4/RQ5: ALM, funding, new-book credit, collateral execution and unavailable internal data are key follow-ups.",
], note="Answers reflect public annual-report evidence and the stated study limitations.", sources=["FY24 Annual Report, supplied PDF p.31; FY25 Annual Report, p.33; FY26 Annual Report, pp.4, 14–15, 114–118."]),
pg("CHAPTER 8 · CONCLUSION", "Conclusion", paragraphs=[
    "Fedbank Financial Services Limited's FY2025–26 disclosures present a business that has grown in scale, returned to higher reported profitability and moved materially toward secured lending. The management narrative also describes investment in underwriting systems, in-house collections and funding diversification. These are important risk-management developments for a retail NBFC serving households and small businesses.",
    "The principal conclusion is conditional: the quality of growth matters more than growth alone. Sustained outcomes will depend on ST LAP cohort performance, Gold collateral and custody controls, mortgage recoveries, stable funding, liquidity planning, capital use, technology resilience, fair collections and robust governance. Monthly EWS, risk papers, trigger comparisons, bounce analysis and quarterly RMC reporting are useful only when definitions and source data are controlled.",
], note="The report concludes on the evidence available; it does not provide an investment opinion or assurance over internal controls.", sources=[]),
pg("CHAPTER 8 · CONCLUSION", "Limitations and Further Study", paragraphs=[
    "The project relies on annual-report PDFs and student-supplied internship particulars. It has no access to monthly MIS, borrower-level data, internal risk policy thresholds, RMC decks/minutes, branch visit notes, management interviews, model validation reports or confidential audit findings. Annual aggregates cannot establish causality, cohort performance or the accuracy of management action attribution.",
    "Further research could analyse anonymised month-on-month product/vintage data, measure bounce-to-DPD migration, back-test EWS performance, compare approved trigger status with actual outcomes, assess gold-price and property recovery stress, and review funding maturity under behavioural scenarios. Any such work requires company authorisation, data minimisation, confidentiality controls and supervisor approval.",
], bullets=["No internal numeric trigger or bounce KPI is claimed.", "Some FY25 historic yield/funding values differ between annual reports.", "Operational disclosure is not an independent audit opinion.", "Future study should use defined, authorised and anonymised data."], sources=[]),
pg("CHAPTER 8 · CONCLUSION", "Internship Learning Reflection", paragraphs=[
    "The risk-analyst role connects classroom finance with operational decision-making. I learned that the same movement can have different meanings depending on whether it is a stock or flow, gross or net, a company average or a cohort, a public disclosure or an internal limit. A credible analyst documents the source and denominator before presenting the chart.",
    "The stated workstreams—monthly graphs/EWS, monthly risk paper, quarterly RMC preparation, policy-trigger-versus-actual review and bounce analysis—require accuracy, judgement and clear writing. The most valuable output is not a colourful dashboard but a verified exception, a plausible root cause, a proportionate action and evidence that the issue was resolved without compromising customer fairness or confidentiality.",
], bullets=["Technical learning: trend, ratio, credit, liquidity and sensitivity analysis.", "Process learning: data validation, versioning, review and action tracking.", "Professional learning: escalation, confidentiality and balanced interpretation."], sources=[]),
pg("CHAPTER 8 · CONCLUSION", "Final Risk Dashboard and Submission View", paragraphs=[
    "A concise senior-management view should lead with risk appetite and material exceptions, then show portfolio quality, funding/liquidity, capital, operations, customer outcomes and remediation. Each status should be tied to an approved definition and owner. A dashboard should not bury an unresolved high-severity event among routine metrics or imply that a green annual ratio removes a localised risk.",
    "For academic submission, verify name, roll number, programme, institution, guide and dates; replace any provisional terminology; attach only authentic employer documents; and update internal values only from authorised records. The appendices provide blank analytical templates; no confidential company data is included.",
], table={"headers":["Final check", "Status"], "rows":[
    ["Student and internship details", "Provided; verify exact programme/institution style"],
    ["Annual-report data and page citations", "Included; latest-series conflicts disclosed"],
    ["Internal bounce / policy / RMC evidence", "Not supplied; templates left blank"],
    ["Employer certificate and signatures", "Not fabricated; attach originals if required"],
]}, sources=[]),

# References pp.88–89
pg("REFERENCES", "Bibliography: Annual Reports", paragraphs=[
    "The following three company annual reports were supplied with the project and are the primary sources for company-specific information. PDF page numbers are used in in-text source notes because the supplied files contain cover letters, spreads and two-page layouts; printed report page numbers may appear in the footer and are noted where useful.",
], table={"headers":["Reference", "Use in this study"], "rows":[
    ["Fedbank Financial Services Limited, Annual Report 2023–24, supplied PDF (FY24).", "Historical financial trends; 85% secured AUM; risk framework and controls. Key PDF pp.13–14, 24, 31."],
    ["Fedbank Financial Services Limited, Annual Report 2024–25, supplied PDF (FY25).", "Transition-year trend; risk framework, monthly EWS and quarterly RMC reporting; 89.5% secured AUM. Key PDF pp.12–13, 33."],
    ["Fedbank Financial Services Limited, Annual Report 2025–26, supplied PDF (FY26), filed 4 September 2026.", "Primary FY26 snapshot, five-year chart series, strategy, RMC terms, maturity and sensitivity notes. Key PDF pp.1, 4, 7–15, 53, 114–118."],
]}, note="The annual reports are public company disclosures. Historical ratios may be restated or presented on different bases.", sources=[]),
pg("REFERENCES", "Source Reconciliation and Calculation Notes", paragraphs=[
    "Selected yield, cost-of-borrowings and spread values differ across report editions. FY24's report gives 16.2%, 8.8% and 7.4%, respectively; FY25's report repeats those FY24 values and reports FY25 at 17.4%, 9.2% and 8.1%. The FY26 five-year charts instead show FY24 at 16.7%, 8.6% and 8.1%, and FY25 at 17.1%, 9.0% and 8.2%. No full reconciliation of these historical differences is provided in the supplied reports.",
    "This report uses the latest FY26 series consistently for trend charts and separately discloses earlier as-reported values; it does not silently blend them. Other calculations: FY26 AUM growth = (201,530 ÷ 158,115) − 1 ≈ 27.5%; FY22–FY26 AUM CAGR = (201,530 ÷ 61,872)^(1/4) − 1 ≈ 34.3%; PAT growth = (3,436 ÷ 2,252) − 1 ≈ 52.6%. ₹ million is converted to ₹ crore by dividing by 10; ₹ lakh by dividing by 100.",
], table={"headers":["Metric", "FY24 report: FY24", "FY26 chart: FY24", "FY25 report: FY25", "FY26 chart: FY25"], "rows":[
    ["Yield", "16.2%", "16.7%", "17.4%", "17.1%"],
    ["Cost of borrowings", "8.8%", "8.6%", "9.2%", "9.0%"],
    ["Spread", "7.4%", "8.1%", "8.1%", "8.2%"],
    ["AUM / PAT", "Consistent across reports", "Same chart series", "Consistent across reports", "Same chart series"],
]}, note="Differences may reflect definition, methodology or reclassification; the supplied reports do not fully reconcile them.", sources=["FY24 Annual Report, supplied PDF p.13; FY25 Annual Report, supplied PDF p.12; FY26 Annual Report, supplied PDF pp.14–15."]),

# Appendices 90–100
pg("APPENDIX A", "Data Dictionary for Monthly Risk Reporting", paragraphs=[
    "Use one approved definition for each field and record the source system, owner, population, frequency, cut-off, unit and validation. The names below are a generic template, not Fedfina field names. Company MIS and the current policy take precedence.",
], table={"headers":["Field", "Definition to confirm", "Control"], "rows":[
    ["AUM", "On-/off-book scope; reporting date; product mapping", "Reconcile to source and disclose basis"],
    ["Presentment", "Valid first/retry debit population", "Unique instalment / attempt key"],
    ["Bounce", "Return event and reason-code mapping", "Separate technical and customer causes"],
    ["DPD", "Days past due at an approved cut-off", "Reconcile to loan-servicing system"],
    ["Cure", "Account returning to defined current state", "Specify observation window"],
    ["EWS alert", "Approved signal, rule version and population", "Retain version and validation outcome"],
    ["Policy trigger", "Approved floor/ceiling and direction", "Policy clause, version and effective date"],
]}, note="Never compare two metrics until their definitions and populations match.", sources=[]),
pg("APPENDIX B", "Monthly Graph Catalogue", paragraphs=[
    "The monthly graph pack should be small enough to review and broad enough to reveal risk migration. A graph is complete only when its period, unit, numerator/denominator, population, source, owner and any restatement are visible. Use stable scales; annotate policy changes and portfolio exits.",
], table={"headers":["Graph", "Recommended cut", "Companion metric"], "rows":[
    ["AUM and disbursals", "Product, vintage, geography, channel", "Delinquency and capital use"],
    ["DPD / Stage migration", "Product, vintage, branch", "Cure, write-off and ECL"],
    ["Bounce", "Cause, mandate, product, due cycle", "Subsequent DPD and cure"],
    ["Collections", "Due vs received, channel, agency", "Cost-to-collect and complaints"],
    ["Funding / ALM", "Maturity, lender, currency, reset", "Liquidity buffer and EaR"],
    ["Operations / conduct", "Incident, complaint, branch, ageing", "Loss, repeat issue and closure"],
]}, sources=[]),
pg("APPENDIX C", "EWS Register and Validation Template", paragraphs=[
    "This blank template supports signal governance. A signal should be tested before it is treated as an effective early-warning rule. Review both the accounts that triggered and the accounts that did not, use an approved observation window, and record changes to definitions or cut-offs.",
], table={"headers":["EWS field", "Entry"], "rows":[
    ["Signal name / rule version", "[Insert approved label and version]"],
    ["Population / source / frequency", "[Define eligible accounts and system]"],
    ["Threshold / direction / effective date", "[Insert only from approved policy]"],
    ["Alerts / exposure / age", "[Month-end count and amount]"],
    ["Confirmed deterioration / cure", "[Outcome window and definition]"],
    ["False positives / missed events", "[Validation sample and result]"],
    ["Owner / action / due date", "[Named accountable owner and evidence]"],
]}, note="Do not paste customer identifiers into an academic report or an unsecured personal file.", sources=[]),
pg("APPENDIX D", "Monthly Risk-Paper Template", paragraphs=[
    "A risk paper should separate the executive conclusion from detailed backup. The summary should make the quarter/month movement, material exceptions, customer impact and decision request clear without requiring the reader to reconstruct every chart. Use an appendix for definitions and large data tables.",
], table={"headers":["Page / section", "Content prompt"], "rows":[
    ["1. Executive summary", "Three material movements; decisions required; red/amber items"],
    ["2. Portfolio", "AUM/disbursal, product/vintage quality, concentration"],
    ["3. Credit / collections", "DPD, EWS, bounce, cure, recovery, ECL"],
    ["4. ALM / capital / market", "Maturity, liquidity, repricing, sensitivity, capital"],
    ["5. Non-financial risk", "Fraud, cyber, operational, compliance, conduct"],
    ["6. Actions", "Owner, due date, status, evidence, escalation"],
]}, note="Attach source and metric definitions to every chart.", sources=[]),
pg("APPENDIX E", "Quarterly RMC Pack Agenda", paragraphs=[
    "The agenda below maps the disclosed FY26 RMC terms of reference to a practical quarterly sequence. The committee secretary and authorised risk owner should confirm the current terms, materiality and required papers. The annual report's public terms do not replace the internal agenda or policy.",
], table={"headers":["Agenda item", "Review question", "Evidence / decision"], "rows":[
    ["Risk appetite / policy", "Any breach, near miss or policy change?", "Limit register; approval / escalation"],
    ["Portfolio / NPA", "Which product, vintage or region changed?", "AUM, DPD, ECL, cure and actions"],
    ["Liquidity / ALM", "Any gap, funding or stress concern?", "Bucket report, stress and contingency"],
    ["Operational / cyber / BCP", "Any material incident or resilience weakness?", "Loss log, test result, remediation"],
    ["Customer / compliance", "Any conduct, grievance or regulatory issue?", "Impact, ageing and corrective action"],
    ["Prior actions", "What is overdue or repeatedly reopened?", "Owner, evidence and closure decision"],
]}, sources=["FY26 Annual Report, supplied PDF p.53."]),
pg("APPENDIX F", "Policy Trigger-versus-Actual Register", paragraphs=[
    "Populate this register from the current approved risk policy and authorised month-end data only. Select direction carefully: for a maximum limit, actual above the threshold may be a breach; for a minimum floor, actual below the threshold may be a breach. Tolerance, duration and escalation must follow the approved policy.",
], table={"headers":["Metric / policy clause", "Limit / direction", "Actual / date", "Status / headroom", "Owner / action"], "rows":[
    ["[Metric 1]", "[Approved value; MAX/MIN]", "[Value; date]", "[Within / near / breach]", "[Owner; due date]"],
    ["[Metric 2]", "[Approved value; MAX/MIN]", "[Value; date]", "[Within / near / breach]", "[Owner; due date]"],
    ["[Metric 3]", "[Approved value; MAX/MIN]", "[Value; date]", "[Within / near / breach]", "[Owner; due date]"],
]}, note="No actual internal limit is provided in this report. Leave blank until authorised source data is available.", sources=[]),
pg("APPENDIX G", "Bounce-Analysis Data Template and Formulas", paragraphs=[
    "Use one row per reporting month and product/segment. If this template is populated with authorised data, validate the formulas, ensure that retry attempts are counted consistently, and use a unique instalment key to prevent duplication. Rates below are undefined where the denominator is zero; blank input must not be interpreted as zero performance.",
], table={"headers":["Month / segment", "Valid presentments", "Bounced", "Presented ₹", "Returned ₹", "Count rate", "Amount rate"], "rows":[
    ["[Month / product]", "[n]", "[n]", "[₹]", "[₹]", "Bounced ÷ valid", "Returned ÷ presented"],
    ["[Month / product]", "[n]", "[n]", "[₹]", "[₹]", "[Formula]", "[Formula]"],
    ["[Month / product]", "[n]", "[n]", "[₹]", "[₹]", "[Formula]", "[Formula]"],
]}, bullets=["Add return code, first/retry flag, cure window, next DPD and complaint flag.", "Reconcile totals to bank/mandate and servicing-system control reports.", "No actual Fedfina bounce rate is reported in this report."], sources=[]),
pg("APPENDIX H", "Five-Year Company-Reported Trend Series", paragraphs=[
    "The series below reproduces the FY26 annual-report five-year charts. Monetary values originally labelled ₹ million are converted to ₹ crore. The latest FY26 series is preferred for chart consistency; where the FY25 report's historical yield, spread or borrowing-cost values differ, the report does not silently splice them. Ratios are as reported, not recalculated from financial statements.",
], table={"headers":["Metric", "FY22", "FY23", "FY24", "FY25", "FY26"], "rows":[
    ["AUM (₹ Cr)", "6,187.2", "9,069.6", "12,191.9", "15,811.5", "20,153.0"],
    ["PAT (₹ Cr)", "103.5", "180.1", "244.7", "225.2", "343.6"],
    ["Yield (%)", "16.0", "16.1", "16.7", "17.1", "16.7"],
    ["Spread (%)", "8.2", "8.3", "8.1", "8.2", "8.6"],
    ["Cost of borrowings (%)", "7.8", "7.8", "8.6", "9.0", "8.1"],
    ["ROA (%)", "1.7", "2.3", "2.4", "1.8", "2.4"],
    ["ROE (%)", "10.4", "14.4", "13.5", "9.4", "12.6"],
    ["GNPA / NNPA (%)", "2.2 / 1.8", "2.0 / 1.6", "1.7 / 1.3", "2.0 / 1.2", "1.9 / 1.3"],
    ["CRAR (%)", "23.0", "17.9", "23.5", "21.9", "22.4"],
]}, sources=["FY26 Annual Report, supplied PDF pp.14–15."]),
pg("APPENDIX I", "FY26 Risk-Disclosure Reference Log", paragraphs=[
    "This log connects public disclosures to the analytical themes in the report. It is not a completeness opinion: the annual report contains additional notes, definitions, audit material and statutory disclosures. Consult the original PDF before citing a specific number or making a policy decision.",
], table={"headers":["Topic", "Disclosed fact used", "Source PDF page"], "rows":[
    ["FY26 snapshot", "AUM, secured AUM, NPA, credit cost, PAT, return", "p.4"],
    ["Trend series", "AUM, PAT, pricing, quality, CRAR, returns", "pp.14–15"],
    ["Strategy / collections", "Gold, ST/MT LAP, sourcing, cure and funding", "p.13"],
    ["RMC", "Terms of reference and meeting record", "p.53"],
    ["Maturity analysis", "Assets/liabilities by within/after-one-year bucket", "pp.114–115"],
    ["Credit / ECL", "EAD, PD, LGD, stages and SICR", "p.116"],
    ["Rate / FX / gold", "Gold stress, rate sensitivity and hedge narrative", "p.118"],
]}, note="Earlier-report source map: FY24 pp.13–14, 24, 31; FY25 pp.12–13, 33.", sources=[]),
pg("APPENDIX J", "Stress-Test Design Sheet", paragraphs=[
    "The following scenario matrix is intentionally unpopulated. Risk, Finance and business owners should approve shock sizes, horizons, correlations and management actions before calculations. Report ranges and sensitivities where precision is limited; do not label a deterministic scenario as a probability forecast.",
], table={"headers":["Risk factor", "Base assumption", "Adverse shock", "Severe shock", "Output"], "rows":[
    ["Gold price / LTV", "[Approved]", "[Approved]", "[Approved]", "Margin, loss, cure"],
    ["Mortgage recovery", "[Approved]", "[Haircut / time]", "[Haircut / time]", "LGD / ECL"],
    ["Bounce / delinquency", "[Approved]", "[Rate / roll]", "[Rate / roll]", "Collections / Stage / PAT"],
    ["Funding cost / maturity", "[Approved]", "[bp / closure]", "[bp / closure]", "NII / liquidity / CRAR"],
    ["Branch / system disruption", "[Approved]", "[Duration]", "[Duration]", "Service / cash / loss"],
]}, note="All scenario cells are placeholders; this appendix contains no Fedfina forecast.", sources=[]),
pg("APPENDIX K", "Submission Checklist and Viva Questions", paragraphs=[
    "Before printing or uploading, refresh the table of contents if pages change, check that the PDF opens and all 100 pages render, verify the roll number and internship dates, and obtain the institution's required signatures. Replace provisional wording only after supervisor confirmation. Attach a genuine employer certificate if the college requires one; do not use this student-prepared particulars page as employer certification.",
], bullets=["Why does secured AUM not eliminate credit and operational risk?", "How are GNPA, NNPA, credit cost and ECL different?", "Why is a bounce not automatically an NPA?", "What does the FY26 maturity table's negative longer-tenor net imply—and not imply?", "Why do the FY25 and FY26 annual reports show different historic yield/cost figures?", "How would you prove a policy trigger breach and its closure?", "What controls make a quarterly RMC pack decision-useful?"], note="Report prepared 4 October 2026 from files supplied in the repository; company figures are FY2025–26 unless explicitly identified otherwise.", sources=[]),
]
