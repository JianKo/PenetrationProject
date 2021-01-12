# Machine IP : 10.10.19.165
# Machine Name : Vulnversity

***TASK1 : Deploy the machine***

***TASK2 : Reconnaissance<br>***
```
 1. {No answer}
 2. {6} 
 3. {3.5.12}
 4. {400} 
 5. {DNS} 
 6. {Ubuntu}
 7. {3333} 
 8. {No answer}
```
***TASK3 : Locating Directories using GoBuster***<br>
 ```
 1. {No answer}
 2. {/internal/}
     &nbsp; Reference : gobusterResult.md 
```

***TASK4 : Compromise the webserver***<br>
```
 1. Try upload a few file types to the server, what common extension seems to be blocked? {.php}

 2. To identify which extensions are not blocked, we're going to fuzz the upload form. To do this, we're doing to use BurpSuite. If you are unsure to what BurpSuite is, or how to set it up please complete our BurpSuite room first. {No answer}

3. We're going to use Intruder (used for automating customised attacks). To begin, make a wordlist with the following extensions in: {.phtml}

4. Now we know what extension we can use for our payload we can progress.<br>
  {No answer}<br>

5. What user was running the web server? {bill} 

6. What is the user flag? <br>
  {8bd7992fbe8a6ad22a63361004cfcedb}

  ***TASK5:Privilege Escalation***

  1. On the system, search for all SUID files. What file stands out?<br> /bin/systemctl
    Privilege Escalte Reference File : PriVilegeList.md

  2. Become root and get the last flag (/root/root.txt)
```