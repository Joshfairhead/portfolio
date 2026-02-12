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
<!-- Ink bleed - slight edge softening -->
<filter id="ink-bleed" x="-2%" y="-2%" width="104%" height="104%">
<feGaussianBlur stdDeviation="1.2 0.4"/>
</filter>
<!-- Rough edge displacement - organic bristle edges -->
<filter id="rough-edge" x="-4%" y="-4%" width="108%" height="108%">
<feTurbulence type="fractalNoise" baseFrequency="0.04 0.15" numOctaves="4" seed="3" result="noise"/>
<feDisplacementMap in="SourceGraphic" in2="noise" scale="6" xChannelSelector="R" yChannelSelector="G"/>
</filter>
<!-- Combined rough + blur for filled shapes -->
<filter id="brush-fill" x="-4%" y="-4%" width="108%" height="108%">
<feTurbulence type="fractalNoise" baseFrequency="0.03 0.12" numOctaves="5" seed="7" result="noise"/>
<feDisplacementMap in="SourceGraphic" in2="noise" scale="5" xChannelSelector="R" yChannelSelector="G" result="displaced"/>
<feGaussianBlur in="displaced" stdDeviation="0.8 0.3"/>
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
<!-- H1: Declining S-curve (red) -->
<g>
<!-- Filled shape with rough displacement edges -->
<path d="M -20,-6 C 190,-4 385,65 598,208 C 810,355 1010,462 1220,484
         L 1220,488 C 998,471 790,375 605,232 C 408,98 210,32 -20,30 Z"
      fill="url(#r-fade)" filter="url(#brush-fill)"/>
<!-- Tightly woven bristle paths within the stroke body -->
<path d="M -20,2 C 195,0 390,67 600,210 C 808,356 1008,462 1220,484.5" stroke="url(#r-fade)" stroke-width="2" fill="none" stroke-dasharray="300 2 450 3 280 2" stroke-dashoffset="0" filter="url(#ink-bleed)"/>
<path d="M -20,5 C 210,4 405,72 605,214 C 805,354 1005,460 1220,485" stroke="url(#r-fade)" stroke-width="2.5" fill="none" stroke-dasharray="420 3 260 2 380" stroke-dashoffset="80" filter="url(#ink-bleed)"/>
<path d="M -20,8 C 185,6 395,70 598,212 C 810,358 1010,464 1220,485.5" stroke="url(#r-fade)" stroke-width="2" fill="none" stroke-dasharray="350 2 500 3 200 2" stroke-dashoffset="150" filter="url(#ink-bleed)"/>
<path d="M -20,12 C 220,12 420,80 612,218 C 808,358 1004,464 1220,486" stroke="url(#r-fade)" stroke-width="3" fill="none" stroke-dasharray="480 2 320 3 400" stroke-dashoffset="40" filter="url(#ink-bleed)"/>
<path d="M -20,16 C 200,16 400,84 602,220 C 805,362 1006,466 1220,486.5" stroke="url(#r-fade)" stroke-width="2.5" fill="none" stroke-dasharray="550 2 380 3 290 2" stroke-dashoffset="200" filter="url(#ink-bleed)"/>
<path d="M -20,20 C 215,22 410,90 608,226 C 806,366 1004,468 1220,487" stroke="url(#r-fade)" stroke-width="2" fill="none" stroke-dasharray="400 3 300 2 500" stroke-dashoffset="0" filter="url(#ink-bleed)"/>
<path d="M -20,24 C 198,26 398,96 604,230 C 804,370 1002,470 1220,488" stroke="url(#r-fade)" stroke-width="1.5" fill="none" stroke-dasharray="320 2 460 3 350 2" stroke-dashoffset="120" filter="url(#ink-bleed)"/>
<!-- Stray edge bristles -->
<path d="M -20,-4 C 200,-6 400,60 600,204 C 802,348 1004,454 1220,482" stroke="url(#r-fade)" stroke-width="1" fill="none" stroke-dasharray="40 8 80 12 30 6 100 10 50 15"/>
<path d="M -20,32 C 200,36 400,100 600,236 C 802,378 1004,476 1220,494" stroke="url(#r-fade)" stroke-width="0.8" fill="none" stroke-dasharray="30 14 70 10 50 18 90 12" stroke-dashoffset="50"/>
</g>
<!-- H3: Rising S-curve (green) - mirror of H1 -->
<g>
<path d="M 1220,-6 C 1010,-4 815,65 602,208 C 390,355 190,462 -20,484
         L -20,488 C 202,471 410,375 595,232 C 792,98 990,32 1220,30 Z"
      fill="url(#g-fade)" filter="url(#brush-fill)"/>
<path d="M 1220,2 C 1005,0 810,67 600,210 C 392,356 192,462 -20,484.5" stroke="url(#g-fade)" stroke-width="2" fill="none" stroke-dasharray="300 2 450 3 280 2" stroke-dashoffset="0" filter="url(#ink-bleed)"/>
<path d="M 1220,5 C 990,4 795,72 595,214 C 395,354 195,460 -20,485" stroke="url(#g-fade)" stroke-width="2.5" fill="none" stroke-dasharray="420 3 260 2 380" stroke-dashoffset="80" filter="url(#ink-bleed)"/>
<path d="M 1220,8 C 1015,6 805,70 602,212 C 390,358 190,464 -20,485.5" stroke="url(#g-fade)" stroke-width="2" fill="none" stroke-dasharray="350 2 500 3 200 2" stroke-dashoffset="150" filter="url(#ink-bleed)"/>
<path d="M 1220,12 C 980,12 780,80 588,218 C 392,358 196,464 -20,486" stroke="url(#g-fade)" stroke-width="3" fill="none" stroke-dasharray="480 2 320 3 400" stroke-dashoffset="40" filter="url(#ink-bleed)"/>
<path d="M 1220,16 C 1000,16 800,84 598,220 C 395,362 194,466 -20,486.5" stroke="url(#g-fade)" stroke-width="2.5" fill="none" stroke-dasharray="550 2 380 3 290 2" stroke-dashoffset="200" filter="url(#ink-bleed)"/>
<path d="M 1220,20 C 985,22 790,90 592,226 C 394,366 196,468 -20,487" stroke="url(#g-fade)" stroke-width="2" fill="none" stroke-dasharray="400 3 300 2 500" stroke-dashoffset="0" filter="url(#ink-bleed)"/>
<path d="M 1220,24 C 1002,26 802,96 596,230 C 396,370 198,470 -20,488" stroke="url(#g-fade)" stroke-width="1.5" fill="none" stroke-dasharray="320 2 460 3 350 2" stroke-dashoffset="120" filter="url(#ink-bleed)"/>
<path d="M 1220,-4 C 1000,-6 800,60 600,204 C 398,348 196,454 -20,482" stroke="url(#g-fade)" stroke-width="1" fill="none" stroke-dasharray="40 8 80 12 30 6 100 10 50 15"/>
<path d="M 1220,32 C 1000,36 800,100 600,236 C 398,378 196,476 -20,494" stroke="url(#g-fade)" stroke-width="0.8" fill="none" stroke-dasharray="30 14 70 10 50 18 90 12" stroke-dashoffset="50"/>
</g>
<!-- H2: Bell curve (blue) -->
<g>
<path d="M -20,471 C 98,452 272,348 402,220 C 482,148 544,84 588,58 C 618,46 652,46 682,58 C 728,84 790,148 870,220 C 998,348 1095,452 1220,471
         L 1220,481 C 1102,466 1008,375 880,252 C 800,182 738,120 694,96 C 666,84 636,84 606,96 C 550,120 488,182 408,252 C 280,375 108,466 -20,481 Z"
      fill="url(#b-fade)" filter="url(#brush-fill)"/>
<path d="M -20,472 C 100,454 276,348 406,220 C 486,148 548,84 592,58 C 622,46 656,46 686,58 C 730,84 792,148 872,220 C 1000,348 1096,454 1220,472" stroke="url(#b-fade)" stroke-width="2" fill="none" stroke-dasharray="300 2 450 3 280 2" stroke-dashoffset="0" filter="url(#ink-bleed)"/>
<path d="M -20,474 C 96,456 270,350 402,224 C 484,152 546,88 590,62 C 620,50 654,50 684,62 C 728,88 790,152 872,224 C 1002,350 1098,456 1220,474" stroke="url(#b-fade)" stroke-width="2.5" fill="none" stroke-dasharray="420 3 260 2 380" stroke-dashoffset="80" filter="url(#ink-bleed)"/>
<path d="M -20,476 C 102,460 278,354 408,228 C 488,156 550,92 594,66 C 624,54 658,54 688,66 C 732,92 796,156 878,228 C 1006,354 1100,460 1220,476" stroke="url(#b-fade)" stroke-width="3" fill="none" stroke-dasharray="350 2 500 3 200 2" stroke-dashoffset="150" filter="url(#ink-bleed)"/>
<path d="M -20,478 C 98,462 274,358 404,232 C 486,160 548,96 592,70 C 622,58 656,58 686,70 C 730,96 794,160 876,232 C 1004,358 1098,462 1220,478" stroke="url(#b-fade)" stroke-width="2.5" fill="none" stroke-dasharray="480 2 320 3 400" stroke-dashoffset="40" filter="url(#ink-bleed)"/>
<path d="M -20,480 C 100,466 276,362 406,236 C 488,164 550,100 594,76 C 624,64 658,64 688,76 C 732,100 796,164 878,236 C 1006,362 1100,466 1220,480" stroke="url(#b-fade)" stroke-width="2" fill="none" stroke-dasharray="550 2 380 3 290 2" stroke-dashoffset="200" filter="url(#ink-bleed)"/>
<!-- Stray edge bristles -->
<path d="M -20,468 C 100,448 276,342 406,214 C 486,142 548,78 592,52 C 622,40 656,40 686,52 C 730,78 792,142 872,214 C 1000,342 1096,448 1220,468" stroke="url(#b-fade)" stroke-width="1" fill="none" stroke-dasharray="40 8 80 12 30 6 100 10 50 15"/>
<path d="M -20,486 C 92,474 258,382 394,260 C 476,190 540,128 588,104 C 618,92 658,92 690,104 C 738,128 802,190 884,260 C 1020,382 1110,474 1220,486" stroke="url(#b-fade)" stroke-width="0.8" fill="none" stroke-dasharray="30 14 70 10 50 18 90 12" stroke-dashoffset="50"/>
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
