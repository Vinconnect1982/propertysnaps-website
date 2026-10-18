# Property Snaps website — deployment notes

**Site:** www.propertysnaps.com.au and propertysnaps.com.au
**Netlify project:** https://app.netlify.com/projects/propertysnaps
**Website:** 39 static pages; 16 optimised gallery images; 3 six-page PDF guides.

## Deploy to existing project
1. In the Netlify project open **Deploys**.
2. Drag the `propertysnaps-netlify-upload.zip` file into the deploy area for this *existing* project, or select **Deploy manually** and upload the ZIP.
3. Confirm the published production deploy is marked **Published**.
4. Open the custom domain, verify the HTTPS certificate, and test the two forms.

**Already configured:** Netlify Forms enabled. Site visitor access changed to public. The DNS records were added at VentraIP by the owner.

## Critical launch checks
- Check the phone number `0408 559 555` and email `vince@propertysnaps.com.au`. These appeared in 2021–22 Property Snaps brochures, so they must be confirmed before a public launch.
- Forms use native Netlify Forms and require the site to be deployed for submissions to be processed.
- `guide-download` leads to `/downloads/`, with PDFs available in `/assets/guides/`. It is a lead form, not access protection.
- Photographs of properties are newly generated marketing images and should not be assigned real client addresses or fake client testimonials. Replace imagery when verified current photos become available.
- Review brand ownership and any model/release requirements before public use.
- The custom domain's SSL certificate may take time after DNS verification.
- Remove old pricing from any other marketing material. This build and its 2026 PDFs intentionally have no rates.

## Pages
Homepage, 10 services, 5 industry pages, portfolio, 14 service suburbs, area index, about, guides, download confirmation, contact and enquiry confirmation.
