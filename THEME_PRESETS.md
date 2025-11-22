# Theme Presets

This document contains saved theme configurations for quick recall and switching.

## Original Theme (Orange)
**Currently Active**

```toml
accent_color = "#ff7800"
accent_color_dark = "#ffa348"
fix_contrast_dark = true
```

**Styles:**
```toml
styles = [
  "portfolio-cards.css",
]
```

## Forest Theme (Emerald Green)
**With aerial forest background**

```toml
accent_color = "#50C878"  # Emerald green
accent_color_dark = "#7CFC00"  # Lawn green/chartreuse
fix_contrast_dark = true
```

**Styles:**
```toml
styles = [
  "portfolio-cards.css",
  "forest-background.css",
]
```

**Background image:** `/static/forest-background.png`

**Description:**
- Light mode uses emerald green (#50C878) - professional, rich forest tone
- Dark mode uses vibrant lawn green (#7CFC00) - bright chartreuse matching sunlit canopy
- Fixed background with aerial forest photography
- 85% white overlay (light mode) / 75% black overlay (dark mode) for readability

## Butterfly Nebula Theme (Cosmic Purple/Orange)
**With space nebula background**

```toml
accent_color = "#CC00CC"  # Vibrant magenta/purple
accent_color_dark = "#FF8C42"  # Fiery orange/coral
fix_contrast_dark = true
```

**Styles:**
```toml
styles = [
  "portfolio-cards.css",
  "nebula-background.css",
]
```

**Background image:** `/static/butterfly-nebula.jpg`

**Color palette inspiration:**
- Magenta/Purple (#CC00CC) - Captures the mystical central region of the nebula
- Fiery Orange (#FF8C42) - Hot gas clouds in the upper wings
- Electric Blue (#4169E1) - Ionized gas in lower wings
- Deep Navy (#0F1419) - Cosmic background

**Description:**
- Light mode uses vibrant magenta (#CC00CC) - cosmic energy of the nebula's core
- Dark mode uses fiery orange (#FF8C42) - glowing hot gas from the stellar wings
- Fixed background with Butterfly Nebula (planetary nebula) imagery
- 75% white overlay (light mode) / 60-70% dark overlay (dark mode) to let nebula colors shine through
- Creates a dramatic, cosmic atmosphere perfect for showcasing creative work

---

## How to Switch Themes

1. Update `config.toml` lines 52-55 with desired accent colors
2. Update `config.toml` lines 80-83 to add/remove background CSS
3. Run `zola build` or let auto-reload handle it in dev mode
