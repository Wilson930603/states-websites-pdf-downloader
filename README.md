# **Epum - Municipality Crawlers**

Welcome to Epum's Municipality Crawlers project repository.

## **Dependencies**

Ensure the following dependencies are installed and properly configured before proceeding:

- **Python**: Version 3.11 or higher is required.
- **Conda**: Used for managing dependencies. Please ensure it is installed.

## **Setup**

Follow these steps to set up your development environment:

### **1. Install Dependencies**

```bash
bashCopy code
conda env create -f environment.yml
conda activate muni-crawlers
playwright install 
```

Install the DeploySentinel browser extension:

[DeploySentinel Recorder](https://github.com/DeploySentinel/Recorder?tab=readme-ov-file)

### **2. Run Application**

Find the crawler you wish to run under the directory `crawlers/states/`. Each crawler has its own `crawl.py` file which can be run to start the crawler.

### **3. Configuration**

Here are the links to various municipalities:

- **Zephyrhills**: [Zephyrhills Portal](https://zephyrhillsfl.portal.civicclerk.com/?category_id=29)
- **Dare**: [Dare County](https://www.darenc.gov/departments/planning/planning-board/agenda-minutes)
- **Chemung**: [Chemung County](https://www.chemungcountyny.gov/506/Chemung-County-Planning-Board)
- **Stanly**: [Stanly County](https://www.stanlycountync.gov/planning-agendas-minutes/)
- **Fanin**: [Fanin County](https://fannincountyga.com/board-of-commissioners/#minutes)

Follow these steps to configure the crawler for each municipality above:

### **1. Create Municipality Package**

Create a new package for the municipality in the `crawlers/states/` directory.

*Note: Ignore special characters in the package name and replace whitespace with an underscore (e.g. `St. John -> St_John`)

### **2. Record Browser Actions**

Record the browser actions using the DeploySentinel browser extension:

[DeploySentinel Recorder](https://github.com/DeploySentinel/Recorder?tab=readme-ov-file)

Copy the recorded actions to the `crawlers/states/<municipality>/sentinel.js` file.

*Note: DeploySentinel is a powerful tool that allows us to record browser actions and replay them in a headless browser. This is useful for automating the process of crawling websites that require user interaction. It also assists in creating the crawlers faster and more accurately.*
*Hint: Try pasting the sentinel.js code along with the website-relevant HTML and the base classes for the crawlers into a ChatGPT chat and see what it can do for you!*

### **3. Create Crawler**

Create a new crawler in the `crawlers/states/<municipality>/crawl.py` file.

*Note1: When extracting and downloading the files, make sure to only download files from 2021 onwards.*
*Note2: The `crawl()` function of the base crawler cass can be execute with `debug=True` to see the browser actions in real-time.*

### **4. Run Crawler**

Run the crawler using the `crawl.py` file. Files will be saved in the `crawlers/states/<municipality>/download_dir` directory.

### **Notes:**

- Ignore special characters in the package name and replace whitespace with an underscore (e.g. `St. John -> St_John`).
- Make sure you are connected to a US VPN since some websites will block foreign access.

### **Evaluation**

You will be evaluated based on the following criteria:

- Accuracy of the crawler
- Code quality
- Documentation
- Velocity (we ask you to be candid about the time you spent on this task)

*Bonus: If you feel the current framework lacks some features, feel free to add them and explain why you think they are necessary.*

### **Base Crawlers**

Under the `crawlers/base_crawlers` directory, you will find the base classes for some crawlers. You can extend these classes to create your own crawler.

- **base.py (BaseCrawler)**: Base class for all crawlers.
- **civicclerk.py (CivicClerkCrawler)**: Base class for all CivicClerk crawlers.
- **civicengage.py (CivicEngageCrawler)**: Base class for all CivicEngage crawlers.
- **granicus.py (GranicusCrawler)**: Base class for all Granicus crawlers.
- **legistar.py (LegistarCrawler)**: Base class for all Legistar crawlers.
- **towncloud.py (TownCloudCrawler)**: Base class for all TownCloud crawlers.
- **table_base.py (TableBaseCrawler)**: Base class for all table-based crawlers.

Every crawler needs to have a few attributes defined:

- **url**: The URL of the website to crawl.
- **commission**: The name of the commission (e.g., 'Planning Commission', 'Planning Board', 'Board of Commissioners', etc.).
- **municipality**: The name of the municipality (e.g., 'Boca Raton', 'Lee County', etc.).
- **state**: The state of the municipality (e.g., 'Florida', 'North Carolina', etc.).
- **document_type**: The type of document to download (e.g., 'Agenda Packet', 'Minutes').
- **file_extension**: File's extension (e.g., 'pdf', 'docx', etc.).

## **Logs**

Crawlers logs are available under the **`logs`** directory for each crawler.