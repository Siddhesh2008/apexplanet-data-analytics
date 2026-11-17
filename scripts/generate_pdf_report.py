"""
ApexPlanet Data Analytics Internship — Executive Summary PDF Generator
Script: scripts/generate_pdf_report.py
Author: Siddhesh (Data Analytics Intern)
Organization: ApexPlanet Solutions
Description:
    Generates an exact 2-page executive summary PDF report using ReportLab.
"""

import sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
import pypdf

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PDF = BASE_DIR / "reports" / "Executive_Summary.pdf"

# Source chart paths
VIZ_DIR = BASE_DIR / "task_3_visualization" / "visualizations"
ADV_VIZ_DIR = BASE_DIR / "task_4_advanced_analytics" / "visualizations"
DASH_IMG = BASE_DIR / "dashboard" / "powerbi_dashboard_screenshot.png"

CAT_CHART = VIZ_DIR / "category_revenue.png"
MONTHLY_CHART = VIZ_DIR / "monthly_revenue.png"
CLUSTER_CHART = ADV_VIZ_DIR / "customer_clusters.png"

# Palette
PRIMARY_NAVY = colors.HexColor("#0F2C59")
SECONDARY_BLUE = colors.HexColor("#1E3A8A")
ACCENT_BLUE = colors.HexColor("#2563EB")
LIGHT_BG = colors.HexColor("#F8FAFC")
BORDER_COLOR = colors.HexColor("#CBD5E1")
TEXT_DARK = colors.HexColor("#0F172A")
TEXT_MUTED = colors.HexColor("#475569")
GREEN_ACCENT = colors.HexColor("#166534")

def build_pdf():
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    
    # Page dimensions: letter = 612 x 792 pt
    # Margins: 0.35 in (25.2 pt) left/right, 0.35 in top/bottom
    margin = 26
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=letter,
        leftMargin=margin,
        rightMargin=margin,
        topMargin=margin,
        bottomMargin=margin
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=PRIMARY_NAVY
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=ACCENT_BLUE
    )
    
    sec_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=PRIMARY_NAVY,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.2,
        textColor=TEXT_DARK
    )
    
    body_bold = ParagraphStyle(
        'BodyDarkBold',
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10.2,
        textColor=TEXT_DARK
    )
    
    meta_style = ParagraphStyle(
        'MetaText',
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.2,
        textColor=TEXT_MUTED
    )
    
    insight_title = ParagraphStyle(
        'InsightTitle',
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10,
        textColor=SECONDARY_BLUE
    )
    
    kpi_num_style = ParagraphStyle(
        'KpiNum',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=PRIMARY_NAVY,
        alignment=1
    )
    
    kpi_lbl_style = ParagraphStyle(
        'KpiLbl',
        fontName='Helvetica-Bold',
        fontSize=6.5,
        leading=8,
        textColor=TEXT_MUTED,
        alignment=1
    )
    
    story = []
    
    # =========================================================================
    # PAGE 1 — Project Overview, KPIs & Top 5 Business Insights
    # =========================================================================
    
    # Header Banner
    header_data = [
        [
            Paragraph("<b>E-COMMERCE DATA ANALYTICS — END-TO-END ANALYSIS</b>", title_style),
            Paragraph("<b>APEXPLANET SOLUTIONS</b><br/><font color='#64748B'>Data Analytics Internship | Final Executive Report</font>", ParagraphStyle('HRight', parent=meta_style, alignment=2, fontSize=7.5, leading=9.5))
        ],
        [
            Paragraph("<b>Author:</b> Siddhesh | <b>Discipline:</b> B.Tech AI & Data Science | <b>Dataset:</b> 50,000 Global Transactions ($25.16M USD)", subtitle_style),
            Paragraph("<b>Evaluation Period:</b> 30-Day Internship Portfolio", ParagraphStyle('HRightSub', parent=meta_style, alignment=2))
        ]
    ]
    header_table = Table(header_data, colWidths=[380, 180])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY_NAVY, spaceAfter=4, spaceBefore=3))
    
    # Executive Summary & Scope
    exec_summary_text = (
        "<b>Executive Summary:</b> This study presents an enterprise analytical investigation of 50,000 global e-commerce "
        "transactions totaling <b>$25.16 Million USD</b> recorded between March 2023 and March 2025. Spanning a 5-task "
        "roadmap—exploratory data hygiene, PostgreSQL relational extraction, interactive Power BI dashboarding, inferential "
        "statistics (Welch's <i>t</i>-test, Chi-square), time-series forecasting (MAPE: 3.08%), and K-means customer segmentation—"
        "this project establishes an empirical foundation for inventory, revenue velocity, and cohort retention management."
    )
    story.append(Paragraph(exec_summary_text, body_style))
    story.append(Spacer(1, 4))
    
    # Dataset Overview & KPI Cards Row
    kpi_card_data = [
        [
            Paragraph("$25.16M", kpi_num_style),
            Paragraph("50,000", kpi_num_style),
            Paragraph("$503.16", kpi_num_style),
            Paragraph("10 Markets", kpi_num_style),
            Paragraph("8 Categories", kpi_num_style),
            Paragraph("100 Cohorts", kpi_num_style),
        ],
        [
            Paragraph("GROSS REVENUE", kpi_lbl_style),
            Paragraph("ORDERS COMPLETED", kpi_lbl_style),
            Paragraph("AVERAGE TICKET", kpi_lbl_style),
            Paragraph("GLOBAL REACH", kpi_lbl_style),
            Paragraph("MERCHANDISE LINES", kpi_lbl_style),
            Paragraph("USER LABELS", kpi_lbl_style),
        ]
    ]
    kpi_table = Table(kpi_card_data, colWidths=[93, 93, 93, 93, 93, 95])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 0.75, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 4))
    
    # Dataset Overview Metadata Table
    ds_meta_data = [
        [
            Paragraph("<b>Temporal Window:</b> March 9, 2023 – March 8, 2025 (24 Full Billing Months)", meta_style),
            Paragraph("<b>Data Cleanliness:</b> 0 Missing Values (0.00%) | 0 Duplicate Rows (0.00%)", meta_style),
        ],
        [
            Paragraph("<b>Payment Channels (6):</b> Cash on Delivery, UPI, Debit Card, PayPal, Credit Card, Net Banking", meta_style),
            Paragraph("<b>Geographies (10):</b> USA, France, Canada, Mexico, Australia, Brazil, India, Germany, Japan, UK", meta_style),
        ]
    ]
    ds_meta_table = Table(ds_meta_data, colWidths=[280, 280])
    ds_meta_table.setStyle(TableStyle([
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(ds_meta_table)
    story.append(Spacer(1, 4))
    
    # Section: Top 5 Business Insights
    story.append(Paragraph("<b>TOP 5 STRATEGIC BUSINESS INSIGHTS</b>", sec_heading))
    
    insights = [
        ("1. Catalog Revenue Parity & Zero Portfolio Dependency:",
         "Revenue is exceptionally balanced across all 8 merchandising categories, led by <b>Sports ($3.20M, 12.70%)</b> "
         "and anchored by <b>Beauty ($3.06M, 12.15%)</b>. The marginal 4.5% spread proves zero vulnerability to single-category demand shocks."),
        
        ("2. Consistent Run-Rate & High-Fidelity Forecasting:",
         "Gross revenue generated a steady run-rate of <b>~$1.05M/month</b> (peaking in July 2023 at $1.11M). An additive time-series "
         "decomposition and rolling 3-month moving average achieved a <b>3.08% MAPE</b> on out-of-sample test data."),
        
        ("3. Statistical Independence of Payment Rails & Age Inelasticity:",
         "Rigorous hypothesis testing proved customer spend is independent of payment method (Welch's <i>t</i> = -1.0362, <i>p</i> = 0.3001) "
         "and category choices (Chi-square &chi;<sup>2</sup> = 34.41, <i>p</i> = 0.496). Age correlation is near zero (<i>r</i> = -0.0036)."),
        
        ("4. Senior Demographic Volume Dominance (Ages 56–70):",
         "Customers aged 56–70 drive <b>28.2% ($7.09M)</b> of total sales across 14,113 orders. This revenue dominance stems from "
         "consistently higher purchase frequency across an older demographic rather than inflated individual ticket sizes ($502.71 AOV)."),
        
        ("5. Concentrated Account Activity & Unsupervised Segmentation:",
         "The 50,000 orders map to 100 repeating customer labels (averaging 500 transactions each), led by Sophia Harris ($296.3K, 568 orders). "
         "K-Means clustering (<i>K</i>=4, silhouette = 0.398, PCA variance = 99.4%) successfully isolated distinct VIP and frequency tiers.")
    ]
    
    insight_table_data = []
    for title, desc in insights:
        p_text = f"<b>{title}</b> {desc}"
        insight_table_data.append([Paragraph(p_text, body_style)])
        
    insight_table = Table(insight_table_data, colWidths=[560])
    insight_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFFFFF")),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#F1F5F9")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(insight_table)
    story.append(Spacer(1, 5))
    
    # Visual Highlights Row (2 Actual Project Charts)
    story.append(Paragraph("<b>EMPIRICAL VISUAL HIGHLIGHTS (MATPLOTLIB & SCIKIT-LEARN)</b>", sec_heading))
    chart_row = [
        [
            Image(str(CAT_CHART), width=275, height=125),
            Image(str(CLUSTER_CHART), width=275, height=125)
        ],
        [
            Paragraph("<b>Figure 1:</b> Balanced Gross Sales by Product Category ($3.06M - $3.20M)", ParagraphStyle('Fig1', parent=meta_style, alignment=1)),
            Paragraph("<b>Figure 2:</b> 2D PCA Customer Clusters (K=4, 99.4% Variance Explained)", ParagraphStyle('Fig2', parent=meta_style, alignment=1))
        ]
    ]
    charts_table = Table(chart_row, colWidths=[280, 280])
    charts_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(charts_table)
    
    # Page 1 Footer Note
    story.append(Spacer(1, 3))
    p1_footer = Table([[
        Paragraph("<font color='#64748B'>ApexPlanet Solutions Data Analytics Internship | Task 5 Final Deliverable</font>", meta_style),
        Paragraph("<font color='#64748B'>Page 1 of 2</font>", ParagraphStyle('P1', parent=meta_style, alignment=2))
    ]], colWidths=[460, 100])
    p1_footer.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(p1_footer)
    
    # =========================================================================
    # FORCE PAGE BREAK — EXACTLY PAGE 2
    # =========================================================================
    story.append(PageBreak())
    
    # =========================================================================
    # PAGE 2 — Dashboard Screenshot, Recommendations & Conclusion
    # =========================================================================
    
    # Header Page 2
    p2_header_data = [
        [
            Paragraph("<b>EXECUTIVE DASHBOARD, STRATEGIC ROADMAP & CONCLUSION</b>", title_style),
            Paragraph("<b>APEXPLANET SOLUTIONS</b><br/><font color='#64748B'>Governance & Recommendations</font>", ParagraphStyle('H2Right', parent=meta_style, alignment=2, fontSize=7.5, leading=9.5))
        ]
    ]
    p2_header_table = Table(p2_header_data, colWidths=[380, 180])
    p2_header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(p2_header_table)
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY_NAVY, spaceAfter=4, spaceBefore=3))
    
    # Subsection: Power BI Dashboard
    story.append(Paragraph("<b>INTERACTIVE EXECUTIVE DASHBOARD ARCHITECTURE</b>", sec_heading))
    dash_desc = (
        "The Power BI dashboard integrates dynamic slicers (Month, Geography, Category, Payment Channel), dynamic DAX measures "
        "(<i>Total Sales, Total Orders, AOV, Distinct User Labels</i>), and multi-visual cross-filtering. Below is the operational "
        "dashboard interface displaying real-time aggregation across the $25.16M gross revenue base."
    )
    story.append(Paragraph(dash_desc, body_style))
    story.append(Spacer(1, 3))
    
    # Dashboard Screenshot (Height carefully budgeted to guarantee exact 2 pages)
    dash_table = Table([
        [Image(str(DASH_IMG), width=560, height=210)],
        [Paragraph("<b>Figure 3:</b> Actual Production Executive Dashboard Interface (In-Memory DAX Filtering Engine)", ParagraphStyle('Fig3', parent=meta_style, alignment=1))]
    ], colWidths=[560])
    dash_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('BOX', (0,0), (0,0), 0.75, BORDER_COLOR),
    ]))
    story.append(dash_table)
    story.append(Spacer(1, 5))
    
    # Subsection: 3 Actionable Recommendations
    story.append(Paragraph("<b>ACTIONABLE STRATEGIC RECOMMENDATIONS</b>", sec_heading))
    
    recs = [
        ("1. Cross-Category Collaborative Bundling:",
         "Capitalize on catalog spending uniformity and category independence by deploying automated recommendation engines at checkout. "
         "Cross-promoting complementary categories (e.g., Sports with Books or Apparel) will cross-subsidize baskets, lifting average order value toward $600."),
        
        ("2. Dedicated VIP Account Management Program:",
         "The top 100 customer account labels account for 100% of recorded volume, each averaging ~$250,000+ in lifetime spend. Management must introduce "
         "exclusive account concierge services, volume rebates, and custom invoicing to protect these high-lifetime-value enterprise accounts from churn."),
        
        ("3. Dual-Channel Payment Optimization (COD & Instant Digital Rails):",
         "With Cash on Delivery ($4.28M) and UPI ($4.26M) capturing equal volume, preserve COD to avoid top-of-funnel friction in developing regions, while "
         "implementing a 2.0% instant checkout incentive on digital rails to reduce physical remittance costs, return rates, and cash-handling lag.")
    ]
    
    rec_table_data = []
    for title, desc in recs:
        p_text = f"<b>{title}</b> {desc}"
        rec_table_data.append([Paragraph(p_text, body_style)])
        
    rec_table = Table(rec_table_data, colWidths=[560])
    rec_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFFFFF")),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#F1F5F9")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(rec_table)
    story.append(Spacer(1, 5))
    
    # Subsection: Project Conclusion & Analytical Limitations
    story.append(Paragraph("<b>PROJECT CONCLUSION & ANALYTICAL LIMITATIONS</b>", sec_heading))
    conclusion_text = (
        "<b>Accomplishments & Business Value:</b> Successfully executed an end-to-end analytics lifecycle from raw transactional auditing to "
        "PostgreSQL data extraction, executive visualization, statistical hypothesis verification, predictive machine learning pipelines, and "
        "headless pipeline automation. The resulting artifacts provide leadership with rigorous, audit-ready intelligence regarding product resilience "
        "and revenue predictability.<br/>"
        "<b>Dataset Limitations:</b> (1) <i>User_Name</i> reflects repeating account labels and cannot be construed as verified individual identities. "
        "(2) Catalog granularity is restricted to 8 broad product categories without item-level SKUs. (3) The absence of unit cost/margin data limits "
        "profitability modeling to gross top-line revenue metrics."
    )
    story.append(Paragraph(conclusion_text, body_style))
    story.append(Spacer(1, 4))
    
    # Subsection: Enterprise Technology Stack
    story.append(Paragraph("<b>VERIFIED ENTERPRISE TECHNOLOGY STACK</b>", sec_heading))
    tech_data = [
        [
            Paragraph("<b>Core Languages & Database:</b> Python 3.10+, PostgreSQL 15+, SQLAlchemy, psycopg2", meta_style),
            Paragraph("<b>Data Science & Modeling:</b> Pandas, NumPy, SciPy, statsmodels, scikit-learn, joblib", meta_style),
        ],
        [
            Paragraph("<b>Visualization & BI:</b> Matplotlib, Seaborn, Plotly, Microsoft Power BI Desktop, DAX", meta_style),
            Paragraph("<b>Reporting & Automation:</b> ReportLab, openpyxl, Windows Task Scheduler / GitHub Actions", meta_style),
        ]
    ]
    tech_table = Table(tech_data, colWidths=[280, 280])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(tech_table)
    
    # Page 2 Footer Note
    story.append(Spacer(1, 3))
    p2_footer = Table([[
        Paragraph("<font color='#64748B'>ApexPlanet Solutions Data Analytics Internship | Verified Final Submission Portfolio</font>", meta_style),
        Paragraph("<font color='#64748B'>Page 2 of 2</font>", ParagraphStyle('P2', parent=meta_style, alignment=2))
    ]], colWidths=[460, 100])
    p2_footer.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(p2_footer)
    
    # Build document
    doc.build(story)
    
    # Verification of page count
    reader = pypdf.PdfReader(str(OUTPUT_PDF))
    page_count = len(reader.pages)
    print(f"Generated PDF: {OUTPUT_PDF}")
    print(f"Total Page Count: {page_count}")
    return page_count

if __name__ == "__main__":
    count = build_pdf()
    if count != 2:
        print(f"ERROR: Expected exactly 2 pages, got {count}")
        sys.exit(1)
    else:
        print("SUCCESS: Executive summary PDF is EXACTLY 2 pages.")
        sys.exit(0)
