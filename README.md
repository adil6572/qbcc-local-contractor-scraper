# QBCC Local Contractor Scraper

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

Welcome to the **QBCC Local Contractor Scraper**. This repository houses a Python scraper designed to collect data from the [QBCC website](https://my.qbcc.qld.gov.au/myQBCC/s/findlocalcontractor). The QBCC (Queensland Building and Construction Commission) maintains a database of licensed building contractors in Queensland. This scraper automates the process of extracting valuable information from this source, allowing users to create datasets for analysis and other applications in the building and construction industry.

## Features

- Efficiently extracts data from the QBCC website.
- Provides a comprehensive dataset, including licensee details and contact information.
- Facilitates analysis, database creation, and can be used for lead generation

## Installation

To install the QBCC Local Contractor Scraper, follow these steps:

### Prerequisites

- Python 3.11

### Instructions

1. Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/adil6572/qbcc-local-contractor-scraper.git
   cd qbcc-local-contractor-scraper
   ```

2. Install the required Python packages:

   ```bash
   pip install beautifulsoup4 playwright
   ```

   ```bash
   playwright install
   ```

## Usage

To utilize the QBCC Local Contractor Scraper, follow these steps:

```bash
python main.py --category 'Builders' --filename 'builders.csv'
```

Note: You can replace `'Builders'` with any other category from the available options.

- Building Certifiers
- Building Inspectors
- Designers
- Client Side Project Managers
- Air Con & Refrigeration
- Bricklaying
- Carpenters
- Concretors
- Flooring
- Gasfitting
- Glass & Glazing
- Guttering
- Kitchens
- Landscaping (Structural)
- Painting
- Paving
- Pest Control (Termites)
- Plastering
- Plumbing and Drainage
- Roofs and Roof Restoration
- Screens & Grilles
- Shade Sails
- Sheds
- Soil Testing
- Swimming Pools
- Tiling
- Waterproofing
- Fire Services
- Shop fitting
- Structural Steel
- Stone Masonry

The scraped data will be saved in a CSV file with the specified filname

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
