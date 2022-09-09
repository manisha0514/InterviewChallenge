
# UK Postcode formatting and Validation

## File Structure
    Exercise2-postcodeUK
      ---Database
          Contains all the UK postcode which we will be using for validation
      ---PostCodeUK
          ---TestResults
              stores the results from testing formatting and validation module
              
              Format : test-formating.csv(regex validation)
              PostCode   TestResults
              AA1A 1A     Fail
              A1 1AA      Pass
              
              Format : test-validation.csv(checks if the postcode is in database or not)
              PostCode   TestResults
              AA1A 1A     Fail
              A1 1AA      Fail
              
          ---postcode_test.py
              formating and validation python file used by --main-- file inside UK-postcode-lib
              
          ---test_cases.csv
              Format : test-formating.csv(regex validation)
              PostCode   
              AA1A 1A     
              A1 1AA     
              ### add your test codes here
              Run ## postcode_test.py file in pycharm environment to get the test results
          
      ---tests
          Contains unittest python file and testcases
          
      ---UK-postcode-lib
          library for validating the postcode
          Example :
          Run ### python UK-postcode-lib AA1A 1AA
