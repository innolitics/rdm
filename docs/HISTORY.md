# Change History

## v0.11.0

- Replace the `rdm tex` command with heavily customized pandoc calls. This simplifies
  the RDM code and allows for more easier PDF-customization.
- Add support for folders in the documents folder.
- Add support word document generation.
- Remove support for SVGs in the PDF files, which was fragile anyway since the
  SVG-to-PDF conversion is imperfect.
- Start adding a few 510(k)-related documents.
- Ignore all of the release files by default.
