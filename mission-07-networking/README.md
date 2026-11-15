# Mission 07 - How computers communicate

Status: Completed.

## 1. Task / objective

Explain basic network concepts, check connectivity and DNS for a public example website, and describe how a browser opens a website.

## 2. Work completed

Codex ran the commands in my Mac's zsh environment. The starting state was a clean working tree on `main`, with Mission 6 commit `b4c37d825075cf97c06784bb488f05f6c7c07628` present and the correct GitHub remote.

Task 7.1 and the website steps in Task 7.3 explain concepts. Task 7.2 records the actual network tests.

### Task 7.1 - Explain network concepts

| Concept | Explanation | Example |
| --- | --- | --- |
| LAN | A network covering a small area, such as a home or computer lab. | Computers connected within one lab. |
| MAN | A network connecting locations across a city. | A city network linking municipal offices. |
| WAN | A network connecting devices or networks over large distances. | The Internet connects networks across countries. |
| DNS | Helps find IP addresses for a domain name. | Looking up `example.com`. |
| Router | Connects networks and forwards packets between them. | A home router forwards traffic towards the Internet. |
| Protocol | A set of rules for communication. | HTTPS carries protected web requests and responses. |
| Packet switching | Data is divided into packets that travel through a network and are put back together at the destination. | A web page's data travels in packets. |
| Client-server | A client requests a service, and a server provides a response. | A browser requests a page from a web server. |

A computer network lets devices exchange data and share resources. The examples above illustrate the concepts; they are not claims that each type of network was tested.

### Task 7.2 - Observe network information

The public example domain used for both checks was `example.com`.

| Command | Purpose | Actual result |
| --- | --- | --- |
| `ping -c 4 example.com` | Sends four ICMP echo requests to check whether the target replies. | 4 packets transmitted, 4 received, 0.0% loss. Average round-trip time: 5.759 ms. Exit status: 0. |
| `nslookup example.com` | Asks DNS for addresses associated with the domain. | Returned `104.20.23.154` and `172.66.147.243`. Exit status: 0. |

Actual ping summary:

```text
--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 4.367/5.759/6.571/0.876 ms
```

Actual DNS output, with resolver details redacted:

```text
Server: [DNS resolver redacted]
Address: [DNS resolver address redacted]

Non-authoritative answer:
Name:   example.com
Address: 104.20.23.154
Name:   example.com
Address: 172.66.147.243
```

The DNS output above uses spaces in place of alignment tabs. The transcript preserves the original alignment. The two visible IP addresses belong to the public example website; they are not my computer's addresses.

**What does the connectivity test check?** Ping checks whether the target responds to ICMP echo requests. Four replies showed that the selected host was reachable by this method during the test. This does not test loading the website over HTTPS. A failed ping would not by itself prove that a website is offline, because echo requests or replies may be blocked.

**What does a DNS lookup display?** It can show the resolver used and the addresses returned for the queried name. This lookup returned two addresses. The resolver details are redacted. A non-authoritative answer comes from a resolver that is not the domain's authoritative DNS server.

**What does DNS do when a website name is entered?** DNS helps the browser find an IP address associated with the domain so it can contact a server. A domain name such as `example.com` is a readable name; an IP address is a numerical network address. One domain can have several addresses, and answers can change with time or location.

### Task 7.3 - What happens when you open a website?

1. A website address is entered in the browser. The browser acts as the **client**.
2. The browser or operating system checks cached DNS information or asks a **DNS** resolver for the domain's IP addresses.
3. The client contacts a **server** using an address. Packets travel through the network, and a **router** forwards them between networks. For an HTTPS website, a secure connection is established.
4. The browser sends a request using the HTTP **protocol**. HTTPS protects this communication using TLS encryption.
5. The server processes the request and prepares a response, such as the page's HTML.
6. The response travels back through the network in packets and is reassembled on the client's computer.
7. The browser reads the response, requests other needed resources such as images, and displays the page.

These steps explain the usual process. The experiment checked ping replies and DNS answers; it did not inspect browser requests, TLS or the route taken by packets.

## 3. Commands / tools used

- `ping -c 4 example.com`: checked four echo requests and recorded replies and timing.
- `nslookup example.com`: looked up the example domain's addresses.
- `command -v ping`, `command -v nslookup`: confirmed that the macOS tools were available.
- `pwd`, `git status`, `git branch`, `git log --oneline -5`, `git remote -v`: checked the project and its clean starting state. Private paths were not copied into public evidence.
- Swift, PDFKit and Vision: read the complete Mission 7 instructions from PDF page 9 using OCR.
- Python helper and zsh: ran the checks, captured actual outputs and redacted resolver details.

## 4. My understanding

I learned that a network lets devices exchange data. A domain name is easier to remember than an IP address, and DNS helps find the address needed to contact a server. The ping results showed that the target replied during the test, while the DNS lookup returned two public addresses. When a website opens, the browser acts as a client and exchanges requests and responses with a server using a protocol.

## 5. Difficulties faced

No personal difficulties. Both network commands completed successfully, with no error output.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- [Network command transcript](evidence/network-session.txt): commands, actual outputs, exit statuses and redactions.
- [This README](README.md): network table, test results and seven website steps.

DNS resolver details were redacted before saving. No interface listing, Wi-Fi name, MAC address, credentials or personal public-IP lookup was collected. No screenshots were required or created.

## 8. Evidence / links

- [Project overview](../README.md).
- [Actual network evidence](evidence/network-session.txt).
- [Mission 7 commit history](https://github.com/aryangetsreal/digital-detective-8427/commits/main/mission-07-networking/README.md).

## 9. Commit details

- Commit message: `Complete networking mission`.
- Scope: approved Mission 7 files and approved root README status and progress corrections.
- Branch: `main`.
- Commit hash: `df0b6caaef6c907c58a349254153f7b31c750f63`.
- Push status: Verified on GitHub `main`; the published commit and files were checked during the final review.
- [Published commit](https://github.com/aryangetsreal/digital-detective-8427/commit/df0b6caaef6c907c58a349254153f7b31c750f63).

Verification checks the published README and evidence, public visibility, matching local and remote commits, and a clean working tree before reporting success.
