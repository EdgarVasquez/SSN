# Validate SSN Number
## Requirements
<p>R1. The system must request the entry of 9 digits</p>
<p>R2. the SSN CODE should have divided into 3 parts separated by hyphens, the first of 3 digits, the second of 2 and the third of 4</p>
<p>R3.  the first part should have not 000 or 666 or a number between 900 and 999</p>
<p>R4.  the second part should have  between 01 and 99</p>
<p>R5.  the last part should have between 0001 and 9999</p>

## Criteria of acceptance
<p> CR 1.1 the system must validate that it has 9 digits without hyphens</p>
<p>CR 2.1 the system must validate that the first part has 3 digits, the second has 2 and the last has 5, without hyphens</p>
<p>CR 3.1 the system must validate that the first part has 3 digits and is not 000,666 or between 900 and 999 without hyphens</p>
<p>CR 4.1 the system must validate that the second part has this between 01 and 99 without hyphens</p>
<p>CR 5.1 the system must validate that the last part has this between 0001 and 9999 without hyphens</p>

## Test Plan
___<p> TC 1 A blank space is entered</p>___
<p> system response "The number of characters must be 9 and separated by hyphens"</p>
***<p> TC 2 in the first part 4 digits were entered</p>***
<p> system response "The first part must have 3 digits, it must be different from 000 and 666"</p>
 ***<p>TC 3 in the second part 3 digits were entered</p> ***
<p> system response "The second part must have 2 digits and must be greater than 01 but less than 99"</p>
***<p> TC 4 in the last part were entered "0000"</p>***
<p> system response "The third part must have 4 digits and must be greater than 0001 but less than 9999"</p>

### Positive Scenarios
<p> PS 1 123-45-6789 was entered, the system responded: Valid SSN number</p>
<p> PS 2 345-35-8457 was entered, the system responded: Valid SSN number</p>
<p> PS 3 632-98-1234 was entered, the system responded: Valid SSN number</p>
<p> PS 4 723-23-5678 was entered, the system responded: Valid SSN number</p>

### Negative Scenarios
<p>  PS 1 123-453-6789 was entered, the system responded: The number of characters must be 9 and separated by hyphens</p>
<p>  PS 2 3458-35-845 was entered, the system responded: The first part must have 3 digits, it must be different from 000 and 666</p>
<p> PS 3 632-00-1234 was entered, the system responded: The second part must have 2 digits and must be greater than 01 but less than 99</p>
<p> PS 4 723-23-0000 was entered, the system responded: The third part must have 4 digits and must be greater than 0001 but less than 9999</p>
