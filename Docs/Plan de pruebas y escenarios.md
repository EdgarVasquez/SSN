# Validate SSN Number
## Requirements
-R1. The system must request the entry of 9 digits
-R2. the SSN CODE should have divided into 3 parts separated by hyphens, the first of 3 digits, the second of 2 and the third of 4
-R3.  the first part should have not 000 or 666 or a number between 900 and 999
-R4.  the second part should have  between 01 and 99
-R5.  the last part should have between 0001 and 9999

## Criteria of acceptance
#### CR 1.1 the system must validate that it has 9 digits without hyphens
#### CR 2.1 the system must validate that the first part has 3 digits, the second has 2 and the last has 5, without hyphens
#### CR 3.1 the system must validate that the first part has 3 digits and is not 000,666 or between 900 and 999 without hyphens
#### CR 4.1 the system must validate that the second part has this between 01 and 99 without hyphens
#### CR 5.1 the system must validate that the last part has this between 0001 and 9999 without hyphens

## Test Plan
#### TC 1 A blank space is entered
#### system response "The number of characters must be 9 and separated by hyphens"
#### TC 2 in the first part 4 digits were entered
#### system response "The first part must have 3 digits, it must be different from 000 and 666"
#### TC 3 in the second part 3 digits were entered
#### system response "The second part must have 2 digits and must be greater than 01 but less than 99"
#### TC 4 in the last part were entered "0000"
#### system response "The third part must have 4 digits and must be greater than 0001 but less than 9999"

### Positive Scenarios
#### PS 1 123-45-6789 was entered, the system responded: Valid SSN number
#### PS 2 345-35-8457 was entered, the system responded: Valid SSN number
#### PS 3 632-98-1234 was entered, the system responded: Valid SSN number
#### PS 4 723-23-5678 was entered, the system responded: Valid SSN number

### Negative Scenarios
#### PS 1 123-453-6789 was entered, the system responded: The number of characters must be 9 and separated by hyphens
#### PS 2 3458-35-845 was entered, the system responded: The first part must have 3 digits, it must be different from 000 and 666
#### PS 3 632-00-1234 was entered, the system responded: The second part must have 2 digits and must be greater than 01 but less than 99
#### PS 4 723-23-0000 was entered, the system responded: The third part must have 4 digits and must be greater than 0001 but less than 9999
