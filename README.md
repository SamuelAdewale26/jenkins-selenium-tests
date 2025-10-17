Jenkins Selenium Tests
Automated browser testing with Selenium integrated into Jenkins CI/CD pipeline.
Overview
This repository contains automated UI tests using Selenium that run automatically through Jenkins whenever code is pushed to GitHub.
What This Does

Automates web browser testing
Runs tests automatically via Jenkins pipeline
Generates professional HTML reports
Sends email notifications on test pass/fail
Integrates with GitHub for version control

Project Structure
jenkins-selenium-tests/
├── test_google_search.py      # Selenium test cases
├── Jenkinsfile                # Jenkins pipeline configuration
├── README.md                  # This file
└── pytest.ini                 # Pytest configuration
Test Files
test_google_search.py
Contains Selenium tests for Google search functionality:

test_google_homepage_loads() - Verifies Google homepage loads
test_google_search() - Tests search functionality
test_page_title_changes() - Verifies page title updates

Requirements

Python 3.8+
pip (Python package manager)
Jenkins 2.532+
Chrome/Chromium browser
Git

Installation
Local Setup

Clone the repository:

bashgit clone https://github.com/SamuelAdewale26/jenkins-selenium-tests.git
cd jenkins-selenium-tests

Install Python dependencies:

bashpip install selenium pytest pytest-html webdriver-manager

Run tests locally:

bashpytest -v --html=report.html --self-contained-html

View test report:
Open report.html in your browser

Jenkins Setup
Prerequisites

Jenkins 2.532 installed
HTML Publisher Plugin installed
Email Extension Plugin installed
Python installed on Jenkins server

Configure Jenkins Job

Create new Pipeline job in Jenkins
Configure GitHub repository:

Repository URL: https://github.com/SamuelAdewale26/jenkins-selenium-tests.git
Script Path: Jenkinsfile


Add GitHub webhook (optional - for automatic triggering)
Run pipeline

GitHub Webhook Setup

Go to repository Settings
Click "Webhooks"
Add webhook:

Payload URL: http://localhost:8080/github-webhook/
Content type: application/json


Save

Now tests run automatically when you push to GitHub!
Pipeline Workflow

Developer pushes code to GitHub
GitHub webhook triggers Jenkins job
Jenkins pulls latest code
Jenkins installs dependencies
Tests run in headless Chrome browser
HTML report generated
Report published to Jenkins UI
Email notification sent

Running Tests
Run all tests:
bashpytest -v
Run specific test file:
bashpytest test_google_search.py -v
Run specific test:
bashpytest test_google_search.py::TestGoogleSearch::test_google_search -v
Run with HTML report:
bashpytest -v --html=report.html --self-contained-html
Run with detailed output:
bashpytest -v -s
Test Report
After running tests, open report.html to see:

Test results (Pass/Fail)
Execution time
Error messages (if any)
System information

In Jenkins, reports are published to the "Selenium Test Report" link on the build page.
Adding New Tests

Create new test function in test_google_search.py
Follow naming convention: def test_name(self, driver):
Use pytest assertions
Push to GitHub
Jenkins runs automatically

Example:
pythondef test_new_feature(self, driver):
    """Test description"""
    driver.get("https://website.com")
    element = driver.find_element(By.ID, "element_id")
    assert element.is_displayed()
Troubleshooting
Tests fail locally but pass in Jenkins

Check Chrome version compatibility
Verify ChromeDriver installation
Check Python version

Jenkins job fails

Check Jenkins console output
Verify dependencies installed
Check GitHub connection
Verify Python path is correct

Email not sending

Configure SMTP server in Jenkins
Check email address is correct
Verify credentials in Jenkins

Best Practices

Keep tests focused (one assertion per test)
Use explicit waits instead of sleep()
Clean up resources (quit driver)
Use meaningful test names
Comment complex test logic
Run tests locally before pushing
Keep test data in separate files

Resources

Selenium Documentation
Pytest Documentation
Jenkins Pipeline Guide

Maintenance

Update Selenium regularly: pip install --upgrade selenium
Review test results regularly
Add new tests for new features
Remove obsolete tests
Keep Jenkins plugins updated

Continuous Integration Status
Latest build: Check Jenkins dashboard for real-time status
Contact & Support
For questions or issues:

Check test reports for error details
Review test documentation
Check Jenkins logs

License
This project is for automation testing purposes.
Version History

v1.0 - Initial setup with basic Google search tests
Ready for expansion
