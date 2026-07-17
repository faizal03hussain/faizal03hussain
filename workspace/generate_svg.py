import os

def generate_svg(theme):
    is_dark = theme == 'dark'
    
    bg = '#030712' if is_dark else '#FFFFFF'
    panel_bg = '#0F172A' if is_dark else '#F8FAFC'
    border = 'rgba(255,255,255,0.08)' if is_dark else 'rgba(15,23,42,0.08)'
    primary_text = '#F8FAFC' if is_dark else '#0F172A'
    secondary_text = '#94A3B8' if is_dark else '#475569'
    
    # Gradients
    acc_1 = '#7C3AED' if is_dark else '#2563EB'
    acc_2 = '#22D3EE' if is_dark else '#06B6D4'
    acc_3 = '#10B981'
    
    ascii_gradient = f"""
    <linearGradient id="ascii_grad_{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="{acc_1}" />
        <stop offset="50%" stop-color="{acc_2}" />
        <stop offset="100%" stop-color="{acc_3}" />
        <animate attributeName="x1" values="0%;100%;0%" dur="10s" repeatCount="indefinite" />
        <animate attributeName="y1" values="0%;100%;0%" dur="13s" repeatCount="indefinite" />
        <animate attributeName="x2" values="100%;0%;100%" dur="10s" repeatCount="indefinite" />
        <animate attributeName="y2" values="100%;0%;100%" dur="13s" repeatCount="indefinite" />
    </linearGradient>
    """

    # Particle generator
    particles = ""
    import random
    random.seed(42)
    for i in range(20):
        x = random.randint(0, 1180)
        y = random.randint(0, 610)
        r = random.uniform(1, 3)
        dur = random.uniform(10, 20)
        particles += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{acc_2}" opacity="0.2"><animate attributeName="cy" values="{y};{y-100};{y}" dur="{dur}s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.1;0.5;0.1" dur="{dur/2}s" repeatCount="indefinite"/></circle>\n'

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
        # Reveal line by line
        delay = idx * 0.1
        ascii_svg += f'<text x="20" y="{30 + idx*14}" font-family="monospace" font-size="12" fill="url(#ascii_grad_{theme})" opacity="0"><animate attributeName="opacity" values="0;1;1" keyTimes="0;0.1;1" dur="{2 + delay}s" fill="freeze" begin="0s" />{line.replace(" ", "&#160;")}</text>\n'

    roles = [
        "Agentic AI Platform Engineer",
        "Multi-Agent Systems Architect",
        "NLP Engineer",
        "Software Associate @ Oracle"
    ]
    
    typing_svg = ""
    total_dur = 12
    for i, role in enumerate(roles):
        char_width = 9.6
        max_w = len(role) * char_width
        start_ratio = i * (3 / total_dur)
        type_end = start_ratio + (1 / total_dur)
        hold_end = start_ratio + (2.5 / total_dur)
        del_end = start_ratio + (3 / total_dur)
        
        kt = f"0; {start_ratio}; {type_end}; {hold_end}; {del_end}; 1"
        vw = f"0; 0; {max_w}; {max_w}; 0; 0"
        
        if i == 0:
            kt = f"0; {type_end}; {hold_end}; {del_end}; 1"
            vw = f"0; {max_w}; {max_w}; 0; 0"
            
        typing_svg += f"""
        <g>
            <clipPath id="clip_role_{i}_{theme}">
                <rect x="0" y="-15" height="30" width="0">
                    <animate attributeName="width" values="{vw}" keyTimes="{kt}" dur="{total_dur}s" repeatCount="indefinite" />
                </rect>
            </clipPath>
            <text x="0" y="0" font-family="monospace" font-size="16" fill="{acc_2}" clip-path="url(#clip_role_{i}_{theme})">{role}</text>
            <rect x="0" y="-12" width="8" height="16" fill="{acc_2}">
                <animate attributeName="x" values="{vw}" keyTimes="{kt}" dur="{total_dur}s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />
            </rect>
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
        delay = 1.5 + (i * 0.3)
        info_svg += f"""
        <g opacity="0" transform="translate(0, {i*35})">
            <animate attributeName="opacity" values="0;1" dur="0.5s" begin="{delay}s" fill="freeze" />
            <animateTransform attributeName="transform" type="translate" values="0,{i*35 + 10}; 0,{i*35}" dur="0.5s" begin="{delay}s" fill="freeze" />
            <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="{secondary_text}">{k}</text>
            <text x="120" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="14" fill="{primary_text}">{v}</text>
        </g>
        """

    skills = ["Python", "Java", "Agentic AI", "RAG", "Spring Boot", "Oracle Cloud", "FastAPI", "Multi-Agent Systems", "SQL", "GCP", "LLMs", "NLP"]
    skills_svg = ""
    x_offset = 0
    y_offset = 0
    for i, skill in enumerate(skills):
        delay = 3 + (i * 0.1)
        w = len(skill) * 8 + 30
        if x_offset + w > 600:
            x_offset = 0
            y_offset += 40
            
        skills_svg += f"""
        <g opacity="0" transform="translate({x_offset}, {y_offset})">
            <animate attributeName="opacity" values="0;1" dur="0.5s" begin="{delay}s" fill="freeze" />
            <animateTransform attributeName="transform" type="translate" values="{x_offset},{y_offset + 10}; {x_offset},{y_offset}" dur="0.5s" begin="{delay}s" fill="freeze" />
            <rect width="{w}" height="30" rx="15" fill="{panel_bg}" stroke="{border}" stroke-width="1">
                <animate attributeName="stroke" values="{border};{acc_1};{border}" dur="3s" begin="{delay + i*0.5}s" repeatCount="indefinite" />
            </rect>
            <text x="{w/2}" y="20" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" fill="{primary_text}" text-anchor="middle">{skill}</text>
        </g>
        """
        x_offset += w + 10

    social_svg = ""
    socials = ["GitHub", "LinkedIn", "Twitter", "Portfolio"]
    for i, s in enumerate(socials):
        delay = 4.5 + (i * 0.2)
        social_svg += f"""
        <g opacity="0" transform="translate({i*100}, 0)">
            <animate attributeName="opacity" values="0;1" dur="0.5s" begin="{delay}s" fill="freeze" />
            <rect width="80" height="30" rx="6" fill="{panel_bg}" stroke="{border}" stroke-width="1" />
            <text x="40" y="20" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="12" fill="{primary_text}" text-anchor="middle">{s}</text>
        </g>
        """

    svg = f"""<svg width="1180" height="610" viewBox="0 0 1180 610" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        {ascii_gradient}
        <radialGradient id="bg_grad_{theme}" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{acc_1}" stop-opacity="0.1" />
            <stop offset="100%" stop-color="{bg}" stop-opacity="1" />
        </radialGradient>
        <filter id="glow_{theme}" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="10" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
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
            <rect width="400" height="530" rx="12" fill="{panel_bg}" fill-opacity="0.8" stroke="{border}" stroke-width="1" />
            
            <!-- Scanline effect -->
            <rect width="400" height="4" fill="{acc_2}" opacity="0.3" filter="url(#glow_{theme})">
                <animate attributeName="y" values="0;530;0" dur="8s" repeatCount="indefinite" />
            </rect>
            
            <!-- ASCII floating container -->
            <g>
                <animateTransform attributeName="transform" type="translate" values="0,0; 0,10; 0,0" dur="6s" repeatCount="indefinite" />
                <g transform="translate(30, 80)">
                    {ascii_svg}
                </g>
            </g>
        </g>
        
        <!-- Right Panel -->
        <g transform="translate(460, 40)">
            <rect width="680" height="530" rx="12" fill="{panel_bg}" fill-opacity="0.6" stroke="{border}" stroke-width="1" />
            
            <!-- Terminal Header -->
            <rect width="680" height="40" rx="12" fill="{border}" opacity="0.5" />
            <circle cx="20" cy="20" r="6" fill="#EF4444" />
            <circle cx="40" cy="20" r="6" fill="#F59E0B" />
            <circle cx="60" cy="20" r="6" fill="#10B981" />
            
            <!-- Content -->
            <g transform="translate(40, 80)">
                <!-- Greeting -->
                <g opacity="0">
                    <animate attributeName="opacity" values="0;1" dur="1s" fill="freeze" />
                    <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="28" font-weight="bold" fill="{primary_text}">Hi 👋</text>
                    <text x="0" y="35" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="32" font-weight="bold" fill="{primary_text}">I'm Faizal Hussain</text>
                </g>
                
                <!-- Roles Typing -->
                <g transform="translate(0, 80)">
                    {typing_svg}
                </g>
                
                <!-- Divider -->
                <rect x="0" y="110" width="600" height="1" fill="{border}" opacity="0">
                    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="1s" fill="freeze" />
                </rect>
                
                <!-- Info Grid -->
                <g transform="translate(0, 140)">
                    {info_svg}
                </g>
                
                <!-- Skills -->
                <g transform="translate(0, 320)">
                    <text x="0" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="16" font-weight="bold" fill="{primary_text}" opacity="0">
                        <animate attributeName="opacity" values="0;1" dur="0.5s" begin="2.8s" fill="freeze" />
                        Technical Arsenal
                    </text>
                    <g transform="translate(0, 20)">
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
