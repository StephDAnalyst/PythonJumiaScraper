# Jumia to MYSQL Phone Scraping Project

This project involves web scraping to extract phone information from the Jumia website, utilizing the Scrapy framework. The scraped data is validated using pipelines and then forwarded to a MySQL database for storage after running the spider.

## Components

| Spider Name          | Description                                                                                                                                                                                                                                                                                                             |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Database Connection   | Establishes a MySQL connection, prints success/error messages, and closes the connection.                                                                                                             |
| PhonespiderSpider    | Scrapes product details (URL, name, seller info, rating) from a specified URL on Jumia, following pagination and using custom settings. |
| ValphonespiderSpider | Similar to PhonespiderSpider, this spider scrapes Jumia for phone details, using pagination. Data is stored in a MySQL database via a custom pipeline.                                                            |

## ScrapeOps Proxy

This project utilizes ScrapeOps Proxy as the proxy solution. ScrapeOps offers a free plan allowing up to 1,000 requests per month, which is sufficient for testing and development.

1. Install the ScrapeOps proxy middleware:
    ```bash
    pip install scrapeops-scrapy-proxy-sdk
    ```

2. Activate the ScrapeOps Proxy by adding your API key to the settings:
    ```python
    SCRAPEOPS_API_KEY = 'YOUR_API_KEY'
    SCRAPEOPS_PROXY_ENABLED = True

    DOWNLOADER_MIDDLEWARES = {
        'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    }
    ```

## Project Overview

The project comprises several components:

1. **Scrapy Spiders**
   - Two Scrapy spiders, `PhonespiderSpider` and `ValphonespiderSpider`, scrape data from the Jumia website, following specific URLs and extracting phone-related information.

2. **Custom Settings**
   - Custom settings are defined to configure Scrapy's behavior during scraping, including settings related to robots.txt, download delays, and more.

3. **Item Models**
   - Two item models, `JumiaItem` and `JumiaphoneItem`, define the structure of scraped data.

4. **MySQL Pipeline**
   - A custom pipeline, `SaveToMySQLJumiaPipeline`, processes the scraped items and stores them in a MySQL database.

5. **Scrapy Settings**
   - Various Scrapy settings are configured to control crawling behavior, concurrent requests, download delay, and item pipelines.

## Usage

To use this project:

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate

2. Install the necessary Python libraries and dependencies, including Scrapy and the MySQL connector.

3. Configure the MySQL database settings in the `SaveToMySQLJumiaPipeline` pipeline.

4. Run the Scrapy spiders to initiate the scraping process.

## Contributing

Contributions to this project are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE), allowing for both personal and commercial use.

For more details on the components and how to use them, refer to the code and comments in the respective files. If you have any questions or issues, please reach out for assistance.
