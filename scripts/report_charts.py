"""Chart generation (matplotlib) for the Fedfina report. Output PNGs go to a temp dir."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from report_data import *

NAVY, TEAL, GOLD, GREY, RED, LIGHT = "#123A63", "#167D9A", "#C9A227", "#8A8F98", "#B5443C", "#DCE6F0"
plt.rcParams.update({
    "font.size": 8.5, "axes.titlesize": 9.5, "axes.titleweight": "bold", "axes.edgecolor": "#444444",
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False, "legend.fontsize": 8,
    "figure.dpi": 200,
})


def _save(fig, path):
    fig.tight_layout(pad=0.6)
    fig.savefig(path, dpi=200)
    plt.close(fig)


def _label_bars(ax, bars, fmt="{:,.0f}", fs=7.5, off=0.01):
    ymax = ax.get_ylim()[1]
    for b in bars:
        h = b.get_height()
        ax.text(b.get_x() + b.get_width() / 2, h + ymax * off, fmt.format(h), ha="center", va="bottom", fontsize=fs)


def make_all(outdir):
    os.makedirs(outdir, exist_ok=True)
    p = lambda n: os.path.join(outdir, n)

    # 1. AUM FY19-FY26 (₹ crore)
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    vals = [AUM_MN[y] / 10 for y in YEARS8]
    bars = ax.bar(YEARS8, vals, color=[GREY] * 3 + [NAVY] * 5)
    _label_bars(ax, bars)
    ax.set_title("Assets Under Management, FY2018-19 to FY2025-26 (₹ crore)")
    ax.set_ylim(0, max(vals) * 1.18)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    _save(fig, p("aum.png"))

    # 2. PAT FY19-FY26 (₹ crore)
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    vals = [PAT_MN[y] / 10 for y in YEARS8]
    bars = ax.bar(YEARS8, vals, color=[GREY] * 3 + [TEAL] * 5)
    _label_bars(ax, bars, "{:,.1f}")
    ax.set_title("Profit After Tax, FY2018-19 to FY2025-26 (₹ crore)")
    ax.set_ylim(0, max(vals) * 1.18)
    _save(fig, p("pat.png"))

    # 3. Product mix stacked bars
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    yrs = ["FY24", "FY25", "FY26"]
    g = [MIX[y]["Gold"] for y in yrs]; m = [MIX[y]["Mortgage"] for y in yrs]; b = [MIX[y]["Business/Other"] for y in yrs]
    ax.bar(yrs, g, color=GOLD, label="Gold loans"); ax.bar(yrs, m, bottom=g, color=NAVY, label="Mortgage loans (LAP + HL)")
    ax.bar(yrs, b, bottom=np.array(g) + np.array(m), color=GREY, label="Business loans / other")
    for i, y in enumerate(yrs):
        ax.text(i, g[i] / 2, f"{g[i]:.1f}%", ha="center", va="center", color="white", fontsize=8, fontweight="bold")
        ax.text(i, g[i] + m[i] / 2, f"{m[i]:.1f}%", ha="center", va="center", color="white", fontsize=8, fontweight="bold")
        if b[i] > 4: ax.text(i, g[i] + m[i] + b[i] / 2, f"{b[i]:.1f}%", ha="center", va="center", color="white", fontsize=8)
    ax.set_ylim(0, 100); ax.set_ylabel("% of AUM"); ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3)
    ax.set_title("Product mix of AUM: shift from mortgage-led to gold-led secured book")
    _save(fig, p("mix.png"))

    # 4. ROA & ROE
    fig, ax1 = plt.subplots(figsize=(6.6, 2.5))
    roa = [ROA[y] for y in YEARS5]; roe = [ROE[y] for y in YEARS5]
    ax1.bar(YEARS5, roe, color=LIGHT, label="RoE (%)", width=0.55)
    for i, v in enumerate(roe): ax1.text(i, v + 0.3, f"{v:.1f}", ha="center", fontsize=8)
    ax1.set_ylabel("RoE (%)"); ax1.set_ylim(0, 18)
    ax2 = ax1.twinx(); ax2.plot(YEARS5, roa, color=RED, marker="o", label="RoA (%)"); ax2.set_ylim(0, 3.2); ax2.set_ylabel("RoA (%)")
    for i, v in enumerate(roa): ax2.text(i, v + 0.12, f"{v:.1f}", ha="center", fontsize=8, color=RED)
    ax2.spines["right"].set_visible(True)
    ax1.set_title("Return on Assets and Return on Equity, FY22-FY26")
    h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax1.legend(h1 + h2, l1 + l2, loc="upper left")
    _save(fig, p("roa_roe.png"))

    # 5. Yield / CoB / Spread / C-I
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    ax.plot(YEARS5, [YIELD_26[y] for y in YEARS5], marker="o", color=NAVY, label="Yield (%)")
    ax.plot(YEARS5, [COB_26[y] for y in YEARS5], marker="s", color=RED, label="Cost of borrowings (%)")
    ax.plot(YEARS5, [SPREAD_26[y] for y in YEARS5], marker="^", color=TEAL, label="Spread (%)")
    for y_i, y in enumerate(YEARS5):
        ax.text(y_i, YIELD_26[y] + 0.4, f"{YIELD_26[y]:.1f}", ha="center", fontsize=7.5, color=NAVY)
        ax.text(y_i, COB_26[y] - 0.9, f"{COB_26[y]:.1f}", ha="center", fontsize=7.5, color=RED)
        ax.text(y_i, SPREAD_26[y] + 0.4, f"{SPREAD_26[y]:.1f}", ha="center", fontsize=7.5, color=TEAL)
    ax.set_ylim(5, 19); ax.legend(ncol=3, loc="upper center"); ax.set_title("Yield, cost of borrowings and spread, FY22-FY26 (FY26 report basis)")
    _save(fig, p("margins.png"))

    # 6. GNPA / NNPA / PCR
    fig, ax1 = plt.subplots(figsize=(6.6, 2.5))
    x = np.arange(5); w = 0.36
    b1 = ax1.bar(x - w / 2, [GNPA[y] for y in YEARS5], w, color=NAVY, label="GNPA (%)")
    b2 = ax1.bar(x + w / 2, [NNPA[y] for y in YEARS5], w, color=TEAL, label="NNPA (%)")
    _label_bars(ax1, b1, "{:.1f}"); _label_bars(ax1, b2, "{:.1f}")
    ax1.set_xticks(x); ax1.set_xticklabels(YEARS5); ax1.set_ylim(0, 3.2); ax1.set_ylabel("%")
    ax2 = ax1.twinx(); ax2.plot(x, [PCR[y] for y in YEARS5], color=GOLD, marker="o", label="Provision coverage (%)"); ax2.set_ylim(0, 60)
    ax2.spines["right"].set_visible(True); ax2.set_ylabel("PCR (%)")
    for i, y in enumerate(YEARS5): ax2.text(i, PCR[y] + 2.5, f"{PCR[y]:.1f}", ha="center", fontsize=7.5, color="#8a6d10")
    h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax1.legend(h1 + h2, l1 + l2, loc="upper left", ncol=3)
    ax1.set_title("Asset quality: GNPA, NNPA and provision coverage, FY22-FY26")
    _save(fig, p("npa.png"))

    # 7. CRAR & BVPS
    fig, ax1 = plt.subplots(figsize=(6.6, 2.5))
    bars = ax1.bar(YEARS5, [CRAR[y] for y in YEARS5], color=NAVY, width=0.55, label="CRAR (%)")
    _label_bars(ax1, bars, "{:.1f}"); ax1.set_ylim(0, 30); ax1.set_ylabel("CRAR (%)")
    ax1.axhline(15, color=RED, ls="--", lw=0.8); ax1.text(4.35, 15.4, "RBI minimum 15%", color=RED, fontsize=7, ha="right")
    ax2 = ax1.twinx(); ax2.plot(YEARS5, [BVPS[y] for y in YEARS5], color=GOLD, marker="o", label="Book value per share (₹)"); ax2.set_ylim(0, 100)
    ax2.spines["right"].set_visible(True); ax2.set_ylabel("₹ per share")
    for i, y in enumerate(YEARS5): ax2.text(i, BVPS[y] + 4, f"{BVPS[y]:.1f}", ha="center", fontsize=7.5, color="#8a6d10")
    h1, l1 = ax1.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax1.legend(h1 + h2, l1 + l2, loc="upper left", ncol=2)
    ax1.set_title("Capital adequacy and book value per share, FY22-FY26")
    _save(fig, p("crar.png"))

    # 8. Borrowing composition FY26 (pie)
    fig, ax = plt.subplots(figsize=(6.6, 2.7))
    labels = ["Bank term loans", "Federal Bank term loan", "ECB (hedged)", "Other FI term loans", "Demand loans / WC",
              "Secured NCDs", "Commercial paper", "Subordinated NCDs"]
    vals = [568211, 106413, 238236, 86557, 84330, 56588, 116443, 91635]
    cols = [NAVY, "#2E5A88", TEAL, "#5BA3B8", GREY, GOLD, "#E0C464", RED]
    wedges, _ = ax.pie(vals, colors=cols, startangle=90, counterclock=False, wedgeprops=dict(width=0.45, edgecolor="white"))
    tot = sum(vals)
    ax.legend(wedges, [f"{l} – ₹{v/100:,.0f} cr ({v/tot*100:.1f}%)" for l, v in zip(labels, vals)], loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=7.5)
    ax.set_title("Borrowings by instrument, 31 March 2026 (total ₹13,484 crore)")
    _save(fig, p("borrow.png"))

    # 9. Branch network
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    yrs = ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]
    g = [BRANCH_GOLD[y] for y in yrs]; m = [BRANCH_MSME[y] for y in yrs]; c = [BRANCH_COLOC.get(y, 0) for y in yrs]
    ax.bar(yrs, g, color=GOLD, label="Gold loan branches"); ax.bar(yrs, m, bottom=g, color=NAVY, label="MSME hubs")
    ax.bar(yrs, c, bottom=np.array(g) + np.array(m), color=TEAL, label="Co-located (Vyapaar)")
    for i, y in enumerate(yrs): ax.text(i, g[i] + m[i] + c[i] + 12, f"{BRANCHES[y]}", ha="center", fontsize=8, fontweight="bold")
    ax.set_ylim(0, 880); ax.legend(ncol=3, loc="upper left"); ax.set_title("Branch network by format, FY21-FY26 (total branches labelled)")
    _save(fig, p("branches.png"))

    # 10. Disbursements by product
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    x = np.arange(5); w = 0.27
    b1 = ax.bar(x - w, [DISB_GOLD[y] for y in YEARS5], w, color=GOLD, label="Gold loans")
    b2 = ax.bar(x, [DISB_MTLAP[y] for y in YEARS5], w, color=NAVY, label="Medium-ticket LAP")
    b3 = ax.bar(x + w, [DISB_STLAP[y] for y in YEARS5], w, color=TEAL, label="Small-ticket LAP & HL")
    for bs in (b1, b2, b3): _label_bars(ax, bs, "{:,.0f}", fs=6.5)
    ax.set_xticks(x); ax.set_xticklabels(YEARS5); ax.set_ylim(0, 33000); ax.legend(ncol=3, loc="upper left")
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax.set_title("Disbursements by product, FY22-FY26 (₹ crore)")
    _save(fig, p("disb.png"))

    # 11. Stage-wise loans
    fig, ax = plt.subplots(figsize=(6.6, 2.3))
    cats = ["Stage 1", "Stage 2", "Stage 3"]
    v25 = [LOANS["FY25"][k] / LOANS["FY25"]["amort"] * 100 for k in ("s1", "s2", "s3")]
    v26 = [LOANS["FY26"][k] / LOANS["FY26"]["amort"] * 100 for k in ("s1", "s2", "s3")]
    x = np.arange(3); w = 0.36
    b1 = ax.bar(x - w / 2, v25, w, color=GREY, label="31 Mar 2025"); b2 = ax.bar(x + w / 2, v26, w, color=NAVY, label="31 Mar 2026")
    for bs in (b1, b2):
        for b in bs: ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{b.get_height():.1f}%", ha="center", fontsize=7.5)
    ax.set_xticks(x); ax.set_xticklabels(cats); ax.set_ylim(0, 110); ax.legend(loc="upper right")
    ax.set_title("Stage classification of loans at amortised cost (% of gross)")
    _save(fig, p("stages.png"))

    # 12. Shareholding pie
    fig, ax = plt.subplots(figsize=(6.6, 2.6))
    lab = [s[0] for s in SHAREHOLDING]; v = [s[1] for s in SHAREHOLDING]
    cols = [NAVY, TEAL, GOLD, "#2E5A88", "#5BA3B8", GREY, "#E0C464", RED, "#9DB9D3", "#C9C9C9", "#777777"]
    wedges, _ = ax.pie(v, colors=cols, startangle=90, counterclock=False, wedgeprops=dict(width=0.45, edgecolor="white"))
    ax.legend(wedges, [f"{l} – {x:.2f}%" for l, x in zip(lab, v)], loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=7)
    ax.set_title("Shareholding pattern, 31 March 2026")
    _save(fig, p("shareholding.png"))

    # 13. Top-5 state concentration
    fig, ax = plt.subplots(figsize=(6.6, 2.2))
    yrs = ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]
    v = [TOP5_STATES_AUM[y] for y in yrs]
    ax.plot(yrs, v, marker="o", color=NAVY)
    for i, x in enumerate(v): ax.text(i, x + 0.6, f"{x:.1f}%", ha="center", fontsize=8)
    ax.set_ylim(70, 90); ax.set_title("Share of AUM in top five states (%), FY21-FY26 – gradual diversification")
    _save(fig, p("top5.png"))

    # 14. Cost structure FY26 vs FY25 (₹ crore)
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    items = ["Finance costs", "Employee benefits", "Other expenses", "Depreciation", "Impairment (credit cost)"]
    v26 = [87932, 44393, 27281, 5447, 11527]; v25 = [85378, 39030, 24828, 4885, 21636]
    x = np.arange(5); w = 0.36
    b1 = ax.bar(x - w / 2, [a / 100 for a in v25], w, color=GREY, label="FY25"); b2 = ax.bar(x + w / 2, [a / 100 for a in v26], w, color=NAVY, label="FY26")
    _label_bars(ax, b1, "{:,.0f}", 7); _label_bars(ax, b2, "{:,.0f}", 7)
    ax.set_xticks(x); ax.set_xticklabels(items, fontsize=7.5); ax.set_ylim(0, 1050); ax.legend()
    ax.set_title("Expense structure, FY25 vs FY26 (₹ crore)")
    _save(fig, p("costs.png"))

    # 15. ALM cumulative gap FY26
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    adv = np.cumsum(ALM_ADV_26) / 100; bor = np.cumsum(ALM_BOR_26) / 100
    ax.plot(ALM_BUCKETS, adv, marker="o", color=NAVY, label="Cumulative advances maturing (₹ cr)")
    ax.plot(ALM_BUCKETS, bor, marker="s", color=RED, label="Cumulative borrowings maturing (₹ cr)")
    ax.fill_between(range(10), adv, bor, where=adv >= bor, color=LIGHT, alpha=0.7)
    ax.legend(loc="upper left"); ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax.set_title("Structural liquidity: cumulative maturity of advances vs borrowings, 31 March 2026")
    _save(fig, p("alm.png"))

    # 16. Revenue vs PAT FY23-FY26 (₹ crore) with PAT margin
    fig, ax1 = plt.subplots(figsize=(6.6, 2.4))
    yrs = ["FY23", "FY24", "FY25", "FY26"]
    rev = [FIN[y]["rev"] / 100 for y in yrs]; pat = [FIN[y]["pat"] / 100 for y in yrs]
    x = np.arange(4); w = 0.36
    b1 = ax1.bar(x - w / 2, rev, w, color=NAVY, label="Total revenue"); b2 = ax1.bar(x + w / 2, pat, w, color=TEAL, label="PAT")
    _label_bars(ax1, b1, "{:,.0f}", 7.5); _label_bars(ax1, b2, "{:,.0f}", 7.5)
    ax1.set_xticks(x); ax1.set_xticklabels(yrs); ax1.set_ylim(0, 2700); ax1.legend(loc="upper left")
    ax2 = ax1.twinx(); ax2.plot(x, [p_ / r * 100 for p_, r in zip(pat, rev)], color=GOLD, marker="o", label="PAT margin (%)"); ax2.set_ylim(0, 25)
    ax2.spines["right"].set_visible(True); ax2.set_ylabel("PAT margin (%)")
    for i, (p_, r) in enumerate(zip(pat, rev)): ax2.text(i, p_ / r * 100 + 1.2, f"{p_/r*100:.1f}%", ha="center", fontsize=7.5, color="#8a6d10")
    ax1.set_title("Total revenue, PAT and PAT margin, FY23-FY26 (₹ crore)")
    _save(fig, p("rev_pat.png"))

    return outdir


if __name__ == "__main__":
    make_all("/tmp/work/charts")
    print("ok")
