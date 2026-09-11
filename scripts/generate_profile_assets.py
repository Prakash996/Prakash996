from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent



def create_contrib_banner() -> None:
    output = ROOT / "profile-3d-contrib" / "profile-night-rainbow.svg"
    output.parent.mkdir(parents=True, exist_ok=True)

    svg = '''<svg width="1200" height="320" viewBox="0 0 1200 320" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1200" y2="320" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#0B1020"/>
      <stop offset="0.5" stop-color="#111827"/>
      <stop offset="1" stop-color="#090C14"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#8B5CF6"/>
      <stop offset="0.5" stop-color="#22D3EE"/>
      <stop offset="1" stop-color="#A3E635"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="320" rx="28" fill="url(#bg)"/>
  <g opacity="0.18">
    <circle cx="120" cy="80" r="110" fill="#8B5CF6"/>
    <circle cx="980" cy="210" r="150" fill="#06B6D4"/>
    <circle cx="760" cy="60" r="120" fill="#A78BFA"/>
  </g>

  <g>
    <rect x="80" y="70" width="1040" height="180" rx="20" fill="#0F172A" stroke="rgba(148,163,184,0.2)"/>
    <g fill="#1E293B" stroke="#334155" stroke-width="1.5">
      <rect x="110" y="105" width="18" height="18" rx="4"/>
      <rect x="138" y="105" width="18" height="18" rx="4"/>
      <rect x="166" y="105" width="18" height="18" rx="4"/>
      <rect x="194" y="105" width="18" height="18" rx="4"/>
      <rect x="222" y="105" width="18" height="18" rx="4"/>
      <rect x="250" y="105" width="18" height="18" rx="4"/>
      <rect x="278" y="105" width="18" height="18" rx="4"/>
      <rect x="306" y="105" width="18" height="18" rx="4"/>

      <rect x="110" y="133" width="18" height="18" rx="4"/>
      <rect x="138" y="133" width="18" height="18" rx="4"/>
      <rect x="166" y="133" width="18" height="18" rx="4"/>
      <rect x="194" y="133" width="18" height="18" rx="4"/>
      <rect x="222" y="133" width="18" height="18" rx="4"/>
      <rect x="250" y="133" width="18" height="18" rx="4"/>
      <rect x="278" y="133" width="18" height="18" rx="4"/>
      <rect x="306" y="133" width="18" height="18" rx="4"/>

      <rect x="110" y="161" width="18" height="18" rx="4"/>
      <rect x="138" y="161" width="18" height="18" rx="4"/>
      <rect x="166" y="161" width="18" height="18" rx="4"/>
      <rect x="194" y="161" width="18" height="18" rx="4"/>
      <rect x="222" y="161" width="18" height="18" rx="4" fill="url(#glow)"/>
      <rect x="250" y="161" width="18" height="18" rx="4" fill="url(#glow)"/>
      <rect x="278" y="161" width="18" height="18" rx="4" fill="url(#glow)"/>
      <rect x="306" y="161" width="18" height="18" rx="4" fill="url(#glow)"/>

      <rect x="110" y="189" width="18" height="18" rx="4"/>
      <rect x="138" y="189" width="18" height="18" rx="4" fill="url(#glow)"/>
      <rect x="166" y="189" width="18" height="18" rx="4" fill="url(#glow)"/>
      <rect x="194" y="189" width="18" height="18" rx="4" fill="url(#glow)"/>
      <rect x="222" y="189" width="18" height="18" rx="4" fill="url(#glow)"/>
      <rect x="250" y="189" width="18" height="18" rx="4"/>
      <rect x="278" y="189" width="18" height="18" rx="4"/>
      <rect x="306" y="189" width="18" height="18" rx="4"/>
    </g>

    <g>
      <rect x="390" y="100" width="300" height="18" rx="9" fill="#0B1120"/>
      <rect x="390" y="100" width="230" height="18" rx="9" fill="url(#glow)"/>
      <rect x="390" y="146" width="350" height="18" rx="9" fill="#0B1120"/>
      <rect x="390" y="146" width="286" height="18" rx="9" fill="url(#glow)"/>
      <rect x="390" y="192" width="280" height="18" rx="9" fill="#0B1120"/>
      <rect x="390" y="192" width="210" height="18" rx="9" fill="url(#glow)"/>
    </g>

    <g fill="#E2E8F0" font-family="Arial, Helvetica, sans-serif">
      <text x="90" y="52" font-size="18" font-weight="700">Development streak</text>
      <text x="920" y="130" font-size="18" font-weight="700" fill="#A5B4FC">+ 42 commits</text>
      <text x="920" y="165" font-size="18" font-weight="700" fill="#67E8F9">UI + DX</text>
      <text x="920" y="200" font-size="18" font-weight="700" fill="#86EFAC">steady growth</text>
    </g>
  </g>
</svg>
'''

    output.write_text(svg, encoding="utf-8")


def create_footer_banner() -> None:
    output = ROOT / "assets" / "one-piece-profile-bg.svg"
    output.parent.mkdir(parents=True, exist_ok=True)

    svg = '''<svg width="1600" height="420" viewBox="0 0 1600 420" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="420" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#0B1020"/>
      <stop offset="0.55" stop-color="#111827"/>
      <stop offset="1" stop-color="#0F172A"/>
    </linearGradient>
    <linearGradient id="line" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#8B5CF6"/>
      <stop offset="0.5" stop-color="#22D3EE"/>
      <stop offset="1" stop-color="#F472B6"/>
    </linearGradient>
  </defs>

  <rect width="1600" height="420" fill="url(#bg)"/>
  <circle cx="200" cy="100" r="110" fill="#8B5CF6" opacity="0.2"/>
  <circle cx="1380" cy="200" r="160" fill="#22D3EE" opacity="0.12"/>
  <circle cx="970" cy="90" r="110" fill="#A78BFA" opacity="0.18"/>

  <g opacity="0.8">
    <path d="M0 300C180 250 260 225 380 250C500 275 580 328 700 315C820 302 900 210 1010 218C1120 226 1212 300 1320 286C1430 272 1500 225 1600 250V420H0V300Z" fill="#111827"/>
    <path d="M0 332C180 282 260 300 380 310C500 320 580 360 700 350C820 340 900 292 1010 302C1120 312 1212 360 1320 350C1430 340 1500 305 1600 330V420H0V332Z" fill="#0F172A"/>
  </g>

  <g>
    <path d="M70 276H1530" stroke="url(#line)" stroke-width="3" stroke-linecap="round" opacity="0.45"/>
    <path d="M150 250L360 250" stroke="#94A3B8" stroke-width="1.5" stroke-linecap="round" opacity="0.4"/>
    <path d="M430 250L720 250" stroke="#94A3B8" stroke-width="1.5" stroke-linecap="round" opacity="0.4"/>
    <path d="M790 250L1020 250" stroke="#94A3B8" stroke-width="1.5" stroke-linecap="round" opacity="0.4"/>
    <path d="M1090 250L1370 250" stroke="#94A3B8" stroke-width="1.5" stroke-linecap="round" opacity="0.4"/>
  </g>

  <g>
    <circle cx="180" cy="180" r="68" fill="#8B5CF6" opacity="0.32"/>
    <circle cx="180" cy="180" r="38" fill="#E2E8F0" opacity="0.85"/>
    <path d="M155 180L178 203L216 165" stroke="#0F172A" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>

    <circle cx="650" cy="180" r="68" fill="#22D3EE" opacity="0.25"/>
    <path d="M620 180H680" stroke="#E2E8F0" stroke-width="10" stroke-linecap="round"/>
    <path d="M650 150V210" stroke="#E2E8F0" stroke-width="10" stroke-linecap="round"/>

    <circle cx="1110" cy="180" r="68" fill="#F472B6" opacity="0.22"/>
    <path d="M1090 158L1130 202L1185 145" stroke="#E2E8F0" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <g fill="#E2E8F0" font-family="Arial, Helvetica, sans-serif" font-weight="700">
    <text x="72" y="110" font-size="24">BUILD • EXPLORE • LEVEL UP</text>
    <text x="72" y="345" font-size="18" fill="#94A3B8">FRONTEND • UI ARCHITECTURE • PRODUCTIVITY</text>
  </g>
</svg>
'''

    output.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    create_contrib_banner()
    create_footer_banner()
    print("Generated profile assets")
