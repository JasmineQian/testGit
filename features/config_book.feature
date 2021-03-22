Feature: stage 01 This is a test

  Scenario: This is a test sample
    Given I have a book and its name is learn
    And I have finished 20 pages
    When I begin to read the 21 page
    And I read 10 pages
    Then I verify the next time I should read from Page 31

