# DNS in Detail

**Platform:** TryHackMe  
**Difficulty:** Easy  
**Category:** Networking / Fundamentals

## Overview
This room covered how DNS works — how domain names get translated into IP addresses, 
the different record types, and how the resolution process works step by step.

## Commands Used
nslookup website.thm
nslookup --type=TXT website.thm
nslookup --type=MX website.thm
nslookup --type=CNAME shop.website.thm

## DNS Record Types

**A Record** — Maps a domain to an IPv4 address.  
**AAAA Record** — Maps a domain to an IPv6 address.  
**CNAME Record** — Alias pointing to another domain (e.g. shop.website.thm → shops.myshopify.com).  
**MX Record** — Points to mail servers. Has a priority value — lower number = higher priority.  
**TXT Record** — Free-text field. Used for SPF/DMARC records to prevent email spoofing.

## Practical Task
Used the in-browser terminal to query DNS records against a simulated DNS server. 
Queried TXT records using nslookup --type=TXT and retrieved the flag. 
Also identified the CNAME for shop.website.thm, MX priority value, and A record for www.website.thm.

<img width="1919" height="943" alt="dns-practical" src="https://github.com/user-attachments/assets/c26b62b2-de55-430c-a0aa-0715799c07a3" />


## What I Learned
DNS record types matter beyond just browsing — during reconnaissance, querying MX and TXT 
records can reveal mail providers, SPF configurations, and third-party services a target uses. 
TXT records in particular are worth checking early in any investigation.

Save your screenshot into a screenshots/ folder in the same directory and name it dns-practical.png so the image link works.Sonnet 4.6

