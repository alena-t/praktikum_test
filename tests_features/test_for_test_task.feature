
Feature: Delivery cost checking
  Checks the correctness of delivery calculations in different conditions

  Scenario: Min sum of delivery
    Given I have standard delivery terms
    When I click on login button
    Then I see min sum of delivery

  Scenario: Fragile more 30 km
    Given I have fragile delivery terms
    Then I see delivery is not possible

  Scenario Outline: Change sum for distance
    Given I have <condition> delivery terms
    Then I see delivery sum is right for <result>

    Examples:
    |condition |result|
    |distance_1| sum_1|
    |distance_2| sum_2|
    |distance_3| sum_3|
    |distance_4| sum_4|

  Scenario Outline: Change sum for dimension
    Given I have <condition> delivery terms
    Then I see delivery sum is right for <result>

    Examples:
    |condition |result|
    |small     | sum_2|
    |large     | sum_3|


  Scenario Outline: Change sum for workload
    Given I have <condition> delivery terms
    Then I see delivery sum is right for <result>

    Examples:
    |condition|result|
    |normal   | sum_4|
    |increased| sum_5|
    |high     | sum_6|
    |very high| sum_7|
