# Contrib

This directory contains scripts and other files which, while they may be useful to people using RDM, weren't generic enough to include in the default RDM templates. Most of these scripts must be copied and inserted into your build process.

See below for a brief description of each of the scripts.

## [GitHub Workflow](https://github.com/innolitics/rdm/tree/main/contrib/github_workflow.yml)

One benefit of storing the design history file in the Git repository alongside the code is that you can easily generate the documents for various versions of the code. This GitHub workflow will generate the release PDFs or word documents and store them as artifacts.

## [Simple Requirements Format](https://github.com/innolitics/rdm/tree/main/contrib/convert_requirements.py)

This script lets you write software requirements in a simpler format that looks like this:

```
1 Hardware
1.1 First requirements goes here.

2 Loading
2.1 Second requirement goes here.

# Comments start with a "#" and are ignored by the converter
3 Users
3.1 Third requirement goes here.
3.2 Fourth requirement goes here.
3.3 User logins
3.3.1 Fifth requirement goes here.
3.3.2 Sixth requirement goes here.
3.4 Seventh requirement goes here.
```

The script converts this format into a YAML format that can be consumed by the `rdm render` command. This script illustrates that you can customize RDM to your project's unique needs.

## [Download Linked Images](https://github.com/innolitics/rdm/tree/main/contrib/download_images.py)

Markdown lets you include images from web links while latex does not. This script solves this problem. To use it, filter your markdown through it before sending it to pandoc for PDF conversion.

The script parses markdown from stdin, downloads any linked images to directory provided as the first argument, swaps out the URL for the local path, and write the updated markdown to stdout.

Only images linked with a URL with an http or https scheme are included.

The downloaded files retain the extension present in the path portion of the URL, but the name is replaced with the sha256 hash of their contents.

## [Format Packages](https://github.com/innolitics/rdm/tree/main/contrib/format_packages.py)

For some projects, it may be useful to include the list of installed packages in the test record. To use this script, save the output of `dpkg -l` to a text file, then use that file as the input argument.

The script formats the contents of the packages file into a YAML document, allowing for easy inclusion of the package list into the markdown templates.

To add such a table, use the following template or modify it as needed:

```
## Installed System Packages

| Desired/Status/Error | Name | Version |
| --- | --- | --- |
{% for package_name in packages -%}
| {{ packages[package_name].states }} | {{ package_name }} | {{ packages[package_name].version }} |
{% endfor -%}
```
