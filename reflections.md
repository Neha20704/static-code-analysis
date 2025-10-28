1) which issues were the easiest to fix and which were the hardest? why?
A) the easiest to fix are the style related warnings which were given in the flake8 and pylint files like missing blank lines as they just needed small formatting changes. the toughest to change were the security related ones given in the bandit files- like the eval() and the bare except clause since these required understanding the underlying risk and we had to rewrite the code logic.

2) did the static analysis tools report any false positives? if so, describe one example
A) yes, pylint's warning about "import outside top level" (C0415) was a false positive, the import was moved into a function on purpose to avoid loading an optional dependency globally. 

3) how would you integrate static analysis tools into your actual software development workflow?
A) integrating these tools into a continuous integration pipeline is the best approach so that every push or pull request will trigger automated checks. 

4) what tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
A) after the fixes, code became:
    1) more secure- removal of eval() and proper execution handling reduced risks
    2) more maintainable- following PEP8 spacing and naming conventions made it easier to read
    3) more stable- replacing bare except with specific exception- KeyError prevents unintended error suppression

overall the code clarity improved and the pylint score increased from 4.8 to 5.88 which shows improvement for just the 4 changes i made. 

as mentioned in the instructions about the 2 extra marks, i have fixed all the errors as mentioned by the analysis tools. 

pylint_report2 is the final pylint report with a score of 10.00/10. it has improved from 4.8 to 5.88 after i fixed 4 errors- which is for the lab assignment. 5.88 to 10 improvement after i fixed all the errors.

flake8 report2 is the final flake8 report, which has nothing in it since everything has been fixed. 

bandit_report2 is the final bandit report which reports 0 issues in the code. 

