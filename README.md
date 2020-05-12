# Congress_Senate_Analysis
 Analysing by clustering all 100 American Congress Senates(same/different parties) based on each individuals' voting histories from 28 different acts/policies in the year 2016

 ### Algorithm in english(custom k_means)
    - Pick arbituary point as guesses for the center of each group
    - Assign all the data points to the closest maching group
    - Within each group, average the points to get to a new guess
    - For the center of the group
    - Repeat multiple times: assign data and average the points

### Clean, Fast, Readable and Memory effecient Code

> - [x] Using DefaultDict to Accumulate Votes from all different bills
> - [x] Using Counter to count all senators with same voting patterns
> - [x] Using python comprehentions to make business logic clearer
> - [x] Using Iterator Protocols to save memory and increase execution time
> - [x] Improving Function definition and Tuple structures for comeback code readibility

### Testing done using
> - [x] Pytest
> - [x] PyFlakes

## Output
-------------- CLUSTER 1 --------------\
Senator(name='Sen. James Lankford [R]', party='Republican', state='OK')\
Senator(name='Sen. Dan Sullivan [R]', party='Republican', state='AK')\
Senator(name='Sen. Roger Wicker [R]', party='Republican', state='MS')\
Senator(name='Sen. John Boozman [R]', party='Republican', state='AR')\
Senator(name='Sen. Claire McCaskill [D]', party='Democrat', state='MO')\
Senator(name='Sen. David Vitter [R]', party='Republican', state='LA')\
Senator(name='Sen. Barbara Mikulski [D]', party='Democrat', state='MD')\
Senator(name='Sen. Patrick “Pat” Toomey [R]', party='Republican', state='PA')\
Senator(name='Sen. Ron Johnson [R]', party='Republican', state='WI')\
Senator(name='Sen. Daniel Coats [R]', party='Republican', state='IN')\
Senator(name='Sen. John McCain [R]', party='Republican', state='AZ')\
Senator(name='Sen. Bob Corker [R]', party='Republican', state='TN')\
Senator(name='Sen. Heidi Heitkamp [D]', party='Democrat', state='ND')\
Senator(name='Sen. Timothy Kaine [D]', party='Democrat', state='VA')\
-------------- CLUSTER 2 --------------\
...\
-------------- CLUSTER 3 --------------\
...

## Insights
We can observe that senates from different parties also have similar interests in certain bills other than members belonging to the same party. 

###### Tribute Raymond Hettinger
