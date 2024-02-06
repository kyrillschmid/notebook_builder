import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


def get_java_doc_html(topic):
    url = f"https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    # page_content = soup.find("div", id="PageContent")
    page_content = soup.find("div", class_="article_content")
    if page_content:
        content = str(page_content)
        filename = f"output/{topic}.html"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Content within 'PageContent' saved to {filename}")
    else:
        print("'PageContent' div not found in the HTML.")
    return content


allowed_tags = ["div", "section", "h1", "h2", "h3", "h4", "h5", "h6", "p"]


def get_python_org_html():
    url = f"https://docs.python.org/3/tutorial/introduction.html#numbers"
    response = requests.get(url)
    html_content = response.content

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Function to remove all tags except for the allowed ones
    def clean_html(soup, allowed_tags):
        for tag in soup.find_all(True):
            if tag.name not in allowed_tags:
                tag.unwrap()  # Remove the tag but keep its content

    # List of allowed tags

    # Clean the HTML
    body_div = soup.find("div", class_="body")

    # Check if the div exists
    if body_div:
        # Clean the HTML inside the div
        clean_html(body_div, allowed_tags)

        body_str = str(body_div)

        # Split the string at each <h2> tag
        split_content = body_str.split("<h2>")

        # Re-add the <h2> tag that was removed during splitting, except for the first segment
        split_content = [
            segment if i == 0 else "<h2>" + segment
            for i, segment in enumerate(split_content)
        ]

        with open("output/parsed_html.txt", "w", encoding="utf-8") as file:
            for index, segment in enumerate(split_content):
                # Write each segment to the file
                file.write(f"Segment {index+1}:\n{segment}\n{'-' * 20}\n\n")

        return split_content

    else:
        print("No div with class 'body' found.")


def split_on_h2(soup):
    segments = []
    current_segment = []
    start_new_segment = False

    for element in soup.descendants:
        if element.name == "h2":
            if current_segment:
                segments.append("".join(str(e) for e in current_segment))
                current_segment = [element]
            else:
                start_new_segment = True
                current_segment.append(element)
        elif start_new_segment and (
            isinstance(element, NavigableString) or element.name in allowed_tags
        ):
            current_segment.append(element)

    if current_segment:
        segments.append("".join(str(e) for e in current_segment))

    return segments


def get_data_science_handbook_html(args):
    assert args.url != "--", "Please provide a url to the html file."
    url = args.url
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    # Remove all <a> elements
    for a_tag in soup.find_all("a"):
        a_tag.decompose()

    for code_tag in soup.find_all("code"):
        code_text = code_tag.get_text()
        new_text = f"`{code_text}`"
        code_tag.replace_with(new_text)

    # Find all divs that contain the spans you want to group
    highlight_divs = soup.find_all("div", class_="highlight hl-ipython3")

    for div in highlight_divs:
        # Extract text from all span elements within the div
        span_texts = [span.get_text() for span in div.find_all("span")]

        combined_text = " ".join(span_texts)

        # Create a new code element with the combined text
        new_code_tag = soup.new_tag("code")
        new_code_tag.string = combined_text
        # print(new_code_tag)
        # Replace the div with the new code element
        div.replace_with(new_code_tag)

    # Extracting the <header>
    article = soup.find("article")

    result = []
    current_section = []

    def should_include(tag):
        # Determines if the tag should be included in the output
        if tag.name in ["header", "code", "h2"]:
            return True
        if tag.name == "p" and tag.find_parent("div", class_="text_cell_render"):
            return True
        if tag.name == "span" and tag.find_parent("div", class_="highlight"):
            return True
        return False

    for element in article.descendants:
        if element.name == "h2":
            # Include the <h2> element in the current section
            current_section.append(str(element))
            # Finalize the current section and start a new one
            result.append("".join(current_section))
            current_section = []
        if should_include(element):
            # Add other relevant elements to the current section
            current_section.append(str(element))

    # Add the last section if it's not empty
    if current_section:
        result.append("".join(current_section))

    # Save the content to a file
    with open("output/data_science_1.txt", "w", encoding="utf-8") as file:
        for index, segment in enumerate(result):
            # Write each segment to the file
            file.write(f"Segment {index+1}:\n{segment}\n{'-' * 20}\n\n")

    return result


def get_green_tea_press_html(args):
    assert args.url != "--", "Please provide a url to the html file."
    url = args.url
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "lxml")

    # Find and replace <pre class="verbatim"> with <code>

    for pre_tag in soup.find_all("pre", {"class": "verbatim"}):
        # Create a new <code> tag
        code_tag = soup.new_tag("code")
        code_tag.string = pre_tag.string
        # Replace the <pre> tag with the <code> tag
        pre_tag.replace_with(code_tag)

        # Initialize a list to hold the text blocks
        text_blocks = []

        # Find all h1, h2, and h3 elements
        headers = soup.find_all(["h1", "h2", "h3"])

    for header in headers:
        # Remove class and id attributes from the header
        header.attrs = {}  # This clears all attributes, making the tag cleaner

        # Initialize the current block with the header itself
        current_block = [str(header)]

        # Iterate over the siblings of the header
        for sibling in header.find_next_siblings():
            # Break the loop if another header is found
            if sibling.name in ["h1", "h2", "h3"]:
                break
            # Skip specified tags
            if sibling.name not in ["a", "td", "tr"]:
                # Append <code> tags directly, get text for others
                if isinstance(sibling, Tag) and sibling.name == "code":
                    current_block.append(str(sibling))
                else:
                    # Only append the text content if it's not empty or just space
                    sibling_text = sibling.get_text(strip=True)
                    if sibling_text:
                        current_block.append(sibling_text)

        # Join the texts and tags in the current block into one string
        block_text = " ".join(current_block)
        text_blocks.append(block_text.strip())

    # Save the content to a file
    with open("output/green-tea/green-tea.txt", "w", encoding="utf-8") as file:
        for index, segment in enumerate(text_blocks):
            # Write each segment to the file
            file.write(f"Segment {index+1}:\n{segment}\n{'-' * 20}\n\n")

    return text_blocks


def get_raw_py_file(args):
    assert args.url != "--", "Please provide a url to the html file."
    url = args.url
    response = requests.get(url)
    # print(response.text)
    return response.text
