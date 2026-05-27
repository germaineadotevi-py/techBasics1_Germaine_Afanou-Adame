### Assignment 7
Add a record-saving system to one of the games you have created so far.

Your record-saving system shall save the following information:
- Name
- A timestamp
- The score achieved / time used (depending on your scenario)

At the end of the game, you shall display a simple leader board based on previous records:
- If no existing data is found, create a new record file with the current result
- If a record file already exists, load the data and add the current result to the corresponding location
- Include try/except blocks into your code to practice error handling
- Add a debugging flag to your submitted game and set it to `DEBUG = True`. This shall skip the main body of the game and only allow you to enter your name. In this case, a placeholder score/time will be saved just for testing purpose.

You may choose whether to export the data as a TXT or Excel file or which method to read/write to files.


