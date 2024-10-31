# London GitHub Users Data Scraper

## Overview

This project aims to scrape data from GitHub for users located in London who have over 500 followers. The collected data includes user information and their repositories, providing insights into their activities and contributions on GitHub. 

## Table of Contents

- [Introduction](#introduction)
- [Data Collected](#data-collected)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In today's digital age, GitHub is a pivotal platform for developers to showcase their work and collaborate on projects. This project aims to identify and analyze GitHub users from London, specifically focusing on their public repositories and activity metrics.

## Data Collected

The project collects the following data for each user:
- `login`: GitHub username
- `name`: Full name of the user
- `company`: Company associated with the user
- `location`: User's location
- `email`: User's email address (if available)
- `hireable`: Indicates if the user is open to job opportunities
- `bio`: User's bio description
- `public_repos`: Number of public repositories
- `followers`: Number of followers
- `following`: Number of users they follow
- `created_at`: Account creation date

The project also gathers data on users' repositories, including:
- `full_name`: Full name of the repository
- `created_at`: Repository creation date
- `stargazers_count`: Number of stars the repository has received
- `watchers_count`: Number of users watching the repository
- `language`: Primary programming language used in the repository
- `has_projects`: Whether the repository has projects enabled
- `has_wiki`: Whether the repository has a wiki enabled
- `license_name`: The license type of the repository

## Technologies Used

- Python
- Pandas
- Requests (for API calls)
- GitHub API
- Jupyter Notebooks / Google Colab (for analysis)


