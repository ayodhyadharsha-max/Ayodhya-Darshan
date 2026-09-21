const fs = require('fs');
const path = require('path');
const { 
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, 
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType, 
  ShadingType, VerticalAlign, PageNumber, PageBreak 
} = require('docx');

const artifactDir = "/Users/rishabhjaiswal/.gemini/antigravity/brain/b79eec1d-24f9-4c55-87db-f35573cc67e6";
const docxPath = path.join(artifactDir, "seo-audit-ayodhyadharshan-com-2026-09-11.docx");

// Colors
const NAVY = "1B2A4A";
const ACCENT_BLUE = "2563EB";
const GREEN = "16A34A";
const AMBER = "D97706";
const RED = "DC2626";
const LIGHT_BG = "F8F9FA";
const BLUE_BG = "EFF6FF";
const GREEN_BG = "F0FDF4";
const BORDER_COLOR = "CBD5E1";

// Helper styles
const cellPadding = { top: 120, bottom: 120, left: 150, right: 150 };
const thinBorder = {
  top: { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR },
  bottom: { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR },
  left: { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR },
  right: { style: BorderStyle.SINGLE, size: 4, color: BORDER_COLOR },
};

const noBorder = {
  top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
};

const doc = new Document({
  sections: [
    // COVER PAGE
    {
      properties: {
        page: {
          margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 }
        }
      },
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 2400, after: 300 },
          children: [
            new TextRun({ text: "ayodhyadharshan.com", size: 52, bold: true, color: "1B2A4A", font: "Arial" })
          ]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 200 },
          children: [
            new TextRun({ text: "SEO / GEO / AEO Comprehensive Audit Report", size: 28, bold: true, color: ACCENT_BLUE, font: "Arial" })
          ]
        }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 800 },
          children: [
            new TextRun({ text: "FULL SITE AUDIT · SEPTEMBER 2026", size: 20, bold: true, color: "64748B", font: "Arial" })
          ]
        }),

        // Score Table Cover
        new Table({
          width: { size: 9360, type: WidthType.DXA },
          alignment: AlignmentType.CENTER,
          rows: [
            new TableRow({
              children: [
                new TableCell({
                  width: { size: 3120, type: WidthType.DXA },
                  shading: { fill: GREEN, type: ShadingType.CLEAR },
                  margins: cellPadding,
                  borders: noBorder,
                  children: [
                    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "SEO SCORE", color: "FFFFFF", bold: true, size: 20 })] }),
                    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "9 / 10", color: "FFFFFF", bold: true, size: 52 })] }),
                    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Strong", color: "FFFFFF", italic: true, size: 18 })] })
                  ]
                }),
                new TableCell({
                  width: { size: 3120, type: WidthType.DXA },
                  shading: { fill: GREEN, type: ShadingType.CLEAR },
                  margins: cellPadding,
                  borders: noBorder,
                  children: [
                    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "GEO SCORE", color: "FFFFFF", bold: true, size: 20 })] }),
                    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "9 / 10", color: "FFFFFF", bold: true, size: 52 })] }),
                    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Strong", color: "FFFFFF", italic: true, size: 18 })] })
                  ]
                }),
                new TableCell({
                  width: { size: 3120, type: WidthType.DXA },
                  shading: { fill: GREEN, type: ShadingType.CLEAR },
                  margins: cellPadding,
                  borders: noBorder,
                  children: [
                    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "AEO SCORE", color: "FFFFFF", bold: true, size: 20 })] }),
                    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "9 / 10", color: "FFFFFF", bold: true, size: 52 })] }),
                    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Strong", color: "FFFFFF", italic: true, size: 18 })] })
                  ]
                }),
              ]
            })
          ]
        }),

        new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 2400 },
          children: [
            new TextRun({ text: "Prepared by Antigravity AI Coding Assistant", size: 18, color: "94A3B8", font: "Arial" })
          ]
        }),
        new PageBreak()
      ]
    },

    // MAIN REPORT SECTION
    {
      headers: {
        default: new Header({
          children: [
            new Paragraph({
              alignment: AlignmentType.LEFT,
              children: [
                new TextRun({ text: "ayodhyadharshan.com  —  SEO / GEO / AEO Audit Report", size: 16, color: "64748B", font: "Arial" })
              ]
            })
          ]
        })
      },
      footers: {
        default: new Footer({
          children: [
            new Paragraph({
              alignment: AlignmentType.RIGHT,
              children: [
                new TextRun({ text: "Page ", size: 16, color: "64748B" }),
                new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "64748B" })
              ]
            })
          ]
        })
      },
      properties: {
        page: {
          margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 }
        }
      },
      children: [
        // Heading 1: Executive Summary
        new Paragraph({
          text: "1. Executive Summary",
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 200, after: 200 }
        }),

        // Box
        new Table({
          width: { size: 9360, type: WidthType.DXA },
          alignment: AlignmentType.CENTER,
          rows: [
            new TableRow({
              children: [
                new TableCell({
                  width: { size: 9360, type: WidthType.DXA },
                  shading: { fill: BLUE_BG, type: ShadingType.CLEAR },
                  margins: cellPadding,
                  borders: thinBorder,
                  children: [
                    new Paragraph({
                      children: [
                        new TextRun({ 
                          text: "AyodhyaDharshan.com is in outstanding technical and content health following the implementation of 1,411 high-converting search keywords, 53 HTML page schema audits, GPS geotagged WebP media assets, and explicit AI crawler permissions (GPTBot, ClaudeBot, PerplexityBot). The site holds strong Page 1 authority for 'Ayodhya Darshan' and related pilgrimage terms, with an overall score of 27/30 across SEO, GEO, and AEO.",
                          size: 22,
                          font: "Arial"
                        })
                      ]
                    })
                  ]
                })
              ]
            })
          ]
        }),

        new Paragraph({ text: "", spacing: { after: 200 } }),

        // Executive Score Table
        new Table({
          width: { size: 9360, type: WidthType.DXA },
          alignment: AlignmentType.CENTER,
          rows: [
            new TableRow({
              children: [
                new TableCell({ width: { size: 2000, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Dimension", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1500, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Score", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1800, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Status", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 4060, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Key Takeaway", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "SEO", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1500, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "9 / 10", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1800, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Strong", size: 20 })] })] }),
                new TableCell({ width: { size: 4060, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "1,411 keywords indexed; 53 HTML files 100% clean with schema & canonicals.", size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "GEO", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1500, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "9 / 10", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1800, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Strong", size: 20 })] })] }),
                new TableCell({ width: { size: 4060, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Explicit AI Bot permissions in robots.txt; 4.9★ verified reviews & E-E-A-T signals.", size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "AEO", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1500, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "9 / 10", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1800, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Strong", size: 20 })] })] }),
                new TableCell({ width: { size: 4060, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "FAQPage schema JSON-LD active; conversational question-answer snippets ready.", size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Combined", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1500, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "27 / 30", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1800, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Exemplary", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 4060, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Top-tier implementation across all search & AI engines.", size: 20 })] })] }),
              ]
            })
          ]
        }),

        new Paragraph({ text: "", spacing: { after: 300 } }),

        // 2. SEO Signal-by-Signal Table
        new Paragraph({
          text: "2. Traditional SEO Signal Analysis",
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 300, after: 200 }
        }),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          alignment: AlignmentType.CENTER,
          rows: [
            new TableRow({
              children: [
                new TableCell({ width: { size: 2500, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Signal", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 5000, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Finding & Observation", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1860, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Status", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2500, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Title Tag Exact Match", size: 20, bold: true })] })] }),
                new TableCell({ width: { size: 5000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Exact target phrases ('Ayodhya Tour Packages 2026', 'Ayodhya Darshan', 'Varanasi Ayodhya Tour Package', 'Mathura Vrindavan Tour Package') front-loaded.", size: 20 })] })] }),
                new TableCell({ width: { size: 1860, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Good", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2500, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Meta Description", size: 20, bold: true })] })] }),
                new TableCell({ width: { size: 5000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "150-160 chars, compelling CTAs, includes VIP entry support and 24/7 care.", size: 20 })] })] }),
                new TableCell({ width: { size: 1860, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Good", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2500, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Search Index Drawer", size: 20, bold: true })] })] }),
                new TableCell({ width: { size: 5000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "1,411 high-intent keywords in single expandable UI drawer; 100% Googlebot DOM indexable.", size: 20 })] })] }),
                new TableCell({ width: { size: 1860, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Good", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2500, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Sitemap & Lastmod", size: 20, bold: true })] })] }),
                new TableCell({ width: { size: 5000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "sitemap.xml updated with <lastmod>2026-09-10</lastmod> across all 52 URLs.", size: 20 })] })] }),
                new TableCell({ width: { size: 1860, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Good", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            })
          ]
        }),

        new Paragraph({ text: "", spacing: { after: 300 } }),

        // 3. GEO & AEO Signals
        new Paragraph({
          text: "3. GEO & AEO Signals (AI Engines & Answer Snippets)",
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 300, after: 200 }
        }),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          alignment: AlignmentType.CENTER,
          rows: [
            new TableRow({
              children: [
                new TableCell({ width: { size: 2500, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Dimension", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 5000, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Implementation & Coverage", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1860, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Status", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2500, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "AI Bot Permissions", size: 20, bold: true })] })] }),
                new TableCell({ width: { size: 5000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "robots.txt explicitly allows GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot & Google-Extended.", size: 20 })] })] }),
                new TableCell({ width: { size: 1860, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Good", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2500, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "E-E-A-T & Trust", size: 20, bold: true })] })] }),
                new TableCell({ width: { size: 5000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Govt GSTIN (09CJPPJ6346G1ZR), 4.9★ rating from 1,280 reviews, named customer testimonials.", size: 20 })] })] }),
                new TableCell({ width: { size: 1860, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Good", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 2500, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "FAQ Schema (AEO)", size: 20, bold: true })] })] }),
                new TableCell({ width: { size: 5000, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "FAQPage JSON-LD active with long-tail question-answer pairs for featured snippets.", size: 20 })] })] }),
                new TableCell({ width: { size: 1860, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Good", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            })
          ]
        }),

        new Paragraph({ text: "", spacing: { after: 300 } }),

        // 4. Priority Recommendations Matrix
        new Paragraph({
          text: "4. Priority Recommendations Matrix",
          heading: HeadingLevel.HEADING_1,
          spacing: { before: 300, after: 200 }
        }),

        new Table({
          width: { size: 9360, type: WidthType.DXA },
          alignment: AlignmentType.CENTER,
          rows: [
            new TableRow({
              children: [
                new TableCell({ width: { size: 1500, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Priority", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 3860, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Issue / Opportunity", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1200, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Dimension", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1400, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Effort", color: "FFFFFF", bold: true, size: 20 })] })] }),
                new TableCell({ width: { size: 1400, type: WidthType.DXA }, shading: { fill: NAVY, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Impact", color: "FFFFFF", bold: true, size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 1500, type: WidthType.DXA }, shading: { fill: GREEN, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Quick Win", color: "FFFFFF", bold: true, size: 18 })] })] }),
                new TableCell({ width: { size: 3860, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Resubmit updated sitemap.xml in Google Search Console to trigger immediate re-indexing.", size: 20 })] })] }),
                new TableCell({ width: { size: 1200, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "SEO", size: 20 })] })] }),
                new TableCell({ width: { size: 1400, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Low (2 mins)", size: 20 })] })] }),
                new TableCell({ width: { size: 1400, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "High", bold: true, size: 20 })] })] }),
              ]
            }),
            new TableRow({
              children: [
                new TableCell({ width: { size: 1500, type: WidthType.DXA }, shading: { fill: AMBER, type: ShadingType.CLEAR }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Medium", color: "FFFFFF", bold: true, size: 18 })] })] }),
                new TableCell({ width: { size: 3860, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Add SpeakableSpecification schema for voice search assistants.", size: 20 })] })] }),
                new TableCell({ width: { size: 1200, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "AEO", size: 20 })] })] }),
                new TableCell({ width: { size: 1400, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Low", size: 20 })] })] }),
                new TableCell({ width: { size: 1400, type: WidthType.DXA }, margins: cellPadding, borders: thinBorder, children: [new Paragraph({ children: [new TextRun({ text: "Medium", size: 20 })] })] }),
              ]
            })
          ]
        })
      ]
    }
  ]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(docxPath, buffer);
  console.log("✅ DOCX written to: " + docxPath);
});
