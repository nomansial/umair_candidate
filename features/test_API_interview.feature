
  Feature: Validate Json Schema

    @test
    Scenario: write api test to validate json schema and to make sure all the values are present
      Given api url is provided
      When user hits api url
      Then response is retrieved
