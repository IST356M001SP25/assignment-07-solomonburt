# Reflection

Student Name:  Solomon Burt
Sudent Email:  sdburt@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

This assignment focused on web scraping a restaurant menu from Tully's Good Times website to extract menu items and store them in a CSV file. The process involved using the Playwright library for web automation, CSS selectors for identifying relevant page elements, and custom Python functions to clean and structure the extracted data. The goal was to create a structured dataset containing the category, name, price, and description of each menu item.

The assignment was structured into several key parts. menuitem.py introduced a MenuItem dataclass to represent individual menu items with attributes for category, name, price, and description. It also included methods for converting a MenuItem object to a dictionary and creating a MenuItem object from a dictionary, which provided a structured way to handle the scraped data. menuitemextractor.py contained the core logic for processing the raw text scraped from the website and converting it into MenuItem objects. The key functions implemented were: clean_price(price: str) -> float, responsible for cleaning price strings; clean_scraped_text(scraped_text: str) -> list[str], which processed the raw text of a menu item; and extract_menu_item(title: str, scraped_text: str) -> MenuItem, which orchestrated the extraction process. tully_scraper.py was the main script, responsible for navigating the Tully's Good Times menu webpage using Playwright and CSS selectors, extracting menu item data, and saving it to a CSV file. Finally, the testing phase used test_menuitemextractor.py and test_tully_scraper_output.py to verify the correctness of the code.

A primary challenge was to carefully inspect the HTML structure of the Tully's Good Times menu webpage to identify the correct CSS selectors. This involved using browser developer tools to understand the DOM hierarchy. Implementing the clean_scraped_text function required careful consideration of the different types of text present within each menu item block. The logic to filter out unwanted lines was crucial. The extract_menu_item function needed to handle cases where a menu item did not have a description. Successfully using Playwright to navigate the webpage, locate elements using CSS selectors, and extract their text required understanding the asynchronous nature of web scraping. Converting the list of dictionaries into a Pandas DataFrame provided a convenient way to structure the scraped data.

The MenuItem dataclass provided a clear and concise way to represent the structured menu data. The assignment reinforced the importance of precise CSS selectors. Cleaning and processing scraped text is a vital step in web scraping, and the assignment provided a practical understanding of a typical web scraping workflow. The included tests highlighted the importance of verifying the functionality of the code.

The scraper could be made more robust by adding more comprehensive error handling. CSS selectors and output file paths could be externalized into a configuration file. If the website used more dynamic content loading, different techniques might be necessary. For real-world scraping scenarios, implementing delays and adhering to the website's robots.txt file are crucial. Adding logging statements would provide better visibility into the scraping process.