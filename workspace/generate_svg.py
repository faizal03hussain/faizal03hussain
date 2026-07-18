import os
import xml.sax.saxutils as saxutils

def generate_svg(theme):
    is_dark = theme == 'dark'
    
    bg = '#030712' if is_dark else '#FFFFFF'
    panel_bg = '#0F172A' if is_dark else '#F8FAFC'
    border = 'rgba(255,255,255,0.08)' if is_dark else 'rgba(15,23,42,0.08)'
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
        ascii_svg += f'<text x="20" y="{30 + idx*14}" font-family="monospace" font-size="12" fill="url(#ascii_grad_{theme})">{escaped_line}</text>\n'

    roles = [
        "Agentic AI Platform Engineer",
        "Multi-Agent Systems Architect",
        "NLP Engineer",
        "Software Associate @ Oracle"
    ]
    
    typing_svg = ""
    for i, role in enumerate(roles):
        escaped_role = saxutils.escape(role)
        typing_svg += f"""
        <g class="role-group role-{i}">
            <text x="0" y="0" font-family="monospace" font-size="16" fill="{acc_2}">{escaped_role}</text>
        </g>
        """
        
    info_items = [
        ("Location", "Bengaluru, India"),
        ("Education", "B.Tech in AI & Data Science, REVA University"),
        ("Current Focus", "Enterprise RAG & Agentic AI Systems"),
        ("Portfolio", "faizalhussain.in"),
        ("Email", "faizal03hussain@gmail.com")
    ]
    
    info_svg = ""
    for i, (k, v) in enumerate(info_items):
        escaped_k = saxutils.escape(k)
        escaped_v = saxutils.escape(v)
        info_svg += f"""
        <g transform="translate(0, {i*35})">
            <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="{secondary_text}">{escaped_k}</text>
            <text x="120" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="14" fill="{primary_text}">{escaped_v}</text>
        </g>
        """

    skills = ["Python", "Java", "Agentic AI", "RAG Pipelines", "Spring Boot", "Oracle Cloud", "FastAPI", "Multi-Agent Systems", "Vector Search", "Google Cloud", "LLM Orchestration", "LangChain"]
    skills_svg = ""
    x_offset = 0
    y_offset = 0
    for i, skill in enumerate(skills):
        escaped_skill = saxutils.escape(skill)
        w = len(skill) * 8 + 30
        if x_offset + w > 600:
            x_offset = 0
            y_offset += 40
            
        skills_svg += f"""
        <g transform="translate({x_offset}, {y_offset})">
            <rect width="{w}" height="30" rx="15" fill="{panel_bg}" stroke="{acc_1}" stroke-opacity="0.4" stroke-width="1" />
            <text x="{w/2}" y="20" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" fill="{primary_text}" text-anchor="middle">{escaped_skill}</text>
        </g>
        """
        x_offset += w + 10

    socials = ["GitHub", "LinkedIn", "Website", "Email"]
    social_svg = ""
    for i, s in enumerate(socials):
        escaped_s = saxutils.escape(s)
        social_svg += f"""
        <g transform="translate({i*100}, 0)">
            <rect width="85" height="30" rx="6" fill="{panel_bg}" stroke="{border}" stroke-width="1" />
            <text x="42.5" y="20" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="12" fill="{primary_text}" text-anchor="middle">{escaped_s}</text>
        </g>
        """

    css_styles = f"""
        @keyframes floatAnim {{
            0%, 100% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(8px); }}
        }}
        @keyframes scanlineAnim {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(530px); }}
            100% {{ transform: translateY(0px); }}
        }}
        @keyframes blinkAnim {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0; }}
        }}
        @keyframes role0 {{
            0%, 22% {{ opacity: 1; }}
            25%, 100% {{ opacity: 0; }}
        }}
        @keyframes role1 {{
            0%, 24% {{ opacity: 0; }}
            25%, 47% {{ opacity: 1; }}
            50%, 100% {{ opacity: 0; }}
        }}
        @keyframes role2 {{
            0%, 49% {{ opacity: 0; }}
            50%, 72% {{ opacity: 1; }}
            75%, 100% {{ opacity: 0; }}
        }}
        @keyframes role3 {{
            0%, 74% {{ opacity: 0; }}
            75%, 98% {{ opacity: 1; }}
            100% {{ opacity: 0; }}
        }}
        .ascii-float {{ animation: floatAnim 6s ease-in-out infinite; }}
        .scanline {{ animation: scanlineAnim 8s linear infinite; }}
        .cursor {{ animation: blinkAnim 0.8s infinite; }}
        .role-0 {{ animation: role0 12s infinite; }}
        .role-1 {{ animation: role1 12s infinite; }}
        .role-2 {{ animation: role2 12s infinite; }}
        .role-3 {{ animation: role3 12s infinite; }}
    """

    svg = f"""<svg width="1180" height="610" viewBox="0 0 1180 610" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <style>
            {css_styles}
        </style>
        <linearGradient id="ascii_grad_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{acc_1}" />
            <stop offset="50%" stop-color="{acc_2}" />
            <stop offset="100%" stop-color="{acc_3}" />
        </linearGradient>
        <radialGradient id="bg_grad_{theme}" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{acc_1}" stop-opacity="0.12" />
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
            <rect width="400" height="530" rx="12" fill="{panel_bg}" fill-opacity="0.85" stroke="{border}" stroke-width="1" />
            
            <!-- Scanline effect -->
            <rect class="scanline" width="400" height="3" fill="{acc_2}" opacity="0.4" />
            
            <!-- ASCII floating container -->
            <g class="ascii-float">
                <g transform="translate(30, 80)">
                    {ascii_svg}
                </g>
            </g>
        </g>
        
        <!-- Right Panel -->
        <g transform="translate(460, 40)">
            <rect width="680" height="530" rx="12" fill="{panel_bg}" fill-opacity="0.7" stroke="{border}" stroke-width="1" />
            
            <!-- Terminal Header -->
            <rect width="680" height="40" rx="12" fill="{border}" opacity="0.6" />
            <circle cx="20" cy="20" r="6" fill="#EF4444" />
            <circle cx="40" cy="20" r="6" fill="#F59E0B" />
            <circle cx="60" cy="20" r="6" fill="#10B981" />
            <text x="340" y="24" font-family="monospace" font-size="12" fill="{secondary_text}" text-anchor="middle">faizal03hussain@terminal ~</text>
            
            <!-- Content -->
            <g transform="translate(40, 80)">
                <!-- Greeting -->
                <g>
                    <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="26" font-weight="bold" fill="{primary_text}">Hi 👋</text>
                    <text x="0" y="35" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="30" font-weight="bold" fill="{primary_text}">I'm Faizal Hussain</text>
                </g>
                
                <!-- Roles Typing -->
                <g transform="translate(0, 75)">
                    {typing_svg}
                    <rect class="cursor" x="275" y="-14" width="8" height="18" fill="{acc_2}" />
                </g>
                
                <!-- Divider -->
                <line x1="0" y1="100" x2="600" y2="100" stroke="{border}" stroke-width="1" />
                
                <!-- Info Grid -->
                <g transform="translate(0, 135)">
                    {info_svg}
                </g>
                
                <!-- Skills -->
                <g transform="translate(0, 320)">
                    <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="15" font-weight="bold" fill="{primary_text}">Technical Focus</text>
                    <g transform="translate(0, 18)">
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
