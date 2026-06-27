# Industry Reasoning Rules - Psychology Decision Engine
# Purpose: Smart rules for combining psychology principles by industry and context

## HOW THIS REASONING ENGINE WORKS

When Claude receives a UI/UX request, it runs through this file to:
1. Detect the industry
2. Load the correct principle weights
3. Apply the right combinations
4. Avoid industry-specific anti-patterns
5. Generate the Psychology Decisions table

## STEP 1: INDUSTRY DETECTION RULES

### Detection Keywords by Industry

#### Ecommerce Triggers
Keywords: shop, store, product, cart, checkout, buy, purchase, delivery,
shipping, catalog, listing, D2C, marketplace, retail, order, SKU,
inventory, collection, wishlist, COD, return policy
→ Load: ecommerce.md + high FOMO + orange/red CTA

#### SaaS Triggers
Keywords: software, app, platform, dashboard, subscription, trial, features,
pricing plans, users, team, workspace, integration, API, workflow,
automation, B2B, enterprise, seats, admin
→ Load: saas.md + pricing psychology heavy + blue/purple palette

#### Fintech Triggers
Keywords: payment, banking, finance, money, transfer, invest, loan, credit,
insurance, wallet, UPI, NEFT, EMI, interest, portfolio, trading,
mutual fund, RBI, SEBI, IRDAI, gateway, settlement
→ Load: fintech.md + trust signals maximum + minimal FOMO

#### Healthcare Triggers
Keywords: doctor, health, medical, patient, appointment, clinic, hospital,
diagnosis, symptom, medicine, prescription, therapy, wellness, mental health,
consult, HIPAA, telemedicine, pharma, insurance claim
→ Load: healthcare.md + trust maximum + zero FOMO

#### Edtech Triggers
Keywords: course, learn, education, student, teacher, curriculum, certificate,
bootcamp, cohort, placement, skill, training, mentor, lecture, quiz,
assignment, syllabus, LMS, tutor, career
→ Load: edtech.md + social proof heavy + medium-high FOMO

### Multi-Industry Detection
Some products span multiple industries. Apply rules for both:
- Healthtech SaaS → fintech trust + healthcare ethics + SaaS pricing
- Edtech Fintech (ISA/EMI) → edtech FOMO + fintech trust for payment
- Ecommerce Healthcare (pharmacy) → ecommerce flow + healthcare trust
- When conflict: Always apply the MORE conservative ethics rules

## STEP 2: PRINCIPLE WEIGHT MATRIX

### How to Read This Matrix
Score 1-5: 1 = minimal application, 5 = maximum application

| Principle | Ecommerce | SaaS | Fintech | Healthcare | Edtech |
|-----------|-----------|------|---------|------------|--------|
| CTA Psychology | 5 | 5 | 4 | 3 | 5 |
| Color Psychology | 4 | 4 | 5 | 5 | 4 |
| Social Proof | 5 | 4 | 4 | 4 | 5 |
| FOMO / Scarcity | 5 | 3 | 1 | 0 | 4 |
| Eye Patterns | 4 | 4 | 4 | 4 | 4 |
| Above The Fold | 5 | 5 | 5 | 5 | 5 |
| Pricing Psychology | 4 | 5 | 3 | 2 | 5 |
| Form Psychology | 5 | 4 | 5 | 5 | 4 |
| Trust Signals | 3 | 4 | 5 | 5 | 3 |
| Avoid Dark Patterns | 4 | 4 | 5 | 5 | 4 |

### Reading the Matrix
- Above The Fold = 5 for ALL industries: Always non-negotiable
- FOMO = 0 for Healthcare: Absolute prohibition
- Trust Signals = 5 for Fintech AND Healthcare: Both require maximum trust
- FOMO = 5 for Ecommerce: Highest tolerance for urgency triggers
- Pricing Psychology = 5 for SaaS AND Edtech: Subscription and course pricing

## STEP 3: DECISION TREES

### Decision Tree 1: What CTA Color to Use?
Is industry Healthcare?

YES → Blue or Green only. Never Red or Orange for CTAs.

NO → Is industry Fintech?

YES → Blue or Green. Avoid Orange (too casual for finance).

NO → Is industry Ecommerce?

YES → Orange or Red. High impulse color.

NO → Is industry SaaS?

YES → Brand color (usually Blue or Purple). High contrast.

NO → Is industry Edtech?

YES → Orange or Purple. Energy and creativity.

### Decision Tree 2: Should I Add FOMO Elements?
Is industry Healthcare?

YES → NO FOMO. Exception: "Dr. X has 2 slots today" (factual availability only)

NO → Is industry Fintech?

YES → Minimal FOMO only. Rate validity dates acceptable. No countdown on decisions.

NO → Is this a digital product with unlimited supply?

YES → No quantity scarcity. Time scarcity only (real deadlines).

NO → Is industry Ecommerce with real stock limits?

YES → Full FOMO stack: stock + demand + timer

NO → Is industry Edtech with real cohort seats?

YES → Cohort FOMO: seats remaining + enrollment deadline

NO → Is industry SaaS with real pricing deadline?

YES → Founding pricing countdown (real deadline only)

### Decision Tree 3: How Much Social Proof is Needed?
Is this a new/unknown brand (under 2 years old or under 10K users)?

YES → Maximum social proof. Every available signal deployed.

NO → Is this a well-known brand?

YES → Selective social proof. Quality over quantity.
What type of social proof fits best?

B2C Ecommerce → Reviews + ratings + purchase counts

B2B SaaS → Logo strip + case studies + G2 badges

Fintech → Transaction volume + enterprise logos + regulatory badges

Healthcare → Doctor credentials + patient count + certifications

Edtech → Placement stats + student count + alumni company logos

### Decision Tree 4: What Goes Above The Fold?
ALWAYS above fold (no exceptions):

Clear headline (what this is)
Primary CTA
ONE trust signal

Industry-specific above fold additions:

Ecommerce product page → Product image + price + scarcity signal

SaaS homepage → Product screenshot or demo

Fintech → Regulatory badge + security claim

Healthcare → Doctor count + consultation count + warm image

Edtech → Outcome claim + cohort start date + seats remaining

### Decision Tree 5: Which Pricing Pattern to Apply?
Is this a subscription product (SaaS/Edtech)?

YES → Three-plan structure + annual toggle + highlight middle plan

NO → Is this an ecommerce product?

YES → Reference price + sale price + savings amount (both % and absolute)

NO → Is this a fintech product?

YES → Transparent fee table + cost calculator + no hidden fees

NO → Is this a healthcare product?

YES → Clear per-consultation pricing + package options + insurance info

## STEP 4: PAGE-TYPE SPECIFIC RULES

### Landing Page Rules (Any Industry)
Always apply in this order:
1. Z-pattern layout
2. Above fold: headline + sub + CTA + trust signal + hero visual
3. Social proof section immediately after hero
4. Features/benefits section
5. Testimonials above pricing
6. Pricing section
7. Final CTA section
8. Trust footer

### Product Page Rules (Ecommerce)
1. F-pattern right column: title → rating → price → variants → CTA
2. Scarcity signal within 100px of Add to Cart
3. Trust stack below Add to Cart
4. Reviews section below fold
5. Related products at bottom

### Pricing Page Rules (SaaS/Edtech)
1. Three plans: Left to right, most expensive first OR highlight middle
2. Annual toggle defaulting to annual
3. Social proof above pricing cards
4. Guarantee badge below every CTA
5. FAQ section below cards
6. Feature comparison table

### Form / Signup Page Rules
1. Social login above email form
2. Maximum 3 fields for initial signup
3. Progress bar if more than 3 fields
4. Privacy micro-copy below email field
5. CTA describes outcome, not action
6. Risk reduction below CTA

### Dashboard / App Rules
1. F-pattern layout for data-heavy screens
2. Most important metric top-left
3. Action buttons: Right side or bottom
4. Color: Green for success, Red for errors, Amber for warnings
5. Empty states: Show what filled state looks like

## STEP 5: ANTI-PATTERN RULES

### Never Apply These Combinations

#### Healthcare + Any FOMO
- No countdown timers on appointment booking
- No "X people viewing this doctor" signals
- No "Last slot today" (unless literally true and stated factually)
- No urgency copy around health decisions

#### Fintech + Aggressive Scarcity
- No "Only 3 accounts left" (absurd for digital product)
- No countdown on investment decisions
- No "Act before market changes" language
- No manufactured urgency around financial decisions

#### Any Industry + Fake Data
- No fake review counts
- No reset countdown timers
- No hardcoded "X people viewing" without real data
- No fabricated "bestseller" badges

#### Premium/Luxury + Charm Pricing
- No $99 or ₹999 for luxury products
- Round numbers ($100, ₹10,000) signal premium confidence
- Charm pricing signals discount — wrong for luxury

#### Healthcare + Dark Patterns
- Absolute prohibition: All dark patterns in healthcare
- No confirmshaming around health decisions
- No hidden costs in medical billing
- No roach motel for health subscription cancellation

## STEP 6: CONTEXT MODIFIERS

### Mobile Context (Additional Rules)
- CTA: Sticky bottom bar always
- FOMO: Badge must be visible without scrolling
- Form: Single column, larger touch targets (minimum 44px)
- Social proof: Condensed — one line, not full testimonial
- Above fold: Only 3 elements (logo + headline + CTA)

### Dark Mode Context
- Reduce saturation of all colors by 15-20%
- Background: #121212 not #000000
- Text: #E8E8E8 not #FFFFFF
- CTA: Increase brightness by 10%
- Trust badges: May need light versions

### First-Time Visitor vs Returning Visitor
- First visit: Maximum trust signals, full social proof
- Returning (logged in): Reduce trust signals, increase personalization
- Abandoned cart: FOMO + reminder of what they were looking at
- Churned user: Re-engagement focus, updated feature proof

### B2B vs B2C Modifier
- B2B: Logic first, emotion second — ROI proof, case studies
- B2C: Emotion first, logic second — desire triggers, social proof
- B2B CTA: "Request Demo" or "Contact Sales" for high-value decisions
- B2C CTA: "Get Started" or "Buy Now" — direct, immediate

## STEP 7: OUTPUT GENERATION RULES

### Psychology Decisions Table
After every UI/UX output, generate this table:

| Principle | Applied | Reason | Expected Impact |
|-----------|---------|--------|-----------------|
| CTA Psychology | [specific color + copy used] | [industry rule triggered] | [conversion lift estimate] |
| Color Psychology | [palette chosen] | [emotional goal] | [trust/urgency impact] |
| Social Proof | [type + placement] | [buyer stage need] | [trust increase] |
| FOMO | [applied/not applied + reason] | [industry rule] | [urgency impact] |
| Eye Pattern | [F or Z + why] | [page type] | [scan optimization] |
| Above Fold | [elements included] | [3-second rule] | [bounce reduction] |
| Pricing | [pattern applied] | [product type] | [revenue impact] |
| Form | [fields + friction reduction] | [completion goal] | [abandonment reduction] |
| Trust Signals | [types + placement] | [industry requirement] | [conversion impact] |
| Dark Patterns | [avoided + alternatives used] | [ethical + legal] | [long-term trust] |

### A/B Test Recommendations
Always end with 3 specific A/B test suggestions:
1. Highest impact: CTA color or copy (easiest to test, high impact)
2. Medium impact: Social proof placement or type
3. Long-term: Pricing structure or trial length

## QUICK REFERENCE CHEAT SHEET

### 30-Second Industry Decision
- Ecommerce → Red/Orange CTA + Full FOMO + Reviews prominent
- SaaS → Blue/Purple CTA + Free trial + Logo strip + Pricing psychology
- Fintech → Blue CTA + Zero FOMO + Trust maximum + Transparent pricing
- Healthcare → Blue/Green CTA + Zero FOMO + Doctor credentials + Privacy first
- Edtech → Orange CTA + Cohort FOMO + Placement stats + EMI pricing

### 3 Rules That Apply to Every Industry
1. Above the fold always has: Headline + CTA + One trust signal
2. Never use fake data for any psychology trigger
3. Dark patterns are always prohibited — they destroy long-term brand value
