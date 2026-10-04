from report_builder import Page
from report_data import *

AR26 = "Fedfina Annual Report 2025-26"
AR25 = "Fedfina Annual Report 2024-25"
AR24 = "Fedfina Annual Report 2023-24"
L2C = lambda x: x / 100.0  # lakh → crore


def cr(x, d=1):
    return f"{x/100:,.{d}f}"


def pct(a, b, d=1):
    return f"{(a/b-1)*100:+.{d}f}%"


def cagr(a, b, years):
    return ((b / a) ** (1 / years) - 1) * 100


def pages(C):
    P = []
    F26, F25, F24, F23 = FIN["FY26"], FIN["FY25"], FIN["FY24"], FIN["FY23"]
    P26, P25 = PL["FY26"], PL["FY25"]
    B26, B25 = BS["FY26"], BS["FY25"]
    L26, L25 = LOANS["FY26"], LOANS["FY25"]

    # ================================================================== CHAPTER 3 COMPANY
    pg = Page("Chapter 3 — Company Background and Corporate Journey")
    pg.p("Fedbank Financial Services Limited was incorporated in 1995 in Kochi, Kerala, as a subsidiary of The Federal Bank Limited. For its first decade it was a captive distribution arm; in 2007 it began distributing housing loans, home-equity mortgages, personal loans and car loans for the bank, and in 2010 it obtained its RBI licence to operate as a non-deposit-taking NBFC (Certificate of Registration N-16.00187, August 2010). Gold-loan distribution began in 2011 and medium-ticket LAP in 2012. The modern company took shape from 2015, when it crossed 100 branches and a ₹500 crore loan book, and from 2018, when it launched small-ticket LAP and business loans and received a ₹168.6 crore investment from private-equity investor True North. The registered office moved to Mumbai in 2021, the year the network crossed 500 branches and AUM crossed ₹5,000 crore. The company listed on NSE and BSE in November 2023 through a ₹1,092 crore IPO.")
    pg.table(["Year", "Milestone (as disclosed by the company)"],
             [["1995", "Incorporated in Kochi, Kerala; certificates of incorporation and commencement of business"],
              ["2007", "Began distributing housing loans, home-equity mortgage loans, personal and car loans for Federal Bank"],
              ["2010", "RBI licence to operate as an NBFC"],
              ["2011 / 2012", "Commenced gold-loan distribution (2011) and medium-ticket LAP (2012)"],
              ["2015", "Crossed 100 branches; loan book crossed ₹500 crore"],
              ["2018", "Launched small-ticket LAP and business loans; loan book crossed ₹1,000 crore; True North invested ₹168.6 crore"],
              ["2020", "Digital transformation initiated; 303 branches; loan book ₹3,838 crore; net worth ₹691 crore"],
              ["2021", "Registered office shifted to Mumbai; 500+ branches; net worth > ₹1,000 crore; doorstep gold loans launched; AUM > ₹5,000 crore"],
              ["2023", "Net worth > ₹1,350 crore; loan book > ₹8,000 crore; IPO and listing on NSE/BSE (₹1,092 crore)"],
              ["2024", "621 branches; AUM ₹12,192 crore; ratings upgraded – CARE AA+/Stable, India Ratings AA+/Stable, CRISIL AA/Positive"],
              ["2025", "Fedfina 2.0 launched under new MD&CEO Parvez Mulla; ST LAP reset; exit from unsecured lending begun; 694 branches; AUM ₹15,800 crore"],
              ["2026", "AUM ₹20,153 crore; gold AUM > ₹10,000 crore; 757 branches; 98.9% secured; AA+/Stable from four agencies; True North exits; USD 250 mn ECB programme"]],
             widths=[0.9, 6.15], source=f"{AR24} ‘Reflecting on our journey’ p.8–9; {AR25}; {AR26} Key Highlights and Directors’ Report.")
    pg.p(f"Scale today. Over the eight years FY19–FY26, AUM grew ten-fold from ₹{AUM_MN['FY19']/10:,.0f} crore to ₹{AUM_MN['FY26']/10:,.0f} crore ({cagr(AUM_MN['FY19'], AUM_MN['FY26'], 7):.1f}% CAGR, derived), branches from {BRANCHES['FY19']} to {BRANCHES['FY26']}, and PAT from ₹{PAT_MN['FY19']/10:,.0f} crore to ₹{PAT_MN['FY26']/10:,.1f} crore. Net worth rose from ₹1,356 crore (FY23) to ₹2,926 crore (FY26), helped by the ₹600 crore fresh issue in the IPO and retained earnings; no dividend has been paid, with profits ploughed back to support growth (Directors’ Report FY26 recommends no dividend and transfers ₹68.7 crore to the statutory reserve under Section 45-IC of the RBI Act).")
    P.append(pg)

    # ------------------------------------------------------------------ 29 Parentage & shareholding
    pg = Page("Federal Bank Parentage and Shareholding Structure")
    pg.p("Fedfina is a subsidiary of The Federal Bank Limited, a Kerala-headquartered private-sector scheduled commercial bank. Federal Bank held 60.79% of the equity at 31 March 2026 (61.03% a year earlier; the small dilution reflects ESOP allotments). The relationship provides what the company calls “institutional credibility, governance standards and operational alignment”: two of the bank’s senior executives (Mr. K.V.S. Manian and Mr. Harsh Dugar) sit on the Board as nominee directors; the bank’s former MD&CEO Mr. Shyam Srinivasan is Fedfina’s non-executive Chairman; the bank is a lender (term loan ₹1,064 crore, demand loan ₹60 crore and subordinated NCDs ₹246 crore at 31 March 2026 – about 10% of borrowings); and Fedfina distributes bank products, earning ₹33.1 crore of distribution income in FY26.")
    pg.fig(f"{C}/shareholding.png", "Figure 12 – Shareholding pattern at 31 March 2026. Source: " + AR26 + ", Report on Corporate Governance (distribution of shareholding).", 2.5, width=5.0)
    pg.table(["Category of shareholder", "31 Mar 2026 (%)", "31 Mar 2025 (%)", "Change (pp)"],
             [[s[0], f"{s[1]:.2f}", f"{s[2]:.2f}", f"{s[1]-s[2]:+.2f}"] for s in SHAREHOLDING] +
             [["Total", "100.00", "100.00", ""]],
             widths=[3.4, 1.2, 1.2, 1.0], font=8, source=f"{AR26}, Report on Corporate Governance – categories of shareholders. Shares outstanding {SHARES_OUT:,} (FY25: {SHARES_OUT_PY:,}).")
    pg.p("Two changes in the year matter for governance. First, private-equity investor True North, a shareholder since 2018, exited the company: its nominee director Mr. Maninder Singh Juneja resigned with effect from 14 May 2026, and the holding of Alternate Investment Funds fell from 14.38% to 13.01% with the balance absorbed by public individuals (up to 15.94%), mutual funds (2.71%) and others. Second, the free float broadened – NRIs, HUFs and KMP holdings all increased – and the market capitalisation stood at ₹4,642 crore on 31 March 2026, implying a share price of about ₹124 against a book value of ₹78.19 (price-to-book ≈ 1.59x, derived).")
    P.append(pg)

    # ------------------------------------------------------------------ 30 Vision, values
    pg = Page("Vision, Values and Strategic Intent")
    pg.p("Vision. The company’s stated vision is “Empowering Emerging India with Easy Access to Loans”. Its customers are described as self-employed households, small business owners and MSME borrowers across Tier 2, 3 and 4 markets who need reliable access to organised credit – people for whom Fedfina is “often the first point of access to formal finance”.")
    pg.p("Values. The culture is codified as E.P.I.C. – Execution Excellence, People Focus, Integrity and Customer-Centricity – each with four stated behaviours, reproduced below from the FY26 report.")
    pg.table(["Execution Excellence", "People Focus", "Integrity", "Customer-Centric"],
             [["Clear objectives", "Empowerment", "Transparency", "Customer goals"],
              ["Resource optimisation", "Development opportunities", "Accountability", "Clear communication"],
              ["Adaptability", "Recognition and rewards", "Building trust", "Customer support"],
              ["Continuous improvement", "Work-life integration", "Ethical decisioning", "Seamless experience"]],
             widths=[1.76, 1.76, 1.76, 1.77], source=f"{AR26}, ‘Our Vision / Our Values’ (Corporate Overview).")
    pg.h2("Strategic priorities under Fedfina 2.0")
    pg.p("The FY25 annual report set out three priorities under the “Fedfina 2.0: Sharper, Stronger, More Focussed” programme launched by the new MD&CEO, Mr. Parvez Mulla: (1) scale gold loans through disciplined branch-led expansion, productivity uplift and tight risk management; (2) rebuild mortgage loans with sharper underwriting, strengthened collections and a renewed focus on small-ticket LAP while scaling mid-ticket LAP in a capital-efficient manner; and (3) embed technology and data in decisioning to simplify customer experience, speed up turnaround and improve operating efficiency. The stated aim was to align the portfolio “to higher RoA/RoE segments, secured exposures and predictable outcomes”.")
    pg.p("The FY26 report confirms the direction and adds the Board’s medium-term ambition: growth “targeted at 20 to 25% on a sustainable basis” (Chairman), a sub-1% credit-cost commitment, a long-term gold tonnage CAGR of 10–12% “rather than relying solely on gold price movements” (MD&CEO), and a “fully secured construct” achieved by assigning the ₹886 crore unsecured business-loan portfolio in H1 FY26.")
    pg.h2("Investment proposition as articulated by the company")
    pg.bullets([
        "Twin-engine growth strategy:: short-tenor, high-velocity gold loans paired with stable, long-tenor mortgage yields – liquidity products complemented by duration assets.",
        "Rapid and scalable ‘phygital’ distribution:: hub-and-spoke branch model (757 branches) supported by digital origination, servicing and collections.",
        "Technology-enabled underwriting:: automated underwriting and workflow tools within a collateral-based framework; 10-day approval and 15-day disbursement TAT for mortgages.",
        "Efficient funding structure:: AA+/Stable ratings from CARE, CRISIL, ICRA and India Ratings; borrowing mix of 50% term loans, 17% ECB, 13% NCDs/CPs and 14% direct assignments; USD 250 million ECB programme.",
        "Experienced leadership and risk discipline:: seasoned banking leadership; collection efficiency 99.7%; NIM 8.8%; debt-equity 4.6x.",
        "Strong institutional backing:: 60.8% Federal Bank ownership, “advantages that many standalone NBFCs lack”.",
    ])
    pg.p("Assessment. The vision and priorities are specific enough to be tested against outcomes, which this report does on the next pages (Fedfina 2.0 commitments versus delivery) and in Chapter 5.")
    P.append(pg)

    # ------------------------------------------------------------------ 31 Business model
    pg = Page("Business Model: The Twin-Engine Secured Lender")
    pg.p("Fedfina’s business model rests on two secured products that behave very differently and therefore diversify each other. Gold loans are short-tenor (typically up to 12 months), small-ticket (₹2.7 lakh average), high-yield and highly liquid: the collateral is standardised, valued daily and auctionable. Mortgage loans (LAP and housing loans) are long-tenor, larger-ticket (₹16.1 lakh to ₹72.4 lakh), lower-yield and illiquid, but they provide duration, stable interest income and a customer relationship that lasts years. The company describes the combination as “liquidity products complemented by duration assets”, which gives resilience across economic cycles and supports predictable earnings.")
    pg.fig(f"{C}/mix.png", "Figure 3 – Product mix of AUM, FY24–FY26. Sources: " + AR24 + " MD&A (FY24 mix); " + AR25 + " MD&CEO letter (FY25 mix); " + AR26 + " product pages (FY26 mix). ‘Business loans/other’ derived as residual.", 2.5)
    pg.table(["Engine", "Gold loans", "Mortgage loans (MT LAP + ST LAP/HL)"],
             [["AUM 31 Mar 2026 / share", "₹10,352 crore / 51.4%", "₹9,362 crore / 46.5% (MT LAP ₹5,570 cr; ST LAP+HL ₹3,792 cr)"],
              ["FY26 growth", "+76%", "+16.1%"],
              ["FY26 disbursements", "₹28,326 crore", "₹3,084 crore (MT LAP ₹2,180 cr; ST LAP+HL ₹904 cr)"],
              ["Average ticket", "₹2.7 lakh", "MT LAP ₹72.4 lakh; ST LAP ₹16.1 lakh"],
              ["Origination yield / collateral", "Portfolio LTV 60.9%; onboarding LTV ≈70%; 12.6 tonnes gold", "MT LAP 12.0%; ST LAP 15.1%; 82.2% self-occupied property"],
              ["Branch format", "558 gold branches (₹16.5 cr AUM each)", "129 MSME hubs + 70 co-located ‘Vyapaar’ branches"],
              ["Role in model", "Velocity, liquidity, high RoA, fee-light", "Duration, stable yield, cross-sell base, capital-intensive"]],
             widths=[1.6, 2.4, 3.05], font=8, source=f"{AR26}, Key Highlights p.2–3 and product pages p.10–13; Directors’ Report (branch network).")
    pg.p("How the model earns. Interest on loans (₹1,968 crore in FY26, 93% of interest income) is the primary revenue; income from direct assignment (₹102 crore), fee and commission (₹97 crore, including ₹33 crore from distributing Federal Bank products) and fair-value gains (₹18 crore) are secondary. Against this, finance costs absorbed 39.5% of total revenue, operating expenses 34.6% and credit cost 5.2%, leaving a pre-tax margin of 20.7% (derived from the FY26 statement of profit and loss). The model is capital-light at the margin through co-lending (₹2,433 crore of gold AUM) and sell-downs (₹2,579 crore in FY26), which keep 12.1% of AUM off the balance sheet.")
    P.append(pg)

    # ------------------------------------------------------------------ 32 Fedfina 2.0 commitments vs delivery
    pg = Page("Fedfina 2.0: Commitments versus Delivery")
    pg.p("The FY25 annual report made a series of explicit commitments. The table compares each commitment with the outcome reported in the FY26 annual report – a direct test of management credibility that a fundamental analyst should always perform.")
    pg.table(["FY25 commitment (source: FY25 report)", "FY26 outcome (source: FY26 report)", "Verdict"],
             [["Scale gold loans through branch-led expansion and productivity", "Gold AUM +76% to ₹10,352 crore; 148 branches added (74 gold); gold AUM per branch up ₹4.4 crore to ₹16.5 crore; tonnage +12% to 12.6 t", "Delivered"],
              ["Rebuild small-ticket LAP with sharper underwriting and collections", "ST LAP moved to API-led BRE model; ~76% of mortgage AUM from CIBIL >700; in-house collections 1.8x; disbursements ₹904 crore (FY25: ₹1,004 crore); Q4 run-rate rising", "Largely delivered; volumes still below FY24"],
              ["Scale mid-ticket LAP in a capital-efficient manner", "MT LAP AUM ₹5,570 crore; disbursements ₹2,180 crore (FY25: ₹2,303 crore); Q4 ₹632 crore (+16% QoQ); yield pressure acknowledged", "Partly – growth paused in H1, resumed in H2"],
              ["Move to a predominantly secured portfolio; stop unsecured BL (Dec 2024)", "₹886 crore BL portfolio assigned in H1 FY26; secured AUM 98.9% (FY25 ≈ 89%); on-book BL ₹48 crore (0.4%)", "Delivered"],
              ["Bring credit cost down (FY25: 1.8%)", "Credit cost 0.8% of average assets (−93 bps); Stage 2+3 share of amortised book 3.5% vs 7.4%", "Delivered"],
              ["Diversify funding, lengthen tenor", "Lenders 39 → 41; ECB USD 250 mn (17% of debt); CP 9%; ₹450 crore Tier II; fixed-rate share 10% → 40%", "Delivered"],
              ["Embed technology and data in decisioning", "BRE + Salesforce for ST LAP; Credit GPT; Fedfina Lite app; 90% e-NACH; 70% digital collections; 35% bot-served requests", "Delivered"],
              ["Protect profitability while restructuring", "PAT +53% to ₹343.6 crore; RoA 2.4% (Q4 2.6%); RoE 12.6% (Q4 14.0%); cost-to-income 57.2%", "Delivered"],
              ["Grow sustainably with discipline", "AUM +27.5%; GNPA 1.9% / NNPA 1.3%; CRAR 22.4%; but debt-equity rose to 4.6x", "Delivered with higher leverage"]],
             widths=[2.2, 3.75, 1.1], font=8)
    pg.p("What ‘Fedfina 2.0’ meant in practice. The FY25 report described the reset as a move from a growth-at-any-cost posture to a ‘secured, granular and digital’ model: unsecured business loans were discontinued in December 2024, the small-ticket mortgage team was rebuilt around a rules-based engine, collections were brought in-house and verticalised, and the funding desk was asked to lengthen tenor and lock in fixed rates. The FY26 report is the first full year in which all four changes were operating simultaneously, which is why its results are the appropriate test of the programme rather than FY25’s transition-year numbers.")
    pg.p("Reading the table. Eight of nine commitments were met or largely met within one year; the two qualifications are that small-ticket LAP volumes have not yet returned to FY24 levels (₹1,475 crore) and that growth was funded with more debt per rupee of equity. Importantly, management also disclosed the costs of the transition – ₹88 crore of net write-offs on amortised-cost loans, ₹50 crore on FVOCI loans, sale of 814 NPA accounts (₹105 crore principal) to ARCs, and a 24% fall in direct-assignment volume – rather than presenting only the favourable metrics. The FY26 report’s own summary is that the year marked “an inflection point in Fedfina’s financial trajectory … a meaningful recovery in profitability after the portfolio recalibration of FY 2024-25”.")
    P.append(pg)

    # ------------------------------------------------------------------ 33 Distribution
    pg = Page("Distribution Network and Geographic Presence")
    pg.p(f"Fedfina operates a hub-and-spoke ‘phygital’ network of {BRANCHES['FY26']} branches in 17 states and union territories (31 March 2026), up from {BRANCHES['FY25']} a year earlier and {BRANCHES['FY19']} in FY19. The network has three formats: {BRANCH_TOTAL[1]} gold-loan branches, {BRANCH_TOTAL[0]} MSME (mortgage) hubs and {BRANCH_TOTAL[2]} co-located ‘Vyapaar’ branches where small-ticket LAP teams sit inside existing gold-loan premises – a format introduced in FY26 to exploit the 20–25% customer overlap between the two products and reduce operating cost. Field teams extend reach to within about 30 km of each branch, supported by telemarketing and digital engagement, and a network of 200+ connectors, aggregators and trader partners supplies additional leads.")
    pg.fig(f"{C}/branches.png", "Figure 9 – Branch network by format, FY21–FY26. Sources: " + AR24 + " (FY21–FY24), " + AR25 + " p.7 (FY25), " + AR26 + " Directors’ Report (FY26). FY26 MSME count reflects re-classification of 70 hubs as co-located branches.", 2.5)
    top = BRANCH_STATE[:8]
    pg.table(["State / UT", "MSME", "Gold", "Co-located", "Total", "Share (%)"],
             [[s[0], s[1], s[2], s[3], s[4], f"{s[4]/757*100:.1f}"] for s in top] +
             [["Other 9 states/UTs (RJ, HR, UP, MP, PB, UK, Goa, PY, DNH, CH)", sum(s[1] for s in BRANCH_STATE[8:]), sum(s[2] for s in BRANCH_STATE[8:]), sum(s[3] for s in BRANCH_STATE[8:]), sum(s[4] for s in BRANCH_STATE[8:]), f"{sum(s[4] for s in BRANCH_STATE[8:])/757*100:.1f}"],
              ["Total", 129, 558, 70, 757, "100.0"]],
             widths=[3.0, 0.75, 0.75, 0.9, 0.75, 0.9], font=8, source=f"{AR26}, Directors’ Report – branch network as at 31 March 2026 (full state-wise list in Appendix C).")
    pg.p(f"Concentration. Four western and southern states – Maharashtra, Gujarat, Karnataka and Tamil Nadu – host 462 branches (61%), and the top five states accounted for {TOP5_STATES_AUM['FY26']}% of AUM in FY26, down steadily from {TOP5_STATES_AUM['FY21']}% in FY21 as the company expanded into Delhi NCR, Telangana, Rajasthan, Haryana, Uttar Pradesh and Madhya Pradesh. Geographic diversification reduces exposure to state-level events (floods, local regulation, agrarian stress) but adds operating complexity; the company notes it “expanded our reach across non-metro markets” and that the 148 FY26 branches are still young.")
    P.append(pg)

    # ------------------------------------------------------------------ 34 Customers
    pg = Page("Customer Segments and Customer Experience")
    pg.p(f"Fedfina served {KPI26['customers_lakh']} lakh active customers at 31 March 2026 – about {KPI26['cust_per_branch']} per branch. Its customers sit in what the Chairman calls the gap between India’s household credit-to-GDP ratio of 42% and the 60–76% seen in China, the US and the UK: self-employed households, small business owners and MSME borrowers in Tier 2–4 markets who are typically underserved by conventional banking channels.")
    pg.table(["Segment", "Who they are (company description)", "Typical need", "Product", "Credit profile disclosed"],
             [["Gold-loan customers", "Traders, owners of service and manufacturing units, their staff receiving informal cash wages, individuals with urgent needs (e.g., housewives)", "Short-term working capital and emergency liquidity", "Gold loan, doorstep gold loan", "Collateral-based; portfolio LTV 60.9%; 4,633 accounts auctioned in FY26 (0.2% of 12.6 t book value)"],
              ["Small-ticket LAP / HL borrowers", "Self-employed with informal income, median annual income ≈ ₹5 lakh, outskirts of Tier 1 and Tier 2–3 towns", "Business working capital, home purchase/extension", "ST LAP, affordable housing loan", "68% CIBIL >700, 16% 650–700, 7% <650, 9% new-to-credit"],
              ["Medium-ticket LAP borrowers", "Established traders, wholesalers, distributors, small manufacturers with formal income records", "Expansion capital, debt consolidation", "MT LAP", "81% CIBIL >700, 12% 650–700, 4% <650, 3% new-to-credit"],
              ["Business-loan customers (legacy)", "Eligible MSMEs needing short-term working capital", "Unsecured working capital", "Discontinued Dec 2024; portfolio assigned", "95% CIBIL >700 at the time of exit"]],
             widths=[1.25, 2.1, 1.3, 1.1, 1.3], font=7.5, source=f"{AR24} MD&A (gold customer profile); {AR26} MD&A ‘Portfolio quality’ (CIBIL distribution) and product pages.")
    pg.h2("Customer experience indicators")
    pg.kpis([("85%", "Positive customer-satisfaction score"), ("100%", "Complaints resolved within TAT"), ("35%", "Service requests auto-served via bot"),
             ("4.58 / 5", "Google rating; reviews 1,500 → 7,500+"), ("10 / 15 days", "Mortgage approval / disbursement TAT"), ("90%", "Loan accounts on e-NACH (86% registered digitally)")], cols=3)
    pg.p("Acquisition and engagement. The FY26 marketing report describes a hyperlocal approach: geo-targeted digital campaigns on Google and Meta, branch-level SEO through a partnership with Promanage, local activations and festival campaigns aligned to regional demand cycles. Digital channels generated roughly 17 lakh leads and 65,000+ conversions (about 4% lead-to-conversion) and telemarketing a further 3.7 lakh leads and 12,000+ conversions. About 75% of business is now originated by in-house teams, with DSA dependence reduced to 25% – a change management links directly to credit quality “from day one”. Customer-protection measures include a fair-practices code, transparent pricing, a grievance-redressal mechanism with an Internal Ombudsman (RBI Directions 2026), and financial-literacy programmes delivered through educational institutions and self-help groups.")
    P.append(pg)

    # ------------------------------------------------------------------ 35 Human capital
    pg = Page("Human Capital")
    pg.p(f"People are the principal operating cost of a branch-led lender: employee benefits of ₹{P26['emp']/100:,.0f} crore were 57.6% of FY26 operating expenses (derived). Headcount rose from {EMPLOYEES['FY24']:,} (FY24) to {EMPLOYEES['FY25']:,} (FY25) and {EMPLOYEES['FY26']:,} at 31 March 2026 – an addition of {EMPLOYEES['FY26']-EMPLOYEES['FY25']} in the year, largely to staff 148 new branches and the enlarged in-house collections and sales teams. AUM per employee was ₹{KPI26['aum_per_emp']} crore.")
    pg.table(["Indicator", "FY24", "FY25", "FY26", "Source / note"],
             [["Permanent employees (31 March)", f"{EMPLOYEES['FY24']:,}", f"{EMPLOYEES['FY25']:,}", f"{EMPLOYEES['FY26']:,}", "Directors’ Reports (remuneration disclosure)"],
              ["Employee benefit expense (₹ crore)", "–", cr(P25['emp'], 1), cr(P26['emp'], 1), "Note 33; +13.7% in FY26"],
              ["Share-based payment expense (₹ crore)", "–", cr(EMP_BREAKUP['Share based payments'][1], 1), cr(EMP_BREAKUP['Share based payments'][0], 1), "Note 33; ESOS 2018 and 2024"],
              ["Women in workforce (%)", "–", f"{KPI26['women_prev']}", f"{KPI26['women']}", "BRSR; target ≥22% women in senior management by FY28"],
              ["Average voluntary turnover (%)", "–", "–", f"{KPI26['attrition']}", "BRSR"],
              ["Average training hours per employee", "–", "–", f"{KPI26['training_hrs']}", "Corporate Overview; 70.3% attended ≥1 targeted session; 57 online modules"],
              ["Investment in employee development (₹ crore)", "–", "–", "0.27", "Corporate Overview"],
              ["Apprentices engaged", "–", "–", f"{KPI26['apprentices']}+", "Corporate Overview"],
              ["Median remuneration increase (%)", "–", "–", "6.32", "Directors’ Report; MD&CEO ratio to median 40.6:1"],
              ["POSH complaints (received / resolved / pending)", "–", "–", "3 / 3 / 0", "Directors’ Report"]],
             widths=[2.5, 0.7, 0.7, 0.7, 2.45], font=8)
    pg.h2("Capability building and culture")
    pg.p("The FY26 report describes a deliberate investment in capability alongside performance: the Gurukul programme delivers product and process training across gold, LAP and MT LAP teams and was extended to “Branch Gurukul Days” for face-to-face frontline learning; the DREAM programme targets high-performing relationship managers to build the leadership pipeline; monthly technology sessions with start-ups build AI awareness; and regular town halls and open leadership forums support internal communication. Employees are given a ‘voluntary day off’ for CSR volunteering. Rewards include ESOS 2018 and ESOS 2024 – 14,89,247 shares were allotted to employees on exercise of options during FY26 – and the ‘Fedfina Lite’ mobile app was launched to raise field productivity.")
    pg.p("Assessment. Voluntary attrition of 35.85% is the number to watch: it is typical of field-sales-heavy NBFCs but expensive in underwriting and collections roles, where tenure drives judgement. The Directors’ Report describes employee strength as having “grown 6.3%”, whereas the disclosed headcount rose about 16%; the report records both and treats the headcount figures as authoritative. Female representation (16.4%) is low but rising, and the FY28 senior-management target is specific and time-bound.")
    P.append(pg)

    # ------------------------------------------------------------------ 36 Technology
    pg = Page("Technology, Digital Transformation and Cyber-Security")
    pg.p("The company’s FY25 report described a migration to a fully digital loan-origination platform and the FY26 report documents the next layer: integration of the loan-origination system, loan-management system and CRM; an API-led, system-driven operating model for small-ticket LAP anchored on a business rule engine (BRE) and Salesforce; and AI tools (“Credit GPT” and AI-powered assistants) for query resolution and credit evaluation. Through the ‘Startup Friday’ initiative, 89 start-ups were evaluated, 6 onboarded and 8 are under proof-of-concept.")
    pg.table(["Layer", "Systems / partners named in the FY26 report", "Business outcome disclosed"],
             [["Origination and underwriting", "Digital LOS; Business Rule Engine; Salesforce; Perfios, Experian, TrackWizz, Setu (Account Aggregator), Digio, SignDesk, Lentra, Nucleus Software", "Consistent ST LAP decisions; reduced process variability; 10-day approval TAT; ~76% of mortgage AUM from CIBIL >700"],
              ["Customer servicing", "Fedfina Loans app; chatbot; e-NACH; BillDesk, Paytm", "35% of service requests auto-served; 90% e-NACH coverage, 86% registered digitally; 100% resolution within TAT"],
              ["Collections", "Fedfina Collect app; digital payment rails", "Over 70% of monthly collections through digital channels; collection efficiency 99.7%"],
              ["Field productivity", "Fedfina Lite app (unified lead, application and tracking interface); Tableau analytics", "Faster field processing; data-led branch-level campaign targeting"],
              ["Infrastructure and security", "AWS cloud; Microsoft 365/Teams; Palo Alto, Fortinet, Netskope, Forcepoint, Klassify, ManageEngine; Zero Trust network access, MFA, EDR/XDR, VAPT, red-team exercises, vendor risk management", "No material cyber incident disclosed; IT Strategy Committee met 4 times; prototype ‘security box’ for doorstep gold (dual authentication, live tracking, remote unlock)"]],
             widths=[1.4, 3.1, 2.55], font=8, source=f"{AR26}, Corporate Overview – ‘Our Digital Landscape’, technology and cyber-security sections; MD&CEO statement; Report on Corporate Governance (IT Strategy Committee).")
    pg.h2("Cost of technology")
    pg.p(f"Technology cost in other expenses was ₹{OTHER_EXP_TOP['Technology cost'][0]/100:.1f} crore in FY26 (FY25: ₹{OTHER_EXP_TOP['Technology cost'][1]/100:.1f} crore) – flat year-on-year despite a 23% larger loan book, suggesting the platform investments were largely made in earlier years and are now being leveraged. Intangible assets on the balance sheet were small (₹3.6 crore plus ₹0.3 crore under development), consistent with a software-as-a-service model in which most technology spend is expensed.")
    pg.h2("Why technology matters to the thesis")
    pg.p("The FY25 problem – collections infrastructure lagging growth – was fundamentally an information problem: the company could not see early delinquency quickly enough or allocate collectors efficiently. The FY26 tools address precisely this: BRE-driven underwriting removes discretion at origination, early-warning signals and digital collections shorten resolution cycles (early-bucket cure rates up ~2 percentage points, Stage 1–2 cure rates up 5–6 points, monthly Stage 3 recoveries up from ₹6.5 crore to ₹14.5 crore), and the integrated LOS–LMS–CRM stack gives management a single view of each customer. Cyber-security is the other side of the coin: the company’s own MD&A flags a sharp rise in attacks on BFSI digital portals, and the Zero-Trust/MFA/EDR stack is the mitigation. The analytical conclusion is that technology has moved from enabler to control function at Fedfina – a positive for sustainability of asset quality, provided the controls keep pace with the 148 new branches.")
    P.append(pg)

    # ------------------------------------------------------------------ 37 Board & governance
    pg = Page("Board of Directors and Corporate Governance")
    pg.p("At the date of the FY26 Directors’ Report the Board comprised nine directors: one non-executive non-independent Chairman, two nominee directors of Federal Bank, five independent directors (including two women) and the Managing Director & CEO. The Chairman is not related to the MD&CEO. A third nominee director, representing True North Fund VI LLP, resigned on 14 May 2026 following the fund’s exit. The Board met 11 times during FY26 (23 and 28–29 April, 2 May, 28 July, 25 August, 17 October, 7 November 2025; 15 January, 26 February and 3 March 2026) with no gap exceeding 120 days.")
    pg.table(["Director", "Category", "Background / role (as disclosed)"],
             [["Mr. Shyam Srinivasan", "Non-Executive Chairman", "Former MD&CEO of Federal Bank for fourteen years; earlier Citibank and Standard Chartered; DIN 02274773"],
              ["Mr. K.V.S. Manian", "Nominee Director (Federal Bank)", "MD&CEO of Federal Bank"],
              ["Mr. Harsh Dugar", "Nominee Director (Federal Bank)", "Executive Director, Federal Bank; retires by rotation at the 31st AGM and offers himself for re-appointment"],
              ["Mr. Maninder Singh Juneja", "Nominee Director (True North) – resigned 14 May 2026", "Represented True North Fund VI LLP until its exit"],
              ["Mr. Sunil Gulati", "Independent Director", "Banking and financial services professional; remuneration ratio to median 3.9:1"],
              ["Mr. Ramesh Sundararajan", "Independent Director", "Remuneration ratio to median 4.2:1"],
              ["Ms. Sonal Dave", "Independent Director", "Remuneration ratio 4.02:1"],
              ["Ms. Mona Bhide", "Independent Director", "Remuneration ratio 3.2:1"],
              ["Mr. Muralidharan Rajamani", "Independent Director (from 24 Jan 2025; approved 16 Apr 2025)", "Remuneration ratio 4.1:1"],
              ["Mr. Parvez Mulla", "Managing Director & CEO", "Leads Fedfina 2.0; remuneration ratio to median 40.6:1; 15% increase in FY26"]],
             widths=[1.7, 2.0, 3.35], font=8, source=f"{AR26}, Corporate Information, Directors’ Report (changes in directorship; remuneration disclosure under Rule 5(1)).")
    pg.h2("Governance architecture and FY26 disclosures")
    pg.bullets([
        "Committees:: Audit, Nomination & Remuneration, Stakeholders’ Relationship, Risk Management, CSR, IT Strategy (met 4 times), plus ALCO, Business Development, Committee of Directors (Operations), Wilful Default Review, Customer Service and a Special Committee for monitoring frauds.",
        "Auditors:: Statutory – KKC & Associates LLP (unmodified opinion; term to the 32nd AGM); joint statutory auditor V. Sankar Aiyar & Co. proposed from the 31st AGM under RBI’s 2026 directions for NBFCs with assets ≥ ₹15,000 crore; secretarial – DKJ & Associates (no qualification).",
        "KMP changes:: Company Secretary Mr. Rajaraman Sundaresan completed his term on 31 July 2025; Mr. Parthasarathy Iyengar appointed from 1 August 2025. CFO: Mr. C.V. Ganesh.",
        "Integrity mechanisms:: whistle-blower policy (16 complaints in FY26, 3 under the vigil mechanism); POSH committee (3 complaints, all resolved); fraud policy (₹110 lakh of frauds reported to RBI); related-party transactions at arm’s length (Federal Bank interest paid ₹84.8 crore).",
        "Regulatory record:: no RBI penalty disclosed; three BSE fines for filing delays (₹10,000 and ₹1,53,400 relating to 2023; ₹10,000 relating to 2024, later waived).",
    ])
    P.append(pg)

    # ------------------------------------------------------------------ 38 Capital raising, listing, ratings
    pg = Page("Capital Raising, Listing History and Credit Ratings")
    pg.p("Equity. Fedfina’s equity base was built in three stages: promoter capital from Federal Bank; a ₹168.6 crore investment by True North in 2018 (which later exited in FY26); and the November 2023 IPO of ₹1,092 crore comprising a ₹600 crore fresh issue and an offer for sale, subscribed about 2.2 times. Share capital at 31 March 2026 was ₹374.2 crore (37,42,06,101 shares of ₹10) after the allotment of 14,89,247 ESOP shares during the year; other equity was ₹2,551.9 crore. No equity has been raised since the IPO – FY24–FY26 growth was funded entirely by retained earnings and debt, which is why debt-equity rose from 3.6x (FY24, derived) to 4.6x.")
    pg.table(["Equity indicator", "FY23", "FY24", "FY25", "FY26"],
             [["Net worth (₹ crore)", cr(F23['nw'], 0), cr(F24['nw'], 0), cr(F25['nw'], 0), cr(F26['nw'], 0)],
              ["Book value per share (₹)", f"{F23['bvps']:.2f}", f"{F24['bvps']:.2f}", f"{F25['bvps']:.2f}", f"{F26['bvps']:.2f}"],
              ["Basic EPS (₹)", f"{F23['eps']:.2f}", f"{F24['eps']:.2f}", f"{F25['eps']:.2f}", f"{F26['eps']:.2f}"],
              ["Dividend", "Nil", "Nil", "Nil", "Nil (recommended)"],
              ["Debt / equity (x, derived = borrowings ÷ net worth)", f"{F23['borr']/F23['nw']:.2f}", f"{F24['borr']/F24['nw']:.2f}", f"{F25['borr']/F25['nw']:.2f}", f"{F26['borr']/F26['nw']:.2f}"],
              ["Market capitalisation (₹ crore, 31 March)", "unlisted", "n.a.", "n.a.", f"{MCAP_CR:,}"]],
             widths=[3.0, 1.0, 1.0, 1.0, 1.05], source="Directors’ Reports FY24–FY26 (financial highlights); " + AR26 + " inside cover (market capitalisation).")
    pg.h2("Debt capital markets activity in FY26")
    pg.p("The Board approved fresh NCD issuance of up to ₹2,500 crore on 25 August 2025 and the company issued ₹200 crore of 7.29% secured reset-rate NCDs (6 January 2026), ₹250 crore of 8.85% and ₹200 crore of 8.90% unsecured subordinated Tier II NCDs (24 March 2026). Commercial paper outstanding peaked at ₹1,375 crore during the year (FY25: ₹575 crore). The USD 250 million ECB programme, fully hedged through cross-currency swaps, lifted ECB borrowings from ₹257 crore to ₹2,382 crore. The debenture trustees are Axis Trustee, Beacon Trusteeship and IDBI Trusteeship; the registrar is MUFG Intime India. Appendix D lists all NCDs outstanding.")
    pg.h2("Credit ratings")
    pg.table(["Agency", "Long-term instruments (bank loans / NCDs / sub-debt)", "Short-term (CP)", "Change over study period"],
             [["CARE Ratings", "AA+ / Stable", "A1+", "Upgraded to AA+/Stable in FY24"],
              ["CRISIL Ratings", "AA+ / Stable", "A1+", "AA/Positive in FY24 → AA+/Stable"],
              ["India Ratings & Research", "AA+ / Stable", "A1+", "AA+/Stable since FY24"],
              ["ICRA", "AA+ / Stable", "A1+", "Added as fourth agency"]],
             widths=[1.5, 2.6, 1.0, 1.95], source=f"{AR26}, Report on Corporate Governance – credit ratings; {AR24} journey page (FY24 ratings).")
    pg.p("Four AA+/Stable ratings place Fedfina one notch below the AAA enjoyed by the largest NBFCs and bank-backed lenders, and give it access to mutual funds, insurers and pension funds for its NCDs and CP. The rating headroom is important for the funding-cost analysis in Chapter 5: any downgrade would raise the cost of the 13% of debt that is market-sourced and could restrict CP access.")
    P.append(pg)

    # ================================================================== CHAPTER 4 PRODUCTS
    pg = Page("Chapter 4 — Product Portfolio Overview")
    pg.p("Fedfina offers four products: gold loans, medium-ticket loans against property (MT LAP), small-ticket loans against property and housing loans (ST LAP + HL), and – until its discontinuation in December 2024 – unsecured business loans. The table summarises the FY26 key numbers for each product exactly as disclosed on the product pages of the FY26 annual report, followed by the five-year disbursement trend.")
    pg.table(["Product", "AUM 31 Mar 2026 (₹ cr)", "Share of AUM", "FY26 disbursements (₹ cr)", "Average ticket", "Growth drivers cited"],
             [["Gold loans", "10,352", "51.4%", "28,326", "₹2.7 lakh", "Gold price rally; shift to secured credit; branch expansion; doorstep channel; co-lending"],
              ["Medium-ticket LAP", "5,570", "27.6%", "2,180", "₹72.4 lakh", "MSME demand; property-led wealth effect; Tier 2–3 growth; digital underwriting"],
              ["Small-ticket LAP and housing loans", "3,792", "18.8%", "904", "₹16.1 lakh", "Softening rates; affordable-housing demand; self-employed/informal-income reach; branch co-location"],
              ["Business loans (legacy, on book)", "≈ 48", "0.4% (unsecured ≈ 2%)", "nil", "–", "Phased down under Fedfina 2.0; ₹886 crore assigned"],
              ["Total", "20,153", "100%", "31,410", "", "AUM +27.5%; disbursements +67%"]],
             widths=[1.5, 1.0, 0.9, 1.1, 0.8, 1.75], font=8, source=f"{AR26}, product pages p.10–13 and Key Highlights p.2–3; Directors’ Report (total disbursements ₹31,41,014 lakh). Shares sum to 98.2% because the residual is business loans/other.")
    pg.fig(f"{C}/disb.png", "Figure 10 – Disbursements by product, FY22–FY26 (₹ crore). Source: " + AR26 + ", five-year product disbursement charts (Corporate Overview); FY22–FY24 cross-checked with " + AR24 + ".", 2.5, width=5.6)
    pg.p(f"The chart makes the shift visible. Gold disbursements rose from ₹{DISB_GOLD['FY22']:,} crore in FY22 to ₹{DISB_GOLD['FY26']:,} crore in FY26 ({cagr(DISB_GOLD['FY22'], DISB_GOLD['FY26'], 4):.0f}% CAGR, derived), 90% of all disbursements – though short-tenor gold volume adds less AUM than equal mortgage volume. MT LAP disbursements quadrupled between FY22 and FY25 before a 5% pause in FY26; ST LAP peaked at ₹{DISB_STLAP['FY24']:,} crore in FY24 and was cut to ₹{DISB_STLAP['FY25']:,} crore and ₹{DISB_STLAP['FY26']:,} crore during the rebuild. Total FY26 disbursements of ₹31,410 crore were 67% above FY25 (₹18,787 crore) and 2.3x FY24 (₹13,578 crore).")
    P.append(pg)

    # ------------------------------------------------------------------ 40 Gold loan review
    pg = Page("Gold Loans: Performance Review")
    pg.p(f"Gold loans became Fedfina’s largest product in FY26. AUM grew 76% to ₹10,352 crore and crossed the ₹10,000 crore mark for the first time; gold under custody rose 12% to 12.6 tonnes; disbursements nearly doubled to ₹28,326 crore; and the product contributed 51.4% of AUM against 32.6% two years earlier. Gold-backed loans were {L26['gold_pct_assets']}% of total assets at 31 March 2026 (FY25: {L25['gold_pct_assets']}%) – a regulatory disclosure that also marks the scale of the shift.")
    pg.table(["Metric", "FY24", "FY25", "FY26", "Source"],
             [["Gold AUM (₹ crore)", "3,969", "5,880", "10,352", "AR24 MD&A; AR25 CEO letter; AR26 p.10"],
              ["Share of total AUM", "32.6%", "37.2%", "51.4%", "as above"],
              ["Disbursements (₹ crore)", f"{DISB_GOLD['FY24']:,}", f"{DISB_GOLD['FY25']:,}", f"{DISB_GOLD['FY26']:,}", "AR26 five-year chart"],
              ["Average ticket size", "₹1.1 lakh", "n.a.", "₹2.7 lakh", "AR24 MD&A; AR26 Key Highlights"],
              ["Portfolio LTV", "70.5%", "n.a.", "60.9%", "AR24 MD&A; AR26 MD&CEO"],
              ["Gold branches", "438", "484", "558", "AR24/AR25/AR26 branch tables"],
              ["Doorstep gold loan (DSGL) share of gold AUM", "n.a.", "just under 15% (AUM doubled; 13,000+ new customers)", "₹1,730 crore (≈16.7%, derived)", "AR25 CEO letter; AR26 p.10"],
              ["Gold auctions – accounts / principal (₹ lakh)", "n.a.", "10,906 / 5,080", "4,633 / 2,039", "AR26 Directors’ Report and note 48"]],
             widths=[2.4, 0.9, 1.5, 1.2, 1.05], font=8)
    pg.h2("Price versus tonnage")
    pg.p("Because gold prices rose about 65% during calendar 2025, part of the AUM growth is a valuation effect. The company itself separates the two: tonnage grew 12%, so the remaining growth came from higher loan amounts per gram and higher onboarding LTV (≈70%) on new loans. On a simple decomposition (derived), a 12% tonnage increase combined with a 76% AUM increase implies AUM per gram rose about 57% – consistent with the price move. The Chairman nonetheless states that growth was “driven by physical tonnage growth rather than price effects alone”, and management targets a 10–12% long-term tonnage CAGR “rather than relying solely on gold price movements”. For the analyst the implication is that roughly one-sixth of FY26 gold growth is replicable without price support, and the rest depends on gold staying near current levels.")
    pg.p("Branch productivity. With 558 gold branches, AUM per branch was ₹16.5 crore, up ₹4.4 crore in the year even though 74 of the branches were newly opened. Mature-branch productivity is therefore higher than the average, and the FY26 cohort provides built-in growth as it seasons. Co-lending (₹2,433 crore) and sell-downs are used to keep part of the gold book off balance sheet, while the DSGL channel (₹1,730 crore, +108%) extends reach without new premises.")
    P.append(pg)

    # ------------------------------------------------------------------ 41 Gold controls/LTV/auctions
    pg = Page("Gold Loans: Risk Controls, LTV Policy and Auctions")
    pg.p("A gold loan is only as safe as its custody, purity assessment and LTV discipline. The company discloses several layers of control, which are summarised here together with the FY26 auction data and the changes required by the RBI’s 2025 Directions.")
    pg.table(["Control area", "Practice disclosed", "FY26 evidence"],
             [["Loan-to-value", "Portfolio LTV held at 60.9% against the regulatory ceiling (75% in FY26; 75–85% tiered from 1 April 2026); onboarding LTV calibrated at ≈70%; prices tracked daily", "A 35–40% price fall would be needed before principal is uncovered on the average loan (derived)"],
              ["Valuation and purity", "Standardised appraisal at branch; AI/analytics for fraud detection; cash disbursal capped at ₹20,000 per RBI", "Frauds reported to RBI ₹110 lakh across all products (0.005% of AUM, derived)"],
              ["Custody", "Branch strong-rooms; insurance; prototype portable ‘security box’ with dual authentication, live GPS tracking and remote unlocking for doorstep loans", "DSGL AUM ₹1,730 crore delivered without a disclosed custody loss"],
              ["Collections and auctions", "Borrower notices, renewal/top-up options, auction as last resort under RBI norms; surplus refunded", "4,633 accounts auctioned (FY25: 10,906); principal ₹20.4 crore and interest ₹27.6 crore outstanding; ₹44.0 crore realised"],
              ["Concentration", "Small tickets (₹2.7 lakh) and ~3.4 lakh customers; top-20 borrowers 0.47% of advances (all products)", "Portfolio granular by construction"],
              ["Co-lending", "Gold loans originated under RBI co-lending with bank partners (₹2,433 crore)", "Risk shared with partners; income recognised on retained share and servicing"]],
             widths=[1.3, 3.1, 2.65], font=8, source=f"{AR26}, MD&CEO statement, Directors’ Report (gold auctions, frauds), note 48 (concentration, auctions), technology section.")
    pg.h2("Auction economics")
    pg.p("Accounts auctioned fell 58% (10,906 → 4,633) and principal at auction fell 60% (₹50.8 crore → ₹20.4 crore) as rising prices let more borrowers redeem or refinance. Realisation of ₹44.0 crore against total dues of ₹48.0 crore indicates recovery of about 92% of dues, with the shortfall confined to accrued interest. No sister-concern participation in auctions is reported.")
    pg.h2("Impact of the 2025 RBI Directions")
    pg.p("From 1 April 2026 the tiered LTV ceiling (85%/80%/75%), the requirement to maintain LTV through the tenor (computed on the maturity amount for bullet loans), the 12-month cap on bullet loans, mandatory credit assessment above ₹2.5 lakh and standardised auction/return-of-gold norms apply. Fedfina’s conservative portfolio LTV, daily price tracking and existing short-tenor design mean the direct balance-sheet impact should be limited; the operational impact lies in renewal/top-up behaviour (the FY25 report already noted volume pressure from revised rollover rules) and in documentation for larger tickets. Higher permitted LTV on small loans could support growth in the ₹2.5 lakh and below segment that forms the bulk of the book.")
    pg.p("Assessment. Low average LTV, granular tickets, falling auction counts and a 92% realisation rate make the gold book the lowest-risk part of the balance sheet in credit terms; its risks are market (price) and operational (custody, fraud) rather than borrower default – a theme developed in Chapter 6.")
    P.append(pg)

    # ------------------------------------------------------------------ 42 MT LAP
    pg = Page("Medium-Ticket Loans Against Property (MT LAP)")
    pg.p("Medium-ticket LAP serves established MSMEs – traders, wholesalers, distributors and small manufacturers with formal income records – with property-backed term loans averaging ₹72.4 lakh. It is Fedfina’s second-largest product (₹5,570 crore, 27.6% of AUM) and its oldest mortgage business (launched 2012). The product competes directly with private banks and large NBFCs, so pricing discipline and service are its differentiators; the FY26 origination yield was 12.0%, the lowest in the portfolio.")
    pg.kpis([("₹5,570 cr", "AUM, 31 Mar 2026"), ("₹2,180 cr", "FY26 disbursements (Q4: ₹632 cr, +16% QoQ)"), ("₹72.4 lakh", "Average ticket"),
             ("12.0%", "Origination yield"), ("81%", "AUM from CIBIL >700 customers"), ("129", "MSME hubs")], cols=3)
    pg.table(["Metric", "FY22", "FY23", "FY24", "FY25", "FY26"],
             [["Disbursements (₹ crore)"] + [f"{DISB_MTLAP[y]:,}" for y in YEARS5],
              ["YoY growth (derived)", "–"] + [f"{(DISB_MTLAP[YEARS5[i]]/DISB_MTLAP[YEARS5[i-1]]-1)*100:+.0f}%" for i in range(1, 5)],
              ["Mortgage AUM, all LAP + HL (₹ crore)", "n.a.", "n.a.", "6,218", "8,060", "9,362"],
              ["Mortgage share of AUM", "n.a.", "n.a.", "51.0%", "51.0%", "46.5%"]],
             widths=[2.6, 0.85, 0.85, 0.9, 0.9, 0.95], source=f"{AR26} five-year disbursement chart and product page; {AR24} MD&A; {AR25} CEO letter. Product-level AUM for MT LAP is disclosed only for FY26.")
    pg.h2("FY26 performance and outlook")
    pg.p("Disbursements of ₹2,180 crore were 5% lower than FY25’s ₹2,303 crore, reflecting a deliberate slowdown in H1 while the mortgage business was re-staffed and re-tooled, followed by a strong recovery in H2: Q4 disbursements of ₹632 crore were 16% higher sequentially. Management acknowledges “broader industry yield pressures” in this segment – a consequence of bank competition and falling policy rates – and has therefore positioned MT LAP as the capital-efficient, lower-risk engine to be scaled “in a capital-efficient manner” (FY25 strategy) rather than the margin driver. Credit quality is the strongest among the mortgage products: 81% of AUM is from customers with CIBIL above 700 and only 3% is new-to-credit.")
    pg.h2("Sourcing, underwriting and collateral")
    pg.bullets([
        "Sourcing through 129 MSME hubs, in-house relationship managers (≈75% of total origination is in-house), DSAs (25%), builder tie-ups and digital channels; 200+ connectors and trader partners.",
        "Underwriting on documented income (GST, bank statements via Account Aggregator, financials) plus property valuation; 10-day approval and 15-day disbursement TAT.",
        "Collateral is predominantly residential and self-occupied property (82.2% of mortgage AUM backed by self-occupied property); regulatory real-estate exposure at 31 March 2026 was ₹5,413 crore residential and ₹852 crore commercial (note 48).",
        "Loans against property to MSMEs qualify as priority-sector lending for bank co-lenders and assignees, supporting sell-down demand (₹2,579 crore sold down across products in FY26).",
    ])
    pg.p("Assessment. MT LAP’s role is stability rather than growth: it carries the longest duration, the best bureau profile and the lowest yield. Its principal risks are yield compression and balance-transfer attrition as banks compete for the same prime MSME borrowers; its principal opportunity is cross-selling into the 3.4 lakh customer base and the 70 co-located branches.")
    P.append(pg)

    # ------------------------------------------------------------------ 43 ST LAP + HL
    pg = Page("Small-Ticket LAP and Housing Loans: Reset and Rebuild")
    pg.p("Small-ticket LAP and affordable housing loans (average ticket ₹16.1 lakh; AUM ₹3,792 crore, 18.8% of total) serve self-employed borrowers with informal incomes – median annual income around ₹5 lakh – in the outskirts of Tier 1 cities and in Tier 2–3 towns. It is the highest-yielding mortgage product (origination yield 15.1%) and the most operationally demanding. It is also the product whose FY25 stress triggered the Fedfina 2.0 reset, making it the most important product to understand for a judgement on sustainability.")
    pg.table(["Phase", "What the company disclosed", "Numbers"],
             [["FY22–FY24: rapid growth", "ST LAP disbursements grew every year; small-ticket book built through branch expansion and DSA sourcing", f"Disbursements ₹{DISB_STLAP['FY22']} cr → ₹{DISB_STLAP['FY23']:,} cr → ₹{DISB_STLAP['FY24']:,} cr; MSME hubs 109 → 183"],
              ["FY25: stress and reset", "“Elevated level of delinquencies with a delay and drop in realisation for deeper-bucket NPA pools … attributable to our collection infrastructure having not kept pace with business growth”; provisions shored up; new leadership", f"Credit cost 1.8% (FY24 0.7%); impairment ₹216 crore; disbursements cut to ₹{DISB_STLAP['FY25']:,} cr; Stage 2 loans 5.1% of amortised book"],
              ["FY26: rebuild", "API-led, system-driven operating model anchored by a Business Rule Engine and Salesforce; in-house collections 1.8x; agency reliance 0.4x; 70 ST LAP branches co-located in gold premises; sale of deeply delinquent pools to ARCs", f"Disbursements ₹{DISB_STLAP['FY26']} cr with rising quarterly run-rate; new book quality better than old book; Stage 2 share 1.9%; 814 NPA accounts (₹105 cr) sold to ARCs; credit cost 0.8%"]],
             widths=[1.4, 3.5, 2.15], font=8, source=f"{AR25}, MD&CEO letter p.12–15; {AR26}, MD&CEO statement p.18–21, product page p.11, note 48 (NPA sales).")
    pg.h2("Credit profile of the new book")
    pg.p("The FY26 MD&A discloses the bureau distribution of the small-ticket LAP and housing-loan portfolio: 68% of AUM from customers with CIBIL above 700, 16% between 650 and 700, 7% below 650 and 9% new-to-credit (score 0/−1). Compared with MT LAP (81% above 700) this is a riskier profile, as expected for the segment, but the company states that the new book is performing better than the old book, that early-bucket cure rates improved by about 2 percentage points and Stage 1–2 cure rates by 5–6 points, and that monthly Stage 3 recoveries more than doubled to ₹14.5 crore. Collateral is mostly self-occupied residential property, and borrowers are assessed on observed household cash flows rather than documents alone.")
    pg.h2("Housing loans")
    pg.p("Affordable housing loans are bundled with ST LAP in reporting and distributed through the same hubs. The FY26 report cites softening interest rates, improved affordability and eligibility, healthy demand in affordable and Tier 2–3 markets, expansion of sourcing through branches, DSAs, builder tie-ups and digital channels, and stable funding access as the segment’s growth drivers. Housing loans lengthen the portfolio’s duration and carry lower yields than LAP, but they also qualify for priority-sector treatment within limits and support co-lending.")
    pg.p("Assessment. ST LAP is where the thesis will be proved or disproved. The evidence so far – lower Stage 2, better cure rates, system-driven underwriting, in-house collections and a conservative restart in volumes – is positive, but the FY26 cohort is less than a year old. The appropriate analytical stance is to monitor 30+ and 90+ day delinquency on the FY26 vintage through FY27 before concluding that the rebuild is complete.")
    P.append(pg)

    # ------------------------------------------------------------------ 44 BL exit
    pg = Page("Exit from Unsecured Business Loans")
    pg.p("Fedfina began distributing unsecured business loans in 2018 and built the book to roughly 16% of AUM by FY24 (derived from the FY24 product mix) and ₹1,656 crore (10.5%) by March 2025. The product offered high yields and quick disbursement to MSMEs needing short-term working capital, but it also carried the highest credit losses and the greatest sensitivity to the unsecured-credit stress that spread across the industry in FY25. Fresh origination was stopped in December 2024 and, under Fedfina 2.0, the portfolio was “gradually phased down as the Company transitions towards a predominantly secured lending portfolio”.")
    pg.table(["Step", "Date / period", "Detail", "Effect"],
             [["Stop new origination", "December 2024", "FY25 report: unsecured business lending discontinued", "No new unsecured exposure"],
              ["Opening position FY26", "1 April 2025", "Business-loan AUM ₹1,656 crore; assets under finance (on-book) ₹1,216 crore", "≈10.5% of AUM unsecured"],
              ["Portfolio assignment", "H1 FY26", "Complete assignment of ₹886 crore business-loan portfolio; sale of deeply delinquent pools to ARCs", "Took the company “out of unsecured lending in H1 FY 2025-26”"],
              ["Closing position FY26", "31 March 2026", "On-book business loans ≈ ₹48 crore (0.4% of AUF); unsecured loans in note 8 ₹48.4 crore (FY25: ₹1,232 crore); secured AUM 98.9%", "Fully secured construct achieved"],
              ["P&L cost", "FY26", "Bad debts net of recovery ₹83.5 crore (amortised) and ₹50.2 crore (FVOCI); ECL provisions released ₹12.3 crore as the unsecured book left the balance sheet", "Credit cost 0.8% despite clean-up"]],
             widths=[1.4, 1.1, 3.0, 1.55], font=8, source=f"{AR26}, MD&CEO statement (‘Our Fully Secured Construct’), note 8 (secured/unsecured split), note 32 (impairment); {AR25}, MD&CEO letter.")
    pg.h2("Why the exit matters analytically")
    pg.bullets([
        "Loss-given-default:: an unsecured MSME loan that defaults is largely written off, whereas a gold or property loan recovers most of its principal. Removing the unsecured book structurally lowers expected credit cost; the FY26 impairment note shows provision releases on both amortised and FVOCI books.",
        "Capital:: unsecured loans attract 100% risk weight; gold loans and qualifying mortgages attract lower weights. The exit therefore supports the CRAR (22.4%) even as the balance sheet grows.",
        "Earnings mix:: the business-loan yield premium is lost, but FY26 shows NIM of 8.8% and spread of 8.6% – above FY25 – because gold yields and lower funding costs more than compensated.",
        "Credibility:: the company chose to crystallise losses (ARC sales, write-offs) rather than carry them, and disclosed the amounts; the FY25 provision build (₹216 crore impairment) was the price of that choice.",
    ])
    pg.p("Assessment. The exit converts Fedfina into a pure secured lender comparable in risk construct to the large gold-loan NBFCs and the affordable-housing financiers, at the cost of a slightly lower blended yield. Given sector-wide stress in unsecured small-business credit, the decision looks well-timed; its success will be measured by whether credit cost stays within the sub-1% commitment through FY27.")
    P.append(pg)

    # ------------------------------------------------------------------ 45 Co-lending / DA
    pg = Page("Co-lending, Direct Assignment and Off-Book AUM")
    pg.p("Fedfina uses two capital-light mechanisms. Under RBI’s co-lending model a bank funds most of a loan originated and serviced by the NBFC, which retains a minority share on book. Under direct assignment (DA) the NBFC sells a seasoned pool to a bank, retains minimum risk and services the loans; the excess interest spread is recognised as DA income. Both keep AUM off balance sheet and improve capital efficiency, but DA income is front-loaded and affects earnings quality.")
    pg.table(["Indicator", "FY24", "FY25", "FY26", "Source"],
             [["Off-book AUM as % of total AUM", "18.7%", "25.1%", "12.1%", "Directors’ Reports FY24–FY26"],
              ["Co-lending AUM (₹ crore)", "522", "1,131", "2,433", "Directors’ Reports (co-lending); FY26 gold loans"],
              ["Sell-down / DA during the year (₹ crore)", "1,461", "2,130", "2,579", "Directors’ Reports"],
              ["Direct-assignment balance (₹ crore)", "n.a.", "2,349", "1,901", "Corporate Overview (‘DA book down 24%’, derived from the two figures: −19%)"],
              ["Income on direct assignment (₹ crore)", "n.a.", "152.3", "102.0", "Note 26 (interest income)"],
              ["DA income as % of PBT", "n.a.", "21.7%", "1.6% (company) / 22.1% (derived from note 26 ÷ PBT)", "FY26 Corporate Overview vs derived – see note below"],
              ["Loans at FVOCI (held for sale, ₹ crore)", "n.a.", "3,444", "2,982", "Note 8"],
              ["Securitisation expenses (₹ crore)", "n.a.", "6.7", "11.6", "Note 34"]],
             widths=[2.4, 0.8, 0.8, 1.6, 1.45], font=8)
    pg.p("Note on DA income. The Corporate Overview states that income from direct assignment fell to ₹7.4 crore (−88.8%), 1.6% of PBT, whereas note 26 shows “income on direct assignment” of ₹102.0 crore (FY25: ₹152.3 crore). The definitions evidently differ (up-front gain on new assignments versus total accruals on the assigned pool). Both are shown; on either basis dependence on DA income fell sharply.")
    pg.h2("Interpretation")
    pg.bullets([
        "Shift from DA to co-lending:: co-lending AUM more than doubled while the DA balance shrank 19%, and off-book AUM fell from 25.1% to 12.1%. Co-lending income accrues over the life of the loan and is less volatile than DA gains – a positive for earnings quality.",
        "AUM versus on-book loans:: AUM of ₹20,153 crore compares with gross on-book loans of ₹14,505 crore (note 8); the ₹5,648 crore gap (28%) exceeds the 12.1% off-book disclosure, indicating that AUM also includes co-lending partners’ shares and possibly other managed assets. The company does not publish a full bridge, and this report does not attempt to construct one.",
    ])
    P.append(pg)

    # ------------------------------------------------------------------ 46 Product economics
    pg = Page("Product Economics and Portfolio Quality by Product")
    pg.p("Public disclosures do not give a product-level profit and loss, but they do give enough to compare the economics of each product on yield, ticket size, tenor, collateral and bureau quality. The table consolidates those datapoints; where a figure is a derived approximation it is marked.")
    pg.table(["Dimension", "Gold loans", "Medium-ticket LAP", "Small-ticket LAP + HL", "Business loans (exited)"],
             [["AUM FY26 / share", "₹10,352 cr / 51.4%", "₹5,570 cr / 27.6%", "₹3,792 cr / 18.8%", "≈ ₹48 cr on book / 0.4%"],
              ["Average ticket", "₹2.7 lakh", "₹72.4 lakh", "₹16.1 lakh", "n.a."],
              ["Origination yield (FY26)", "n.a. (portfolio yield 16.7% overall)", "12.0%", "15.1%", "n.a."],
              ["Typical tenor", "≤ 12 months (bullet / EMI)", "Long (multi-year EMI)", "Long (multi-year EMI)", "Short (1–3 years)"],
              ["Collateral / cover", "Gold jewellery; LTV 60.9%", "Property; 82.2% of mortgage AUM self-occupied", "Property; mostly self-occupied residential", "None"],
              ["Bureau profile (% AUM CIBIL >700)", "Collateral-led; not disclosed", "81%", "68% (9% new-to-credit)", "95%"],
              ["Main risk", "Gold price; custody/fraud", "Yield pressure; attrition", "Collections; early delinquency", "Default; write-off"],
              ["Capital treatment", "Low risk weight; co-lending eligible", "Priority-sector for MSME; DA/co-lending eligible", "Priority-sector / affordable housing", "100% risk weight"],
              ["Role FY26", "Growth and liquidity engine", "Stability and duration", "Yield and inclusion; rebuilt", "Eliminated"]],
             widths=[1.45, 1.5, 1.4, 1.45, 1.25], font=7.5, source=f"{AR26}, product pages, MD&CEO statement, MD&A portfolio-quality section, note 48; {AR24} MD&A for gold LTV history.")
    pg.h2("Portfolio quality by stage and security")
    pg.table(["Note 8 disclosure (₹ crore)", "31 Mar 2025", "31 Mar 2026", "Change"],
             [["Gross loans (amortised cost + FVOCI)", cr(L25['gross'], 0), cr(L26['gross'], 0), pct(L26['gross'], L25['gross'])],
              ["– secured by tangible assets", cr(L25['secured'], 0), cr(L26['secured'], 0), pct(L26['secured'], L25['secured'])],
              ["– unsecured", cr(L25['unsecured'], 0), cr(L26['unsecured'], 0), pct(L26['unsecured'], L25['unsecured'])],
              ["Secured share of gross loans (derived)", f"{L25['secured']/L25['gross']*100:.1f}%", f"{L26['secured']/L26['gross']*100:.1f}%", ""],
              ["Loans against gold jewellery (gross)", cr(L25['gold_gross'], 0), cr(L26['gold_gross'], 0), pct(L26['gold_gross'], L25['gold_gross'])],
              ["ECL allowance", cr(L25['ecl'], 0), cr(L26['ecl'], 0), pct(L26['ecl'], L25['ecl'])],
              ["ECL as % of gross loans (derived)", f"{L25['ecl']/L25['gross']*100:.2f}%", f"{L26['ecl']/L26['gross']*100:.2f}%", ""]],
             widths=[3.2, 1.2, 1.2, 1.45], font=8, source=f"{AR26}, note 8 – Loans.")
    pg.p("The on-book data corroborate the product narrative: unsecured loans fell 96%, gold loans rose 67% on the balance sheet, the secured share of gross loans rose from 89.6% to 99.5%, and the ECL allowance fell slightly in absolute terms even as the book grew 23% – the arithmetic of a safer mix. Chapter 5 quantifies the profitability consequences.")
    P.append(pg)

    # ================================================================== CHAPTER 5 FINANCIALS
    pg = Page("Chapter 5 — Financial Analysis: Framework")
    pg.p("Analysing a lender requires a different toolkit from analysing a manufacturer. This chapter uses the following framework, applied to five years of data (FY22–FY26) with the longer eight-year series where available.")
    pg.table(["Dimension", "Metrics used", "Why it matters for an NBFC", "Fedfina FY26"],
             [["Scale and growth", "AUM, on-book loans, disbursements, branches, growth rates and CAGR", "Growth is the main driver of future NII; must be read with mix and vintage", "AUM ₹20,153 cr (+27.5%); disbursements ₹31,410 cr (+67%)"],
              ["Margin", "Yield on advances, cost of borrowings, spread, NIM", "Spread × earning assets = NII, the core of revenue", "Yield 16.7%; CoB 8.1%; spread 8.6%; NIM 8.8%"],
              ["Efficiency", "Cost-to-income ratio, opex to average assets, AUM per employee/branch", "Branch-led models carry fixed costs; operating leverage appears as branches mature", "C/I 57.2%; AUM/employee ₹3.8 cr; gold AUM/branch ₹16.5 cr"],
              ["Asset quality", "GNPA, NNPA, PCR, stage-wise loans, credit cost, write-offs, ARC sales", "Credit losses are the largest swing factor in lender profits", "GNPA 1.9%; NNPA 1.3%; PCR 32.3%; credit cost 0.8%"],
              ["Profitability", "PPOP, PBT, PAT, RoA, RoE, EPS, DuPont decomposition", "Return on assets × leverage = return on equity", "PAT ₹343.6 cr; RoA 2.44%; RoE 12.62%; EPS ₹9.20"],
              ["Capital and leverage", "CRAR (Tier I/II), debt-equity, net worth, book value", "Regulatory floor 15%; leverage amplifies both return and risk", "CRAR 22.4% (Tier I 17.5%); D/E 4.6x; BVPS ₹78.19"],
              ["Funding and liquidity", "Borrowing mix, lender count, fixed/floating, ALM buckets, cash", "NBFCs cannot take deposits; refinancing risk is existential", "41 lenders; ECB 17%; fixed 40%; cash ₹1,340 cr"],
              ["Earnings quality", "Share of DA income, fee income, fair-value gains, OCI", "Front-loaded or non-recurring income overstates sustainable earnings", "DA income 1.6% of PBT (company basis)"]],
             widths=[1.15, 2.0, 2.2, 1.7], font=8)
    pg.h2("Conventions used in this chapter")
    pg.bullets([
        "Units: statutory tables are shown in ₹ lakh where reproduced from the annual report and converted to ₹ crore (÷100) in analytical tables; the header states the unit.",
        "Averages: where this report derives a ratio on average balances it uses the simple average of opening and closing balance-sheet figures; the company’s own methodology (daily or monthly averages) can differ slightly – e.g., reported RoA 2.44% versus 2.28% on a two-point average.",
        "Reported versus derived: company-reported ratios are shown as reported; computed figures are labelled ‘derived’ with the formula in Appendix F.",
        "Basis changes: yield, cost of borrowings and spread for FY22–FY25 are taken from the FY26 report’s restated series; the earlier-basis figures are shown in Table T8 for comparison.",
    ])
    pg.p("The chapter proceeds from the two-year snapshot (FY25 vs FY26) to five-year trends in growth, profitability, margins and risk, then to a line-by-line reading of the FY26 income statement, expense structure, balance sheet, funding, capital and asset quality, and ends with DuPont analysis and per-share/valuation metrics.")
    pg.p("Ratios that are deliberately not used. The company’s own key-ratio table marks debtors turnover, inventory turnover, operating margin and interest-coverage ratio as ‘not applicable’, because a lender’s inventory is its loan book and interest is its principal cost of goods. For the same reason current ratio and working-capital measures are replaced here by the structural-liquidity (ALM) buckets, and debt-equity is read alongside the regulatory capital ratio rather than against manufacturing norms. Where a ratio can be computed in more than one way – notably RoA, where the company uses average total assets and this report also shows a simple two-point average – both values are given with the formula so that the reader can reconcile them.")
    P.append(pg)

    # ------------------------------------------------------------------ 48 FY25 vs FY26 snapshot
    pg = Page("Financial Snapshot: FY 2024-25 versus FY 2025-26")
    pg.p("The Directors’ Report presents a standard table of financial highlights each year. The FY26 and FY25 figures are reproduced below in ₹ lakh exactly as disclosed, with growth rates derived.")
    pg.table(["Particulars (₹ lakh unless stated)", "FY 2025-26", "FY 2024-25", "Change"],
             [["Total revenue", f"{F26['rev']:,}", f"{F25['rev']:,}", pct(F26['rev'], F25['rev'])],
              ["Net interest income", f"{F26['nii']:,}", f"{F25['nii']:,}", pct(F26['nii'], F25['nii'])],
              ["Fee and other income", f"{F26['fee']:,}", f"{F25['fee']:,}", pct(F26['fee'], F25['fee'])],
              ["Operating expenses and provisions", f"{F26['opex_prov']:,}", f"{F25['opex_prov']:,}", pct(F26['opex_prov'], F25['opex_prov'])],
              ["Profit before tax", f"{F26['pbt']:,}", f"{F25['pbt']:,}", pct(F26['pbt'], F25['pbt'])],
              ["Profit after tax", f"{F26['pat']:,}", f"{F25['pat']:,}", pct(F26['pat'], F25['pat'])],
              ["Advances (net)", f"{F26['adv']:,}", f"{F25['adv']:,}", pct(F26['adv'], F25['adv'])],
              ["Borrowings", f"{F26['borr']:,}", f"{F25['borr']:,}", pct(F26['borr'], F25['borr'])],
              ["Total assets (balance-sheet size)", f"{F26['assets']:,}", f"{F25['assets']:,}", pct(F26['assets'], F25['assets'])],
              ["Net worth", f"{F26['nw']:,}", f"{F25['nw']:,}", pct(F26['nw'], F25['nw'])],
              ["Return on average assets (%)", f"{F26['roa']:.2f}", f"{F25['roa']:.2f}", f"{F26['roa']-F25['roa']:+.2f} pp"],
              ["Return on equity (%)", f"{F26['roe']:.2f}", f"{F25['roe']:.2f}", f"{F26['roe']-F25['roe']:+.2f} pp"],
              ["EPS – basic / diluted (₹)", f"{F26['eps']:.2f} / {F26['deps']:.2f}", f"{F25['eps']:.2f} / {F25['deps']:.2f}", pct(F26['eps'], F25['eps'])],
              ["Book value per share (₹)", f"{F26['bvps']:.2f}", f"{F25['bvps']:.2f}", pct(F26['bvps'], F25['bvps'])],
              ["Cost-to-income ratio (%)", f"{F26['ci']:.2f}", f"{F25['ci']:.2f}", f"{F26['ci']-F25['ci']:+.2f} pp"],
              ["Capital adequacy ratio (%)", f"{F26['crar']:.2f}", f"{F25['crar']:.2f}", f"{F26['crar']-F25['crar']:+.2f} pp"]],
             widths=[3.2, 1.3, 1.3, 1.25], font=8.5, source=f"{AR26}, Directors’ Report – Financial Highlights; growth rates derived.")
    pg.p(f"Three-year context (Directors’ Report FY24). FY24 revenue was ₹{F24['rev']:,} lakh, NII ₹{F24['nii']:,} lakh, PAT ₹{F24['pat']:,} lakh, net worth ₹{F24['nw']:,} lakh and total assets ₹{F24['assets']:,} lakh. Over the two years to FY26, therefore, revenue grew {(F26['rev']/F24['rev']-1)*100:.0f}%, NII {(F26['nii']/F24['nii']-1)*100:.0f}%, PAT {(F26['pat']/F24['pat']-1)*100:.0f}%, assets {(F26['assets']/F24['assets']-1)*100:.0f}% and net worth {(F26['nw']/F24['nw']-1)*100:.0f}% (all derived) – FY26 PAT is well above the FY24 level despite the FY25 dip.")
    pg.h2("Reading the snapshot")
    pg.p("Three features stand out. First, revenue grew only 7% while NII grew 15% and PAT 53%: the gap between revenue and NII reflects lower finance-cost growth (+3%) as borrowing costs fell, and the gap between NII and PAT reflects a ₹101 crore fall in impairment charges (₹216 crore → ₹115 crore). Second, the balance sheet grew faster than revenue (assets +27%, borrowings +31%) because more AUM was held on book and because gold loans – short-tenor and disbursed late in a fast-growing year – earn a full year of interest only in the following year. Third, every return and efficiency ratio improved except leverage: RoA, RoE, EPS, book value, cost-to-income and CRAR all moved in the right direction, while debt-equity rose from 4.0x to 4.6x. Fee and other income fell 24% as distribution income from Federal Bank products declined and FVOCI gains shrank; this is examined on the income-statement page.")
    P.append(pg)

    # ------------------------------------------------------------------ 49 AUM / disbursement trend
    pg = Page("Five-Year Trend: AUM, Loan Book and Disbursements")
    pg.fig(f"{C}/aum.png", "Figure 1 – AUM FY19–FY26 (₹ crore). Sources: " + AR24 + " KPI pages (FY19–FY24); " + AR25 + " (FY25); " + AR26 + " (FY26).", 2.4)
    rows = []
    for y in YEARS8:
        prev = YEARS8[YEARS8.index(y) - 1] if y != "FY19" else None
        rows.append([y, f"{AUM_MN[y]/10:,.0f}", (pct(AUM_MN[y], AUM_MN[prev]) if prev else "–"), f"{BRANCHES[y]}", f"{AUM_MN[y]/10/BRANCHES[y]:.1f}"])
    pg.table(["Year", "AUM (₹ crore)", "YoY growth (derived)", "Branches", "AUM per branch (₹ cr, derived)"], rows,
             widths=[0.8, 1.4, 1.6, 1.2, 2.05], font=8, source="AUM and branch counts from the annual reports’ KPI pages; growth and per-branch figures derived.")
    pg.table(["Growth measure (derived)", "Value", "Growth measure (derived)", "Value"],
             [["AUM CAGR FY19–FY26 (7 yrs)", f"{cagr(AUM_MN['FY19'], AUM_MN['FY26'], 7):.1f}%", "AUM CAGR FY22–FY26 (4 yrs)", f"{cagr(AUM_MN['FY22'], AUM_MN['FY26'], 4):.1f}%"],
              ["Net advances CAGR FY23–FY26 (3 yrs)", f"{cagr(F23['adv'], F26['adv'], 3):.1f}%", "Total disbursements FY24 → FY26", f"₹{TOTAL_DISB_LAKH['FY24']/100:,.0f} cr → ₹{TOTAL_DISB_LAKH['FY26']/100:,.0f} cr ({cagr(TOTAL_DISB_LAKH['FY24'], TOTAL_DISB_LAKH['FY26'], 2):.0f}% CAGR)"],
              ["Gold disbursement CAGR FY22–FY26", f"{cagr(DISB_GOLD['FY22'], DISB_GOLD['FY26'], 4):.0f}%", "Mortgage AUM FY24 → FY26", f"₹6,218 cr → ₹9,362 cr ({cagr(6218, 9362, 2):.1f}% CAGR)"]],
             widths=[2.2, 1.3, 2.2, 1.35], font=8)
    pg.p(f"Interpretation. AUM growth has been fast but uneven: a 32% jump in FY22 and 29% in FY24 bracket a slower FY25 (+30% headline, but with the unsecured book being run down) and a 27.5% FY26 in which the mix changed radically. AUM per branch has risen from ₹{AUM_MN['FY19']/10/BRANCHES['FY19']:.1f} crore in FY19 to ₹{AUM_MN['FY26']/10/BRANCHES['FY26']:.1f} crore in FY26 even as the network grew five-fold, which indicates that expansion has not diluted productivity. On-book net advances (₹14,319 crore) grew 23% in FY26, slightly below AUM, while gross loans rose 22.5%; the difference between AUM and on-book growth reflects co-lending. The FY26 disbursement figure of ₹31,410 crore (2.3x FY24) is inflated relative to AUM by the short tenor of gold loans – the same rupee of gold-loan capital turns over more than once a year – so AUM, not disbursements, is the better measure of scale.")
    P.append(pg)

    # ------------------------------------------------------------------ 50 Profitability trend
    pg = Page("Five-Year Trend: Profitability")
    pg.fig(f"{C}/pat.png", "Figure 2 – Profit after tax FY19–FY26 (₹ crore). Sources: annual reports FY24, FY25, FY26 (KPI pages and Directors’ Reports).", 2.3)
    pg.table(["₹ lakh", "FY23", "FY24", "FY25", "FY26", "CAGR FY23–26 (derived)"],
             [["Total revenue", f"{F23['rev']:,}", f"{F24['rev']:,}", f"{F25['rev']:,}", f"{F26['rev']:,}", f"{cagr(F23['rev'], F26['rev'], 3):.1f}%"],
              ["Net interest income", f"{F23['nii']:,}", f"{F24['nii']:,}", f"{F25['nii']:,}", f"{F26['nii']:,}", f"{cagr(F23['nii'], F26['nii'], 3):.1f}%"],
              ["Fee and other income", f"{F23['fee']:,}", f"{F24['fee']:,}", f"{F25['fee']:,}", f"{F26['fee']:,}", f"{cagr(F23['fee'], F26['fee'], 3):.1f}%"],
              ["Operating expenses and provisions", f"{F23['opex_prov']:,}", f"{F24['opex_prov']:,}", f"{F25['opex_prov']:,}", f"{F26['opex_prov']:,}", f"{cagr(F23['opex_prov'], F26['opex_prov'], 3):.1f}%"],
              ["Profit before tax", f"{F23['pbt']:,}", f"{F24['pbt']:,}", f"{F25['pbt']:,}", f"{F26['pbt']:,}", f"{cagr(F23['pbt'], F26['pbt'], 3):.1f}%"],
              ["Profit after tax", f"{F23['pat']:,}", f"{F24['pat']:,}", f"{F25['pat']:,}", f"{F26['pat']:,}", f"{cagr(F23['pat'], F26['pat'], 3):.1f}%"],
              ["PAT margin on total revenue (derived)", f"{F23['pat']/F23['rev']*100:.1f}%", f"{F24['pat']/F24['rev']*100:.1f}%", f"{F25['pat']/F25['rev']*100:.1f}%", f"{F26['pat']/F26['rev']*100:.1f}%", ""],
              ["Effective tax rate (derived)", f"{(1-F23['pat']/F23['pbt'])*100:.1f}%", f"{(1-F24['pat']/F24['pbt'])*100:.1f}%", f"{(1-F25['pat']/F25['pbt'])*100:.1f}%", f"{(1-F26['pat']/F26['pbt'])*100:.1f}%", ""],
              ["Basic EPS (₹)", f"{F23['eps']:.2f}", f"{F24['eps']:.2f}", f"{F25['eps']:.2f}", f"{F26['eps']:.2f}", f"{cagr(F23['eps'], F26['eps'], 3):.1f}%"]],
             widths=[2.3, 0.9, 0.9, 0.9, 0.9, 1.15], font=8, source="Directors’ Reports FY24 (FY23 and FY24 columns), FY25 and FY26 – Financial Highlights.")
    pg.p(f"Eight-year view. PAT grew from ₹{PAT_MN['FY19']/10:.0f} crore in FY19 to ₹{PAT_MN['FY26']/10:.1f} crore in FY26 – a {cagr(PAT_MN['FY19'], PAT_MN['FY26'], 7):.1f}% CAGR (derived) – with two interruptions: FY20 (₹{PAT_MN['FY20']/10:.0f} crore, pandemic-year provisioning) and FY25 (₹{PAT_MN['FY25']/10:.1f} crore, −8%, the ST LAP reset). Over FY22–FY26 the CAGR was {cagr(PAT_MN['FY22'], PAT_MN['FY26'], 4):.1f}%, broadly matching AUM growth of {cagr(AUM_MN['FY22'], AUM_MN['FY26'], 4):.1f}% – evidence that growth has, over the cycle, been converted into profit at a constant rate rather than bought with margin.")
    pg.p("Composition of FY26 profit growth (derived from the Directors’ Report table). NII rose ₹159 crore and fee/other income fell ₹38 crore, so total operating income rose ₹121 crore (+9.9%); operating expenses and provisions fell ₹36 crore because the ₹101 crore drop in impairment more than offset ₹65 crore of higher operating costs; PBT therefore rose ₹157 crore (+52%) and, with a stable 25.5% tax rate, PAT rose ₹118 crore (+53%). Put differently, roughly two-thirds of the FY26 profit improvement came from lower credit cost and one-third from NII growth net of cost growth – an important input to the hypothesis test in Chapter 8. EPS growth (+52%) matched PAT growth because the share count rose only 0.4% through ESOPs.")
    P.append(pg)

    # ------------------------------------------------------------------ 51 Margin trend
    pg = Page("Five-Year Trend: Yield, Cost of Borrowings and Spread")
    pg.fig(f"{C}/margins.png", "Figure 5 – Yield on advances, cost of borrowings and spread, FY22–FY26, on the FY26 report basis. Source: " + AR26 + ", five-year KPI charts.", 2.4)
    rows = []
    for y in YEARS5:
        rows.append([y, f"{YIELD_26[y]:.1f}", f"{COB_26[y]:.1f}", f"{SPREAD_26[y]:.1f}", f"{YIELD_OLD.get(y, float('nan')):.1f}" if y in YIELD_OLD else "–", f"{COB_OLD.get(y, float('nan')):.1f}" if y in COB_OLD else "–", f"{SPREAD_OLD.get(y, float('nan')):.1f}" if y in SPREAD_OLD else "–", f"{COST_INCOME[y]:.1f}"])
    pg.table(["Year", "Yield % (FY26 basis)", "CoB % (FY26 basis)", "Spread % (FY26 basis)", "Yield % (earlier basis)", "CoB % (earlier basis)", "Spread % (earlier basis)", "Cost-to-income %"],
             rows, widths=[0.6, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.8], font=8,
             source=f"FY26 basis: {AR26} KPI charts. Earlier basis: {AR24} and {AR25} KPI charts (FY25 earlier-basis yield 17.4%, CoB 9.2%). Cost-to-income: Directors’ Reports.")
    pg.p("What the series shows. On the FY26 basis, yield rose from 16.0% (FY22) to a peak of 17.1% in FY25 – when the high-yield unsecured and small-ticket books were largest – and eased to 16.7% in FY26 as gold loans (lower yield than unsecured business loans but higher than MT LAP) became half the book. Cost of borrowings rose 120 bps between FY22 and FY25 (7.8% → 9.0%) because of the repo-rate tightening cycle and the November 2023 increase in risk weights on bank lending to NBFCs (the FY25 letter attributes about 40 bps of the increase to this), and fell 90 bps to 8.1% in FY26 as the RBI cut rates by 125 bps and the company diversified into ECBs and CP. The quarterly picture is sharper still: daily-average cost of borrowing fell from 8.72% in Q4 FY25 to 7.83% in Q4 FY26.")
    pg.p("Spread – the difference between yield and cost of borrowings – was remarkably stable at 8.1–8.3% for four years and widened to 8.6% in FY26, the best in the series. Net interest margin, which the company reports on average assets, was 8.8% in FY26. The widening spread is the first of the three margin levers behind FY26 profit growth; the other two (operating leverage and credit cost) are examined on the following pages.")
    pg.p("Basis note. The FY26 report restates earlier years: FY24 yield is shown as 16.7% versus 16.2% in the FY24 report and FY25 yield as 17.1% versus 17.4% in the FY25 report, with corresponding differences in cost of borrowings. The restated series is internally consistent and is used in this report; the earlier figures are reproduced for transparency. The direction of every trend is the same on both bases.")
    P.append(pg)

    # ------------------------------------------------------------------ 52 Risk & capital trend
    pg = Page("Five-Year Trend: Asset Quality, Capital and Returns")
    pg.fig(f"{C}/npa.png", "Figure 6 – GNPA, NNPA and provision coverage, FY22–FY26. Sources: annual reports FY24–FY26 KPI charts; FY26 GNPA per Key Highlights (1.9%); the FY26 five-year chart shows 2.2% – see note.", 2.4, width=5.0)
    pg.table(["Year", "GNPA %", "NNPA %", "PCR %", "CRAR %", "RoA %", "RoE %", "BVPS ₹", "Credit cost % (avg assets)"],
             [[y, f"{GNPA[y]:.1f}", f"{NNPA[y]:.1f}", f"{PCR[y]:.1f}", f"{CRAR[y]:.1f}", f"{ROA[y]:.1f}", f"{ROE[y]:.1f}", f"{BVPS[y]:.1f}",
               {"FY22": "n.a.", "FY23": "n.a.", "FY24": "0.7", "FY25": "1.8", "FY26": "0.8"}[y]] for y in YEARS5],
             widths=[0.6, 0.7, 0.7, 0.7, 0.75, 0.7, 0.7, 0.8, 1.4], font=8.5,
             source=f"{AR24}, {AR25}, {AR26} – KPI charts and Directors’ Reports; credit cost from Key Highlights FY24–FY26.")
    pg.table(["Eight-year series", "FY19", "FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"],
             [["GNPA %"] + [f"{GNPA[y]:.1f}" for y in YEARS8], ["NNPA %"] + [f"{NNPA[y]:.1f}" for y in YEARS8],
              ["CRAR %"] + [f"{CRAR[y]:.1f}" for y in YEARS8], ["RoA %"] + [f"{ROA[y]:.1f}" for y in YEARS8],
              ["RoE %"] + [f"{ROE[y]:.1f}" for y in YEARS8], ["Book value / share ₹"] + [f"{BVPS[y]:.1f}" for y in YEARS8],
              ["Cost-to-income %"] + [f"{COST_INCOME[y]:.1f}" for y in YEARS8]],
             widths=[1.6, 0.68, 0.68, 0.68, 0.68, 0.68, 0.68, 0.68, 0.69], font=8, source=f"{AR24} KPI pages (FY19–FY24), {AR25} and {AR26} (FY25–FY26). Table T8.")
    pg.p("Asset quality has moved in a narrow band. GNPA has stayed between 1.0% and 2.3% for eight years and NNPA between 0.7% and 1.9%; the FY22 peak reflected the pandemic and the FY25 uptick the ST LAP stress. Provision coverage doubled from 20.4% to 40.0% in FY25 as the company built provisions ahead of the clean-up, then fell to 32.3% in FY26 after write-offs and ARC sales consumed part of the stock – a normal sequence. Note that the FY26 report’s five-year chart shows FY26 GNPA of 2.2% while the Key Highlights and MD&A show 1.9%; the difference likely reflects the inclusion or exclusion of FVOCI (held-for-sale) loans or the timing of ARC sales, and both figures are disclosed here.")
    pg.p("Capital has been maintained comfortably above the 15% floor throughout, replenished by the 2018 True North investment (FY21: 23.5%), the IPO (FY24: 23.5%) and FY26 Tier II issuance (22.4%). Returns follow the credit cycle: RoA of 2.3–2.4% and RoE of 13–14% in the good years (FY23, FY24, FY26) versus 1.8% and 9.4% in the FY25 reset year. Book value per share has compounded at 21.6% a year since FY19 (derived) without any dividend.")
    P.append(pg)

    # ------------------------------------------------------------------ 53 Income statement
    pg = Page("Income Statement Analysis FY 2025-26")
    rows = [
        ["Interest income", P26['int_income'], P25['int_income']], ["Fee and commission income", P26['fee_comm'], P25['fee_comm']],
        ["Net gain on fair value changes", P26['fv_gain'], P25['fv_gain']], ["Revenue from operations", P26['rev_ops'], P25['rev_ops']],
        ["Other income", P26['other_inc'], P25['other_inc']], ["Total revenue", P26['total_rev'], P25['total_rev']],
        ["Finance costs", P26['fin_cost'], P25['fin_cost']], ["Fee and commission expense", P26['fee_exp'], P25['fee_exp']],
        ["Impairment on financial instruments", P26['impairment'], P25['impairment']], ["Employee benefits expense", P26['emp'], P25['emp']],
        ["Depreciation and amortisation", P26['dep'], P25['dep']], ["Other expenses", P26['other_exp'], P25['other_exp']],
        ["Total expenses", P26['total_exp'], P25['total_exp']], ["Profit before tax", P26['pbt'], P25['pbt']],
        ["Current tax", P26['cur_tax'], P25['cur_tax']], ["Deferred tax", P26['def_tax'], P25['def_tax']],
        ["Profit after tax", P26['pat'], P25['pat']], ["Other comprehensive income (net)", P26['oci'], P25['oci']],
        ["Total comprehensive income", P26['tci'], P25['tci']]]
    tbl = []
    for name, a, b in rows:
        chg = pct(a, b) if b not in (0,) and a * b > 0 else "n.m."
        tbl.append([name, f"{a:,}", f"{b:,}", chg, f"{a/P26['total_rev']*100:.1f}%", f"{b/P25['total_rev']*100:.1f}%"])
    pg.table(["Statement of profit and loss (₹ lakh)", "FY26", "FY25", "Change", "% of revenue FY26", "% of revenue FY25"], tbl,
             widths=[2.6, 0.95, 0.95, 0.8, 0.9, 0.85], font=8, source=f"{AR26}, Statement of Profit and Loss; common-size percentages derived.")
    pg.table(["Interest income by source (note 26, ₹ lakh)", "FY26", "FY25", "Change"],
             [[k, f"{v[0]:,}", f"{v[1]:,}", pct(v[0], v[1])] for k, v in INT_INCOME_BREAKUP.items()] +
             [["Total interest income", f"{P26['int_income']:,}", f"{P25['int_income']:,}", pct(P26['int_income'], P25['int_income'])]],
             widths=[3.2, 1.3, 1.3, 1.25], font=8, source=f"{AR26}, note 26.")
    pg.p("Interpretation. Interest on loans – the core, recurring revenue – grew 13.4% to ₹1,968 crore and rose to 93.3% of interest income (FY25: 90.2%), while income on direct assignment fell 33% and fee/commission income fell 13% (distribution income from Federal Bank products ₹40.8 crore vs ₹59.2 crore). Finance costs grew just 3% on a 31% larger borrowing base, confirming the fall in cost of funds. The impairment line – ₹115 crore against ₹216 crore – is the single largest contributor to the profit recovery. Employee costs rose 13.7% and other expenses 9.9%, both slower than AUM growth. The effective tax rate was 25.5% (derived). Other comprehensive income of ₹15 crore mainly reflects fair-value movements on FVOCI loans and cash-flow hedges on the ECB programme.")
    P.append(pg)

    # ------------------------------------------------------------------ 54 Expense structure
    pg = Page("Expense Structure and Operating Efficiency")
    pg.fig(f"{C}/costs.png", "Figure 14 – Expense structure FY25 vs FY26 (₹ crore). Source: " + AR26 + ", Statement of Profit and Loss.", 2.3, width=5.2)
    opex26 = P26['emp'] + P26['dep'] + P26['other_exp']; opex25 = P25['emp'] + P25['dep'] + P25['other_exp']
    inc26 = F26['nii'] + F26['fee']; inc25 = F25['nii'] + F25['fee']
    avg26 = (B26['total_assets'] + B25['total_assets']) / 2
    pg.table(["Efficiency measure", "FY25", "FY26", "Formula / source"],
             [["Operating expenses (₹ crore)", cr(opex25, 1), cr(opex26, 1), "Employee + depreciation + other expenses (P&L)"],
              ["Net operating income (₹ crore)", cr(inc25, 1), cr(inc26, 1), "NII + fee and other income (Directors’ Report)"],
              ["Cost-to-income ratio – reported", f"{F25['ci']:.2f}%", f"{F26['ci']:.2f}%", "Directors’ Report"],
              ["Cost-to-income ratio – derived", f"{opex25/inc25*100:.1f}%", f"{opex26/inc26*100:.1f}%", "Opex ÷ net operating income (reconciles to reported)"],
              ["Pre-provision operating profit (₹ crore, derived)", cr(inc25 - opex25, 1), cr(inc26 - opex26, 1), "Net operating income − opex; FY25 PPOP ₹520 cr (+32%) per FY25 report"],
              ["Opex to average total assets (derived)", f"{opex25/((B25['total_assets']+F24['assets'])/2)*100:.2f}%", f"{opex26/avg26*100:.2f}%", "Opex ÷ average of opening and closing total assets"],
              ["AUM per employee (₹ crore)", f"{AUM_MN['FY25']/10/EMPLOYEES['FY25']:.1f}", f"{KPI26['aum_per_emp']}", "Reported FY26; FY25 derived"],
              ["Credit cost on average assets", "1.8%", "0.8%", "Reported; FY26 derived = ₹115 cr ÷ ₹15,062 cr = 0.77%"]],
             widths=[2.6, 0.9, 0.9, 2.65], font=8)
    pg.table(["Largest ‘other expenses’ (note 34, ₹ lakh)", "FY26", "FY25", "Change", "Largest ‘other expenses’ (note 34, ₹ lakh)", "FY26", "FY25", "Change"],
             [[k1, f"{v1[0]:,}", f"{v1[1]:,}", pct(v1[0], v1[1], 0), k2, f"{v2[0]:,}", f"{v2[1]:,}", pct(v2[0], v2[1], 0)]
              for (k1, v1), (k2, v2) in zip(list(OTHER_EXP_TOP.items())[:5], list(OTHER_EXP_TOP.items())[5:10])],
             widths=[1.75, 0.6, 0.6, 0.6, 1.75, 0.6, 0.6, 0.55], font=7.5, source=f"{AR26}, note 34 – Other expenses.")
    pg.p("Interpretation. The cost-to-income ratio has improved only gradually (58.6% → 57.2% over four years) because the company has kept adding branches and people: 148 branches and 735 employees in FY26 alone. Within other expenses, the fastest-growing lines are those tied to the new strategy – sourcing expenses (+105%, in-house origination), securitisation expenses (+74%) and insurance (+160%, larger gold holdings) – while collection-agency commission fell 7% as collections moved in-house and rent fell as branches moved to long-term leases (captured in depreciation of right-of-use assets, +11.5%). Operating leverage should emerge as the FY26 branch cohort matures; the MD&CEO expects these branches to “contribute significantly to AUM without proportionate cost addition”.")
    P.append(pg)

    # ------------------------------------------------------------------ 55 Balance sheet
    pg = Page("Balance Sheet Analysis")
    def row(name, k):
        return [name, f"{B26[k]:,}", f"{B25[k]:,}", pct(B26[k], B25[k]) if B25[k] else "n.m.", f"{B26[k]/B26['total_assets']*100:.1f}%", f"{B25[k]/B25['total_assets']*100:.1f}%"]
    pg.table(["Balance sheet (₹ lakh)", "31 Mar 2026", "31 Mar 2025", "Change", "% of total FY26", "% of total FY25"],
             [row("Cash and cash equivalents", "cash"), row("Bank balances other than cash", "bank_bal"), row("Derivative financial instruments", "deriv"),
              row("Receivables (trade and other)", "trade_rec"), row("Loans (net)", "loans"), row("Investments", "inv"), row("Other financial assets", "other_fin"),
              row("Total financial assets", "total_fin"), row("Property, plant and equipment", "ppe"), row("Right-of-use assets", "rou"),
              row("Other non-financial assets (incl. tax)", "other_nonfin"), row("Total non-financial assets", "total_nonfin"), row("TOTAL ASSETS", "total_assets"),
              row("Debt securities (NCDs, CP)", "debt_sec"), row("Borrowings other than debt securities", "borr"), row("Subordinated liabilities", "subdebt"),
              row("Lease liabilities", "lease"), row("Other financial liabilities (incl. payables)", "other_fin_l"), row("Total financial liabilities", "total_fin_l"),
              row("Non-financial liabilities", "total_nonfin_l"), row("Equity share capital", "share_cap"), row("Other equity", "other_eq"), row("TOTAL EQUITY", "equity")],
             widths=[2.6, 0.95, 0.95, 0.8, 0.9, 0.85], font=7.5, source=f"{AR26}, Balance Sheet; common-size percentages derived. Receivables line combines trade and other receivables; other non-financial assets include current tax and deferred tax assets.")
    pg.p(f"Interpretation. The balance sheet grew 27.4% to ₹16,875 crore. Loans are {B26['loans']/B26['total_assets']*100:.1f}% of assets (FY25: {B25['loans']/B25['total_assets']*100:.1f}%); the slight fall reflects an 85% increase in cash and cash equivalents to ₹1,340 crore, as the company carried more liquidity at year-end after the March 2026 NCD and ECB draw-downs. Derivative assets of ₹215 crore are the mark-to-market of cross-currency swaps hedging the ECB programme (notional ₹2,446 crore) – they are matched by the rupee value of the hedged borrowings, not a speculative position. On the liability side, borrowings of all types were {(B26['debt_sec']+B26['borr']+B26['subdebt'])/B26['total_assets']*100:.1f}% of total assets and equity {B26['equity']/B26['total_assets']*100:.1f}% (FY25: {B25['equity']/B25['total_assets']*100:.1f}%) – the arithmetic of rising leverage. Debt securities more than tripled (CP ₹1,164 crore and new NCDs) and subordinated liabilities nearly doubled with the ₹450 crore Tier II issue. Right-of-use assets (₹174 crore) and lease liabilities (₹191 crore) reflect the leased branch network. The equity base of ₹2,926 crore comprises ₹374 crore of share capital and ₹2,552 crore of reserves; no goodwill or intangible of significance exists, so book value is tangible book value.")
    P.append(pg)

    # ------------------------------------------------------------------ 56 Funding profile
    pg = Page("Funding Profile and Liability Management")
    pg.fig(f"{C}/borrow.png", "Figure 8 – Borrowings by instrument, 31 March 2026. Source: " + AR26 + ", notes 16, 17 and 18 (carrying amounts).", 2.4, width=5.6)
    tot26 = sum(v[0] for v in BORROW.values()); tot25 = sum(v[1] for v in BORROW.values())
    pg.table(["Borrowing instrument (₹ lakh)", "31 Mar 2026", "Share", "31 Mar 2025", "Share", "Change"],
             [[k, f"{v[0]:,}", f"{v[0]/tot26*100:.1f}%", f"{v[1]:,}", f"{v[1]/tot25*100:.1f}%", pct(v[0], v[1], 0)] for k, v in BORROW.items()] +
             [["Total borrowings", f"{tot26:,}", "100%", f"{tot25:,}", "100%", pct(tot26, tot25)]],
             widths=[2.8, 1.0, 0.65, 1.0, 0.65, 0.95], font=8, source=f"{AR26}, notes 16 (debt securities), 17 (borrowings other than debt securities) and 18 (subordinated liabilities). Totals reconcile to Directors’ Report borrowings of ₹13,48,413 lakh.")
    pg.bullets([
        "Diversification:: 41 lenders (FY25: 39) across public, private and foreign banks, financial institutions and capital markets; the company lists more than 30 bank relationships. Bank term loans remain the anchor at 50% (company basis), with ECBs 17%, NCDs/CP 13% and direct assignments 14% of the funding mix.",
        "ECB programme:: USD 250 million raised under the ECB route, fully hedged for the entire maturity through cross-currency swaps (notional ₹2,446 crore); FCNR borrowings of ₹62.5 crore. ECBs lengthen tenor and diversify the investor base.",
        "Commercial paper:: ₹1,164 crore outstanding (maximum ₹1,375 crore during the year; FY25 maximum ₹575 crore), all under one year – cheaper but adds rollover exposure.",
        "Related-party funding:: Federal Bank provided ₹1,370 crore (term loan ₹1,064 crore, demand loan ₹60 crore, subordinated NCDs ₹246 crore) – 10.2% of borrowings (derived); interest paid to the bank ₹84.8 crore.",
        "Rate structure and cost:: fixed-rate borrowings raised from about 10% to 40% of the book during FY26; finance costs ₹879 crore (+3%) on average borrowings of ₹11,876 crore (derived) ≈ 7.4% all-in; reported cost of borrowings 8.1% for the year, 7.83% in Q4 FY26.",
    ])
    P.append(pg)

    # ------------------------------------------------------------------ 57 Capital adequacy
    pg = Page("Capital Adequacy and Leverage")
    pg.fig(f"{C}/crar.png", "Figure 7 – Capital adequacy and book value per share, FY22–FY26. Sources: annual reports FY24–FY26 KPI charts and Directors’ Reports.", 2.3, width=5.2)
    c26, c25 = CRAR_DETAIL["FY26"], CRAR_DETAIL["FY25"]
    pg.table(["Capital measure", "31 Mar 2026", "31 Mar 2025", "Comment"],
             [["CRAR (%)", f"{c26[0]:.2f}", f"{c25[0]:.2f}", "RBI minimum for NBFC-ML: 15%"],
              ["Tier I capital ratio (%)", f"{c26[1]:.2f}", f"{c25[1]:.2f}", "Minimum Tier I 10%; fell 1.4 pp as risk-weighted assets grew faster than retained earnings"],
              ["Tier II capital ratio (%)", f"{c26[2]:.2f}", f"{c25[2]:.2f}", "Raised by ₹450 crore subordinated debt in March 2026"],
              ["Subordinated debt raised in year (₹ lakh)", f"{c26[3]:,}", f"{c25[3]:,}", "Note 48 capital disclosure"],
              ["Net worth (₹ lakh)", f"{F26['nw']:,}", f"{F25['nw']:,}", "+14.9%; retained earnings + ESOP allotments"],
              ["Borrowings (₹ lakh)", f"{F26['borr']:,}", f"{F25['borr']:,}", "+31.3%"],
              ["Debt-to-equity (x) – reported", "4.6", "4.0", "Investment case page / Key Highlights"],
              ["Debt-to-equity (x) – derived", f"{F26['borr']/F26['nw']:.2f}", f"{F25['borr']/F25['nw']:.2f}", "Borrowings ÷ net worth"],
              ["Equity to total assets (%) – derived", f"{F26['nw']/F26['assets']*100:.1f}", f"{F25['nw']/F25['assets']*100:.1f}", "Simple leverage measure"],
              ["Transfer to statutory reserve (₹ lakh)", "6,872", "4,504", "20% of PAT under Section 45-IC, RBI Act (FY25 derived)"]],
             widths=[2.5, 1.0, 1.0, 2.55], font=8, source=f"{AR26}, note 48 (capital), Directors’ Report; {AR25} Directors’ Report.")
    pg.p("Interpretation. Capital adequacy of 22.4% gives headroom of 7.4 percentage points over the regulatory floor, but the composition has shifted: Tier I fell from 18.9% to 17.5% while Tier II rose from 3.0% to 4.9%. Since Tier II is capped relative to Tier I and does not absorb losses on a going-concern basis, future growth at 20–25% will require Tier I accretion from profits (RoE 12.6% supports roughly 12–13% growth in equity with no dividend) or, eventually, fresh equity. The derived debt-equity of 4.61x is above the 4.0x of FY25 and well above the 3.6x of FY24; it remains moderate for a secured retail NBFC (sector leverage of 5–6x is common) but it is the metric that rating agencies and the Board will watch most closely. The lower risk weights on gold loans and the elimination of 100%-weighted unsecured loans help: risk-weighted assets grew more slowly than the balance sheet, which is why CRAR rose despite higher leverage.")
    P.append(pg)

    # ------------------------------------------------------------------ 58 Asset quality & ECL
    pg = Page("Asset Quality, Stage Analysis and Expected Credit Loss")
    pg.fig(f"{C}/stages.png", "Figure 11 – Stage classification of loans at amortised cost, 31 March 2025 vs 2026 (% of gross). Source: " + AR26 + ", note 8; percentages derived.", 2.2, width=5.0)
    I26, I25 = IMPAIRED["FY26"], IMPAIRED["FY25"]
    pg.table(["Stage-wise loans at amortised cost (₹ lakh)", "31 Mar 2026", "% of book", "31 Mar 2025", "% of book"],
             [["Stage 1 (performing)", f"{L26['s1']:,}", f"{L26['s1']/L26['amort']*100:.1f}%", f"{L25['s1']:,}", f"{L25['s1']/L25['amort']*100:.1f}%"],
              ["Stage 2 (significant increase in credit risk)", f"{L26['s2']:,}", f"{L26['s2']/L26['amort']*100:.1f}%", f"{L25['s2']:,}", f"{L25['s2']/L25['amort']*100:.1f}%"],
              ["Stage 3 (credit-impaired)", f"{L26['s3']:,}", f"{L26['s3']/L26['amort']*100:.1f}%", f"{L25['s3']:,}", f"{L25['s3']/L25['amort']*100:.1f}%"],
              ["Total at amortised cost", f"{L26['amort']:,}", "100%", f"{L25['amort']:,}", "100%"],
              ["Loans at FVOCI (held for sale)", f"{L26['fvoci']:,}", "", f"{L25['fvoci']:,}", ""]],
             widths=[3.0, 1.1, 0.9, 1.1, 0.95], font=8, source=f"{AR26}, note 8; percentages derived.")
    pg.table(["Movement of credit-impaired loans incl. FVOCI (note 48.09, ₹ lakh)", "FY26", "FY25"],
             [["Gross credit-impaired – opening", f"{I26['open']:,}", f"{I25['open']:,}"], ["Additions during the year", f"{I26['add']:,}", f"{I25['add']:,}"],
              ["Reductions (upgrades, recoveries, sales)", f"{I26['red']:,}", f"{I25['red']:,}"], ["Write-offs", f"{I26['wo']:,}", f"{I25['wo']:,}"],
              ["Gross credit-impaired – closing", f"{I26['close']:,}", f"{I25['close']:,}"], ["Net credit-impaired – closing", f"{I26['net_close']:,}", f"{I25['net_close']:,}"],
              ["Net credit-impaired ratio (%)", f"{I26['net_ratio']:.2f}", f"{I25['net_ratio']:.2f}"],
              ["NPA accounts sold to ARCs – number / principal", f"{NPA_SOLD['FY26'][0]} / {NPA_SOLD['FY26'][1]:,}", f"{NPA_SOLD['FY25'][0]} / {NPA_SOLD['FY25'][1]:,}"],
              ["Top-20 borrowers – exposure / % of advances", f"{TOP20['FY26'][0]:,} / {TOP20['FY26'][1]}%", f"{TOP20['FY25'][0]:,} / {TOP20['FY25'][1]}%"]],
             widths=[4.0, 1.5, 1.55], font=8, source=f"{AR26}, note 48 – RBI disclosures.")
    pg.p("Interpretation. On an Ind AS basis the improvement is unambiguous: Stage 2 loans fell from 5.1% to 1.9% of the amortised-cost book and Stage 3 from 2.3% to 1.6%, so the share of the book showing any stress fell from 7.4% to 3.5%. The movement table shows how: additions to credit-impaired loans rose 16% (₹227 crore – the old ST LAP and business-loan vintages continuing to slip) but write-offs rose thirteen-fold to ₹88 crore and 814 accounts with ₹105 crore principal were sold to ARCs, so the closing stock of impaired loans (₹272 crore, +14%) grew more slowly than the book (+23%). Impairment expense of ₹115 crore comprised ₹134 crore of bad debts net of recoveries offset by ₹19 crore of ECL releases; the ECL allowance ended at ₹187 crore, 1.29% of gross loans. The net credit-impaired ratio of 1.28% and NNPA of 1.3% reconcile. Concentration is negligible: the top 20 borrowers are 0.47% of advances and the four largest impaired accounts total ₹9.4 crore.")
    P.append(pg)

    # ------------------------------------------------------------------ 59 DuPont
    pg = Page("DuPont Analysis and Return Decomposition")
    pg.fig(f"{C}/roa_roe.png", "Figure 4 – Return on assets and return on equity, FY22–FY26. Source: annual reports FY24–FY26 KPI charts.", 2.3)
    avg_a26 = (F26['assets'] + F25['assets']) / 2; avg_a25 = (F25['assets'] + F24['assets']) / 2
    avg_e26 = (F26['nw'] + F25['nw']) / 2; avg_e25 = (F25['nw'] + F24['nw']) / 2
    def comp(P, F, avg_a, avg_e):
        return dict(ii=P['int_income'] / avg_a * 100, fc=P['fin_cost'] / avg_a * 100, nii=(P['int_income'] - P['fin_cost']) / avg_a * 100,
                    oth=(P['total_rev'] - P['int_income'] - P['fee_exp']) / avg_a * 100, opex=(P['emp'] + P['dep'] + P['other_exp']) / avg_a * 100,
                    cc=P['impairment'] / avg_a * 100, pbt=P['pbt'] / avg_a * 100, tax=(P['pbt'] - P['pat']) / avg_a * 100, roa=P['pat'] / avg_a * 100,
                    lev=avg_a / avg_e, roe=P['pat'] / avg_e * 100)
    d26 = comp(P26, F26, avg_a26, avg_e26); d25 = comp(P25, F25, avg_a25, avg_e25)
    pg.table(["Component (% of average total assets, derived)", "FY26", "FY25", "Change (pp)"],
             [["Interest income", f"{d26['ii']:.2f}", f"{d25['ii']:.2f}", f"{d26['ii']-d25['ii']:+.2f}"],
              ["Less: finance costs", f"{d26['fc']:.2f}", f"{d25['fc']:.2f}", f"{d26['fc']-d25['fc']:+.2f}"],
              ["= Net interest income (NIM on assets)", f"{d26['nii']:.2f}", f"{d25['nii']:.2f}", f"{d26['nii']-d25['nii']:+.2f}"],
              ["Add: fee, fair-value and other income (net of fee expense)", f"{d26['oth']:.2f}", f"{d25['oth']:.2f}", f"{d26['oth']-d25['oth']:+.2f}"],
              ["Less: operating expenses", f"{d26['opex']:.2f}", f"{d25['opex']:.2f}", f"{d26['opex']-d25['opex']:+.2f}"],
              ["Less: impairment (credit cost)", f"{d26['cc']:.2f}", f"{d25['cc']:.2f}", f"{d26['cc']-d25['cc']:+.2f}"],
              ["= Profit before tax", f"{d26['pbt']:.2f}", f"{d25['pbt']:.2f}", f"{d26['pbt']-d25['pbt']:+.2f}"],
              ["Less: tax", f"{d26['tax']:.2f}", f"{d25['tax']:.2f}", f"{d26['tax']-d25['tax']:+.2f}"],
              ["= Return on average assets (two-point average)", f"{d26['roa']:.2f}", f"{d25['roa']:.2f}", f"{d26['roa']-d25['roa']:+.2f}"],
              ["Reported RoA (company methodology)", f"{F26['roa']:.2f}", f"{F25['roa']:.2f}", f"{F26['roa']-F25['roa']:+.2f}"],
              ["× Leverage (average assets ÷ average equity)", f"{d26['lev']:.2f}x", f"{d25['lev']:.2f}x", f"{d26['lev']-d25['lev']:+.2f}"],
              ["= Return on average equity (derived)", f"{d26['roe']:.2f}", f"{d25['roe']:.2f}", f"{d26['roe']-d25['roe']:+.2f}"],
              ["Reported RoE", f"{F26['roe']:.2f}", f"{F25['roe']:.2f}", f"{F26['roe']-F25['roe']:+.2f}"]],
             widths=[3.6, 1.0, 1.0, 1.45], font=8, source="Derived from the Statement of Profit and Loss and Balance Sheets in " + AR26 + " and " + AR25 + "; averages are simple two-point averages, hence the small difference from reported RoA/RoE.")
    pg.p(f"Interpretation. The decomposition isolates the three levers of FY26: (1) the margin lever – NIM on assets widened by {d26['nii']-d25['nii']:+.2f} pp as finance costs fell faster than asset yields; (2) the credit lever – impairment fell {abs(d26['cc']-d25['cc']):.2f} pp of assets, the largest single contribution; and (3) the efficiency lever – operating expenses fell {abs(d26['opex']-d25['opex']):.2f} pp of assets as the balance sheet grew faster than costs. Against these, non-interest income fell {abs(d26['oth']-d25['oth']):.2f} pp (lower DA and distribution income). Leverage rose from {d25['lev']:.2f}x to {d26['lev']:.2f}x, so RoE improved by more than RoA. The reported RoE of 12.62% and derived 12.55% agree closely. A 2.3–2.4% RoA on 5.5x average leverage yields a 12–13% RoE; reaching the mid-teens RoE of FY23 (14.4%) requires either further credit-cost normalisation below 0.8%, operating leverage from branch maturity, or higher leverage – the last of which has its own limits.")
    P.append(pg)

    # ------------------------------------------------------------------ 60 Per share & valuation
    pg = Page("Per-Share Metrics, Market Capitalisation and Valuation Perspective")
    price = MCAP_CR * 1e7 / SHARES_OUT
    pg.p(f"Fedfina’s equity shares have traded on NSE and BSE since 30 November 2023. The FY26 annual report discloses a market capitalisation of ₹{MCAP_CR:,} crore at 31 March 2026, which with {SHARES_OUT:,} shares outstanding implies a closing price of about ₹{price:.0f} per share (derived). The IPO price in November 2023 was ₹140 per share, so the shares were below the issue price at the end of FY26 despite the recovery in earnings. The report does not reproduce monthly price data in text form, so no price-trend analysis is attempted here.")
    pg.table(["Per-share and valuation measure", "FY24", "FY25", "FY26", "Basis"],
             [["Shares outstanding (crore)", "37.0", f"{SHARES_OUT_PY/1e7:.2f}", f"{SHARES_OUT/1e7:.2f}", "Balance sheet / CG report"],
              ["Basic EPS (₹)", f"{F24['eps']:.2f}", f"{F25['eps']:.2f}", f"{F26['eps']:.2f}", "Directors’ Reports"],
              ["Diluted EPS (₹)", f"{F24['deps']:.2f}", f"{F25['deps']:.2f}", f"{F26['deps']:.2f}", "Directors’ Reports"],
              ["Book value per share (₹)", f"{F24['bvps']:.2f}", f"{F25['bvps']:.2f}", f"{F26['bvps']:.2f}", "Directors’ Reports"],
              ["Dividend per share (₹)", "Nil", "Nil", "Nil", "No dividend recommended"],
              ["Market capitalisation (₹ crore)", "n.a.", "n.a.", f"{MCAP_CR:,}", f"{AR26} inside cover"],
              ["Implied price per share (₹)", "–", "–", f"{price:.0f}", "Derived: mcap ÷ shares"],
              ["Price-to-book (x)", "–", "–", f"{price/F26['bvps']:.2f}", "Derived"],
              ["Price-to-earnings (x, basic)", "–", "–", f"{price/F26['eps']:.1f}", "Derived"],
              ["Earnings yield (%)", "–", "–", f"{F26['eps']/price*100:.1f}", "Derived"],
              ["Market cap to AUM (%)", "–", "–", f"{MCAP_CR/AUM_MN['FY26']*10*100:.1f}", "Derived"]],
             widths=[2.7, 1.0, 1.0, 1.0, 1.35], font=8.5)
    pg.h2("Valuation perspective (illustrative, not a recommendation)")
    pg.p(f"At roughly {price/F26['bvps']:.1f}x book and {price/F26['eps']:.0f}x FY26 earnings, the market was valuing Fedfina at a discount to the large gold-loan NBFCs and bank-backed lenders, which typically trade at higher multiples of book when RoE is in the high teens. The discount is consistent with an RoE of 12.6% (below the 15%+ that justifies a premium to book), the recent FY25 earnings reset, leverage rising to 4.6x, True North’s exit overhang during the year and the small free float. Factors that could narrow it include sustained sub-1% credit cost, RoE moving towards the Q4 FY26 run-rate of 14.0%, and evidence that the FY26 branch cohort is scaling. Conversely, a gold-price correction or renewed ST LAP slippage would widen it.")
    pg.p("Sensitivity (derived, illustrative). Each ₹10 crore of additional annual PAT adds about ₹0.27 to EPS; each 10 bps of credit cost on FY26 average assets is worth about ₹15 crore of PBT (₹11 crore of PAT, or ₹0.30 of EPS). Book value grows by roughly ₹9 per share a year at the FY26 earnings level with no dividend. These sensitivities show why the credit-cost line dominates the equity story.")
    pg.p("Caveat. All market-based figures use the single market-capitalisation disclosure in the annual report and are therefore dated; they are provided to complete the fundamental picture, not as a valuation opinion.")
    P.append(pg)

    return P
