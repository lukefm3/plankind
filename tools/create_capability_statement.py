from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "website" / "downloads" / "plankind-capability-statement.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor("#12323A")
DEEP = colors.HexColor("#0C252B")
CREAM = colors.HexColor("#F3F0E7")
CORAL = colors.HexColor("#EC7757")
SAGE = colors.HexColor("#AEBF99")
MUTED = colors.HexColor("#647477")

styles = getSampleStyleSheet()
brand = ParagraphStyle("brand", fontName="Helvetica-Bold", fontSize=25, leading=28, textColor=NAVY)
descriptor = ParagraphStyle("descriptor", fontName="Helvetica-Bold", fontSize=7, leading=10, tracking=3, textColor=CORAL)
tagline = ParagraphStyle("tagline", fontName="Times-Italic", fontSize=20, leading=23, textColor=NAVY, spaceAfter=8)
heading = ParagraphStyle("heading", fontName="Helvetica-Bold", fontSize=8, leading=11, tracking=1.6, textColor=CORAL, spaceBefore=12, spaceAfter=7)
subhead = ParagraphStyle("subhead", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=NAVY, spaceAfter=4)
body = ParagraphStyle("body", fontName="Helvetica", fontSize=8.7, leading=13, textColor=DEEP, spaceAfter=5)
small = ParagraphStyle("small", fontName="Helvetica", fontSize=7.4, leading=10, textColor=MUTED)
right = ParagraphStyle("right", parent=small, alignment=TA_RIGHT)

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DEEP)
    canvas.rect(0, 0, LETTER[0], .45 * inch, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(.65 * inch, .18 * inch, "PlanKind Insights  |  Grounded in evidence. Focused on impact.")
    canvas.drawRightString(7.85 * inch, .18 * inch, f"{doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER, leftMargin=.65*inch, rightMargin=.65*inch,
                        topMargin=.58*inch, bottomMargin=.62*inch,
                        title="PlanKind Insights Capability Statement", author="Luke F. Miller")

services = [
    [Paragraph("STRATEGY & PLANNING", subhead), Paragraph("Strategic, organizational, program, and operational planning; governance support; facilitation.", body)],
    [Paragraph("EVALUATION", subhead), Paragraph("Program and impact evaluation; monitoring systems; cost-benefit analysis; logic models and theories of change.", body)],
    [Paragraph("RESEARCH & ANALYTICS", subhead), Paragraph("Economic and policy analysis; statistical modeling; GIS; dashboards; forecasting; data visualization.", body)],
    [Paragraph("PROCESS IMPROVEMENT", subhead), Paragraph("Workflow redesign; SOPs; automation; reporting systems; performance measurement.", body)],
    [Paragraph("EMERGENCY PREPAREDNESS", subhead), Paragraph("Emergency and continuity planning; ICS; exercises; After Action Reports; public health preparedness.", body)],
]

story = [
    Table([[Paragraph("Plan <font color='#EC7757'>|</font> Kind", brand),
            Paragraph("Luke F. Miller<br/>lukefm@hawaii.edu<br/>(412) 807-8570", right)]], colWidths=[4.8*inch, 2.4*inch]),
    Paragraph("I N S I G H T S", descriptor),
    Spacer(1, 18),
    Table([[Paragraph("Grounded in evidence.<br/>Focused on impact.", tagline),
            Paragraph("PlanKind helps government agencies, public health departments, nonprofits, universities, foundations, and other mission-driven organizations make better decisions through evidence-based planning and practical implementation.", body)]],
          colWidths=[3.15*inch, 4.05*inch], style=TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LINEABOVE",(0,0),(-1,0),1.2,NAVY),("TOPPADDING",(0,0),(-1,-1),12)])),
    Paragraph("CORE CAPABILITIES", heading),
    Table(services, colWidths=[2.15*inch, 5.05*inch], style=TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),("GRID",(0,0),(-1,-1),.5,colors.HexColor("#CCD5D0")),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[colors.white,CREAM]),("TOPPADDING",(0,0),(-1,-1),8),
        ("BOTTOMPADDING",(0,0),(-1,-1),7),("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8)
    ])),
    Paragraph("OUR APPROACH", heading),
    Table([
        [Paragraph("<b>1 · Frame the decision</b><br/>Begin with the choice or outcome that matters.", body),
         Paragraph("<b>2 · Build the evidence</b><br/>Use the strongest appropriate mix of data, research, and stakeholder knowledge.", body),
         Paragraph("<b>3 · Design for people</b><br/>Make findings understandable and useful to those who must act.", body)],
        [Paragraph("<b>4 · Plan for implementation</b><br/>Translate recommendations into ownership, workflows, and measures.", body),
         Paragraph("<b>5 · Leave capacity behind</b><br/>Create maintainable tools, clear documentation, and reusable systems.", body),
         Paragraph("<b>The test</b><br/><font color='#EC7757'>How does this improve decisions?</font>", body)]
    ], colWidths=[2.4*inch]*3, style=TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#DCE5DF")),
        ("BOX",(0,0),(-1,-1),.5,colors.HexColor("#A8B8B2")),("INNERGRID",(0,0),(-1,-1),.5,colors.HexColor("#A8B8B2")),
        ("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),7),("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9)
    ])),
    Paragraph("EXPERTISE", heading),
    Paragraph("Economics  ·  Disaster preparedness  ·  Public health  ·  Governance  ·  Energy policy  ·  Program evaluation  ·  Monitoring & Evaluation  ·  Data science  ·  R programming  ·  GIS  ·  Statistical analysis  ·  Academic research", body),
    Spacer(1, 6),
    Table([[Paragraph("<b>CONTACT</b><br/>lukefm@hawaii.edu<br/>luke.freddy.miller@gmail.com<br/>linkedin.com/in/luke-miller-283258127/", body),
            Paragraph("<b>PUBLIC DEMONSTRATION</b><br/>The PlanKind Resilience Monitor demonstrates a reproducible R and GitHub Actions pipeline that automatically collects, validates, and publishes OpenFEMA data.", body)]],
          colWidths=[3.6*inch,3.6*inch], style=TableStyle([("BACKGROUND",(0,0),(-1,-1),SAGE),("VALIGN",(0,0),(-1,-1),"TOP"),("TOPPADDING",(0,0),(-1,-1),10),("BOTTOMPADDING",(0,0),(-1,-1),9),("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10)])),
]

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)

