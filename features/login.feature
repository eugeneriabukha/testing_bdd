Feature: Authentication

    Scenario: Login as a administrator and check link "Accounts Management"
         When user opens browser and navigates on the page "site.com"
             and user "admin" enters login and password in the login form
             and user clicks "Login" button on the login form
         Then user should see the link "Accounts Management"