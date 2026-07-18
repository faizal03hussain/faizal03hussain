import os
import xml.sax.saxutils as saxutils

def generate_svg(theme):
    is_dark = theme == 'dark'
    
    bg = '#030712' if is_dark else '#FFFFFF'
    panel_bg = '#0F172A' if is_dark else '#F8FAFC'
    border = 'rgba(255,255,255,0.1)' if is_dark else 'rgba(15,23,42,0.1)'
    primary_text = '#F8FAFC' if is_dark else '#0F172A'
    secondary_text = '#94A3B8' if is_dark else '#475569'
    
    acc_1 = '#7C3AED' if is_dark else '#2563EB'
    acc_2 = '#22D3EE' if is_dark else '#06B6D4'
    acc_3 = '#10B981'

    # ASCII Art
    ascii_art = r"""
              .,-:;//;:=,
          . :H@@@MM@M#H/.,+%;,
       ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=             .---=-=:=,.
  =@#@@@MX.,                -%HX$$%%%:;
 =-./@M@M$                   .;@MMMM@MM:
 X@/ -$MM/                    . +MM@@@M$
,@M@H: :@:                    . =X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MM@@@MMH,.                  XM@MH; =;
  /%+%$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@= =,
               =++%%%%+/:-.
    """.strip("\n")
    
    ascii_lines = ascii_art.split("\n")
    ascii_svg = ""
    for idx, line in enumerate(ascii_lines):
        escaped_line = saxutils.escape(line).replace(" ", "&#160;")
        ascii_svg += f'<text x="25" y="{30 + idx*14}" font-family="monospace" font-size="12" fill="url(#ascii_grad_{theme})">{escaped_line}</text>\n'

    info_items = [
        ("Location", "Bengaluru, India"),
        ("Education", "B.Tech in AI &amp; Data Science, REVA University"),
        ("Current Focus", "Enterprise RAG &amp; Agentic AI Systems"),
        ("Portfolio", "faizalhussain.in"),
        ("Email", "faizal03hussain@gmail.com")
    ]
    
    info_svg = ""
    for i, (k, v) in enumerate(info_items):
        info_svg += f"""
        <g transform="translate(0, {i*32})">
            <text x="0" y="0" font-family="sans-serif" font-size="14" font-weight="bold" fill="{secondary_text}">{k}</text>
            <text x="130" y="0" font-family="sans-serif" font-size="14" fill="{primary_text}">{v}</text>
        </g>
        """

    skills = ["Python", "Java", "Agentic AI", "RAG Pipelines", "Spring Boot", "Oracle Cloud", "FastAPI", "Multi-Agent Systems", "Vector Search", "Google Cloud", "LLM Orchestration", "LangChain"]
    skills_svg = ""
    x_offset = 0
    y_offset = 0
    for i, skill in enumerate(skills):
        escaped_skill = saxutils.escape(skill)
        w = len(skill) * 8 + 28
        if x_offset + w > 580:
            x_offset = 0
            y_offset += 36
            
        skills_svg += f"""
        <g transform="translate({x_offset}, {y_offset})">
            <rect width="{w}" height="28" rx="14" fill="{panel_bg}" stroke="{acc_1}" stroke-opacity="0.5" stroke-width="1" />
            <text x="{w/2}" y="19" font-family="sans-serif" font-size="12" fill="{primary_text}" text-anchor="middle">{escaped_skill}</text>
        </g>
        """
        x_offset += w + 8

    socials = ["GitHub", "LinkedIn", "Website", "Email"]
    social_svg = ""
    for i, s in enumerate(socials):
        escaped_s = saxutils.escape(s)
        social_svg += f"""
        <g transform="translate({i*95}, 0)">
            <rect width="85" height="28" rx="6" fill="{panel_bg}" stroke="{border}" stroke-width="1" />
            <text x="42.5" y="19" font-family="sans-serif" font-size="12" fill="{primary_text}" text-anchor="middle">{escaped_s}</text>
        </g>
        """

    svg = f"""<svg width="1180" height="610" viewBox="0 0 1180 610" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="ascii_grad_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{acc_1}" />
            <stop offset="50%" stop-color="{acc_2}" />
            <stop offset="100%" stop-color="{acc_3}" />
        </linearGradient>
        <radialGradient id="bg_grad_{theme}" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{acc_1}" stop-opacity="0.15" />
            <stop offset="100%" stop-color="{bg}" stop-opacity="1" />
        </radialGradient>
        <clipPath id="canvas_clip">
            <rect width="1180" height="610" rx="16" />
        </clipPath>
    </defs>
    
    <rect width="1180" height="610" rx="16" fill="{bg}" />
    <rect width="1180" height="610" rx="16" fill="url(#bg_grad_{theme})" />
    
    <g clip-path="url(#canvas_clip)">
        <!-- Left Panel -->
        <g transform="translate(40, 40)">
            <rect width="400" height="530" rx="12" fill="{panel_bg}" fill-opacity="0.9" stroke="{border}" stroke-width="1" />
            
            <g transform="translate(20, 70)">
                {ascii_svg}
            </g>
        </g>
        
        <!-- Right Panel -->
        <g transform="translate(460, 40)">
            <rect width="680" height="530" rx="12" fill="{panel_bg}" fill-opacity="0.8" stroke="{border}" stroke-width="1" />
            
            <!-- Terminal Header -->
            <rect width="680" height="40" rx="12" fill="{border}" opacity="0.6" />
            <circle cx="20" cy="20" r="6" fill="#EF4444" />
            <circle cx="40" cy="20" r="6" fill="#F59E0B" />
            <circle cx="60" cy="20" r="6" fill="#10B981" />
            <text x="340" y="24" font-family="monospace" font-size="12" fill="{secondary_text}" text-anchor="middle">faizal03hussain@terminal ~</text>
            
            <!-- Content -->
            <g transform="translate(40, 75)">
                <!-- Greeting -->
                <g>
                    <text x="0" y="0" font-family="sans-serif" font-size="26" font-weight="bold" fill="{primary_text}">Hi 👋</text>
                    <text x="0" y="34" font-family="sans-serif" font-size="30" font-weight="bold" fill="{primary_text}">I'm Faizal Hussain</text>
                </g>
                
                <!-- Roles -->
                <g transform="translate(0, 70)">
                    <text x="0" y="0" font-family="monospace" font-size="16" font-weight="bold" fill="{acc_2}">Enterprise-Scale RAG &amp; Agentic AI Systems Architect</text>
                </g>
                
                <!-- Divider -->
                <line x1="0" y1="92" x2="600" y2="92" stroke="{border}" stroke-width="1" />
                
                <!-- Info Grid -->
                <g transform="translate(0, 125)">
                    {info_svg}
                </g>
                
                <!-- Skills -->
                <g transform="translate(0, 310)">
                    <text x="0" y="0" font-family="sans-serif" font-size="15" font-weight="bold" fill="{primary_text}">Technical Focus</text>
                    <g transform="translate(0, 16)">
                        {skills_svg}
                    </g>
                </g>
                
                <!-- Social Icons (Bottom) -->
                <g transform="translate(0, 425)">
                    {social_svg}
                </g>
                
            </g>
        </g>
    </g>
</svg>"""
    return svg

with open("dark.svg", "w", encoding="utf-8") as f:
    f.write(generate_svg("dark"))
    
with open("light.svg", "w", encoding="utf-8") as f:
    f.write(generate_svg("light"))
