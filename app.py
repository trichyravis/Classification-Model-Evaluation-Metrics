
"""
Model Evaluation Metrics — Interactive Learning Lab
The Mountain Path Academy | Prof. V. Ravichandran
"""
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# ══════════════════════════════════════════════════════════════
# MOUNTAIN PATH ACADEMY — DESIGN SYSTEM
# ══════════════════════════════════════════════════════════════
GOLD = "#FFD700"
BLUE = "#003366"
MID = "#004d80"
CARD = "#112240"
TXT = "#e6f1ff"
MUTED = "#8892b0"
GRN = "#28a745"
RED = "#dc3545"
LB = "#ADD8E6"
BG_GRAD = "linear-gradient(135deg,#1a2332,#243447,#2a3f5f)"
WARN = "#FFC107"

st.set_page_config(
    page_title="Model Evaluation Metrics — The Mountain Path Academy",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Global CSS ──
st.html(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Source+Sans+3:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {{
    --gold: {GOLD}; --blue: {BLUE}; --mid: {MID}; --card: {CARD};
    --txt: {TXT}; --muted: {MUTED}; --grn: {GRN}; --red: {RED};
    --lb: {LB}; --warn: {WARN};
}}

.stApp {{
    background: {BG_GRAD};
    font-family: 'Source Sans 3', sans-serif;
}}

/* Sidebar */
section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #0a1628 0%, #112240 50%, #0a1628 100%) !important;
    border-right: 2px solid {GOLD} !important;
}}
section[data-testid="stSidebar"] * {{
    color: {TXT} !important;
    -webkit-text-fill-color: {TXT} !important;
}}
section[data-testid="stSidebar"] .stRadio label span {{
    color: {TXT} !important;
    -webkit-text-fill-color: {TXT} !important;
    font-family: 'Source Sans 3', sans-serif !important;
    font-size: 0.95rem !important;
}}
section[data-testid="stSidebar"] .stRadio label[data-checked="true"] span {{
    color: {GOLD} !important;
    -webkit-text-fill-color: {GOLD} !important;
    font-weight: 600 !important;
}}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {{
    gap: 0.5rem;
    background: rgba(17,34,64,0.6);
    border-radius: 12px;
    padding: 6px;
}}
.stTabs [data-baseweb="tab"] {{
    color: {MUTED} !important;
    background: transparent !important;
    border-radius: 8px !important;
    font-family: 'Source Sans 3', sans-serif !important;
    font-weight: 500 !important;
    padding: 8px 16px !important;
}}
.stTabs [aria-selected="true"] {{
    color: {GOLD} !important;
    background: rgba(255,215,0,0.12) !important;
    border-bottom: 2px solid {GOLD} !important;
}}
.stTabs [data-baseweb="tab-panel"] {{
    background: transparent !important;
}}

/* Metrics */
[data-testid="stMetric"] {{
    background: {CARD} !important;
    border: 1px solid rgba(255,215,0,0.2) !important;
    border-radius: 12px !important;
    padding: 16px !important;
}}
[data-testid="stMetricValue"] {{
    color: {GOLD} !important;
    -webkit-text-fill-color: {GOLD} !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1.6rem !important;
}}
[data-testid="stMetricLabel"] {{
    color: {TXT} !important;
    -webkit-text-fill-color: {TXT} !important;
}}
[data-testid="stMetricDelta"] {{
    font-family: 'JetBrains Mono', monospace !important;
}}

/* Slider */
.stSlider label {{
    color: {TXT} !important;
    -webkit-text-fill-color: {TXT} !important;
}}
.stSlider [data-baseweb="slider"] div {{
    color: {TXT} !important;
    -webkit-text-fill-color: {TXT} !important;
}}

/* Number input */
.stNumberInput label {{
    color: {TXT} !important;
    -webkit-text-fill-color: {TXT} !important;
}}

/* Selectbox */
.stSelectbox label {{
    color: {TXT} !important;
    -webkit-text-fill-color: {TXT} !important;
}}

/* Expander */
.streamlit-expanderHeader {{
    color: {GOLD} !important;
    -webkit-text-fill-color: {GOLD} !important;
    background: {CARD} !important;
    border-radius: 10px !important;
}}
details[data-testid="stExpander"] {{
    background: {CARD} !important;
    border: 1px solid rgba(255,215,0,0.15) !important;
    border-radius: 10px !important;
}}
details[data-testid="stExpander"] * {{
    color: {TXT} !important;
    -webkit-text-fill-color: {TXT} !important;
}}

/* Radio horizontal */
.stRadio > div {{
    gap: 0.5rem;
}}

/* Hide default Streamlit footer */
footer {{visibility: hidden;}}
#MainMenu {{visibility: hidden;}}
</style>
""")


# ══════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════

def mp_header(title, subtitle=""):
    """Mountain Path branded header."""
    sub_html = f'<div style="color:{MUTED};-webkit-text-fill-color:{MUTED};font-family:Source Sans 3,sans-serif;font-size:1rem;margin-top:4px;user-select:none;">{subtitle}</div>' if subtitle else ""
    st.html(f"""
    <div style="user-select:none;margin-bottom:18px;">
        <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:Playfair Display,serif;font-size:2rem;font-weight:700;letter-spacing:0.5px;">{title}</div>
        {sub_html}
        <div style="height:3px;background:linear-gradient(90deg,{GOLD},transparent);border-radius:2px;margin-top:8px;width:40%;"></div>
    </div>
    """)

def mp_subheader(title):
    st.html(f"""
    <div style="color:{LB};-webkit-text-fill-color:{LB};font-family:Playfair Display,serif;font-size:1.35rem;font-weight:600;margin:20px 0 10px 0;user-select:none;">{title}</div>
    """)

def mp_card(content, border_color=GOLD, bg=CARD):
    st.html(f"""
    <div style="background:{bg};border:1px solid {border_color};border-left:4px solid {border_color};border-radius:10px;padding:18px 22px;margin:10px 0;user-select:none;">
        <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-family:Source Sans 3,sans-serif;font-size:0.95rem;line-height:1.7;">{content}</div>
    </div>
    """)

def mp_insight(title, content):
    st.html(f"""
    <div style="background:rgba(255,215,0,0.08);border:1px solid rgba(255,215,0,0.3);border-left:4px solid {GOLD};border-radius:10px;padding:16px 20px;margin:12px 0;user-select:none;">
        <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:Playfair Display,serif;font-size:1rem;font-weight:700;margin-bottom:6px;">💡 {title}</div>
        <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-family:Source Sans 3,sans-serif;font-size:0.92rem;line-height:1.7;">{content}</div>
    </div>
    """)

def mp_warning(title, content):
    st.html(f"""
    <div style="background:rgba(220,53,69,0.08);border:1px solid rgba(220,53,69,0.3);border-left:4px solid {RED};border-radius:10px;padding:16px 20px;margin:12px 0;user-select:none;">
        <div style="color:{RED};-webkit-text-fill-color:{RED};font-family:Source Sans 3,sans-serif;font-size:0.95rem;font-weight:700;margin-bottom:6px;">⚠️ {title}</div>
        <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-family:Source Sans 3,sans-serif;font-size:0.92rem;line-height:1.7;">{content}</div>
    </div>
    """)

def mp_success(title, content):
    st.html(f"""
    <div style="background:rgba(40,167,69,0.08);border:1px solid rgba(40,167,69,0.3);border-left:4px solid {GRN};border-radius:10px;padding:16px 20px;margin:12px 0;user-select:none;">
        <div style="color:{GRN};-webkit-text-fill-color:{GRN};font-family:Source Sans 3,sans-serif;font-size:0.95rem;font-weight:700;margin-bottom:6px;">✅ {title}</div>
        <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-family:Source Sans 3,sans-serif;font-size:0.92rem;line-height:1.7;">{content}</div>
    </div>
    """)

def mp_formula(label, formula, explanation=""):
    expl = f'<div style="color:{MUTED};-webkit-text-fill-color:{MUTED};font-size:0.85rem;margin-top:6px;">{explanation}</div>' if explanation else ""
    st.html(f"""
    <div style="background:rgba(0,51,102,0.4);border:1px solid rgba(173,216,230,0.25);border-radius:10px;padding:14px 20px;margin:8px 0;user-select:none;">
        <div style="color:{LB};-webkit-text-fill-color:{LB};font-family:Source Sans 3,sans-serif;font-size:0.85rem;font-weight:600;margin-bottom:4px;">{label}</div>
        <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:JetBrains Mono,monospace;font-size:1.05rem;font-weight:500;">{formula}</div>
        {expl}
    </div>
    """)

def plotly_theme(fig, title="", h=420):
    fig.update_layout(
        title=dict(text=title, font=dict(family="Playfair Display", size=18, color=GOLD), x=0.5),
        paper_bgcolor="rgba(17,34,64,0.85)",
        plot_bgcolor="rgba(17,34,64,0.4)",
        font=dict(family="Source Sans 3", color=TXT, size=13),
        height=h,
        margin=dict(l=50, r=30, t=60, b=50),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=TXT)),
        xaxis=dict(gridcolor="rgba(136,146,176,0.15)", zerolinecolor="rgba(136,146,176,0.15)"),
        yaxis=dict(gridcolor="rgba(136,146,176,0.15)", zerolinecolor="rgba(136,146,176,0.15)"),
    )
    return fig

def compute_metrics(tp, tn, fp, fn):
    total = tp + tn + fp + fn
    acc = (tp + tn) / total if total > 0 else 0
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0
    spec = tn / (tn + fp) if (tn + fp) > 0 else 0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    npv = tn / (tn + fn) if (tn + fn) > 0 else 0
    fdr = fp / (fp + tp) if (fp + tp) > 0 else 0
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0
    bal_acc = (rec + spec) / 2
    denom = np.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)) if (tp+fp)*(tp+fn)*(tn+fp)*(tn+fn) > 0 else 1
    mcc = (tp*tn - fp*fn) / denom
    return dict(accuracy=acc, precision=prec, recall=rec, specificity=spec,
                f1_score=f1, fpr=fpr, npv=npv, fdr=fdr, fnr=fnr,
                balanced_accuracy=bal_acc, mcc=mcc, total=total)


# ══════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════

with st.sidebar:
    st.html(f"""
    <div style="text-align:center;padding:15px 0 5px 0;user-select:none;">
        <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:Playfair Display,serif;font-size:1.3rem;font-weight:800;letter-spacing:1px;">THE MOUNTAIN PATH</div>
        <div style="color:{LB};-webkit-text-fill-color:{LB};font-family:Source Sans 3,sans-serif;font-size:0.8rem;letter-spacing:3px;margin-top:2px;">ACADEMY</div>
        <div style="height:2px;background:linear-gradient(90deg,transparent,{GOLD},transparent);margin:10px auto;width:80%;"></div>
        <div style="color:{MUTED};-webkit-text-fill-color:{MUTED};font-size:0.75rem;">World of Finance</div>
    </div>
    """)

    st.html(f'<div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:Playfair Display,serif;font-size:1rem;font-weight:700;margin:20px 0 8px 0;user-select:none;">📚 Navigate</div>')

    page = st.radio(
        "Select Topic",
        [
            "🏠 Home",
            "1️⃣ Binary Classification",
            "2️⃣ Type I & II Errors",
            "3️⃣ Confusion Matrix",
            "4️⃣ Key Metrics Calculator",
            "5️⃣ ROC Curve & AUC",
            "6️⃣ Threshold Tuning Lab",
            "7️⃣ Advanced Metrics",
            "8️⃣ Finance Applications",
            "9️⃣ Q&A Practice",
        ],
        label_visibility="collapsed"
    )

    st.html(f"""
    <div style="position:fixed;bottom:0;left:0;width:inherit;padding:12px 16px;background:rgba(10,22,40,0.95);border-top:1px solid rgba(255,215,0,0.2);text-align:center;user-select:none;">
        <div style="color:{MUTED};-webkit-text-fill-color:{MUTED};font-size:0.7rem;">Prof. V. Ravichandran</div>
        <div style="margin-top:4px;">
            <a href="https://themountainpathacademy.com" target="_blank" style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-size:0.7rem;text-decoration:none;">themountainpathacademy.com</a>
        </div>
        <div style="margin-top:3px;">
            <a href="https://www.linkedin.com/in/trichyravis" target="_blank" style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-size:0.65rem;text-decoration:none;margin-right:8px;">LinkedIn</a>
            <a href="https://github.com/trichyravis" target="_blank" style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-size:0.65rem;text-decoration:none;">GitHub</a>
        </div>
    </div>
    """)


# ══════════════════════════════════════════════════════════════
# PAGE: HOME
# ══════════════════════════════════════════════════════════════

if page == "🏠 Home":
    st.html(f"""
    <div style="text-align:center;padding:30px 20px 10px 20px;user-select:none;">
        <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:Playfair Display,serif;font-size:0.9rem;letter-spacing:4px;font-weight:600;">THE MOUNTAIN PATH ACADEMY</div>
        <div style="color:white;-webkit-text-fill-color:white;font-family:Playfair Display,serif;font-size:2.8rem;font-weight:800;margin-top:12px;line-height:1.15;">Model Evaluation Metrics</div>
        <div style="color:{LB};-webkit-text-fill-color:{LB};font-family:Source Sans 3,sans-serif;font-size:1.15rem;margin-top:10px;">Interactive Learning Lab — Classification Model Performance</div>
        <div style="height:3px;background:linear-gradient(90deg,transparent,{GOLD},transparent);margin:20px auto;width:50%;"></div>
        <div style="color:{MUTED};-webkit-text-fill-color:{MUTED};font-size:0.85rem;">Prof. V. Ravichandran &nbsp;|&nbsp; NMIMS Bangalore &nbsp;|&nbsp; BITS Pilani &nbsp;|&nbsp; RV University Bangalore &nbsp;|&nbsp; Goa Institute of Management</div>
    </div>
    """)

    st.html(f'<div style="height:20px;"></div>')

    mp_subheader("Why Do We Evaluate Models?")
    mp_card("""
    When we build a predictive model — say, one that predicts whether a loan applicant will <b style="color:{0};-webkit-text-fill-color:{0};">default</b>
    or <b style="color:{1};-webkit-text-fill-color:{1};">not default</b> — we need concrete numbers to tell us:<br><br>
    <b style="color:{2};-webkit-text-fill-color:{2};">✦</b> How often does the model get it <b>right</b>?<br>
    <b style="color:{2};-webkit-text-fill-color:{2};">✦</b> When it gets it <b>wrong</b>, what <em>kind</em> of mistake does it make?<br>
    <b style="color:{2};-webkit-text-fill-color:{2};">✦</b> Is the model better at catching positives or avoiding false alarms?
    """.format(RED, GRN, GOLD))

    mp_insight("What We Are Trying to Find Out",
        "Model evaluation metrics answer: <em>\"Can I trust this model's predictions?\"</em> "
        "In finance, a wrong prediction can mean approving a bad loan or rejecting a good customer. "
        "The cost of errors is real and measurable.")

    mp_subheader("📋 What You'll Learn")

    cols = st.columns(3)
    topics = [
        ("🎯", "Foundations", "Binary classification, TP/TN/FP/FN, Type I & II Errors, Confusion Matrix"),
        ("📊", "Core Metrics", "Accuracy, Precision, Recall, Specificity, F1 Score, FPR — with live calculator"),
        ("🚀", "Advanced Topics", "ROC/AUC, PR curves, Threshold tuning, MCC, Log Loss, F-beta, Finance applications"),
    ]
    for col, (icon, title, desc) in zip(cols, topics):
        with col:
            st.html(f"""
            <div style="background:{CARD};border:1px solid rgba(255,215,0,0.15);border-radius:12px;padding:22px;text-align:center;min-height:180px;user-select:none;">
                <div style="font-size:2.2rem;margin-bottom:8px;">{icon}</div>
                <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:Playfair Display,serif;font-size:1.1rem;font-weight:700;">{title}</div>
                <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.88rem;margin-top:8px;line-height:1.6;">{desc}</div>
            </div>
            """)

    mp_subheader("🏦 Running Example Throughout This App")
    mp_card("""
    <b style="color:{0};-webkit-text-fill-color:{0};">Loan Default Prediction</b><br><br>
    A bank builds a model to predict loan default:<br>
    <b style="color:{1};-webkit-text-fill-color:{1};">Positive (1)</b> = Borrower <b>WILL default</b> (the event we want to detect)<br>
    <b style="color:{2};-webkit-text-fill-color:{2};">Negative (0)</b> = Borrower will <b>NOT default</b>
    """.format(GOLD, RED, GRN), border_color=LB)


# ══════════════════════════════════════════════════════════════
# PAGE: BINARY CLASSIFICATION
# ══════════════════════════════════════════════════════════════

elif page == "1️⃣ Binary Classification":
    mp_header("Binary Classification — The Setup", "Understanding the four possible outcomes")

    mp_card("""
    A <b style="color:{};-webkit-text-fill-color:{};">binary classification</b> model takes in data and outputs one of
    <b>two possible labels</b>. When we compare the model's prediction against the actual outcome,
    exactly <b>one of four things</b> happens.
    """.format(GOLD, GOLD))

    mp_subheader("The Four Outcomes")

    outcomes = [
        ("✅ True Positive (TP)", "Model predicted DEFAULT and borrower actually defaulted.",
         "The model correctly raised the alarm.", GRN),
        ("✅ True Negative (TN)", "Model predicted NO DEFAULT and borrower did not default.",
         "The model correctly stayed quiet.", GRN),
        ("❌ False Positive (FP)", "Model predicted DEFAULT but borrower did NOT default.",
         "False alarm! A good customer was wrongly flagged.", RED),
        ("❌ False Negative (FN)", "Model predicted NO DEFAULT but borrower actually defaulted.",
         "Missed alarm! A bad loan slipped through.", RED),
    ]
    for label, desc, note, color in outcomes:
        st.html(f"""
        <div style="background:{CARD};border-left:4px solid {color};border-radius:8px;padding:14px 18px;margin:8px 0;user-select:none;">
            <div style="color:{color};-webkit-text-fill-color:{color};font-family:Source Sans 3,sans-serif;font-size:1rem;font-weight:700;">{label}</div>
            <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.9rem;margin-top:4px;">{desc}</div>
            <div style="color:{MUTED};-webkit-text-fill-color:{MUTED};font-size:0.82rem;font-style:italic;margin-top:3px;">{note}</div>
        </div>
        """)

    mp_subheader("Visual Summary — The 2×2 Grid")
    st.html(f"""
    <div style="display:grid;grid-template-columns:140px 1fr 1fr;grid-template-rows:40px 1fr 1fr;gap:4px;max-width:550px;margin:10px auto;user-select:none;">
        <div></div>
        <div style="background:{MID};color:{GOLD};-webkit-text-fill-color:{GOLD};font-weight:700;text-align:center;padding:8px;border-radius:8px 8px 0 0;font-size:0.85rem;">Predicted: DEFAULT</div>
        <div style="background:{MID};color:{GOLD};-webkit-text-fill-color:{GOLD};font-weight:700;text-align:center;padding:8px;border-radius:8px 8px 0 0;font-size:0.85rem;">Predicted: NO DEFAULT</div>
        <div style="background:{MID};color:{GOLD};-webkit-text-fill-color:{GOLD};font-weight:700;text-align:center;padding:10px 8px;border-radius:8px 0 0 8px;font-size:0.85rem;">Actual:<br>DEFAULT</div>
        <div style="background:rgba(40,167,69,0.15);border:2px solid {GRN};border-radius:8px;text-align:center;padding:15px;color:{GRN};-webkit-text-fill-color:{GRN};font-weight:700;font-size:1.1rem;">TP ✅<br><span style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.78rem;font-weight:400;">Correct Alarm</span></div>
        <div style="background:rgba(220,53,69,0.12);border:2px solid {RED};border-radius:8px;text-align:center;padding:15px;color:{RED};-webkit-text-fill-color:{RED};font-weight:700;font-size:1.1rem;">FN ❌<br><span style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.78rem;font-weight:400;">Missed!</span></div>
        <div style="background:{MID};color:{GOLD};-webkit-text-fill-color:{GOLD};font-weight:700;text-align:center;padding:10px 8px;border-radius:0 0 0 8px;font-size:0.85rem;">Actual:<br>NO DEFAULT</div>
        <div style="background:rgba(220,53,69,0.12);border:2px solid {RED};border-radius:8px;text-align:center;padding:15px;color:{RED};-webkit-text-fill-color:{RED};font-weight:700;font-size:1.1rem;">FP ❌<br><span style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.78rem;font-weight:400;">False Alarm</span></div>
        <div style="background:rgba(40,167,69,0.15);border:2px solid {GRN};border-radius:8px;text-align:center;padding:15px;color:{GRN};-webkit-text-fill-color:{GRN};font-weight:700;font-size:1.1rem;">TN ✅<br><span style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.78rem;font-weight:400;">Correct Clear</span></div>
    </div>
    """)

    mp_insight("Key Insight", "Not all errors are equal! A <b>False Negative</b> (missing a defaulter) is far more <b>dangerous</b> than a <b>False Positive</b> (wrongly flagging a good customer). Understanding the <em>type</em> of error matters enormously.")


# ══════════════════════════════════════════════════════════════
# PAGE: TYPE I & II ERRORS
# ══════════════════════════════════════════════════════════════

elif page == "2️⃣ Type I & II Errors":
    mp_header("Type I and Type II Errors", "Classical statistical error types mapped to FP and FN")

    c1, c2 = st.columns(2)
    with c1:
        st.html(f"""
        <div style="background:{CARD};border:2px solid {RED};border-radius:14px;padding:22px;min-height:280px;user-select:none;">
            <div style="color:{RED};-webkit-text-fill-color:{RED};font-family:Playfair Display,serif;font-size:1.2rem;font-weight:700;">🔴 Type I Error</div>
            <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:JetBrains Mono,monospace;font-size:0.85rem;margin:10px 0;padding:8px;background:rgba(220,53,69,0.1);border-radius:6px;">= False Positive (FP)</div>
            <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.9rem;line-height:1.7;">
                <b>Definition:</b> Rejecting the null hypothesis when it is actually TRUE.<br><br>
                <b>Null hypothesis:</b> <em>"The borrower will NOT default."</em><br><br>
                <b>What happens:</b> We predict DEFAULT for a borrower who is actually <b style="color:{GRN};-webkit-text-fill-color:{GRN};">good</b>. We sound a <b>false alarm</b>.
            </div>
        </div>
        """)
    with c2:
        st.html(f"""
        <div style="background:{CARD};border:2px solid {WARN};border-radius:14px;padding:22px;min-height:280px;user-select:none;">
            <div style="color:{WARN};-webkit-text-fill-color:{WARN};font-family:Playfair Display,serif;font-size:1.2rem;font-weight:700;">🟠 Type II Error</div>
            <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:JetBrains Mono,monospace;font-size:0.85rem;margin:10px 0;padding:8px;background:rgba(255,193,7,0.1);border-radius:6px;">= False Negative (FN)</div>
            <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.9rem;line-height:1.7;">
                <b>Definition:</b> Failing to reject the null hypothesis when it is actually FALSE.<br><br>
                <b>What happens:</b> We predict NO DEFAULT for a borrower who actually <b style="color:{RED};-webkit-text-fill-color:{RED};">defaults</b>. We <b>miss the real threat</b>.
            </div>
        </div>
        """)

    mp_subheader("🔔 Everyday Analogy — Fire Alarm System")
    c1, c2 = st.columns(2)
    with c1:
        mp_card("""
        <b style="color:{};-webkit-text-fill-color:{};">Type I Error (FP):</b><br>
        The alarm goes off but there is <b>NO fire</b>.<br>
        <span style="color:{};-webkit-text-fill-color:{};">Annoying, but you are safe.</span>
        """.format(RED, RED, MUTED, MUTED), border_color=RED)
    with c2:
        mp_card("""
        <b style="color:{};-webkit-text-fill-color:{};">Type II Error (FN):</b><br>
        There <b>IS a fire</b> but the alarm stays <b>SILENT</b>.<br>
        <span style="color:{};-webkit-text-fill-color:{};">This is DANGEROUS! ⚠️</span>
        """.format(WARN, WARN, RED, RED), border_color=WARN)

    mp_insight("The Trade-Off",
        "There is always a trade-off between Type I and Type II errors. If we make the model very aggressive "
        "(flag everyone as potential defaulter), Type II errors fall but Type I errors rise. "
        "The optimal balance depends on the <b>business cost</b> of each error type.")


# ══════════════════════════════════════════════════════════════
# PAGE: CONFUSION MATRIX
# ══════════════════════════════════════════════════════════════

elif page == "3️⃣ Confusion Matrix":
    mp_header("The Confusion Matrix", "The single most important tool for understanding classifier performance")

    mp_card("The <b>Confusion Matrix</b> is a simple 2×2 table that organises the four outcomes (TP, TN, FP, FN). "
            "Every evaluation metric is derived directly from these four values.")

    mp_subheader("📊 Interactive Confusion Matrix — Enter Your Own Values")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        tp = st.number_input("True Positives (TP)", 0, 10000, 40, help="Correctly predicted defaults")
    with c2:
        fn = st.number_input("False Negatives (FN)", 0, 10000, 10, help="Missed defaults")
    with c3:
        fp = st.number_input("False Positives (FP)", 0, 10000, 20, help="False alarms")
    with c4:
        tn = st.number_input("True Negatives (TN)", 0, 10000, 130, help="Correctly cleared")

    total = tp + tn + fp + fn

    # Visual confusion matrix
    st.html(f"""
    <div style="display:grid;grid-template-columns:160px 1fr 1fr 100px;grid-template-rows:45px 1fr 1fr 45px;gap:5px;max-width:620px;margin:20px auto;user-select:none;">
        <div></div>
        <div style="background:{MID};color:{GOLD};-webkit-text-fill-color:{GOLD};font-weight:700;text-align:center;padding:10px;border-radius:10px 10px 0 0;font-size:0.9rem;">Predicted: Default</div>
        <div style="background:{MID};color:{GOLD};-webkit-text-fill-color:{GOLD};font-weight:700;text-align:center;padding:10px;border-radius:10px 10px 0 0;font-size:0.9rem;">Predicted: No Default</div>
        <div style="background:{MID};color:{LB};-webkit-text-fill-color:{LB};font-weight:600;text-align:center;padding:10px;border-radius:10px 10px 0 0;font-size:0.8rem;">Total</div>

        <div style="background:{MID};color:{GOLD};-webkit-text-fill-color:{GOLD};font-weight:700;text-align:center;padding:16px 8px;border-radius:10px 0 0 0;font-size:0.9rem;">Actual:<br>Default</div>
        <div style="background:rgba(40,167,69,0.18);border:2px solid {GRN};border-radius:10px;text-align:center;padding:16px;">
            <div style="color:{GRN};-webkit-text-fill-color:{GRN};font-family:JetBrains Mono,monospace;font-size:1.8rem;font-weight:700;">{tp}</div>
            <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.78rem;">TP ✅</div>
        </div>
        <div style="background:rgba(220,53,69,0.12);border:2px solid {RED};border-radius:10px;text-align:center;padding:16px;">
            <div style="color:{RED};-webkit-text-fill-color:{RED};font-family:JetBrains Mono,monospace;font-size:1.8rem;font-weight:700;">{fn}</div>
            <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.78rem;">FN ❌</div>
        </div>
        <div style="background:rgba(173,216,230,0.08);border-radius:10px;text-align:center;padding:16px;">
            <div style="color:{LB};-webkit-text-fill-color:{LB};font-family:JetBrains Mono,monospace;font-size:1.4rem;font-weight:600;">{tp+fn}</div>
        </div>

        <div style="background:{MID};color:{GOLD};-webkit-text-fill-color:{GOLD};font-weight:700;text-align:center;padding:16px 8px;border-radius:0 0 0 10px;font-size:0.9rem;">Actual:<br>No Default</div>
        <div style="background:rgba(220,53,69,0.12);border:2px solid {RED};border-radius:10px;text-align:center;padding:16px;">
            <div style="color:{RED};-webkit-text-fill-color:{RED};font-family:JetBrains Mono,monospace;font-size:1.8rem;font-weight:700;">{fp}</div>
            <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.78rem;">FP ❌</div>
        </div>
        <div style="background:rgba(40,167,69,0.18);border:2px solid {GRN};border-radius:10px;text-align:center;padding:16px;">
            <div style="color:{GRN};-webkit-text-fill-color:{GRN};font-family:JetBrains Mono,monospace;font-size:1.8rem;font-weight:700;">{tn}</div>
            <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.78rem;">TN ✅</div>
        </div>
        <div style="background:rgba(173,216,230,0.08);border-radius:10px;text-align:center;padding:16px;">
            <div style="color:{LB};-webkit-text-fill-color:{LB};font-family:JetBrains Mono,monospace;font-size:1.4rem;font-weight:600;">{fp+tn}</div>
        </div>

        <div></div>
        <div style="background:rgba(173,216,230,0.08);border-radius:0 0 10px 10px;text-align:center;padding:10px;">
            <div style="color:{LB};-webkit-text-fill-color:{LB};font-family:JetBrains Mono,monospace;font-size:1rem;font-weight:600;">{tp+fp}</div>
        </div>
        <div style="background:rgba(173,216,230,0.08);border-radius:0 0 10px 10px;text-align:center;padding:10px;">
            <div style="color:{LB};-webkit-text-fill-color:{LB};font-family:JetBrains Mono,monospace;font-size:1rem;font-weight:600;">{fn+tn}</div>
        </div>
        <div style="background:rgba(255,215,0,0.12);border-radius:0 0 10px 10px;text-align:center;padding:10px;">
            <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:JetBrains Mono,monospace;font-size:1.1rem;font-weight:700;">{total}</div>
        </div>
    </div>
    """)

    mp_subheader("📖 Reading the Matrix")
    mp_success(f"Correct Predictions", f"<b>{tp}</b> actual defaulters correctly caught (TP) + <b>{tn}</b> good borrowers correctly cleared (TN) = <b>{tp+tn}</b> correct")
    mp_warning(f"Errors", f"<b>{fp}</b> good borrowers wrongly flagged (FP — Type I) + <b>{fn}</b> defaulters missed (FN — Type II) = <b>{fp+fn}</b> errors")


# ══════════════════════════════════════════════════════════════
# PAGE: KEY METRICS CALCULATOR
# ══════════════════════════════════════════════════════════════

elif page == "4️⃣ Key Metrics Calculator":
    mp_header("Key Metrics Calculator", "All metrics derived from TP, TN, FP, FN — with live computation")

    mp_subheader("📝 Enter Confusion Matrix Values")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        tp = st.number_input("TP", 0, 100000, 85, key="m_tp")
    with c2:
        fn = st.number_input("FN", 0, 100000, 15, key="m_fn")
    with c3:
        fp = st.number_input("FP", 0, 100000, 20, key="m_fp")
    with c4:
        tn = st.number_input("TN", 0, 100000, 130, key="m_tn")

    m = compute_metrics(tp, tn, fp, fn)

    # Metric cards row 1
    mp_subheader("🎯 Core Metrics")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Accuracy", f"{m['accuracy']:.2%}")
        mp_formula("Formula", "(TP + TN) / Total", "Overall correctness of all predictions")
    with c2:
        st.metric("Precision (PPV)", f"{m['precision']:.2%}")
        mp_formula("Formula", "TP / (TP + FP)", "Trust in positive predictions — when model says 'default', how often is it right?")
    with c3:
        st.metric("Recall / Sensitivity", f"{m['recall']:.2%}")
        mp_formula("Formula", "TP / (TP + FN)", "Coverage of actual positives — what % of real defaulters does the model catch?")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Specificity (TNR)", f"{m['specificity']:.2%}")
        mp_formula("Formula", "TN / (TN + FP)", "Coverage of actual negatives")
    with c2:
        st.metric("F1 Score", f"{m['f1_score']:.2%}")
        mp_formula("Formula", "2 × P × R / (P + R)", "Harmonic mean balancing Precision & Recall")
    with c3:
        st.metric("False Positive Rate", f"{m['fpr']:.2%}")
        mp_formula("Formula", "FP / (FP + TN) = 1 − Specificity", "False alarm rate")

    # Additional metrics
    mp_subheader("📊 Extended Metrics")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("NPV", f"{m['npv']:.2%}")
    with c2:
        st.metric("FDR", f"{m['fdr']:.2%}")
    with c3:
        st.metric("Balanced Accuracy", f"{m['balanced_accuracy']:.2%}")
    with c4:
        st.metric("MCC", f"{m['mcc']:.4f}")

    mp_warning("The Accuracy Trap",
        "Accuracy can be <b>misleading</b> with imbalanced data! If only 5 of 200 borrowers default, a model that "
        "ALWAYS predicts 'no default' achieves 195/200 = <b>97.5% accuracy</b> — yet catches <b>ZERO</b> defaulters!")

    mp_insight("Precision vs Recall — The Trade-off",
        "<b style='color:{};-webkit-text-fill-color:{}'>High Precision, Low Recall:</b> Conservative model — when it flags, it's usually right, but misses many.<br>"
        "<b style='color:{};-webkit-text-fill-color:{}'>High Recall, Low Precision:</b> Aggressive model — catches most defaulters, but also flags many good borrowers.".format(GRN, GRN, WARN, WARN))

    # Metrics radar chart
    mp_subheader("📈 Metrics Radar Chart")
    categories = ['Accuracy', 'Precision', 'Recall', 'Specificity', 'F1 Score', 'Balanced Acc.']
    values = [m['accuracy'], m['precision'], m['recall'], m['specificity'], m['f1_score'], m['balanced_accuracy']]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor='rgba(255,215,0,0.12)',
        line=dict(color=GOLD, width=2.5),
        marker=dict(size=8, color=GOLD),
        name='Model'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1], tickfont=dict(color=MUTED, size=10),
                           gridcolor="rgba(136,146,176,0.15)"),
            angularaxis=dict(tickfont=dict(color=TXT, size=12, family="Source Sans 3"),
                            gridcolor="rgba(136,146,176,0.15)"),
            bgcolor="rgba(17,34,64,0.4)"
        ),
        paper_bgcolor="rgba(17,34,64,0.85)",
        font=dict(family="Source Sans 3", color=TXT),
        height=450,
        margin=dict(l=60, r=60, t=30, b=30),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════
# PAGE: ROC CURVE & AUC
# ══════════════════════════════════════════════════════════════

elif page == "5️⃣ ROC Curve & AUC":
    mp_header("ROC Curve & AUC", "Visualising model performance across all thresholds")

    mp_card("""
    Most classification models output a <b style="color:{};-webkit-text-fill-color:{};">probability</b>
    (e.g., "this borrower has a 73% chance of defaulting"). We then choose a
    <b style="color:{};-webkit-text-fill-color:{};">threshold</b> above which we classify as "default".
    The ROC curve shows performance at <b>every</b> threshold.
    """.format(GOLD, GOLD, LB, LB))

    mp_subheader("🎛️ Interactive ROC Curve — Adjust Model Quality")

    auc_target = st.slider("Model Quality (AUC)", 0.50, 1.00, 0.85, 0.01)

    # Generate ROC curve data
    np.random.seed(42)
    n_points = 500
    if auc_target >= 0.99:
        fpr_vals = np.array([0, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0])
        tpr_vals = np.array([0, 0.9, 0.95, 0.97, 0.99, 0.995, 0.999, 1.0])
    else:
        spread = 2 * (auc_target - 0.5)
        x = np.linspace(0, 1, n_points)
        fpr_vals = x
        tpr_vals = np.clip(x + spread * np.sqrt(x * (1-x)) * 2 + spread * x * 0.3, 0, 1)
        tpr_vals[0] = 0
        tpr_vals[-1] = 1
        tpr_vals = np.sort(tpr_vals)

    actual_auc = np.trapz(tpr_vals, fpr_vals)

    # Determine quality label
    if actual_auc >= 0.90: qlabel, qcolor = "⭐ Excellent", GRN
    elif actual_auc >= 0.80: qlabel, qcolor = "👍 Good", "#17a2b8"
    elif actual_auc >= 0.70: qlabel, qcolor = "👌 Fair", WARN
    elif actual_auc >= 0.60: qlabel, qcolor = "⚠️ Poor", "#fd7e14"
    else: qlabel, qcolor = "❌ Fail", RED

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("AUC", f"{actual_auc:.3f}")
    with c2:
        st.metric("Quality", qlabel)
    with c3:
        st.metric("Interpretation", f"{actual_auc:.0%} discrimination")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0,1], y=[0,1], mode='lines', name='Random (AUC=0.5)',
                            line=dict(color=MUTED, dash='dash', width=1.5)))
    fig.add_trace(go.Scatter(x=fpr_vals, y=tpr_vals, mode='lines', name=f'Model (AUC={actual_auc:.3f})',
                            fill='tozeroy', fillcolor='rgba(255,215,0,0.08)',
                            line=dict(color=GOLD, width=3)))
    fig = plotly_theme(fig, "ROC Curve — Receiver Operating Characteristic", 450)
    fig.update_xaxes(title="False Positive Rate (FPR)", range=[0,1])
    fig.update_yaxes(title="True Positive Rate (Recall)", range=[0,1])
    st.plotly_chart(fig, use_container_width=True)

    mp_insight("AUC in Plain English",
        f"An AUC of <b>{actual_auc:.2f}</b> means: if you randomly pick one actual defaulter and one actual non-defaulter, "
        f"there is a <b>{actual_auc:.0%}</b> chance the model assigns a <em>higher</em> probability of default to the actual defaulter.")

    mp_subheader("🏆 AUC Quality Ranges")
    ranges = [
        ("0.90 – 1.00", "⭐ Excellent", GRN),
        ("0.80 – 0.90", "👍 Good", "#17a2b8"),
        ("0.70 – 0.80", "👌 Fair / Acceptable", WARN),
        ("0.60 – 0.70", "⚠️ Poor", "#fd7e14"),
        ("0.50 – 0.60", "❌ Fail", RED),
    ]
    cols = st.columns(5)
    for col, (rng, label, color) in zip(cols, ranges):
        with col:
            st.html(f"""
            <div style="background:{CARD};border-top:3px solid {color};border-radius:10px;padding:14px;text-align:center;user-select:none;">
                <div style="color:{color};-webkit-text-fill-color:{color};font-family:JetBrains Mono,monospace;font-size:0.85rem;font-weight:600;">{rng}</div>
                <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.82rem;margin-top:6px;">{label}</div>
            </div>
            """)


# ══════════════════════════════════════════════════════════════
# PAGE: THRESHOLD TUNING LAB
# ══════════════════════════════════════════════════════════════

elif page == "6️⃣ Threshold Tuning Lab":
    mp_header("Threshold Tuning Lab", "See how changing the classification threshold affects every metric")

    mp_card("""
    The default threshold of <b>0.50</b> is not always optimal. This lab lets you see how
    <b style="color:{};-webkit-text-fill-color:{};">Precision</b>,
    <b style="color:{};-webkit-text-fill-color:{};">Recall</b>, and
    <b style="color:{};-webkit-text-fill-color:{};">F1 Score</b>
    change as you move the threshold.
    """.format(GRN, GRN, "#17a2b8", "#17a2b8", GOLD, GOLD))

    # Use data from Excel File 2
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    precision_v = [0.65, 0.72, 0.78, 0.80, 0.8095, 0.85, 0.89, 0.93, 0.97]
    recall_v    = [0.98, 0.95, 0.92, 0.88, 0.85,   0.78, 0.68, 0.52, 0.30]
    f1_v        = [0.7816, 0.8192, 0.8442, 0.8381, 0.8293, 0.8135, 0.7710, 0.6670, 0.4583]

    thresh = st.slider("Classification Threshold", 0.10, 0.90, 0.50, 0.10,
                       help="Move slider to see how metrics change")

    idx = thresholds.index(thresh)
    p_val, r_val, f_val = precision_v[idx], recall_v[idx], f1_v[idx]

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Precision", f"{p_val:.2%}")
    with c2:
        st.metric("Recall", f"{r_val:.2%}")
    with c3:
        st.metric("F1 Score", f"{f_val:.2%}")

    # Plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=thresholds, y=precision_v, name='Precision',
                            line=dict(color=GRN, width=3), mode='lines+markers',
                            marker=dict(size=8)))
    fig.add_trace(go.Scatter(x=thresholds, y=recall_v, name='Recall',
                            line=dict(color="#17a2b8", width=3), mode='lines+markers',
                            marker=dict(size=8)))
    fig.add_trace(go.Scatter(x=thresholds, y=f1_v, name='F1 Score',
                            line=dict(color=GOLD, width=3), mode='lines+markers',
                            marker=dict(size=8)))
    # Vertical line at current threshold
    fig.add_vline(x=thresh, line_dash="dot", line_color=RED, line_width=2,
                  annotation_text=f"Threshold = {thresh}", annotation_font_color=RED)
    fig = plotly_theme(fig, "Precision, Recall & F1 vs Classification Threshold", 430)
    fig.update_xaxes(title="Threshold", dtick=0.1)
    fig.update_yaxes(title="Metric Value", range=[0.2, 1.05])
    st.plotly_chart(fig, use_container_width=True)

    # PR Curve
    mp_subheader("📉 Precision-Recall Curve")
    fig_pr = go.Figure()
    fig_pr.add_trace(go.Scatter(x=recall_v, y=precision_v, mode='lines+markers',
                               line=dict(color=GOLD, width=3),
                               marker=dict(size=8, color=GOLD),
                               text=[f"Threshold={t}" for t in thresholds],
                               hovertemplate="Recall: %{x:.2%}<br>Precision: %{y:.2%}<br>%{text}"))
    # Highlight current
    fig_pr.add_trace(go.Scatter(x=[r_val], y=[p_val], mode='markers',
                               marker=dict(size=16, color=RED, symbol='star'),
                               name=f'Current (t={thresh})', showlegend=True))
    fig_pr = plotly_theme(fig_pr, "Precision-Recall Curve", 400)
    fig_pr.update_xaxes(title="Recall", range=[0.2, 1.05])
    fig_pr.update_yaxes(title="Precision", range=[0.6, 1.02])
    st.plotly_chart(fig_pr, use_container_width=True)

    # Scenario guidance
    mp_subheader("🎯 Practical Threshold Selection")
    c1, c2 = st.columns(2)
    with c1:
        mp_card("""
        <b style="color:{};-webkit-text-fill-color:{};">🏦 Scenario 1: Loan Approval</b><br><br>
        <b>Cost:</b> Missing a defaulter = loan loss<br>
        <b>Goal:</b> Maximise RECALL<br>
        <b>Action:</b> ⬇️ LOWER threshold (e.g., 0.30)<br>
        <span style="color:{};-webkit-text-fill-color:{};">Accept more false alarms to catch more defaults</span>
        """.format(GOLD, GOLD, MUTED, MUTED), border_color="#17a2b8")
    with c2:
        mp_card("""
        <b style="color:{};-webkit-text-fill-color:{};">📧 Scenario 2: Spam Filter</b><br><br>
        <b>Cost:</b> Blocking legit email = missed opportunity<br>
        <b>Goal:</b> High PRECISION<br>
        <b>Action:</b> ⬆️ RAISE threshold (e.g., 0.80)<br>
        <span style="color:{};-webkit-text-fill-color:{};">Only flag when very confident it's spam</span>
        """.format(GOLD, GOLD, MUTED, MUTED), border_color=GRN)


# ══════════════════════════════════════════════════════════════
# PAGE: ADVANCED METRICS
# ══════════════════════════════════════════════════════════════

elif page == "7️⃣ Advanced Metrics":
    mp_header("Advanced Metrics", "F-beta Score, Matthews Correlation Coefficient (MCC), and Log Loss")

    tabs = st.tabs(["📊 F-beta Score", "🧠 MCC", "📉 Log Loss"])

    with tabs[0]:
        mp_subheader("F-beta Score — Tilting the Balance")
        mp_formula("Formula", "F_β = (1+β²) × (P×R) / (β²×P + R)",
                   "β controls the relative weight of Recall vs Precision")

        beta_data = [
            ("β = 0.5", "F0.5 Score", "Weights PRECISION higher", "Use when false alarms are costly (spam, trading)", WARN),
            ("β = 1", "F1 Score", "Equal weight", "Standard balanced metric (churn prediction)", GOLD),
            ("β = 2", "F2 Score", "Weights RECALL higher", "Use when missing positives is costly (credit, AML)", "#17a2b8"),
        ]
        cols = st.columns(3)
        for col, (bval, name, weight, use, color) in zip(cols, beta_data):
            with col:
                st.html(f"""
                <div style="background:{CARD};border-top:3px solid {color};border-radius:12px;padding:18px;text-align:center;min-height:170px;user-select:none;">
                    <div style="color:{color};-webkit-text-fill-color:{color};font-family:JetBrains Mono,monospace;font-size:1rem;font-weight:700;">{bval}</div>
                    <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-size:1rem;font-weight:600;margin:6px 0;">{name}</div>
                    <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.85rem;">{weight}</div>
                    <div style="color:{MUTED};-webkit-text-fill-color:{MUTED};font-size:0.8rem;margin-top:6px;">{use}</div>
                </div>
                """)

        # Interactive F-beta calculator
        mp_subheader("🎛️ F-beta Calculator")
        c1, c2, c3 = st.columns(3)
        with c1:
            p_in = st.slider("Precision", 0.01, 1.00, 0.81, 0.01, key="fb_p")
        with c2:
            r_in = st.slider("Recall", 0.01, 1.00, 0.85, 0.01, key="fb_r")
        with c3:
            b_in = st.slider("Beta (β)", 0.1, 3.0, 1.0, 0.1, key="fb_b")

        fbeta = (1 + b_in**2) * (p_in * r_in) / (b_in**2 * p_in + r_in)
        st.metric(f"F{b_in:.1f} Score", f"{fbeta:.4f}")

        # Plot F-beta across beta values
        betas = np.arange(0.1, 3.1, 0.1)
        fb_vals = [(1 + b**2) * (p_in * r_in) / (b**2 * p_in + r_in) for b in betas]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=betas, y=fb_vals, mode='lines', line=dict(color=GOLD, width=3),
                                name='F-beta'))
        fig.add_vline(x=b_in, line_dash="dot", line_color=RED, line_width=2)
        fig = plotly_theme(fig, f"F-beta Score (P={p_in:.2f}, R={r_in:.2f}) across β values", 360)
        fig.update_xaxes(title="β value")
        fig.update_yaxes(title="F-beta Score")
        st.plotly_chart(fig, use_container_width=True)

    with tabs[1]:
        mp_subheader("Matthews Correlation Coefficient (MCC)")
        mp_formula("Formula", "MCC = (TP·TN − FP·FN) / √[(TP+FP)(TP+FN)(TN+FP)(TN+FN)]",
                   "Ranges from −1 to +1. Uses all four confusion matrix values.")

        ranges_mcc = [
            ("+1", "Perfect prediction", GRN),
            ("0", "No better than random", WARN),
            ("−1", "Total disagreement", RED),
        ]
        cols = st.columns(3)
        for col, (val, desc, color) in zip(cols, ranges_mcc):
            with col:
                st.html(f"""
                <div style="background:{CARD};border-left:4px solid {color};border-radius:10px;padding:16px;text-align:center;user-select:none;">
                    <div style="color:{color};-webkit-text-fill-color:{color};font-family:JetBrains Mono,monospace;font-size:1.4rem;font-weight:700;">{val}</div>
                    <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-size:0.85rem;margin-top:4px;">{desc}</div>
                </div>
                """)

        mp_subheader("🧮 MCC Calculator")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            mtp = st.number_input("TP", 0, 10000, 85, key="mcc_tp")
        with c2:
            mfn = st.number_input("FN", 0, 10000, 15, key="mcc_fn")
        with c3:
            mfp = st.number_input("FP", 0, 10000, 20, key="mcc_fp")
        with c4:
            mtn = st.number_input("TN", 0, 10000, 130, key="mcc_tn")

        denom = np.sqrt((mtp+mfp)*(mtp+mfn)*(mtn+mfp)*(mtn+mfn))
        mcc_val = (mtp*mtn - mfp*mfn) / denom if denom > 0 else 0
        st.metric("MCC", f"{mcc_val:.4f}")

        mp_insight("Why MCC is Considered One of the Best Metrics",
            "MCC uses <b>all four</b> confusion matrix values. Unlike Accuracy, it cannot be fooled by class imbalance. "
            "A model that always predicts the majority class gets MCC ≈ 0, correctly reflecting its uselessness.")

    with tabs[2]:
        mp_subheader("Log Loss (Cross-Entropy Loss)")
        mp_formula("Formula", "Log Loss = −(1/N) Σ [yᵢ·ln(p̂ᵢ) + (1−yᵢ)·ln(1−p̂ᵢ)]",
                   "Evaluates the quality of probability estimates, not just labels")

        mp_card("""
        Unlike metrics above, Log Loss penalises <b>confidently wrong</b> predictions heavily.<br><br>
        <b style="color:{};-webkit-text-fill-color:{};">Example:</b> A model predicts 0.95 probability of "no default" for a borrower who
        actually defaults. The Log Loss penalty for this single prediction is extremely high because
        the model was <b>very confident AND very wrong</b>.
        """.format(GOLD, GOLD))

        mp_subheader("🔬 See Log Loss Penalty in Action")
        pred_prob = st.slider("Predicted Probability (p̂) for an actual POSITIVE case", 0.01, 0.99, 0.50, 0.01)
        loss = -np.log(pred_prob)
        st.metric("Log Loss Contribution", f"{loss:.4f}")

        probs = np.linspace(0.01, 0.99, 100)
        losses = -np.log(probs)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=probs, y=losses, mode='lines', line=dict(color=GOLD, width=3)))
        fig.add_trace(go.Scatter(x=[pred_prob], y=[loss], mode='markers',
                                marker=dict(size=14, color=RED, symbol='star'), name='Current'))
        fig = plotly_theme(fig, "Log Loss Penalty for Actual Positive (y=1)", 380)
        fig.update_xaxes(title="Predicted Probability p̂")
        fig.update_yaxes(title="−ln(p̂) = Loss")
        st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════
# PAGE: FINANCE APPLICATIONS
# ══════════════════════════════════════════════════════════════

elif page == "8️⃣ Finance Applications":
    mp_header("Application in Finance & Risk Management", "Which metric matters for which financial use case?")

    apps = [
        ("🏦", "Credit Default Prediction", "Recall / F2", "Missing a defaulter is costly (loan loss). Must catch as many as possible.", "#17a2b8"),
        ("🔍", "Fraud Detection", "Recall + Precision", "Must catch fraud but not block legitimate transactions.", GOLD),
        ("🚨", "Anti-Money Laundering", "Recall", "Regulatory risk of missing suspicious activity. Compliance is paramount.", RED),
        ("📉", "Customer Churn", "F1 Score", "Balanced view of retention targeting — catch churners without wasting resources.", GRN),
        ("📈", "Algorithmic Trading Signals", "Precision", "False buy/sell signals erode capital. Only act when very confident.", WARN),
        ("🛡️", "Insurance Claim Fraud", "AUC / F1", "Need overall discriminative power across all thresholds.", "#fd7e14"),
        ("🏛️", "Basel IRB (PD Estimation)", "AUC + Calibration", "Regulatory requirement for discriminative power AND accuracy of PD estimates.", LB),
    ]

    for icon, app, metric, why, color in apps:
        st.html(f"""
        <div style="background:{CARD};border-left:4px solid {color};border-radius:10px;padding:16px 20px;margin:8px 0;display:flex;align-items:flex-start;gap:16px;user-select:none;">
            <div style="font-size:1.8rem;min-width:36px;text-align:center;">{icon}</div>
            <div style="flex:1;">
                <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-family:Playfair Display,serif;font-size:1.05rem;font-weight:600;">{app}</div>
                <div style="color:{color};-webkit-text-fill-color:{color};font-family:JetBrains Mono,monospace;font-size:0.85rem;margin:4px 0;">Key Metric: {metric}</div>
                <div style="color:{MUTED};-webkit-text-fill-color:{MUTED};font-size:0.85rem;line-height:1.5;">{why}</div>
            </div>
        </div>
        """)

    mp_insight("Key Principle",
        "There is <b>no single 'best' metric</b> — context determines which matters most. "
        "Always choose metrics based on the <b>business cost</b> of each type of error.")

    # Decision flowchart as visual
    mp_subheader("📊 Decision Flowchart — Which Metric to Use?")
    fig = go.Figure()
    # Nodes
    nodes_x = [0.5, 0.5, 0.85, 0.5, 0.85, 0.5, 0.5]
    nodes_y = [0.95, 0.75, 0.75, 0.55, 0.55, 0.35, 0.18]
    labels = ["Binary Classification\nProblem", "Is dataset\nbalanced?", "Accuracy is\nmeaningful",
              "Is FP more\ncostly?", "Focus on\nPRECISION", "Focus on\nRECALL", "Use F1 /\nF-beta"]
    colors = [MID, GOLD, GRN, GOLD, GRN, "#17a2b8", GOLD]

    for x, y, lbl, clr in zip(nodes_x, nodes_y, labels, colors):
        fig.add_shape(type="rect", x0=x-0.13, y0=y-0.06, x1=x+0.13, y1=y+0.06,
                     fillcolor=CARD, line=dict(color=clr, width=2))
        fig.add_annotation(x=x, y=y, text=lbl, showarrow=False,
                          font=dict(color=TXT, size=11, family="Source Sans 3"))

    # Arrows
    arrows = [(0.5,0.89,0.5,0.81), (0.63,0.75,0.72,0.75), (0.5,0.69,0.5,0.61),
              (0.63,0.55,0.72,0.55), (0.5,0.49,0.5,0.41), (0.5,0.29,0.5,0.24)]
    arrow_labels = ["", "Yes", "", "Yes", "No (FN costly)", ""]
    for (x0,y0,x1,y1), lbl in zip(arrows, arrow_labels):
        fig.add_annotation(x=x1, y=y1, ax=x0, ay=y0, xref="x", yref="y", axref="x", ayref="y",
                          showarrow=True, arrowhead=3, arrowsize=1.5, arrowwidth=2, arrowcolor=MUTED,
                          text=lbl, font=dict(color=LB, size=10))

    fig.update_layout(
        xaxis=dict(range=[0,1.1], visible=False),
        yaxis=dict(range=[0.05,1.05], visible=False),
        paper_bgcolor="rgba(17,34,64,0.85)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=520, margin=dict(l=10, r=10, t=10, b=10)
    )
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════
# PAGE: Q&A PRACTICE
# ══════════════════════════════════════════════════════════════

elif page == "9️⃣ Q&A Practice":
    mp_header("Q&A Practice — Self-Assessment", "Test your understanding with 25 questions across 4 sections")

    mp_card("💡 Try answering each question in your head <b>before</b> expanding to see the answer. "
            "This active recall technique dramatically improves retention.")

    sections = {
        "Section A: Conceptual Foundations": [
            ("Q1", "Why is it not enough to simply say \"the model is good\"? What do we need instead?",
             "We need concrete, quantifiable metrics that tell us how often the model is right, what kind of mistakes it makes, and whether it is better at catching positives or avoiding false alarms. In finance, wrong predictions have real, measurable costs."),
            ("Q2", "In a binary classifier predicting loan default, what are the four possible outcomes?",
             "<b>TP:</b> Predicted default, actually defaulted (correct alarm).<br><b>TN:</b> Predicted no default, didn't default (correct quiet).<br><b>FP:</b> Predicted default, didn't default (false alarm).<br><b>FN:</b> Predicted no default, actually defaulted (missed alarm)."),
            ("Q3", "What is a Type I Error? Give the statistical definition and a practical example.",
             "Type I Error = Rejecting the null hypothesis when it is actually true = <b>False Positive (FP)</b>. Example: A fire alarm goes off when there is no fire. In lending, flagging a good borrower as a defaulter."),
            ("Q4", "What is a Type II Error? Why is it often considered more dangerous?",
             "Type II Error = Failing to reject the null hypothesis when it is false = <b>False Negative (FN)</b>. It's often more dangerous because the real threat goes undetected — like a fire alarm staying silent during a fire, or a bank missing a borrower who will default."),
            ("Q5", "What is the Confusion Matrix? Why is it the 'foundation' of model evaluation?",
             "The Confusion Matrix is a 2×2 table organising TP, TN, FP, and FN counts. It is the foundation because <b>every single evaluation metric</b> (Accuracy, Precision, Recall, F1, etc.) is derived directly from these four values."),
        ],
        "Section B: Metrics & Calculations": [
            ("Q6", "Given TP=40, TN=130, FP=20, FN=10, calculate Accuracy. What does it mean?",
             "Accuracy = (40+130)/(200) = 170/200 = <b>85%</b>. It means 85% of all predictions were correct."),
            ("Q7", "What is the 'Accuracy Trap'? Give an example.",
             "With imbalanced data, accuracy is misleading. If only 5 of 200 borrowers default, a model that ALWAYS predicts 'no default' achieves 195/200 = <b>97.5% accuracy</b> — yet catches <b>zero</b> defaulters!"),
            ("Q8", "Calculate Precision from TP=40, FP=20. What question does Precision answer?",
             "Precision = 40/(40+20) = 40/60 = <b>66.7%</b>. It answers: 'Of all borrowers the model flagged as defaulters, how many actually defaulted?'"),
            ("Q9", "Calculate Recall from TP=40, FN=10. How does it differ from Precision?",
             "Recall = 40/(40+10) = 40/50 = <b>80%</b>. While Precision asks about positive predictions, Recall asks: 'Of all who actually defaulted, how many did the model catch?'"),
            ("Q10", "Why does the F1 Score use the harmonic mean instead of the arithmetic mean?",
             "The harmonic mean penalises extreme imbalances. Precision=1.0, Recall=0.01 → Arithmetic mean = 0.505 (looks decent), but F1 = 0.0198 (terrible!). The harmonic mean correctly reveals the model is useless."),
            ("Q11", "What is Specificity? How does it relate to FPR?",
             "Specificity = TN/(TN+FP) = 130/150 = <b>86.7%</b>. FPR = 1 − Specificity = 13.3%. As Specificity increases, the false alarm rate decreases."),
            ("Q12", "Explain the Precision-Recall trade-off with aggressive vs conservative models.",
             "<b>Aggressive (low threshold):</b> High Recall, Low Precision — catches most defaulters but flags many good borrowers.<br><b>Conservative (high threshold):</b> High Precision, Low Recall — when it flags, it's usually right, but misses many."),
        ],
        "Section C: Advanced Topics & Curves": [
            ("Q13", "What does the ROC curve plot? What does each point represent?",
             "ROC plots <b>TPR (Recall)</b> vs <b>FPR</b> at every possible threshold from 0 to 1. Each point represents a different trade-off between catching defaulters and false alarms at a specific threshold."),
            ("Q14", "What does an AUC of 0.85 mean in plain English?",
             "If you randomly pick one actual defaulter and one non-defaulter, there is an <b>85% chance</b> the model assigns a higher default probability to the actual defaulter."),
            ("Q15", "When should you use a PR Curve instead of ROC?",
             "Use PR Curve when the <b>positive class is rare</b> (fraud, default, disease). It ignores the large number of true negatives, giving a more informative picture for imbalanced datasets."),
            ("Q16", "Why is threshold 0.50 not always optimal? Give two scenarios.",
             "<b>Bank loan:</b> Missing defaulters is costly → lower threshold to ~0.30 to maximise Recall.<br><b>Spam filter:</b> Blocking legit email is costly → raise threshold to ~0.80 to maximise Precision."),
            ("Q17", "What is MCC and why is it great for imbalanced datasets?",
             "MCC ranges from −1 to +1 and uses <b>all four</b> confusion matrix values. Unlike Accuracy, it can't be fooled by class imbalance. +1 = perfect, 0 = random, −1 = total disagreement."),
            ("Q18", "How does Log Loss differ from other metrics?",
             "Log Loss evaluates <b>probability estimate quality</b>, not just labels. A prediction of 0.95 for a non-defaulter receives a much heavier penalty than 0.55, because the model was very confident yet completely wrong."),
        ],
        "Section D: Application & Scenario-Based": [
            ("Q19", "A fraud system has Precision=95%, Recall=30%. Is this acceptable?",
             "When it flags fraud, it's right 95% of the time — but it only catches <b>30%</b> of actual fraud. 70% goes undetected! Likely unacceptable. Need to lower the threshold to boost Recall."),
            ("Q20", "Which metric for an AML model and why?",
             "<b>Recall.</b> The regulatory risk of missing suspicious activity is severe (fines, sanctions). Better to flag extra transactions for review than to miss actual money laundering."),
            ("Q21", "Why does algorithmic trading focus on Precision?",
             "False buy/sell signals directly erode capital. Better to miss some profitable trades (lower Recall) than to act on bad signals (lower Precision)."),
            ("Q22", "A model has AUC = 0.52. What does this tell you?",
             "AUC 0.52 is barely better than random (0.50). The model has essentially <b>no discriminating ability</b>. Investigate features, try different algorithms, check data quality. Do NOT deploy."),
            ("Q23", "Difference between F1, F2, and F0.5 scores?",
             "<b>F1:</b> Equal weight (balanced).<br><b>F2:</b> Weights Recall higher (missing positives is costly).<br><b>F0.5:</b> Weights Precision higher (false alarms are costly)."),
            ("Q24", "1,000 applicants, 20 actual defaults. Model predicts 'no default' for everyone. Calculate Accuracy, Recall, Precision.",
             "Accuracy = 980/1000 = <b>98%</b>. Recall = 0/20 = <b>0%</b>. Precision = 0/0 = <b>undefined</b>. Classic Accuracy Trap — 98% accuracy but completely useless!"),
            ("Q25", "Basel IRB requires AUC + Calibration. Why isn't AUC enough?",
             "AUC measures <b>discrimination</b> (ranking), not <b>calibration</b> (probability accuracy). A model could rank perfectly (AUC=1.0) but predict 50% PD when true rate is 2%. Regulators need both for capital calculations."),
        ]
    }

    for section_name, questions in sections.items():
        mp_subheader(section_name)
        for qid, question, answer in questions:
            with st.expander(f"**{qid}:** {question}"):
                st.html(f"""
                <div style="color:{TXT};-webkit-text-fill-color:{TXT};font-family:Source Sans 3,sans-serif;font-size:0.92rem;line-height:1.75;padding:4px 0;">
                    {answer}
                </div>
                """)


# ══════════════════════════════════════════════════════════════
# FOOTER (all pages)
# ══════════════════════════════════════════════════════════════

st.html(f"""
<div style="text-align:center;padding:30px 0 15px 0;margin-top:40px;border-top:1px solid rgba(255,215,0,0.2);user-select:none;">
    <div style="height:2px;background:linear-gradient(90deg,transparent,{GOLD},transparent);margin:0 auto 18px auto;width:40%;"></div>
    <div style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-family:Playfair Display,serif;font-size:1.1rem;font-weight:700;">The Mountain Path Academy</div>
    <div style="color:{MUTED};-webkit-text-fill-color:{MUTED};font-size:0.78rem;margin-top:4px;">World of Finance — Prof. V. Ravichandran</div>
    <div style="color:{MUTED};-webkit-text-fill-color:{MUTED};font-size:0.72rem;margin-top:2px;">NMIMS Bangalore | BITS Pilani | RV University Bangalore | Goa Institute of Management</div>
    <div style="margin-top:10px;">
        <a href="https://themountainpathacademy.com" target="_blank" style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-size:0.82rem;text-decoration:none;font-weight:600;">themountainpathacademy.com</a>
    </div>
    <div style="margin-top:6px;">
        <a href="https://www.linkedin.com/in/trichyravis" target="_blank" style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-size:0.75rem;text-decoration:none;margin-right:12px;">LinkedIn</a>
        <a href="https://github.com/trichyravis" target="_blank" style="color:{GOLD};-webkit-text-fill-color:{GOLD};font-size:0.75rem;text-decoration:none;">GitHub</a>
    </div>
</div>
""")
