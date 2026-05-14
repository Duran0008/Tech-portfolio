# Junior Security Analyst Intro

**Platform:** TryHackMe  
**Difficulty:** Easy  
**Date Completed:** May 14, 2026

---

## Overview
This room simulates what a Junior Security Analyst actually does day-to-day. It puts you inside a SOC environment, working with a SIEM dashboard to triage alerts, investigate suspicious activity, escalate incidents, and block threats — all the core tasks of a Tier 1 analyst.

---

## Key Concepts Covered
- SIEM dashboard navigation and alert triage
- Identifying and prioritising alerts by severity (Critical, Medium, Low)
- Investigating suspicious IP addresses
- Escalating incidents to senior analysts
- Blocking malicious IPs via a firewall

---

## Tasks & Findings

### Practical Lab – A Day in the Life of a Junior Security Analyst
Worked through a simulated SOC environment at security.tryhackme.com. The SIEM dashboard showed live alerts across four categories: Malware (20%), Phishing (30%), Intrusion (35%), Anomaly (15%).

Key findings:
- Identified malicious IP **221.181.185.159** from two critical alerts — a successful SSH login and repeated unauthorised login attempts to port 22
- Escalated the incident to **Will Griffin**
- Blocked the IP on the firewall → `THM{until-we-meet-again}`

<img width="1877" height="984" alt="image" src="https://github.com/user-attachments/assets/8646fe1a-7e91-439b-a5cd-2f84e849518e" />

---

## What I Learned
Triaging alerts isn't just about spotting the red ones — it's about understanding context. Two critical alerts from the same IP told a clearer story than either one alone. Escalation is also a key part of the job; knowing when something is above your pay grade and flagging it properly is just as important as the technical investigation.

---

## Reflection
This room is directly relevant to the apprenticeship roles I'm targeting. Working through a real SOC workflow — even in a simulation — gave me a clearer picture of what Tier 1 analyst work actually looks like day to day.
