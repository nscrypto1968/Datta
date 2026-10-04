"""
Data layer for the Fedfina Summer Internship Project report.

Every figure here is transcribed from the three annual reports supplied with the
assignment (FY 2023-24, FY 2024-25, FY 2025-26) unless explicitly marked
"derived" (computed from reported figures) or "web" (verified external source,
listed in the bibliography).  Nothing is estimated or assumed.

Units: ₹ lakh unless noted. 1 crore = 100 lakh. 1 million = 10 lakh.
"""

YEARS5 = ["FY22", "FY23", "FY24", "FY25", "FY26"]
YEARS8 = ["FY19", "FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]

# ---------------------------------------------------------------------------
# Five-year / eight-year highlight series (Corporate Overview "Financial
# Highlights" pages of AR FY24 p.20-23, AR FY25 p.18-21 and AR FY26 p.22-25).
# The FY26 report presents FY22-FY26; FY24 report presents FY19-FY24.
# Where the FY26 report re-states yield/spread/cost-of-borrowings on a revised
# basis, the FY26 series is used and the difference is noted in the text.
# ---------------------------------------------------------------------------
AUM_MN = {  # ₹ million
    "FY19": 20193, "FY20": 38382, "FY21": 48624, "FY22": 61872,
    "FY23": 90696, "FY24": 121919, "FY25": 158115, "FY26": 201530,
}
PAT_MN = {  # ₹ million
    "FY19": 361, "FY20": 391, "FY21": 617, "FY22": 1035,
    "FY23": 1801, "FY24": 2447, "FY25": 2252, "FY26": 3436,
}
ROA = {"FY19": 2.0, "FY20": 1.3, "FY21": 1.3, "FY22": 1.7, "FY23": 2.3, "FY24": 2.4, "FY25": 1.8, "FY26": 2.4}
ROE = {"FY19": 10.1, "FY20": 6.8, "FY21": 8.1, "FY22": 10.4, "FY23": 14.4, "FY24": 13.5, "FY25": 9.4, "FY26": 12.6}
GNPA = {"FY19": 2.3, "FY20": 1.4, "FY21": 1.0, "FY22": 2.2, "FY23": 2.0, "FY24": 1.7, "FY25": 2.0, "FY26": 1.9}
NNPA = {"FY19": 1.9, "FY20": 1.1, "FY21": 0.7, "FY22": 1.8, "FY23": 1.6, "FY24": 1.3, "FY25": 1.2, "FY26": 1.3}
CRAR = {"FY19": 21.6, "FY20": 17.9, "FY21": 23.5, "FY22": 23.0, "FY23": 17.9, "FY24": 23.5, "FY25": 21.9, "FY26": 22.4}
BVPS = {"FY19": 19.9, "FY20": 25.3, "FY21": 28.8, "FY22": 35.9, "FY23": 42.1, "FY24": 61.2, "FY25": 68.3, "FY26": 78.2}
PCR = {"FY19": 14.6, "FY20": 25.5, "FY21": 29.9, "FY22": 22.1, "FY23": 22.2, "FY24": 20.4, "FY25": 40.0, "FY26": 32.3}
COST_INCOME = {"FY19": 61.9, "FY20": 70.8, "FY21": 61.5, "FY22": 58.4, "FY23": 58.6, "FY24": 58.2, "FY25": 57.6, "FY26": 57.2}
# FY26-report basis (revised presentation) for yield / cost of borrowings / spread
YIELD_26 = {"FY22": 16.0, "FY23": 16.1, "FY24": 16.7, "FY25": 17.1, "FY26": 16.7}
COB_26 = {"FY22": 7.8, "FY23": 7.8, "FY24": 8.6, "FY25": 9.0, "FY26": 8.1}
SPREAD_26 = {"FY22": 8.2, "FY23": 8.3, "FY24": 8.1, "FY25": 8.2, "FY26": 8.6}
# Earlier-report basis (as printed in AR FY24 / AR FY25) – shown for transparency
YIELD_OLD = {"FY19": 13.2, "FY20": 14.5, "FY21": 15.5, "FY22": 15.6, "FY23": 15.8, "FY24": 16.2, "FY25": 17.4}
COB_OLD = {"FY19": 8.3, "FY20": 8.4, "FY21": 8.3, "FY22": 7.4, "FY23": 7.8, "FY24": 8.8, "FY25": 9.2}
SPREAD_OLD = {"FY19": 4.9, "FY20": 6.1, "FY21": 7.2, "FY22": 8.2, "FY23": 8.0, "FY24": 7.4, "FY25": 8.1}

BRANCHES = {"FY19": 149, "FY20": 303, "FY21": 359, "FY22": 516, "FY23": 575, "FY24": 621, "FY25": 694, "FY26": 757}
BRANCH_GOLD = {"FY21": 301, "FY22": 407, "FY23": 437, "FY24": 438, "FY25": 484, "FY26": 558}
BRANCH_MSME = {"FY21": 58, "FY22": 109, "FY23": 138, "FY24": 183, "FY25": 210, "FY26": 129}
BRANCH_COLOC = {"FY26": 70}  # MSME + Gold (Vyapaar) co-located branches
STATES = {"FY19": 8, "FY24": 18, "FY25": 18, "FY26": 17}
EMPLOYEES = {"FY24": 4298, "FY25": 4568, "FY26": 5303}
TOP5_STATES_AUM = {"FY21": 85.1, "FY22": 80.3, "FY23": 78.7, "FY24": 77.9, "FY25": 76.0, "FY26": 75.1}

# Disbursements by product (₹ crore) – AR FY26 MD&A p.64-65
DISB_GOLD = {"FY22": 5515, "FY23": 7437, "FY24": 9377, "FY25": 14603, "FY26": 28326}
DISB_MTLAP = {"FY22": 518, "FY23": 1091, "FY24": 1359, "FY25": 2303, "FY26": 2180}
DISB_STLAP = {"FY22": 765, "FY23": 1102, "FY24": 1475, "FY25": 1004, "FY26": 904}
TOTAL_DISB_LAKH = {"FY24": 1357828, "FY25": 1878732, "FY26": 3141014}  # Directors' Reports

# Product mix (% of AUM) – AR FY24 MD&A p.57-59, AR FY25 CEO letter p.14, AR FY26 p.10-13
MIX = {
    "FY24": {"Gold": 32.6, "Mortgage": 51.0, "Business/Other": 16.4},   # Business derived = 100-32.6-51.0
    "FY25": {"Gold": 37.2, "Mortgage": 51.0, "Business/Other": 10.5},   # 1.3% rounding residual not shown
    "FY26": {"Gold": 51.4, "Mortgage": 46.5, "Business/Other": 2.1},    # Business/other derived
}
AUM_PRODUCT_CR = {
    "FY24": {"Gold": 3969.4, "Mortgage": 6217.9},
    "FY25": {"Gold": 5880, "Mortgage": 8060, "Business": 1660},
    "FY26": {"Gold": 10352, "Mortgage": 9362, "MT LAP": 5570, "ST LAP+HL": 3792, "Total": 20153},
}

# ---------------------------------------------------------------------------
# Directors' Report financial highlights (₹ lakh) – FY23 & FY24 from AR FY24
# p.64; FY25 from AR FY25 p.64; FY26 from AR FY26 p.68.
# ---------------------------------------------------------------------------
FIN = {
    "FY23": dict(rev=121467, nii=63801, fee=10451, opex_prov=48413, pbt=24302, pat=18013,
                 adv=799970, borr=713583, assets=907099, nw=135568, roa=2.31, roe=14.36,
                 eps=5.60, deps=5.59, bvps=42.11, ci=58.60, crar=17.94),
    "FY24": dict(rev=162300, nii=81212, fee=13132, opex_prov=61536, pbt=32808, pat=24470,
                 adv=982245, borr=821460, assets=1113784, nw=226083, roa=2.42, roe=13.54,
                 eps=7.22, deps=7.12, bvps=61.20, ci=58.24, crar=23.46),
    "FY25": dict(rev=207982, nii=107080, fee=15524, opex_prov=92229, pbt=30375, pat=22518,
                 adv=1164637, borr=1026866, assets=1324970, nw=254736, roa=1.82, roe=9.39,
                 eps=6.06, deps=6.04, bvps=68.35, ci=57.58, crar=21.92),
    "FY26": dict(rev=222661, nii=122975, fee=11754, opex_prov=88628, pbt=46101, pat=34360,
                 adv=1431885, borr=1348413, assets=1687478, nw=292610, roa=2.44, roe=12.62,
                 eps=9.20, deps=9.12, bvps=78.19, ci=57.23, crar=22.40),
}

# Statement of Profit & Loss FY26 vs FY25 (₹ lakh) – AR FY26 p.169 and notes 26-34
PL = {
    "FY26": dict(int_income=210907, fee_comm=9669, fv_gain=1784, rev_ops=222360, other_inc=301, total_rev=222661,
                 fin_cost=87932, fee_exp=-20, impairment=11527, emp=44393, dep=5447, other_exp=27281,
                 total_exp=176560, pbt=46101, cur_tax=12107, def_tax=-366, pat=34360, oci=1502, tci=35862),
    "FY25": dict(int_income=192458, fee_comm=11171, fv_gain=2558, rev_ops=206187, other_inc=1795, total_rev=207982,
                 fin_cost=85378, fee_exp=1850, impairment=21636, emp=39030, dep=4885, other_exp=24828,
                 total_exp=177607, pbt=30375, cur_tax=10169, def_tax=-2312, pat=22518, oci=4159, tci=26677),
}
INT_INCOME_BREAKUP = {  # note 26
    "Interest on loans": (196762, 173517),
    "Income on direct assignment": (10198, 15231),
    "Interest income from investments": (2175, 1957),
    "Interest on fixed deposits": (1624, 1555),
    "Interest on security deposit": (148, 198),
}
FEE_BREAKUP = {  # note 27
    "Income from distribution": (4083, 5915),
    "Loan servicing fee": (525, 272),
    "Other fee and charges": (5061, 4984),
}
FIN_COST_BREAKUP = {  # note 30
    "Interest on borrowings (other than debt securities)": (73394, 73220),
    "Interest on debt securities (NCD/CP)": (7127, 8403),
    "Interest on subordinated liabilities": (4356, 1257),
    "Interest on lease liability": (1328, 1204),
    "Other interest expense": (1555, 1054),
    "Foreign currency translation loss (net)": (172, 240),
}
IMPAIRMENT_BREAKUP = {  # note 32
    "Bad debts (net of recovery) – amortised cost loans": (8352, 3151),
    "ECL provision – amortised cost loans": (-537, 9824),
    "Bad debts (net of recovery) – FVOCI loans": (5023, 1564),
    "ECL provision – FVOCI loans": (-689, 6392),
    "ECL on investments": (-625, 375),
    "ECL on receivables": (3, 330),
}
OTHER_EXP_TOP = {  # note 34 – largest items
    "Technology cost": (4387, 4348),
    "Legal and professional fees": (4237, 3997),
    "GST expenses": (3037, 3126),
    "Collection agency commission": (2389, 2581),
    "Travelling and conveyance": (2290, 2264),
    "Housekeeping and security": (1596, 1310),
    "Sourcing expenses": (1474, 720),
    "Securitisation expenses": (1162, 669),
    "Insurance": (1101, 424),
    "Rent (short-term/low value)": (681, 956),
    "Postage and courier": (609, 603),
    "Printing and stationery": (609, 407),
    "Advertisement and business promotion": (600, 471),
    "CSR expenditure": (584, 473),
}
EMP_BREAKUP = {  # note 33
    "Salaries and wages": (40027, 35928),
    "Contribution to provident and other funds": (1799, 1650),
    "Share based payments": (1181, 130),
    "Staff welfare": (1386, 1322),
}

# Balance sheet (₹ lakh) – AR FY26 p.168
BS = {
    "FY26": dict(cash=133973, bank_bal=5122, deriv=21502, trade_rec=727, other_rec=2240, loans=1431885,
                 inv=40167, other_fin=20736, total_fin=1656352, cur_tax=199, dta=938, ppe=4179, rou=17433,
                 cwip=177, intang_dev=27, intang=362, other_nonfin=7811, total_nonfin=31126, total_assets=1687478,
                 deriv_l=0, trade_pay=910, other_pay=0, debt_sec=173031, borr=1083747, subdebt=91635,
                 lease=19074, other_fin_l=21638, total_fin_l=1390035, cur_tax_l=0, prov=1983, other_nonfin_l=2850,
                 total_nonfin_l=4833, share_cap=37421, other_eq=255189, equity=292610),
    "FY25": dict(cash=72460, bank_bal=11009, deriv=58, trade_rec=565, other_rec=1366, loans=1164637,
                 inv=40419, other_fin=8671, total_fin=1299185, cur_tax=0, dta=1070, ppe=3191, rou=15395,
                 cwip=28, intang_dev=64, intang=292, other_nonfin=5745, total_nonfin=25785, total_assets=1324970,
                 deriv_l=123, trade_pay=873, other_pay=157, debt_sec=50022, borr=929237, subdebt=47607,
                 lease=16854, other_fin_l=20229, total_fin_l=1065102, cur_tax_l=1161, prov=1381, other_nonfin_l=2590,
                 total_nonfin_l=5132, share_cap=37272, other_eq=217464, equity=254736),
}

# Borrowing composition FY26 / FY25 (₹ lakh) – notes 16, 17, 18
BORROW = {
    "Term loans from banks (other than related party)": (568211, 563264),
    "Term loan from related party (Federal Bank)": (106413, 102963),
    "External commercial borrowings (ECB)": (238236, 25669),
    "Term loans from other parties (FIs)": (86557, 70568 + 2515),
    "Loans repayable on demand – banks": (78330, 158254),
    "Loans repayable on demand – related party": (6000, 6004),
    "Secured NCDs (carrying amount)": (56588, 40144),
    "Commercial paper (net of discount)": (116443, 9878),
    "Subordinated NCDs – related party": (24612, 24548),
    "Subordinated NCDs – others": (67023, 23059),
}

# Loans note 8 (₹ lakh)
LOANS = {
    "FY26": dict(gross=1450548, amort=1152348, fvoci=298200, ecl=18663, net=1431885,
                 secured=1443902, guaranteed=1806, unsecured=4840,
                 s1=1112245, s2=22225, s3=17878, gold_gross=791943, gold_pct_assets=46.93),
    "FY25": dict(gross=1183842, amort=839410, fvoci=344432, ecl=19205, net=1164637,
                 secured=1060316, guaranteed=323, unsecured=123203,
                 s1=777298, s2=42637, s3=19475, gold_gross=474957, gold_pct_assets=35.85),
}
# Note 48.09 movement of credit-impaired loans (₹ lakh)
IMPAIRED = {
    "FY26": dict(open=23888, add=22713, red=10590, wo=8817, close=27194, net_open=14438, net_close=18505,
                 allow_open=9450, allow_close=8689, net_ratio=1.28),
    "FY25": dict(open=16457, add=19523, red=11409, wo=683, close=23888, net_open=13199, net_close=14438,
                 allow_open=3258, allow_close=9450, net_ratio=1.22),
}
NPA_SOLD = {"FY26": (814, 10490), "FY25": (1, 1690)}  # accounts, principal ₹ lakh
TOP20 = {"FY26": (6848, 0.47), "FY25": (8251, 0.70)}  # ₹ lakh, % of advances
TOP4_IMPAIRED = {"FY26": 942, "FY25": 1976}
CRAR_DETAIL = {"FY26": (22.40, 17.52, 4.88, 66417), "FY25": (21.92, 18.92, 3.00, 31960)}
REAL_ESTATE = {"FY26": (541315, 85230), "FY25": (485115, 76490)}  # residential, commercial ₹ lakh

# ALM maturity pattern FY26 (₹ lakh) – note 48 (10 buckets)
ALM_BUCKETS = ["1-7d", "8-14d", "15-31d", "1-2m", "2-3m", "3-6m", "6-12m", "1-3y", "3-5y", ">5y"]
ALM_ADV_26 = [8343, 1589, 14179, 21668, 17987, 65315, 772096, 198436, 198201, 134071]
ALM_BOR_26 = [33032, 1344, 24910, 44537, 60103, 136918, 225313, 640921, 132503, 48832]
ALM_ADV_25 = [12506, 2912, 15049, 38563, 34168, 89760, 428503, 233081, 173906, 136189]
ALM_BOR_25 = [13170, 5923, 29875, 67209, 74808, 124034, 158016, 439855, 85845, 28131]

# Gold auctions FY26 – Directors' Report
AUCTION = dict(accounts=4633, principal=2039, interest=2756, value=4401)
FRAUDS_LAKH = 110
CSR_SPEND_LAKH = 583.63
BOARD_MEETINGS = 11
WHISTLE = (16, 3)
POSH = (3, 3, 0)

# Shareholding 31 Mar 2026 vs 2025 (%) – Corporate Governance Report p.106
SHAREHOLDING = [
    ("Promoter and Promoter Group (Federal Bank)", 60.79, 61.03),
    ("Public (individuals)", 15.94, 14.34),
    ("Alternate Investment Funds", 13.01, 14.38),
    ("Insurance Companies", 3.10, 4.04),
    ("Mutual Funds", 2.71, 2.39),
    ("Other Bodies Corporate", 1.63, 1.85),
    ("Foreign Portfolio Investors", 0.66, 0.49),
    ("NRIs (repatriable + non-repatriable)", 0.98, 0.74),
    ("HUF", 0.53, 0.43),
    ("Key Managerial Personnel", 0.30, 0.20),
    ("LLPs, Trusts, Clearing Members", 0.35, 0.11),
]
SHARES_OUT = 374206101
SHARES_OUT_PY = 372716854
ESOP_ALLOTTED = 1489247
MCAP_CR = 4642  # as of 31 March 2026, AR FY26 inside cover

# Branch network by state FY26 – Directors' Report p.69
BRANCH_STATE = [
    ("Maharashtra", 31, 102, 8, 141), ("Gujarat", 11, 110, 15, 136), ("Karnataka", 9, 77, 9, 95),
    ("Tamil Nadu", 26, 57, 7, 90), ("Andhra Pradesh", 9, 42, 6, 57), ("Delhi NCR", 1, 45, 0, 46),
    ("Telangana", 4, 27, 11, 42), ("Rajasthan", 10, 19, 5, 34), ("Haryana", 7, 25, 0, 32),
    ("Uttar Pradesh", 9, 21, 2, 32), ("Madhya Pradesh", 7, 8, 5, 20), ("Punjab", 1, 12, 0, 13),
    ("Uttarakhand", 1, 5, 2, 8), ("Goa", 0, 5, 0, 5), ("Pondicherry", 2, 1, 0, 3),
    ("Dadra & Nagar Haveli (UT)", 0, 2, 0, 2), ("Chandigarh", 1, 0, 0, 1),
]
BRANCH_TOTAL = (129, 558, 70, 757)

# NCDs outstanding 31 Mar 2026 – Directors' Report p.71
NCDS = [
    ("Reset-rate secured NCDs", "26 Jun 2023", "26 Jun 2027", 31.25),
    ("9.00% unsecured subordinated Tier II NCDs", "26 May 2023", "26 Apr 2030", 200.00),
    ("G-Sec linked secured market-linked NCDs", "4 Jan 2023", "4 Apr 2026", 200.00),
    ("9.90% unsecured NCDs", "30 Sep 2020", "30 Sep 2027", 250.00),
    ("Repo-rate linked secured NCDs (Series I-2408)", "14 Aug 2024", "14 Aug 2028", 75.00),
    ("G reset-rate secured NCDs Series 4 (7.29%)", "6 Jan 2026", "5 Jan 2029", 200.00),
    ("8.85% unsecured subordinated NCDs Series I", "24 Mar 2026", "21 Oct 2033", 250.00),
    ("8.90% unsecured subordinated NCDs Series II", "24 Mar 2026", "21 Nov 2033", 200.00),
]

# Peer snapshot FY26 (web-verified results coverage, May 2026) – see bibliography
PEERS = [
    ("Fedbank Financial Services (standalone)", "20,153", "10,352 (51%)", "343.6", "22.4", "757", "1.9 / 1.3"),
    ("Muthoot Finance (standalone)", "1,62,826", "1,65,030 (consol.)", "10,134", "20.75", "7,568", "n.a."),
    ("Manappuram Finance (consolidated)", "63,798", "50,953 (80%)", "993", "21.3", "n.a.", "n.a."),
]

# Macro / sector datapoints quoted in AR FY26 MD&A (with its cited sources)
SECTOR = dict(
    gdp_fy26=7.7, gdp_fy25=7.1, gdp_fy24=7.2, gdp_fy27_range="6.6%-7.2%", repo_cut_bps=125, repo=5.25,
    cpi_fy26="~2.1% (approx. 1.7% Apr-Dec 2025)", gfcf=7.8, nbfc_assets_tn=45, nbfc_growth="15-17%",
    nbfc_fy27_tn=50, retail_credit_growth=19.8, retail_credit_tn=82, msme_units_cr=7.47, msme_emp_cr=32.8,
    msme_gdp=31.1, msme_exports=48.58, msme_mfg=35.4, udyam_cr=7.9, gold_loan_mkt_lakh_cr=15, gold_loan_fy27=18,
    bank_share_gold=82, nbfc_share_2021=22, top4_nbfc_share_2025=81, top4_nbfc_share_2022=90,
    gold_price_rise=65, gold_price_from=2607, gold_price_to=4315, gold_demand_t=711, gold_imports_bn=72.4,
    gold_imports_prev=57.9, household_gold_t=25000, housing_gdp=11, housing_gdp_2015=8, housing_loans_lakh_cr=37,
    lap_growth="16-18%", household_credit_gdp=42, china=60, us=69, uk=76, bank_credit_gdp=56,
    msme_credit_gap_tn=92, msme_addressable_tn=25,
)

# Operating KPIs FY26 – Key Highlights p.2-3, CEO statement p.18-21, Investment case p.14-15
KPI26 = dict(
    aum_cr=20153, secured=98.9, gnpa=1.9, nnpa=1.3, credit_cost=0.8, roa=2.4, roe=12.6, disb_cr=31410, pat_cr=343.6,
    branches_added=148, ats_mtlap=72.4, ats_stlap=16.1, ats_gold=2.7, emp_added=735, aum_per_emp=3.8,
    customers_lakh=3.44, bot=35, cust_per_branch=455, tat=100, csat=85, nim=8.8, coll_eff=99.7, de=4.6,
    tat_approval=10, tat_disb=15, gold_growth=76, mort_growth=16.1, gold_tonnes=12.6, gold_tonnes_growth=12,
    gold_aum_per_branch=16.5, gold_ltv=60.9, onboard_ltv=70, dsgl_aum=1730, dsgl_growth=108,
    lenders=41, lenders_prev=39, ecb_usd_mn=250, ecb_share=17, cp_share=9, cob_q4_26=7.83, cob_q4_25=8.72,
    fixed_rate=40, fixed_rate_prev=10, da_cr=1901, da_cr_prev=2349, colending_lakh=243265, selldown_lakh=257933,
    offbook=12.1, offbook_prev=25.1, offbook_fy24=18.7, da_income_cr=7.4, da_income_drop=88.8, da_pbt_share=1.6,
    da_pbt_share_prev=21.7, inhouse_sourcing=75, dsa=25, collections_x=1.8, agency_x=0.4, stage3_rec_from=6.5,
    stage3_rec_to=14.5, credit_cost_drop_bps=93, roa_q4=2.6, roe_q4=14.0, bl_exit_cr=886, bl_aum_open=1656,
    bl_auf_open=1216, bl_onbook=0.4, mort_self_occ=82.2, mtlap_yield=12.0, stlap_yield=15.1, cibil700=76,
    enach=90, enach_digital=86, digital_coll=70, startups_eval=89, startups_onboard=6, startups_poc=8,
    tier2=4.9, subdebt_raised=450, women=16.4, women_prev=15.7, training_hrs=7.44, attrition=35.85,
    apprentices=400, google_reviews_from=1500, google_reviews_to=7500, rating=4.58, leads_lakh=17,
    conversions=65000, tele_leads_lakh=3.7, tele_conv=12000, emission_int_from=3.93, emission_int_to=2.96,
    water_kl=89432, ewaste_t=1.9, cuddles_children=496, samarthanam_women=700, growth_target="20-25%",
)
