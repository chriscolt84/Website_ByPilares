ByPilares is a healing and meditation brand. It speaks softly and leaves room: one thought per surface, flat grounds of dusty colour, gold foil line art, and a lot of empty space. Everything should feel like a breath out.

## Content fundamentals

- Write in Spanish first, in the informal *tú* ("No te rindas", "Ahí donde te rompes"). English is fine for a quote that originates in English ("Calm is a super power").
- One idea per piece. A quote card holds at most 25 words; a headline holds one sentence.
- Sentence case for quotes, UPPERCASE only for the condensed poster style, eyebrows and the wordmark.
- Gentle, never clinical, never salesy. Invite rather than instruct: "Reservar lugar", not "¡Compra ya!". No exclamation marks, no emoji, no urgency.
- Attribute borrowed quotes plainly at the end ("- Yoda"), in the card's own ink.
- Dates follow Mexican usage: "Sábado 21 de junio · 8:00".

## Colour

The palette comes straight from the source posts: five grounds and two metals.

- Grounds: `sage-teal` (foil posts), `sage` (caps affirmations), `slate` (handwritten reflections), `blush` (rose posts and events), `peach` (the feather). One ground per composition, edge to edge, never a gradient.
- Metals: `gold-foil` and `gold-light` for line art and display quotes, `rose` for the lotus line and rose posters. These are decorative values: on their grounds they sit between 1.9:1 and 3.8:1, which the source accepts at poster scale only.
- For anything people must read, use the legible set: `ink`, `ink-muted`, `gold-ink` and `rose-ink` on `surface`, `surface-raised`, `surface-tint` (blush) or `blush`. Each token's note lists the grounds it passes on.
- `sage-deep` is the one added colour: a deepened sage-teal for primary buttons and any sage panel carrying text. `ivory` and `gold-light` both pass on it.
- The dark theme moves the page to a deep sage (`surface` #1f2927) and turns `accent` and `gold-ink` to a soft gold. Brand grounds keep their values in both themes.

## Typography

Four hosted families, each with one job. Do not mix more than two in a single piece, plus the wordmark.

- `display` (Cormorant Garamond): the `wordmark`, titles (`display-xl`, `display-l`) and the italic "by".
- `sans` (Montserrat): the gold quote voice in thin weights (`quote-l` at 200, `quote-m` at 300) and all UI text (`heading`, `body`, `small`, `eyebrow`). Body never goes lighter than 400.
- `condensed` (Antonio): tall thin caps for affirmations (`poster-l`, `poster-m`).
- `script` (Shadows Into Light Two): handwritten reflections on `slate` only (`note`), never in UI and never under 28px.

These are the closest open Google Fonts to the faces in the source posts; swap in licensed originals if the brand owns them.

## Space, shape and depth

- Generous space is part of the voice. Use `space-12` to `space-24` between sections and keep at least `space-12` (scaled) inside a social card.
- Social cards and imagery are square-cornered (`radius-none`). Product UI uses `radius-md` for cards, `radius-sm` for inputs and `radius-pill` for buttons, echoing the petal curve.
- Flat by default (`shadow-none`). `shadow-soft` only for a sheet floating over an image.
- Separate with colour or `hairline` rules. Controls take a 1px `ink-muted` border so they hold 3:1.
- Keyboard focus is `focus-ring`: a solid 2px ring with a 2px offset, at least 4.7:1 on every surface.

## Imagery and iconography

- Line art is gold foil: the mandala elephant and the peacock feather (Illustrations group). One illustration per composition, never recoloured, decorative `alt=""`.
- The brand symbol is the lotus inside a drop (`Logos/lotus-mark-cream.png`). It exists only as a small raster: keep it at 64px or below until a vector arrives.
- There is no icon set yet. Use words instead of icons; if one becomes necessary, choose a thin single-line set at 1.5px stroke in `ink`.
- No photography direction was supplied.

## Components

- `Wordmark`: "by" + PILARES, the name set in type.
- `QuoteCard`: the 4:5 social quote post in five ground variants.
- `EventCard`: announcement for a class, ceremony or workshop.
- `Button`: primary, secondary and quiet pills. Added for web use; the source posts show no buttons.

Styles live in `components/bundle.css` (classes prefixed `bp-`); there is no JavaScript bundle. Load `tokens.css` first, then `bundle.css`, which also pulls the four Google Fonts.
