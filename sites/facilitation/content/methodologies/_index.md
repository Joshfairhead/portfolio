+++
title = "Visual Facilitation"
template = "facilitation.html"
weight = 1
+++

<section class="hero">
<div class="container">
<h1 class="hero__headline">Helping teams find alignment through visual facilitation.</h1>
</div>
<svg class="hero__curves" viewBox="0 0 1200 500" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
<defs>
<filter id="ink-bleed" x="-2%" y="-2%" width="104%" height="104%">
<feGaussianBlur stdDeviation="1.2 0.4"/>
</filter>
<!-- Patchy multi-stop gradients for dry brush pressure variation -->
<linearGradient id="r-fade" x1="0" y1="0" x2="1" y2="0">
<stop offset="0%" stop-color="rgb(220,38,38)" stop-opacity="1"/>
<stop offset="12%" stop-color="rgb(220,38,38)" stop-opacity="0.85"/>
<stop offset="28%" stop-color="rgb(220,38,38)" stop-opacity="0.3"/>
<stop offset="40%" stop-color="rgb(220,38,38)" stop-opacity="0.7"/>
<stop offset="55%" stop-color="rgb(220,38,38)" stop-opacity="0.4"/>
<stop offset="72%" stop-color="rgb(220,38,38)" stop-opacity="0.15"/>
<stop offset="100%" stop-color="rgb(220,38,38)" stop-opacity="0"/>
</linearGradient>
<linearGradient id="g-fade" x1="1" y1="0" x2="0" y2="0">
<stop offset="0%" stop-color="rgb(34,197,94)" stop-opacity="1"/>
<stop offset="12%" stop-color="rgb(34,197,94)" stop-opacity="0.85"/>
<stop offset="28%" stop-color="rgb(34,197,94)" stop-opacity="0.3"/>
<stop offset="40%" stop-color="rgb(34,197,94)" stop-opacity="0.7"/>
<stop offset="55%" stop-color="rgb(34,197,94)" stop-opacity="0.4"/>
<stop offset="72%" stop-color="rgb(34,197,94)" stop-opacity="0.15"/>
<stop offset="100%" stop-color="rgb(34,197,94)" stop-opacity="0"/>
</linearGradient>
<linearGradient id="b-fade" x1="0" y1="0" x2="1" y2="0">
<stop offset="0%" stop-color="rgb(59,130,246)" stop-opacity="0.9"/>
<stop offset="18%" stop-color="rgb(59,130,246)" stop-opacity="0.6"/>
<stop offset="32%" stop-color="rgb(59,130,246)" stop-opacity="0.85"/>
<stop offset="48%" stop-color="rgb(59,130,246)" stop-opacity="0.5"/>
<stop offset="65%" stop-color="rgb(59,130,246)" stop-opacity="0.3"/>
<stop offset="80%" stop-color="rgb(59,130,246)" stop-opacity="0.15"/>
<stop offset="100%" stop-color="rgb(59,130,246)" stop-opacity="0"/>
</linearGradient>
</defs>
<!-- H1: Declining S-curve (red) - filled tapered shape -->
<g>
<path d="M -20,-6 C 190,-4 385,65 598,208 C 810,355 1010,462 1220,484
         L 1220,488 C 998,471 790,375 605,232 C 408,98 210,32 -20,30 Z"
      fill="url(#r-fade)" filter="url(#ink-bleed)"/>
<!-- bristle trails extending beyond filled shape -->
<path d="M -20,0 C 200,0 400,68 600,208 C 802,352 1004,456 1220,480"
      stroke="url(#r-fade)" stroke-width="1.5" fill="none"
      stroke-dasharray="40 8 80 12 30 6 100 10 50 15"/>
<path d="M -20,22 C 200,22 400,90 600,228 C 802,372 1004,472 1220,492"
      stroke="url(#r-fade)" stroke-width="1" fill="none"
      stroke-dasharray="60 10 40 15 90 8 70 12" stroke-dashoffset="25"/>
<path d="M -20,34 C 200,38 400,100 600,236 C 802,378 1004,476 1220,494"
      stroke="url(#r-fade)" stroke-width="0.8" fill="none"
      stroke-dasharray="30 14 70 10 50 18 90 12" stroke-dashoffset="50"/>
</g>
<!-- H3: Rising S-curve (green) - filled tapered shape, mirror of H1 -->
<g>
<path d="M 1220,-6 C 1010,-4 815,65 602,208 C 390,355 190,462 -20,484
         L -20,488 C 202,471 410,375 595,232 C 792,98 990,32 1220,30 Z"
      fill="url(#g-fade)" filter="url(#ink-bleed)"/>
<path d="M 1220,0 C 1000,0 800,68 600,208 C 398,352 196,456 -20,480"
      stroke="url(#g-fade)" stroke-width="1.5" fill="none"
      stroke-dasharray="40 8 80 12 30 6 100 10 50 15"/>
<path d="M 1220,22 C 1000,22 800,90 600,228 C 398,372 196,472 -20,492"
      stroke="url(#g-fade)" stroke-width="1" fill="none"
      stroke-dasharray="60 10 40 15 90 8 70 12" stroke-dashoffset="25"/>
<path d="M 1220,34 C 1000,38 800,100 600,236 C 398,378 196,476 -20,494"
      stroke="url(#g-fade)" stroke-width="0.8" fill="none"
      stroke-dasharray="30 14 70 10 50 18 90 12" stroke-dashoffset="50"/>
</g>
<!-- H2: Bell curve (blue) - filled shape, swells at peak -->
<g>
<path d="M -20,471 C 98,452 272,348 402,220 C 482,148 544,84 588,58 C 618,46 652,46 682,58 C 728,84 790,148 870,220 C 998,348 1095,452 1220,471
         L 1220,481 C 1102,466 1008,375 880,252 C 800,182 738,120 694,96 C 666,84 636,84 606,96 C 550,120 488,182 408,252 C 280,375 108,466 -20,481 Z"
      fill="url(#b-fade)" filter="url(#ink-bleed)"/>
<path d="M -20,468 C 100,448 276,342 406,214 C 486,142 548,78 592,52 C 622,40 656,40 686,52 C 730,78 792,142 872,214 C 1000,342 1096,448 1220,468"
      stroke="url(#b-fade)" stroke-width="1.5" fill="none"
      stroke-dasharray="40 8 80 12 30 6 100 10 50 15"/>
<path d="M -20,484 C 94,470 262,378 396,256 C 478,186 542,124 590,100 C 620,88 658,88 688,100 C 736,124 800,186 882,256 C 1018,378 1108,470 1220,484"
      stroke="url(#b-fade)" stroke-width="1" fill="none"
      stroke-dasharray="60 10 40 15 90 8 70 12" stroke-dashoffset="25"/>
<path d="M -20,488 C 90,476 254,386 390,266 C 474,196 538,136 586,112 C 618,100 660,100 692,112 C 740,136 806,196 890,266 C 1024,386 1112,476 1220,488"
      stroke="url(#b-fade)" stroke-width="0.8" fill="none"
      stroke-dasharray="30 14 70 10 50 18 90 12" stroke-dashoffset="50"/>
</g>
</svg>
</section>

<section class="about">
<div class="container">
<p class="section-label">About</p>
<div class="about__divider"></div>
<p class="about__text">When teams encounter complex challenges, unclear priorities, or competing perspectives, I offer a facilitated process around shared frameworks (referents) where commonalities emerge naturally as structured wholeness. We map what's actually happening, what matters most, and the most resonant pathways forward.</p>
</div>
</section>

<section class="services">
<div class="container">
<p class="section-label">How We Work Together</p>
<div class="services__grid">
<div class="service-hex">Events</div>
<div class="service-hex">Workshops</div>
<div class="service-hex">Retreats</div>
<div class="service-hex">Tactics</div>
<div class="service-hex service-hex--center">Facilitation</div>
<div class="service-hex">Strategy</div>
<div class="service-hex">Planning</div>
<div class="service-hex">Design</div>
<div class="service-hex">Prototyping</div>
<div class="service-hex">Product</div>
</div>
</div>
</section>

<section class="methodologies">
<div class="container">
<p class="section-label">Core Methodologies</p>
<div class="methodologies__grid">
<div class="methodology-card">
<div class="methodology-card__title">Complexity Mapping</div>
<div class="methodology-card__description">Visual mapping of complex system dynamics and stakeholder relationships.</div>
</div>
<div class="methodology-card">
<div class="methodology-card__title">Dilemma Resolution</div>
<div class="methodology-card__description">Navigating tensions between competing values and priorities.</div>
</div>
<div class="methodology-card">
<div class="methodology-card__title">Three Horizons</div>
<div class="methodology-card__description">Mapping transitions from present reality to future possibilities.</div>
</div>
<div class="methodology-card">
<div class="methodology-card__title">Causal Texture</div>
<div class="methodology-card__description">Understanding how environmental conditions shape organizational responses.</div>
</div>
<a href="viable-systems-model/" class="methodology-card">
<div class="methodology-card__title">Viable Systems Model</div>
<div class="methodology-card__description">A reformulation of Stafford Beer's VSM for visual facilitation through the pentadic lens.</div>
</a>
<div class="methodology-card">
<div class="methodology-card__title">Hexagon Clustering</div>
<div class="methodology-card__description">Collaborative pattern recognition and theme emergence.</div>
</div>
<a href="synergy-graphs/" class="methodology-card">
<div class="methodology-card__title">Synergy Graphs</div>
<div class="methodology-card__description">Seven term systematics for understanding synergy and wholeness.</div>
</a>
<div class="methodology-card">
<div class="methodology-card__title">Wheel of Wisdom</div>
<div class="methodology-card__description">Integrative framework for navigating decision-making with wisdom.</div>
</div>
<div class="methodology-card">
<div class="methodology-card__title">World Game</div>
<div class="methodology-card__description">Making the world work for 100% of humanity through collaborative design.</div>
</div>
</div>
</div>
</section>

<section class="cta">
<div class="container">
<h2 class="cta__headline">Let's discuss your challenge.</h2>
<a href="mailto:hello@joshafairhead.com" class="cta__button">Get in touch</a>
</div>
</section>
