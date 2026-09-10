skills = {
    "frontend": 95,
    "react": 90,
    "javascript": 95,
    "typescript": 80,
    "ui": 90,
    "automation": 85,
    "problemsolving": 90,
    "learning": 100,
}

TEMPLATE = """<svg width="400" height="30" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="barGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6D28D9"/>
      <stop offset="50%" stop-color="#C026D3"/>
      <stop offset="100%" stop-color="#E9D5FF"/>
    </linearGradient>
  </defs>

  <!-- track -->
  <rect
    x="0"
    y="10"
    width="400"
    height="10"
    rx="5"
    fill="#1B102B"
  />

  <!-- animated fill -->
  <rect
    x="0"
    y="10"
    height="10"
    rx="5"
    fill="url(#barGradient)"
  >
    <animate
      attributeName="width"
      from="0"
      to="{fill}"
      dur="1.5s"
      fill="freeze"
    />
  </rect>

  <!-- glow pulse on the fill -->
  <rect
    x="0"
    y="10"
    height="10"
    rx="5"
    fill="url(#barGradient)"
    opacity="0.5"
  >
    <animate
      attributeName="width"
      from="0"
      to="{fill}"
      dur="1.5s"
      fill="freeze"
    />
    <animate
      attributeName="opacity"
      values="0.5;0.9;0.5"
      dur="2s"
      repeatCount="indefinite"
      begin="1.5s"
    />
  </rect>
</svg>"""

import os

os.makedirs("assets/bars", exist_ok=True)

for name, pct in skills.items():
    fill = round(pct * 3.8)  # 380 = 95% of 400
    svg = TEMPLATE.format(fill=fill)

    with open(f"assets/bars/skill-{name}.svg", "w") as f:
        f.write(svg)
