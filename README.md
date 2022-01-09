# Google Python Class Exercise Solutions 
## Regular expressions
### Basic Patterns
The power of regular expressions is that they can specify patterns, not just fixed characters. Here are the most basic patterns which match single chars:

1. a, X, 9, < -- ordinary characters just match themselves exactly. The meta-characters which do not match themselves because they have special meanings are: . ^ $ * + ? { [ ] \ | ( ) (details below)
2. . (a period) -- matches any single character except newline '\n' 
3. \w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches any non-word character. 
4. \b -- boundary between word and non-word 
5. \s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]. \S (upper case S) matches any non-whitespace character. 
6. \t, \n, \r -- tab, newline, return 
7. \d -- decimal digit [0-9] (some older regex utilities do not support \d, but they all support \w and \s)
8. ^ = start, $ = end -- match the start or end of the string 
9. \ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash. If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, \@, to make sure it is treated just as a character.
