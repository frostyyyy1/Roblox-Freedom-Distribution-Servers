<h2 align="center">
  <img src="https://github.com/Windows81/Roblox-Freedom-Distribution/blob/main/Assets/Logo.png" height="20px"/>
  <a href="https://github.com/Windows81/Roblox-Freedom-Distribution">
    Roblox-Freedom-Distribution
  </a>
  Server List.
  <img src="https://github.com/Windows81/Roblox-Freedom-Distribution/blob/main/Assets/Logo.png" height="20px"/>
</h2>

<!-- STATUS-START -->
## Status Test
Last check: 2026-02-02 00:02:36 UTC

### Online
- 172.88.194.43:2005

### Offline / Unreachable
- 79.208.64.176:80 | RCC Services 55000,55001,55002 | Notes: this is a note
- 79.208.64.177:2005
- frostdev.cloud:2005
<!-- STATUS-END -->

## What is this?

This repository contains a community-maintained list of public Roblox Freedom Distribution servers.
All listed servers are checked automatically for availability and must follow the rules below.

## How to Join

1. Choose an **online server** from the list above
2. Download the [RFD client](https://github.com/Windows81/Roblox-Freedom-Distribution/releases/latest)
3. Run one of the commands below, replacing the values as needed

---

### Standard Join (single RCC service)

Use this if the server has **one RCC service** or does not specify a separate RCC port.

```bash
./RFD.exe player -h IPADDRESSHERE -p PORTHERE -u yourusername
./RFD.exe player -h IPADDRESSHERE:PORTHERE -u yourusername
```

### Join a Server with Multiple RCC Services

Some servers run **multiple RCC services** behind a single web server.  
In this setup, you must choose which RCC service to connect to by specifying its port.

Use the `--rcc_port`, `--port`, `-rp` flag to select the desired RCC service:

```bash
./RFD.exe player -h IPADDRESSHERE -p PORTHERE -rp RCCPORTHERE -u yourusername
./RFD.exe player -h IPADDRESSHERE:PORTHERE -rp RCCPORTHERE -u yourusername
```

## Adding a Server

To add a server to this list, please open an issue with the following information:

- Server address (IP or domain)
- Server port
- RCC service ports (if applicable)
- Any additional notes

Once submitted, the server will be checked and added to the list.

  
## More Information

For detailed documentation, usage examples, and technical information about Roblox Freedom Distribution,  
see the official project README:
https://github.com/Windows81/Roblox-Freedom-Distribution
