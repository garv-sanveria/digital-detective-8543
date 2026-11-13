# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 was to explore basic computer networking concepts and architectures, observe real-world network connectivity and DNS resolution using terminal tools, and describe the step-by-step process of what happens when a user opens a website in a browser.

## 2. Work completed
- Defined and gave everyday examples for eight fundamental networking terms (LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, Client-server).
- Ran connectivity tests using `ping` and inspected latency and packet delivery.
- Conducted DNS lookups using `nslookup` to observe domain-to-IP resolution.
- Answered questions regarding connectivity diagnostics, DNS data, and name resolution.
- Detailed the 7-step journey of an HTTP/HTTPS web request from browser input to final rendered webpage.

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested network connectivity, latency, and packet loss.
- `nslookup example.com`: Queried DNS servers to resolve domain names to IP addresses.

## 4. My understanding

### Task 7.1 — Explain network concepts

| Concept | Explain in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A network connecting computers and devices within a limited physical area such as a single home, school lab, or office. | A home Wi-Fi network connecting a laptop, phone, smart TV, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A larger network that covers an entire town, city, or university campus, bridging multiple LANs together. | A city municipal fiber-optic network connecting government offices, police stations, and public libraries. |
| **WAN (Wide Area Network)** | A telecommunication network spanning huge geographical regions across states, nations, or continents. | The global Internet connecting millions of private, corporate, and educational networks worldwide. |
| **DNS (Domain Name System)** | The internet's distributed lookup phonebook that translates human-friendly domain names into machine-readable IP addresses. | Translating `example.com` into `172.66.147.243`. |
| **Router** | A specialized networking device that forwards data packets between different networks and directs them along the fastest route. | A home Wi-Fi broadband router connecting local home devices to the Internet Service Provider's (ISP) network. |
| **Protocol** | An established set of standard rules and conventions that govern how devices format, transmit, and receive data. | HTTPS (Hypertext Transfer Protocol Secure) for encrypted web traffic, or TCP/IP for addressing and reliable packet delivery. |
| **Packet switching** | The networking technique where large messages are split into small, numbered packets, routed independently over the best available paths, and reassembled at the destination. | How web pages, audio streams, and email messages travel in fragmented chunks across routers on the internet. |
| **Client-server** | A system architecture where client devices request services, data, or files, and dedicated server computers process the requests and return answers. | A web browser (client) requesting an assignment webpage from a GitHub web server. |

---

### Task 7.2 — Observe network information

#### 1. Connectivity Test Output (`ping -c 3 8.8.8.8`):
```text
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: icmp_seq=0 ttl=115 time=34.153 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=14.603 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=115 time=13.677 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 13.677/20.811/34.153/9.442 ms
```

#### 2. DNS Lookup Output (`nslookup example.com`):
```text
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	example.com
Address: 172.66.147.243
Name:	example.com
Address: 104.20.23.154
```

#### Observations and Questions:
- **What a connectivity test helps you check:**
  It confirms whether a remote server is reachable over the network, detects any packet loss (dropped packets indicate network congestion or firewall blocking), and measures round-trip time (latency in milliseconds).
- **What information a DNS lookup displays:**
  It shows the DNS resolver server used, the domain queried, and the IP addresses (IPv4 or IPv6) mapped to that domain.
- **The role of DNS when you enter a website name in a browser:**
  Network routers cannot find web servers by text names like `example.com`; they only understand numeric IP addresses. DNS acts as the essential translation service that converts the text address into an IP address so the browser knows where to route its connection requests.

---

### Task 7.3 — What happens when you open a website?
Here is the step-by-step sequence of what occurs when opening a website:
1. **Entering the URL:** The user types `https://example.com` into the browser and presses Enter.
2. **DNS Resolution:** The browser checks its local cache. If not cached, it queries a DNS resolver to look up the IP address mapped to `example.com` (e.g., `172.66.147.243`).
3. **Establishing Connection (TCP Handshake):** The client initiates a TCP 3-way handshake (SYN, SYN-ACK, ACK) with the web server on port 443, followed by a TLS handshake to establish secure end-to-end encryption.
4. **Sending HTTP GET Request:** The browser sends an encrypted HTTP GET request asking the web server for the index page.
5. **Routing Across the Network:** The local router breaks the request into IP packets and routes them across intermediate ISP routers across the internet to the destination server.
6. **Server Response:** The web server receives and processes the request, locates the web assets, and transmits an HTTP response (with status code `200 OK`) containing the HTML, CSS, images, and JavaScript payloads.
7. **Browser Rendering:** The browser receives and reassembles the response packets, parses the HTML DOM tree and stylesheets, runs scripts, and renders the webpage on the user's screen.

## 5. Difficulties faced
Understanding why `nslookup` sometimes outputs multiple IP addresses for a single domain name.

## 6. How I resolved them
I learned that high-traffic websites use multiple IP addresses for DNS round-robin load balancing and content delivery networks (CDNs) so requests are distributed efficiently across multiple servers.

## 7. Evidence / files
- `mission-07-networking/README.md` (this file)

## 8. Commit details
- Branch: `main`
- Commit message: `Explain networking concepts and website communication`
