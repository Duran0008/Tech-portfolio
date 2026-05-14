# HTTP in Detail

**Platform:** TryHackMe  
**Difficulty:** Easy  
**Date Completed:** April 25, 2026  
**Badge Earned:** Webbed

---

## Overview
This room covers how HTTP works as the foundation of web communication. It goes through requests and responses, HTTP methods, status codes, and headers — all essential knowledge for any security role dealing with web traffic.

---

## Key Concepts Covered
- HTTP request and response structure
- HTTP methods: GET, POST, PUT, DELETE
- Status codes and what they mean
- URL structure and parameters
- HTTP headers and cookies

---

## Tasks & Findings

### Task 1–6 – Theory
Covered how HTTP works, the structure of requests and responses, common status codes (200, 301, 403, 404, 500), and how headers pass extra information between client and server.

### Task 7 – Making Requests
Used the built-in HTTP request emulator to make real requests against a demo site:

- GET /room → THM{YOU'RE_IN_THE_ROOM}
- GET /blog?id=1 → THM{YOU_FOUND_THE_BLOG}
- DELETE /user/1 → THM{USER_IS_DELETED}
- PUT /user/2 (username: admin) → THM{USER_HAS_UPDATED}
- POST /login (username: thm, password: letmein) → THM{HTTP_REQUEST_MASTER}


<img width="1312" height="826" alt="image" src="https://github.com/user-attachments/assets/a07a342f-0fac-4614-a631-ebf06265ee54" />


---

## What I Learned
HTTP methods aren't just for browsing — GET, POST, PUT and DELETE map directly to reading, creating, updating and deleting data on a server. Understanding this is important in security because attackers exploit poorly secured endpoints using exactly these methods. Status codes also help identify what's happening on a server during recon.

---

## Reflection
Knowing how HTTP works at this level is essential for web app security testing and SOC work, both of which are core to the apprenticeship roles I'm targeting.

---

**Badge:**  

<img width="729" height="536" alt="image" src="https://github.com/user-attachments/assets/660d12ab-173e-4868-a8a7-10f71df23cde" />

