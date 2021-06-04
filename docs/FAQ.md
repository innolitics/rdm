# Frequently Asked Questions

## Customization

*We have a separate Risk Management Plan. Can we use RDM?*

Yes! We recommend replacing the content of the risk related activities in the
Software Plan with references to the Risk Management plan. Then search through
the references of the word "risk" in the Software Plan and update as necessary
(we suspect few changes will be necessary). We have used this approach on
Innolitics' client projects. You will also want to update the
`risk_matrix_location` in `system.yml`.

## Audits

*How do you exclude items from a checklist?*

For example, if you run `rdm gap 62304_2015_class_b regulatory/release/*.md`
and there are a few items that you don't want to address or are addressed
elsewhere, what do you do?

There is no mechanism to explicitly exclude items. Instead, we recommend
creating a file that includes all of the checklist items along with a
description of where they are met or why they do not need to be met.

Alternatively, if you want to make a modified copy of a built in checklist,
direct the output of the above into a file.  The format will be correct for a
checklist which you can then edit to meet your specific needs:

```
rdm gap some_checklist > my_custom_checklist.txt
```

*Can I check multiple checklists with a single `rdm gap` call?*

No, but you can create a master checklist using `include` lines in your master
checklist that reference the various standards you intend to meet.

For example if you have a class B device and want to meet the latest ISO 62304
standard as well as ISO 13485:2016 then you could use the following master
checklist:

```
include 62304_2006_AMD1_class_b
include 13485_2016
```

## PDF Formatting

*How do you add vertical lines to the edges of a table?*

Due to Pandoc's limited support for table models, this isn't very easy to do. See this [GitHub Issue](https://github.com/jgm/pandoc/issues/922).

There is a [hacky](https://github.com/jgm/pandoc/issues/922#issuecomment-833909197) approach you can use. You can also include [raw tex](https://pandoc.org/MANUAL.html#extension-raw_tex) in the Pandoc markdown.

*How do you add colspans or rowspans to a table?*

Pandoc doesn't support colspans or rowspans, since it's document model must support the least common denominator of many formats. You can, however, use [raw tex](https://pandoc.org/MANUAL.html#extension-raw_tex) if you need to.
