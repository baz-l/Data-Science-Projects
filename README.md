# Y Combinator Companies Web Scraper

## What is this?

This project is a Python script that scrapes company links from the Y Combinator website. It automates the process using Selenium, a tool for web scraping and browser automation.

## How does it work?

1. **Setup**: Make sure you have Python installed on your computer. You'll also need the Chrome browser and ChromeDriver.                                                                   
   ```
   https://getwebdriver.com/
   ```
   
2. **Installation**: Clone this repository to your computer and install the required Python libraries by running `pip install -r requirements.txt`.

3. **Running the Script**: Simply run the `All_links.py` script. It will launch a Chrome browser, go to the Y Combinator companies page, select checkboxes for each batch, extract company links from the displayed columns, and save the links to a text file named `company_links.txt`.Then run the acript `Web-scrapping.py` to scrap the information from the website and store it to `data.json`

4. **Customization**: Feel free to customize the script according to your needs. You can modify it to scrape different websites or extract different types of data.
5. Once the extraction is complete, you will find the extracted data saved in JSON format in the file data.json.
6. I have also submitted my report after the completion of the project `Web-scraping_report.pdf`

## Requirements

- Python 3.x
- Chrome browser
- ChromeDriver (compatible with your Chrome version)

## How to Use

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/baz-l/Web-Scrapping.git
   ```

2. Install the required Python libraries:

   ```
   pip install -r requirements.txt
   ```

3. Download the appropriate ChromeDriver for your Chrome version and place it in the project directory.

4. Run the script:

  

### Extracting Company Links

To extract company links from Y Combinator's website, run the following command:

```bash
python All_link.py
```

This script will extract the links and save them to a text file named `company_links.txt`.

### Web Scraping

To perform web scraping on the extracted company links, run the following command:

```bash
python Web-scrapping.py
```

This script will scrape data from each company's website and save the information in JSON format in the file `data.json`.

Make sure to install the required dependencies before running the code. See the Installation and Usage section for more details.

Feel free to adjust the file names and descriptions to match your specific project's structure and functionality. Let me know if you need further assistance!

## Acknowledgments

We would like to express our gratitude to the following individuals and organizations for their contributions and support:

- **Datahut**: We are thankful to Datahut for providing us with the opportunity to work on this project during our internship. Their guidance and mentorship have been invaluable in the development of this software.
- **Y Combinator**: We are grateful to Y Combinator for providing valuable insights into the startup ecosystem and for inspiring this project.
- **Open Source Community**: We extend our thanks to the open-source community for creating and maintaining the tools and libraries used in this project, including Selenium and ChromeDriver.
- **Contributors**: A special thank you to Sir Tony Paul who have helped improve this project through feature suggestions, and valuable insights.

Your support has been instrumental in making this project a success.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors

- Basil Eldhose(https://github.com/baz-l)
