import os
import xml.sax.saxutils as saxutils

def generate_svg(theme):
    is_dark = theme == 'dark'
    
    bg = '#030712' if is_dark else '#FFFFFF'
    panel_bg = '#0F172A' if is_dark else '#F8FAFC'
    border = '#1E293B' if is_dark else '#E2E8F0'
    primary_text = '#F8FAFC' if is_dark else '#0F172A'
    secondary_text = '#94A3B8' if is_dark else '#475569'
    
    acc_1 = '#7C3AED' if is_dark else '#2563EB'
    acc_2 = '#22D3EE' if is_dark else '#06B6D4'
    acc_3 = '#10B981'

    # Linear Gradient for shifting colors
    ascii_gradient = f"""
    <linearGradient id="ascii_grad_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="{acc_1}">
            <animate attributeName="stop-color" values="{acc_1};{acc_2};{acc_3};{acc_1}" dur="8s" repeatCount="indefinite" />
        </stop>
        <stop offset="50%" stop-color="{acc_2}">
            <animate attributeName="stop-color" values="{acc_2};{acc_3};{acc_1};{acc_2}" dur="8s" repeatCount="indefinite" />
        </stop>
        <stop offset="100%" stop-color="{acc_3}">
            <animate attributeName="stop-color" values="{acc_3};{acc_1};{acc_2};{acc_3}" dur="8s" repeatCount="indefinite" />
        </stop>
    </linearGradient>
    """

    # Floating particles
    particles = ""
    import random
    random.seed(42)
    for i in range(25):
        cx = random.randint(20, 1160)
        cy = random.randint(20, 590)
        r = round(random.uniform(1.2, 2.8), 2)
        dur = round(random.uniform(8, 16), 2)
        delay = round(random.uniform(0, 5), 2)
        particles += f"""
        <circle cx="{cx}" cy="{cy}" r="{r}" fill="{acc_2}" opacity="0.2">
            <animate attributeName="cy" values="{cy};{cy-60};{cy}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.1;0.6;0.1" dur="{dur/2}s" begin="{delay}s" repeatCount="indefinite"/>
        </circle>
        """

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
        line_delay = round(idx * 0.08, 2)
        ascii_svg += f"""
        <text x="20" y="{30 + idx*14}" font-family="monospace" font-size="12" fill="url(#ascii_grad_{theme})" opacity="0">
            <animate attributeName="opacity" values="0;1;1" keyTimes="0;0.2;1" dur="{1.5 + line_delay}s" fill="freeze" />
            {escaped_line}
        </text>
        """

    roles = [
        "Agentic AI Platform Engineer",
        "Multi-Agent Systems Architect",
        "NLP Engineer",
        "Software Associate @ Oracle"
    ]
    
    typing_svg = ""
    total_dur = 12
    for i, role in enumerate(roles):
        escaped_role = saxutils.escape(role)
        char_width = 9.6
        max_w = round(len(role) * char_width, 1)
        
        start_ratio = round(i * 0.25, 3)
        type_end = round(start_ratio + 0.083, 3)
        hold_end = round(start_ratio + 0.208, 3)
        del_end = round(start_ratio + 0.25, 3)
        
        kt = f"0; {start_ratio}; {type_end}; {hold_end}; {del_end}; 1"
        vw = f"0; 0; {max_w}; {max_w}; 0; 0"
        op_val = "0; 0; 1; 1; 0; 0"
        
        if i == 0:
            kt = f"0; {type_end}; {hold_end}; {del_end}; 1"
            vw = f"0; {max_w}; {max_w}; 0; 0"
            op_val = "1; 1; 1; 0; 0"
            
        typing_svg += f"""
        <g opacity="0">
            <animate attributeName="opacity" values="{op_val}" keyTimes="{kt}" dur="{total_dur}s" repeatCount="indefinite" />
            <clipPath id="clip_role_{i}_{theme}">
                <rect x="0" y="-18" height="30" width="0">
                    <animate attributeName="width" values="{vw}" keyTimes="{kt}" dur="{total_dur}s" repeatCount="indefinite" />
                </rect>
            </clipPath>
            <text x="0" y="0" font-family="monospace" font-size="16" font-weight="bold" fill="{acc_2}" clip-path="url(#clip_role_{i}_{theme})">{escaped_role}</text>
            <rect x="0" y="-14" width="8" height="18" fill="{acc_2}">
                <animate attributeName="x" values="{vw}" keyTimes="{kt}" dur="{total_dur}s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
            </rect>
        </g>
        """

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
            <rect width="{w}" height="28" rx="14" fill="{panel_bg}" stroke="{acc_1}" stroke-opacity="0.6" stroke-width="1">
                <animate attributeName="stroke" values="{acc_1};{acc_2};{acc_1}" dur="{3 + i*0.4}s" repeatCount="indefinite" />
            </rect>
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
        {ascii_gradient}
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
        {particles}
        
        <!-- Left Panel -->
        <g transform="translate(40, 40)">
            <rect width="400" height="530" rx="12" fill="{panel_bg}" fill-opacity="0.9" stroke="{border}" stroke-width="1" />
            
            <!-- Scanline -->
            <rect width="400" height="3" fill="{acc_2}" opacity="0.4">
                <animate attributeName="y" values="0;530;0" dur="7s" repeatCount="indefinite" />
            </rect>
            
            <!-- ASCII floating container -->
            <g transform="translate(0, 0)">
                <animateTransform attributeName="transform" type="translate" values="0,0; 0,8; 0,0" dur="5s" repeatCount="indefinite" />
                <g transform="translate(20, 70)">
                    {ascii_svg}
                </g>
            </g>
        </g>
        
        <!-- Right Panel -->
        <g transform="translate(460, 40)">
            <rect width="680" height="530" rx="12" fill="{panel_bg}" fill-opacity="0.8" stroke="{border}" stroke-width="1" />
            
            <!-- Terminal Header -->
            <rect width="680" height="40" rx="12" fill="{border}" fill-opacity="0.6" />
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
                
                <!-- Roles Typing -->
                <g transform="translate(0, 70)">
                    {typing_svg}
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
