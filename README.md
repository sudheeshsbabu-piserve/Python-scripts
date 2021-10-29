<h1>Python</h1>
<h2>Create windows services using python scripts</h2>

References:
1. https://youtu.be/fKwPQ-dQ58g?list=PLf7vZM95Oxnd8tq45lv-4MQkLQlWbr1ng
2. http://thepythoncorner.com/dev/how-to-create-a-windows-service-in-python/
3. https://gist.github.com/guillaumevincent/d8d94a0a44a7ec13def7f96bfb713d3f

Add python installation path in the SYSTEM PATH section(bottom section) of environment variables. Adding it on the USER PATH (top section) will not work for services.

Python to EXE
1. Using auto py to exe<br>
    Installation command: pip install auto-py-to-exe<br>
    Command: auto-py-to-exe<br>
    This will open up the wizard and the GUI is self explanatory.<br>
2. Using Pyinstaller<br>
    Installation command: pip install pyinstaller<br>
    Command: pyinstaller file.py<br>
    In the case of windows services, make sure to add win32timezone in the hiddenimports[] of file.spec to avoid the common win32timezone not found issue.<br>
    Eg: hiddenimports=['win32timezone'],<br>

Packages installation command
  pip install package_name

Requried packages
  1. pywin32
  2. pyinstaller


Windows service<br>
  Note: run cmd as administrator<br>
  Execution: <br>
    1. To install and/or update the service code<br>
          python script.py install<br>
    2. To start the service<br>
        python script.py start<br>
    3. To debug the service<br>
        python script.py debug<br>
    4. To remove/delete the service from the services list. Alternate command: SC DELETE serviceid<br>
        python script.py remove<br>

Command to delete service
  1. SC DELETE TestService
  2. python script.py remove



