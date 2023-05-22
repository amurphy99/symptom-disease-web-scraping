# Data Scraping for SymptomSifter

This repository contains the web scraping code used to gather data for [SymptomSifter](https://andrewemurphy.com/sd/select), a tool that facilitates symptom and disease matching based on data sourced from [MedlinePlus.gov](https://medlineplus.gov/encyclopedia.html). The code extracts relevant information from the website to build a database of known diseases and their associated symptoms.

## Data Source

All data in this project is sourced from MedlinePlus.gov, a comprehensive online health resource. The code scrapes the website to collect information on various diseases and their symptoms.

## Scraping Process

The web scraping code follows a two-step process to gather the necessary data:

1. Gathering URLs: The code initially scrapes the MedlinePlus encyclopedia to create a list of URLs for each individual entry. These URLs are extracted from pages categorized alphabetically (A-Z) and numerically (0-9).

2. Extracting Data: With the list of URLs, the code proceeds to scrape each page individually to retrieve the relevant information. Most of the pages contain a section titled "Symptoms" followed by a bulleted list of symptoms. Thus, any page featuring a section titled "Symptoms" is included as a disease, and all bullet points from the symptom section are associated with it.

## Limitations

It is important to acknowledge certain limitations of the scraping process due to the lack of standardized formatting across different pages on MedlinePlus.gov. The variation in formatting may result in some loss of context during data extraction. For instance, symptom sections may be divided into subcategories such as "in men" and "in women." Additionally, some symptoms may be described in paragraphs followed by bulleted lists, potentially omitting the symptom mentioned in the paragraph. Furthermore, variations in symptom listings pose a challenge, as there are no set regulations for the symptom entries. For example, symptoms like "jaundice" may have multiple slightly different listings, such as "yellow skin and whites of the eyes" or "yellow skin (jaundice)." Automatically matching these variations accurately can be non-trivial.

To ensure confidence in automated processes within a medical context, limited programmatic changes were made to the data. Rarities and severities were filtered out, allowing for matching of related symptoms such as "severe headaches" and "headaches" or "fever" and "fever (rare)." This basic string matching approach, combined with filtering, provides a foundational framework for the current proof-of-concept stage of the project.

## Future Development

As the SymptomSifter project progresses, incorporating additional databases and data sources will enhance the accuracy and usefulness of the tool. With an expanded range of data, more advanced matching techniques and filtering methods can be explored. The goal is to improve symptom and disease matching while maintaining confidence in the automated processes within the medical context.
