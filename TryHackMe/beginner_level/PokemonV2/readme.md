# PokeMon V2
```
export ip = ""
```

## SCAN
```
80 http
```

## Enumeration
```
1. http://{Export_IP}/ <-- View Page Source
2. SSH Credential --> pokemon:hack_the_pokemon
```

## Walk Throught
```
1. Find the Grass-Type Pokemon
PoKeMoN{Bulbasaur} <-- /home/pokemon

2. Find the Water-Type Pokemon
Squirtle_SqUaD{Squirtle} <-- /var/www/html

3. Find the Fire-Type Pokemon
P0k3m0n{Charmander} <-- find / -perm -4000 2>/dev/null

4. Who is Root's Favorite Pokemon?
Pikachu! <-- /Videos/~ <-- root creds (ash:pikapika)
```