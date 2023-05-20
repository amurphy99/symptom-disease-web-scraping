#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:05:26 2023

@author: andrewmurphy
"""

import requests
from bs4 import BeautifulSoup







def get_page_entry(URL):

    #URL  = "https://medlineplus.gov/ency/article/001654.htm"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")


    # Page title and summary
    # -----------------------
    page_content = soup.find_all("div", id="mplus-content")

    # Page URL
    page_URL = page_content[0].find("span", class_="page-url").contents[0]
    page_URL = page_URL.split("//")[1]
    page_URL = page_URL.strip(" ").strip("\n").strip("\r")
    if "sorrypages" in page_URL:
        print(URL)
        return None

    # Page Title
    page_title = page_content[0].find("div", class_="page-title")
    page_title = page_title.find("h1").contents[0]

    # Page Summary
    page_summary = page_content[0].find("div", id="ency_summary")
    #page_summary = page_summary.find("p").contents[0]
    page_summary = page_summary.find("p").get_text().replace('\n', ' ').replace('\r', '')


    symptoms_section = -1


    # Get each section
    # -----------------------
    page_sections = page_content[0].find_all("section")

    finished_sections = []
    i = -1
    for section in page_sections:
        i += 1
        current_section = section

        # Section Title
        section_title = current_section.find("div", class_="section-title")
        section_title = section_title.find("h2")
        if section_title == None:   section_title = ''
        else:                       section_title = section_title.contents[0]
        section_title = section_title.strip(" ")


        # Check if section title is Symptoms
        if section_title == "Symptoms":
            symptoms_section = i


        # Section Body
        section_body = current_section.find("div", class_="section-body")
        if section_body == None: section_body = []

        finished_section_body = []
        for element in section_body:
            element_tag = element.name
            
            if element_tag == 'p':
                element_contents = element.get_text().replace('\n', '').replace('\r', '').strip()
                
            elif element_tag == 'ul' or element_tag == 'ol':
                element_contents_raw = element.contents
                element_contents = []
                for item in element_contents_raw:
                    element_contents.append(item.get_text().replace('\n', '').replace('\r', '').strip())

            
            # this shouldn't happen
            else:
                element_contents = element.get_text().strip("\n").strip("\r")
            
            # create the final section body item
            section_body_item = (element_tag, element_contents)
            finished_section_body.append(section_body_item)


        finished_section = [section_title, finished_section_body]
        finished_sections.append(finished_section)


    # return completed page
    finished_page = [page_URL, page_title, page_summary, finished_sections, symptoms_section]
    return finished_page






















































































# end