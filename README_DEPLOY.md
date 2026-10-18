# Property Snaps — 2026 rebuild

**Scope:** Full replacement static website for Property Snaps, focused on Casey and Cardinia, Melbourne south-east.

## Included

- 42 hand-authored/generator-built HTML pages: homepage, full service pages, industry pages, 14 local-area pages, portfolio, About, guides, enquiry/contact, FAQs, preparation resource and privacy.
- 16 unique website-ready WebP images in `assets/images` and a full sortable/filterable portfolio.
- Three new six-page service guides in `assets/guides`: Real Estate, Builder & Trade, Pools & Outdoors. No public prices.
- Two native Netlify forms: `project-enquiry` (contact) and `guide-download` (guide request).
- Responsive design, accessible menu, sitemap, robots.txt, SEO title and description per page, LocalBusiness JSON-LD, FAQ schema, legacy redirects.

## Publish to the existing Netlify project

1. Open https://app.netlify.com/projects/propertysnaps and choose **Deploys → Deploy manually / Netlify Drop**.
2. Upload the **contents of this site zip** to the `propertysnaps` project. Netlify can accept a zip/folder. Do not make a second Netlify site.
3. In Netlify Domain management, keep `propertysnaps.com.au` and `www.propertysnaps.com.au` associated with the same site. The current primary domain was `propertysnaps.com.au` in the screenshot.
4. Confirm production visibility is Public; last screenshot showed Private because the project was not deployed yet.
5. Go to Forms to ensure both `project-enquiry` and `guide-download` are detected and form submissions are enabled. Set email notifications to the correct business inbox.
6. Submit a real test enquiry and test guide download on the deployed site. Verify SSL/DNS once propagation is complete.

## Editorial notes

- Historical content recovered from supplied 2021–22 brochures and an archived public summary of earlier Property Snaps website/social content. Direct Wayback Machine CDX/web archive retrieval was blocked in this environment; archived coverage was not exhaustive.
- Phone `0408 559 555` and email `vince@propertysnaps.com.au` were present in the supplied old brochures. **Verify they are still current before public launch.**
- No dated 2021–22 rates were included in the site or replacement guides.
- Gallery imagery has neutral subject labels only; there are no fabricated case-study or specific-property claims.
- Service statements about measured drawings, drone operations and compliance support should be reviewed against current scope/certifications.

## Maintenance

- Source images are kept separately in Dropbox `/Property Snaps/Marketing Images` once synchronization is complete.
- To replace any image while preserving page layout, keep its basename in `assets/images`; use WebP with reasonable size. Regenerating pages is done by `_build/build_site.py` in the development archive (not included in public Netlify zip).
- Contact and guide forms send submissions to the Netlify Forms dashboard. `downloads/` is a page after the form, not a password-protected distribution endpoint.
- Website CSS in `assets/site.css`, JS menu/gallery filters in `assets/site.js`.
