# Environmental Site Survey API QA Tester

## Overview
A lightweight QA automation suite testing data validation and edge cases for an environmental site survey API, built with Python and pytest.

This project demonstrates a streamlined Quality Assurance process focusing on API endpoint reliability, data validation, and edge-case handling for engineering field data.

## Why I Built This
Effective QA is about anticipating how systems might break in the real world. Drawing on my experience building data preprocessing pipelines and managing cross-functional technical projects, I developed this test suite to showcase how I approach:
* **The Happy Path:** Ensuring valid JSON payloads (e.g., active site locations, accurate soil pH levels) process correctly with a `201 Created` status.
* **Error Handling:** Validating that missing required fields (like a forgotten location) fail gracefully with descriptive `400 Bad Request` messages rather than crashing the system.
* **Boundary Testing:** Catching physically impossible data inputs (such as a soil pH of 15.0) and ensuring the system returns a `422 Unprocessable Entity` error.

## Technologies Used
* **Python:** 
* **pytest:** Testing framework utilized for its readability and modularity.
* **Requests:** HTTP library for API interaction.

## Running the Tests
*(Note: This suite targets a mock endpoint for demonstration purposes.)*
To execute the tests locally:
1. Clone repository.
2. Install dependencies: `pip install pytest requests`
3. Run the test suite: `pytest test_site_api.py -v`
