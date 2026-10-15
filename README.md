# ByPilares website

Static marketing site for ByPilares (healing, meditation, yoga). Plain HTML, CSS and a few lines of JavaScript: no build step, no framework, no dependencies.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Inicio |
| `sesiones.html` | Sesiones (meditación, acompañamiento, yoga y respiración, círculos) |
| `sobre.html` | Sobre ByPilares |
| `contacto.html` | Contacto (form) |

## Structure

```
assets/css/tokens.css      generated from design-system/tokens.json (do not edit by hand)
assets/css/components.css  ByPilares components: wordmark, buttons, cards (bp- classes)
assets/css/site.css        page layout
assets/js/site.js          mobile menu, contact form, footer year
assets/img/                logos and gold-foil illustrations
design-system/tokens.json  source of truth for colours, type, spacing, radii
design-system/BRAND.md     brand book: voice, colour rules, typography, imagery
scripts/build_tokens.py    rebuilds tokens.css after editing tokens.json
```

To change a colour or font size, edit `design-system/tokens.json`, then run:

```
python3 scripts/build_tokens.py
```

## Run locally

```
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Publish with GitHub Pages

1. In the repository, open Settings > Pages.
2. Under "Build and deployment", choose "Deploy from a branch", branch `main`, folder `/ (root)`.
3. Save. The site goes live at `https://<user>.github.io/Website_ByPilares/` within a few minutes.
4. For a custom domain (for example bypilares.com), add it in the same screen and point the domain's DNS to GitHub Pages.

The site also works as-is on Netlify, Vercel or Cloudflare Pages (no build command, publish directory `/`).

## Contact form

The form posts JSON to the URL in the `data-endpoint` attribute of `<form id="contact-form">` in `contacto.html`. It is empty, so the form currently shows a thank-you note without sending anything.

To connect it with Formspree (free tier available):

1. Create a form at formspree.io and copy its endpoint, for example `https://formspree.io/f/abcdwxyz`.
2. Paste it into `data-endpoint="..."` in `contacto.html` and commit.

## Booking and contact

- "Reservar sesión" and "Agendar sesión" buttons open Calendly: https://calendly.com/pilares-yoga/30min
- WhatsApp and phone: 55 2565 2318 (`wa.me/525525652318`). Instagram: @pilaresyoga.
- To change any of these, edit them in every HTML page (search for `calendly.com`, `wa.me` or `pilaresyoga`).

## Logo

`assets/img/logos/lotus-mark.svg` is a vector trace of the lotus mark from the original posts. Pages reference it with `<use href="...#lotus">`, and `site.css` uses it as the faint watermark on every page. Replace it with the designer's master SVG when available (keep `id="lotus"` on the path).

## Open items before launch

- Prices and schedules per practice (the copy currently invites people to ask or book).
- A short biography for the "Sobre" page if the brand is led by a named practitioner.
