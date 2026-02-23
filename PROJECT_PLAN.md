# 🌐 SALWAUAE.COM — Website Development Project Plan

## 1. Project Overview

**Goal:** Develop a modern multi-business website representing Salwa brand divisions (Studio, Cafe, Bookshop, Perfume, Electricals) with strong visual branding, enquiry functionality, and portfolio showcasing.

**Primary Inspiration:** tata.com (structure), tatamotors.com (animation), joescafedubai.com & deirastarsdubai.com (business sections)

**Core Message:** **"FEEL THE REALITY"**

**Tech Stack:** HTML/CSS/JS (frontend), Django (backend), SQLite (database).

---

## 2. Website Structure (Sitemap)

### Main Website 🏠
| Page | Status | Notes |
|------|--------|--------|
| Home | ✅ | home2.html – hero "Feel the Reality", division cards, inline viewer, logo, meta |
| About / Company Overview | ✅ | Full page, division links, extends division_base |
| Business Divisions (Cards) | ✅ | On home + "Full page" links to division pages |
| Careers | ✅ | Page + WhatsApp apply CTA |
| Contact | ✅ | WhatsApp + social links from settings |
| Social Media Integration | ✅ | Footer (home + all pages); Instagram/Facebook/LinkedIn from settings |
| Header + Logo Branding | ✅ | Logo from `static/logos/logo.png` with text fallback site-wide |

### Business Division Pages 🏢
| Division | Theme | Status |
|----------|--------|--------|
| **Salwa Studio** | B&W, Yellow + Red | ✅ Full page: 4 branches, services, portfolio, reviews placeholder, enquiry→WhatsApp |
| **Salwa Perfume** | Gold & White, Black | ✅ Full page: brand bio, enquiry→WhatsApp |
| **Salwa Bookshop** | Royal Green, Beige | ✅ Full page: stationery, printing A0–A6, enquiry→WhatsApp |
| **Salwa Cafe** | Black & Pink, White | ✅ Full page: services (free delivery), menu link, reviews placeholder, enquiry→WhatsApp |
| **Salwa Electricals** | Blue/dark (TBD) | ✅ Full page: product/service info, enquiry→WhatsApp |

---

## 3. Design Requirements

- **UI/UX:** Corporate premium, smooth animations, card-based divisions, responsive mobile-first.
- **Branding:** Logo, color-coded divisions, consistent typography, social embedding.

---

## 4. Functional Requirements

- **Core:** Responsive, SEO-friendly, fast loading, contact/enquiry forms, Google reviews, Instagram, portfolio gallery.
- **Enquiry:** Redirect to WhatsApp (per plan).
- **Optional:** CMS, analytics, booking/order, multi-language.

---

## 5. Development Phases (from plan)

| Phase | Focus | Deliverables |
|-------|--------|--------------|
| 1 — Planning | Requirements, branding, sitemap, content | Wireframes, tech stack ✅ |
| 2 — UI/UX (2 weeks) | Homepage, division cards, mobile, animation | Design mockups |
| 3 — Development (3–5 weeks) | Frontend + backend, enquiry→WhatsApp, social | Working prototype |
| 4 — Testing (1 week) | Mobile, Lighthouse 80+, SEO, bugs | QA report |
| 5 — Deployment (3–5 days) | salwauae.com, hosting, SSL | Live site |

---

## 6. Content Needed From Client

- [x] Logo files (in `static/logos/`)
- [ ] Brand colors confirmation (check Instagram)
- [ ] Business descriptions
- [ ] Portfolio images
- [ ] Branch details
- [ ] Contact info
- [ ] Social media credentials (if embedding)

---

## 7. Division Specs (Summary)

- **Studio:** 4 branches, services, branch detail pages, enquiry (branch-specific), portfolio, Google reviews, optional rating, frames showcase.
- **Perfume:** Brand bio, enquiry (lowest priority).
- **Bookshop:** Stationery, printing A0–A6, enquiry.
- **Cafe:** Free delivery, Google reviews, enquiry, menu.
- **Electricals:** Product/service info, contact/enquiry.

---

## 8. Risks / Challenges

- Content delays  
- Changing requirements  
- Animation complexity  
- Review API integration limits  

---

*Last updated to align codebase with plan: hero "FEEL THE REALITY", main nav/footer, About/Careers/Contact routes, division deep links.*
