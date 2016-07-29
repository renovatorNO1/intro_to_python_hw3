Chapter5 Exercise6:
open the exercise6.py in your python compiler.
Explanations for different parts of codes from top to bottom:
1. Create the directory if it does not exist
2. Create thisFile.txt and write some lines into it for transcription later
3. open thisFile in reading mode
4. Create thatFile in writing mode
5. Define funtion write_every_other_line to perform the transcription. keep track of the line number
   storing them it into the variable count_of_line. Only when the line number is odd, nameyly the count_of_line is     odd, the transcription gets executed.
6. Call the funtion write_every_other_line
7. Close both files.

Project2.py
Open project2,py in your python compiler.
Explanations for different parts of the codes from top to bottom:
1. Define find() function
   (a) slice the some_string into string_range by taking the starting element up till the ending element(inclusive)
   (b) initialize local variable counter inside the loop so it can be used to determine the whether we should
       break out from the loop later.
   (c) check if the index of the last element exceeds the index range of string_range
   (d) compare elements of the string_range to the elements of the substring. If every element
       matches up, then return the lowest index, thus breaking the nested loops.
   (e) If some elemen does mathc up, then break from the current loop and test on the next i
2. Define multifind() function:
   The main structure is similar to find(). The only difference is I store all the found indices into
   the list named "index_list". When the iteration on elements is finished, the index_list will be printed
   in a designed format. 
3. The main function is used to test the functionality of the find() and multifind() functions.