REQUIREMENTS
============
1.  Python 2.7
2.  Selenium Webbdriver
3.  Java SDK
4.  Mozilla Firefox (tested on version 35.0)


INSTALLATIONS
=============

Python
——————
1.  Python is preinstalled on mac, to verify enter this on the terminal:
	$ python
2.  If you don’t have python you can download Python on:
	https://www.python.org/downloads/

Selenium Webdriver
——————————————————

1.  Make sure you have pip, if not:
	i.  	Goto, https://bootstrap.pypa.io/get-pip.py
	ii. 	SELECT ALL, COPY & PASTE and SAVE into a python file <get-pip.py>
	iii.	On the Terminal cd to directory where you saved <get-pip.py> and enter:
		$ python get-pip.py

2.  Install selenium using pip by entering this on the terminal:
	$ pip install selenium

3.  You may need admin privalages, if so enter this on the terminal:
	$ sudo pip install -U selenium


Java SDK
————————

1.  You can download Java SDK at:
	http://www/oracle.com/technetwork/java/javase/downloads

2.  Follow the instructions to install



RUNNING THE SELENIUM SCRIPTS
============================

1.  [first time only] On the git shell:
	git clone <https://github.com/izzie1349/Athlete-test-scripts.git>

2.  On the terminal, cd to the directory where <tests.py> is located, and enter:
	$ python tests.py > TestReport.html

3.  After the tests run, there will be a <TestReport.html> file to view pass/fail






