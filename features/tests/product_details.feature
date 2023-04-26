# Created by swomb at 4/6/2023
Feature: Tests for product page
  # Enter feature description here

  Scenario: User can add a product to a cart
    Given Open Product sunscreen-spf-30 Details page
    When Click to add product to cart
    Then Verify product has been added to cart
    When Click "View my cart"
    Then Verify user is taken to the cart page