from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,Color
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PIL import Image
from textwrap import wrap
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import re
R=Path('/mnt/data/propertysnaps-site'); OUT=R/'assets/guides';OUT.mkdir(parents=True,exist_ok=True)
W,H=A4
try:
 pdfmetrics.registerFont(TTFont('Noto','/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf'))
 pdfmetrics.registerFont(TTFont('NotoBold','/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf'))
except Exception:
 pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
 pdfmetrics.registerFont(TTFont('DejaVuBold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
F='Noto' if 'Noto' in pdfmetrics.getRegisteredFontNames() else 'DejaVu'; B='NotoBold' if 'NotoBold' in pdfmetrics.getRegisteredFontNames() else 'DejaVuBold'
DARK=HexColor('#143837');TEAL=HexColor('#326662');ACC=HexColor('#BE936F');CREAM=HexColor('#F7F6F2');WHITE=HexColor('#FFFFFF');INK=HexColor('#213232');SOFT=HexColor('#61736F')

def rect(c,x,y,w,h,color):c.setFillColor(color);c.rect(x,y,w,h,stroke=0,fill=1)
def text(c,x,y,s,size=11,font=F,color=INK):c.setFillColor(color);c.setFont(font,size);c.drawString(x,y,s)
def P(c,body,x,top,w,size=10,leading=17,col=SOFT,font=F):
 st=ParagraphStyle('x',fontName=font,fontSize=size,leading=leading,textColor=col,spaceAfter=0,allowWidows=0,allowOrphans=0)
 p=Paragraph(body.replace('&','&amp;'),st);pw,ph=p.wrap(w,600);p.drawOn(c,x,top-ph);return top-ph

def photo(c,slug,x,y,w,h):
 path=R/'assets/images'/f'{slug}.webp';im=Image.open(path).convert('RGB')
 ar=w/h;iw,ih=im.size
 if iw/ih>ar:
  nw=int(ih*ar); l=(iw-nw)//2;im=im.crop((l,0,l+nw,ih))
 else:
  nh=int(iw/ar);top=(ih-nh)//2;im=im.crop((0,top,iw,top+nh))
 # JPEG intermediate gives small, efficient PDF embeddings.
 jpgdir=R/'_build/pdf-image-cache';jpgdir.mkdir(parents=True,exist_ok=True)
 key=f'{slug}-{int(w)}x{int(h)}';j=jpgdir/(key+'.jpg')
 if not j.exists():
  im.thumbnail((1600,1600))
  im.save(j,format='JPEG',quality=80,optimize=True,subsampling=0)
 c.drawImage(str(j),x,y,w,h)

def badge(c,n,y,marker='01'):
 rect(c,46,y-4,32,30,TEAL);text(c,54,y+7,marker,10,B,WHITE);text(c,92,y+8,n,14,B,INK)

def foot(c,pg,category):
 c.setLineWidth(.5);c.setStrokeColor(HexColor('#DDDEDA'));c.line(45,44,W-45,44)
 text(c,45,28,'PROPERTY SNAPS  /  EST. 2006',8,B,SOFT)
 text(c,W-130,28,category.upper()+f'   {pg:02d}',8,F,SOFT)

def cover(c,d):
 rect(c,0,0,W,H,DARK)
 photo(c,d['hero'],0,H*.36,W,H*.64)
 rect(c,0,0,W,H*.38,DARK)
 rect(c,45,267,55,3,ACC)
 text(c,45,241,'PROPERTY  SNAPS',16,B,WHITE)
 text(c,45,224,'REAL ESTATE MEDIA  /  MELBOURNE SOUTH-EAST',8,B,HexColor('#C0D5CD'))
 title=d['title'].split(' | ')
 text(c,45,165,title[0],32,B,WHITE)
 if len(title)>1:text(c,45,120,title[1],32,B,WHITE)
 text(c,45,75,'2026 SERVICE GUIDE  ·  CASEY & CARDINIA',10,B,ACC)
 text(c,45,38,'Photography  ·  Aerial  ·  Floor Plans  ·  Film',9,F,HexColor('#BDD2CB'))
 c.showPage()

def intro(c,d):
 rect(c,0,H-22,W,22,DARK)
 text(c,45,H-80,'WHAT WE BRING TO THE FRAME',10,B,TEAL)
 text(c,45,H-142,d['headline'],26,B,INK)
 P(c,d['intro'],45,H-168,W-90,12,21,SOFT)
 photo(c,d['main_photo'],45,240,W-90,285)
 rect(c,45,153,W-90,63,CREAM)
 text(c,68,184,'SINCE 2006',14,B,TEAL)
 text(c,68,165,'Local understanding, considered imaging and coordinated media.',9,F,INK)
 foot(c,2,d['short']);c.showPage()

def options(c,d):
 rect(c,0,H-22,W,22,DARK)
 text(c,45,H-81,'WHAT WE OFFER',10,B,TEAL)
 text(c,45,H-136,'The right assets for the brief.',27,B,INK)
 P(c,'Property Snaps can create individual deliverables or coordinate the media needed for a complete campaign.',45,H-150,W-90,11,19,SOFT)
 y=H-238
 for i,(heading,description) in enumerate(d['services']):
  col=i%2;row=i//2
  x=45+col*255; yy=y-row*170
  rect(c,x,yy-127,236,144,CREAM)
  rect(c,x,yy-127,5,144,ACC)
  text(c,x+17,yy-13,f'0{i+1}',9,B,TEAL)
  P(c,heading,x+17,yy-22,205,13,18,INK,B)
  P(c,description,x+17,yy-67,203,9.1,15,SOFT,F)
 foot(c,3,d['short']);c.showPage()

def process(c,d):
 rect(c,0,H-22,W,22,DARK)
 text(c,45,H-80,'HOW WE WORK',10,B,TEAL)
 text(c,45,H-133,'From brief to delivery.',28,B,INK)
 steps=[('01','TELL US ABOUT THE PROPERTY','Suburb, type, timing, planned channels and the assets you need.'),('02','AGREE ON THE SCOPE','We confirm the shoot approach, deliverables and the quote.'),('03','CAPTURE AND CREATE','Photography, aerial footage, drawing or editing according to the brief.'),('04','READY TO MARKET','Approved files supplied in agreed formats for use across channels.')]
 y=H-188
 for id,name,desc in steps:
  rect(c,45,y-69,W-90,77,CREAM)
  text(c,62,y-25,id,21,B,TEAL)
  text(c,114,y-12,name,11,B,INK)
  P(c,desc,114,y-24,W-180,9.4,15,SOFT)
  y-=91
 photo(c,d['process_photo'],45,82,W-90,203)
 foot(c,4,d['short']);c.showPage()

def showcase(c,d):
 rect(c,0,H-22,W,22,DARK)
 text(c,45,H-80,'VISUAL DIRECTIONS',10,B,TEAL)
 text(c,45,H-129,'Media with purpose.',28,B,INK)
 text(c,45,H-154,'Different perspectives are useful for different stories.',10,F,SOFT)
 photo(c,d['gallery'][0],45,377,W-90,245)
 photo(c,d['gallery'][1],45,105,(W-101)/2,256)
 photo(c,d['gallery'][2],56+(W-101)/2,105,(W-101)/2,256)
 foot(c,5,d['short']);c.showPage()

def back(c,d):
 rect(c,0,0,W,H,DARK)
 photo(c,d['hero'],0,H-314,W,314)
 rect(c,0,0,W,H-314,DARK)
 rect(c,45,410,64,3,ACC)
 text(c,45,360,'WHAT IS YOUR NEXT PROPERTY?',10,B,ACC)
 text(c,45,315,'Let’s make it',33,B,WHITE)
 text(c,45,273,'worth looking at.',33,B,WHITE)
 P(c,'Share the property suburb, timing and your marketing requirements. We will discuss an approach and prepare a tailored quote.',45,244,W-110,11,20,HexColor('#D5E5DE'))
 text(c,45,153,'propertysnaps.com.au/contact/',12,B,WHITE)
 text(c,45,130,'vince@propertysnaps.com.au  |  0408 559 555',10,F,HexColor('#C0D5CD'))
 text(c,45,63,'PROPERTY SNAPS',20,B,WHITE)
 text(c,45,42,'SERVING CASEY AND CARDINIA SINCE 2006',9,F,ACC)
 c.showPage()

D=[
 dict(file='property-snaps-real-estate-guide-2026.pdf',short='Real Estate',title='Real Estate Media | Service Guide',hero='twilight-street-front',main_photo='interior-wideangle',process_photo='corner-block-aerial',headline='Make every listing matter.',intro='Property Snaps creates photography, measured floor plans, drone imagery and video for agents and property managers across Melbourne\'s south-east. Whether the job is an investment unit or a beautiful family home, we focus on clear spaces, honest presentation and an efficient path from briefing to listing.',services=[('DAYTIME PHOTOGRAPHY','Bright room and exterior photography, edited for online listings and printed marketing.'),('TWILIGHT & DUSK','The atmosphere of a home in evening light, particularly for landscaped or architecturally distinctive properties.'),('DRONE / AERIAL','Grounds, block context, nearby amenities and strong overhead angles where flight conditions allow.'),('MEASURED FLOOR PLANS','Site measurements, 2D layout drawings, optional 3D styling and agency-branded presentation.'),('PROPERTY VIDEO','Walkthroughs, aerial sequences and social-ready edits scoped to the campaign.'),('MARKETING EXTRAS','Graphic overlays, image refinements, virtual furniture and marketing collateral by request.')],gallery=['listing-daylight','twilight-landscaping','three-d-floorplan']),
 dict(file='property-snaps-builders-guide-2026.pdf',short='Builders',title='Builder & Trade | Service Guide',hero='architectural-exterior',main_photo='kitchen-detail',process_photo='modern-home-daylight',headline='Show the craft in every detail.',intro='Finished work deserves images that show the whole achievement, from the overall architectural form to joinery, finishes and fine construction details. We create practical media for building-company portfolios, designers, specialist trades, award entries and proposals across Casey, Cardinia and nearby suburbs.',services=[('BUILDER PORTFOLIOS','Architectural interiors, exteriors and detail images for completed projects.'),('PREMIUM TWILIGHT','Expressive evening photography for standout façades and outdoor spaces.'),('DRONE PERSPECTIVE','Show scale, roof geometry, landscaping and the position of a completed project.'),('VIDEO SHOWCASES','Walkthroughs, progress coverage and short feature films for web and social media.'),('PLANS & VISUALISATION','Marketing floor plans, presentation layouts and CAD-style drafting support.'),('BRANDED MEDIA','Consistent output for tender documents, websites, brochures and award submissions.')],gallery=['architectural-exterior','kitchen-detail','twilight-landscaping']),
 dict(file='property-snaps-pools-guide-2026.pdf',short='Pools & Outdoors',title='Pools & Outdoors | Service Guide',hero='twilight-pool',main_photo='pool-al-fresco',process_photo='parkland-aerial',headline='The finishing touch is the image.',intro='A beautifully finished pool or landscape project comes alive through its proportions, materials, planting and lighting. Property Snaps creates daytime, twilight, aerial and video media for pool builders, landscape businesses and outdoor-living specialists, including portfolio and industry award submissions.',services=[('DAYTIME POOL IMAGERY','Crisp details, pool geometry, water clarity, finishes and garden context.'),('TWILIGHT POOL SHOOTS','Showcase underwater and garden lighting, reflections and the evening atmosphere.'),('AERIAL PHOTOGRAPHY','Reveal the full design, landscaping, surrounds and the connection with the home.'),('VIDEO & MOTION','Short project showcases for websites, social channels and award submissions.'),('SPASA & PORTFOLIOS','Coordinated image selections planned around how projects will be presented.'),('DETAIL & LIFESTYLE','Paving, tiling, outdoor kitchens, alfresco spaces, plantings and design details.')],gallery=['twilight-pool','pool-al-fresco','aerial-evening'])]
for d in D:
 path=OUT/d['file'];c=canvas.Canvas(str(path),pagesize=A4,pageCompression=1);c.setTitle('Property Snaps | '+d['title']);c.setAuthor('Property Snaps');
 cover(c,d);intro(c,d);options(c,d);process(c,d);showcase(c,d);back(c,d);c.save();print(path,round(path.stat().st_size/1024), 'KB')
